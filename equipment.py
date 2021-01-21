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
from models import Equipment, Light

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

	equipment_includes = {'base_form': 'equipment_create/base_form.html', 'damaged': 'equipment_create/damaged.html', 'opposed': 'equipment_create/opposed.html', 'modifiers': 'equipment_create/modifiers.html', 'check': 'equipment_create/check.html', 'limits': 'equipment_create/limits.html', 'descriptor': 'equipment_create/descriptors.html'}

	equipment = Equipment.query.all()

	skills = Skill.query.all()

	origins = db.session.query(Origin).order_by(Origin.name).all()
	
	sources = db.session.query(Source).order_by(Source.name).all()
	
	mediums = db.session.query(MediumType).order_by(MediumType.name).all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	distances = db.session.query(Unit).filter_by(type_id=3)
	
	expertise = db.session.query(SkillBonus).filter_by(skill_id=5).all()

	damages = db.session.query(Descriptor).filter_by(damage=True).order_by(Descriptor.name).all()
	
	checks = db.session.query(Check).all()

	actions = Action.query.all()

	light = Light.query.all()
	
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

	equipment_type = [{'type': '', 'name': 'Equipment Type'}, {'type': 'general', 'name': 'General Equipment'}, {'type': 'electronics', 'name': 'Electronics'}, {'type': 'criminal', 'name': 'Criminal Gear'}, {'type': 'surveil', 'name': 'Surveillance Gear'}, {'type': 'survival', 'name': 'Survival Gear'}, {'type': 'utility', 'name': 'Utility Belt'}]

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




	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, equipment_includes=equipment_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, equipment=equipment, equipment_type=equipment_type, damaged=damaged, skills=skills,
							times=times, distances=distances, expertise=expertise, when=when, conditions=conditions, damages=damages, checks=checks, light=light, environments=environments, senses=senses,
							ranged=ranged, subsenses=subsenses, cover=cover, concealment=concealment, maneuvers=maneuvers, weapon_melee=weapon_melee, weapon_ranged=weapon_ranged, tools=tools, powers=powers,
							consequences=consequences, creatures=creatures, emotions=emotions, conflicts=conflicts, professions=professions, modifier_type=modifier_type, modifier_effect=modifier_effect,
							modifier_trigger=modifier_trigger, multiple=multiple, traits=traits, actions=actions, origins=origins, sources=sources, mediums=mediums)


@equip.route('/equipment/skill/select', methods=['POST'])
def advantage_action_select():
	body = {}
	body['success'] = True
	options = []

	skill_id = request.get_json()['skill_id'] 

	try:
		skill_id = int(skill_id)
		skill = db.session.query(Skill).filter_by(id=skill_id).one()
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


@equip.route('/equipment/medium/subtype/select', methods=['POST'])
def equip_medium_subtype_select():
	body = {}
	body['success'] = True

	medium_type_id = request.get_json()['medium_type']

	print('id ' + medium_type_id)

	try:
		medium_type = db.session.query(MediumType).filter_by(id=medium_type_id).one()
		medium_subtypes = db.session.query(MediumSubType).filter_by(medium_type=medium_type_id).order_by(MediumSubType.name).all()
		mediums = db.session.query(Medium).filter_by(medium_type=medium_type_id).order_by(Medium.name).all()
		
		all_medium_type = 'Any ' + medium_type.name

		title = medium_type.name + ' Type'

		des_title = 'New ' + medium_type.name + ' Type Description'

		medium_type_medium = medium_type.name + ' Mediums'

		options = []

		options_medium = []
		
		options.append({'id': '', 'name': medium_type.name})

		options_medium.append({'id': '', 'name': medium_type.name})

		for subtype in medium_subtypes:
			options.append({'id': subtype.id, 'name': subtype.name})

		for medium in mediums:
			options_medium.append({'id': medium.id, 'name': medium.name})

		body['options'] = options
		body['options_medium'] = options_medium
		body['title'] = title
		body['des_title'] = des_title

	except:
		body['success'] = False
		body['options'] = 'no results'

	print(body)
	return jsonify(body)

@equip.route('/equipment/medium/select', methods=['POST'])
def equip_medium_select():
	body = {}
	body['success'] = True
	
	medium_subtype = request.get_json()['medium_subtype']
	options = []

	print('id ' + medium_subtype)

	if medium_subtype != '' and medium_subtype != 'all' and medium_subtype != 'new':
		try:
			subtype = db.session.query(MediumSubType).filter_by(id=medium_subtype).one()
			mediums = db.session.query(Medium).filter_by(medium_subtype=medium_subtype).order_by(Medium.name).all()
			
			all_subtype = 'Any ' + subtype.name

			options.append({'id': '', 'name': subtype.name})


			for medium in mediums:
				options.append({'id': medium.id, 'name': medium.name})

		except:
			db.session.rollback()
			options.append({'id': '', 'name': 'Medium'})
		finally:
			db.session.close()
	else:
		options.append({'id': '', 'name': 'Medium'})

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
