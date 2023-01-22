import sqlite3


def create_sql_file(name_of_table):
    """
    Run once!!! to intialise or create a table
    """

    #Create file and connect to it:
    conn = sqlite3.connect(f"{name_of_table}.db")
    curr = conn.cursor()
    print("Opened database file successfully")

    return conn

def create_sql_file(conn: sqlite3.connect):
    # create the table
    conn.execute(
                    """CREATE TABLE hours
                    (
                        DATE        DATE    NOT NULL,
                        CATEGORY    TEXT    NOT NULL,
                        HOURS       INT     NOT NULL
                    )
                    """
                )

    print("Table created successfully")