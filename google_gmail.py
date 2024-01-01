import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Mymail :

    SCOPE = ['https://www.googleapis.com/auth/gmail.readonly']
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    messages_payload = []
    service = None
    messages_service = None
    messages_id = None
    


    def auth_google(self):
        
        scope = self.SCOPE
        api_name = self.API_NAME
        api_version = self.API_VERSION
        
        creds = None
        
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", scope)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", scope
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        
        try:
            # Call gmail API
            self.service = build(api_name, api_version, credentials=creds)
            
        except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")
            
    def get_message_service(self):
        self.messages_service = self.service.users().messages()
        
    def get_message_id(self, max_restuls=10):
        results = self.messages_service.list(userId="me", includeSpamTrash=False, maxResults=max_restuls, pageToken=1).execute()
        messages_list = results["messages"]
        self.messages_id = [message["id"] for message in messages_list]

    def get_message_payload(self):
        self.messages_payload.clear()
        for message_id in self.messages_id:
            results = self.messages_service.get(userId="me", id=message_id).execute()
            self.messages_payload.append(results["payload"])
            
    def get_message(self):
        message_dic = []
        for message in self.messages_payload:
            headers = message["headers"]
            subject = None
            from_user = None
            
            for header in headers:
                if header["name"] == "Subject":
                    subject = header["value"]
                if header["name"] == "From":
                    from_user = header["value"] 
            
            try:
                full_content = message.get("parts")[0]
                data = full_content["body"]["data"]
                
                message_content = base64.urlsafe_b64decode(data.encode('UTF-8'))
                
                decoded_content = message_content.decode('utf-8')
                
                #print(f"Subject: {subject}, From: {from_user} , content: {message_content}")
                message_dic.append({
                    "From": from_user,
                    "Subject": subject,
                    "Content": decoded_content
                })
            except:
                continue
                        
        return message_dic
    

            
            