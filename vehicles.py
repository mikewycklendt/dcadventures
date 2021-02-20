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

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_table import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from errors.vehicle_errors import veh_feature_post_errors, veh_save_errors, veh_powers_post_errors
from posts.vehicle_posts import veh_feature_post, veh_powers_post


load_dotenv()

import os

db_path = os.environ.get("db_path")

vehicle = Blueprint('vehicle', __name__)
db = SQLAlchemy()

@vehicle.route('/vehicle/create')
def vehicle_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'vehicle_create/vehicle_create.html'

	vehicle_includes = {'base_form': 'vehicle_create/base_form.html', 'powers': 'vehicle_create/powers.html', 'feature': 'vehicle_create/feature.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Vehicle'
	stylesheets.append({"style": "/static/css/vehicle_create/vehicle_create.css"})

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

	vehicle_type = VehicleType.query.all()

	vehicle_size = VehicleSize.query.all()

	power_type = PowerType.query.all()

	features = db.session.query(Feature).filter(Feature.show == True).order_by(Feature.name).all()

	equipment = db.session.query(Equipment).filter(Equipment.show == True).order_by(Equipment.name).all()

	equipment_type = EquipType.query.all()

	weapon_cat = WeaponCat.query.all()

	addons = [{'type': '', 'name': 'Add-on Type'}, {'type': 'feature', 'name': 'Feature'}, {'type': 'weapon', 'name': 'Weapon'}, {'type': 'equipment', 'name': 'Equipment'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, vehicle_includes=vehicle_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, vehicle_type=vehicle_type, vehicle_size=vehicle_size, power_type=power_type,
							features=features, equioment=equipment, equipment_type=equipment_type, addons=addons, weapon_cat=weapon_cat)

@vehicle.route('/vehicle/size/select', methods=['POST'])
def vehicle_size_select():
	body = {}
	body['success'] = True
	
	size_id = request.get_json()['id'] 

	try:
		size_id = int(size_id)
		size = db.session.query(VehicleSize).filter_by(id=size_id).one()
		body['cost'] = size.cost
		body['rank'] = size.size
		body['defense'] = size.defense
		body['strength'] = size.strength
		body['toughness'] = size.toughness
	except:
		body['success'] = False

	print(body)
	return jsonify(body)


@vehicle.route('/vehicle/create', methods=['POST'])
def post_vehicle(): 
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

	vehicle = db.session.query(Vehicle).filter(Vehicle.name == name).first()

	if vehicle is not None:
		error = True
		body['success'] = False
		message = 'There is already a vehicle with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_vehicle = Vehicle(name=name)
		db.session.add(new_vehicle)
		db.session.commit()
		body['success'] = True
		body['id'] = new_vehicle.id
		body['name'] = new_vehicle.name
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

@vehicle.route('/vehicle/save', methods=['POST'])
def save_vehicle(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = veh_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	vehicle_id = request.get_json()['vehicle_id']
	description = request.get_json()['description']
	type_id = request.get_json()['type_id']
	size = request.get_json()['size']
	strength = request.get_json()['strength']
	speed = request.get_json()['speed']
	toughness = request.get_json()['toughness']
	defense = request.get_json()['defense']
	cost = request.get_json()['cost']
	feature = request.get_json()['feature']
	power = request.get_json()['power']

	vehicle_id = db_integer(vehicle_id)
	type_id = integer(type_id)
	size = integer(size)
	strength = integer(strength)
	speed = integer(speed)
	toughness = integer(toughness)
	defense = integer(defense)
	cost = integer(cost)

	entry = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()

	entry.description = description
	entry.type_id = type_id
	entry.size = size
	entry.strength = strength
	entry.speed = speed
	entry.toughness = toughness
	entry.defense = defense
	entry.cost = cost
	entry.feature = feature
	entry.power = power

	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@vehicle.route('/vehicle/save/success/<vehicle_id>')
def vehicle_save_success(vehicle_id):	
	vehicle = db.session.query(Vehicle).filter_by(id=vehicle_id).one()
	
	flash('Vehicle ' + vehicle.name + ' Successfully Created')
	return redirect(url_for('home'))

@vehicle.route('/vehicle/edit_name', methods=['POST'])
def edit_vehicle_name(): 
	body = {}
	error = False
	error_msgs = []

	vehicle_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	vehicle = db.session.query(Vehicle).filter(Vehicle.name == name).first()
	
	if vehicle is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already a vehicle with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_vehicle = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()
		edit_vehicle.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_vehicle.id
		body['name'] = edit_vehicle.name
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

@vehicle.route('/vehicle/powers/create', methods=['POST'])
def vehicle_post_powers():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()
	print(data)

	errors = veh_powers_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	vehicle_id = request.get_json()['vehicle_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	cost = request.get_json()['cost']
	ranks  = request.get_json()['ranks']
	power = request.get_json()['power']

	vehicle_id = db_integer(vehicle_id)
	cost = integer(cost)
	ranks = integer(ranks)
	power = integer(power)

	entry = VehPower(vehicle_id = vehicle_id,
					cost = cost,
					ranks = ranks,
					power = power)

	db.session.add(entry)
	db.session.commit()

	total_cost = 0
	total_rank = 0

	powers = db.session.query(VehPower).filter(VehPower.vehicle_id == vehicle_id).first()
	if powers is not None:
		powers = db.session.query(VehPower).filter(VehPower.vehicle_id == vehicle_id).all()
		for p in powers:
			total_cost += p.cost
			total_rank += p.ranks

	body = {}
	body['id'] = entry.id
	body['cost'] = total_cost
	body['rank'] = total_rank
	error = False
	error_msg = []
	body['success'] = True

	rows = columns	
	mods = []
	cells = []
	table_id = 'powers'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = veh_powers_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@vehicle.route('/vehicle/powers/delete/<id>', methods=['DELETE'])
def delete_vehicle_powers(id):
	try:
		vehicle_power = db.session.query(VehPower).filter_by(id=id).one()
		vehicle_id = vehicle_power.vehicle_id
		db.session.query(VehPower).filter_by(id=id).delete()
		db.session.commit()
		
		total_cost = 0
		total_rank = 0

		powers = db.session.query(VehPower).filter(VehPower.vehicle_id == vehicle_id).first()
		if powers is not None:
			powers = db.session.query(VehPower).filter(VehPower.vehicle_id == vehicle_id).all()
			for p in powers:
				total_cost += p.cost
				total_rank += p.ranks
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(vehicle_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': vehicle_id, 'power': True, 'feature': False, 'cost': total_cost, 'rank': total_rank })


@vehicle.route('/vehicle/feature/create', methods=['POST'])
def vehicle_post_feature():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = veh_feature_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	vehicle_id = request.get_json()['vehicle_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	feature = request.get_json()['feature']
	cost = request.get_json()['cost']
	equipment = request.get_json()['equipment']
	weapon = request.get_json()['weapon']
	addon = request.get_json()['addon']
	
	vehicle_id = db_integer(vehicle_id)
	feature = db_integer(feature)
	equipment = db_integer(equipment)
	weapon = db_integer(weapon)
	cost = integer(cost)

	entry = VehFeature(vehicle_id = vehicle_id,
					feature = feature,
					cost = cost,
					equipment = equipment,
					weapon = weapon,
					addon = addon)

	db.session.add(entry)
	db.session.commit()

	items = db.session.query(VehFeature).filter(VehFeature.vehicle_id == vehicle_id).all()

	total_cost = 0

	for i in items:
		total_cost += i.cost

	body = {}
	body['id'] = entry.id
	body['cost'] = total_cost
	error = False
	error_msg = []
	body['success'] = True

	rows = columns	
	mods = []
	cells = []
	table_id = 'feature'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = veh_feature_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@vehicle.route('/vehicle/feature/delete/<id>', methods=['DELETE'])
def delete_vehicle_feature(id):
	try:
		entry = db.session.query(VehFeature).filter_by(id=id).one()
		vehicle_id = entry.vehicle_id
		db.session.query(VehFeature).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		total_cost = 0
		items = db.session.query(VehFeature).filter(VehFeature.vehicle_id == vehicle_id).first()
		if powers is not None:
			items = db.session.query(VehFeature).filter(VehFeature.vehicle_id == vehicle_id).all()
			for i in items:
				total_cost += i.cost
		print('\n\n' + str(vehicle_id) + ' DELETED\n\n')
		print(count)
		return jsonify({'success': True, 'id': vehicle_id, 'power': False, 'feature': True, 'cost': total_cost })



@vehicle.route('/vehicle/vehicle/create', methods=['POST'])
def vehicle_post_():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = veh__post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	vehicle_id = request.get_json()['vehicle_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	vehicle_id = db_integer(vehicle_id)

	entry = Vehicle(vehicle_id = vehicle_id)

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
	table_id = ''
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = veh__post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@vehicle.route('/vehicle//delete/<vehicle_id>', methods=['DELETE'])
def delete_vehicle_(vehicle_id):
	try:
		db.session.query().filter_by(id=vehicle_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(vehicle_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': vehicle_id, 'power': False, 'feature': False })
