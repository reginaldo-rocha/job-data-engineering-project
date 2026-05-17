# 🚀 Job Market Insights  
### Pipeline de Dados com API Pública, Python e SQL-Projeto 01

<img width="1536" height="1024" alt="ChatGPT Image 17 de mai  de 2026, 16_31_28" src="https://github.com/user-attachments/assets/13fbb38e-93d0-47b8-a1b8-ad5c44dd0cb1" />



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
- Matplotlib

---

## 📁 Estrutura do Projeto
```
job-data-project/
│
├── data/
│ ├── raw_jobs.json
│ ├── clean_jobs.csv
│
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── analysis.py
│
├── assets/
│ └── fluxo.png
│
├── jobs.db
├── queries.sql
└── README.md
```
📈 Resultados

O projeto permite identificar:
```
Tendências salariais por cargo
Empresas com maior volume de contratações
Distribuição geográfica das vagas
Insights estratégicos sobre o mercado de trabalho
```

🔥 Diferenciais
```
Pipeline completo (API → Python → SQL)
Dados reais (não estáticos)
Organização profissional de projeto
Aplicação prática para análise de mercado
```

👨‍💻 Autor

Projeto desenvolvido por Reginaldo Rocha
