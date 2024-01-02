import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Google_auth :

    SCOPE = ['https://www.googleapis.com/auth/gmail.readonly']
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    messages_payload = []
    service = None
    messages_service = None
    messages_id = None
    
    
    def log(self):
        
        scope = self.SCOPE
        api_name = self.API_NAME
        api_version = self.API_VERSION
        
        creds = None
        """
        if os.path.exists("Data/token.json"):
            creds = Credentials.from_authorized_user_file("Data/token.json", scope)"""
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "Data/credentials.json", scope
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            """with open("Data/token.json", "w") as token:
                token.write(creds.to_json())"""
        try:
            # Call gmail API
            return build(api_name, api_version, credentials=creds)
        except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")