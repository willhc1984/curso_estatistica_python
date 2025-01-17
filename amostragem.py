import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('./arquivos/census.csv')

print(dataset.shape)

# print(dataset.head())
# print(dataset.tail())

# indicar tamanho da amostra e selcionar aleatoriamente da Base
df_amostra_aleatoria_simples = dataset.sample(n=50, replace=1)
print(df_amostra_aleatoria_simples)
