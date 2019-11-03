import psycopg2
import random

def populate_ruser():
    try:
        connection = psycopg2.connect(dbname = "justforplay")

        cursor = connection.cursor()
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
                postgres_insert_query = "INSERT INTO ruser VALUES (\"{}\",\"{}\",\"{}\",\"{}\",{})".format(item[0],\
                    item[1], item[2], item[3], item[4])
                cursor.execute(postgres_insert_query)
                connection.commit()
                count = cursor.rowcount

        print (count, "Record inserted successfully into mobile table")

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
    populate_ruser()
