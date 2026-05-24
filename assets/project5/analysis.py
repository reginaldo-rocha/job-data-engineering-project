import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# conectar no banco
conn = sqlite3.connect("jobs.db")

# query correta (sem salary)
query = """
SELECT title, COUNT(*) as total
FROM jobs
GROUP BY title
ORDER BY total DESC
LIMIT 10
"""

# criar dataframe (ESSA LINHA CRIA O DF)
df = pd.read_sql_query(query, conn)

# fechar conexão
conn.close()

# DEBUG
print(df.head())

# gerar gráfico
plt.figure()
df.plot(kind="bar", x="title", y="total")

plt.xticks(rotation=45)
plt.tight_layout()

# salvar
plt.savefig("data/chart.png")

print("✅ Gráfico gerado com sucesso!")