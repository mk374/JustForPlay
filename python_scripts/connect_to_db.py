#code from https://pynative.com/python-postgresql-tutorial/#Python_PostgreSQL_Database_Connection

import psycopg2
try:
    connection = psycopg2.connect(user = "sysadmin",
                                  password = "pynative@#29",
                                  host = "127.0.0.1",
                                  port = "5000",
                                  database = "postgres_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")