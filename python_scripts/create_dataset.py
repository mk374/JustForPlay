import random
import pandas as pd

"""
This script creates the large sample dataset for our database.
Most of this code was originally in groups_to_messages.py.
"""

###############################
## Populating the Dataframes ##
###############################

# Users
usrs = []
names = ['Dave', 'Sammy', 'Minsoo', 'Benjamin', 'Andy', 'Abby', 'Tommy', 'Ross', 'Rachel','Joey', 'Chandler', 'Phoebe',
                'Monica', 'Bart', 'Homer', 'Marge', 'Lisa', 'Maggie']
snacks = ['crepes', 'goldfish', 'Doritos', 'waffles', 'pancakes', 'pumpkin pie']
zips = [27503, 27517, 27560, 27701, 27703, 27704, 27705, 27707, 27709, 27712, 27713]
for i in range(1000):
    rname = random.choice(names)
    ruid = rname + str(i)
    rpassword = 'password' + str(i)
    rbio = 'My name is ' + rname + ' and I like ' + random.choice(snacks) + '.'
    rzipcode = random.choice(zips)
    temp = (ruid, rname, rpassword, rbio, rzipcode)
    usrs.append(temp)
users = pd.DataFrame(data=usrs,columns=["ruid", "rname", "rpassword", "rbio", "rzipcode"])

# Communities
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

# Groups
group_names = list(community_dict.keys())
grps = []
for i in range(100):
    comm = random.choice(group_names)
    gname = comm + str(i)
    guid = str(i) + gname
    pub_or_priv = random.choice(['public', 'private'])
    gzipcode = random.choice(zips)
    description = "We like " + comm
    temp = (guid, gname, comm, gzipcode, pub_or_priv, description)
    grps.append(temp)
groups = pd.DataFrame(data=grps, columns=["guid", "gname","comm", "gzipcode", "pub_or_priv", "description"])

# Members
members_dict = {}
mems = []
for i in range(2000):
    u = random.choice(usrs)[0]
    g = random.choice(grps)[0]
    if (g in members_dict.keys() and u not in members_dict[g]) or (g not in members_dict.keys()):
        adm = random.choice([False, True, False, False])
        mems.append((u,g,adm))
        if g in members_dict.keys():
            members_dict[g].append(u)
        else:
            members_dict[g] = [u]
members = pd.DataFrame(data=mems, columns=["uid", "gid","admin"])

# Events
evnts = []
for i in range(100):
    g = random.choice(grps)
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
    evnts.append((gid,eid,ename,h,location,edt, etm, pub_or_priv))
events = pd.DataFrame(data=evnts, columns=["gid", "eventid","event_name", "host", "location", "e_date", "e_time", "public_or_private"])

# Attending
attend = []
for e in evnts:
    eid = e[1]
    gid = e[0]
    num = random.choice(range(len(members_dict[gid])))
    for i in range(num+1):
        mid = random.choice(members_dict[gid])
        attend.append((eid,mid))
attend = list(set(attend)) #get rid of duplicates
attending = pd.DataFrame(data=attend, columns=["eventid", "uid"])

# # Requests
# req = []
# # accepted ones means that the user joined the group
# for g in members_dict.keys():
#     for u in members_dict[gid]:
#         convoid = g + u
#         req.append((u,g,convoid, True))
# # generate some false requests
# for i in range(100):
#     uid = random.choice(usrs)[0]
#     gid = random.choice(grps)[0]
#     if (uid not in members_dict[gid]) and ((uid,gid) not in [(a[0],a[1]) for a in req]):
#         convoid = gid + uid
#         req.append((uid,gid,convoid, False))
# requests = pd.DataFrame(data=req, columns= ["uid", "gid", "conversationid", "accepted"])

###########################
## Writing to Excel File ##
###########################
with pd.ExcelWriter("Static_Sample_Data.xlsx") as writer:
    users.to_excel(writer, sheet_name="Users", header=True, index=False)
    groups.to_excel(writer, sheet_name="Groups", header=True, index=False)
    members.to_excel(writer, sheet_name="Members", header=True, index=False)
    events.to_excel(writer, sheet_name="Events", header=True, index=False)
    attending.to_excel(writer, sheet_name="Attending", header=True, index=False)
    writer.save()
