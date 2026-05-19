CREATE TABLE dim_company (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE dim_location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT
);

CREATE TABLE dim_job (
    job_id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE fact_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER,
    company_id INTEGER,
    location_id INTEGER,
    salary_min REAL,
    salary_max REAL
);