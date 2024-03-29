from sqlalchemy import sql, orm
from app import db
import datetime

class Zip(db.Model):
	__tablename__ = 'zip'
	zip_code = db.Column('zip_code', db.SmallInteger, primary_key =True)
	latitude = db.Column('latitude', db.Float(), nullable=False)
	longitude = db.Column('longitude', db.Float(), nullable=False)
	

class User(db.Model):
	__tablename__ = 'ruser'
	uid = db.Column('uid', db.String(256), primary_key=True, nullable=False)
	name = db.Column('name', db.String(64), primary_key=False, nullable=False)
	password = db.Column('password', db.String(64), primary_key=False, nullable=False)
	bio = db.Column('bio', db.String(1024), primary_key=False, nullable=False)
	zip_code = db.Column('zip_code', db.SmallInteger, db.ForeignKey('zip.zip_code'), nullable=False,) 

	
	def serialize_self(user):
		dictionary = {
			'uid': user.uid,
			'name': user.name,
			'password': user.password,
			'bio': user.bio,
			'zip_code': user.zip_code
		}
		return dictionary
	def get_groups(user_id):
		try:
			query = """select groups.gid, groups.group_name, groups.community, 
					groups.zip_code, groups.public_or_private, groups.description
					from groups, members where groups.gid = members.gid and members.uid = :uid"""
			
			groups = db.session.execute(query, dict(uid=user_id))
			
			def serialize(_gid, _group_name, _community, _zip_code, _public_or_private, _description):
				dictionary = {
					'gid': _gid,
					'group_name': _group_name,
					'community': _community,
					'zip_code': _zip_code,
					'public_or_private': _public_or_private,
					'description': _description
				}
				return dictionary
			
			list_dict_groups = [serialize(g.gid, g.group_name, g.community, g.zip_code, \
							g.public_or_private, g.description) for g in groups]
			return list_dict_groups
		except Exception as e:
			print(e)
			db.session.rollback()
			raise e
	
	def insert(uid, name, password, bio, zip_code):
		try:
			dictionary = {
				'uid': uid,
				'name': name,
				'password': password,
				'bio': bio,
				'zip_code': zip_code
			}

			db.session.execute('INSERT INTO ruser VALUES (:uid, :name, :password, :bio, :zip_code)', dictionary)
			db.session.commit()

		except Exception as e:
			print(e)
			db.session.rollback()
			raise e
	def query(uid):
		try:
			dictionary = {
				'uid': uid
			}

			query = "SELECT * FROM ruser WHERE uid = :uid"
			users = db.session.execute(query, dictionary)

			return [(user.uid, user.name, user.password, user.bio, user.zip_code) for user in users]
		except Exception as e:
			db.session.rollback()
			raise e
		
			
#     #something about orm. https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
# class Community(db.Model):
# 	__tablename__ = 'community'
# 	communityid = db.Column('communityid', db.String(256), primary_key=True, nullable=False)
# 	description = db.Column('description', db.String(1000), nullable=False)
	
