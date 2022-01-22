import requests
import json
import pandas as pd

response = requests.get('https://pomber.github.io/covid19/timeseries.json')

response = json.loads(json.dumps(response.json()))

row = list()

for c in response.keys():

    for item in response[c]:
        rowTemp = list()
        rowTemp.append(c)
        rowTemp.extend(item.values())

        row.append(rowTemp)

df = pd.DataFrame(row, columns=['country','date','confirmed','deaths','recovered'])

df.to_csv('C:/Users/marcf/Documents/COVID-19/Data/covid-19.csv', sep=';', encoding='utf-8', index=False)