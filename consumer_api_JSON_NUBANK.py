#A NUBANK PROCESS 
import pandas as pd
import requests


# 1) Seu código aqui
url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=RJ&tipo_interessado=Munic%C3%ADpio'

r = requests.get(url)
r.status_code
data_json = r.json()
print(data_json['items'])

base = pd.DataFrame(data_json['items'])

#base in data pandas
base

base.value_counts(['status'])