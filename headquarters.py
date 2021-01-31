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
from models import Headquarters, HeadFeature, HeadFeatAddon, HeadSize, HeadCharFeat

from errors.headquarters_errors import head_addon_post_errors, head_feature_post_errors
from posts.headquarters_posts import head_feature_post, head_addon_post


load_dotenv()

import os

db_path = os.environ.get("db_path")

head = Blueprint('head', __name__)
db = SQLAlchemy()

@head.route('/headquarters/create')
def headquarters_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'headquarters_create/headquarters_create.html'

	headquarters_includes = {'base_form': 'headquarters_create/base_form.html', 'addon': 'headquarters_create/addon.html', 'feature': 'headquarters_create/feature.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Headquarters'
	stylesheets.append({"style": "/static/css/headquarters_create/headquarters_create.css"})

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
	
	head_toughness = []
	for i in range(0, 21, 1):
		toughness = i * 2
		head_toughness.append({'cost': i, 'value': '+' + str(toughness)})

	head_size = HeadSize.query.all()

	addons = [{'type': '', 'name': 'Add-on Type'}, {'type': 'feature', 'name': 'Feature'}, {'type': 'weapon', 'name': 'Weapon'}, {'type': 'equipment', 'name': 'Equipment'}]

	features = db.session.query(Feature).filter(Feature.name != '').order_by(Feature.name).all()

	equipment = db.session.query(Equipment).order_by(Equipment.name).all()

	equipment_type = EquipType.query.all()

	weapon_cat = WeaponCat.query.all()

	head_features = HeadFeature.query.all()

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, headquarters_includes=headquarters_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, head_toughness=head_toughness, head_size=head_size, addons=addons, features=features,
							equipment=equipment, equipment_type=equipment_type, weapon_cat=weapon_cat, head_features=head_features)

@head.route('/headquarters/size/select', methods=['POST'])
def headquarters_size_select():
	body = {}
	body['success'] = True
	
	id = request.get_json()['id'] 

	try:
		id = int(id)
		size = db.session.query(HeadSize).filter_by(id=id).one()
		body['cost'] = size.size
		body['rank'] = size.name
	except:
		body['success'] = False

	print(body)
	return jsonify(body)

@head.route('/headquarters/feature/select/info', methods=['POST'])
def head_feature_info_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id']

	try:
		type_id = int(type_id)	
		item = db.session.query(HeadFeature).filter_by(id=type_id).one()
		items = db.session.query(HeadFeatAddon).filter_by(head_feature=type_id).all()
		weapons = []
		weapon_check = False
		equipment = []
		equipment_check = False
		features = []
		feature_check = False
		for i in items:
			if i.weapon is not None:
				weapon_check = True
				weapon = db.session.query(Weapon).filter_by(id=i.weapon).one()
				weapons.append(weapon.name)
			if i.equipment is not None:	
				equipment_check = True
				equip = db.session.query(Equipment).filter_by(id=i.equipment).one()
				equipment.append(equip.name)
			if i.feature is not None:
				feature_check = True
				feature = db.session.query(Feature).filter_by(id=i.feature).one()
				features.append(feature.name)
		if weapon_check == False:
			weapons.append('No Weaopons')
		if equipment_check == False:	
			equipment.append('No Equipment')
		if feature_check == False:
			features.append('No Features')
		name = item.name
		cost = 1	
		description = item.description
		body['name'] = name
		body['description'] = description
		body['cost'] = cost
		body['weapons'] = weapons
		body['equipment'] = equipment
		body['features'] = features
	except:
		body['success'] = False

	print(body)
	return jsonify(body)
	

@head.route('/headquarters/create', methods=['POST'])
def post_headquarters(): 
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

	try:
		new_head = Headquarters(name=name)
		db.session.add(new_head)
		db.session.commit()
		body['success'] = True
		body['id'] = new_head.id
		body['name'] = new_head.name
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

