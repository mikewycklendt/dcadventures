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

from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add
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
from db.skill_models import SkillBonus, SkillAbility, SkillMove, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from posts.skill_posts import skill_ability_post, skill_move_post, skill_check_post, skill_circ_post, skill_dc_post, skill_degree_post, skill_levels_post, skill_modifiers_post, skill_opposed_post, skill_time_post
from errors.skill_errors import skill_save_errors, skill_move_post_errors, skill_ability_post_errors, skill_check_post_errors, skill_circ_post_errors, skill_dc_post_errors, skill_degree_post_errors, skill_levels_post_errors, skill_modifiers_post_errors, skill_opposed_post_errors, skill_time_post_errors


load_dotenv()

import os

db_path = os.environ.get("db_path")

skill = Blueprint('skill', __name__)
db = SQLAlchemy()

@skill.route('/skill/create')
def headquarters_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'skill_create/skill_create.html'

	skill_includes = {'base_form': 'skill_create/base_form.html', 'dc': 'skill_create/dc_table.html', 'levels': 'skill_create/levels.html', 'degree_mod': 'skill_create/degree_mod.html', 'circ': 'skill_create/circ.html', 'alt_check': 'skill_create/alt_check.html', 'opposed': 'skill_create/opposed.html', 'modifiers': 'skill_create/modifiers.html', 'time': 'skill_create/time.html', 'ability': 'skill_create/ability.html', 'move': 'skill_create/move.html'}
	
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

	bonus_select = db.session.query(SkillBonus).filter_by(show=True).all()
	
	distances = db.session.query(Unit).filter_by(type_id=3)

	conditions = db.session.query(Condition).filter(Condition.hide == None).order_by(Condition.name).all()
	
	powers = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()

	advantages = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()

	abilities = db.session.query(Ability).filter(Ability.hide == None).order_by(Ability.name).all()

	complexity = Complex.query.all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	skills = db.session.query(Skill).filter(Skill.hide == None).order_by(Skill.name).all()

	weapon_cat = WeaponCat.query.all()

	environments = db.session.query(Environment).filter(Environment.show == True).order_by(Environment.name).all()
	
	senses = db.session.query(Sense).filter(Sense.hide == None).order_by(Sense.name).all()
	
	ranged = db.session.query(Ranged).filter_by(show=True)

	subsenses = db.session.query(SubSense).filter(SubSense.hide == None).order_by(SubSense.name).all()

	cover = Cover.query.all()

	concealment = Conceal.query.all()

	maneuvers = db.session.query(Maneuver).filter(Maneuver.hide == None).order_by(Maneuver.name).all()
	
	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1).all()
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2).all()

	creatures = db.session.query(Creature).filter(Creature.show == True).order_by(Creature.name).all()
		
	emotions = db.session.query(Emotion).filter(Emotion.show == True).order_by(Emotion.name).all()

	professions = db.session.query(Job).filter(Job.show == True).order_by(Job.name).all()
	
	conflicts = db.session.query(ConflictAction).filter(ConflictAction.hide == None).order_by(ConflictAction.name).all()
	
	damages = db.session.query(Descriptor).filter(Descriptor.damage == True, Descriptor.show == True).order_by(Descriptor.name).all()
	
	light = Light.query.all()

	checks = db.session.query(Check).filter(Check.hide == None).order_by(Check.name).all()

	actions = db.session.query(Action).filter(Action.hide == None).order_by(Action.name).all()

	defenses = db.session.query(Defense).filter(Defense.hide == None).order_by(Defense.name).all()

	skill_type = SkillType.query.all()

	maths = Math.query.all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	unit_type = MeasureType.query.all()

	units = Unit.query.all()

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Skill Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'Check Table'}]

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'routine', 'name': 'Routine Check'}, {'type': 'none', 'name': 'No DC'}, {'type': 'choice', 'name': 'Chosen by Player'}]
	
	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Measurement'}, {'type': 'gm', 'name': 'Set by GM'}]

	value_mod = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Modifier'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_bonus', 'name': 'This Skill'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'active', 'name': 'Active Opponent Rank'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	circ_targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'distance', 'name': 'Distance Penalty'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'bonus', 'name': 'This Enhanced Skill'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}, {'type': 'skill', 'name': 'Skill Check'}, {'type': 'light', 'name': 'Lighting'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	required_tools = [{'type': '', 'name': 'Tools'}, {'type': 'correct', 'name': 'Correct Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'gm', 'name': 'GM Decides'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	concealment_type = [{'type': '', 'name': 'Concealment Type'}, {'type': 'requires', 'name': 'Requires'}, {'type': 'provides', 'name': 'Provides'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'check', 'name': 'Check'}]

	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	updown = [{'id': '', 'name': 'Direction'}, {'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	circ_effect = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'temp', 'name': 'Effect Temporary'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill_rank', 'name': 'Skill Rank Modifier'}, {'type': 'skill_unit', 'name': 'Skill Unit Modifier'}]
	
	measure_effect_circ = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}]
	
	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	dc_damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}]

	repair = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	direction = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]

	frequency = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}]

	attached = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}]

	lasts = [{'type': '', 'name': 'Lasts'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'time', 'name': 'Time'}, {'type': 'rank', 'name': 'Time Rank'}]

	gm_circ = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Alwats'}, {'type': '', 'name': 'Sometimes'}]

	nullify = [{'type': '', 'name': 'Nullify Type'}, {'type': 'dc', 'name': 'DC'}, {'type': 'mod', 'name': 'Modifier'}]

	greater_less = [{'type': '', 'name': 'Type'}, {'type': 'greater', 'name': 'Greater'}, {'type': 'less', 'name': 'Less Than'}]

	speed = [{'type': '', 'name': 'Speed Type'}, {'type': 'rank', 'name': 'Speed Rank'}, {'type': 'mod', 'name': 'Modifier'}]

	distance = [{'type': '', 'name': 'Distance Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'unit_math', 'name': 'Unit Math'}, {'type': 'rank_math', 'name': 'Rank Math'}]

	trait_type = [{'type': 'rank', 'name': 'Trait Rank'}, {'type': 'check', 'name': 'Check Result'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, skill_includes=skill_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, skills=skills, checks=checks, actions=actions, skill_type=skill_type, maths=maths,
							value_type=value_type, traits=traits, level_types=level_types, conditions=conditions, targets=targets, deg_mod_type=deg_mod_type, action_type=action_type, knowledge=knowledge,
							consequences=consequences, specificity=specificity, measure_rank=measure_rank, condition_type=condition_type, updown=updown, circ_effect=circ_effect, measure_effect=measure_effect,
							unit_type=unit_type, check_trigger=check_trigger, check_type=check_type, conflicts=conflicts, ranged=ranged, multiple_opposed=multiple_opposed, dc_type=dc_type, damage_type=damage_type,
							inflict=inflict, direction=direction, value_mod=value_mod, modifier_effect=modifier_effect, modifier_trigger=modifier_trigger, modifier_type=modifier_type, multiple=multiple, tools=tools,
							environments=environments, senses=senses, subsenses=subsenses, cover=cover, concealment=concealment, maneuvers=maneuvers, weapon_ranged=weapon_ranged, weapon_melee=weapon_melee,
							creatures=creatures, emotions=emotions, professions=professions, damages=damages, light=light, powers=powers, weapon_cat=weapon_cat, times=times, time_effect=time_effect,
							abilities=abilities, frequency=frequency, lasts=lasts, attached=attached, complexity=complexity, repair=repair, advantages=advantages, time_value=time_value, circ_targets=circ_targets,
							dc_value=dc_value, required_tools=required_tools, concealment_type=concealment_type, bonus_select=bonus_select, gm_circ=gm_circ, nullify=nullify, greater_less=greater_less, units=units,
							speed=speed, distance=distance, distances=distances, trait_type=trait_type, measure_effect_circ=measure_effect_circ)


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

	skill_id = request.get_json()['skill_id']
	description = request.get_json()['description']
	ability = request.get_json()['ability']
	skill = request.get_json()['skill']
	check_type = request.get_json()['check_type']
	action = request.get_json()['action']
	type = request.get_json()['type']
	dc_type = request.get_json()['dc_type']
	dc_value = request.get_json()['dc_value']
	dc_mod = request.get_json()['dc_mod']
	target = request.get_json()['target']
	targets = request.get_json()['targets']
	speed_type = request.get_json()['speed_type']
	speed_turns = request.get_json()['speed_turns']
	speed_direction = request.get_json()['speed_direction']
	speed_mod = request.get_json()['speed_mod']
	speed_value = request.get_json()['speed_value']
	condition = request.get_json()['condition']
	attack = request.get_json()['attack']
	advantage = request.get_json()['advantage']
	concealment_type = request.get_json()['concealment_type']
	concealment = request.get_json()['concealment']
	for_weapon = request.get_json()['for_weapon']
	weapon_cat = request.get_json()['weapon_cat']
	weapon_type = request.get_json()['weapon_type']
	weapon = request.get_json()['weapon']
	untrained = request.get_json()['untrained']
	tools = request.get_json()['tools']
	required_tools = request.get_json()['required_tools']
	subskill = request.get_json()['subskill']
	check_dc = request.get_json()['check_dc']
	secret = request.get_json()['secret']
	secret_frequency = request.get_json()['secret_frequency']
	gm_circ_value = request.get_json()['gm_circ_value']
	gm_circ_type = request.get_json()['gm_circ_type']
	gm_circ = request.get_json()['gm_circ']
	ability_check = request.get_json()['ability_check']
	check_check = request.get_json()['check_check']
	circumstance = request.get_json()['circumstance']
	dc = request.get_json()['dc']
	degree = request.get_json()['degree']
	levels = request.get_json()['levels']
	modifiers = request.get_json()['modifiers']
	move = request.get_json()['move']
	opposed = request.get_json()['opposed']
	time = request.get_json()['time']
	opposed_multiple = request.get_json()['opposed_multiple']
	modifiers_multiple = request.get_json()['modifiers_multiple']
	modifiers_multiple_count = request.get_json()['modifiers_multiple_count']

	ability = db_integer(Ability, ability)
	skill = db_integer(Skill, skill)
	check_type = db_integer(Check, check_type)
	action = db_integer(Action, action)
	type = db_integer(SkillType, type)
	condition = db_integer(Condition, condition)
	advantage = db_integer(Advantage, advantage)
	concealment = db_integer(Conceal, concealment)
	weapon_cat = db_integer(WeaponCat, weapon_cat)
	weapon_type = db_integer(WeaponType, weapon_type)
	weapon = db_integer(Weapon, weapon)

	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	targets = integer(targets)
	speed_turns = integer(speed_turns)
	speed_mod = integer(speed_mod)
	speed_value = integer(speed_value)
	gm_circ_value = integer(gm_circ_value)
	attack = integer(attack)
	modifiers_multiple_count = integer(modifiers_multiple_count)

	entry = db.session.query(SkillBonus).filter(SkillBonus.id == skill_id).one()

	entry.description = description
	entry.ability = ability
	entry.skill = skill
	entry.check_type = check_type
	entry.action = action
	entry.type = type
	entry.dc_type = dc_type
	entry.dc_value = dc_value
	entry.dc_mod = dc_mod
	entry.target = target
	entry.targets = targets
	entry.speed_type = speed_type
	entry.speed_turns = speed_turns
	entry.speed_direction = speed_direction
	entry.speed_mod = speed_mod
	entry.speed_value = speed_value
	entry.condition = condition
	entry.attack = attack
	entry.advantage = advantage
	entry.concealment_type = concealment_type
	entry.concealment = concealment
	entry.for_weapon = for_weapon
	entry.weapon_cat = weapon_cat
	entry.weapon_type = weapon_type
	entry.weapon = weapon
	entry.untrained = untrained
	entry.tools = tools
	entry.required_tools = required_tools
	entry.subskill = subskill
	entry.check_dc = check_dc
	entry.secret = secret
	entry.secret_frequency = secret_frequency
	entry.gm_circ_value = gm_circ_value
	entry.gm_circ_type = gm_circ_type
	entry.gm_circ = gm_circ
	entry.ability_check = ability_check
	entry.check_check = check_check
	entry.circumstance = circumstance
	entry.dc = dc
	entry.degree = degree
	entry.levels = levels
	entry.modifiers = modifiers
	entry.move = move
	entry.opposed = opposed
	entry.time = time
	entry.opposed_multiple = opposed_multiple
	entry.modifiers_multiple = modifiers_multiple
	entry.modifiers_multiple_count = modifiers_multiple_count

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



@skill.route('/skill/ability/create', methods=['POST'])
def skill_bonus_post_ability():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_ability_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	ability = request.get_json()['ability']
	circumstance = request.get_json()['circumstance']

	skill_id = integer(skill_id)
	ability = db_integer(Ability, ability)

	entry = SkillAbility(skill_id = skill_id,
							ability = ability,
							circumstance = circumstance)

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
	table_id = 'ability'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_ability_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/ability/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_ability(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillAbility).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)


@skill.route('/skill/check/create', methods=['POST'])
def skill_bonus_post_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	check_type = request.get_json()['check_type']
	mod = request.get_json()['mod']
	circumstance = request.get_json()['circumstance']
	trigger = request.get_json()['trigger']
	when = request.get_json()['when']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	conflict = request.get_json()['conflict']
	conflict_range = request.get_json()['conflict_range']
	conflict_weapon = request.get_json()['conflict_weapon']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	action_type = request.get_json()['action_type']
	action = request.get_json()['action']
	free = request.get_json()['free']

	skill_id = integer(skill_id)
	check_type = db_integer(Check, check_type)
	conflict = db_integer(ConflictAction, conflict)
	conflict_range = db_integer(Ranged, conflict_range)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)

	mod = integer(mod)
	trait = integer(trait)
	action = integer(action)

	entry = SkillCheck(skill_id = skill_id,
						check_type = check_type,
						mod = mod,
						circumstance = circumstance,
						trigger = trigger,
						when = when,
						trait_type = trait_type,
						trait = trait,
						conflict = conflict,
						conflict_range = conflict_range,
						conflict_weapon = conflict_weapon,
						condition1 = condition1,
						condition2 = condition2,
						action_type = action_type,
						action = action,
						free = free)

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
	
	body = skill_check_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/check/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_check(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillCheck).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/circ/create', methods=['POST'])
def skill_bonus_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_circ_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	circ_target = request.get_json()['circ_target']
	mod = request.get_json()['mod']
	effect = request.get_json()['effect']
	speed = request.get_json()['speed']
	temp = request.get_json()['temp']
	target = request.get_json()['target']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	time = request.get_json()['time']
	condition_type = request.get_json()['condition_type']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	conditions = request.get_json()['conditions']
	conditions_effect = request.get_json()['conditions_effect']
	measure_effect = request.get_json()['measure_effect']
	measure_rank_value = request.get_json()['measure_rank_value']
	measure_rank = request.get_json()['measure_rank']
	unit_value = request.get_json()['unit_value']
	unit_type = request.get_json()['unit_type']
	unit = request.get_json()['unit']
	measure_trait_type = request.get_json()['measure_trait_type']
	measure_trait = request.get_json()['measure_trait']
	measure_trait_math = request.get_json()['measure_trait_math']
	measure_mod = request.get_json()['measure_mod']
	measure_math_rank = request.get_json()['measure_math_rank']
	keyword = request.get_json()['keyword']
	cumulative = request.get_json()['cumulative']
	optional = request.get_json()['optional']
	lasts = request.get_json()['lasts']
	turns = request.get_json()['turns']
	unit_time = request.get_json()['unit_time']
	time_units = request.get_json()['time_units']
	time_rank = request.get_json()['time_rank']
	circumstance = request.get_json()['circumstance']

	skill_id = integer(skill_id)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	time_units = db_integer(Unit, time_units)

	mod = integer(mod)
	speed = integer(speed)
	temp = integer(temp)
	time = integer(time)
	conditions = integer(conditions)
	conditions_effect = integer(conditions_effect)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	turns = integer(turns)
	unit_time = integer(unit_time)
	time_rank = integer(time_rank)

	if level is not None:
		try:
			level_circ = db.session.query(Levels).filter(Levels.id == level).one()
			level_circ.bonus_citc = True
			db.session.commit()
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()
		finally:
			db.session.close()

	entry = SkillCirc(skill_id = skill_id,
						circ_target = circ_target,
						mod = mod,
						effect = effect,
						speed = speed,
						temp = temp,
						target = target,
						level_type = level_type,
						level = level,
						time = time,
						condition_type = condition_type,
						condition1 = condition1,
						condition2 = condition2,
						conditions = conditions,
						conditions_effect = conditions_effect,
						measure_effect = measure_effect,
						measure_rank_value = measure_rank_value,
						measure_rank = measure_rank,
						unit_value = unit_value,
						unit_type = unit_type,
						unit = unit,
						measure_trait_type = measure_trait_type,
						measure_trait = measure_trait,
						measure_trait_math = measure_trait_math,
						measure_mod = measure_mod,
						measure_math_rank = measure_math_rank,
						keyword = keyword,
						cumulative = cumulative,
						optional = optional,
						lasts = lasts,
						turns = turns,
						unit_time = unit_time,
						time_units = time_units,
						time_rank = time_rank,
						circumstance = circumstance)

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
	table_id = 'circ'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_circ_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/circ/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_circ(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillCirc).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/dc/create', methods=['POST'])
def skill_bonus_post_dc():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_dc_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	dc = request.get_json()['dc']
	description = request.get_json()['description']
	value = request.get_json()['value']
	mod = request.get_json()['mod']
	math_value = request.get_json()['math_value']
	math = request.get_json()['math']
	math_trait_type = request.get_json()['math_trait_type']
	math_trait = request.get_json()['math_trait']
	condition = request.get_json()['condition']
	levels = request.get_json()['levels']
	damage = request.get_json()['damage']
	cover = request.get_json()['cover']
	complex = request.get_json()['complex']
	measure = request.get_json()['measure']
	change_action = request.get_json()['change_action']
	conceal = request.get_json()['conceal']
	action = request.get_json()['action']
	action_when = request.get_json()['action_when']
	damage_type = request.get_json()['damage_type']
	inflict_type = request.get_json()['inflict_type']
	inflict_flat = request.get_json()['inflict_flat']
	inflict_trait_type = request.get_json()['inflict_trait_type']
	inflict_trait = request.get_json()['inflict_trait']
	inflict_math = request.get_json()['inflict_math']
	inflict_mod = request.get_json()['inflict_mod']
	inflict_bonus = request.get_json()['inflict_bonus']
	damage_mod = request.get_json()['damage_mod']
	damage_consequence = request.get_json()['damage_consequence']
	measure_effect = request.get_json()['measure_effect']
	measure_rank_value = request.get_json()['measure_rank_value']
	measure_rank = request.get_json()['measure_rank']
	unit_value = request.get_json()['unit_value']
	unit_type = request.get_json()['unit_type']
	unit = request.get_json()['unit']
	measure_trait_type = request.get_json()['measure_trait_type']
	measure_trait = request.get_json()['measure_trait']
	measure_trait_math = request.get_json()['measure_trait_math']
	measure_mod = request.get_json()['measure_mod']
	measure_math_rank = request.get_json()['measure_math_rank']
	measure_trait_type_unit = request.get_json()['measure_trait_type_unit']
	measure_trait_unit = request.get_json()['measure_trait_unit']
	measure_trait_math_unit = request.get_json()['measure_trait_math_unit']
	measure_mod_unit = request.get_json()['measure_mod_unit']
	measure_math_unit = request.get_json()['measure_math_unit']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	condition_turns = request.get_json()['condition_turns']
	action_no_damage = request.get_json()['action_no_damage']
	condition_no_damage = request.get_json()['condition_no_damage']
	keyword = request.get_json()['keyword']
	complexity = request.get_json()['complexity']

	skill_id = integer(skill_id)
	math = db_integer(Math, math)
	action = db_integer(Action, action)
	inflict_math = db_integer(Math, inflict_math)
	damage_consequence = db_integer(Consequence, damage_consequence)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	measure_trait_math_unit = db_integer(Math, measure_trait_math_unit)
	measure_math_unit = db_integer(Unit, measure_math_unit)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	complexity = db_integer(Complex, complexity)

	value = integer(value)
	mod = integer(mod)
	math_value = integer(math_value)
	math_trait = integer(math_trait)
	inflict_flat = integer(inflict_flat)
	inflict_trait = integer(inflict_trait)
	inflict_mod = integer(inflict_mod)
	inflict_bonus = integer(inflict_bonus)
	damage_mod = integer(damage_mod)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	measure_trait_unit = integer(measure_trait_unit)
	measure_mod_unit = integer(measure_mod_unit)
	condition_turns = integer(condition_turns)

	if level is not None:
		try:
			level_dc = db.session.query(Levels).filter(Levels.id == level).one()
			level_dc.bonus_dc = True
			db.session.commit()
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()
		finally:
			db.session.close()

	entry = SkillDC(skill_id = skill_id,
					target = target,
					dc = dc,
					description = description,
					value = value,
					mod = mod,
					math_value = math_value,
					math = math,
					math_trait_type = math_trait_type,
					math_trait = math_trait,
					condition = condition,
					levels = levels,
					damage = damage,
					cover = cover,
					complex = complex,
					measure = measure,
					change_action = change_action,
					conceal = conceal,
					action = action,
					action_when = action_when,
					damage_type = damage_type,
					inflict_type = inflict_type,
					inflict_flat = inflict_flat,
					inflict_trait_type = inflict_trait_type,
					inflict_trait = inflict_trait,
					inflict_math = inflict_math,
					inflict_mod = inflict_mod,
					inflict_bonus = inflict_bonus,
					damage_mod = damage_mod,
					damage_consequence = damage_consequence,
					measure_effect = measure_effect,
					measure_rank_value = measure_rank_value,
					measure_rank = measure_rank,
					unit_value = unit_value,
					unit_type = unit_type,
					unit = unit,
					measure_trait_type = measure_trait_type,
					measure_trait = measure_trait,
					measure_trait_math = measure_trait_math,
					measure_mod = measure_mod,
					measure_math_rank = measure_math_rank,
					measure_trait_type_unit = measure_trait_type_unit,
					measure_trait_unit = measure_trait_unit,
					measure_trait_math_unit = measure_trait_math_unit,
					measure_mod_unit = measure_mod_unit,
					measure_math_unit = measure_math_unit,
					level_type = level_type,
					level = level,
					condition1 = condition1,
					condition2 = condition2,
					condition_turns = condition_turns,
					keyword = keyword,
					action_no_damage = action_no_damage,
					condition_no_damage = condition_no_damage,
					complexity = complexity)

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
	table_id = 'dc'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_dc_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/dc/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_dc(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillDC).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/degree/create', methods=['POST'])
def skill_bonus_post_degree():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_degree_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	value = request.get_json()['value']
	type = request.get_json()['type']
	action = request.get_json()['action']
	time = request.get_json()['time']
	recovery = request.get_json()['recovery']
	damage_type = request.get_json()['damage_type']
	object = request.get_json()['object']
	object_effect = request.get_json()['object_effect']
	inflict_type = request.get_json()['inflict_type']
	inflict_flat = request.get_json()['inflict_flat']
	inflict_trait_type = request.get_json()['inflict_trait_type']
	inflict_trait = request.get_json()['inflict_trait']
	inflict_math = request.get_json()['inflict_math']
	inflict_mod = request.get_json()['inflict_mod']
	inflict_bonus = request.get_json()['inflict_bonus']
	damage_mod = request.get_json()['damage_mod']
	damage_consequence = request.get_json()['damage_consequence']
	consequence_action_type = request.get_json()['consequence_action_type']
	consequence_action = request.get_json()['consequence_action']
	consequence_trait_type = request.get_json()['consequence_trait_type']
	consequence_trait = request.get_json()['consequence_trait']
	consequence = request.get_json()['consequence']
	knowledge = request.get_json()['knowledge']
	knowledge_count = request.get_json()['knowledge_count']
	knowledge_specificity = request.get_json()['knowledge_specificity']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	level_direction = request.get_json()['level_direction']
	circumstance = request.get_json()['circumstance']
	circ_target = request.get_json()['circ_target']
	measure_effect = request.get_json()['measure_effect']
	measure_rank_value = request.get_json()['measure_rank_value']
	measure_rank = request.get_json()['measure_rank']
	unit_value = request.get_json()['unit_value']
	unit_type = request.get_json()['unit_type']
	unit = request.get_json()['unit']
	measure_trait_type = request.get_json()['measure_trait_type']
	measure_trait = request.get_json()['measure_trait']
	measure_trait_math = request.get_json()['measure_trait_math']
	measure_mod = request.get_json()['measure_mod']
	measure_math_rank = request.get_json()['measure_math_rank']
	measure_trait_type_unit = request.get_json()['measure_trait_type_unit']
	measure_trait_unit = request.get_json()['measure_trait_unit']
	measure_trait_math_unit = request.get_json()['measure_trait_math_unit']
	measure_mod_unit = request.get_json()['measure_mod_unit']
	measure_math_unit = request.get_json()['measure_math_unit']
	condition_type = request.get_json()['condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	condition_turns = request.get_json()['condition_turns']
	keyword = request.get_json()['keyword']
	nullify = request.get_json()['nullify']
	nullify_type = request.get_json()['nullify_type']
	cumulative = request.get_json()['cumulative']
	linked = request.get_json()['linked']
	check_type = request.get_json()['check_type']
	opposed = request.get_json()['opposed']
	resist_dc = request.get_json()['resist_dc']
	resist_trait_type = request.get_json()['resist_trait_type']
	resist_trait = request.get_json()['resist_trait']
	skill_dc = request.get_json()['skill_dc']
	skill_trait_type = request.get_json()['skill_trait_type']
	skill_trait = request.get_json()['skill_trait']
	routine_trait_type = request.get_json()['routine_trait_type']
	routine_trait = request.get_json()['routine_trait']
	routine_mod = request.get_json()['routine_mod']
	attack = request.get_json()['attack']
	attack_turns = request.get_json()['attack_turns']
	compare = request.get_json()['compare']

	skill_id = integer(skill_id)
	action = db_integer(Action, action)
	inflict_math = db_integer(Math, inflict_math)
	damage_consequence = db_integer(Consequence, damage_consequence)
	consequence = db_integer(Consequence, consequence)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	circumstance = integer(circumstance)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	measure_trait_math_unit = db_integer(Math, measure_trait_math_unit)
	measure_math_unit = db_integer(Unit, measure_math_unit)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	
	check_type = db_integer(Check, check_type)
	opposed = db_integer(SkillOpposed, opposed)
	resist_dc = db_integer(SkillDC, resist_dc)
	skill_dc = db_integer(SkillDC, skill_dc)
	compare = db_integer(SkillOpposed, compare)

	resist_trait = integer(resist_trait)
	skill_trait = integer(skill_trait)
	routine_trait = integer(routine_trait)
	routine_mod = integer(routine_mod)
	attack = integer(attack)
	attack_turns = integer(attack_turns)

	value = integer(value)
	time = integer(time)
	object = integer(object)
	inflict_flat = integer(inflict_flat)
	inflict_trait = integer(inflict_trait)
	inflict_mod = integer(inflict_mod)
	inflict_bonus = integer(inflict_bonus)
	damage_mod = integer(damage_mod)
	consequence_action = integer(consequence_action)
	consequence_trait = integer(consequence_trait)
	knowledge_count = integer(knowledge_count)
	level_direction = integer(level_direction)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	measure_trait_unit = integer(measure_trait_unit)
	measure_mod_unit = integer(measure_mod_unit)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	condition_turns = integer(condition_turns)
	nullify = integer(nullify)
	
	if level is not None:
		try:
			level_degree = db.session.query(Levels).filter(Levels.id == level).one()
			level_degree.bonus_degree = True
			db.session.commit()
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()
		finally:
			db.session.close()

	entry = SkillDegree(skill_id = skill_id,
						target = target,
						value = value,
						type = type,
						action = action,
						time = time,
						recovery = recovery,
						damage_type = damage_type,
						object = object,
						object_effect = object_effect,
						inflict_type = inflict_type,
						inflict_flat = inflict_flat,
						inflict_trait_type = inflict_trait_type,
						inflict_trait = inflict_trait,
						inflict_math = inflict_math,
						inflict_mod = inflict_mod,
						inflict_bonus = inflict_bonus,
						damage_mod = damage_mod,
						damage_consequence = damage_consequence,
						consequence_action_type = consequence_action_type,
						consequence_action = consequence_action,
						consequence_trait_type = consequence_trait_type,
						consequence_trait = consequence_trait,
						consequence = consequence,
						knowledge = knowledge,
						knowledge_count = knowledge_count,
						knowledge_specificity = knowledge_specificity,
						level_type = level_type,
						level = level,
						level_direction = level_direction,
						circumstance = circumstance,
						circ_target = circ_target,
						measure_effect = measure_effect,
						measure_rank_value = measure_rank_value,
						measure_rank = measure_rank,
						unit_value = unit_value,
						unit_type = unit_type,
						unit = unit,
						measure_trait_type = measure_trait_type,
						measure_trait = measure_trait,
						measure_trait_math = measure_trait_math,
						measure_mod = measure_mod,
						measure_math_rank = measure_math_rank,
						measure_trait_type_unit = measure_trait_type_unit,
						measure_trait_unit = measure_trait_unit,
						measure_trait_math_unit = measure_trait_math_unit,
						measure_mod_unit = measure_mod_unit,
						measure_math_unit = measure_math_unit,
						condition_type = condition_type,
						condition_damage_value = condition_damage_value,
						condition_damage = condition_damage,
						condition1 = condition1,
						condition2 = condition2,
						condition_turns = condition_turns,
						keyword = keyword,
						nullify = nullify,
						nullify_type = nullify_type,
						cumulative = cumulative,
						linked = linked,
						check_type = check_type,
						opposed = opposed,
						resist_dc = resist_dc,
						resist_trait_type = resist_trait_type,
						resist_trait = resist_trait,
						skill_dc = skill_dc,
						skill_trait_type = skill_trait_type,
						skill_trait = skill_trait,
						routine_trait_type = routine_trait_type,
						routine_trait = routine_trait,
						routine_mod = routine_mod,
						attack = attack,
						attack_turns = attack_turns,
						compare = compare)

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
	table_id = 'deg-mod'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_degree_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/degree/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_degree(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillDegree).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/move/create', methods=['POST'])
def skill_bonus_post_move():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_move_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	speed = request.get_json()['speed']
	speed_rank = request.get_json()['speed_rank']
	speed_trait_type = request.get_json()['speed_trait_type']
	speed_trait = request.get_json()['speed_trait']
	speed_math1 = request.get_json()['speed_math1']
	speed_value1 = request.get_json()['speed_value1']
	speed_math2 = request.get_json()['speed_math2']
	speed_value2 = request.get_json()['speed_value2']
	speed_description = request.get_json()['speed_description']
	distance = request.get_json()['distance']
	distance_rank = request.get_json()['distance_rank']
	distance_value = request.get_json()['distance_value']
	distance_units = request.get_json()['distance_units']
	distance_rank_trait_type = request.get_json()['distance_rank_trait_type']
	distance_rank_trait = request.get_json()['distance_rank_trait']
	distance_rank_math1 = request.get_json()['distance_rank_math1']
	distance_rank_value1 = request.get_json()['distance_rank_value1']
	distance_rank_math2 = request.get_json()['distance_rank_math2']
	distance_rank_value2 = request.get_json()['distance_rank_value2']
	distance_unit_trait_type = request.get_json()['distance_unit_trait_type']
	distance_unit_trait = request.get_json()['distance_unit_trait']
	distance_unit_math1 = request.get_json()['distance_unit_math1']
	distance_unit_value1 = request.get_json()['distance_unit_value1']
	distance_unit_math2 = request.get_json()['distance_unit_math2']
	distance_unit_value2 = request.get_json()['distance_unit_value2']
	distance_math_units = request.get_json()['distance_math_units']
	distance_description = request.get_json()['distance_description']
	direction = request.get_json()['direction']
	check_type = request.get_json()['check_type']
	turns = request.get_json()['turns']

	speed_rank = integer(speed_rank)
	speed_trait = integer(speed_trait)
	speed_value1 = integer(speed_value1)
	speed_value2 = integer(speed_value2)
	distance_rank = integer(distance_rank)
	distance_value = integer(distance_value)
	distance_rank_trait = integer(distance_unit_trait)
	distance_rank_value1 = integer(distance_rank_value1)
	distance_rank_value2 = integer(distance_rank_value2)
	distance_unit_trait = integer(distance_unit_trait)
	distance_unit_value1 = integer(distance_unit_value1)
	distance_unit_value2 = integer(distance_unit_value2)
	turns = integer(turns)

	speed_math1 = db_integer(Math, speed_math1)
	speed_math2 = db_integer(Math, speed_math2)
	distance_units = db_integer(Unit, distance_units)
	distance_rank_math1 = db_integer(Math, distance_rank_math1)
	distance_rank_math2 = db_integer(Math, distance_rank_math2)
	distance_unit_math1 = db_integer(Math, distance_unit_math1)
	distance_unit_math2 = db_integer(Math, distance_unit_math2)
	distance_math_units = db_integer(Unit, distance_math_units)
	check_type = db_integer(Check, check_type)

	entry = SkillMove(skill_id = skill_id,
						speed = speed,
						speed_rank = speed_rank,
						speed_trait_type = speed_trait_type,
						speed_trait = speed_trait,
						speed_math1 = speed_math1,
						speed_value1 = speed_value1,
						speed_math2 = speed_math2,
						speed_value2 = speed_value2,
						speed_description = speed_description,
						distance = distance,
						distance_rank = distance_rank,
						distance_value = distance_value,
						distance_units = distance_units,
						distance_rank_trait_type = distance_rank_trait_type,
						distance_rank_trait = distance_rank_trait,
						distance_rank_math1 = distance_rank_math1,
						distance_rank_value1 = distance_rank_value1,
						distance_rank_math2 = distance_rank_math2,
						distance_rank_value2 = distance_rank_value2,
						distance_unit_trait_type = distance_unit_trait_type,
						distance_unit_trait = distance_unit_trait,
						distance_unit_math1 = distance_unit_math1,
						distance_unit_value1 = distance_unit_value1,
						distance_unit_math2 = distance_unit_math2,
						distance_unit_value2 = distance_unit_value2,
						distance_math_units = distance_math_units,
						distance_description = distance_description,
						direction = direction,
						check_type = check_type,
						turns = turns)			


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
	table_id = 'move'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_move_post(entry, body, cells)
	
	db.session.close()

	return jsonify(body)

@skill.route('/skill/move/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_move(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillMove).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
	
	print (body)
	return jsonify(body)

@skill.route('/skill/opposed/create', methods=['POST'])
def skill_bonus_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	attached = request.get_json()['attached']
	frequency = request.get_json()['frequency']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	opponent_trait_type = request.get_json()['opponent_trait_type']
	opponent_trait = request.get_json()['opponent_trait']
	opponent_mod = request.get_json()['opponent_mod']
	player_secret = request.get_json()['player_secret']
	player_check = request.get_json()['player_check']
	opponent_check = request.get_json()['opponent_check']
	secret = request.get_json()['secret']
	recurring = request.get_json()['recurring']
	multiple = request.get_json()['multiple']
	recurring_value = request.get_json()['recurring_value']
	recurring_units = request.get_json()['recurring_units']
	description = request.get_json()['description']
	keyword = request.get_json()['keyword']

	skill_id = integer(skill_id)
	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)
	recurring_units = db_integer(Unit, recurring_units)

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)
	recurring_value = integer(recurring_value)

	entry = SkillOpposed(skill_id = skill_id,
						attached = attached,
						frequency = frequency,
						trait_type = trait_type,
						trait = trait,
						mod = mod,
						opponent_trait_type = opponent_trait_type,
						opponent_trait = opponent_trait,
						opponent_mod = opponent_mod,
						player_secret = player_secret,
						player_check = player_check,
						opponent_check = opponent_check,
						secret = secret,
						recurring = recurring,
						multiple = multiple,
						recurring_value = recurring_value,
						recurring_units = recurring_units,
						description = description,
						keyword = keyword)			

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
	
	body = skill_opposed_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/opposed/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_opposed(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillOpposed).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/time/create', methods=['POST'])
def skill_bonus_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_time_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	skill_id = request.get_json()['skill_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	type = request.get_json()['type']
	value_type = request.get_json()['value_type']
	rank1 = request.get_json()['rank1']
	rank1_value = request.get_json()['rank1_value']
	rank_math = request.get_json()['rank_math']
	rank2 = request.get_json()['rank2']
	rank2_value = request.get_json()['rank2_value']
	value = request.get_json()['value']
	units = request.get_json()['units']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	math = request.get_json()['math']
	math_value = request.get_json()['math_value']
	recovery = request.get_json()['recovery']
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_time = request.get_json()['recovery_time']
	recovery_incurable = request.get_json()['recovery_incurable']

	skill_id = integer(skill_id)
	rank1 = db_integer(Rank, rank1)
	rank_math = db_integer(Math, rank_math)
	rank2 = db_integer(Rank, rank2)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)

	rank1_value = integer(rank1_value)
	rank2_value = integer(rank2_value)
	value = integer(value)
	trait = integer(trait)
	math_value = integer(math_value)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)

	entry = SkillTime(skill_id = skill_id,
						type = type,
						value_type = value_type,
						rank1 = rank1,
						rank1_value = rank1_value,
						rank_math = rank_math,
						rank2 = rank2,
						rank2_value = rank2_value,
						value = value,
						units = units,
						trait_type = trait_type,
						trait = trait,
						math = math,
						math_value = math_value,
						recovery = recovery,
						recovery_penalty = recovery_penalty,
						recovery_time = recovery_time,
						recovery_incurable = recovery_incurable)

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
	table_id = 'time'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	
	body = skill_time_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@skill.route('/skill/time/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_time(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillTime).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/modifiers/create', methods=['POST'])
