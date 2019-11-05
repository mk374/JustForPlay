import psycopg2
import pandas as pd

def get_sub_communities():
    df_sub_communities = pd.read_excel("../Sample_Datasets.xlsx",sheet_name="SubCommunity", header=[0])
    
    return df_sub_communities

def connect_communities(subcomm):
    try:
        connection = psycopg2.connect(dbname="justforplay")
        cursor = connection.cursor()
        
        for index, row in subcomm.iterrows():
            postgres_insert_query = " INSERT INTO SubCommunity (communityid, subid, sub_description) VALUES (\'{}\',\'{}\', \'{}\') ".format(str(row[0].replace("'", "")), str(row[1]).replace("'", ""), str(row[2]).replace("'", ""))
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
    sub_communities = get_sub_communities()
    connect_communities(sub_communities)

if __name__ == "__main__":
    main()