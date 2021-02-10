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


from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add
from posts.equipment_posts import equip_belt_post, equip_check_post, equip_damaged_post, equip_descriptor_post, equip_effect_post, equip_feature_post, equip_limits_post, equip_modifiers_post, equip_opposed_post
from errors.equipment_errors import equip_belt_post_errors, equip_check_post_errors, equip_damaged_post_errors, equip_descriptor_post_errors, equip_effect_post_errors, equip_feature_post_errors, equip_limits_post_errors, equip_modifiers_post_errors, equip_opposed_post_errors, equip_save_errors, feature_save_errors

load_dotenv()

import os

db_path = os.environ.get("db_path")

equip = Blueprint('equipment', __name__)
db = SQLAlchemy()

@equip.route('/equipment/create')
def equipment_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'equipment_create/equipment_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Equipment'
	stylesheets.append({"style": "/static/css/equipment_create/equipment_create.css"})

	equipment_includes = {'base_form': 'equipment_create/base_form.html', 'damaged': 'equipment_create/damaged.html', 'opposed': 'equipment_create/opposed.html', 'modifiers': 'equipment_create/modifiers.html', 'check': 'equipment_create/check.html', 'limits': 'equipment_create/limits.html', 'descriptor': 'equipment_create/descriptors.html', 'feature': 'equipment_create/feature.html', 'effect': 'equipment_create/effect.html', 'belt': 'equipment_create/belt.html'}

	equipment = Equipment.query.all()

	weapon_cat = WeaponCat.query.all()

	old_feature = ''

	features = db.session.query(Feature).filter(Feature.name != old_feature).order_by(Feature.name).all()

	skills = Skill.query.all()

	origins = db.session.query(Origin).order_by(Origin.name).all()
	
	sources = db.session.query(Source).order_by(Source.name).all()
	
	mediums = db.session.query(MediumType).order_by(MediumType.name).all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	distances = db.session.query(Unit).filter_by(type_id=3)
	
	expertise = db.session.query(SkillBonus).filter_by(skill_id=5).all()

	damages = db.session.query(Descriptor).filter_by(damage=True).order_by(Descriptor.name).all()
	
	light = Light.query.all()
	
	checks = db.session.query(Check).all()

	actions = Action.query.all()
	
	environments = db.session.query(Environment).order_by(Environment.name).all()
	
	senses = db.session.query(Sense).order_by(Sense.name).all()
	
	ranged = db.session.query(Ranged).filter_by(show=True)

	subsenses = db.session.query(SubSense).order_by(SubSense.name).all()

	cover = Cover.query.all()

	concealment = Conceal.query.all()

	maneuvers = db.session.query(Maneuver).order_by(Maneuver.name).all()
	
	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1).all()
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	creatures = db.session.query(Creature).order_by(Creature.name).all()
		
	emotions = db.session.query(Emotion).order_by(Emotion.name).all()

	conflicts = db.session.query(ConflictAction).order_by(ConflictAction.name).all()

	professions = db.session.query(Job).order_by(Job.name).all()
	

	base_conditions = Condition.query.all()
	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

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

	equipment_type = EquipType.query.all()

	damaged = [{'type': '', 'name': 'Damaged Effect'}, {'type': 'feature', 'name': 'Loses a Feature'}, {'type': 'circ', 'name': '-1 Circumstance'}]

	when = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]
	
	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'distance', 'name': 'Distance Penalty'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}, {'type': 'skill', 'name': 'Skill Check'}, {'type': 'light', 'name': 'Lighting'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	simultaneous = [{'type': '', 'name': 'Type'}, {'type': 'same', 'name': 'At Same Time'}, {'type': 'maintain', 'name': 'While Maintaining Previous'}, {'type': 'both', 'name': 'Either'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_advantage', 'name': 'This Advantage'}, {'type': 'any', 'name': 'Any Trait'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}, {'type': 'advantage', 'name': 'Advantage'}]

	belt = [{'type': '', 'name': 'Add Item'}, {'type': 'equip', 'name': 'Equipment'}, {'type': 'weapon', 'name': 'Weapon'}, {'type': 'feature', 'name': 'Feature'}]

	move = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}]

	locks = [{'type': '', 'name': 'Lock Type'}, {'type': 'keys', 'name': 'Keys'}, {'type': 'electric', 'name': 'Electronic'}, {'type': 'both', 'name': 'Both'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, equipment_includes=equipment_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, equipment=equipment, equipment_type=equipment_type, damaged=damaged, skills=skills,
							times=times, distances=distances, expertise=expertise, when=when, conditions=conditions, damages=damages, checks=checks, light=light, environments=environments, senses=senses,
							ranged=ranged, subsenses=subsenses, cover=cover, concealment=concealment, maneuvers=maneuvers, weapon_melee=weapon_melee, weapon_ranged=weapon_ranged, tools=tools, powers=powers,
							consequences=consequences, creatures=creatures, emotions=emotions, conflicts=conflicts, professions=professions, modifier_type=modifier_type, modifier_effect=modifier_effect,
							modifier_trigger=modifier_trigger, multiple=multiple, traits=traits, actions=actions, origins=origins, sources=sources, mediums=mediums, weapon_cat=weapon_cat, features=features, belt=belt,
							move=move, locks=locks)



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
		message = 'There is already an item of equipment with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

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
		errors['error_msgs'] = error_msgs
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
	type_id = request.get_json()['type_id']
	cost = request.get_json()['cost']
	description = request.get_json()['description']
	toughness = request.get_json()['toughness']
	expertise = request.get_json()['expertise']
	alternate = request.get_json()['alternate']
	move = request.get_json()['move']
	speed_mod = request.get_json()['speed_mod']
	direction = request.get_json()['direction']
	locks = request.get_json()['locks']
	lock_type = request.get_json()['lock_type']
	mod_multiple = request.get_json()['mod_multiple']
	mod_multiple_count = request.get_json()['mod_multiple_count']
	check = request.get_json()['check']
	damaged = request.get_json()['damaged']
	descriptor = request.get_json()['descriptor']
	feature = request.get_json()['feature']
	limits = request.get_json()['limits']
	modifiers = request.get_json()['modifiers']
	opposed = request.get_json()['opposed']

	equip_id = integer(equip_id)
	type_id = db_integer(type_id)
	cost = integer(cost)
	toughness = integer(toughness)
	expertise = db_integer(expertise)
	speed_mod = integer(speed_mod)
	mod_multiple_count = integer(mod_multiple_count)

	if feature:
		features = db.session.query(Feature).filter_by(equip_id = equip_id).count()
		cost += features

	entry = db.session.query(Equipment).filter(Equipment.id == equip_id).one()

	entry.type_id = type_id
	entry.cost = cost
	entry.description = description
	entry.toughness = toughness
	entry.expertise = expertise
	entry.alternate = alternate
	entry.move = move
	entry.speed_mod = speed_mod
	entry.direction = direction
	entry.locks = locks
	entry.lock_type = lock_type
	entry.mod_multiple = mod_multiple
	entry.mod_multiple_count = mod_multiple_count
	entry.check = check
	entry.damaged = damaged
	entry.descriptor = descriptor
	entry.feature = feature
	entry.limits = limits
	entry.modifiers = modifiers
	entry.opposed = opposed

	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@equip.route('/equipment/feature/save', methods=['POST'])
def save_feature(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = feature_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@equip.route('/feature/save/success')
def feature_save_success():
	
	flash('Features Successfully Created')
	return redirect(url_for('home'))


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

	
@equip.route('/equipment/belt/create', methods=['POST'])
def equipment_post_belt():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_belt_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	feature = request.get_json()['feature']
	weapon = request.get_json()['weapon']
	equipment = request.get_json()['equipment']
	belt_item_type = request.get_json()['belt_item_type']

	equip_id = db_integer(equip_id)
	feature = db_integer(feature)
	weapon = db_integer(weapon)
	equipment = db_integer(equipment)
	
	if belt_item_type == 'equip':
		cost_query = db.session.query(Equipment).filter_by(id=equipment).one()
		cost = cost_query.cost		
	elif belt_item_type == 'weapon':
		cost_query = db.session.query(Weapon).filter_by(id=weapon).one()
		cost = cost_query.cost
	elif belt_item_type == 'feature':
		cost = int(1)
	else:
		cost = None


	entry = EquipBelt(equip_id = equip_id,
						feature = feature,
						weapon = weapon,
						equipment = equipment,
						cost = cost,
						belt_item_type = belt_item_type)

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
	table_id = 'belt'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font

	total_cost = 0
	total_cost_query =  db.session.query(EquipBelt).filter_by(equip_id=equip_id).all()
	for c in total_cost_query:
		total_cost += c.cost

	body['total_cost'] = total_cost

	body = equip_belt_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/belt/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_belt(equipment_id):
	try:
		
		get_id = db.session.query(EquipBelt).filter_by(id=equipment_id).one()
		equip_id = get_id.equip_id

		db.session.query(EquipBelt).filter_by(id=equipment_id).delete()
		db.session.commit()


		total_cost = 0
		cost_query = db.session.query(EquipBelt).filter_by(equip_id=equip_id).first()
		if cost_query is None:
			total_cost = 0
		else:
			cost_query = db.session.query(EquipBelt).filter_by(equip_id=equip_id).all()
			for c in cost_query:
				total_cost += c.cost
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': True, 'total_cost': total_cost, 'feature': False})

	
@equip.route('/equipment/check/create', methods=['POST'])
def equipment_post_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	when = request.get_json()['when']
	skill_type = request.get_json()['skill_type']
	skill = request.get_json()['skill']
	check_type = request.get_json()['check_type']
	action = request.get_json()['action']
	action_time = request.get_json()['action_time']

	equip_id = db_integer(equip_id)
	effect = db_integer(effect)
	feature = db_integer(feature)
	skill_type = db_integer(skill_type)
	skill = db_integer(skill)
	check_type = db_integer(check_type)
	action = db_integer(action)

	entry = EquipCheck(equip_id = equip_id,
						effect = effect,
						feature = feature,
						when = when,
						skill_type = skill_type,
						skill = skill,
						check_type = check_type,
						action = action,
						action_time = action_time)

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
	table_id = 'check'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = equip_check_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/check/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_check(equipment_id):
	try:
		db.session.query(EquipCheck).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})
	
@equip.route('/equipment/damaged/create', methods=['POST'])
def equipment_post_damaged():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()
	write = True
	error_msgs = []

	errors = equip_damaged_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	damage = request.get_json()['damage']
	skill_type = request.get_json()['skill_type']
	skill = request.get_json()['skill']
	toughness = request.get_json()['toughness']
	penalty = request.get_json()['penalty']

	equip_id = db_integer(equip_id)
	effect = db_integer(effect)
	feature = db_integer(feature)
	damage = db_integer(damage)
	skill_type = db_integer(skill_type)
	skill = db_integer(skill)
	toughness = integer(toughness)

	if feature is not None:
		try:
			f = db.session.query(Feature).filter_by(id=feature).one()
			f.toughness = toughness
		except:
			write = False
			error_msgs.append('The feature you selected for this rule is invalid.  You may have deleted it.')
		
	entry = EquipDamage(equip_id = equip_id,
						effect = effect,
						feature = feature,
						damage = damage,
						skill_type = skill_type,
						skill = skill,
						toughness = toughness,
						penalty = penalty)

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
	table_id = 'damaged'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = equip_damaged_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/damaged/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_damaged(equipment_id):
	try:
		db.session.query(EquipDamage).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})
	
