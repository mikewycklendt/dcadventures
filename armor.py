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
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense
from armor_errors import arm_descriptor_post_errors, arm_defense_post_errors, arm_save_errors
from armor_posts import arm_descriptor_post, arm_defense_post
load_dotenv()

import os

db_path = os.environ.get("db_path")

arm = Blueprint('arm', __name__)
db = SQLAlchemy()

@arm.route('/armor/create')
def armor_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'armor_create.html'

	armor_includes = {'base_form': 'armor_create/base_form.html', 'descriptor': 'armor_create/descriptor.html', 'defense': 'armor_create/defense.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Armor'
	stylesheets.append({"style": "/static/css/armor_create.css"})

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

	armor_type = ArmorType.query.all()

	defenses = Defense.query.all()

	origins = db.session.query(Origin).order_by(Origin.name).all()
	
	sources = db.session.query(Source).order_by(Source.name).all()
	
	mediums = db.session.query(MediumType).order_by(MediumType.name).all()

	materials = db.session.query(Material).order_by(Material.name).all()


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, armor_includes=armor_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, armor_type=armor_type, defenses=defenses, origins=origins, sources=sources,
							mediums=mediums, materials=materials)
							

@arm.route('/armor/create', methods=['POST'])
def post_armor(): 
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

	armor = db.session.query(Armor).filter(Armor.name == name).first()

	if armor is not None:
		error = True
		body['success'] = False
		message = 'There is already armor with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_armor = Armor(name=name)
		db.session.add(new_armor)
		db.session.commit()
		body['success'] = True
		body['id'] = new_armor.id
		body['name'] = new_armor.name
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

@arm.route('/armor/save', methods=['POST'])
def save_armor(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = arm_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	armor_id = request.get_json()['armor_id']
	description = request.get_json()['description']
	type_id = request.get_json()['type_id']
	cost = request.get_json()['cost']
	material = request.get_json()['material']
	toughness = request.get_json()['toughness']
	active = request.get_json()['active']
	subtle = request.get_json()['subtle']
	perception = request.get_json()['perception']
	impervious = request.get_json()['impervious']
	defense = request.get_json()['defense']
	descriptor = request.get_json()['descriptor']

	type_id = db_integer(type_id)
	cost = integer(cost)
	material = db_integer(material)
	toughness = integer(toughness)
	active = integer(active)
	perception = integer(perception)
	
	entry = db.session.query(Armor).filter(Armor.id == armor_id).one()

	entry.description = description
	entry.type_id = type_id
	entry.cost = cost
	entry.toughness = toughness
	entry.active = active
	entry.subtle = subtle
	entry.perception = perception
	entry.impervious = impervious
	entry.defense = defense
	entry.descriptor = descriptor

	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@arm.route('/armor/save/success/<armor_id>')
def armor_save_success(armor_id):	
	armor = db.session.query(Armor).filter_by(id=armor_id).one()
	
	flash('Armor ' + armor.name + ' Successfully Created')
	return redirect(url_for('home'))

@arm.route('/armor/edit_name', methods=['POST'])
def edit_armor_name(): 
	body = {}
	error = False
	error_msgs = []

	armor_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	armor = db.session.query(Armor).filter(Armor.name == name).first()
	
	if armor is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already a weapon with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_armor = db.session.query(Armor).filter(Armor.id == armor_id).one()
		edit_armor.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_armor.id
		body['name'] = edit_armor.name
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


@arm.route('/armor/descriptor/create', methods=['POST'])
def armor_post_descriptor():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = arm_descriptor_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	armor_id = request.get_json()['armor_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	descriptor = request.get_json()['descriptor']

	armor_id = db_integer(armor_id)
	descriptor = db_integer(descriptor)

	entry = ArmDescriptor(armor_id = armor_id,
							descriptor = descriptor)

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
	table_id = 'descriptor'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = arm_descriptor_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@arm.route('/armor/descriptor/delete/<armor_id>', methods=['DELETE'])
def delete_armor_descriptor(armor_id):
	try:
		db.session.query(ArmDescriptor).filter_by(id=armor_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(armor_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': armor_id, 'cost': False})


@arm.route('/armor/defense/create', methods=['POST'])
def armor_post_defensev():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = arm_defense_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	armor_id = request.get_json()['armor_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	defense = request.get_json()['defense']
	bonus = request.get_json()['bonus']

	armor_id = db_integer(armor_id)
	bonus = integer(bonus)
	defense = db_integer(defense)

	entry = ArmDefense(armor_id = armor_id,
							defense = defense,
							bonus = bonus)

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
	table_id = 'defense'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = arm_defense_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@arm.route('/armor/defense/delete/<armor_id>', methods=['DELETE'])
def delete_armor_defense(armor_id):
	try:
		db.session.query(ArmDefense).filter_by(id=armor_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(armor_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': armor_id, 'cost': False})
