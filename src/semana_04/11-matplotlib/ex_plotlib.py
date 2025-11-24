"""Dado o arquivo classification_results_trial_0001.csv que apresenta os resultados de classificação de um modelo entre imagens com câncer e saudáveis:"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("semana_4/10-pandas/classification_results_trial_0001.csv")

# 1. Gráfico de barras para real_class
plt.figure(figsize=(6, 4))
real_counts = df["real_class"].value_counts()
plt.bar(real_counts.index, real_counts.values, color='skyblue')
plt.title("Contagem por Classe Real")
plt.xlabel("Classe Real")
plt.ylabel("Quantidade")
plt.show()

# 2. Gráfico de barras para predicted_class
plt.figure(figsize=(6, 4))
pred_counts = df["predicted_class"].value_counts()
plt.bar(pred_counts.index, pred_counts.values, color='lightgreen')
plt.title("Contagem por Classe Predita")
plt.xlabel("Classe Predita")
plt.ylabel("Quantidade")
plt.show()

# 3. Hhstograma para prob_benign
plt.figure(figsize=(6, 4))
plt.hist(df["prob_benign"], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title("Distribuição de prob_benign")
plt.xlabel("Probabilidade de ser benigno")
plt.ylabel("Frequência")
plt.show()

# 4. Histograma para prob_malign
plt.figure(figsize=(6, 4))
plt.hist(df["prob_malign"], bins=20, color='red', edgecolor='black', alpha=0.7)
plt.title("Distribuição de prob_malign")
plt.xlabel("Probabilidade de ser maligno")
plt.ylabel("Frequência")
plt.show()

# 5. Scatter plot: prob_benign (x) vs prob_malign (y)
df["acertou"] = df["real_class"] == df["predicted_class"]

plt.figure(figsize=(6, 6))

# Separar os pontos certos e errados
acertos = df[df["acertou"] == True]
erros = df[df["acertou"] == False]

plt.scatter(acertos["prob_benign"], acertos["prob_malign"], color='green', label='Acerto', alpha=0.6)
plt.scatter(erros["prob_benign"], erros["prob_malign"], color='red', label='Erro', alpha=0.6)

plt.title("Probabilidades: Acertos vs Erros")
plt.xlabel("Probabilidade de ser benigno")
plt.ylabel("Probabilidade de ser maligno")
plt.grid(True)
plt.legend()
plt.show()

# 6. Contar falsos positvios ou negativos
FP = len(df[(df["real_class"] == "benign") & (df["predicted_class"] == "malign")])
FN = len(df[(df["real_class"] == "malign") & (df["predicted_class"] == "benign")])

# gráfico comparando FP e FN
plt.figure(figsize=(6, 4))
plt.bar(["Falso Positivo", "Falso Negativo"], [FP, FN], color=["orange", "purple"])
plt.title("Comparação: Falso Positivo vs Falso Negativo")
plt.ylabel("Quantidade")
plt.show()

print(f"Falsos Positivos: {FP}")
print(f"Falsos Negativos: {FN}")
