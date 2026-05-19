# 🚀 Job Data Engineering Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SQL](https://img.shields.io/badge/SQL-Analytics-green)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange)

---

# 📌 Project Evolution

## 🥇 Version 1
API + SQL (base técnica)

## 🥈 Version 2
Data Warehouse + Star Schema

## 🥉 Version 3
Automation + Historical Pipeline

## 🏆 Version 4
AWS + Docker + Airflow

---

# 📌 Overview

This project simulates a real-world Data Engineering pipeline using Python and SQL.

The pipeline extracts job market data from a public API, transforms the data, stores it in a dimensional Data Warehouse model, and generates analytical insights.

---

# 🏗️ Architecture

![Architecture](assets/architecture.png)

---

# ⚙️ Technologies

- Python
- Pandas
- SQL
- SQLite
- Requests
- Matplotlib

---

# 📂 Project Structure

![Structure](assets/project_structure.png)

---

# 🔄 Pipeline Flow

```text
API → RAW → TRANSFORM → DATA WAREHOUSE → SQL ANALYTICS
```

---

# 🧱 Data Warehouse Model

### Fact Table
- fact_jobs

### Dimension Tables
- dim_company
- dim_location
- dim_job

---

# 📊 SQL Analytics

```sql
SELECT d.title, AVG(f.salary_min) as avg_salary
FROM fact_jobs f
JOIN dim_job d ON f.job_id = d.job_id
GROUP BY d.title;
```

---

# 🖼️ Query Example

![Query Result](assets/query_result.png)

---

# 📈 Salary Analysis

![Salary Chart](assets/salary_chart.png)

---

# 💾 Database Example

![Database](assets/database.png)

---

# 🚀 Features

✔️ ETL Pipeline  
✔️ API Data Extraction  
✔️ Data Transformation  
✔️ Data Warehouse Modeling  
✔️ SQL Analytics  
✔️ Data Visualization  

---

# ▶️ Run Project

```bash
python main.py
```

---

# 📌 Future Improvements

- Pipeline automation
- Historical data tracking
- Docker
- Apache Airflow
- AWS Cloud

---

# 👨‍💻 Author

Reginaldo Rocha