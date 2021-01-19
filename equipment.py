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
from advantage_posts import adv_benefit_post, adv_alt_check_post, adv_circ_post, adv_combined_post, adv_condition_post, adv_dc_post, adv_deg_mod_post, adv_effort_post, adv_minion_post, adv_modifiers_post, adv_opposed_post, adv_points_post, adv_resist_post, adv_rounds_post, adv_skill_post, adv_time_post, adv_variable_post, adv_levels_post
from advantage_errors import adv_benefit_post_errors, adv_alt_check_post_errors, adv_circ_post_errors, adv_combined_post_errors, adv_condition_post_errors, adv_dc_post_errors, adv_deg_mod_post_errors, adv_effort_post_errors, adv_minion_post_errors, adv_modifiers_post_errors, adv_opposed_post_errors, adv_points_post_errors, adv_resist_post_errors, adv_rounds_post_errors, adv_skill_post_errors, adv_time_post_errors, adv_variable_post_errors, adv_save_errors, adv_levels_post_errors
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add
from app import sidebar, stylesheets, meta_name, meta_content, title

load_dotenv()

import os

db_path = os.environ.get("db_path")

equipment = Blueprint('equipment', __name__)
db = SQLAlchemy()

stylesheets = stylesheets
meta_name = meta_name
meta_content = meta_content
title = title
sidebar = sidebar

@equipment.route('/equipment/create')
def equipment_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'equipment_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Equipment'
	stylesheets.append({"style": "/static/css/equipment_create.css"})

	equipment_includes = {'base_form': 'equipment_create/base_form.html'}

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


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, equipment_includes=equipment_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers)


@advantage.route('/equipment/create', methods=['POST'])
def post_advantage(): 
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

	advantage = db.session.query(Advantage).filter(Advantage.name == name).first()

	if advantage is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an advantage with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		new_advantage = Advantage(name=name)
		db.session.add(new_advantage)
		db.session.commit()
		body['success'] = True
		body['id'] = new_advantage.id
		body['name'] = new_advantage.name
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