def skill_post_modifiers():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_modifiers_post_errors(data)

	skill_id = request.get_json()['skill_id']
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

		skill_id = integer(skill_id)
		environment = db_integer(Environment, environment)
		sense = db_integer(Sense, sense)
		mod_range = db_integer(Ranged, mod_range)
		subsense = db_integer(SubSense, subsense)
		cover = db_integer(Cover, cover)
		conceal = db_integer(Conceal, conceal)
		maneuver = db_integer(Maneuver, maneuver)
		weapon_melee = db_integer(WeaponType, weapon_melee)
		weapon_ranged = db_integer(WeaponType,  weapon_ranged)
		condition = db_integer(Condition, condition)
		power = db_integer(Power, power)
		consequence = db_integer(Consequence, consequence)
		creature = db_integer(Creature, creature)
		emotion = db_integer(Emotion, emotion)
		conflict = db_integer(ConflictAction, conflict)
		profession = db_integer(Job, profession)
		bonus_conflict = db_integer(ConflictAction, bonus_conflict)
		penalty_conflict = db_integer(ConflictAction, penalty_conflict)
		skill = db_integer(Skill, skill)
		light = db_integer(Light, light)
		bonus_check = db_integer(Check, bonus_check)
		bonus_check_range = db_integer(Ranged, bonus_check_range)
		penalty_check = db_integer(Check, penalty_check)
		penalty_check_range = db_integer(Ranged, penalty_check_range)

		bonus = integer(bonus)
		penalty = integer(penalty)
		bonus_trait = integer(bonus_trait)
		penalty_trait = integer(penalty_trait)
		multiple_count = integer(multiple_count)
		lasts = integer(lasts)

		entry = SkillMod(skill_id = skill_id,
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
		
		body = skill_modifiers_post(entry, body, cells)
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)

