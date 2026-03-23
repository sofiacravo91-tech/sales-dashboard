import pandas as pd
from sklearn.linear_model import LinearRegression
import os

os.chdir(r"C:\Users\sofia\OneDrive\sales-dashboard")

df = pd.read_csv("data/dados_vendas.csv")
df["data_fechamento"] = pd.to_datetime(df["data_fechamento"])

won = df[df["status"] == "Won"].copy()
won["mes"] = won["data_fechamento"].dt.to_period("M")

receita_mensal = won.groupby("mes")["valor"].sum().reset_index()
receita_mensal["mes_num"] = range(len(receita_mensal))
receita_mensal["mes"] = receita_mensal["mes"].astype(str)

X = receita_mensal[["mes_num"]]
y = receita_mensal["valor"]

model = LinearRegression()
model.fit(X, y)

proximos = pd.DataFrame({"mes_num": range(len(receita_mensal), len(receita_mensal) + 3)})
proximos["previsao"] = model.predict(proximos[["mes_num"]]).round(2)
proximos["mes"] = ["Previsão M+1", "Previsão M+2", "Previsão M+3"]

print("📈 Receita mensal histórica:")
print(receita_mensal[["mes", "valor"]].to_string(index=False))
print("\n📊 Previsão dos próximos 3 meses:")
print(proximos[["mes", "previsao"]].to_string(index=False))

receita_mensal.to_csv("outputs/receita_mensal.csv", index=False)
proximos[["mes", "previsao"]].to_csv("outputs/previsao_receita.csv", index=False)
print("\n✅ Ficheiros de previsão guardados em outputs/")