from flask import Blueprint
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
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add
from base_files import sidebar, stylesheets, meta_name, meta_content, title
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from equipment_posts import equip_belt_post, equip_check_post, equip_damaged_post, equip_descriptor_post, equip_effect_post, equip_feature_post, equip_limits_post, equip_modifiers_post, equip_opposed_post
from equipment_errors import equip_belt_post_errors, equip_check_post_errors, equip_damaged_post_errors, equip_descriptor_post_errors, equip_effect_post_errors, equip_feature_post_errors, equip_limits_post_errors, equip_modifiers_post_errors, equip_opposed_post_errors, equip_save_errors

load_dotenv()

import os

db_path = os.environ.get("db_path")

weap = Blueprint('weap', __name__)
db = SQLAlchemy()

@weap.route('/weapon/create')
def weapon_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'weapon_create.html'

	weapon_includes = {'base_form': 'weapon_create/base_form.html'}

	title = 'DC Adventures Online Roleplaying Game: Create Weapon'
	stylesheets.append({"style": "/static/css/weapon_create.css"})

	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	positives = []
	for i in range(1, 41, 1):
		positives.append(i)

	hundred = []
	for i in range(1, 101, 1):
		hundred.append(i)

	die = []
	for i in range(1, 21, 1):
		die.append(i)

	time_numbers = []
	for i in range(1, 61, 1):
		time_numbers.append(i)


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, weapon_includes=weapon_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers)

@weap.route('/weapon/create', methods=['POST'])
def post_weapon(): 
	body = {}
	error = False
	error_msgs = []

	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	weapon = db.session.query(Weapon).filter(Weapon.name == name).first()

	if weapon is not None:
		error = True
		body['success'] = False
		message = 'There is already a weapon with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_weapon = Weapon(name=name)
		db.session.add(new_weapon)
		db.session.commit()
		body['success'] = True
		body['id'] = new_weapon.id
		body['name'] = new_weapon.name
	except:
		error = True
		errors['success'] = False
		error_msgs.append('There was an error processing the request')
		errors['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@weap.route('/weapon/save', methods=['POST'])
def save_weapon(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = weap_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	weapon_id = request.get_json()['weapon_id']

	weapon_id = integer(weapon_id)

	entry = db.session.query(Weapon).filter(Weapon.id == weapon_id).one()


	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@weap.route('/weapon/save/success/<weapon_id>')
def weapon_save_success(weapon_id):	
	weapon = db.session.query(Weapon).filter_by(id=weapon_id).one()
	
	flash('Weapon ' + weapon.name + ' Successfully Created')
	return redirect(url_for('home'))

@weap.route('/weapon/edit_name', methods=['POST'])
def edit_weapon_name(): 
	body = {}
	error = False
	error_msgs = []

	weapon_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	weapon = db.session.query(Weapon).filter(Weapon.name == name).first()
	
	if weapon is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already a weapon with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_weapon = db.session.query(Weapon).filter(Weapon.id == weapon_id).one()
		edit_weapon.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_weapon.id
		body['name'] = edit_weapon.name
	except:
		error = True
		body['success'] = False
		error_msgs.append('There was an error processing the request')
		body['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
		return jsonify(body)