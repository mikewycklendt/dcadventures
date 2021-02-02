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
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus
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



load_dotenv()

import os

db_path = os.environ.get("db_path")

skill = Blueprint('skill', __name__)
db = SQLAlchemy()

@skill.route('/skill/create')
def headquarters_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'skill_create/skill_create.html'

	skill_includes = {'base_form': 'skill_create/base_form.html', 'dc': 'skill_create/dc_table.html', 'levels': 'skill_create/levels.html', 'degree_mod': 'skill_create/degree_mod.html', 'circ': 'skill_create/circ.html'}
	
	title = 'DC Adventures Online Roleplaying Game: Create Enhanced Skill'
	stylesheets.append({"style": "/static/css/skill_create/skill_create.css"})

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
	
	base_conditions = Condition.query.all()
	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)
	
	skills = Skill.query.all()

	checks = Check.query.all()

	actions = Action.query.all()

	defenses = Defense.query.all()

	skill_type = SkillType.query.all()

	maths = Math.query.all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	unit_type = MeasureType.query.all()

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_bonus', 'name': 'This Skill'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}]
	elif trait == 'speed':	
		body['options'] = [{'id': 'Speed Rank', 'name': 'Speed Rank'}] 
	elif trait == 'intim':
		body['options'] = [{'id': 'Intimidation Rank', 'name': 'Intimidation Rank'}
	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'uncontrolled', 'name': 'Effect Uncontrolled'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}]

	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	updown = [{'id': '', 'name': 'Direction'}, {'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	circ_effect = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'measure', 'name': 'If Measurement'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, skill_includes=skill_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, skills=skills, checks=checks, actions=actions, skill_type=skill_type, maths=maths,
							value_type=value_type, traits=traits, level_types=level_types, conditions=conditions, targets=targets, deg_mod_type=deg_mod_type, action_type=action_type, knowledge=knowledge,
							consequences=consequences, specificity=specificity, measure_rank=measure_rank, condition_type=condition_type, updown=updown, circ_effect=circ_effect, measure_effect=measure_effect,
							unit_type=unit_type)


@skill.route('/skill/create', methods=['POST'])
def post_skill_bonus(): 
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

	bonus = db.session.query(SkillBonus).filter(SkillBonus.name == name).first()

	if bonus is not None:
		error = True
		body['success'] = False
		message = 'There is already an enhanced skill with that name'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_bonus = SkillBonus(name=name)
		db.session.add(new_bonus)
		db.session.commit()
		body['success'] = True
		body['id'] = new_bonus.id
		body['name'] = new_bonus.name
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

@skill.route('/skill/save', methods=['POST'])
def save_skill_bonus(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = skill_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	bonus_id = request.get_json()['bonus_id']

	bonus_id = db_integer(bonus_id)

	entry = db.session.query(SkillBonus).filter(SkillBonus.id == bonus_id).one()

	db.session.commit()

	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@skill.route('/skill/save/success/<id>')
def skill_bonus_save_success(id):	
	bonus = db.session.query(SkillBonus).filter_by(id=id).one()
	
	flash('Enhanced Skill ' + bonus.name + ' Successfully Created')
	return redirect(url_for('home'))

@skill.route('/skill/edit_name', methods=['POST'])
def edit_skill_bonus_name(): 
	body = {}
	error = False
	error_msgs = []

	bonus_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	bonus = db.session.query(SkillBonus).filter(SkillBonus.name == name).first()
	
	if bonus is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an Enhanced Skill with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_bonus = db.session.query(SkillBonus).filter(SkillBonus.id == bonus_id).one()
		edit_bonus.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_bonus.id
		body['name'] = edit_bonus.name
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



@skill.route('/skill//create', methods=['POST'])
def skill_bonus_post_():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill__post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	bonus_id = request.get_json()['bonus_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	bonus_id = db_integer(bonus_id)

	entry = Headquarters(bonus_id = bonus_id)

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
	table_id = 'TABLEID-------'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill__post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill//delete/<id>', methods=['DELETE'])
def delete_skill_bonus_(id):
	try:
		db.session.query().filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })



@skill.route('/skill/trait/select', methods=['POST'])
def skill_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['id'] 

	this = ['This Power']

	skills_query = db.session.query(Skill).order_by(Skill.name).all()
	skills = [{'id': '', 'name': 'Skill'}]
	for skill in skills_query:
		skills.append({'id': skill.name, 'name': skill.name})

	abilities_query = db.session.query(Ability).order_by(Ability.name).all()
	abilities = [{'id': '', 'name': 'Ability'}]
	for a in abilities_query:
		abilities.append({'id': a.name, 'name': a.name})

	defenses_query = db.session.query(Defense).order_by(Defense.name).all()
	defenses = [{'id': '', 'name': 'Defense'}]
	for d in defenses_query:
		defenses.append({'id': d.name, 'name': d.name})

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers_sorted = sorted(powers_raw)
	powers = [{'id': '', 'name': 'Power'}]
	for p in powers_sorted:
		powers.append({'id': p, 'name': p})

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses_sorted = sorted(bonuses_raw)
	bonuses = [{'id': '', 'name': 'Enhanced Skill'}]
	for b in bonuses_sorted:
		bonuses.append({'id': b, 'name': b})

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages_sorted = sorted(advantages_raw)
	advantages = [{'id': '', 'name': 'Advantage'}]
	for a in advantages_sorted:
		advantages.append({'id': a, 'name': a})

	extras_query = db.session.query(Extra).order_by(Extra.name).all()
	extras = [{'id': '', 'name': 'Extra'}]
	for e in extras_query:
		extras.append({'id': e.name, 'name': e.name})

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
	elif trait == 'advantage':
		body['options'] = advantages
	elif trait == 'extra':
		body['options'] = extras
	elif trait == 'interact':
		body['options'] = [{'id': 'Any Interaction', 'name': 'Any Interarction'}]
	elif trait == 'interact':
		body['options'] = [{'id': 'Any Interaction', 'name': 'Any Manipulation'}]
	elif trait == 'this_power':
		body['options'] = [{'id': 'This Power', 'name': 'This Power'}]
	elif trait == 'this_advantage':
		body['options'] = [{'id': 'This Advantage', 'name': 'This Advantage'}]
	elif trait == 'sense':
		body['options'] = [{'id': 'Sense', 'name': 'Sense'}]
	elif trait == 'size':	
		body['options'] = [{'id': 'Size Rank', 'name': 'Size Rank'}]
	elif trait == 'speed':	
		body['options'] = [{'id': 'Speed Rank', 'name': 'Speed Rank'}] 
	elif trait == 'intim':
		body['options'] = [{'id': 'Intimidation Rank', 'name': 'Intimidation Rank'}]
	elif trait == 'any':
		body['options'] = [{'id': 'Any Trait', 'name': 'Any Trait'}]
	elif trait == 'x':
		body['options'] = [{'id': 'Variable', 'name': 'Variable'}]
	elif trait == 'auto':
		body['options'] = [{'id': 'Automatic', 'name': 'Automatic'}]
	elif trait == '':
		body['options'] = [{'id': '', 'name': 'Trait'}]
	elif trait == 'immoveable':
		body['options'] = [{'id': 'Immoveable', 'name': 'Immoveable'}]
	elif trait == 'this_bonus':
		body['options'] = [{'id': 'This Skill', 'name': 'This Skill'}]
	else:
		body['success'] = False
		body['options'] = [{'id': '', 'name': ''}]


	print(body)
	return jsonify(body)


@skill.route('/unit/select', methods=['POST'])
def unit_select():
	body = {}
	body['success'] = True

	id = request.get_json()['id']
	options = []

	try:
		id = int(id)
		get = db.session.query(MeasureType).filter_by(id=id).one()
		name = get.name + ' Units'
		results = db.session.query(Unit).filter_by(type_id=id).all()
		options.append({'id': '', 'name': name})
		for r in results:
			options.append({'id': r.id, 'name': r.name})
		body['options'] = options 
	except:
		body['success'] = False

	print(body)
	return jsonify(body)
