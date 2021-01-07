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
from models import Advantage
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv
from power_errors import integer, extra_convert, power_save_errors, alt_check_post_errors, change_action_post_errors, character_post_errors, circ_post_errors, create_post_errors, damage_post_errors, dc_table_post_errors, defense_post_errors, degree_post_errors, degree_mod_post_errors, environment_post_errors, levels_post_errors, minion_post_errors, mod_post_errors, move_post_errors, opposed_post_errors, ranged_post_errors, resist_post_errors, resisted_by_post_errors, reverse_effect_post_errors, sense_post_errors, time_post_errors
from power_posts import delete_row, grid_columns, alt_check_post, change_action_post, character_post, circ_post, create_post, damage_post, dc_table_post, defense_post, degree_post, degree_mod_post, environment_post, levels_post, minion_post, mod_post, move_post, opposed_post, ranged_post, resist_post, resisted_by_post, reverse_effect_post, sense_post, time_post

load_dotenv()

import os

db_path = os.environ.get("db_path")

advantage = Blueprint('advantage', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

@advantage.route('/advantage/create')
def advantage_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'advantage_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Advantage'
	stylesheets.append({"style": "/static/css/advantage_create.css"})

	advantage_includes = {'base_form': 'advantage_create/base_form.html', 'dc_table': 'advantage_create/dc_table.html', 'modifiers': 'advantage_create/modifiers.html', 'skill': 'advantage_create/skill.html', 'opposed': 'advantage_create/opposed.html', 'circ': 'advantage_create/circ.html'}

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

	advantage_type = [{'type': '', 'name': 'Advantage Type'}, {'type': 'combat', 'name': 'Combat'}, {'type': 'fortune', 'name': 'Fortune'}, {'type': 'General', 'name': 'General'}, {'type': 'skill', 'name': 'Skill'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Advantaage Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	actions = db.session.query(Action).all()

	checks = db.session.query(Check).all()
	
	base_conditions = Condition.query.all()
	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'opp', 'name': 'Opponent'}]

	traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_advantage', 'name': 'This Advantage'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'trait', 'name': 'Trait'}]
	
	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'} {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'descriptor', 'name': 'From Descriptor'}, {'type': 'condition', 'name': 'From Condition'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, advantage_includes=advantage_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							advantage_type=advantage_type, actions=actions, checks=checks, conditions=conditions, dc_type=dc_type, modifier_type=modifier_type, targets=targets, modifier_effect=modifier_effect,
							traits=traits, who_check=who_check, circ_type=circ_type, circ_null=circ_null)


@advantage.route('/advantage/create', methods=['POST'])
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
	

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']

	advantage = db.session.query(Advantage).filter(Advantage.id == advantage_id).one()


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
	
	if power is not None:
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
