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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, Material, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck 
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




@app.route('/materials/create')
def materials_create():

	materials = []

	materials.append({
		'name': 'Paper',
		'toughness': 0
	})
	
	materials.append({
		'name': 'Soil',
		'toughness': 0
	})

	
	materials.append({
		'name': 'Glass',
		'toughness': 1
	})

	materials.append({
		'name': 'Ice',
		'toughness': 1
	})
	
	materials.append({
		'name': 'Rope',
		'toughness': 1
	})
	
	materials.append({
		'name': 'Wood',
		'toughness': 3
	})

	materials.append({
		'name': 'Stone',
		'toughness': 5
	})
	
	materials.append({
		'name': 'Iron',
		'toughness': 7
	})
	
	materials.append({
		'name': 'Reinforced Concrete',
		'toughness': 8
	})
	
	materials.append({
		'name': 'Steel',
		'toughness': 9
	})
	
	materials.append({
		'name': 'Titanium',
		'toughness': 15
	})
	
	materials.append({
		'name': 'Promedtheum',
		'toughness': 20
	})

	for material in materials:
		name = material['name']
		toughness = material['toughness']

		entry = Material(name=name, toughness=toughness)
		db.session.add(entry)
		db.session.commit()

	return ('materials created')

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