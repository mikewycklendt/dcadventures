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
from models import setup_db, Ability, Defense, Damage, ConflictAction, DamageType, Modifier, Descriptor, SkillAlt, Origin, Source, Medium, PowerDes, MediumType, MediumSubType, Range, Power, Emotion, Extra, Complex, Ground, Action, Skill, SkillType, Check, Material, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck 
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponCat, WeaponType, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from tables import tables
from skills import skills
from powers import powers
from advantage import advantage
from equipment import equip
from weapons import weap
from armor import arm
from vehicles import vehicle
from headquarters import head
from dotenv import load_dotenv
from base_files import sidebar, stylesheets, meta_name, meta_content, title

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
app.register_blueprint(advantage)
app.register_blueprint(equip)
app.register_blueprint(weap)
app.register_blueprint(arm)
app.register_blueprint(vehicle)
app.register_blueprint(head)
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def home(sidebar=sidebar, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, title=title):
	includehtml = 'home.html'

	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)


@app.route('/headquarters_traits/create')
def headquarters_traits_create():

	name = 'Awesome'
	size = 6

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()
	name = 'Colossal'
	size = 5

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Gargantuan'
	size = 4

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Huge'
	size = 3

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Large'
	size = 2

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Medium'
	size = 1

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Small'
	size = 0

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Tiny'
	size = -1

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Diminutive'
	size = -2

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Fine'
	size = -3

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Miniscule'
	size = -4

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()


	results = HeadSize.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.size)

	return ('headquarters sizes added')
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