from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
import models
import forms
import json
import datetime


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


@app.route('/get-groups', methods=['OPTIONS', 'POST'])
def return_group_meta():
	response.headers.add('Access-Control-Allow-Origin', '*')
	#returns everything related to a specific group
	try:
		members = db.session.query(models.Members).filter(models.Members.gid == request.data.get('gid'))
		members_response = [models.Members.serialize_self(member) for member in members]
	except:
		members_response = ""
		
	try:
# 		print("how you doing")
		events = db.session.query(models.Events).filter(models.Events.gid == request.data.get('gid'))
		print(events)
		events_response = [models.Events.serialize_self(event) for event in events]
	except:
		
		events_response = ""
		
	return json.dumps([members_response, events_response])
	
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
		return "Successful", 202
	except:
		return "NO MEMBER OR NO GROUP", 204
	
	return "godfad", 204

@app.route('/add-events', methods=['POST'])
def insert_new_event():

	print("why isn't anything working")
	fgid = request.data.get('gid')
	print(1)
	feventid = request.data.get('eventid')
	print(2)
	fevent_name = request.data.get('event_name')
	print(3)
	
	fhost = request.data.get('host')
	print(4)

	flocation = request.data.get('location')
	print(5)

	fe_date = request.data.get('e_date')
	print(6)

	fe_time = request.data.get('e_time')
	print(7)

	fpublic_or_private = request.data.get('public_or_private')
	print("check1")
	date_time_str = fe_date + " " + fe_time
# 	date_time_str = '2018-06-29 08:15:27.243860'
	date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
	print("check2")
# 	print('Date:', date_time_obj.date())
	fe_date = date_time_obj.date()
	fe_time = date_time_obj.time()
# 	print('Time:', date_time_obj.time())
# 	print('Date-time:', date_time_obj)
	print("check3")
	try:
		print('begin')
		models.Events.insert(fgid, feventid, fevent_name, fhost, flocation, fe_date, fe_time, fpublic_or_private)
		return "Successful", 202
	except:
		return "NO MEMBER OR NO GROUP", 204
	
	return "godfad", 204

	

# @app.route('/drinker/<name>')
# def drinker(name):
#     drinker = db.session.query(models.Drinker)\
#         .filter(models.Drinker.name == name).one()
#     return render_template('drinker.html', drinker=drinker)

# @app.route('/edit-drinker/<name>', methods=['GET', 'POST'])
# def edit_drinker(name):
#     drinker = db.session.query(models.Drinker)\
#         .filter(models.Drinker.name == name).one()
#     beers = db.session.query(models.Beer).all()
#     bars = db.session.query(models.Bar).all()
#     form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
#     if form.validate_on_submit():
#         try:
#             form.errors.pop('database', None)
#             models.Drinker.edit(name, form.name.data, form.address.data,
#                                 form.get_beers_liked(), form.get_bars_frequented())
#             return redirect(url_for('drinker', name=form.name.data))
#         except BaseException as e:
#             form.errors['database'] = str(e)
#             return render_template('edit-drinker.html', drinker=drinker, form=form)
#     else:
#         return render_template('edit-drinker.html', drinker=drinker, form=form)

# @app.template_filter('pluralize')
# def pluralize(number, singular='', plural='s'):
#     return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
