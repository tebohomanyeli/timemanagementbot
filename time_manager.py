import connect_to_api as api
import connect_to_calendar as calendar

def main():
    creds = api.login()     #creates login credentials for user
    service = calendar.connect_to_calendar_api(creds)   #calls the google calendar api

    try:
        calendar.commitHours(service)

    except calendar.HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()