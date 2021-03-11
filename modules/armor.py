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
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from errors.armor_errors import arm_descriptor_post_errors, arm_defense_post_errors, arm_save_errors
from posts.armor_posts import arm_descriptor_post, arm_defense_post
from create_functions.armor_create import arm_entry_check

load_dotenv()

import os

db_path = os.environ.get("db_path")

arm = Blueprint('arm', __name__)
db = SQLAlchemy()

@arm.route('/armor/create')
def armor_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'advantage_create/armor_create.html'

	armor_includes = {'base_form': 'armor_create/base_form.html', 'descriptor': 'armor_create/descriptor.html', 'defense': 'armor_create/defense.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Armor'
	stylesheets.append({"style": "/static/css/advantage_create/armor_create.css"})

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

	defenses = db.session.query(Defense).filter(Defense.hide == None).all()

	origins = db.session.query(Origin).filter(Origin.show == True).order_by(Origin.name).all()
	
	sources = db.session.query(Source).filter(Source.show == True).order_by(Source.name).all()
	
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

	type_id = integer(type_id)
	cost = integer(cost)
	material = integer(material)
	toughness = integer(toughness)
	active = integer(active)
	perception = integer(perception)
	
	entry = db.session.query(Armor).filter(Armor.id == armor_id).one()

	entry.description = description
	entry.type_id = type_id
	entry.cost = cost
	entry.material = material
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

	armor_id = integer(aemor_id)
	descriptor = db_integer(Descriptor, descriptor)

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
	body = {}
	body['success'] = True
	body['id'] = armor_id
	body['cost'] = False
	try:
		db.session.query(ArmDescriptor).filter_by(id=armor_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete that Descriptor.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(armor_id) + ' DELETED\n\n')
		return jsonify(body)


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

	armor_id = integer(aemor_id)
	defense = db_integer(Defense, defense)
	bonus = integer(bonus)
	
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
	body = {}
	body['success'] = True
	body['id'] = armor_id
	body['cost'] = False
	try:
		db.session.query(ArmDefense).filter_by(id=armor_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete that Descriptor.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(armor_id) + ' DELETED\n\n')
		return jsonify(body)