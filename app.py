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
from models import setup_db, Ability, Defense, Modifier, Action
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

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)



'''
@app.route('/debilitated/create')
def debilitated_create():

	entries = []

	entries.append({
		'name': 'Debilitated ',
		'effects': 
		'condition_id': 
		'actions':
		'controlled':
		'ability_id': 
		})
'''

@app.route('/action/create')
def action_create():

	actions = []

	actions.append({
		'name': 'Multiple Actions',
		'cost': True,
		'turn': True,
		'description': 'This kind of action takes more than one standard action and may take up multiple turns.'	
		})

	for action in actions:
		name = action['name']
		cost = action['cost']
		turn = action['turn']
		description= action['description']

		entry = Action(name=name, cost=cost, turn=turn, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Action.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.cost)
		print (result.turn)
		print (result.description)

	return ('Actions Added')

'''

@app.route('/skills/create')
def skills_create():

	skills = []

	skills.append({
		'name': 'Acrobatics',
		'ability_id': 3,
		'untrained': False,
		'action_id': 1,
		'description': ''
		})

	skills.append({
		'name': 'Athletics',
		'ability_id': 1,
		'untrained': True,
		'action_id': 2,
		'description': ''
		})

	skills.append({
		'name': 'Close Combat',
		'ability_id': 5,
		'untrained': True,
		'action_id': 1,
		'description': ''
		})

	skills.append({
		'name': 'Deception',
		'ability_id': 8,
		'untrained': True,
		'action_id': 1,
		'description': ''
		})

	skills.append({
		'name': 'Expertise',
		'ability_id': 6,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

'''




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)