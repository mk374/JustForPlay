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
	zip_code = db.Column('zip_code', db.SmallInteger, nullable=False, db.ForeignKey('zip.zip_code')) 

				
    
    #something about orm. https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
class Community(db.Model):
	__tablename__ = 'community'
	communityid = db.Column('communityid', db.String(256), primary_key=True, nullable=False)
	description = db.Column('description', db.String(1000), nullable=False)
	
class SubCommunity(db.Model):
	__tablename__ = 'subcommunity'
	communityid = db.Column('communityid', db.String(256), nullable=False, db.ForeignKey('community.communityid'))
	subid = db.Column('subid', db.String(256))
	sub_description = db.Column('sub_description', db.String(1000), nullable=False)
	__table_args__ = (PrimaryKeyConstraint(communityid, subid), {})


    
    
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
