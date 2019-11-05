import psycopg2
import random

def populate_all_tables():
    try:
        connection = psycopg2.connect(dbname = "justforplay")

        cursor = connection.cursor()
        
        ### USERS ###
        names = ['Dave', 'Sammy', 'Minsoo', 'Benjamin', 'Andy', 'Abby', 'Tommy', 'Ross', 'Rachel','Joey', 'Chandler', 'Phoebe',
                'Monica', 'Bart', 'Homer', 'Marge', 'Lisa', 'Maggie']
        snacks = ['crepes', 'goldfish', 'Doritos', 'waffles', 'pancakes', 'pumpkin pie']
        users = []
        zips = [27503, 27517, 27560, 27701, 27703, 27704, 27705, 27707, 27709, 27712, 27713]
        for i in range(1000):
            rname = random.choice(names)
            ruid = rname + str(i)
            rpassword = 'password' + str(i)
            rbio = 'My name is ' + rname + ' and I like ' + random.choice(snacks) + '.'
            rzipcode = random.choice(zips)
            temp = (ruid, rname, rpassword, rbio, rzipcode)
            users.append(temp)

        for item in users:
                postgres_insert_query = "INSERT INTO ruser VALUES (\'{}\',\'{}\',\'{}\',\'{}\',{})".format(item[0],\
                    item[1], item[2], item[3], item[4])
                cursor.execute(postgres_insert_query)
                connection.commit()

        print ("Record inserted successfully into User table")

        ### Communities ###
        community_dict = {'Music': ['Playing together'], 
            'Animals': ['Birdwatching'], 
            'Games': ['Dungeons and Dragons'], 
            'Sports': ['Football'], 
            'Nightlife': ['Trivia Nights', 'Bar hopping'], 
            'Foodies': ["Restaurant openings"], 
            'LGBTQ+': ["Mixers"],
            'Language Practice': ['Chinese practice', 'Spanish practice'], 
            'Students': ['Free food'], 
            'Religion': ['Catholic Mass', 'Jewish Holidays'], 
            'Philanthropy': ['Animal shelter'], 
            'Wellbeing': ['Yoga'], 
            'Movies and Theatre': ['MARVEL movies'], 
            'Odd jobs': ['Babysitting', 'Lawn mowers'], 
            'Happy Hours': ['Durham'], 
            'Crafts': ['Knitting Club'], 
            'History': ['Monuments'], 
            'Book Club': ['Oprahs Book Club'], 
            'Nature': ['Surfing', 'Hiking'], 
            'Politics': ['Debate Watch Party']}
        
        ### Groups ###
        group_name = list(community_dict.keys())
        groups = []
        for i in range(100):
            comm_id = random.choice(group_name)
            sub_id = random.choice(community_dict[comm_id])
            gname = comm_id + str(i)
            guid = str(i) + gname
            pub_or_priv = random.choice(['public', 'private'])
            gzipcode = random.choice(zips)
            description = "We like to", comm_id
            temp = (guid, gname, comm_id, sub_id, gzipcode, pub_or_priv, description)
            groups.append(temp)

        for item in groups:
                postgres_insert_query = "INSERT INTO Groups VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(item[0],\
                    item[1], item[2], item[3], item[4], item[5], item[6])
                cursor.execute(postgres_insert_query)
                connection.commit()

        print ("Record inserted successfully into Groups table")

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