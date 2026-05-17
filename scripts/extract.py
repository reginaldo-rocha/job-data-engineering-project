import requests
import json

APP_ID = "3554ad36"
APP_KEY = "bae8d28b9da25044a9dfc4f030d6ddce"

url = "https://api.adzuna.com/v1/api/jobs/br/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY
}

response = requests.get(url, params=params)
data = response.json()

with open("data/raw_jobs.json", "w") as f:
    json.dump(data, f)

print("Dados extraídos com sucesso!")