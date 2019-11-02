
import csv
from collections import defaultdict
import psycopg2

def zipcodes():


    zipcode_latitude_longitude = defaultdict(list)

    with open('us-zip-code-latitude-and-longitude.csv', 'r') as csvfile:
        dataRow = csv.reader(csvfile, delimiter=',')

        for i, row in enumerate(dataRow):
            if i == 0: 
                continue
            lat_long_data = row[0].split(";")
            zipcode = int(lat_long_data[0])
            latitude = float(lat_long_data[3])
            longitude = float(lat_long_data[4])
            zipcode_latitude_longitude[zipcode] = [latitude, longitude]

            if i == 10: 
                break
    
    return zipcode_latitude_longitude

def connect_zip(zipcodes):
    try:
        connection = psycopg2.connect(dbname = "justforplay")
        cursor = connection.cursor()

    
        for key, value in zipcodes.items():
            postgres_insert_query = "INSERT INTO zip VALUES ({},{},{})".format(key, value[0], value[1])
            cursor.execute(postgres_insert_query)
            connection.commit()
            count = cursor.rowcount
            
        print ("Record inserted successfully into mobile table")
      
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":
    zipcodes = zipcodes()
    connect_zip(zipcodes)
