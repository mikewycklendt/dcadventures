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
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

load_dotenv()

import os

db_path = os.environ.get("db_path")

descrip = Blueprint('descrip', __name__)
db = SQLAlchemy()

@descrip.route('/descriptor/create', methods=['POST'])
def post_descriptor(): 
	body = {}
	body['success'] = True
	body['descriptor'] = False
	body['add_select'] = False
	new_selects = []
	error = False
	error_msgs = []
	descriptor = {}

	results = request.get_json()

	print('\n\n\nCreate Descriptor input:\n')
	print(results)

	origin = request.get_json()['origin']
	origin_name = request.get_json()['origin_name']
	origin_des = request.get_json()['origin_des']
	source = request.get_json()['source']
	source_name = request.get_json()['source_name']
	source_des = request.get_json()['source_des']
	medium_type = request.get_json()['medium_type']
	medium_subtype = request.get_json()['medium_subtype']
	medium_subtype_name = request.get_json()['medium_subtype_name']
	medium_subtype_des = request.get_json()['medium_subtype_des']
	medium = request.get_json()['medium']
	medium_name = request.get_json()['medium_name']
	medium_des = request.get_json()['medium_des']
	descriptor_field = request.get_json()['descriptor']
	descriptor_name = request.get_json()['descriptor_name']
	descriptor_result = request.get_json()['descriptor_result']
	descriptor_type = request.get_json()['descriptor_type']
	damage = request.get_json()['damage']
	power_id = request.get_json()['power_id']

	name = ''
	one_medium_name = ''

	rare = 0

	if descriptor_type == 'power':
		is_descriptor = True
		body['type'] = 'power'
	elif descriptor_type == 'effect':
		is_descriptor = False
		body['type'] = 'effect'
	else:
		error = True
		body['success'] = False
		error_msgs.append('You must specify whether or not this descriptor is assigned to this power.')
		body['error'] = error_msgs

	if power_id == '':
		error = True
		body['success'] = False
		error_msgs.append('You Must create a power first ')
		body['error'] = error_msgs

	if error:
		print('body: ')
		print(body)
		errors = body['error']
		for err in errors:
			print(err)
		return jsonify(body)

	if origin == 'new':
		process = True
		try:
			origin_check = db.session.query(Origin).filter(Origin.name == origin_name).first()
			if origin_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already an origin with that name')
				body['error'] = error_msgs
			if process:
				rare += 1
				entry = Origin(name=origin_name, description=origin_des)
				db.session.add(entry)
				db.session.commit()
				origin_id = entry.id
				entry = Descriptor(name=origin_name, origin=entry.id, result=origin_des, damage=damage)
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_origin', 'id': entry.id, 'name': entry.name})
				if name == '':
					name = name + entry.name
				else:
					name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that origin')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif origin == '':
		origin_id = None
	else:
		try:
			print('\n\norigin')
			print(origin)
			print(type(origin))			
			input_id = int(origin)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Origin).filter(Origin.id == input_id).one()
			origin_id = entry.id
			if name == '':	
				name = name + entry.name
			else:
				name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that origin')
			db.session.rollback()
		
	if source == 'new':
		process = True
		try:
			source_check = db.session.query(Source).filter(Source.name == source_name).first()
			if source_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a source with that name')
				body['error'] = error_msgs
			if process:
				rare += 1
				entry = Source(name=source_name, description=source_des)
				db.session.add(entry)
				db.session.commit()
				source_id = entry.id
				entry = Descriptor(name=source_name, source=entry.id, result=source_des, damage=damage)
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_source', 'id': entry.id, 'name': entry.name})
				if name == '':
					name = name + entry.name
				else:
					name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that source')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif source == '':
		source_id = None
	else:
		try:
			print('\n\nsource')
			print(source)
			print(type(source))	
			input_id = int(source)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Source).filter(Source.id == input_id).one()
			source_id = entry.id
			if name == '':
				name = name + entry.name
			else:
				name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that source')
			db.session.rollback()
		
	if medium_type != '':
		try:
			rare += 1
			print('\n\nsource')
			print(medium_type)
			print(type(medium_type))	
			input_id = int(medium_type)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(MediumType).filter(MediumType.id == input_id).one()
			medium_type_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium type')
			db.session.rollback()
	else:
		medium_type_id = None

	if medium_subtype == 'new':
		process = True
		try:
			medium_subtype_check = db.session.query(MediumSubType).filter(MediumSubType.name == medium_subtype_name).first()
			if medium_subtype_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a medium subtype with that name')
				body['error'] = error_msgs
			if process:
				rare += 1
				entry = MediumSubType(name=medium_subtype_name, medium_type=medium_type_id, description=medium_subtype_des)
				db.session.add(entry)
				db.session.commit()
				medium_subtype_id = entry.id
				entry = Descriptor(name=medium_subtype_name, medium_type=medium_type_id, medium_subtype=entry.id, result=medium_subtype_des, damage=damage)
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_medium_subtype', 'id': entry.id, 'name': entry.name})
				one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium subtype')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif medium_subtype == '':
		medium_subtype_id = None
	elif medium_subtype == 'all':
		medium_subtype_id = None
	else:
		try:
			print('\n\nmedium_subtype')
			print(medium_subtype)
			print(type(medium_subtype))	
			input_id = int(medium_subtype)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(MediumSubType).filter(MediumSubType.id == input_id).one()
			medium_subtype_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium subtype')
			db.session.rollback()

	if medium == 'new':
		process = True
		try:
			medium_check = db.session.query(Medium).filter(Medium.name == medium_name).first()
			if medium_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a medium with that name')
				body['error'] = error_msgs
			if process:
				rare += 4
				entry = Medium(name=medium_name, medium_type=medium_type_id, medium_subtype=medium_subtype_id, description=medium_des)
				db.session.add(entry)
				db.session.commit()
				medium_id = entry.id
				entry = Descriptor(name=medium_name, medium_type=medium_type_id, medium_subtype=medium_subtype_id, medium=entry.id, result=medium_des, damage=damage)
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_medium', 'id': entry.id, 'name': entry.name})
				one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif medium == '':
		medium_id = None
	elif medium == 'all':
		medium_id = None
	else:
		try:
			print('\n\nmedium')
			print(medium)
			print(type(medium))	
			input_id = int(medium)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Medium).filter(Medium.id == input_id).one()
			medium_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium')
			body['error'] = error_msgs
			db.session.rollback()

	if one_medium_name != '':
		if name == '':
			name = name + one_medium_name
		else:
			name = name + ', ' + one_medium_name

	if rare == 1:
		rarity = 'very'
	if rare == 2:	
		rarity = 'common'
	if 2 < rare < 5:
		rarity = 'uncommon'
	if rare > 4:
		rarity= 'rare'

	if descriptor_field == 'new':
		process = True
		try:
			descriptor_check = db.session.query(Descriptor).filter(Descriptor.name == descriptor_name).first()
			if descriptor_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a descriptor with that name')
				body['error'] = error_msgs
			if process:
				entry = Descriptor(name=descriptor_name, origin=origin_id, source=source_id, medium_type=medium_type_id, medium_subtype=medium_subtype_id, medium=medium_id, result=descriptor_result, damage=damage, rarity=rarity)
				db.session.add(entry)
				db.session.commit()
				descriptor_id = entry.id
				body['descriptor'] = True
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_field', 'id': entry.id, 'name': entry.name})
				name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that descriptor')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif descriptor_field == '':
		descriptor_id = None
	elif descriptor_field == 'all':
		descriptor_id = None
	else:
		try:
			print('\n\ndescriptor_field')
			print(descriptor_field)
			print(type(descriptor_field))	
			input_id = int(descriptor_field)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Descriptor).filter(Descriptor.id == input_id).one()
			descriptor_id = entry.id
			body['descriptor'] = True
			name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that descriptor')
			body['error'] = error_msgs
			db.session.rollback()

	if error:
		body['error'] = error_msgs
		print('body: ')
		print(body)
		errors = body['error']
		for err in errors:
			print(err)
		return jsonify(body)

	try:
		power_id = int(power_id)
		power_descriptor = PowerDes(name=name, power_id=power_id, des_id=descriptor_id, origin=origin_id, source=source_id, medium=medium_id, medium_type=medium_type_id, medium_subtype=medium_subtype_id, descriptor=is_descriptor, damage=damage)
		db.session.add(power_descriptor)
		db.session.commit()
	
		body['id'] = power_descriptor.id	
		body['name'] = power_descriptor.name
		body['selects'] = new_selects
	except:
		error = True
		body['success'] = False
		error_msgs.append('Could Not find that descriptor')
		body['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()

	db.session.close()
	print('\n\nbody: \n')
	print(body)
	return jsonify(body)
