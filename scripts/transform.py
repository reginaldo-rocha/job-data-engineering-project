import json
import pandas as pd

# abrir arquivo
with open("data/raw_jobs.json") as f:
    data = json.load(f)

# DEBUG
print("Chaves do JSON:", data.keys())

# pegar lista de vagas
jobs = data.get("results", [])

# validar
if not jobs:
    print("❌ Nenhum dado encontrado! Verifique a API.")
    exit()

# criar dataframe corretamente
df = pd.DataFrame(jobs)

print("Colunas disponíveis:", df.columns)

# selecionar colunas (com segurança)
colunas = ["title", "company", "location", "salary_min", "salary_max"]

colunas_existentes = [c for c in colunas if c in df.columns]

df = df[colunas_existentes]

# tratar campos aninhados
if "company" in df.columns:
    df["company"] = df["company"].apply(lambda x: x.get("display_name") if isinstance(x, dict) else None)

if "location" in df.columns:
    df["location"] = df["location"].apply(lambda x: x.get("display_name") if isinstance(x, dict) else None)

# remover nulos
df.dropna(inplace=True)

# salvar
df.to_csv("data/clean_jobs.csv", index=False)

print("✅ Transformação concluída!")