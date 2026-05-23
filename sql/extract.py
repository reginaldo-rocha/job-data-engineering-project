import requests
import pandas as pd

def extract_data():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print(f"Status: {response.status_code}")

    data = response.json()

    jobs = []

    for item in data:

        if isinstance(item, dict):

            if item.get("position"):

                jobs.append({
                    "job_title": item.get("position"),
                    "company": item.get("company"),
                    "location": item.get("location"),
                    "salary": str(item.get("salary"))
                })

    df = pd.DataFrame(jobs)

    print(f"{len(df)} vagas encontradas!")

    return df