import pandas as pd
import random
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

dataset = pd.read_csv('./arquivos/census.csv')

print(dataset['income'].value_counts())

print(7841 / len(dataset), 24720 / len(dataset))
print(7841 + 24720)
print(0.2408095574460244 + 0.7591904425539756)

# amostra estratificada - seleciona conforme a proporção de pessoas que representa
# na base de  Ex.. selecionar proporcionalmente pessoas que ganham menos de 50k ou mais
# por ano, conforme dados no data set.

# seleciona 100 pessoas da base de dados
split = StratifiedShuffleSplit(test_size=0.003071)

# coloca 90% na variavel x e 10% na variavel y
for x, y in split.split(dataset, dataset['income']):
    df_x = dataset.iloc[x]
    df_y = dataset.iloc[y]

print(df_x.shape, df_y.shape)

print(df_y.head)

# verifica se dividiu a amostra proporcional aos valores de renda <=50k ou >50k
print(df_y['income'].value_counts())
