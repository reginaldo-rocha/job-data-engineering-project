CREATE TABLE IF NOT EXISTS dim_company (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT
);

CREATE TABLE IF NOT EXISTS dim_location (
    location_id INTEGER PRIMARY KEY,
    city TEXT
);

CREATE TABLE IF NOT EXISTS dim_job (
    job_id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE IF NOT EXISTS fact_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER,
    company_id INTEGER,
    location_id INTEGER,
    execution_date TEXT,
    salary_min REAL,
    salary_max REAL
);