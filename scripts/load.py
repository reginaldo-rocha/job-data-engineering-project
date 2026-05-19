import pandas as pd
import sqlite3

df = pd.read_csv("data/processed/jobs.csv")

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Criar tabelas
with open("sql/create_tables.sql") as f:
    cursor.executescript(f.read())

# DIMENSÕES
companies = df["company"].drop_duplicates().reset_index(drop=True)
locations = df["location"].drop_duplicates().reset_index(drop=True)
jobs_dim = df[["id", "title"]].drop_duplicates()

# 🔥 corrigir nome da coluna
jobs_dim.rename(columns={"id": "job_id"}, inplace=True)

companies_df = pd.DataFrame({"name": companies})
locations_df = pd.DataFrame({"city": locations})

companies_df.to_sql("dim_company", conn, if_exists="append", index=False)
locations_df.to_sql("dim_location", conn, if_exists="append", index=False)
jobs_dim.to_sql("dim_job", conn, if_exists="append", index=False)

# MAPEAMENTO
company_map = pd.read_sql("SELECT * FROM dim_company", conn)
location_map = pd.read_sql("SELECT * FROM dim_location", conn)

df = df.merge(company_map, left_on="company", right_on="name")
df = df.merge(location_map, left_on="location", right_on="city")

# FACT
fact = df[["id", "company_id", "location_id", "salary_min", "salary_max"]]
fact.rename(columns={"id": "job_id"}, inplace=True)

fact.to_sql("fact_jobs", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Data Warehouse criado com sucesso!")