@head.route('/headquarters/save', methods=['POST'])
def save_headquarters(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = head_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	head_id = request.get_json()['head_id']

	head_id = integer(head_id)

	entry = db.session.query(Headquarters).filter(Headquarters.id == head_id).one()


	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@head.route('/headquarters/save/success/<head_id>')
def headquarters_save_success(head_id):	
	headquarters = db.session.query(Headquarters).filter_by(id=head_id).one()
	
	flash('Headquarters ' + headquarters.name + ' Successfully Created')
	return redirect(url_for('home'))

@head.route('/headquarters/edit_name', methods=['POST'])
def edit_headquarters_name(): 
	body = {}
	error = False
	error_msgs = []

	head_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	try:
		edit_head = db.session.query(Headquarters).filter(Headquarters.id == head_id).one()
		edit_head.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_head.id
		body['name'] = edit_head.name
	except:
		error = True
		body['success'] = False
		error_msgs.append('There was an error processing the request')
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
		return jsonify(body)


@head.route('/headquarters/feature/create', methods=['POST'])
def head_post_feature():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = head_feature_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	head_id = request.get_json()['head_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	name = request.get_json()['name']
	description = request.get_json()['description']
	feature = request.get_json()['feature']

	head_id = db_integer(head_id)
	feature = db_integer(feature)

	if name != '':
		entry = HeadFeature(name = name,
							description = description)

		db.session.add(entry)
		db.session.commit()

		feature = entry.id

		db.session.close()

	entry = HeadCharFeat(head_id = head_id,
						feature = feature)

	db.session.add(entry)
	db.session.commit()

	total_cost = db.session.query(HeadCharFeat).filter(HeadCharFeat.head_id == head_id).count()

	print('\n\n\n')
	print(total_cost)
	print('\n\n')

	body = {}
	body['id'] = entry.id
	body['select_id'] = feature
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
	
	body = head_feature_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@head.route('/headquarters/feature/delete/<id>', methods=['DELETE'])
def delete_head_feature(id):
	try:
		get_id = db.session.query(HeadCharFeat).filter_by(id=id).one()
		feature = get_id.feature
		head_id = get_id.head_id
		db.session.query(HeadCharFeat).filter_by(id=id).delete()
		db.session.query(HeadFeature).filter_by(id=head_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		cost = 0
		remaining = db.session.query(HeadCharFeat).filter_by(head_id=head_id).first()
		if remaining is not None:
			cost = db.session.query(HeadCharFeat).filter_by(head_id=head_id).count()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': feature, 'feature': True, 'cost': cost})


@head.route('/headquarters/addon/create', methods=['POST'])
def head_post_adddon():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = head_addon_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	head_id = request.get_json()['head_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	feature = request.get_json()['feature']
	equipment = request.get_json()['equipment']
	weapon = request.get_json()['weapon']
	addon = request.get_json()['addon']
	head_feature = request.get_json()['head_feature']
	
	head_id = db_integer(head_id)
	feature = db_integer(feature)
	equipment = db_integer(equipment)
	weapon = db_integer(weapon)
	head_feature = db_integer(head_feature)

	entry = HeadFeatAddon(head_id = head_id,
					feature = feature,
					equipment = equipment,
					weapon = weapon,
					addon = addon,
					head_feature = head_feature)

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
	table_id = 'addon'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = head_addon_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@head.route('/headquarters/addon/delete/<id>', methods=['DELETE'])
def delete_head_addon(id):
	try:
		db.session.query(HeadFeatAddon).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:	
		print('\n\n' + str(id) + ' DELETED\n\n')
		print(count)
		return jsonify({'success': True, 'id': id, 'feature': False })


@head.route('/headquarters//create', methods=['POST'])
def head_post_():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = head__post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	head_id = request.get_json()['head_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	head_id = db_integer(head_id)

	entry = Headquarters(head_id = head_id)

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
	
	body = head__post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@head.route('/headquarters//delete/<id>', methods=['DELETE'])
def delete_head_(id):
	try:
		db.session.query().filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })
