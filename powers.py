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
from models import setup_db, Ability, Power, Extra, Defense, Modifier, Complex, Action, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

powers = Blueprint('powers', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

@powers.route('/power/create')
def power_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'power_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Power'
	stylesheets.append({"style": "/static/css/power_create.css"})

	power_includes = {'base_form': 'power_create/base_form.html', 'range': 'power_create/range.html', 'resisted_by': 'power_create/resisted_by.html', 'reverse_effect': 'power_create/reverse_effect.html', 'move': 'power_create/move.html', 'levels': 'power_create/levels.html', 'category': 'power_create/category.html', 'sense': 'power_create/sense.html', 'ranks': 'power_create/ranks.html', 'circ': 'power_create/circumstance_table.html', 'create': 'power_create/create.html', 'damage': 'power_create/damage.html', 'extras': 'power_create/extras.html'}
	
	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	positives = []
	for i in range(1, 41, 1):
		positives.append(i)

	time_numbers = []
	for i in range(1, 61, 1):
		positives.append(i)

	power_type = [{'type': 'attack', 'name': 'Attack'}, 
					{'type': 'move', 'name': 'Movement'},  
					{'type': 'sense', 'name': 'Sensory'},
					{'type': 'control', 'name': 'Control'}, 
					{'type': 'defense', 'name': 'Defense'}, 
					{'type': 'general', 'name': 'General'}]

	action_type = [{'type': 'standard', 'name': 'Standard Action'},
					{'type': 'move', 'name': 'Move Action'},
					{'type': 'free', 'name': 'Free Action'},
					{'type': 'reaction', 'name': 'Reaction'},
					{'type': 'none', 'name': 'None'}]

	range_type = [{'type': 'personal', 'name': 'Personal'}, 
					{'type': 'close', 'name': 'Close'}, 
					{'type': 'ranged', 'name': 'Ranged'}, 
					{'type': 'perception', 'name': 'Perception'}, 
					{'type': 'rank', 'name': 'Rank Table'}]

	duration_type = [{'type': 'instant', 'name': 'Instant'}, 
						{'type': 'conc', 'name': 'Concentration'}, 
						{'type': 'sustained', 'name': 'Sustained'},
						{'type': 'cont', 'name': 'Continuous'},
						{'type': 'perm', 'name': 'Permanent'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Power Rank'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	distance = db.session.query(Unit).filter_by(type_id=3)

	checks = Check.query.all()

	actions = Action.query.all()

	skills = Skill.query.all()

	abilities = Ability.query.all()

	defenses = Defense.query.all()

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	check_types = [{'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}]

	base_conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	effects = [{'type': 'condition', 'name': 'Condition'}, {'type': 'damage', 'name': 'Damage'}]

	dc_value = [{'type': '', 'name': 'DC Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]

	whens = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]

	maths = Math.query.all()

	times = db.session.query(Unit).filter_by(type_id=2)

	distances = db.session.query(Unit).filter_by(type_id=3)

	permanence = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	
	partners = [{'type': '', 'name': 'N/A'}, {'type': 'power', 'name': 'Same Power'}, {'type': 'device', 'name': 'Device'}, {'type': 'both', 'name': 'Power or Device'}]

	senses = Sense.query.all()

	subsenses = SubSense.query.all()

	sense_type =  [{'type': '', 'name': 'Effect Type'}, {'type': 'height', 'name': 'Heightened'}, {'type': 'resist', 'name': 'Resistant'}]

	visual = db.session.query(SubSense).filter_by(sense_id=6)
	
	auditory = db.session.query(SubSense).filter_by(sense_id=7)

	olfactory = db.session.query(SubSense).filter_by(sense_id=8)

	tactile = db.session.query(SubSense).filter_by(sense_id=9)

	radio = db.session.query(SubSense).filter_by(sense_id=10)

	mental = db.session.query(SubSense).filter_by(sense_id=11)

	special = db.session.query(SubSense).filter_by(sense_id=12)

	power_sense = ['Accurate', 'Acute', 'Analytical', 'Awareness', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision', 'Detect', 'Direction Sense', 'Distance Sense', 'Extended', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Ranged', 'Rapid', 'Time Sense', 'Tracking', 'Ultra-Hearing', 'Ultravision']

	circumstances = [{'type': '', 'name': 'N/A'}, {'type': 'gm', 'name': 'Set by GM'}, {'type': 'table', 'name': 'Circumstance Table'}]

	required = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	heightened = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	resistant = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	value_bonus = [{'type': 'value', 'name': 'Value'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses = sorted(bonuses_raw)

	all_some = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	sense_time = [{'type': '', 'name': ''}, {'type': 'value', 'name': 'Value'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	sense_distance = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'rank', 'name': 'By Rank'}]

	darkness = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]

	determined = [{'type': '', 'name': 'Determined By'}, {'type': 'dc', 'name': 'DC'}, {'type': 'target', 'name': 'Target Trait'}, {'type': 'player', 'name': 'Player Trait'}]

	traits = [{'type': '', 'name': 'Trait'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	object_damage = [{'type': '', 'name': 'Damage Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'effect', 'name': 'Effect Rank'}, {'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}, {'type': 'ability', 'name': 'Player Ability'}]

	solidity = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]

	visibility = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]

	against = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]

	moveable = [{'type': '', 'name': 'Moveable With'}, {'type': None, 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]

	complexity = Complex.query.all()

	return render_template('template.html', sense_time=sense_time, all_some=all_some, power_sense=power_sense, bonuses=bonuses, sense_type=sense_type, visual=visual, auditory=auditory, olfactory=olfactory, 
											tactile=tactile, radio=radio, mental=mental, special=special, value_bonus=value_bonus, heightened=heightened, resistant=resistant, required=required, circumstances=circumstances, 
											senses=senses, subsenses=subsenses, actions=actions, permanence=permanence, time_numbers=time_numbers, maths=maths, times=times, targets=targets, whens=whens, dc_value=dc_value, 
											effects=effects, conditions=conditions, check_types=check_types, powers=powers, skills=skills, abilities=abilities, defenses=defenses, checks=checks, dc_type=dc_type, 
											distance=distance, negatives=negatives, positives=positives, power_type=power_type, action_type=action_type, range_type=range_type, duration_type=duration_type, 
											power_includes=power_includes, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar, includehtml=includehtml, title=title, 
											sense_distance=sense_distance, against=against, traits=traits, object_damage=object_damage, darkness=darkness, solidity=solidity, partners=partners, visibility=visibility,
											moveable=moveable, complexity=complexity)

@skills.route('/power/trait/select', methods=['POST'])
def power_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json['trait'] 

	skills_query = Skill.query.all()
	skills_raw = []
	for skill in skills_query:
		skills_raw.append(skill.name)
	skills = sorted(skills_raw)

	abilities_query = Ability.query.all()
	abilities_raw = []
	for ability in abilities_query:
		abilities_raw.append(ability.name)
	abilities = sorted(abilities_raw)

	defenses_query = Defense.query.all()
	defenses_raw = []
	for defense in defenses_query:
		defenses_raw.append(defense.name)
	defenses = sorted(defenses_raw)

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses = sorted(bonuses_raw)

	if trait == 'ability':
		body['options'] = abilities
	elif trait == 'defense':
		body['options'] = defenses
	elif trait == 'skill':
		body['options'] = skills
	elif trait == 'bonus':
		body['options'] = bonuses
	elif trait == 'power':
		body['options'] = powers
	else:
		body['success'] = False
		body['options'] = 'no match'

	return jsonify(body)


@skills.route('/power/create', methods=['POST'])
def post_power(): 
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

	power = db.session.query(Power).filter(Power.name == name).first()

	if power is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already a power with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_power = Power(name=name)
		db.session.add(new_power)
		db.session.commit()
		body['success'] = True
		body['id'] = new_power.id
		body['name'] = new_power.name
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

@skills.route('/power/edit_name', methods=['POST'])
def edit_power_name(): 
	body = {}
	error = False
	error_msgs = []

	power_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	power = db.session.query(Power).filter(Power.name == name).first()
	
	if power is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already a power with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_power = db.session.query(Power).filter(Power.id == edit_power).one()
		edit_power.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_power.id
		body['name'] = edit_power.name
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


@skills.route('/power/extra/create', methods=['POST'])
def post_extra_create():
	body = {}
	body['success'] = True
	error = False
	error_msgs = []
	

	name = request.get_json['name'] 
	power_id = request.get_json['power_id']
	cost = request.get_json['cost']
	ranks = request.get_json['ranks'] 
	des = request.get_json['des'] 
	inherit = request.get_json['inherit']

	power = db.session.query(Extra).filter(Extra.name == name).first()

	if power is not None:
		error = True
		body['success'] = False
		error_msgs.append('You have already created an extra with that name with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)

	try:
		power = Extra(power_id=power_id, name=name, cost=cost, ranks=ranks, des=des, inherit=inherit)
		db.session.add(power)
		db.session.commit()

		body['id'] = power.id
		body['name'] = power.name
		body['power_id'] = power.power_id
		body['cost'] = power.cost
		body['ranks'] = power.ranks
		body['des'] = power.des
		body['inherit'] = power.inherit

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

@skills.route('/power/extra/delete/<power_id>', methods=['DELETE'])
def delete_extra(power_id):
	try:
		db.session.query(Extra).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify({'success': True})