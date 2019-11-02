import psycopg2
import pandas as pd

def bulkInsert(records):
    try:
        connection = psycopg2.connect(dbname="postgres_db")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO Community (communityid, description) 
                           VALUES (%s,%s) """

        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

df_community = pd.read_excel("../Sample Datasets.xlsx", sheet_name="Community", header=True)
records_to_insert = [(row[0],row[1]) for index, row in df_community.iterrows()]
bulkInsert(records_to_insert)