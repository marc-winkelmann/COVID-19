import datetime
import pandas as pd
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

now = datetime.datetime.now()

# create scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# get credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/pythonProjects/COVID-19/Python/covid-19_gsheetsAccess.json', scope)
#credentials = ServiceAccountCredentials.from_json_keyfile_name('covid-19_gsheetsAccess.json', scope)

# get the google spreadsheet ID and worksheet name
spreadsheet_key = '1xTcBbUqPgOnOM5brZtvbGxWuxM2AU16CFBbPWOoR08c'
wks_control = 'control'

################################################################
### load COVID-19 data (Johns Hopkins University) to GSheets ###
################################################################
try:
    exec(open("/home/ubuntu/pythonProjects/COVID-19/Python/getCOVID-19_gsheets.py").read(), globals())
    #exec(open("getCOVID-19_gsheets.py").read(), globals())
except Exception as e:
    loadCovid19 = pd.DataFrame(
        {"job_name": ["getCOVID-19_gsheets.py"],
         "timestamp": [now],
         "success": "n",
         "status": str(e)})
    d2g.upload(df=loadCovid19, gfile=spreadsheet_key, wks_name=wks_control, credentials=credentials, row_names=False, col_names=True)

else:
    loadCovid19 = pd.DataFrame(
        {"job_name": ["getCOVID-19_gsheets.py"],
         "timestamp": [now],
         "success": "y",
         "status": "ok"})

    d2g.upload(df=loadCovid19, gfile=spreadsheet_key, wks_name=wks_control, credentials=credentials, row_names=False, col_names=True)

############################################################
### load COVID-19 data (Robert Koch Institut) to GSheets ###
############################################################
try:
    exec(open("/home/ubuntu/pythonProjects/COVID-19/Python/getCOVID-19_german_gsheets.py").read(), globals())
    #exec(open("getCOVID-19_german_gsheets.py").read(), globals())
except Exception as e:
    loadCovid19_germany = pd.DataFrame(
        {"job_name": ["getCOVID-19_german_gsheets.py"],
         "timestamp": [now],
         "success": "n",
         "status": str(e)})

    d2g.upload(df=loadCovid19_germany, clean=False, gfile=spreadsheet_key, wks_name=wks_control, credentials=credentials, row_names=False, col_names=False, start_cell='A3')

else:
    loadCovid19_germany = pd.DataFrame(
        {"job_name": ["getCOVID-19_german_gsheets.py"],
         "timestamp": [now],
         "success": "y",
         "status": "ok"})

    d2g.upload(df=loadCovid19_germany, clean=False, gfile=spreadsheet_key, wks_name=wks_control, credentials=credentials, row_names=False, col_names=False, start_cell='A3')