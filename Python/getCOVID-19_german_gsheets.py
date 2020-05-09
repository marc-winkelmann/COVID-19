import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

# get the current data for germany (Robert Koch Institut)
germanyCurrent = pd.read_csv('https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv')
gcDf = pd.DataFrame(germanyCurrent)

# get the history data from germany (Robert Koch Institut)
germanyTimeline = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv')
gtDf = pd.DataFrame(germanyTimeline)


# create scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# get credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/pythonProjects/COVID-19/Python/covid-19_gsheetsAccess.json', scope)

# authorize with credentials
gc = gspread.authorize(credentials)

# get the google spreadsheet ID and worksheet name
spreadsheet_key = '1xTcBbUqPgOnOM5brZtvbGxWuxM2AU16CFBbPWOoR08c'
wks_germany_current = 'COVID-19_germany_current'
wks_germany_timeline = 'COVID-19_germany_timeline'

# upload the dataframe to gsheets
d2g.upload(df=gcDf, gfile=spreadsheet_key, wks_name=wks_germany_current, credentials=credentials, row_names=False, col_names=True)
d2g.upload(df=gtDf, gfile=spreadsheet_key, wks_name=wks_germany_timeline, credentials=credentials, row_names=False, col_names=True)