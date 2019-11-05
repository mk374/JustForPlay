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
            description = "We like " + comm_id
            temp = (guid, gname, comm_id, sub_id, gzipcode, pub_or_priv, description)
            groups.append(temp)

        for item in groups:
                postgres_insert_query = "INSERT INTO Groups VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(item[0],\
                    item[1], item[2], item[3], item[4], item[5], item[6])
                cursor.execute(postgres_insert_query)
                connection.commit()

        print ("Record inserted successfully into Groups table")

        ## Members ###
        members_dict = {}
        members = []
        for i in range(2000):
            u = random.choice(users)[0]
            g = random.choice(groups)[0]
            if (g in members_dict.keys() and u not in members_dict[g]) or (g not in members_dict.keys()):
                adm = random.choice([False, True, False, False])
                members.append((u,g,adm))
                if g in members_dict.keys():
                    members_dict[g].append(u)
                else:
                    members_dict[g] = [u]
        
        for item in members:
            postgres_insert_query = "INSERT INTO Members VALUES (\'{}\',\'{}\',{})".format(item[0],\
                    item[1], item[2])
            cursor.execute(postgres_insert_query)
            connection.commit()
                
        print ("Record inserted successfully into Members table")

        ### Events ###
        events = []
        for i in range(100):
            g = random.choice(groups)
            gid = g[0]
            cid = g[2]
            pub_or_priv = random.choice(['public', 'private'])
            eid = str(i)
            ename = str(cid) + " party!"
            h = random.choice(members_dict[gid])
            location = random.choice(["coffee shop", "underneath the bed", "in WU", "house of " + h, "basketball courts", "gym", "Eno River", "Jordan Lake"])
            #date
            year = 2019
            month = str(random.choice(range(1,13)))
            day = str(random.choice(range(1,29)))
            if len(day) == 1:
                day = "0" + day
            if len(month) == 1:
                month = "0" + month
            edt = str(year) + "-" + month + "-" + day
            #time
            hr = str(random.choice(range(1, 25)))
            if len(hr) == 1:
                hr = "0" + hr
            etm = hr + ":00:00"
            events.append((gid,eid,ename,h,location,edt, etm, pub_or_priv))
    
        for item in events:
            postgres_insert_query = "INSERT INTO Events VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(item[0],\
                item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            cursor.execute(postgres_insert_query)
            connection.commit()

        print ("Record inserted successfully into Events table")

        ### Attending ###
        attending = []
        for e in events:
            eid = e[1]
            gid = e[0]
            num = random.choice(range(len(members_dict[gid])))
            for i in range(num+1):
                mid = random.choice(members_dict[gid])
                attending.append((eid,mid))
        attending = list(set(attending)) #get rid of duplicates

        for item in attending:
            postgres_insert_query = "INSERT INTO Attending VALUES (\'{}\',\'{}\')".format(item[0],\
                item[1])
            cursor.execute(postgres_insert_query)
            connection.commit()

        print ("Record inserted successfully into Attending table")

        ### Requests ###
        requests = []
        # accepted ones means that the user joined the group
        for g in members_dict.keys():
            gid = g[0]
            for u in members_dict[gid]:
                uid = u[0]
                convoid = gid + uid
                requests.append((uid,gid,convoid, True))
        # generate some false requests
        ''''for i in range(100):
            uid = random.choice(users)[0]
            gid = random.choice(groups)[0]
            if uid not in members_dict[gid]:
                convoid = gid + uid
                requests.append((uid,gid,convoid, False))'''
        
        for item in requests:
            postgres_insert_query = "INSERT INTO Requests VALUES (\'{}\',\'{}\',\'{}\', {})".format(item[0],\
                item[1], item[2], item[3])
            cursor.execute(postgres_insert_query)
            connection.commit()

        print ("Record inserted successfully into Attending table for answered requests")
        
        # unanswered_requests = []
        # #generate some unanswered requests
        # for i in range(100):
        #     uid = random.choice(users)[0]
        #     gid = random.choice(groups)[0]
        #     if (uid not in members_dict[gid]) and ((uid,gid,gid+uid, False) not in requests):
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