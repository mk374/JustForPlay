from sqlalchemy import sql, orm
from app import db

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
		groups = db.session.execute('select groups.gid, groups.group_name, groups.communityid, groups.subid, \
				groups.zip_code, groups.public_or_private, groups.description\
				from groups, members where groups.gid = members.gid and members.uid = :uid', dict(uid=user_id))
		
		def serialize(_gid, _group_name, _communityid, _subid, _zip_code, _public_or_private, _description):
			dictionary = {
				'gid': _gid,
				'group_name': _group_name,
				'communityid': _communityid,
				'subid': _zip_code,
				'public_or_private': _public_or_private,
				'description': _description
			}
			return dictionary
		
		list_dict_groups = [serialize(g.gid, g.group_name, g.communityid, g.subid, g.zip_code, \
					     g.public_or_private, g.description) for g in groups]
		return list_dict_groups
	

		
			
    #something about orm. https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
class Community(db.Model):
	__tablename__ = 'community'
	communityid = db.Column('communityid', db.String(256), primary_key=True, nullable=False)
	description = db.Column('description', db.String(1000), nullable=False)
	
class SubCommunity(db.Model):
	__tablename__ = 'subcommunity'
	communityid = db.Column('communityid', db.String(256), db.ForeignKey('community.communityid'), nullable=False)
	subid = db.Column('subid', db.String(256))
	sub_description = db.Column('sub_description', db.String(1000), nullable=False)
	__table_args__ = (db.PrimaryKeyConstraint(communityid, subid), {})
	
	
class Groups(db.Model):
	__tablename__ = 'groups'
	gid = db.Column('gid', db.String(256), nullable=False)
	group_name = db.Column('group_name', db.String(256), nullable=False)
	communityid = db.Column('communityid', db.String(256), db.ForeignKey('community.communityid'), nullable=False)
	subid = db.Column('subid', db.String(256), db.ForeignKey('subCommunity.subid'))
	zip_code = db.Column('zip_code', db.SmallInteger, db.ForeignKey('zip.zip_code'), nullable=False)
	public_or_private = db.Column('public_or_private', db.String(32))
	description = db.Column('description', db.String(1024))
	__table_args__ = (db.PrimaryKeyConstraint(gid, communityid), \
			  db.CheckConstraint(public_or_private in ('private', 'public')),
			  {})

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

class Events(db.Model):
	__tablename__ = 'events'
	gid = db.Column('gid', db.String(256), db.ForeignKey('groups.gid'), nullable=False)
	eventid = db.Column('eventid', db.String(256), nullable=False)
	event_name = db.Column('event_name', db.String(512), nullable=False)
	host = db.Column('host', db.String(256), nullable=False)
	location = db.Column('location', db.String(256), nullable=False)
	e_date = db.Column('e_date', db.Date, nullabe=False)
	e_time = db.Column('e_time', db.DateTime, nullable=False)
	public_or_private = db.Column('public_or_private', db.String(32))
	__table_args__ = (db.PrimaryKeyConstraint(gid, eventid), \
			  db.CheckConstraint(public_or_private in ('private', 'public')),
			  {})
	
	def serialize_self(event):
		dictionary = {
			'gid': event.gid,
			'eventid': event.uid,
			'event_name': event.event_name,
			'host': event.host,
			'location': event.location,
			'e_date': event.e_date,
			'e_time': event.e_time,
			'public_or_private': event.public_or_private
		}
		return dictionary
   
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