@equip.route('/equipment/descriptor/create', methods=['POST'])
def equipment_post_descriptor():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_descriptor_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	descriptor = request.get_json()['descriptor']

	equip_id = db_integer(equip_id)
	effect = db_integer(effect)
	feature = db_integer(feature)
	descriptor = db_integer(descriptor)

	entry = EquipDescriptor(equip_id = equip_id,
							effect = effect,
							feature = feature,
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
	
	body = equip_descriptor_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/descriptor/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_descriptor(equipment_id):
	try:
		db.session.query(EquipDescriptor).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})

	
@equip.route('/equipment/effect/create', methods=['POST'])
def equipment_post_effect():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_effect_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	name = request.get_json()['name']
	description = request.get_json()['description']

	equip_id = db_integer(equip_id)

	entry = EquipEffect(equip_id = equip_id,
						name = name,
						description = description)

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
	table_id = 'effect'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
				
	body = equip_effect_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/effect/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_effect(equipment_id):
	try:
		db.session.query(EquipEffect).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})

	
@equip.route('/equipment/feature/create', methods=['POST'])
def equipment_post_feature():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_feature_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	name = request.get_json()['name']
	description = request.get_json()['description']
	feature = request.get_json()['feature']

	equip_id = db_integer(equip_id)
	feature = db_integer(feature)

	if feature is not None:
		old_feature = db.session.query(Feature).filter_by(id=feature).one()
		description = old_feature.description

	entry = Feature(equip_id = equip_id,
					name = name,
					description = description,
					feature = feature)

	db.session.add(entry)
	db.session.commit()

	body = {}
	body['id'] = entry.id
	body['name'] = entry.name	
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
	
	body = equip_feature_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/feature/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_feature(equipment_id):
	try:
		name_check = db.session.query(Feature).filter_by(id=equipment_id).one()
		if name_check.name != '':
			feature = True
		else:
			feature = False
		db.session.query(Feature).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': feature})

	
