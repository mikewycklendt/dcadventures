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
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from tables import tables
from skills import skills
from powers import powers
from advantage import advantage
from equipment import equip
from weapons import weap
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
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def home(sidebar=sidebar, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, title=title):
	includehtml = 'home.html'

	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)




@app.route('/weaponcat/create')
def weaponcat_create():

	entries = ['Melee', 'Ranged', 'Grenades and Explosives', 'Accessory']

	for i in entries:

		entry = WeaponCat(name=i)
		db.session.add(entry)
		db.session.commit()

	results = WeaponCat.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('weqpon category added')


@app.route('/weapontype/create')
def weapontype_create():

	entries = ['Simple', 'Aechaic', 'Exotic']

	for i in entries:

		entry = WeaponType(name=i, type_id=1)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Projectile', 'Energy', 'Heavy', 'Thrown']

	for i in entries:

		entry = WeaponType(name=i, type_id=2)
		db.session.add(entry)
		db.session.commit()
		
		
	entries = ['Grenades', 'Explosives']

	for i in entries:

		entry = WeaponType(name=i, type_id=3)
		db.session.add(entry)
		db.session.commit()


	entries = ['Accessories', 'Other']

	for i in entries:

		entry = WeaponType(name=i, type_id=4)
		db.session.add(entry)
		db.session.commit()

	results = WeaponType.query.all()

	for result in results:
		print (result.id)
		print (result.type_id)
		print (result.name)

	return ('weqpon category added')

@app.route('/weapon/create')
def weapon_create():

	entries = ['Brass Knuckles', 'Club', 'Knife', 'Pepper Spray', 'Stun Gun']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=1, cost=2, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Battleaxe', 'Sword', 'Spear', 'Warhammer']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=2, cost=3, description=description)
		db.session.add(entry)
		db.session.commit()
	
	entries = ['Chain', 'Chainsaw', 'Nunchaku', 'Whip']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=3, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Holdout Pistol', 'Light Pistol', 'Heavy Pistol', 'Machine Pistol', 'Submachine Gun', 'Shotgun', 'Assault Rifle', 'Sniper Rifle', 'Bow', 'Crossbow']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=4, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Blaster Pistol', 'Blaster Rifle', 'Taser']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=5, cost=5, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Flamethrower', 'Grenade Launcher', 'Rocket Launcher']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=6, cost=6, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Bolos', 'Boomerang', 'Javelin', 'Shuriken']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=7, cost=7, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Fragmentation Grenade', 'Smoke Grenade', 'Flash Bang Grenade', 'Sleep Gas Grenade', 'Tear Gas Grrenade', 'Dynamite', 'Plastic Explosives']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=8, cost=8, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Laser Sight', 'Stun Ammo', 'Suppressor', 'Targeting Scope']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id= 9, cost=9, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Weapon.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('weapons added')

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