@advantage.route('/advantage/save', methods=['POST'])
def save_advantage(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = adv_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	description = request.get_json()['description']
	adv_type = request.get_json()['adv_type']
	action = request.get_json()['action']
	check_type = request.get_json()['check_type']
	ranked = request.get_json()['ranked']
	ranked_ranks = request.get_json()['ranked_ranks']
	ranked_max = request.get_json()['ranked_max']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	replaced_trait_type = request.get_json()['replaced_trait_type']
	replaced_trait = request.get_json()['replaced_trait']
	skill_type = request.get_json()['skill_type']
	skill = request.get_json()['skill']
	skill_description = request.get_json()['skill_description']
	skill_untrained = request.get_json()['skill_untrained']
	no_pre_check = request.get_json()['no_pre_check']
	expertise = request.get_json()['expertise']
	conflict = request.get_json()['conflict']
	consequence = request.get_json()['consequence']
	conflict_immune = request.get_json()['conflict_immune']
	dc_type = request.get_json()['dc_type']
	dc_value = request.get_json()['dc_value']
	dc_mod = request.get_json()['dc_mod']
	alter_target = request.get_json()['alter_target']
	simultaneous = request.get_json()['simultaneous']
	simultaneous_type = request.get_json()['simultaneous_type']
	extra_action = request.get_json()['extra_action']
	action1 = request.get_json()['action1']
	action2 = request.get_json()['action2']
	invent = request.get_json()['invent']
	invent_permanence = request.get_json()['invent_permanence']
	invent_trait_type = request.get_json()['invent_trait_type']
	invent_trait = request.get_json()['invent_trait']
	rituals = request.get_json()['rituals']
	gm_secret_check = request.get_json()['gm_secret_check']
	gm_trait_type = request.get_json()['gm_trait_type']
	gm_trait = request.get_json()['gm_trait']
	gm_veto = request.get_json()['gm_veto']
	language = request.get_json()['language']
	languages = request.get_json()['languages']
	language_rank = request.get_json()['language_rank']
	multiple = request.get_json()['multiple']
	groups = request.get_json()['groups']
	pressure = request.get_json()['pressure']
	check_check = request.get_json()['check_check']
	circumstance = request.get_json()['circumstance']
	combined = request.get_json()['combined']
	condition = request.get_json()['condition']
	dc = request.get_json()['dc']
	degree = request.get_json()['degree']
	effort = request.get_json()['effort']
	levels = request.get_json()['levels']
	minion = request.get_json()['minion']
	mods = request.get_json()['mods']
	mods_multiple = request.get_json()['mods_multiple']
	mods_count = request.get_json()['mods_count']
	opposed = request.get_json()['opposed']
	opposed_multiple = request.get_json()['opposed_multiple']
	points = request.get_json()['points']
	resist = request.get_json()['resist']
	resist_multiple = request.get_json()['resist_multiple']
	rounds = request.get_json()['rounds']
	swap = request.get_json()['swap']
	swap_multiple = request.get_json()['swap_multiple']
	time = request.get_json()['time']
	variable = request.get_json()['variable']

	action = db_integer(action)
	check_type = db_integer(check_type)
	expertise = db_integer(expertise)
	conflict = db_integer(conflict)
	consequence = db_integer(consequence)
	conflict_immune = db_integer(conflict_immune)
	action1 = db_integer(action1)
	action2 = db_integer(action2)

	ranked_ranks = integer(ranked_ranks)
	ranked_max = integer(ranked_max)
	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	languages = integer(languages)
	language_rank = integer(language_rank)
	mods_count = integer(mods_count)

	entry = db.session.query(Advantage).filter(Advantage.id == advantage_id).one()

	entry.description = description
	entry.adv_type = adv_type
	entry.action = action
	entry.check_type = check_type
	entry.ranked = ranked
	entry.ranked_ranks = ranked_ranks
	entry.ranked_max = ranked_max
	entry.trait_type = trait_type
	entry.trait = trait
	entry.replaced_trait_type = replaced_trait_type
	entry.replaced_trait = replaced_trait
	entry.skill_type = skill_type
	entry.skill = skill
	entry.skill_description = skill_description
	entry.skill_untrained = skill_untrained
	entry.no_pre_check = no_pre_check
	entry.expertise = expertise
	entry.conflict = conflict
	entry.consequence = consequence
	entry.conflict_immune = conflict_immune
	entry.dc_type = dc_type
	entry.dc_value = dc_value
	entry.dc_mod = dc_mod
	entry.alter_target = alter_target
	entry.simultaneous = simultaneous
	entry.simultaneous_type = simultaneous_type
	entry.extra_action = extra_action
	entry.action1 = action1
	entry.action2 = action2
	entry.invent = invent
	entry.invent_permanence = invent_permanence
	entry.invent_trait_type = invent_trait_type
	entry.invent_trait = invent_trait
	entry.rituals = rituals
	entry.gm_secret_check = gm_secret_check
	entry.gm_trait_type = gm_trait_type
	entry.gm_trait = gm_trait
	entry.gm_veto = gm_veto
	entry.language = language
	entry.languages = languages
	entry.language_rank = language_rank
	entry.multiple = multiple
	entry.groups = groups
	entry.pressure = pressure
	entry.check_check = check_check
	entry.circumstance = circumstance
	entry.combined = combined
	entry.condition = condition
	entry.dc = dc
	entry.degree = degree
	entry.effort = effort
	entry.levels = levels
	entry.minion = minion
	entry.mods = mods
	entry.mods_multiple = mods_multiple	
	entry.mods_count = mods_count
	entry.opposed = opposed
	entry.opposed_multiple = opposed_multiple
	entry.points = points
	entry.resist = resist
	entry.resist_multiple = resist_multiple
	entry.rounds = rounds
	entry.swap = swap
	entry.swap_multiple = swap_multiple
	entry.time = time
	entry.variable = variable

	db.session.commit()
	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@advantage.route('/advantage/save/success/<advantage_id>')
def advantage_save_success(advantage_id):	
	advantage = db.session.query(Advantage).filter_by(id=advantage_id).one()
	
	flash('Advantage ' + advantage.name + ' Successfully Created')
	return redirect(url_for('home'))

@advantage.route('/advantage/edit_name', methods=['POST'])
def edit_advantage_name(): 
	body = {}
	error = False
	error_msgs = []

	advantage_id = request.get_json()['id']
	name = request.get_json()['name']
	print(name)

	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	advantage = db.session.query(Advantage).filter(Advantage.name == name).first()
	
	if advantage is not None:
		error = True
		body['success'] = False
		error_msgs.append('There is already an advantage with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)
	try:
		edit_advantage = db.session.query(Advantage).filter(Advantage.id == advantage_id).one()
		edit_advantage.name = name
		db.session.commit()
		body['success'] = True
		body['id'] = edit_advantage.id
		body['name'] = edit_advantage.name
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
