# access the Gmail API for marko.delgadillo@leftfieldlabs.com (determined by the credentials.json)
# tutorial: https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/
# documentation: https://developers.google.com/gmail/api/quickstart/python
from __future__ import print_function
import pickle
import os.path
import base64 
import email
import pprint
import json 
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():

    pp = pprint.PrettyPrinter(indent=4)
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    messages = service.users().messages().list(userId='me', maxResults= 1).execute()
    message_id = messages['messages'][0]['id']
    recent_message = service.users().messages().get(userId='me', id = message_id).execute()

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

    print(recent_message)

if __name__ == '__main__':
    main()