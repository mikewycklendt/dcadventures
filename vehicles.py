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
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature
from vehicle_errors import veh_feature_post_errors, veh_save_errors
from vehicle_posts import veh_feature_post


load_dotenv()

import os

db_path = os.environ.get("db_path")

vehicle = Blueprint('vehicle', __name__)
db = SQLAlchemy()

@vehicle.route('/vehicle/create')
def vehicle_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'vehicle_create.html'

	vehicle_includes = {'base_form': 'vehicle_create/base_form.html', 'powers': 'vehicle_create/powers.html', 'feature': 'vehicle_create/feature.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Vehicle'
	stylesheets.append({"style": "/static/css/vehicle_create.css"})

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

	features = db.session.query(Feature).filter(Feature.name != '').order_by(Feature.name).all()

	equipment = db.session.query(Equipment).order_by(Equipment.name).all()

	equipment_type = EquipType.query.all()

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, vehicle_includes=vehicle_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, vehicle_type=vehicle_type, vehicle_size=vehicle_size, power_type=power_type,
							features=features, equioment=equipment, equipment_type=equipment_type)

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

@vehicle.route('/vehicle/feature/info', methods=['POST'])
def vehicle_feature_info():
	body = {}
	body['success'] = True
	
	feature_id = request.get_json()['id'] 

	try:
		feature_id = int(feature_id)
		feature = db.session.query(Feature).filter_by(id=feature_id).one()
		body['cost'] = 1
		body['name'] = feature.name 
		body['description'] = feature.description
	except:
		body['success'] = False

	print(body)
	return jsonify(body)


@vehicle.route('/vehicle/equipment/select', methods=['POST'])
def vehicle_equipment_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 

	try:
		type_id = int(type_id)
		equip_type = db.session.query(EquipType).filter_by(id=type_id).one()
		equipment = db.session.query(Equipment).filter_by(type_id=type_id).order_by(Equipment.name).all()
		options.append({'id': '', 'name': equip_type.name})
		options.append({'id': 'all', 'name': 'All Features'})
		for e in equipment:
			options.append({'id': e.id, 'name': e.name})
	except:
		options.append({'id': '', 'name': 'No Equipment of that Type'})
		options.append({'id': 'all', 'name': 'All Features'})
	
	body['options'] = options

	print(body)
	return jsonify(body)



@vehicle.route('/vehicle/feature/select', methods=['POST'])
def vehicle_feature_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 
	
	try:
		type_id = int(type_id)
		print(type_id)
		equipment = db.session.query(Equipment).filter_by(id=type_id).one()
		features = db.session.query(Feature).filter(Feature.equip_id==type_id).order_by(Feature.name).first()
		if features is None:
			options.append({'id': '', 'name': 'Equipment has no Features'})
		else:
			features = db.session.query(Feature).filter(Feature.equip_id==type_id, Feature.name != '').order_by(Feature.name).all()
			equipment_name = equipment.name + "'s Features"
			options.append({'id': '', 'name': equipment_name})
			for f in features:
				options.append({'id': f.id, 'name': f.name})
	except:
		options.append({'id': '', 'name': 'All Features'})
		features = db.session.query(Feature).filter(Feature.name != '').order_by(Feature.name).all()
		for f in features:
			options.append({'id': f.id, 'name': f.name})

	body['options'] = options

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

	vehicle_id = db_integer(vehicle_id)

	entry = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()


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
		error_msgs.append('There is already a weapon with that name')
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
	
	vehicle_id = db_integer(vehicle_id)
	feature = db_integer(feature)

	entry = VehFeature(vehicle_id = vehicle_id,
					feature = feature)

	db.session.add(entry)
	db.session.commit()

	count = db.session.query(VehFeature).filter(VehFeature.vehicle_id == vehicle_id).count()

	body = {}
	body['id'] = entry.id
	body['features'] = count
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
		count = db.session.query(VehFeature).filter(VehFeature.vehicle_id == vehicle_id).count()
		print('\n\n' + str(vehicle_id) + ' DELETED\n\n')
		print(count)
		return jsonify({'success': True, 'id': vehicle_id, 'power': False, 'feature': True, 'features': count })
