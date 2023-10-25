
import json 
import pandas as pd
import numpy as np
arquivo = r"C:\Users\anama\OneDrive\Área de Trabalho\Teste\data.json"

df = pd.read_json (arquivo)
df.head()

# Abre o arquivo json
with open (arquivo) as data:
    dados = json.load(data)

# Normaliza os dados item list
dt = pd.json_normalize(dados,'ItemList')

#
# 
print(dt)
print(df)