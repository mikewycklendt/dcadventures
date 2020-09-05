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

@app.route('/abilities/create')
def abilities_create():
	abilities = []
		
	abilities.append({'name': "Strength",
		'description': ['Damage dealt by your unarmed and strength-based attacks.',
						'How far you can jump.',
						'The amount of weight you can lift, carry, and throw.',
						'Athletics skill checks.'],
		'summary': 'Strength measures sheer muscle power and the ability to apply it. Your Strength rank applies to:'})

	abilities.append({'name': "Stamina",
		'description': ['Toughness defense, for resisting damage.',
						'Fortitude defense, for resisting effects targeting your character’s health.',
						'Stamina checks to resist or recover from things af-fecting your character’s health when a specific de-fense doesn’t apply.'],
		'summary': 'Stamina is health, endurance, and overall physical resil-ience. Stamina is important because it affects a charac-ter’s ability to resist most forms of damage. Your Stamina modifier applies to:'})

	abilities.append({'name': "Agility",
		'description': ['Dodge defense, for avoiding ranged attacks and oth-er hazards.',
						'Initiative bonus, for acting first in combat.',
						'Acrobatics and Stealth skill checks.',
						'Agility checks for feats of coordination, gross move-ment, and quickness when a specific skill doesn’t apply.'],
		'summary': 'Agility is balance, grace, speed, and overall physical coor-dination. Your Agility rank applies to:'})

	abilities.append({'name': "Dexterity",
		'description': ['Attack checks for ranged attacks.',
						'Sleight of Hand and Vehicles skill checks.',
						'Dexterity checks for feats of fine control and preci-sion when a specific skill doesn’t apply.'],
		'summary': 'Dexterity is a measure of hand-eye coordination, precision, and manual dexterity. Your Dexterity rank applies to:'})
					
	abilities.append({'name': "Fighting",
		'description': ['Attack checks for close attacks.',
						'Parry defense, for avoiding close attacks'],
		'summary': 'Fighting measures your character’s ability in close com-bat, from hitting a target to ducking and weaving around any counter-attacks. Your Fighting rank applies to:'})

	abilities.append({'name': "Intellect",
		'description': ['Expertise, Investigation, Technology, and Treatment skill checks.',
						'Intellect checks to solve problems using sheer brain-power when a specific skill doesn’t apply.'],
		'summary': 'Intellect covers reasoning ability and learning. A character with a high Intellect rank tends to be knowledgeable and well educated. Your Intellect modifier applies to:'})

	abilities.append({'name': "Awareness",
		'description': ['Will defense, for resisting attacks on your mind.',
						'Insight and Perception skill checks.',
						'Awareness checks to resolve matters of intuition when a specific skill doesn’t apply.'],
		'summary': 'While Intellect covers reasoning, Awareness describes common sense and intuition, what some might call “wis-dom.” A character with a high Intellect and a low Aware-ness may be an “absent-minded professor” type, smart but not always aware of what’s going on. On the other hand, a not so bright (low Intellect) character may have a great deal of common sense (high Awareness). Your Awareness modifier applies to:'})

	abilities.append({'name': "Presence",
		'description': ['Deception, Intimidation, and Persuasion skill checks.',
						'Presence checks to influence others through force of personality when a specific skill doesn’t apply.'],
		'summary': 'Presence is force of personality, persuasiveness, leader-ship ability and (to a lesser degree) attractiveness. Pres-ence is useful for heroes who intend to be leaders as well as those who strike fear into the hearts of criminals with their presence. Your Presence modifier applies to:'})
	
	for ability in abilities:
		print (ability['name'])
		name = ability['name']
		print (ability['summary'])
		summary = ability['summary']
		description = ability['description']
		newEntry = Ability(name=name, description=description, summary=summary)
		db.session.add(newEntry)
		db.session.commit()
		for describe in description:
			print (describe)

	return ('abilities')


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