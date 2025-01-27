import pandas as pd
import random
import numpy as np

dataset = pd.read_csv('./arquivos/census.csv')

print(len(dataset) / 10)  # gerar 10 grupos

# grupos = []
# id_grupo = 0
# contagem = 0

# divide dataset em grupos
# for _ in dataset.iterrows():
#    grupos.append(id_grupo)
#    contagem += 1
#    if contagem > 3256:
#        contagem = 0
#        id_grupo += 1

# print(grupos)

# print(np.unique(grupos, return_counts=True))  # conta valores unicos

# dataset['grupo'] = grupos  # adiciona coluna grupo em relação a grupos
# print(dataset.head())  # começo do dataset
# print(dataset.tail())  # final do dataset

# print(random.randint(0, 9))  # escolhe randomicamente um dos grupos

# df_agrupamento = dataset[dataset['grupo'] == 7]  # seleciona o grupo 7
# df_agrupamento['grupo'].value_counts()  # conta os valores do grupo 7


# função para retornar uma amostra por grupo aleatoriamente
def amostragem_agrupamento(dataset, numero_grupos):
    intervalo = len(dataset) / numero_grupos

    grupos = []
    id_grupo = 0
    contagem = 0

    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo:
            contagem = 0
            id_grupo += 1

    dataset['grupo'] = grupos
    grupo_selecionado = random.randint(0, numero_grupos)
    return dataset[dataset['grupo'] == grupo_selecionado]


df_amostra_agrupamento = amostragem_agrupamento(dataset, 100)

print(df_amostra_agrupamento['grupo'].value_counts())
