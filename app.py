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
@app.route('/skills/type')
def skill_type_create():

	types = []

	types.append({
		'name': 'Interaction',
		'check_id': 2,
		'group': True,
		'team': False,
		'gm': True,
		'description': 'Certain skills, called interaction skills, are aimed at dealing with others through social interaction. Interaction skills allow you to influence the attitudes of others and get them to cooperate with you in one way or another. Since interaction skills are intended for dealing with others socially, they have certain requirements.\n\n First, you must be able to interact with the subject(s) of the skill. They must be aware of you and able to understand you. If they can’t hear or understand you for some reason, you have a –5 circumstance penalty to your skill check (see Circumstance Modifiers in The Basics). \n\n Interaction skills work best on intelligent subjects, ones with an Intellect rank of –4 or better. You can use them on creatures with Int –5, but again with a –5 circumstance penalty; they’re just too dumb to get the subtleties of your point. You can’t use interaction skills at all on subjects lacking one or more mental abilities. (Try convincing a rock to be your friend—or afraid of you—sometime.) The Immunity effect (see the Powers chapter) can also render characters immune to interaction skills. \n\n You can use interaction skills on groups of subjects at once, but only to achieve the same result for everyone. So you can attempt to use Deception or Persuasion toconvince a group of something, or Intimidation to cow a crowd, for example, but you can’t convince some individuals of one thing and the rest of another, or intimidate some and not others. The GM decides if a particular use of an interaction skill is effective against a group, and may apply modifiers depending on the situation. The general rules for interaction still apply: everyone in the group must be able to hear and understand you, for example, or you suffer a –5 on your skill check against them. Mindless subjects are unaffected, as usual.' 
	})

	types.append({
		'name': 'Manipulation',
		'check_id': 1,
		'group': False,
		'team': True,
		'gm': True,
		'description': 'Some skills, called manipulation skills, require a degree of fine physical manipulation. You need prehensile limbs and a Strength rank or some suitable Precise power effect to use manipulation skills effectively. If your physical manipulation capabilities are impaired in some fashion (such as having your hands tied or full use of only one hand), the GM may impose a circumstance modifier based on the severity of the impairment. Characters lacking the ability to use manipulation skills can still have ranks in them and use them to oversee or assist the work of others (see Team Checks,'
	})
 
	for skill in types:
		name = skill['name']
		check_id = skill['check_id']
		group = skill['group']
		team = skill['team']
		gm = skill['gm']
		description = skill['description']

		entry = SkillType(name=name, check_id=check_id, group=group, team=team, gm=gm, description=description)
		db.session.add(entry)
		db.session.commit()

	results = SkillType.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.description)

	return ('skill types added')



	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)