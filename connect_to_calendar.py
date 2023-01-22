from __future__ import print_function

import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dateutil import parser



def quickstart():
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    from connect_to_api import login
    creds = login()

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)
#-------------------------------------------------------------------------------


def connect_to_calendar_api(creds):
    return build('calendar', 'v3', credentials=creds)


#-------------------------------------------------------------------------------
import connect_to_api as api




def commitHours():
    creds = api.login()
    service = connect_to_calendar_api(creds)
    """
    Objective is to save all the events from this day on in to a database. 
    """

    #Time Formate
    today       = datetime.date.today()         #; print(today)
    start_time  = str(today) + "T00:00:00Z"     #; print(start_time)
    end_time    = str(today) + "T23:59:59Z"     #; print(end_time)      # "Z" indicates UTC time

    print("Getting today's coding hours")

    #My Calendars:
    """NOTE:
    primary = default calendar
    
    Create new calendar for tracking our programming hours:
    Step 1 -    Go to https://calendar.google.com/calendar/
    Step 2 -    Create a new calendar called "programming"
    Step 3 -    Click on programming drop-down
                Click on Settings and Sharing
                Scoll down to "Integrate calendar"
    Step 4 -    Copy the Calendar ID
                08aa21047d1407b92a4ecb3253c4a519377ee8a0bed34cd79816e03d9d3066b9@group.calendar.google.com
    """
    programming_calendar_id = "08aa21047d1407b92a4ecb3253c4a519377ee8a0bed34cd79816e03d9d3066b9@group.calendar.google.com"
    calendar_id = ['primary', programming_calendar_id]

    time_zone = "South Africa Standard Time"

    #Get Events:
    events_result = service.events().list ( calendarId  = programming_calendar_id, 
                                            timeMin     = start_time,
                                            timeMax     = end_time,
                                            singleEvents= True,
                                            orderBy     = 'startTime',
                                            timeZone    = time_zone
                                          ).execute()

    events = events_result.get('items', [])

    if not events:
            print('No upcoming events found.')
            return

    #Time duration monitor:
    total_duration = datetime.timedelta(seconds=0, minutes=0, hours= 0)

    print("Coding/Programming Hours:")
    

    for event in events:
        start   = event['start'].get('dateTime', event['start'].get('date'))
        end     = event['end'].get('dateTime', event['end'].get('date'))


        start_formatted = parser.isoparse(start)    #Changing the start time to datetime format
        end_formatted  = parser.isoparse(end)       #Changing the end time to datetime format 

        duration = end_formatted - start_formatted

        total_duration += duration
        print(f"{event['summary']}, duration: {duration}")
        print(f"Total coding time: {total_duration}")



try:
    commitHours()
except HttpError as error:
        print('An error occurred: %s' % error)