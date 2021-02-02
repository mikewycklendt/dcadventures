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
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus
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
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature
from models import Headquarters, HeadFeature, HeadFeatAddon, HeadSize, HeadCharFeat



load_dotenv()

import os

db_path = os.environ.get("db_path")

skill = Blueprint('skill', __name__)
db = SQLAlchemy()

@skill.route('/skill/create')
def headquarters_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'skill_create/skill_create.html'

	skill_includes = {'base_form': 'skill_create/base_form.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Enhanced Skill'
	stylesheets.append({"style": "/static/css/skill_create/skill_create.css"})

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
	
	skills = Skill.query.all()


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, skill_includes=skill_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, skills=skills)


@skill.route('/vehicle/create', methods=['POST'])
def post_skill_bonus(): 
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

	bonus = db.session.query(SkillBonus).filter(SkillBonus.name == name).first()

	if bonus is not None:
		error = True
		body['success'] = False
		message = 'There is already an enhanced skill with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_bonus = SkillBonus(name=name)
		db.session.add(new_bonus)
		db.session.commit()
		body['success'] = True
		body['id'] = new_bonus.id
		body['name'] = new_bonus.name
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

@skill.route('/skill/save', methods=['POST'])
def save_skill_bonus(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = skill_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	bonus_id = request.get_json()['bonus_id']

	bonus_id = db_integer(bonus_id)

	entry = db.session.query(SkillBonus).filter(SkillBonus.id == bonus_id).one()

	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@skill.route('/skill/save/success/<id>')
def skill_bonus_save_success(id):	
	bonus = db.session.query(SkillBonus).filter_by(id=id).one()
	
	flash('Enhanced Skill ' + bonus.name + ' Successfully Created')
	return redirect(url_for('home'))

@skill.route('/skill/edit_name', methods=['POST'])
def edit_skill_bonus_name(): 
	body = {}
	error = False
	error_msgs = []

	bonus_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	bonus = db.session.query(SkillBonus).filter(SkillBonus.name == name).first()
	
	if bonus is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an Enhanced Skill with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_bonus = db.session.query(SkillBonus).filter(SkillBonus.id == bonus_id).one()
		edit_bonus.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_bonus.id
		body['name'] = edit_bonus.name
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



@skill.route('/skill//create', methods=['POST'])
def skill_bonus_post_():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill__post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	bonus_id = request.get_json()['bonus_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	bonus_id = db_integer(bonus_id)

	entry = Headquarters(bonus_id = bonus_id)

	db.session.add(entry)
	db.session.commit()

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns	
	mods = []
	cells = []
	table_id = 'TABLEID-------'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill__post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill//delete/<id>', methods=['DELETE'])
def delete_skill_bonus_(id):
	try:
		db.session.query().filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })
