#TODO Create your google credentials in Google Cloud Console (enable Google Sheets API)
# and save it into project location as credensials.json

from google_interface import Drive
import pandas as pd

# The ID and range of a spreadsheet you want to read.
SAMPLE_SPREADSHEET_ID_GOOGLE = '1IoK_D6YgaQ6lat3b7KK4LbiE7fNyUgFy1BSzU0v9txA'
SAMPLE_RANGE = 'A:D'
#...or update
SPREADSHEET_TO_UPDATE = '1nBXuCTHT5JQ8Es7aN4Rd6DZTZnifCgJP0tBczo0Pwi8'


g_drive = Drive()

#Creates raw data consisting on rows from google spreadsheet as list of lists.
google_data_raw = g_drive.main(SAMPLE_SPREADSHEET_ID_GOOGLE, SAMPLE_RANGE)

#Creates dataframe out of list (row records from google spreadsheet
df = pd.DataFrame(google_data_raw)

#Exporing data to choosen spreadsheet from a dataframe.
file_to_export = g_drive.update_sheet(df, spreadsheetid=SPREADSHEET_TO_UPDATE)