# class SubCommunity(db.Model):
# 	__tablename__ = 'subcommunity'
# 	communityid = db.Column('communityid', db.String(256), db.ForeignKey('community.communityid'), nullable=False)
# 	subid = db.Column('subid', db.String(256))
# 	sub_description = db.Column('sub_description', db.String(1000), nullable=False)
# 	__table_args__ = (db.PrimaryKeyConstraint(communityid, subid), {})
	
	
class Groups(db.Model):
	__tablename__ = 'groups'
	gid = db.Column('gid', db.String(256), nullable=False)
	group_name = db.Column('group_name', db.String(256), nullable=False)
	community = db.Column('communityid', db.String(256))
	zip_code = db.Column('zip_code', db.SmallInteger, db.ForeignKey('zip.zip_code'), nullable=False)
	public_or_private = db.Column('public_or_private', db.String(32))
	description = db.Column('description', db.String(1024))
	__table_args__ = (db.PrimaryKeyConstraint(gid), \
			  db.CheckConstraint(public_or_private in ('private', 'public')),
			  {})
	
	def insert(fgid, fgroup_name, fcommunity, fzip_code, fpublic_or_private, fdescription):
		try:
			dictionary = {
				'gid': fgid,
				'group_name': fgroup_name,
				'community': fcommunity,
				'zip_code': fzip_code,
				'public_or_private': fpublic_or_private,
				'description': fdescription
			}
			db.session.execute('INSERT INTO Groups Values(:gid, :group_name, :community, :zip_code, :public_or_private, :description)', \
					   dictionary)
			db.session.commit()
			
		except Exception as e:
			db.session.rollback()
			raise e



	def query(identifier, zip_code):
		try: 
			dic = {
				'zip_code': zip_code,
				'iden': '%' + identifier + '%'
			}
			query = """select gid, group_name, community, groups.zip_code, public_or_private, description from groups, 
			(select latitude, longitude from Zip where zip_code = :zip_code) as C, Zip where  
			(2 * 3961 * asin(sqrt((sin(radians((C.latitude - Zip.latitude) / 2))) ^ 2 + 
			cos(radians(Zip.latitude)) * cos(radians(C.latitude)) * (sin(radians((C.longitude - Zip.longitude) / 2))) ^ 2))) < 10
			and (group_name like :iden or community like :iden) and groups.zip_code = Zip.zip_code limit 10
			"""

			
			groups = db.session.execute(query, dic)
			# print(len(groups))
			def serialize(group):
				dictionary = {
					'gid': group.gid,
					'group_name': group.group_name,
					'community': group.community,
					'zip_code': group.zip_code,
					'public_or_private': group.public_or_private,
					'description': group.description
				}
				return dictionary

			# return [serialize(group)
			# 	for group in groups if dic['iden'] in group.group_name or dic['iden'] in group.community]
			return [serialize(group) for group in groups]
			
		except Exception as e:
			print(e)
			db.session.rollback()
			raise e
			
	def second_query(gid):
		try:
			dic = {
				'gid': gid
			}

			query = "SELECT * FROM GROUPS WHERE gid = :gid"

			groups = db.session.execute(query, dic)
			return [(group.gid, group.group_name, group.community, group.zip_code, group.public_or_private, group.description)\
				for group in groups]

		except Exception as e:
			db.session.rollback()
			raise e


class Members(db.Model):
	__tablename__ = 'members'
	uid = db.Column('uid', db.String(256), db.ForeignKey('ruser.uid'), nullable=False)
	gid = db.Column('gid', db.String(256), db.ForeignKey('groups.gid'), nullable=False)
	admin = db.Column('admin', db.Boolean)
	__table_args__ = (db.PrimaryKeyConstraint(uid, gid), {})
	
	
	def serialize_self(member):
		dictionary = {
			'uid': member.uid,
			'gid': member.gid,
			'admin': member.admin
		}
		return dictionary
	
	
	def insert(fuid, fgid, fadmin=None):
		try:
			db.session.execute('INSERT INTO Members VALUES (:uid, :gid, :admin)', dict(uid=fuid, gid=fgid, admin=fadmin))
			db.session.commit()
			print("sucessful")
		except Exception as e:
			db.session.rollback()
			raise e

	def delete(uid, gid):
		dictionary = {
			'uid': uid,
			'gid': gid
		}
		try:
			db.session.execute('DELETE FROM Members WHERE uid = :uid AND gid = :gid', dictionary)
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
			raise e

	def query(uid, gid):
		try:
			dictionary = {
				'uid': uid,
				'gid': gid
			}
			query = "SELECT * FROM Members WHERE uid = :uid and gid = :gid"
			members = db.session.execute(query, dic)

			return [(member.uid, member.gid, member.admin) for member in members]

		except Exception as e:
			db.session.rollback()
			raise e

