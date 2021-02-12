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


@app.route('/table/db')
def table_db_columns_create():



	name = 'Any Chosen Rare' 

	entry = PowerDes(rare=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Uncommon' 

	entry = PowerDes(uncommon=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Common' 

	entry = PowerDes(common=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Very Common' 

	entry = PowerDes(very=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Damage' 

	entry = PowerDes(any_damage=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Origin' 

	entry = PowerDes(any_origin=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Source' 

	entry = PowerDes(any_source=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Medium Type' 

	entry = PowerDes(any_medium_type=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Medium Subtype' 

	entry = PowerDes(any_medium_subtype=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Medium' 

	entry = PowerDes(any_medium=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any Chosen Descriptor' 

	entry = PowerDes(any_descriptor=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerDes).filter_by(hidden=True).all()
	for r in results:
		print(r.name)

	return ('descriptor columns added')

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