@equip.route('/equipment/limits/create', methods=['POST'])
def equipment_post_limits():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_limits_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	time = request.get_json()['time']
	time_units = request.get_json()['time_units']
	range = request.get_json()['range']
	range_units = request.get_json()['range_units']
	extend = request.get_json()['extend']
	extendable = request.get_json()['extendable']
	time_capacity = request.get_json()['time_capacity']
	time_capacity_units = request.get_json()['time_capacity_units']
	capacity = request.get_json()['capacity']
	item = request.get_json()['item']
	ammo = request.get_json()['ammo']
	fuel = request.get_json()['fuel']
	area_long = request.get_json()['area_long']
	area_wide = request.get_json()['area_wide']
	area_units = request.get_json()['area_units']
	recharge = request.get_json()['recharge']
	refill = request.get_json()['refill']
	uses = request.get_json()['uses']
	light = request.get_json()['light']
	internet = request.get_json()['internet']
	needs_internet = request.get_json()['needs_internet']

	
	equip_id = db_integer(equip_id)
	effect = db_integer(effect)
	feature = db_integer(feature)
	time = integer(time)
	time_units = db_integer(time_units)
	range = integer(range)
	range_units = db_integer(range_units)
	time_capacity = integer(time_capacity)
	time_capacity_units = db_integer(time_capacity_units)
	capacity = integer(capacity)
	area_long = integer(area_long)
	area_wide = integer(area_wide)
	area_units = db_integer(area_units)
	uses = integer(uses)
	light = db_integer(light)
	

	entry = EquipLimit(equip_id = equip_id,
						effect = effect,
						feature = feature,
						time = time,
						time_units = time_units,
						range = range,
						range_units = range_units,
						extend = extend,
						extendable = extendable,
						time_capacity = time_capacity,
						time_capacity_units = time_capacity_units,
						capacity = capacity,
						item = item,
						ammo = ammo,
						fuel = fuel,
						area_long = area_long,
						area_wide = area_wide,
						area_units = area_units,
						recharge = recharge,
						refill = refill,
						uses = uses,
						light = light,
						internet = internet,
						needs_internet = needs_internet)

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
	table_id = 'limits'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = equip_limits_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/limits/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_limits(equipment_id):
	try:
		db.session.query(EquipLimit).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})

	
