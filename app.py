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
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv
from base_files import sidebar, stylesheets, meta_name, meta_content, title

from models import setup_db

from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from tables import tables
from skills import skill
from powers import powers
from advantage import advantage
from equipment import equip
from weapons import weap
from armor import arm
from vehicles import vehicle
from headquarters import head
from selects import select
from info_select import info
from icon_select import icon
from descriptor import descrip

load_dotenv()

import os

db_path = os.environ.get("db_path")

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.register_blueprint(tables)
app.register_blueprint(skill)
app.register_blueprint(powers)
app.register_blueprint(advantage)
app.register_blueprint(equip)
app.register_blueprint(weap)
app.register_blueprint(arm)
app.register_blueprint(vehicle)
app.register_blueprint(head)
app.register_blueprint(select)
app.register_blueprint(info)
app.register_blueprint(icon)
app.register_blueprint(descrip)
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def home(sidebar=sidebar, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, title=title):
	includehtml = 'home.html'

	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)

@app.route('/nature/create')
def nature_create():

	entries = ['Ice', 'Rain', 'Snow', 'Wind']


	for i in entries:

		entry = Nature(name=i, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Nature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('nature added')

@app.route('/emotions/create')
def emotions_create():

	emotions = ['Anger', 'Fear', 'Sadness', 'Happiness', 'Surprise', 'Disgust']

	for emotion in emotions:

		entry = Emotion(name=emotion, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Emotion.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('emotions added')

@app.route('/env/create')
def env_create():

	environment = ['Underwater', 'Zero Gravity', 'Mountains', 'Jungle', 'Desert', 'Volcano', 'Space', 'Woodlands', 'Arctic']


	for i in environment:

		entry = Environment(name=i, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Environment.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('environments added')

@app.route('/job/create')
def job_create():

	entries = ['Soldier', 'Police', 'Yakuza', 'Lawyer', 'Artist', 'Business', 'Carpentry', 'Chef', 'Criminal', 'Dancer', 'Historian', 'Journalist', 'Doctor', 'Musician', 'Magiccian',  'Philosopher', 'Politician', 'Actor', 'Psychiatrist', 'Psychologist', 'Scientist', 'Sociologist', 'Gangster', 'Theologist']

	for i in entries:

		entry = Job(name=i, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Job.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('professions added')

@app.route('/creatures/create')
def creatures_create():

	entries = ['Alien', 'Animal', 'Construct', 'mETAHUMAN', 'Undead']

	for i in entries:

		entry = Creature(name=i, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Creature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('creatures added')


@app.route('/conditions/db')
def conditions_extras_create():

	name = 'All Conditions'

	entry = Condition(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current Condition'

	entry = Condition(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Condition'

	entry = Condition(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable Condition'

	entry = Condition(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No Condition'

	entry = Condition(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Linked to First Condition'

	entry = Condition(linked_first=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Linked to Second Condition'

	entry = Condition(linked_second=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Condition).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('conditions db added')

@app.route('/ability/db')
def ability_extras_create():

	tablename = 'Ability'

	name = 'All Abilities'

	entry = Ability(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Ability(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Ability(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Ability(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Ability(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Power Rank' 

	entry = Ability(power=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Skill Rank'

	entry = Ability(skill=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Extra Rank'

	entry = Ability(extra=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Ability).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')

@app.route('/check/db')
def check_db_columns_create():

	tablename = 'Check'

	name = 'All Checks'

	entry = Check(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Check(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Check(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Check(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Check(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Free ' + tablename

	entry = Check(free=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Check).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')


@app.route('/tsble/db')
def table_db_columns_create():

	tablename = 'Ability'

	name = 'All ' + tablename

	entry = Ability(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Ability(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Ability(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Ability(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Ability(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Ability).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')


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