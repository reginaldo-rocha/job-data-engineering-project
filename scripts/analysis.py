import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("jobs.db")

# Query
df = pd.read_sql_query("""
SELECT d.title, AVG(f.salary_min) as avg_salary
FROM fact_jobs f
JOIN dim_job d ON f.job_id = d.job_id
GROUP BY d.title
ORDER BY avg_salary DESC
LIMIT 10
""", conn)

# Plot
df.plot(kind='bar', x='title', y='avg_salary')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("assets/salary_chart.png")

print("Gráfico gerado!")