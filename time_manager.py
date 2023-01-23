import connect_to_api as api
import connect_to_calendar as calendar
import sql_database as database
import datetime


def main():
    
    creds   = api.login()     #creates login credentials for user
    service = calendar.connect_to_calendar_api(creds)   #calls the google calendar api

    try:
        calendar.commitHours(service)

    except calendar.HttpError as error:
        print('An error occurred: %s' % error)





    #Insert Data into SQL Database
    table_name  = 'hours.db'
    conn, curs  = database.load_table(table_name)
    date        = datetime.date.today()
    categ       = "Toy 5 Coding"
    time        = datetime.timedelta(seconds=0, minutes=30, hours= 2)
    time        = time.seconds/60/60

    new_data = (date, categ, time)
    database.add_insert_data(table_name,conn,curs,new_data)

if __name__ == '__main__':
    main()
    
    




