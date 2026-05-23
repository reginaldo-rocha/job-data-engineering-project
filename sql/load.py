from sqlalchemy import create_engine

def load_data(df):

    user = "postgres"
    password = "postgres123"
    host = "localhost"
    port = "5432"
    database = "etl_project"

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )

    df.to_sql(
        "jobs_data",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Dados carregados no PostgreSQL!")