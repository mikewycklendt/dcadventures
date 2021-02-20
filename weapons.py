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
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from errors.weapons_errors import weap_benefit_post_errors, weap_condition_post_errors, weap_descriptor_post_errors, weap_save_errors
from posts.weapons_posts import weap_benefit_post, weap_condition_post, weap_descriptor_post
from functions.create.weapon_create import weap_entry_check

load_dotenv()

import os

db_path = os.environ.get("db_path")

weap = Blueprint('weap', __name__)
db = SQLAlchemy()

@weap.route('/weapon/create')
def weapon_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'weapon_create/weapon_create.html'

	weapon_includes = {'base_form': 'weapon_create/base_form.html', 'descriptor': 'weapon_create/descriptor.html', 'condition': 'weapon_create/condition.html', 'benefit': 'weapon_create/benefit.html'}

	title = 'DC Adventures Online Roleplaying Game: Create Weapon'
	stylesheets.append({"style": "/static/css/weapon_create/weapon_create.css"})

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

	powers = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()

	conditions = db.session.query(Job).filter(Condition.hide == None).order_by(Condition.name).all()

	advantages = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()

	weapon_cat = WeaponCat.query.all()
	
	materials = db.session.query(Material).order_by(Material.name).all()

	origins = db.session.query(Origin).filter(Origin.show == True).order_by(Origin.name).all()
	
	sources = db.session.query(Source).filter(Source.show == True).order_by(Source.name).all()
	
	mediums = db.session.query(MediumType).order_by(MediumType.name).all()
	
	defenses = db.session.query(Defense).filter(Defense.hide == None).order_by(Defense.name).all()

	benefits = db.session.query(Benefit).filter_by(approved=True).order_by(Benefit.name).all()

	conceal = Conceal.query.all()

	senses = db.session.query(Sense).filter(Sense.hide == None).order_by(Sense.name).all()

	condition = [{'type': '', 'name': 'Condition Type'}, {'type': 'active', 'name': 'Active Condition'}, {'type': 'change', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	area  = [{'type': '', 'name': 'Area Type'}, {'type': 'cone', 'name': 'Cone'}, {'type': 'line', 'name': 'Line'}, {'type': 'either', 'name': 'Cone or Line'}, {'type': 'burst', 'name': 'Burst'}, {'type': 'cloud', 'name': 'Cloud'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, weapon_includes=weapon_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, weapon_cat=weapon_cat, powers=powers, materials=materials, origins=origins,
							sources=sources, mediums=mediums, condition=condition, conditions=conditions, updown=updown, benefits=benefits, defenses=defenses, area=area, advantages=advantages, conceal=conceal,
							senses=senses)

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
	cat_id = request.get_json()['cat_id']
	type_id = request.get_json()['type_id']
	cost = request.get_json()['cost']
	description = request.get_json()['description']
	critical = request.get_json()['critical']
	damage = request.get_json()['damage']
	toughness = request.get_json()['toughness']
	material = request.get_json()['material']
	length = request.get_json()['length']
	length_units = request.get_json()['length_units']
	resist_dc = request.get_json()['resist_dc']
	resistance = request.get_json()['resistance']
	power_rank = request.get_json()['power_rank']
	power = request.get_json()['power']
	hands = request.get_json()['hands']
	strength = request.get_json()['strength']
	thrown = request.get_json()['thrown']
	unarmed = request.get_json()['unarmed']
	reach = request.get_json()['reach']
	ranged_attack_bonus = request.get_json()['ranged_attack_bonus']
	protect = request.get_json()['protect']
	ranged_area = request.get_json()['ranged_area']
	ranged_burst = request.get_json()['ranged_burst']
	ranged_area_damage = request.get_json()['ranged_area_damage']
	penetrate = request.get_json()['penetrate']
	attack_bonus = request.get_json()['attack_bonus']
	subtle = request.get_json()['subtle']
	perception_dc = request.get_json()['perception_dc']
	advantage = request.get_json()['advantage']
	grenade_area = request.get_json()['grenade_area']
	grenade_burst = request.get_json()['grenade_burst']
	grenade_area_damage = request.get_json()['grenade_area_damage']
	conceal = request.get_json()['conceal']
	sense = request.get_json()['sense']
	double = request.get_json()['double']
	double_mod = request.get_json()['double_mod']
	benefit = request.get_json()['benefit']
	condition = request.get_json()['condition']
	descriptor = request.get_json()['descriptor']

	weapon_id = integer(weapon_id)
	
	cat_id = db_integer(WeaponCat, cat_id)
	type_id = db_integer(WeaponType, type_id)
	material = db_integer(Material, material)
	length_units = db_integer(Unit, length_units)
	resistance = db_integer(Defense, resistance)
	power = db_integer(Power, power)
	advantage = db_integer(Advantage, advantage)
	conceal = db_integer(Conceal, conceal)
	sense = db_integer(Sense, sense)

	cost = integer(cost)
	critical = integer(critical)
	damage = integer(damage)
	toughness = integer(toughness)
	length = integer(length)
	resist_dc = integer(resist_dc)
	power_rank = integer(power_rank)
	hands = integer(hands)
	reach = integer(reach)
	ranged_attack_bonus = integer(ranged_attack_bonus)
	protect = integer(protect)
	ranged_burst = integer(ranged_burst)
	ranged_area_damage = integer(ranged_area_damage)
	attack_bonus = integer(attack_bonus)
	perception_dc = integer(perception_dc)
	grenade_burst = integer(grenade_burst)
	grenade_area_damage = integer(grenade_area_damage)
	double_mod = integer(double_mod)

	entry = db.session.query(Weapon).filter(Weapon.id == weapon_id).one()

	entry.cat_id = cat_id
	entry.type_id = type_id
	entry.cost = cost
	entry.description = description
	entry.critical = critical
	entry.damage = damage
	entry.toughness = toughness
	entry.material = material
	entry.length = length
	entry.length_units = length_units
	entry.resist_dc = resist_dc
	entry.resistance = resistance
	entry.power_rank = power_rank
	entry.power = power
	entry.hands = hands
	entry.strength = strength
	entry.thrown = thrown
	entry.unarmed = unarmed
	entry.reach = reach
	entry.ranged_attack_bonus = ranged_attack_bonus
	entry.protect = protect
	entry.ranged_area = ranged_area
	entry.ranged_burst = ranged_burst
	entry.ranged_area_damage = ranged_area_damage
	entry.penetrate = penetrate
	entry.attack_bonus = attack_bonus
	entry.subtle = subtle
	entry.perception_dc = perception_dc
	entry.advantage = advantage
	entry.grenade_area = grenade_area
	entry.grenade_burst = grenade_burst
	entry.grenade_area_damage = grenade_area_damage
	entry.conceal = conceal
	entry.sense = sense
	entry.double = double
	entry.double_mod = double_mod
	entry.benefit = benefit
	entry.condition = condition
	entry.descriptor = descriptor

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

@weap.route('/weapon/condition/create', methods=['POST'])
def weapon_post_condition():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = weap_condition_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	weapon_id = request.get_json()['weapon_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	condition_type = request.get_json()['condition_type']
	condition = request.get_json()['condition']
	condition_null = request.get_json()['condition_null']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	damage_value = request.get_json()['damage_value']
	damage = request.get_json()['damage']

	try:
		weapon_id = integer(weapon_id)
		condition = db_integer(Condition, condition)
		condition_null = db_integer(Condition, condition_null)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)

		damage_value = integer(damage_value)
		damage = integer(damage)

		entry = WeapCondition(weapon_id = weapon_id,
									condition_type = condition_type,
									condition = condition,
									condition_null = condition_null,
									condition1 = condition1,
									condition2 = condition2,
									damage_value = damage_value,
									damage = damage)

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
		table_id = 'condition'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
						
		body = weap_condition_post(entry, body, cells)
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@weap.route('/weapon/condition/delete/<weapon_id>', methods=['DELETE'])
def delete_weapon_condition(weapon_id):
	try:
		db.session.query(WeapCondition).filter_by(id=weapon_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(weapon_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': weapon_id, 'cost': False})


@weap.route('/weapon/descriptor/create', methods=['POST'])
def weapon_post_descriptor():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = weap_descriptor_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	weapon_id = request.get_json()['weapon_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	descriptor = request.get_json()['descriptor']

	weapon_id = integer(weapon_id)
	descriptor = db_integer(Descriptor, descriptor)

	entry = WeapDescriptor(weapon_id = weapon_id,
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
	
	body = weap_descriptor_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@weap.route('/weapon/descriptor/delete/<weapon_id>', methods=['DELETE'])
def delete_weapon_descriptor(weapon_id):
	try:
		db.session.query(WeapDescriptor).filter_by(id=weapon_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(weapon_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': weapon_id, 'cost': False})

@weap.route('/weapon/benefit/create', methods=['POST'])
def weapon_post_benefit():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = weap_benefit_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	weapon_id = request.get_json()['weapon_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']

	weapon_id = integer(weapon_id)
	benefit = db_integer(Benefit, benefit)

	entry = WeapBenefit(weapon_id = weapon_id,
						benefit = benefit)

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
	table_id = 'benefit'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = weap_benefit_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@weap.route('/weapon/benefit/delete/<weapon_id>', methods=['DELETE'])
def delete_weapon_benefit(weapon_id):
	try:
		db.session.query(WeapBenefit).filter_by(id=weapon_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(weapon_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': weapon_id, 'cost': False})



