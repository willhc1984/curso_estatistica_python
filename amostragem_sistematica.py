import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('./arquivos/census.csv')

# Dividir a população pela numero de amostras - 100
# print(len(dataset) // 100)  # 2 barras para areddondar a divisão

# retorna numero aleatorio no intervalo
# random.seed(2)  # fixa um numero aleatório
# print(random.randint(0, 325))

# amostra sistematica definida em 38 e selecionando de 271 em 271
# print(np.arange(38, len(dataset), step=271))


# Função para coletar amostra sistematica
def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(3)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step=intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica


df_amostras_sistematica = amostragem_sistematica(dataset, 100)
print(df_amostras_sistematica.shape)
print(df_amostras_sistematica)
