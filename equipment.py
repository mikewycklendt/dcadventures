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
from models import Equipment

load_dotenv()

import os

db_path = os.environ.get("db_path")

equip = Blueprint('equipment', __name__)
db = SQLAlchemy()

@equip.route('/equipment/create')
def equipment_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'equipment_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Equipment'
	stylesheets.append({"style": "/static/css/equipment_create.css"})

	equipment_includes = {'base_form': 'equipment_create/base_form.html', 'damaged': 'equipment_create/damaged.html', 'opposed': 'equipment_create/opposed.html'}

	equipment = Equipment.query.all()

	skills = Skill.quey.all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	distances = db.session.query(Unit).filter_by(type_id=3)
	
	expertise = db.session.query(SkillBonus).filter_by(skill_id=5).all()

	damages = db.session.query(Descriptor).filter_by(damage=True).order_by(Descriptor.name).all()
	
	checks = db.session.query(Check).all()

	base_conditions = Condition.query.all()
	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

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

	equipment_type = [{'type': '', 'name': 'Equipment Type'}, {'type': 'general', 'name': 'General Equipment'}, {'type': 'electronics', 'name': 'Electronics'}, {'type': 'criminal', 'name': 'Criminal Gear'}, {'type': 'surveil', 'name': 'Surveillance Gear'}, {'type': 'survival', 'name': 'Survival Gear'}, {'type': 'utility', 'name': 'Utility Belt'}]

	damaged = [{'type': '', 'name': 'Damaged Effect'}, {'type': 'feature', 'name': 'Loses a Feature'}, {'type': 'circ', 'name': '-1 Circumstance'}]

	when = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]



	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, equipment_includes=equipment_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, equipment=equipment, equipment_type=equipment_type, damaged=damaged, skills=skills,
							times=times, distances=distances, expertise=expertise)


@equip.route('/equipment/skill/select', methods=['POST'])
def advantage_action_select():
	body = {}
	body['success'] = True
	options = []

	skill_id = request.get_json()['skill_id'] 

	try:
		skill = db.session.query(Skilll).filter_by(id=skill_id).one()
		bonuses = db.session.query(SkillBonus).filter_by(skill_id=skill_id).order_by(SkillBonus.name).all()
		skill_name = skill.name + ' Skill'
		options.append({'id': '', 'name': skill_name})
		for b in bonuses:
			options.append({'id': b.id, 'name': b.name})
	except:
		options.append({'id': '', 'name': 'Enhanced Skill'})
	
	body['options'] = options

	print(body)
	return jsonify(body)


@equip.route('/equipment/create', methods=['POST'])
def post_equipment(): 
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

	equipment = db.session.query(Equipment).filter(Equipment.name == name).first()

	if equipment is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an item of equipment with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_equipment = Equipment(name=name)
		db.session.add(new_equipment)
		db.session.commit()
		body['success'] = True
		body['id'] = new_equipment.id
		body['name'] = new_equipment.name
	except:
		error = True
		errors['success'] = False
		error_msgs.append('There was an error processing the request')
		errors['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@equip.route('/equipment/save', methods=['POST'])
def save_equipment(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = equip_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']

	entry = db.session.query(Equipment).filter(Equipment.id == equip_id).one()


	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@equip.route('/equipment/save/success/<equipment_id>')
def equipment_save_success(equipment_id):	
	equipment = db.session.query(Equipment).filter_by(id=equipment_id).one()
	
	flash('Equipment ' + equipment.name + ' Successfully Created')
	return redirect(url_for('home'))

@equip.route('/equipment/edit_name', methods=['POST'])
def edit_equipment_name(): 
	body = {}
	error = False
	error_msgs = []

	equip_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	equipment = db.session.query(Equipment).filter(Equipment.name == name).first()
	
	if equipment is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an item of equipment with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_equipment = db.session.query(Equipment).filter(Equipment.id == equip_id).one()
		edit_equipment.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_equipment.id
		body['name'] = edit_equipment.name
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
