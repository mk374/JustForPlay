
--example, selecting all the groups that Ballistic Ben is a member of; 1 represents an email that will change
--depending on the user logged in
select Groups.gid, group_name, description from groups, members where 'Marge7' = Members.uid and Members.gid = Groups.gid;

--example, selecting all the messages from the group ordered by time
select txt from messages where '16Animals16' = gid order by m_date, m_time asc;

--example selecting all events for a given group
select * from events where '13Philanthropy13' = gid;

--selecting all members in a given group
select * from members where '69Crafts69' = gid;

--example query for displaying groups within a given distance
select gid, group_name, Zip.zip_code, description
from groups, (select latitude, longitude from Zip where 27708 = zip_code) as C, Zip
where communityid = 'Nightlife' and
 (2 * 3961 * asin(sqrt((sin(radians((C.latitude - Zip.latitude) / 2))) ^ 2
+ cos(radians(Zip.latitude)) * cos(radians(C.latitude)) * (sin(radians((C.longitude - Zip.longitude) / 2))) ^ 2))) < 0.01
and groups.public_or_private = 'public';

--example for selecting communities (when the user searches for music)
select * from community where communityid = 'Music';
