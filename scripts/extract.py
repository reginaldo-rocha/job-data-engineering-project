import requests
import json
import os

APP_ID = "3554ad36"
APP_KEY = "bae8d28b9da25044a9dfc4f030d6ddce"

url = "https://api.adzuna.com/v1/api/jobs/br/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "data",
    "where": "brazil"
}

response = requests.get(url, params=params)

# 🔥 DEBUG PROFISSIONAL
print("Status:", response.status_code)

data = response.json()

# 🔥 VERIFICAÇÃO
if "results" not in data:
    print("ERRO NA API:")
    print(data)
    exit()

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/jobs.json", "w") as f:
    json.dump(data, f)

print("Dados válidos salvos!")