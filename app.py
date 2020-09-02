import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from datetime import datetime
from models import setup_db, Ability, Defense, Modifier
import sys

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc'
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
	stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}]
	includehtml = 'home.html'
	title = 'DC Adventures Online Roleplqying Game'
	stylesheets.append({"style": "/static/css/home.css"})
	meta_name="DC Adventures Online"
	meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content)

@app.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h2' 
	table = Ability.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/defense')
def defense():

	title = 'Defense'
	size = 'h2'
	table = Defense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/modifiers')
def modifiers():

	title = 'Modifiers'
	
	size = 'h3'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/modifierid')
def modifierid():
	
	modifier_id = 4
	'''
	entries = [1, 2, 3, 4, 5, 6, 7, 8]
	for row in table:
		for entry in entries:
			if row.id != entry:
				db.session.delete(row)
				db.session.commit()
				db.session.close()
	'''
	

	todelete = list(range(1, 6))

	print(todelete)
	
	for itemid in todelete:
		item = db.session.query(Defense).filter_by(id=itemid).one()
		db.session.delete(item)
		db.session.commit()
		db.session.close()
	
	table = Defense.query.all()

	for row in table:
		print(row.id)
		print(row.name)
		print(row.modifier_id)

	return (str(modifier_id))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)