from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
    

def quickstart():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        return creds
#-------------------------------------------------------------------------------


def login():
    """
    Loads the correct scope for specific user
    """
    global SCOPES

    print("Welcome to Time Managment Bot.\nPlease login")
    email = enter_email()

    if not os.path.exists("admin_users_database.txt"):
        open("admin_users_database.txt","w")

    with open("admin_users_database.txt","r") as users:
        if email in users.read() and os.path.exists(f'{email}.json'):
            creds = Credentials.from_authorized_user_file(f'{email}.json', SCOPES)
            print("Login Successfull")
            return creds

        else:
            print("New User, creating credentials")
            return capture_login(email)


def generate_token(user_email):   
    """
    Creates User Access token:
    - The file token.json stores the user's access and refresh tokens, and is
    created automatically when the authorization flow completes for the first
    time.
    """
    global SCOPES
    creds:Credentials = None
    

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(f'{user_email}.json', 'w') as token:
            token.write(creds.to_json())
            
        
    return creds.client_secret


def capture_login(email:str):
    """
    Captures user's email address and creates a user name from the email address.
    """
    if email.find("@") == -1:    #No @sign
        print("\nInvalid email address. Try again:  ")
        return capture_login(enter_email())

    secret = generate_token(email)
    with open("admin_users_database.txt","a") as add_user:
        add_user.write(f"{email}, {secret}\n")
    
    print("... ... ... ... .. ... complete. Login Again\n")
    return login()


def enter_email():
    return input("Enter your email:  ")





def main():
    creds = login()
    return creds


if __name__ == '__main__':
    main()