@skill.route('/skill/modifiers/delete/<id>', methods=['DELETE'])
def delete_skill_bonus_modifiers(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(SkillMod).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete thst rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

@skill.route('/skill/levels/create', methods=['POST'])
def skill_post_levels():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = skill_levels_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	skill_id = request.get_json()['skill_id']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	level_effect = request.get_json()['level_effect']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	old_level_type = request.get_json()['old_level_type']
	font = request.get_json()['font']
	power_dc = False
	power_degree = False
	skill_dc = False
	skill_degree = False
	bonus_dc = False
	bonus_degree = False
	advantage_dc = False
	advantage_degree = False

	body = {}
	body['success'] = True

	power = True

	skill_id = integer(skill_id)

	level_check = db.session.query(LevelType).filter(LevelType.name == level_type).first()
	if level_check is None:

		level_add = LevelType(bonus_id=skill_id,
									name=level_type)

		db.session.add(level_add)
		db.session.commit()

		type_id = level_add.id

		body['level_type_id'] = type_id
		body['level_type'] = level_add.name
		body['created'] = False
	
		db.session.close()
		
	else:
		level_skill = level_check.bonus_id
		print(skill_id)
		print(level_skill)
		if skill_id != level_skill:
			body['success'] = False
			body['error_msgs'] = ['There is already a level type with that name.']
			return jsonify(body)

		type_id = level_check.id
		body['created'] = True

	entry = Levels(bonus_id = skill_id,
						type_id=type_id,
						level_type = level_type,
						name = level,
						level_effect = level_effect,
						power_dc = power_dc,
						power_degree = power_degree,
						skill_dc = skill_dc,
						skill_degree = skill_degree,
						bonus_dc = bonus_dc,
						bonus_degree = bonus_degree,
						advantage_dc = advantage_dc,
						advantage_degree = advantage_degree)

	db.session.add(entry)
	db.session.commit()


	
	body['id'] = entry.id
	error = False
	error_msg = []

	rows = columns

	mods = []
	cells = []
	spot = "levels-spot"

	body['spot'] = spot
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['title'] = level_type
	type_split = level_type.split(' ')
	type_class = ''
	for t in  type_split:
		type_class += t 
	
	table_id = 'levels-' + type_class

	body['table_id'] = table_id

	body = skill_levels_post(entry, body, cells)

	db.session.close()
	
	return jsonify(body)


@skill.route('/skill/levels/delete/<id>', methods=['DELETE'])
def delete_skill_levels(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(Levels).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
	except:
		body['success'] = False
		message = 'Could not delete this level.  You may have applied it to another rule.  Dekete that rule first.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify(body)

