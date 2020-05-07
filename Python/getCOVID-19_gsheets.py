import requests
import json
import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

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

# create scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# get credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/pythonProjects/COVID-19/Python/covid-19_gsheetsAccess.json', scope)

# authorize with credentials
gc = gspread.authorize(credentials)

# get the google spreadsheet ID and worksheet name
spreadsheet_key = '1xTcBbUqPgOnOM5brZtvbGxWuxM2AU16CFBbPWOoR08c'
wks = 'COVID-19'

# upload the dataframe to gsheets
d2g.upload(df=df, gfile=spreadsheet_key, wks_name=wks, credentials=credentials, row_names=False, col_names=True)

#df.to_csv('C:/Users/Marc/PycharmProjects/COVID-19/Data/covid-19.csv', sep=';', encoding='utf-8', index=False)