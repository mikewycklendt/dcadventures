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

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, value_limit, select_check, check_of, multiple_effect_check, multiple_link_check, required_setting, linked_group_check, required_link_field, linked_field, required_rule
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

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



@app.route('/close/create')
def subskill_close_create():

	ability = 5
	skill = 3
	check_type = 5
	action = 1
	attack = integer('skill')

	styles = db.session.query(WeaponStyle).filter(WeaponStyle.type_id == 1, WeaponStyle.show == True).all()

	for i in styles:

		if i.id == 14:
			description = 'Attack Bonus equal to this rank for all unarmed attacks.'
		else:
			description = 'Attack Bonus equal to this rank for attacks with ' + i.name
 
		entry = SkillBonus(name=i.name, show=True, base=True, subskill=True, description=description, weapon_style=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')

@app.route('/ranged/create')
def subskill_ranged_create():

	ability = 4
	skill = 11
	check_type = 5
	action = 1
	attack = integer('skill')

	styles = db.session.query(WeaponStyle).filter(WeaponStyle.type_id == 2, WeaponStyle.show == True).all()

	for i in styles:
	
		description = 'Attack Bonus equal to this rank for attacks with ' + i.name + ' Weapons.'
 
		entry = SkillBonus(name=i.name, show=True, base=True, subskill=True, description=description, weapon_style=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')


@app.route('/expertise/create')
def subskill_expertise_create():

	ability = db_integer(Ability, 'gm')
	skill = 5
	check_type = 3
	action = 1

	styles = db.session.query(Job).filter(Job.show == True).all()

	for i in styles:
	
		description = 'Can answer all ' + i.name + ' related questions and perform ' + i.name + ' routine tasks as routine checks.'
 
		entry = SkillBonus(name=i.name, show=True, base=True, subskill=True, description=description, profession=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')

if __name__ == '__main__':
	app.debug = True
	app.secret_key = os.urandom(32)
	app.run(host='0.0.0.0', port=80)