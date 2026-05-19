import json
import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

try:
    with open("data/raw/jobs.json") as f:
        data = json.load(f)

    jobs = data.get("results", [])

    if not jobs:
        raise Exception("API retornou vazio")

    df = pd.DataFrame(jobs)

    def get_company(x):
        try:
            return x["display_name"]
        except:
            return None

    def get_location(x):
        try:
            return x["display_name"]
        except:
            return None

    df["company"] = df["company"].apply(get_company)
    df["location"] = df["location"].apply(get_location)

    df = df[[
        "id",
        "title",
        "company",
        "location",
        "salary_min",
        "salary_max"
    ]]

    print("✅ Usando dados da API")

except:
    print("⚠️ API vazia — usando fallback")

    df = pd.DataFrame([
        [1, "Data Analyst", "Google", "São Paulo", 5000, 8000],
        [2, "Data Engineer", "Amazon", "Rio de Janeiro", 7000, 12000],
        [3, "Data Scientist", "Microsoft", "Belo Horizonte", 9000, 15000]
    ], columns=["id","title","company","location","salary_min","salary_max"])

df.dropna(inplace=True)
df.to_csv("data/processed/jobs.csv", index=False)

print("Transform concluído!")