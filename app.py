from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
import models
import forms
import json
import datetime
from random import choice
from string import ascii_uppercase

app = FlaskAPI(__name__)
CORS(app)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

# @app.route('/')
# def all_drinkers():
#     drinkers = db.session.query(models.Drinker).all()
#     return render_template('all-drinkers.html', drinkers=drinkers)

@app.route('/login', methods=['POST'])
def check_login():
	try:
		user = db.session.query(models.User).filter(models.User.uid == str(request.data.get('uid')))\
						.filter(models.User.password == str(request.data.get('password'))).one()
		print(user)
		print(user.uid)
		if not user:
			return "Wrong Password and Username"
		dict_groups = models.User.get_groups(user.uid)
	# 	print(dict_groups)

		user_info = models.User.serialize_self(user)
	# 	print(user_info)

		if not dict_groups:
			return "no groups currently"
		return json.dumps([user_info, dict_groups])
	except:
		return "", 204


@app.route('/get-group', methods=['OPTIONS', 'POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def return_group_meta():
	#returns everything related to a specific group
	fuid = request.data.get('uid')
	fgid = request.data.get('gid')
	try:
		members = db.session.query(models.Members).filter(models.Members.gid == fgid)
		members_response = [models.Members.serialize_self(member) for member in members]
	except:
		members_response = []
		
	try:
# 		print("how you doing")
		events = db.session.query(models.Events).filter(models.Events.gid == fgid).filter(models.Events.e_date > datetime.date.today())
		print(events)
		events_response = [models.Events.serialize_self(event) for event in events]
	except:
		events_response = []

	attended_events = []
	try:
		for event in events_response:
			if (db.session.query(models.Attending).\
				filter(models.Attending.uid == fuid).filter(models.Attending.eventid == event['eventid']).count() >= 1):
				attended_events.append(event['eventid'])
	except:
		attended_events = []

	# except:
	# 	member_in_events = ""
		
	return json.dumps([members_response, events_response, attended_events])
	
@app.route('/add-member', methods=['POST'])
def insert_new_member():
	#say that he gives me uid and gid and if he is an admin or not? ok dope
	fuid = request.data.get('uid')
	fgid = request.data.get('gid')
	fadmin = request.data.get('admin')
	if not fadmin:
		fadmin = False
	print(fuid, fgid)
	try:
		print('begin')
		models.Members.insert(fuid, fgid, fadmin)
		return "Successful", 200
	except:
		return "NO MEMBER OR NO GROUP", 204
	
	return "godfad", 204

@app.route('/add-event', methods=['POST'])
def insert_new_event():

# 	print("why isn't anything working")
	fgid = request.data.get('gid')
# 	print(1) /
	feventid = ''.join(choice(ascii_uppercase) for i in range(5))
# 	print(2)
	fevent_name = request.data.get('event_name')
# 	print(3)
	
	fhost = request.data.get('host')
# 	print(4)

	flocation = request.data.get('location')
# 	print(5)

	fe_date = request.data.get('e_date')
# 	print(6)

	fe_time = request.data.get('e_time')
# 	print(7)

	fpublic_or_private = request.data.get('public_or_private')
# 	print("check1")
	date_time_str = fe_date + " " + fe_time
# 	date_time_str = '2018-06-29 08:15:27.243860'
	date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
# 	print("check2")
# 	print('Date:', date_time_obj.date())
	fe_date = date_time_obj.date()
	fe_time = date_time_obj.time()
# 	print('Time:', date_time_obj.time())
# 	print('Date-time:', date_time_obj)
# 	print("check3")
	try:
# 		print('begin')
		models.Events.insert(fgid, feventid, fevent_name, fhost, flocation, fe_date, fe_time, fpublic_or_private)
		return "Successful", 200
	except:
		return "NO MEMBER OR NO GROUP", 204
	
	return "godfad", 204
@app.route('/add-group', methods=['POST'])
def insert_new_group():
	fuid = request.data.get('uid')
	fadmin = request.data.get('admin')
	
	gid = ''.join(choice(ascii_uppercase) for i in range(5))
	group_name = request.data.get('group_name')
	community = request.data.get('community')
	zip_code = request.data.get('zip_code')
	public_or_private = request.data.get('public_or_private')
	description = request.data.get('description')
	
	
	try:
		models.Groups.insert(gid, group_name, community, zip_code, public_or_private, description)
		models.Members.insert(fuid, gid, fadmin)
		
		return "Successful Insertion into Group Table", 200
	except:
		return "WRONG INPUT", 204
	

@app.route('/add-user', methods=['POST'])
def insert_new_user():
	fuid = request.data.get('uid')
	fname = request.data.get('name')
	fpassword = request.data.get('password')
	fbio = request.data.get('bio')
	fzip_code = request.data.get('zip_code')

	try:
		models.User.insert(fuid, fname, fpassword, fbio, fzip_code)
		return "Successful Insertion into User Table", 200
	except:
		return "WRONG INPUT", 204


@app.route('/del-member', methods=['POST'])
def delete_member():
	fuid = request.data.get('uid')
	fgid = request.data.get('gid')


	try:
		models.Members.delete(fuid,fgid)
		return "Successful Deletion from Members Table", 200
	except:
		return "WRONG DELETION", 204

@app.route('/add-attending', methods=['POST'])
def add_member_atending():
	fuid = request.data.get('uid')
	feventid = request.data.get('eventid')

	try:
		models.Attending.insert(feventid, fuid)
		updated_events = db.session.query(models.Attending).filter(models.Attending.uid == fuid)
		UE = [models.Events.serialize_self(event)['eventid'] for event in updated_events]
		return json.dumps([UE]),200
	except:
		return "WRONG INSERTION", 204


@app.route('/del-attending', methods=['POST'])
def del_member_attending():
	fuid = request.data.get('uid')
	feventid = request.data.get('eventid')

	try:
		models.Attending.delete(feventid, fuid)
		updated_events = db.session.query(models.Attending).filter(models.Attending.uid == fuid)
		UE = [models.Events.serialize_self(event)['eventid'] for event in updated_events]
		return json.dumps([UE]), 200
	except:
		return "WRONG DELETION", 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
