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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from decimal import *
import sys

from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)

def decRound(value):
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def divide(value1, value2):
	value = Decimal(value1) / Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def multiply(value1, value2):
	value = Decimal(value1) * Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

def measure(measurements):

	for measurement in measurements:
		mass = measurement['mass']
		time = measurement['time']
		distance = measurement['distance']
		volume = measurement['volume']

		measurement['mass'] = Decimal(mass).quantize(Decimal('.01'))
		measurement['time'] = Decimal(time).quantize(Decimal('.01'))
		measurement['distance'] = Decimal(distance).quantize(Decimal('.01'))
		measurement['volume'] = Decimal(volume).quantize(Decimal('.01'))

	print (measurements)

	return measurements

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
	size = 'h1' 
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
	
	size = 'h1'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skills')
def skills():

	title = 'Skills'
	
	size = 'h1'

	table = Skill.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skill/type')
def skill_type():

	title = 'Skill Type'
	
	size = 'h1'

	table = SkillType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/checks')
def checks():

	title = 'Check Types'
	
	size = 'h1'

	table = Check.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/conditions')
def conditions():

	title = 'Basic Conditions'
	
	size = 'h1'

	table = Condition.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/phases')
def phases():

	title = 'Phases'
	
	size = 'h1'

	table = Phase.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/senses')
def senses():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measurements')
def measurements():

	title = 'Measurements Table'
	
	size = 'h3'

	measurements = Measurement.query.all()

	formatted = [measurement.format() for measurement in measurements]
	
	print (formatted)

	table = measure(formatted)

	return render_template('measurements.html', table=table, title=title, size=size)


@app.route('/modifier')
def modifiers_create():
	modifiers = []

	modifiers.append({'name': 'Circumstance Modifiers',
						'cost': None,
						'description': 'Some circumstances make checks easier or harder, resulting in a bonus or penalty to the check. Characters in a favorable situation are said to have a circumstance bonus for the check, while those in a disadvantageous situation are said to have a circumstance penalty. \n\n Some circumstances make checks easier or harder, resulting in a bonus or penalty to the check. Characters in a favorable situation are said to have a circumstance bonus or the check, while those in a disadvantageous situation are said to have a circumstance penalty. \n\n UNDER THE HOOD: CIRCUMSTANCES \n\n 	Circumstance modifiers are another useful Gamemaster tool for handling a lot of the variables that come up during game play. Specific examples are discussed throughout the rules for various types of checks. One example includes the following: \n\n TOOLS \n\n Some tasks require tools. If tools are needed, the specific items are mentioned in the description of the task or skill. If you don’t have the appropriate tools, you may still be able to attempt the task, but at a major disadvantage, for a –5 circumstance penalty on your check, if the GM decides you can attempt the task at all. A character may be able to put together makeshift tools in order to make the check. If the GM allows this, reduce the circumstance penalty to –2.',
						'table': True
		})

	for modifier in modifiers:
		name = modifier['name']
		cost = modifier['cost']
		description = modifier['description']
		table = modifier['table']

		entry = Modifier(name=name, cost=cost, description=description, table=table)
		db.session.add(entry)
		db.session.commit()

	added = Modifier.query.all()

	for add in added:
		modifier_id = add.id
		name = add.name

		print(modifier_id)
		print(name)


	return ('modifiers')
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


	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)