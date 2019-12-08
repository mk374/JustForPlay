import psycopg2
import random
import pandas as pd

"""
This script populates the database with randomly-generated data for the tables Groups, Members, Events, Attending, and Requests.
Before running this script, populate the Zip, Community, SubCommunity tables with the other scripts.
"""

def populate_all_tables():
    try:
        connection = psycopg2.connect(dbname = "justforplay")

        cursor = connection.cursor()
        
        file_path = "Static_Sample_Data.xlsx"
        ### USERS ###
        users = pd.read_excel(file_path, sheet_name="Users")

        for index, item in users.iterrows():
                postgres_insert_query = "INSERT INTO ruser VALUES (\'{}\',\'{}\',\'{}\',\'{}\',{})".format(item[0],\
                    item[1], item[2], item[3], item[4])
                cursor.execute(postgres_insert_query)
                connection.commit()

        print ("Record inserted successfully into User table")
        
        ### Groups ###
        groups = pd.read_excel(file_path, sheet_name="Groups")

        for index, item in groups.iterrows():
                postgres_insert_query = "INSERT INTO Groups VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(item[0],\
                    item[1], item[2], item[3], item[4], item[5])
                cursor.execute(postgres_insert_query)
                connection.commit()

        print ("Record inserted successfully into Groups table")

        ## Members ###
        members = pd.read_excel(file_path, sheet_name="Members")
        
        for index, item in members.iterrows():
            postgres_insert_query = "INSERT INTO Members VALUES (\'{}\',\'{}\',{})".format(item[0],\
                    item[1], item[2])
            cursor.execute(postgres_insert_query)
            connection.commit()
                
        print ("Record inserted successfully into Members table")

        ### Events ###
        events = pd.read_excel(file_path, sheet_name="Events")
    
        for index, item in events.iterrows():
            postgres_insert_query = "INSERT INTO Events VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(item[0],\
                item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            cursor.execute(postgres_insert_query)
            connection.commit()

        print ("Record inserted successfully into Events table")

        ### Attending ###
        attending = pd.read_excel(file_path, sheet_name="Attending")

        for index, item in attending.iterrows():
            postgres_insert_query = "INSERT INTO Attending VALUES (\'{}\',\'{}\')".format(item[0],\
                item[1])
            cursor.execute(postgres_insert_query)
            connection.commit()

        print ("Record inserted successfully into Attending table")

#         ### Requests ###
#         requests = pd.read_excel(file_path, sheet_name="Requests")
        
#         for index, item in requests.iterrows():
#             postgres_insert_query = "INSERT INTO Requests VALUES (\'{}\',\'{}\',\'{}\', {})".format(item[0],\
#                 item[1], item[2], item[3])
#             cursor.execute(postgres_insert_query)
#             connection.commit()

#         print ("Record inserted successfully into Attending table for answered requests")
        
        # unanswered_requests = []
        # #generate some unanswered requests
        # for i in range(100):
        #     uid = random.choice(users)[0]
        #     gid = random.choice(groups)[0]
        #     if (uid not in members_dict[gid]) and ((uid,gid,gid+uid, False) not in requests) and ((uid,gid) not in [(a[0], a[1]) for a in unanswered_requests]):
        #         convoid = gid + uid
        #         unanswered_requests.append((uid,gid,convoid))

        # for item in unanswered_requests:
        #     postgres_insert_query = "INSERT INTO Requests VALUES (\'{}\',\'{}\',\'{}\')".format(item[0],\
        #         item[1], item[2])
        #     cursor.execute(postgres_insert_query)
        #     connection.commit()

        # print ("Record inserted successfully into Attending table for unanswered requests")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def main():
    populate_all_tables()

if __name__ == "__main__":
    populate_all_tables()