@equip.route('/equipment/modifiers/create', methods=['POST'])
def equipment_post_modifiers():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_modifiers_post_errors(data)

	equip_id = request.get_json()['equip_id']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	bonus = request.get_json()['bonus']
	bonus_type = request.get_json()['bonus_type']
	penalty = request.get_json()['penalty']
	penalty_type = request.get_json()['penalty_type']
	trigger = request.get_json()['trigger']
	bonus_effect = request.get_json()['bonus_effect']
	penalty_effect = request.get_json()['penalty_effect']
	environment = request.get_json()['environment']
	environment_other = request.get_json()['environment_other']
	sense = request.get_json()['sense']
	mod_range = request.get_json()['mod_range']
	subsense = request.get_json()['subsense']
	cover = request.get_json()['cover']
	conceal = request.get_json()['conceal']
	maneuver = request.get_json()['maneuver']
	weapon_melee = request.get_json()['weapon_melee']
	weapon_ranged = request.get_json()['weapon_ranged']
	tools = request.get_json()['tools']
	condition = request.get_json()['condition']
	power = request.get_json()['power']
	consequence = request.get_json()['consequence']
	creature = request.get_json()['creature']
	creature_other = request.get_json()['creature_other']
	emotion = request.get_json()['emotion']
	emotion_other = request.get_json()['emotion_other']
	conflict = request.get_json()['conflict']
	profession = request.get_json()['profession']
	profession_other = request.get_json()['profession_other']
	bonus_trait_type = request.get_json()['bonus_trait_type']
	bonus_trait = request.get_json()['bonus_trait']
	bonus_check = request.get_json()['bonus_check']
	bonus_check_range = request.get_json()['bonus_check_range']
	bonus_conflict = request.get_json()['bonus_conflict']
	penalty_trait_type = request.get_json()['penalty_trait_type']
	penalty_trait = request.get_json()['penalty_trait']
	penalty_check = request.get_json()['penalty_check']
	penalty_check_range = request.get_json()['penalty_check_range']
	penalty_conflict = request.get_json()['penalty_conflict']
	bonus_active_defense = request.get_json()['bonus_active_defense']
	bonus_conflict_defend = request.get_json()['bonus_conflict_defend']
	penalty_active_defense = request.get_json()['penalty_active_defense']
	penalty_conflict_defend = request.get_json()['penalty_conflict_defend']
	multiple = request.get_json()['multiple']
	multiple_count = request.get_json()['multiple_count']
	lasts = request.get_json()['lasts']
	skill = request.get_json()['skill']
	light = request.get_json()['light']

	error = errors['error']

	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	body = {}

	try:
		environment = db_integer(environment)
		sense = db_integer(sense)
		mod_range = db_integer(mod_range)
		subsense = db_integer(subsense)
		cover = db_integer(cover)
		conceal = db_integer(conceal)
		maneuver = db_integer(maneuver)
		weapon_melee = db_integer(weapon_melee)
		weapon_ranged = db_integer(weapon_ranged)
		consequence = db_integer(consequence)
		creature = db_integer(creature)
		emotion = db_integer(emotion)
		conflict = db_integer(conflict)
		profession = db_integer(profession)
		bonus_check = db_integer(bonus_check)
		bonus_check_range = db_integer(bonus_check_range)
		bonus_conflict = db_integer(bonus_conflict)
		penalty_check = db_integer(penalty_check)
		penalty_check_range = db_integer(penalty_check_range)
		penalty_conflict = db_integer(penalty_conflict)
		skill = db_integer(skill)
		light = db_integer(light)
		equip_id = db_integer(equip_id)
		feature = db_integer(feature)
		effect = db_integer(effect)


		body['new'] = False
		new_items = []

		if emotion == 'other':	
			entry = Emotion(name=emotion_other)
			db.session.add(entry)
			db.session.commit()
			emotion = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = False
			item['field'] = 'modifiers_emotion'
			new_items.append(item)
			db.session.close()

		if environment == 'other':	
			entry = Environment(name=environment_other)
			db.session.add(entry)
			db.session.commit()
			environment = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = False
			item['field'] = 'modifiers_environment'
			new_items.append(item)
			db.session.close()

		if creature == 'other':	
			entry = Creature(name=creature_other)
			db.session.add(entry)
			db.session.commit()
			creature = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = False
			item['field'] = 'modifiers_creature'
			new_items.append(item)
			db.session.close()

		if profession == 'other':	
			entry = Job(name=profession_other)
			db.session.add(entry)
			db.session.commit()
			profession = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = False
			item['field'] = 'modifiers_profession'
			new_items.append(item)
			db.session.close()

		body['new_items'] = new_items

		equip_id = integer(equip_id)
		feature = integer(feature)
		effect = integer(effect)
		skill = integer(skill)
		light = integer(light)
		bonus = integer(bonus)
		penalty = integer(penalty)
		environment = integer(environment)
		sense = integer(sense)
		mod_range = integer(mod_range)
		subsense = integer(subsense)
		cover = integer(cover)
		conceal = integer(conceal)
		maneuver = integer(maneuver)
		weapon_melee = integer(weapon_melee)
		weapon_ranged = integer(weapon_ranged)
		consequence = integer(consequence)
		creature = integer(creature)
		emotion = integer(emotion)
		conflict = integer(conflict)
		profession = integer(profession)
		bonus_check = integer(bonus_check)
		bonus_check_range = integer(bonus_check_range)
		bonus_conflict = integer(bonus_conflict)
		penalty_check = integer(penalty_check)
		penalty_check_range = integer(penalty_check_range)
		penalty_conflict = integer(penalty_conflict)
		multiple_count = integer(multiple_count)
		lasts = integer(lasts)
		skill = integer(skill)
		light = integer(light)

		entry = EquipMod(equip_id = equip_id,
							effect = effect,
							feature = feature,
							bonus = bonus,
							bonus_type = bonus_type,
							penalty = penalty,
							penalty_type = penalty_type,
							trigger = trigger,
							bonus_effect = bonus_effect,
							penalty_effect = penalty_effect,
							environment = environment,
							environment_other = environment_other,
							sense = sense,
							mod_range = mod_range,
							subsense = subsense,
							cover = cover,
							conceal = conceal,
							maneuver = maneuver,
							weapon_melee = weapon_melee,
							weapon_ranged = weapon_ranged,
							tools = tools,
							condition = condition,
							power = power,
							consequence = consequence,
							creature = creature,
							creature_other = creature_other,
							emotion = emotion,
							emotion_other = emotion_other,
							conflict = conflict,
							profession = profession,
							profession_other = profession_other,
							bonus_trait_type = bonus_trait_type,
							bonus_trait = bonus_trait,
							bonus_check = bonus_check,
							bonus_check_range = bonus_check_range,
							bonus_conflict = bonus_conflict,
							penalty_trait_type = penalty_trait_type,
							penalty_trait = penalty_trait,
							penalty_check = penalty_check,
							penalty_check_range = penalty_check_range,
							penalty_conflict = penalty_conflict,
							bonus_active_defense = bonus_active_defense,
							bonus_conflict_defend = bonus_conflict_defend,
							penalty_active_defense = penalty_active_defense,
							penalty_conflict_defend = penalty_conflict_defend,
							multiple = multiple,
							multiple_count = multiple_count,
							lasts = lasts,
							skill = skill,
							light = light)

		db.session.add(entry)
		db.session.commit()
		
		body['id'] = entry.id
		error = False
		error_msg = []	
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'modifiers'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		
		body = equip_modifiers_post(entry, body, cells)
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)

