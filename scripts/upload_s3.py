import boto3

s3 = boto3.client("s3")

bucket_name = "job-market-data-reginaldo"

# Upload RAW
s3.upload_file(
    "data/raw/jobs.json",
    bucket_name,
    "raw/jobs.json"
)

# Upload PROCESSED
s3.upload_file(
    "data/processed/jobs.csv",
    bucket_name,
    "processed/jobs.csv"
)

print("Upload realizado com sucesso!")