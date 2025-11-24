"""Dado o arquivo metrics.csv utilizando o Pandas e Matplotlib crie um gráfico semelhante ao de referência com as curvas de acurácia e perda do conjunto de treinamento e validação."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('metrics.csv', sep=',')


# cada linha do arquivoé uma epoca
# criando colina de epocas de 1 a 50
df['epoch'] = range(len(df))

#figura com 1 linha e duas colunas, como na imagem apresentada
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(df['epoch'], df['train_acc'], label='train', color='blue', linewidth=2)
ax1.plot(df['epoch'], df['val_acc'], label='valid', color='orange', linewidth=2)
ax1.set_title('model accuracy')
ax1.set_xlabel('epoch')
ax1.set_ylabel('accuracy')
ax1.legend() # diz qual linha é o que (train ou valid)
ax1.grid(True, alpha=0.3)

ax2.plot(df['epoch'], df['train_loss'], label='train', color='blue', linewidth=2)
ax2.plot(df['epoch'], df['val_loss'], label='valid', color='orange', linewidth=2)
ax2.set_title('model loss')
ax2.set_xlabel('epoch')
ax2.set_ylabel('loss')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.subplots_adjust(wspace=0.3) # ajustando graficos

plt.show()