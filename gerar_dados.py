import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

vendedores = ["Ana Silva", "Bruno Costa", "Carla Souza", "Diego Lima", "Eva Martins"]
regioes = ["Sul", "Norte", "Sudeste", "Centro-Oeste", "Nordeste"]
segmentos = ["PME", "Enterprise", "Mid-Market"]
status_options = ["Won", "Lost", "Open"]

n = 500
data_inicio = datetime(2023, 1, 1)

dados = []
for i in range(n):
    criado = data_inicio + timedelta(days=random.randint(0, 365))
    ciclo = random.randint(15, 120)
    fechado = criado + timedelta(days=ciclo)
    status = random.choices(status_options, weights=[0.35, 0.30, 0.35])[0]
    valor = round(random.uniform(5000, 150000), 2)
    dados.append({
        "deal_id": f"DEAL-{i+1:04d}",
        "vendedor": random.choice(vendedores),
        "regiao": random.choice(regioes),
        "segmento": random.choice(segmentos),
        "valor": valor,
        "status": status,
        "data_criacao": criado.strftime("%Y-%m-%d"),
        "data_fechamento": fechado.strftime("%Y-%m-%d"),
        "ciclo_dias": ciclo
    })

df = pd.DataFrame(dados)
df.to_csv(r"C:\Users\sofia\OneDrive\sales-dashboard\data\dados_vendas.csv", index=False)
print(f"✅ Arquivo gerado com {len(df)} registros.")