class Events(db.Model):
	__tablename__ = 'events'
	gid = db.Column('gid', db.String(256), db.ForeignKey('groups.gid'), nullable=False)
	eventid = db.Column('eventid', db.String(256), nullable=False)
	event_name = db.Column('event_name', db.String(512), nullable=False)
	host = db.Column('host', db.String(256), nullable=False)
	location = db.Column('location', db.String(256), nullable=False)
	e_date = db.Column('e_date', db.Date, nullable=False)
	e_time = db.Column('e_time', db.DateTime, nullable=False)
	public_or_private = db.Column('public_or_private', db.String(32))
	__table_args__ = (db.PrimaryKeyConstraint(gid, eventid), \
			  db.CheckConstraint(public_or_private in ('private', 'public')),
			  {})
	
	def serialize_self(event):
		dictionary = {
			'gid': event.gid,
			'eventid': event.eventid,
			'event_name': event.event_name,
			'host': event.host,
			'location': event.location,
			'e_date': event.e_date.strftime("%Y-%m-%d"),
			'e_time': event.e_time.strftime("%H:%M"),
			'public_or_private': event.public_or_private
		}
		return dictionary
	
	def insert(gid, eventid, event_name, host, location, e_date, e_time, public_or_private):
		try:
			dictionary = {
				'gid': gid,
				'eventid': eventid,
				'event_name': event_name,
				'host': host,
				'location': location,
				'e_date': e_date,
				'e_time': e_time,
				'public_or_private': public_or_private
			}
			db.session.execute('INSERT INTO Events VALUES (:gid, :eventid, :event_name, :host, :location, :e_date, :e_time, :public_or_private)', \
					   dictionary)
			db.session.commit()
			print("sucessful")
		except Exception as e:
			db.session.rollback()
			raise e

	def query(gid):
		try:
			dictionary = {
				'gid':gid
			}
			all_events = db.session.execute('SELECT * FROM Events WHERE gid = :gid', dictionary)
			db.session.commit()

			all_events = [(event.gid, event.event_name, event.host, event.location, event.e_date, event.e_time, event.public_or_private)\
				for event in all_events]
			
			return all_events
		except Exception as e:
			db.session.rollback()
			raise e



class Attending(db.Model):
	__tablename__ = 'attending'
	eventid = db.Column('eventid', db.String(256), db.ForeignKey('events.eventid'), nullable=False)
	uid = db.Column('uid', db.String(256), db.ForeignKey('ruser.uid'), nullable = False)
	__table_args__ = (db.PrimaryKeyConstraint(eventid, uid), {})
	

	def insert(eventid, uid):
		try:
			dictionary = {
				'eventid': eventid,
				'uid': uid
			}

			db.session.execute('INSERT INTO Attending VALUES (:eventid, :uid)', dictionary)
			db.session.commit()
		except Exception as e:
			db.session.rollback()
			raise e

	def delete(eventid, uid):
		try:
			dictionary = {
				'eventid': eventid,
				'uid': uid
			}
			db.session.execute('DELETE FROM Attending WHERE eventid = :eventid and uid = :uid', dictionary)

			db.session.commit()
		except Exception as e:
			db.session.rollback()
			raise e

	def query(uid):
		try:
			dictionary = {
				'uid': uid
			}

			events = db.session.execute('SELECT * FROM Attending WHERE uid = :uid', dictionary)


			print("welp at least that worked")
			UE = [event.eventid for event in events]
			print(UE)
			return UE
		except Exception as e:
			db.session.rollback()
			raise e
		



   
# class Drinker(db.Model):
#     __tablename__ = 'drinker'
#     name = db.Column('name', db.String(20), primary_key=True)
#     address = db.Column('address', db.String(20))
#     likes = orm.relationship('Likes')
#     frequents = orm.relationship('Frequents')
#     @staticmethod
#     def edit(old_name, name, address, beers_liked, bars_frequented):
#         try:
#             db.session.execute('DELETE FROM likes WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('DELETE FROM frequents WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('UPDATE drinker SET name = :name, address = :address'
#                                ' WHERE name = :old_name',
#                                dict(old_name=old_name, name=name, address=address))
#             for beer in beers_liked:
#                 db.session.execute('INSERT INTO likes VALUES(:drinker, :beer)',
#                                    dict(drinker=name, beer=beer))
#             for bar, times_a_week in bars_frequented:
#                 db.session.execute('INSERT INTO frequents'
#                                    ' VALUES(:drinker, :bar, :times_a_week)',
#                                    dict(drinker=name, bar=bar,
#                                         times_a_week=times_a_week))
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

# class Beer(db.Model):
#     __tablename__ = 'beer'
#     name = db.Column('name', db.String(20), primary_key=True)
#     brewer = db.Column('brewer', db.String(20))

# class Bar(db.Model):
#     __tablename__ = 'bar'
#     name = db.Column('name', db.String(20), primary_key=True)
#     address = db.Column('address', db.String(20))
#     serves = orm.relationship('Serves')

# class Likes(db.Model):
#     __tablename__ = 'likes'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)

# class Serves(db.Model):
#     __tablename__ = 'serves'
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)
#     price = db.Column('price', db.Float())

# class Frequents(db.Model):
#     __tablename__ = 'frequents'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     times_a_week = db.Column('times_a_week', db.Integer())
