<<<<<<< HEAD
# 🚀 Job Data Engineering Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SQL](https://img.shields.io/badge/SQL-Analytics-green)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange)

---

# 📌 Project Evolution

## 🥇 Version 1
API + SQL (base técnica)

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/88f4813b-f108-4f22-b62a-3b38d1bde6fe" />


## 🥈 Version 2
Data Warehouse + Star Schema

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/9531f54e-ad7f-457c-b5d9-9d2058c9be58" />


## 🥉 Version 3
Automation 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/06bc2bab-1118-4f92-b62c-9b5376706be1" />


## 🏆 Version 4
Cloud na AWS + orquestração

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/70cf63f0-f5fa-4bd2-b449-c5abd7dfeda2" />


---

# 📌 Overview

Este projeto simula um fluxo de trabalho de Engenharia de Dados do mundo real usando Python e SQL.

O fluxo de trabalho extrai dados do mercado de trabalho a partir de uma API pública, transforma os dados, armazena-os em um modelo de Data Warehouse dimensional e gera insights analíticos.

=======
# 🚀 Job Market Insights  
### Pipeline de Dados com API Pública, Python e SQL-Projeto 0



Projeto de engenharia/análise de dados que consome uma API pública de vagas de emprego, realiza tratamento com Python e disponibiliza análises utilizando SQL.

---

## 🧠 Objetivo

Demonstrar na prática a construção de um pipeline de dados completo:

- Extração de dados via API
- Transformação e limpeza com Python
- Armazenamento em banco SQL
- Análise de dados com queries

---


---

## 🔄 Pipeline de Dados

1. **Extração**
   - Consumo da API de vagas (Adzuna)
   - Requisições HTTP com `requests`

2. **Transformação**
   - Limpeza de dados
   - Tratamento de valores nulos
   - Padronização de colunas

3. **Carga**
   - Armazenamento em banco SQLite
   - Criação de tabela `jobs`

  <img width="1351" height="762" alt="imagem resultado projeto" src="https://github.com/user-attachments/assets/ba5e5fc3-f5aa-4fab-b5da-0006e834e916" />

4. **Análise**
   - Consultas SQL para geração de insights

<img width="1346" height="754" alt="grafico" src="https://github.com/user-attachments/assets/c83d7e44-1d64-4104-bc44-236b091dc69c" />

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Requests
- SQLite
- SQL

---

--

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
<img width="1014" height="408" alt="2" src="https://github.com/user-attachments/assets/b8d0aa91-946f-4037-853e-e010b6fdad3b" />

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

<img width="1359" height="759" alt="Data Warehouse real" src="https://github.com/user-attachments/assets/ba89ed32-4747-4b09-8043-157550f4877c" />


---

# 📈 Salary Analysis

![Salary Chart](assets/salary_chart.png)

--

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

Project 3 Update — 

<img width="1338" height="732" alt="image" src="https://github.com/user-attachments/assets/64c83341-9edf-4d7e-b903-40a4049cb13d" />

pipeline_execution.png
<img width="1344" height="760" alt="projeto 3 pipiline" src="https://github.com/user-attachments/assets/a0585258-3370-4a38-b05a-7749d9a58db6" />

sqlite_tables.png
<img width="1356" height="759" alt="projeto 3 tabalas fac jobs" src="https://github.com/user-attachments/assets/8b50841f-7d9c-476a-a02c-c5b0893c2569" />
project_structure.png
<img width="1347" height="766" alt="projeto 3" src="https://github.com/user-attachments/assets/c1a41375-ec5b-4273-9f2a-5a55b01b5e6e" /
Pipeline completa executada
<img width="1347" height="766" alt="projeto 3" src="https://github.com/user-attachments/assets/8f7ffd33-ca12-4e51-b688-9d0dc962a3c7" />


```
job-data-project/
│
├── assets/
│   ├── fluxograma-project1.png
│   ├── fluxograma-project2.png
│   ├── fluxograma-project3.png
│   ├── fluxograma-project4.png
│   ├── pipeline_execution.png
│   ├── project_structure.png
│   ├── historical_data.png
│   ├── pipeline_logs.png
│   ├── sqlite_tables.png
│   ├── aws_s3_bucket.png
│   ├── salary_chart.png
│   └── git_push_project3.png
│
├── data/
│   │
│   ├── raw/
│   │   └── jobs.json
│   │
│   └── processed/
│       └── jobs.csv
│
├── logs/
│   └── pipeline.log
│
├── scripts/
│   │
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analysis.py
│   ├── upload_s3.py
│   ├── cloud_load.py
│   └── scheduler.py
│
├── sql/
│   │
│   ├── create_tables.sql
│   ├── analytics.sql
│   ├── historical_queries.sql
│   └── cloud_queries.sql
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── airflow/
│   └── dags/
│       └── etl_pipeline_dag.py
│
├── aws/
│   ├── ec2_setup.md
│   ├── s3_commands.md
│   ├── rds_setup.md
│   └── cloud_architecture.md
│
├── requirements.txt
├── .gitignore
├── README.md
├── main.py
├── jobs.db
└── config.py
```

👨‍💻 Autor

Projeto desenvolvido por Reginaldo Rocha

