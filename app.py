from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
import models
import forms
import json

app = FlaskAPI(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

# @app.route('/')
# def all_drinkers():
#     drinkers = db.session.query(models.Drinker).all()
#     return render_template('all-drinkers.html', drinkers=drinkers)

@app.route('/login', methods=['POST'])
def check_login():
	
	user = db.session.query(models.User).filter(and_(models.User.uid == str(request.data.get('uid')), \
						    models.User.password == str(request.data.get('password')))).one()
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