@equip.route('/equipment/modifiers/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_modifiers(equipment_id):
	try:
		db.session.query(EquipMod).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})


@equip.route('/equipment/opposed/create', methods=['POST'])
def equipment_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = equip_opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	equip_id = request.get_json()['equip_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	effect = request.get_json()['effect']
	feature = request.get_json()['feature']
	dc = request.get_json()['dc']
	skill_type = request.get_json()['skill_type']
	skill = request.get_json()['skill']
	check = request.get_json()['check']
	when = request.get_json()['when']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	
	equip_id = db_integer(equip_id)
	effect = db_integer(effect)
	feature = db_integer(feature)
	dc = integer(dc)
	skill_type = db_integer(skill_type)
	skill = db_integer(skill)
	check = db_integer(check)

	entry = EquipOpposed(equip_id = equip_id,
						effect = effect,
						feature = feature,
						dc = dc,
						skill_type = skill_type,
						skill = skill,
						check = check,
						when = when,
						condition1 = condition1,
						condition2 = condition2)

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
	table_id = 'opposed'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = equip_opposed_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@equip.route('/equipment/opposed/delete/<equipment_id>', methods=['DELETE'])
def delete_equipment_opposed(equipment_id):
	try:
		db.session.query(EquipOpposed).filter_by(id=equipment_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(equipment_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': equipment_id, 'cost': False, 'feature': False})


