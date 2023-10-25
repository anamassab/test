
import json
import pandas as pd

arquivo = r"C:\Users\anama\OneDrive\Área de Trabalho\Teste\data.json"

#lendo arquivo json com o pandas
df = pd.read_json (arquivo)

# carrega os dados usando o modulo json
with open(arquivo, 'r') as d:
    data =  json.loads(d.read())

#usando o argumento record_path para estruturar os campos dentro de Itemlist e json_normalize para normalização dos dados
df_data_list = pd.json_normalize(data, record_path=['ItemList'])

# utilizei o argumento meta para inserir a lista de metadados que quero trazer junto com os campos de itemlist
df_list = pd.json_normalize(
    data,
    record_path=['ItemList'],
    meta = ['CreateDate', 'EmissionDate', 'Discount', 'NFeNumber', 'NFeID']
)


print (df_list)

