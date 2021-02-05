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
from tables import tables
from skills import skill
from powers import powers
from advantage import advantage
from equipment import equip
from weapons import weap
from armor import arm
from vehicles import vehicle
from headquarters import head
from dotenv import load_dotenv
from base_files import sidebar, stylesheets, meta_name, meta_content, title

from models import Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged 
from models import setup_db, Ability,  ConflictAction, Damage, DamageType, flash
from models import Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense
from models import Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank 
from models import Levels, LevelType

from db.advanrtage_modeks import Advantage, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

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
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def home(sidebar=sidebar, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, title=title):
	includehtml = 'home.html'

	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)





@app.route('/abilities/create')
def abilities_create():


	id = 2
	icon = 'athletics-icon'
	skill = db.session.query(Skill).filter(Skill.id == id).one()
	skill.icon = icon
	db.session.commit()
	db.session.close()

	id = 1
	icon = 'strength-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 2
	icon = 'stamina-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 3
	icon = 'agility-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 4
	icon = 'dexterity-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 5
	icon = 'fighting-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 6
	icon = 'intellect-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 7
	icon = 'awareness-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 8
	icon = 'presence-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	results = Ability.query.all()

	for result in results:
		print(result.name)
		print(result.icon)

	return ('abilities icons')


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