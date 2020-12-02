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
from models import setup_db, Ability, Defense, Damage, DamageType, Modifier, Descriptor, Origin, Source, Medium, PowerDes, MediumType, MediumSubType, Range, Power, Emotion, Extra, Complex, Ground, Action, Skill, SkillType, Check, Material, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck 
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from tables import tables
from skills import skills
from powers import powers
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.register_blueprint(tables)
app.register_blueprint(skills)
app.register_blueprint(powers)
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def home():
	includehtml = 'home.html'

	stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
	meta_name="DC Adventures Online"
	meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
	title = 'DC Adventures Online Roleplqying Game'
	sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

	title = 'DC Adventures Online: Create a Special Skill'
	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)


@app.route('/origins/create')
def origins_create():

	origins = ['Accidental', 'Bestowed', 'Invented', 'Metahuman', 'Training']

	for i in origins:

		entry = Origin(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Origin.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('origins added')

@app.route('/sources/create')
def sources_create():

	sources = ['Biological', 'Cosmic', 'Divine', 'Extradimensional', 'Magical', 'Moral', 'Psionic', 'Technological', 'Other']

	for i in sources:

		entry = Source(name=i, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = Source.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('sources added')

@app.route('/mediumtype/create')
def mediumtype_create():

	medium = ['Material', 'Energy']

	for i in medium:
		
		entry = MediumType(name=i, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = MediumType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

@app.route('/mediumsubtype/create')
def mediumsubtypetype_create():

	materials = ['Gas', 'Liquid', 'Earth', 'Biological']

	for i in materials:

		entry = MediumSubType(name=i, medium_type=3, damage=True)
		db.session.add(entry)
		db.session.commit()

	energies = ['Electromagnetic', 'Gravity', 'Kinetic', 'Divine', 'Magical', 'Psionic', 'Cosmic']

	for i in energies:

		entry = MediumSubType(name=i, medium_type=4, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = MediumSubType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

@app.route('/medium/create')
def medium_create():

	medium_gas = ['Air']
	
	medium_liquid = ['Water']
	
	medium_earth = ['Soil', 'Rock', 'Sand']
	
	medium_biological = ['Acid', 'Blood']

	for i in medium_gas:

		entry = Medium(name=i, medium_type=3, medium_subtype=32, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_liquid:

		entry = Medium(name=i, medium_type=3, medium_subtype=33, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_earth:

		entry = Medium(name=i, medium_type=3, medium_subtype=34, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_biological:

		entry = Medium(name=i, medium_type=3, medium_subtype=35, damage=True)
		db.session.add(entry)
		db.session.commit()

	medium_electromagnetic = ['Electricity', 'Light', 'Radio', 'Radiation']

	for i in medium_electromagnetic:

		entry = Medium(name=i, medium_type=4, medium_subtype=36, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')
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
	app.secret_key = os.urandom(32)
	app.run(host='0.0.0.0', port=80)