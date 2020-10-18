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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

skills = Blueprint('skills', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

@skills.route('/skill/create')
def skill_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'special_skill_create.html'
	
	skill_includes = {'base_form': 'special_skill_create/base_form.html','dc_table': 'special_skill_create/dc_table.html', 'levels': 'special_skill_create/levels.html', 'circumstance': 'special_skill_create/circumstance_table.html', 'degree': 'special_skill_create/degree_table.html', 'degree_mod': 'special_skill_create/degree_mod.html', 'movement': 'special_skill_create/movement.html', 'power': 'special_skill_create/power.html', 'rounds': 'special_skill_create/rounds.html', 'subskill': 'special_skill_create/subskill.html', 'action': 'special_skill_create/change_action.html', 'resistance': 'special_skill_create/resistance.html', 'opponent_condition': 'special_skill_create/opponent_condition.html', 'other_char': 'special_skill_create/other_char.html', 'other_checks': 'special_skill_create/other_checks.html', 'resist': 'special_skill_create/resist.html', 'opposed': 'special_skill_create/opposed.html', 'alt_check': 'special_skill_create/alt_check.html', 'pre_check': 'special_skill_create/pre_check.html'}

	title = 'DC Adventures Online Roleplqying Game: Create Special Skill'
	stylesheets.append({"style": "/static/css/special_skill_create.css"})

	skills = Skill.query.all()

	abilities = Ability.query.all()

	opposed_raw = []

	for skill in skills:
		opposed_raw.append(skill.name)

	for ability in abilities:
		opposed_raw.append(ability.name)

	opposed = sorted(opposed_raw)

	checks = Check.query.all()

	base_conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']

	conditions_raw = []

	for condition in base_conditions:
		conditions_raw.append(condition.name)

	for condition in combined_conditions:
		conditions_raw.append(condition)

	conditions = sorted(conditions_raw)
	
	actions = Action.query.all()

	skilltype = SkillType.query.all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	dctype = [{"value": "gm", "name": "Set by GM"}, {"value": "table", "name": "DC Table"}]

	level_target = ['Active Player', 'Other Player', 'GM Controlled']

	targets = ['Other Player', 'GM Controlled']

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	char_rank = db.session.query(Rank).filter_by(rank_type='char')

	deg_mod_type = ['damage', 'measure', 'condition']

	opposed_by = [{'id': 'rank_high', 'name': 'Highest Rank'}, {'id': 'bonus_high', 'name': 'Highest Bonus'}, {'id': 'rank_low', 'name': 'Lowest Rank'}, {'id': 'bonus_low', 'name': 'Lowest Bonus'}, {'id': 'gm', 'name': "GM's Choice"}]
	
	numbers = []
	for i in range(-20, 21, 1):
		numbers.append(i)

	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	dcclasses = []
	for i in range(0, 41, 1):
		dcclasses.append(i)

	dc_rank = []

	char = [rank.format() for rank in char_rank]

	measure = [rank.format() for  rank in measure_rank]

	maths = Math.query.all()

	value_type =['value', 'math']

	defenses = Defense.query.all()

	units = Unit.query.all()

	ranks = Rank.query.all()

	results = ['success', 'failure']

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']

	powers = sorted(powers_raw)

	resists_raw = []

	for oppose in opposed:
		resists_raw.append(oppose)

	for power in powers:
		resists_raw.append(power)

	resists = sorted(resists_raw)

	skills_abilities_raw = []

	whens = ['before', 'after']

	checks_two = [{'id': 'skill', 'name': 'Skill Check'}, {'id': 'opposed', 'name': 'Opposed Check'}]

	for skill in skills:
		skills_abilities_raw.append(skill.name)

	for ability in abilities:
		skills_abilities_raw.append(ability.name)

	skills_abilities = sorted(skills_abilities_raw)

	level_type = [{'id': 1, 'name': 'Attitude'}]
	levels = [{'id': 1, 'name': 'Hostile'}, {'id': 1, 'name': 'Unfavorable'}, {'id': 1, 'name': 'Indifferent'}, {'id': 1, 'name': 'Favorable'}, {'id': 1, 'name': 'Helpful'}]

	return render_template('template.html', targets=targets, checks_two=checks_two, whens=whens, skills_abilities=skills_abilities, level_type=level_type, levels=levels, opposed_by=opposed_by, resists=resists, negatives=negatives, times=times, opposed=opposed, results=results, powers=powers, char_rank=char_rank, combined_conditions=combined_conditions, ranks=ranks, deg_mod_type=deg_mod_type, measure_rank=measure_rank, level_target=level_target, skill_includes=skill_includes, units=units, defenses=defenses, value_type=value_type, maths=maths, dc_rank=dc_rank, dcclasses=dcclasses, dctype=dctype, skilltype=skilltype, actions=actions, conditions=conditions, checks=checks, numbers=numbers, skills=skills, includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)

@skills.route('/skill/create', methods=['POST'])
def post_skill(): 
	body = {}
	error = False
	error_msgs = []
	errors = {}

	name = request.get_json()['name']
	print(name)

	skills = Skill.query.all()
	bonuses = SkillBonus.query.all()

	all_skills = []

	for skill in skills:
		all_skills.append(skill.name)

	for skill in bonuses:
		all_skills.append(skill.name)

	for skill in all_skills:
		if skill == name:
			error = True
			errors['success'] = False
			error_msgs.append('There is already a skill with that name')
			errors['error'] = error_msgs
			break

	try:
		skill = SkillBonus(name=name)
		db.session.add(skill)
		db.session.commit()
		body['success'] = True
		body['id'] = skill.id
		body['name'] = skill.name
	except:
		error = True
		errors['success'] = False
		error_msgs.append('There was an error processing the request')
		errors['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
	if error:
		return jsonify(errors)
	else:
		return jsonify(body)

@skills.route('/skill/edit_name', methods=['POST'])
def edit_skill_name(): 
	body = {}
	error = False
	error_msgs = []
	errors = {}

	skill_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	skills = Skill.query.all()
	bonuses = SkillBonus.query.all()

	all_skills = []

	for skill in skills:
		all_skills.append(skill.name)

	for skill in bonuses:
		all_skills.append(skill.name)

	for skill in all_skills:
		if skill == name:
			error = True
			errors['success'] = False
			error_msgs.append('There is already a skill with that name')
			errors['error'] = error_msgs
			break

	try:
		skill = db.session.query(SkillBonus).filter(SkillBonus.id == skill_id).one()
		skill.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = skill.id
		body['name'] = skill.name
	except:
		error = True
		errors['success'] = False
		error_msgs.append('There was an error processing the request')
		errors['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
	if error:
		return jsonify(errors)
	else:
		return jsonify(body)

@skills.route('/skill/other_checks/create', methods=['POST'])
def post_bonus_other_checks():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	skill_id = request.get_json()['skill_id']
	description = request.get_json()['description']

	skill = db.session.query(Skill).filter_by(id=skill_id).one()

	try:
		bonus = SkillOther(bonus_id=bonus_id, skill_id=skill_id, description=description)
		db.session.add(bonus)
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['skill'] = skill.name
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/pre_check/create', methods=['POST'])
def post_bonus_pre_check():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	check_type = request.get_json()['check_type']
	when = request.get_json()['when']
	check = request.get_json()['check']
	description = request.get_json()['description']
	opposed_check = request.get_json()['opposed_check']

	try:
		bonus = SkillOtherCheck(bonus_id=bonus_id, check_type=check_type, when=when, check=check, opposed_check=opposed_check, description=description)
		db.session.add(bonus)
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['check_type'] = bonus.check_type
		body['when'] = bonus.when
		body['check'] = bonus.check
		body['oppose_check'] = bonus.opposed_check
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/opposed/create', methods=['POST'])
def post_bonus_opposed():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	priority = request.get_json()['priority'] 
	opposed = request.get_json()['opposed']
	mod = request.get_json()['mod']
	description = request.get_json()['description']

	try:
		bonus = SkillOpposed(bonus_id=bonus_id, priority=priority, opposed=opposed, mod=mod, description=description)
		db.session.add(bonus)
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['priority'] = bonus.priority
		body['opposed'] = bonus.opposed
		body['mod'] = bonus.mod
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/rounds/create', methods=['POST'])
def post_bonus_rounds():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	dc = request.get_json()['dc']
	degree = request.get_json()['degree']
	rank_id = request.get_json()['rank']
	mod = request.get_json()['mod']
	rounds = request.get_json()['rounds']

	rank = db.session.query(Rank).filter_by(id=rank_id).one()

	try:
		bonus = SkillRound(bonus_id=bonus_id, dc=dc, degree=degree, rank=rank_id, mod=mod, rounds=rounds)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['dc'] = bonus.dc
		body['degree'] = bonus.degree
		body['rank'] = rank.name
		body['mod'] = bonus.mod
		body['rounds'] = bonus.rounds

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/power/create', methods=['POST'])
def post_bonus_power():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	power = request.get_json()['power']
	description = request.get_json()['description']
	try:
		bonus = SkillPower(bonus_id=bonus_id, power=power, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['power']  = bonus.power
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/level/create', methods=['POST'])
def post_bonus_level():
	body = {}

	bonus_level = request.get_json()['bonus_level']
	bonus_id = request.get_json()['bonus_id']
	type = request.get_json()['type']
	target = request.get_json()['target']
	degree = request.get_json()['degree'] 
	keyword = request.get_json()['keyword']
	description = request.get_json()['description']

	try:
		bonus = SkillLevels(bonus_id=bonus_id, type=type, target=target, degree=degree, keyword=keyword, description=description)
		db.session.add(bonus)	
		db.session.commit()

		if bonus_level:
			level = SkillLevelsType(bonus_id=bonus_id, type=type)
			db.session.add(level)	
			db.session.commit()

		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['type'] = bonus.type
		body['target'] = bonus.target
		body['degree'] = bonus.degree
		body['keyword'] = bonus.keyword
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/circ/create', methods=['POST'])
def post_bonus_circ():
	body = {}
	error = False
	error_msgs = []
	errors = {}

	bonus_id = request.get_json()['bonus_id']
	skill_id = request.get_json()['skill'] 
	target = request.get_json()['target']
	type = request.get_json()['type']
	mod = request.get_json()['mod']
	unit_mod = request.get_json()['unit_mod']
	unit_value = request.get_json()['unit_value']
	unit_type = request.get_json()['unit_type']
	adjust_check_mod = request.get_json()['adjust_check_mod']
	adjust_mod = request.get_json()['adjust_mod']
	adjust_rank = request.get_json()['adjust_rank']
	equip_mod = request.get_json()['equip_mod']
	rounds = request.get_json()['rounds']
	description = request.get_json()['description']

	if mod == '':
		mod = None

	if unit_mod == '':
		unit_mod = None

	if unit_value == '':
		unit_value = None
	
	if adjust_check_mod == '':
		adjust_check_mod = None
	
	if adjust_mod == '':
		adjust_mod = None

	if equip_mod == '':
		equip_mod = None

	if adjust_rank != '':
		rank = db.session.query(Rank).filter_by(id=adjust_rank).one()
		rank_name = rank.name
	else:
		adjust_rank = None
		rank_name = ''

	if unit_type != '':	
		unit = db.session.query(Unit).filter_by(id=unit_type).one()
		unit_name = unit.name
	else:
		unit_type = None
		unit_name = ''

	skill = db.session.query(Skill).filter_by(id=skill_id).one()

	try:
		unitvalue = int(unit_value)
	except:
		error = True
		error_msgs.append('Unit value must be a number')
		body['success'] = False
		body['error'] = error_msgs

	try:
		bonus = SkillCircMod(bonus_id=bonus_id, skill=skill_id, target=target, type=type, mod=mod, unit_mod=unit_mod, unit_type=unit_type, unit_value=unitvalue, adjust_check_mod=adjust_check_mod, adjust_mod=adjust_mod, adjust_rank=adjust_rank, equip_mod=equip_mod, rounds=rounds, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id	
		body['skill'] = skill.name
		body['target'] = bonus.target
		body['type'] = bonus.type
		body['mod'] = bonus.mod
		body['unit_mod'] = bonus.unit_mod
		body['unit_value'] = bonus.unit_value
		body['unit_type'] = unit_name
		body['adjust_check_mod'] = bonus.adjust_check_mod
		body['adjust_mod'] = bonus.adjust_mod
		body['adjust_rank'] = rank_name
		body['equip_mod'] = bonus.equip_mod
		body['rounds'] = bonus.rounds
		body['description'] = bonus.description

	except:
		error = False
		error_msgs.append('There was an error processing the request')
		body['success'] = False
		body['error'] = error_msgs

	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/degree_key/create', methods=['POST'])
def post_bonus_degree_key():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	target = request.get_json()['target']
	degree = request.get_json()['degree']
	keyword = request.get_json()['keyword']
	description = request.get_json()['description']
	type = request.get_json()['type']
	degree_type_check = request.get_json()['degree_type_check']

	try:
		bonus = SkillDegreeKey(bonus_id=bonus_id, type=type, target=target, degree=degree, keyword=keyword, description=description)
		db.session.add(bonus)
		db.session.commit()

		if degree_type_check:
			degree = SkillDegreeType(bonus_id=bonus_id, type=type)
			db.session.add(degree)	
			db.session.commit()

		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['type'] = bonus.type
		body['target'] = bonus.target
		body['degree'] = bonus.degree
		body['keyword'] = bonus.keyword
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/degree_mod/create', methods=['POST'])
def post_bonus_degree_mod():
	body = {}
	error = False
	error_msgs = []
	errors = {}

	bonus_id = request.get_json()['bonus_id']
	target = request.get_json()['target']
	degree = request.get_json()['degree']
	type = request.get_json()['type']
	damage_value_degree = request.get_json()['damage_value_degree']
	damage_value_value = request.get_json()['damage_value_value']
	damage_math_damage = request.get_json()['damage_math_damage']
	damage_math_math1 = request.get_json()['damage_math_math1']
	damage_math_value = request.get_json()['damage_math_value']
	damage_math_math2 = request.get_json()['damage_math_math2']
	damage_math_rank = request.get_json()['damage_math_rank']
	measure_value = request.get_json()['measure_value']
	measure_value_rank = request.get_json()['measure_value_rank']
	measure_math_value = request.get_json()['measure_math_value']
	measure_math_math = request.get_json()['measure_math_math']
	measure_math_rank = request.get_json()['measure_math_rank']
	measure_math_measure_rank = request.get_json()['measure_math_measure_rank']
	condition_1 = request.get_json()['condition_1']
	condition_2 = request.get_json()['condition_2']
	keyword = request.get_json()['keyword']
	description = request.get_json()['description']
	nullify = request.get_json()['nullify']

	if damage_value_degree == '':
		damage_value_degree = None

	if damage_value_value == '':
		damage_value_value = None

	if damage_math_damage == '':
		damage_math_damage = None

	if damage_math_value == '':
		damage_math_value = None

	if measure_value == '':
		measure_value = None

	if measure_math_value == '':
		measure_math_value = None

	if measure_math_measure_rank != '':
		rank = db.session.query(Rank).filter_by(id=measure_math_measure_rank).one()
		measure_math_measure_rank_name = rank.name
	else:
		measure_math_measure_rank = None
		measure_math_measure_rank_name = ''

	if measure_math_rank != '':
		rank = db.session.query(Rank).filter_by(id=measure_math_rank).one()
		measure_math_rank_name = rank.name
	else:
		measure_math_rank = None
		measure_math_rank_name = ''

	if measure_value_rank != '':
		rank = db.session.query(Rank).filter_by(id=measure_value_rank).one()
		measure_value_rank_name = rank.name
	else:
		measure_value_rank = None
		measure_value_rank_name = ''

	if damage_math_rank != '':
		rank = db.session.query(Rank).filter_by(id=damage_math_rank).one()
		damage_math_rank_name = rank.name
	else:
		damage_math_rank = None
		damage_math_rank_name = ''

	if damage_math_math1 != '':	
		math = db.session.query(Math).filter_by(id=damage_math_math1).one()
		damage_math_math1_name = math.symbol
	else:
		damage_math_math1 = None
		damage_math_math1_name = ''

	if damage_math_math2 != '':	
		math = db.session.query(Math).filter_by(id=damage_math_math2).one()
		damage_math_math2_name = math.symbol
	else:
		damage_math_math2 = None
		damage_math_math2_name = ''

	if measure_math_math != '':	
		math = db.session.query(Math).filter_by(id=measure_math_math).one()
		measure_math_math_name = math.symbol
	else:
		measure_math_math = None
		measure_math_math_name = ''

	try:
		bonus = SkillDegreeMod(bonus_id=bonus_id, 
			target=target,
			degree=degree,
			type=type,
			damage_value_degree=damage_value_degree,
			damage_value_value=damage_value_value,
			damage_math_damage=damage_math_damage,
			damage_math_math1=damage_math_math1,
			damage_math_value=damage_math_value,
			damage_math_math2=damage_math_math2,
			damage_math_rank=damage_math_rank,
			measure_value=measure_value,
			measure_value_rank=measure_value_rank,
			measure_math_value=measure_math_value,
			measure_math_math =measure_math_math,
			measure_math_rank=measure_math_rank,
			measure_math_measure_rank=measure_math_measure_rank,
			condition_1=condition_1,
			condition_2=condition_2,
			keyword=keyword,
			description=description,
			nullify=nullify)	
	
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id	
		body['target'] = bonus.target
		body['degree'] = bonus.degree
		body['type'] = bonus.type
		body['damage_value_degree'] = bonus.damage_value_degree
		body['damage_value_value'] = bonus.damage_value_value
		body['damage_math_damage'] = bonus.damage_math_damage
		body['damage_math_math1'] = damage_math_math1_name
		body['damage_math_value'] = bonus.damage_math_value
		body['damage_math_math2'] = damage_math_math2_name
		body['damage_math_rank'] = damage_math_rank_name
		body['measure_value'] = bonus.measure_value
		body['measure_value_rank'] = measure_value_rank_name
		body['measure_math_value'] = bonus.measure_math_value
		body['measure_math_math'] = measure_math_math_name
		body['measure_math_rank'] = measure_math_rank_name
		body['measure_math_measure_rank'] = measure_math_measure_rank_name
		body['condition_1'] = bonus.condition_1
		body['condition_2'] = bonus.condition_2
		body['keyword'] = bonus.keyword
		body['description'] = bonus.description
		body['nullify'] = bonus.nullify

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/resistance/create', methods=['POST'])
def post_bonus_resistance():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	target = request.get_json()['target']
	mod = request.get_json()['mod']
	description = request.get_json()['description']

	try:
		bonus = SkillResistCheck(bonus_id=bonus_id, target=target, mod=mod, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['target'] =  bonus.target
		body['mod'] = bonus.mod
		body['description'] = bonus.description

	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)


@skills.route('/skill/resist/create', methods=['POST'])
def post_bonus_resist():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	effect = request.get_json()['effect']
	description = request.get_json()['description']

	try:
		bonus = SkillResistEffect(bonus_id=bonus_id, effect=effect, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['effect'] = bonus.effect
		body['description'] = bonus.description
		
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/opp_condition/create', methods=['POST'])
def post_bonus_opp_condition():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	degree = request.get_json()['degree']
	condition = request.get_json()['condition']
	rounds = request.get_json()['rounds']
	description = request.get_json()['description']

	try:
		bonus = SkillOppCondition(bonus_id=bonus_id, degree=degree, condition=condition, rounds=rounds, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['degree'] = bonus.degree
		body['condition'] = bonus.condition
		body['rounds'] = bonus.rounds
		body['description'] = bonus.description
		
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/char_check/create', methods=['POST'])
def post_bonus_char_check():
	body = {}

	bonus_id = request.get_json()['bonus_id']
	check_id = request.get_json()['check_id']
	target = request.get_json()['target']
	degree = request.get_json()['degree']
	rank = request.get_json()['rank']
	description = request.get_json()['description']

	checks = db.session.query(Check).filter_by(id=check_id).one()

	try:
		bonus = SkillCharCheck(bonus_id=bonus_id, check_id=check_id, target=target, degree=degree, rank=rank, description=description)
		db.session.add(bonus)	
		db.session.commit()
		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id
		body['check_id'] = checks.name
		body['target'] = bonus.target
		body['degree'] = bonus.degree
		body['rank'] = bonus.rank
		body['description'] = bonus.description
		
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
		print(body)
		return jsonify(body)

@skills.route('/skill/dc/create', methods=['POST'])
def post_bonus_dc():
	body = {}
	error = False
	error_msgs = []
	errors = {}

	bonus_id = request.get_json()['bonus_id']
	type = request.get_json()['type']
	val = request.get_json()['val']
	math_val = request.get_json()['math_val']
	math = request.get_json()['math']
	math_rank = request.get_json()['math_rank']
	measure_type = request.get_json()['measure_type']
	measure_val = request.get_json()['measure_val']
	measure_val_unit = request.get_json()['measure_val_unit']
	measure_math_val = request.get_json()['measure_math_val']
	measure_math = request.get_json()['measure_math']
	measure_rank = request.get_json()['measure_rank']
	damage = request.get_json()['damage']
	keyword = request.get_json()['keyword']
	condition_one = request.get_json()['condition_one']
	condition_two = request.get_json()['condition_two']
	defense = request.get_json()['defense']
	action = request.get_json()['action']
	description = request.get_json()['description']


	if val == '':
		val = None

	if math_val == '':
		math_val = None

	if measure_math_val == '':
		measure_math_val = None

	if damage == '':
		damage = None

	try:
		measureval = int(measure_val)
	except:
		error = True
		error_msgs.append('Measurement value must be a number')
		body['success'] = False
		body['error'] = error_msgs


	if math_rank != '':
		rank = db.session.query(Rank).filter_by(id=math_rank).one()
		math_rank_name = rank.name
	else:
		math_rank = None
		math_rank_name = ''

	if measure_rank != '':
		rank = db.session.query(Rank).filter_by(id=measure_rank).one()
		measure_rank_name = rank.name
	else:
		measure_rank = None
		measure_rank_name = ''

	if defense != '':
		defenses = db.session.query(Defense).filter_by(id=defense).one()
		defense_name = defenses.name
	else:
		defense = None
		defense_name = ''

	if action != '':
		actions = db.session.query(Action).filter_by(id=action).one()
		action_name = actions.name
	else:
		action = None
		action_name = ''

	if measure_math != '':
		maths = db.session.query(Math).filter_by(id=measure_math).one()
		measure_math_name = maths.symbol
	else:
		measure_math = None
		measure_math_name = ''

	if math != '':
		maths = db.session.query(Math).filter_by(id=math).one()
		math_name = maths.symbol
	else:
		math = None
		math_name = ''

	if measure_val_unit != '':	
		unit = db.session.query(Unit).filter_by(id=measure_val_unit).one()
		measure_val_unit_name = unit.name
	else:
		measure_val_unit = None
		measure_val_unit_name = ''

	try:
		bonus = SkillDC(bonus_id = bonus_id,
							type = type,
							val = val,
							math_val = math_val,
							math = math,
							math_rank = math_rank,
							measure_type = measure_type,
							measure_val = measureval,
							measure_val_unit = measure_val_unit,
							measure_math_val = measure_math_val,
							measure_math = measure_math,
							measure_rank = measure_rank,
							damage = damage,
							keyword = keyword,
							condition_one = condition_one,
							condition_two = condition_two,
							defense = defense,
							action = action,
							description = description)		
		db.session.add(bonus)	
		db.session.commit()

		body['success'] = True
		body['id'] = bonus.id
		body['bonus_id'] = bonus.bonus_id	
		body['type'] = bonus.type
		body['val'] = bonus.val
		body['math_val'] = bonus.math_val
		body['math'] = math_name
		body['math_rank'] = math_rank_name
		body['measure_type'] = bonus.measure_type
		body['measure_val'] = bonus.measure_val
		body['measure_val_unit'] = measure_val_unit_name
		body['measure_math_val'] = bonus.measure_math_val
		body['measure_math'] = measure_math_name
		body['measure_rank'] = measure_rank_name
		body['damage'] = bonus.damage
		body['keyword'] = bonus.keyword
		body['condition_one'] = bonus.condition_one
		body['condition_two'] = bonus.condition_two
		body['defense'] = defense_name
		body['action'] = action_name
		body['description'] = bonus.description

	except:
		error = False
		error_msgs.append('There was an error processing the request')
		body['success'] = False
		body['error'] = error_msgs

	finally:
		db.session.close()
		print(body)
		return jsonify(body)