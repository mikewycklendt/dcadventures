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

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc'
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)

def decRound(value):
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

def divide(value1, value2):
	value = Decimal(value1) / Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

def multiply(value1, value2):
	value = Decimal(value1) * Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

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

	table = Measurement.query.all()

	return render_template('measurements.html', table=table, title=title, size=size)

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

@app.route('/measurements/create')
def measurements_create():

	rank = -5
	mass = Decimal(1.5)
	mass_unit = 'Pounds'
	time = divide(1, 8)
	time_unit = 'Seconds'
	distance = 6
	distance_unit = 'Inches'
	volume = divide(1, 32)
	volume_unit = 'Cubic Feet'

	print (mass)
	print (time)
	print (volume)

	
	entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
	db.session.add(entry)
	db.session.commit()

	distance = 1

	for i in range(-5, 30, 1):
		rank = i + 1
		mass = mass * 2
		mass_unit = 'Pounds'
		time = multiply(time, 2)
		time_unit = 'Seconds'
		distance = multiply(distance, 2)
		distance_unit = 'feet'
		volume = multiply(volume, 2)
		volume_unit = 'Cubic Feet'

		if rank == 7:
			mass = 3
	
		if 6 < rank < 17:
			mass_unit = 'Tons'

		if rank == 17:
			mass == Decimal(3.2)

		if 17 < rank:
			mass_unit = 'Kilotons'

		if rank == -2:
			time = 1

		if -1 < rank < 3: 
			time_unit = 'Seconds'

		if rank == 3:
			time = 1

		if 2 < rank < 9:
			time_unit = 'minutes'

		if rank == 9:
			time = 1

		if 8 < rank < 14:
			time_unit = 'Hours'

		if rank == 14:
			time = 1

		if 13 < rank < 17:	
			time_unit = 'Days'

		if rank == 17:
			time = 1

		if 16 < rank < 19:
			time_unit = 'Weeks'

		if rank == 19:
			time = 1

		if 18 < rank < 23:
			time_unit = 'Months'
			
		if rank == 23:
			time == Decimal(1.5)

		if 22 < rank:
			time_unit = 'Years'

		if rank == 6:
			distance == Decimal(l.5)

		if rank > 5:
			distance_unit = 'Miles'

	'''
		entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
		db.session.add(entry)
		db.session.commit()

	results = Measurement.query.all()

	for result in results:
		print (result.rank)
	'''
	return ('measurements added')
		
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)