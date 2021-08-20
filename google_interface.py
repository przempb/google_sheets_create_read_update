from __future__ import print_function
import os.path
from googleapiclient.discovery import build #you may need to use pip install google-api-python-client in the terminal
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient import discovery


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


rangeName = "!A2"

class Drive:

    def __init__(self):
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

#___READS GOOGLE SPREATSHEETS. TRANSFORMING ROWS INTO LIST - MUST BE REFACTORED TO DFRAME EG USING PANDAS
    def main(self, spreadsheet_id, range):

        service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range).execute()
        values = result.get('values', [])
        return values

#___CREATE NEW SPREADSHEET
    def create_result(self):

        service = discovery.build('sheets', 'v4', credentials=self.creds)

        spreadsheet_body = {
            'properties': {
                'title': "abc"
            }
        }

        request = service.spreadsheets().create(body=spreadsheet_body, fields='spreadsheetId')
        response = request.execute()
        return response

#___UPDATE SPREADSHEET VALUES OVERWRITING IT.
    def update_sheet(self, dframe, spreadsheetid):
        service = discovery.build('sheets', 'v4', credentials=self.creds)

        body = {
            "values": dframe.values.tolist(),
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheetid, range=rangeName,
            valueInputOption='RAW', body=body, includeValuesInResponse=True).execute()
        return result

