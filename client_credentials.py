from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
scope = ['https://www.googleapis.com/auth/userinfo.profile']

creds = None
personal_details = []
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

def enter_names():
    first_names = input("Enter your first name: ")
    surname = input("Enter your surname: ")

    return [first_names, surname]


def enter_email():
    email = input("Enter your email address: ")

    return email


def enter_password():
    password = input("Enter your password: ")
    return password


def register():
    global personal_details

    personal_details.append(enter_names())
    personal_details.append(enter_email())
    personal_details.append(enter_password())
    



def login():
    global personal_details
    global creds

    user_email = enter_email()
    user_pass  = enter_password()

    if os.path.exists(f'.{user_email}.json'):
        existing_creds(user_email)
        
        

    else:
        print("We can seem to find your account please register for an account: ")
        print()
        register()

        create_creds(user_email)


def create_creds(user_email):
    global creds


    if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'.{user_email}.json', 'w') as token:
                token.write(creds.to_json())

                print("Auth Succesful")

    # return token


def test_func():
    global creds
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scope)
    creds = flow.run_local_server(port=0)

def existing_creds(user_email):
    global creds
    
    # if os.path.exists(f'.{user_email}.json'):
    creds = Credentials.from_authorized_user_file(f'.{user_email}.json', SCOPES)

    print("user exists")    #delete later
    return creds

    


