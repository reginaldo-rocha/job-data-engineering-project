SELECT 
    d.title,
    c.name AS company,
    l.city,
    f.salary_min,
    f.salary_max
FROM fact_jobs f
JOIN dim_job d ON f.job_id = d.job_id
JOIN dim_company c ON f.company_id = c.company_id
JOIN dim_location l ON f.location_id = l.location_id;