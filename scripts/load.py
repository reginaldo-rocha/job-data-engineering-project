import pandas as pd
import sqlite3
import os
import logging
from datetime import datetime

# =========================
# CONFIGURAR LOGS
# =========================

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# LER CSV PROCESSADO
# =========================

df = pd.read_csv("data/processed/jobs.csv")

# =========================
# CONECTAR BANCO
# =========================

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# =========================
# LOCALIZAR SQL AUTOMATICAMENTE
# =========================

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sql_path = os.path.join(base_dir, "sql", "create_tables.sql")

# =========================
# CRIAR TABELAS
# =========================

with open(sql_path, "r") as f:
    cursor.executescript(f.read())

conn.commit()

# =========================
# LIMPAR TABELAS
# =========================

cursor.execute("DELETE FROM fact_jobs")
cursor.execute("DELETE FROM dim_company")
cursor.execute("DELETE FROM dim_location")
cursor.execute("DELETE FROM dim_job")

conn.commit()

# =========================
# CRIAR DIMENSÕES
# =========================

companies = df["company"].drop_duplicates().reset_index(drop=True)

locations = df["location"].drop_duplicates().reset_index(drop=True)

jobs_dim = df[["id", "title"]].drop_duplicates()

# Renomear coluna id para job_id
jobs_dim.rename(columns={"id": "job_id"}, inplace=True)

# DataFrames dimensões
companies_df = pd.DataFrame({
    "company_name": companies
})

locations_df = pd.DataFrame({
    "city": locations
})

# =========================
# SALVAR DIMENSÕES
# =========================

companies_df.to_sql(
    "dim_company",
    conn,
    if_exists="append",
    index=False
)

locations_df.to_sql(
    "dim_location",
    conn,
    if_exists="append",
    index=False
)

jobs_dim.to_sql(
    "dim_job",
    conn,
    if_exists="append",
    index=False
)

# =========================
# MAPEAR IDS
# =========================

company_map = pd.read_sql(
    "SELECT * FROM dim_company",
    conn
)

location_map = pd.read_sql(
    "SELECT * FROM dim_location",
    conn
)

# Merge company
df = df.merge(
    company_map,
    left_on="company",
    right_on="company_name"
)

# Merge location
df = df.merge(
    location_map,
    left_on="location",
    right_on="city"
)

# =========================
# CRIAR TABELA FATO
# =========================

# Data da execução
execution_date = datetime.now().date()

# Selecionar colunas
fact = df[
    [
        "id",
        "company_id",
        "location_id",
        "salary_min",
        "salary_max"
    ]
]

# Renomear id para job_id
fact.rename(
    columns={"id": "job_id"},
    inplace=True
)

# Adicionar coluna histórica
fact["execution_date"] = execution_date

# =========================
# SALVAR FACT TABLE
# =========================

fact.to_sql(
    "fact_jobs",
    conn,
    if_exists="append",
    index=False
)

# =========================
# FINALIZAR
# =========================

conn.commit()
conn.close()

print("Data Warehouse histórico criado com sucesso!")

logging.info("Pipeline executado com sucesso!")