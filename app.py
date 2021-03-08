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

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeaponStyle, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from tables import tables
from modules.selects import select
from info_select import info
from icon_select import icon
from modules.skills import skill
from modules.powers import powers
from modules.advantage import advantage
from modules.equipment import equip
from modules.weapons import weap
from modules.armor import arm
from modules.vehicles import vehicle
from modules.headquarters import head
from modules.descriptor import descrip

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
	
@app.teardown_appcontext
def shutdown_session(exception=None):
	db.session.remove()


@app.route('/table/db')
def table_db_columns_create():

	tablename =  'Weapon'

	name = 'All Weapons'

	entry = Weapon(all=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Weapon(current=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Weapon(any=True, name=name)
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Weapon(var=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Weapon(none=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Active Power'

	entry = Weapon(active=True, name=name)
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Weapon).filter_by(show=None).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')

@app.route('/weapon/type')
def weapon_type_hhidden():

	tablename =  'Weapon Type'

	name = 'All Weapon Types'

	entry = WeaponType(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = WeaponType(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = WeaponType(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = WeaponType(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = WeaponType(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Active Power'

	entry = WeaponType(active=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(WeaponType).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')

@app.route('/weapon/style')
def weapon_style_create():

	tablename =  'Weapon Style'

	name = 'All Weapon Styles'

	entry = WeaponStyle(all=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = WeaponStyle(current=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = WeaponStyle(any=True, name=name)
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = WeaponStyle(var=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = WeaponStyle(none=True, name=name)
	db.session.add(entry)
	db.session.commit()

	entries = ['Improvised']

	for i in entries:

		entry = WeaponStyle(name=i, improvise=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Swords', 'Knives', 'Axes', 'Spears', 'Whips', 'Clubs', 'Maces', 'Unarmed', 'Lances', 'Hammers', 'Batons']

	for i in entries:

		entry = WeaponStyle(name=i, type_id=1, show=True, base=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Guns', 'Fire', 'Throwing', 'Rockets']

	for i in entries:

		entry = WeaponStyle(name=i, type_id=2, show=True, base=True)
		db.session.add(entry)
		db.session.commit()

	results = WeaponStyle.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('weapon styles added')



if __name__ == '__main__':
	app.debug = True
	app.secret_key = os.urandom(32)
	app.run(host='0.0.0.0', port=80)