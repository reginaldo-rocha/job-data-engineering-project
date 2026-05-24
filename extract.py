import requests
import pandas as pd

def extract_data():
    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    jobs = []

    for item in data[1:]:
        jobs.append({
            "job_title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location"),
            "salary": item.get("salary")
        })

    df = pd.DataFrame(jobs)

    print("Dados extraidos!")

    return df
