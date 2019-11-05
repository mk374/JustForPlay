import psycopg2
import pandas as pd
from collections import defaultdict

def get_communities():
    df_communities = pd.read_excel("../Sample_Datasets.xlsx",sheet_name="Community", header=[0])
    communities = defaultdict(str)
    
    for i, row in df_communities.iterrows():
        community_id = str(row[0])
        description = str(row[1])

        communities[community_id] = description

    return communities



def connect_communities(comm):
    try:
        connection = psycopg2.connect(dbname="justforplay")
        cursor = connection.cursor()
        
        for key, value in comm.items():
            postgres_insert_query = """ INSERT INTO Community (communityid, description) 
                           VALUES ({},{}) """.format(key, value)
            cursor.execute(postgres_insert_query)
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def main():
    communities = get_communities()
    connect_communities(communities)

if __name__ == "__main__":
    main()