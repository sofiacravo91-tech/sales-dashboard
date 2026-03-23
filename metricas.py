import pandas as pd
import sqlite3
import os

os.chdir(r"C:\Users\sofia\OneDrive\sales-dashboard")

df = pd.read_csv("data/dados_vendas.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("vendas", conn, index=False)

queries = {
    "revenue_total":  "SELECT ROUND(SUM(valor),2) as revenue FROM vendas WHERE status = 'Won'",
    "pipeline_value": "SELECT ROUND(SUM(valor),2) as pipeline FROM vendas WHERE status = 'Open'",
    "win_rate":       "SELECT ROUND(100.0 * SUM(CASE WHEN status='Won' THEN 1 ELSE 0 END) / COUNT(*), 1) as win_rate FROM vendas",
    "avg_deal_size":  "SELECT ROUND(AVG(valor), 2) as avg_deal FROM vendas WHERE status = 'Won'",
    "avg_ciclo":      "SELECT ROUND(AVG(ciclo_dias), 1) as avg_ciclo FROM vendas WHERE status = 'Won'",
    "por_vendedor":   "SELECT vendedor, COUNT(*) as deals, ROUND(SUM(CASE WHEN status='Won' THEN valor ELSE 0 END),2) as revenue FROM vendas GROUP BY vendedor ORDER BY revenue DESC",
    "por_regiao":     "SELECT regiao, COUNT(*) as deals, ROUND(AVG(CASE WHEN status='Won' THEN 1.0 ELSE 0 END)*100,1) as win_rate FROM vendas GROUP BY regiao",
    "por_segmento":   "SELECT segmento, ROUND(SUM(CASE WHEN status='Won' THEN valor ELSE 0 END),2) as revenue FROM vendas GROUP BY segmento"
}

os.makedirs("outputs", exist_ok=True)

for nome, q in queries.items():
    resultado = pd.read_sql(q, conn)
    resultado.to_csv(f"outputs/metricas_{nome}.csv", index=False)
    print(f"✅ {nome}:")
    print(resultado.to_string(index=False), "\n")