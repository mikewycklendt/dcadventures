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
from app import sidebar_create
from models import Equipment

load_dotenv()

import os

db_path = os.environ.get("db_path")

equipment = Blueprint('equipment', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = sidebar

@equipment.route('/equipment/create')
def equipment_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'equipment_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Equipment'
	stylesheets.append({"style": "/static/css/equipment_create.css"})

	equipment_includes = {'base_form': 'equipment_create/base_form.html'}

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


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, equipment_includes=equipment_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers)


@equipment.route('/equipment/create', methods=['POST'])
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

@equipment.route('/equipment/save', methods=['POST'])
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

@equipment.route('/equipment/save/success/<equipment_id>')
def equipment_save_success(equipment_id):	
	equipment = db.session.query(Equipment).filter_by(id=equipment_id).one()
	
	flash('Equipment ' + equipment.name + ' Successfully Created')
	return redirect(url_for('home'))

@equipment.route('/equipment/edit_name', methods=['POST'])
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
