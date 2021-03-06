#TODO Create your google credentials in Google Cloud Console (enable Google Sheets API)
# and save it into project location as credensials.json

from google_interface import Drive
import pandas as pd

# The ID and range of a spreadsheet you want to read.
SAMPLE_SPREADSHEET_ID_GOOGLE = 'ENTER YOUR spshID'
SAMPLE_RANGE = 'A:D'
#...or update
SPREADSHEET_TO_UPDATE = 'ENTER YOUR spshID'


g_drive = Drive()

#Creates raw data consisting on rows from google spreadsheet as list of lists.
google_data_raw = g_drive.main(SAMPLE_SPREADSHEET_ID_GOOGLE, SAMPLE_RANGE)

#Creates dataframe out of list (row records from google spreadsheet
df = pd.DataFrame(google_data_raw)

#Exporing data to choosen spreadsheet from a dataframe.
file_to_export = g_drive.update_sheet(df, spreadsheetid=SPREADSHEET_TO_UPDATE)
