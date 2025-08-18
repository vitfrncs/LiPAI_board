import pandas as pd

# 1. Ler o arquivo CSV (ajuste o caminho se necessário)
df = pd.read_csv("semana_4/10-pandas/classification_results_trial_0001.csv", sep=',')

# 2. Quantas imagens são "benign" e "malign"?
print("Contagem de classes reais:")
print(df["real_class"].value_counts())

print("\n" + "="*60)

# 3. Identificar erros do modelo
df["acertou"] = df["real_class"] == df["predicted_class"]
print("Erros do modelo (real ≠ predito):")
print(df[~df["acertou"]][["image_path", "real_class", "predicted_class"]])

print("\n" + "="*60)

# 4. Conferir confiança nos erros
print("Confiança do modelo nos erros:")
print(df[~df["acertou"]][["image_path", "real_class", "predicted_class", "prob_benign", "prob_malign"]])

print("\n" + "="*60)

# 5. Calcular TP, TN, FP, FN
df_malign = df[df["real_class"] == "malign"]
df_benign = df[df["real_class"] == "benign"]

tp = (df_malign["predicted_class"] == "malign").sum()
fn = (df_malign["predicted_class"] == "benign").sum()
tn = (df_benign["predicted_class"] == "benign").sum()
fp = (df_benign["predicted_class"] == "malign").sum()

print(f"TP (malign/malign): {tp}")
print(f"TN (benign/benign): {tn}")
print(f"FP (benign/malign): {fp}")
print(f"FN (malign/benign): {fn}")

print("\n" + "="*60)

# 6. Métricas
total = tp + tn + fp + fn
acuracia = (tp + tn) / total
precisao = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
especificidade = tn / (tn + fp) if (tn + fp) > 0 else 0

print(f"Acurácia: {acuracia:.4f}")
print(f"Precisão (precision): {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"Especificidade: {especificidade:.4f}")

print("\n" + "="*60)

# 7. Top 5 benignos com menor probabilidade de serem benignos
print("Benignos mais incertos (baixa prob_benign):")
benignos_incertos = df_benign.sort_values(by="prob_benign").head(5)
print(benignos_incertos[["image_path", "prob_benign", "prob_malign"]])

print("\n" + "="*60)

# 8. Top 5 malignos com maior probabilidade de serem benignos
print("Malignos mais confiantemente classificados como benignos (alto prob_benign):")
malignos_errados_confiantes = df_malign.sort_values(by="prob_benign", ascending=False).head(5)
print(malignos_errados_confiantes[["image_path", "prob_benign", "prob_malign"]])
