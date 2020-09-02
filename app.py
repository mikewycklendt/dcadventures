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

@app.route('/skills/create')
def skills_create():

	skills = []

	skills.append({
		'name': '',
		'ability_id': ,
		'untrained': ,
		'action_id':
		'description': ''
		})

@app.route('/action/create')
def action_create():

	actions = []

	actions.append({
		'name': 'Standard Action',
		'cost': True,
		'turn': True,
		'description': 'A standard action generally involves acting upon something, whether it’s an attack or using a power to affect something. You’re limited to one standard action each round.'	
		})

	actions.append({
		'name': 'Move Action',
		'cost': True,
		'turn': True,
		'description': 'A move action, like the name implies, usually involves moving. You can take your move action before or afteryour standard action, so you can attack then move, or move then attack. You cannot, however, normally split-up your move action before and after your standard action. Move actions also include things like drawing weapons, standing up, and picking up or manipulating objects.'	
		})

	actions.append({
		'name': 'Free Action',
		'cost': False,
		'turn': True,
		'description': 'A free action is something so comparatively minor it doesn’t take significant time, so you can perform as many free actions in a round as the GM considers reasonable. Free actions include things like talking (heroes and villains always find time to say a lot in the middle of a fight), dropping something, ending the use of a power, activating or maintaining some other powers, and so forth.'	
		})

	actions.append({
		'name': 'Reaction',
		'cost': False,
		'turn': False,
		'description': 'A reaction is something you do in response to something else. A reaction doesn’t take any significant time, like a free action. The difference is you react in response to something else happening during the round, perhaps not even on your turn. Reactions don’t count against your normal allotment of actions and you can react as often as the circumstances dictate, but only when they dictate.'	
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


@app.route('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)