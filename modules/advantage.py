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

from posts.advantage_posts import adv_benefit_post, adv_alt_check_post, adv_circ_post, adv_combined_post, adv_condition_post, adv_dc_post, adv_deg_mod_post, adv_effort_post, adv_minion_post, adv_modifiers_post, adv_opposed_post, adv_points_post, adv_resist_post, adv_rounds_post, adv_skill_post, adv_time_post, adv_variable_post, adv_levels_post
from errors.advantage_errors import adv_benefit_post_errors, adv_alt_check_post_errors, adv_circ_post_errors, adv_combined_post_errors, adv_condition_post_errors, adv_dc_post_errors, adv_deg_mod_post_errors, adv_effort_post_errors, adv_minion_post_errors, adv_modifiers_post_errors, adv_opposed_post_errors, adv_points_post_errors, adv_resist_post_errors, adv_rounds_post_errors, adv_skill_post_errors, adv_time_post_errors, adv_variable_post_errors, adv_save_errors, adv_levels_post_errors
from create_functions.advantage_create import adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry

load_dotenv()

import os

db_path = os.environ.get("db_path")

advantage = Blueprint('advantage', __name__)
db = SQLAlchemy()



@advantage.route('/advantage/create')
def advantage_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'advantage_create/advantage_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Advantage'
	stylesheets.append({"style": "/static/css/advantage_create/advantage_create.css"})

	advantage_includes = {'base_form': 'advantage_create/base_form.html', 'dc_table': 'advantage_create/dc_table.html', 'modifiers': 'advantage_create/modifiers.html', 'skill': 'advantage_create/skill.html', 'opposed': 'advantage_create/opposed.html', 'circ': 'advantage_create/circ.html', 'degree_mod': 'advantage_create/degree_mod.html', 'levels': 'advantage_create/levels.html', 'points': 'advantage_create/points.html', 'time': 'advantage_create/time.html', 'combined': 'advantage_create/combined.html', 'resist': 'advantage_create/resist.html', 'variable': 'advantage_create/variable.html', 'alt_check': 'advantage_create/alt_check.html', 'effort': 'advantage_create/effort.html', 'benefit': 'advantage_create/benefit.html', 'rounds': 'advantage_create/rounds.html', 'condition': 'advantage_create/condition.html', 'minion': 'advantage_create/minion.html'}

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

	advantage_type = AdvantageType.query.all()

	actions = db.session.query(Action).filter(Action.hide == None).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	checks = db.session.query(Check).filter(Check.hide == None).all()

	benefits = db.session.query(Benefit).filter_by(approved=True).order_by(Benefit.name).all()
	benefits_all = db.session.query(Benefit).order_by(Benefit.name).all()
	
	ranges = Range.query.all()

	expertise = db.session.query(SkillBonus).filter_by(skill=5).all()

	cover = Cover.query.all()

	concealment = Conceal.query.all()
	
	times = db.session.query(Unit).filter_by(type_id=2).all()

	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1).all()
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2).all()

	ranged = db.session.query(Ranged).filter_by(show=True)

	conflicts = db.session.query(ConflictAction).filter(ConflictAction.hide == None).order_by(ConflictAction.name).all()
	
	environments = db.session.query(Environment).filter(Environment.show == True).order_by(Environment.name).all()
	
	senses = db.session.query(Sense).filter(Sense.hide == None).order_by(Sense.name).all()

	subsenses = db.session.query(SubSense).filter(SubSense.hide == None).order_by(SubSense.name).all()
	
	creatures = db.session.query(Creature).filter(Creature.show == True).order_by(Creature.name).all()
	
	professions = db.session.query(Job).filter(Job.show == True).order_by(Job.name).all()
	
	maneuvers = db.session.query(Maneuver).filter(Maneuver.hide == None).order_by(Maneuver.name).all()
	
	emotions = db.session.query(Emotion).filter(Emotion.show == True).order_by(Emotion.name).all()

	defenses = db.session.query(Defense).filter(Defense.hide == None).all()

	conditions = db.session.query(Condition).filter(Condition.hide == None).order_by(Condition.name).all()

	advantages = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()

	powers = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	maths = Math.query.all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Advantaage Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]
	
	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	target = [{'type': '', 'name': 'Target'}, {'type': 'become', 'name': 'Become Target'}, {'type': 'redirect', 'name': 'Redirect From Self'}, {'type': 'setup', 'name': 'Transfer Action Result to Teammate'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_Advantage', 'name': 'This Advantage'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'active', 'name': 'Active Opponent Rank'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}, {'type': 'any', 'name': 'Any Trait'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	simultaneous = [{'type': '', 'name': 'Type'}, {'type': 'same', 'name': 'At Same Time'}, {'type': 'maintain', 'name': 'While Maintaining Previous'}, {'type': 'both', 'name': 'Either'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]

	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'condition', 'name': 'From Condition'}, {'type': 'override', 'name': 'Override Trait Circumstance'}]

	permanence = [{'type': '', 'name': 'Permanence'}, {'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]

	low_high = [{'type': '', 'name': 'Lower or Higher'}, {'type': 'lower', 'name': 'Lower'}, {'type': 'high', 'name': 'Higher'}, {'type': 'equal', 'name': 'Equal'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'uncontrolled', 'name': 'Effect Uncontrolled'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	
	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	value_type_mod = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'Modifier'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	condition = [{'type': '', 'name': 'Condition Type'}, {'type': 'active', 'name': 'Active Condition'}, {'type': 'change', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}, {'type': 'null', 'name': 'Nullify Condition'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	points = [{'type': '', 'name': 'Spend For'}, {'type': 'ranks', 'name': 'Gain Ranks'}, {'type': 'benefit', 'name': 'Benefit'}, {'type': 'check', 'name': 'Circumstance Modifier'}, {'type': 'equip', 'name': 'Equipment'}, {'type': 'condition', 'name': 'Change Condition'}, {'type': 'initiative', 'name': 'Gain Initiative'}, {'type': '20', 'name': 'Automatic 20'}]

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]

	which = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Value'}, {'type': 'low', 'name': 'Lower Value'}]

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]

	effort = [{'type': '', 'name': 'Effect'}, {'type': 'benefit', 'name': 'Benefit'}]

	rounds_end = [{'type': '', 'name': 'Ends'}, {'type': 'action', 'name': 'Stop Taking Action'}, {'type': 'resist', 'name': 'Successful Resistance'}, {'type': 'danger', 'name': 'Danger'}]

	minion_type = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]


	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, advantage_includes=advantage_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							advantage_type=advantage_type, actions=actions, checks=checks, conditions=conditions, dc_type=dc_type, modifier_type=modifier_type, targets=targets, modifier_effect=modifier_effect,
							traits=traits, who_check=who_check, circ_type=circ_type, circ_null=circ_null, permanence=permanence, low_high=low_high, deg_mod_type=deg_mod_type, level_types=level_types, 
							value_type= value_type, maths=maths, measure_rank=measure_rank, condition_type=condition_type, updown=updown, knowledge=knowledge, specificity=specificity, negatives=negatives, 
							positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, points=points, conflicts=conflicts, consequences=consequences, action_type=action_type, ranges=ranges,
							times=times, time_effect=time_effect, advantages=advantages, which=which, check_trigger=check_trigger, check_type=check_type, benefits=benefits, effort=effort, rounds_end=rounds_end,
							environments=environments, senses=senses, subsenses=subsenses, modifier_trigger=modifier_trigger, multiple=multiple, creatures=creatures, professions=professions, powers=powers,
							emotions=emotions, simultaneous=simultaneous, multiple_opposed=multiple_opposed, tools=tools, condition=condition, maneuvers=maneuvers, cover=cover, concealment=concealment,
							ranged=ranged, target=target, weapon_melee=weapon_melee, weapon_ranged=weapon_ranged, minion_type=minion_type, benefits_all=benefits_all, defenses=defenses, expertise=expertise)

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
		body['error_msgs'] = error_msgs

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
		errors['error_msgs'] = error_msgs
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

	adv_type = integer(adv_type)
	action = db_integer(Action, action)
	check_type = db_integer(Check, check_type)
	expertise = db_integer(SkillBonus, expertise)
	conflict = db_integer(ConflictAction, conflict)
	consequence = db_integer(Consequence, consequence)
	conflict_immune = db_integer(ConflictAction, conflict_immune)
	action1 = db_integer(Action, action1)
	action2 = db_integer(Action, action2)

	ranked_ranks = integer(ranked_ranks)
	ranked_max = integer(ranked_max)
	trait = integer(trait)
	replaced_trait = integer(replaced_trait)
	skill = integer(skill)
	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	invent_trait = integer(invent_trait)
	gm_trait = integer(gm_trait)
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
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	finally:
		db.session.close()
		print(body)
		return jsonify(body)
	
@advantage.route('/advantage/alt_check/create', methods=['POST'])
def advantage_post_alt_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_alt_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	check_type = request.get_json()['check_type']
	check_trigger = request.get_json()['check_trigger']
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

	try:

		check_type = db_integer(Check, check_type)
		conflict = db_integer(ConflictAction, conflict)
		conflict_range = db_integer(Ranged, conflict_range)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		mod = integer(mod)
		trait = integer(trait)
		action = integer(action)	

		entry = AdvAltCheck(advantage_id = advantage_id,
								benefit = benefit,
								check_trigger = check_trigger,
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
				
		body = adv_alt_check_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/alt_check/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_alt_check(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvAltCheck).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/benefit/create', methods=['POST'])
def advantage_post_benefit():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_benefit_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	name = request.get_json()['name']
	description = request.get_json()['description']
	effort = request.get_json()['effort']

	benefit = db.session.query(Benefit).filter(Benefit.name == name).first()

	if benefit is not None:
		error = True
		error_msgs = []
		body['success'] = False
		error_msgs.append('There is already a benefit with that name')
		body['success'] = False
		body['error_msgs'] = error_msgs
		return jsonify(body)

	try:
		advantage_id = integer(advantage_id)


		
		entry = Benefit(advantage_id = advantage_id,
							name = name,
							description = description,
							effort = effort)

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
		table_id = 'benefit'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_benefit_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/benefit/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_benefit(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(Benefit).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this benefit.  You may have already applied it to another rule.  Delete that rule first.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/circ/create', methods=['POST'])
def advantage_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_circ_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	mod = request.get_json()['mod']
	rounds = request.get_json()['rounds']
	circumstance = request.get_json()['circumstance']
	circ_type = request.get_json()['circ_type']
	circ_range = request.get_json()['circ_range']
	conflict = request.get_json()['conflict']
	check_who = request.get_json()['check_who']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	null_type = request.get_json()['null_type']
	null_condition = request.get_json()['null_condition']
	null_trait_type = request.get_json()['null_trait_type']
	null_trait = request.get_json()['null_trait']
	null_override_trait_type = request.get_json()['null_override_trait_type']
	null_override_trait = request.get_json()['null_override_trait']


	try:
		circ_range = db_integer(Ranged, circ_range)
		conflict = db_integer(ConflictAction, conflict)
		null_condition = db_integer(Condition, null_condition)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
		mod = integer(mod)
		rounds = integer(rounds)
		check_trait = integer(check_trait)
		null_trait = integer(null_trait)
		null_override_trait = integer(null_override_trait)
		
		entry = AdvCirc(advantage_id = advantage_id,
							target = target,
							benefit = benefit,
							mod = mod,
							rounds = rounds,
							circumstance = circumstance,
							circ_type = circ_type,
							circ_range = circ_range,
							conflict = conflict,
							check_who = check_who,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							null_type = null_type,
							null_condition = null_condition,
							null_trait_type = null_trait_type,
							null_trait = null_trait,
							null_override_trait_type = null_override_trait_type,
							null_override_trait = null_override_trait)

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
				
		body = adv_circ_post(entry, body, cells)
		
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/circ/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_circ(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvCirc).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/combined/create', methods=['POST'])
def advantage_post_combined():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_combined_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	ranks = request.get_json()['ranks']
	advantage = request.get_json()['advantage']

	try:
		advantage_id = integer(advantage_id)
		advantage = db_integer(Advantage, advantage)	

		ranks = integer(ranks)

		entry = AdvCombined(advantage_id = advantage_id,
								ranks = ranks,
								advantage = advantage)

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
		table_id = 'combined'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_combined_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/combined/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_combined(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvCombined).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)


@advantage.route('/advantage/condition/create', methods=['POST'])
def advantage_post_condition():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_condition_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	condition_type = request.get_json()['condition_type']
	condition = request.get_json()['condition']
	condition_null = request.get_json()['condition_null']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	damage_value = request.get_json()['damage_value']
	damage = request.get_json()['damage']

	try:
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)

		condition = db_integer(Condition, condition)
		condition_null = db_integer(Condition, condition_null)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
	
		damage_value = integer(damage_value)
		damage = integer(damage)

		entry = AdvCondition(advantage_id = advantage_id,
									benefit = benefit,
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
						
		body = adv_condition_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/condition/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_condition(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvCondition).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/dc/create', methods=['POST'])
def advantage_post_dc():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_dc_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	dc = request.get_json()['dc']
	description = request.get_json()['description']
	value_value = request.get_json()['value_value']
	math_value = request.get_json()['math_value']
	math_math = request.get_json()['math_math']
	math_trait_type = request.get_json()['math_trait_type']
	math_trait = request.get_json()['math_trait']
	condition = request.get_json()['condition']
	keyword_check = request.get_json()['keyword_check']
	check_type = request.get_json()['check_type']
	levels = request.get_json()['levels']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_mod = request.get_json()['check_mod']

	try:
		math_math = db_integer(Math, math_math)
		level_type = db_integer(LevelType, level_type)
		level = db_integer(Levels, level)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value_value = integer(value_value)
		math_value = integer(math_value)
		math_trait = integer(math_trait)
		check_trait = integer(check_trait)
		check_mod = integer(check_mod)

		entry = AdvDC(advantage_id = advantage_id,
							target = target,
							benefit = benefit,
							dc = dc,
							description = description,
							value_value = value_value,
							math_value = math_value,
							math_math = math_math,
							math_trait_type = math_trait_type,
							math_trait = math_trait,
							condition = condition,
							keyword_check = keyword_check,
							check_type = check_type,
							levels = levels,
							level_type = level_type,
							level = level,
							condition1 = condition1,
							condition2 = condition2,
							keyword = keyword,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							check_mod = check_mod)
							
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
				
		body = adv_dc_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/dc/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_dc(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvDC).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/degree_mod/create', methods=['POST'])
def advantage_post_deg_mod():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_deg_mod_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	value = request.get_json()['value']
	deg_mod_type = request.get_json()['deg_mod_type']
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
	circ_value = request.get_json()['circ_value']
	circ_turns = request.get_json()['circ_turns']
	circ_trait_type = request.get_json()['circ_trait_type']
	circ_trait = request.get_json()['circ_trait']
	measure_type = request.get_json()['measure_type']
	measure_val1 = request.get_json()['measure_val1']
	measure_math = request.get_json()['measure_math']
	measure_trait_type = request.get_json()['measure_trait_type']
	measure_trait = request.get_json()['measure_trait']
	measure_value = request.get_json()['measure_value']
	measure_rank = request.get_json()['measure_rank']
	condition_type = request.get_json()['condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	nullify = request.get_json()['nullify']
	cumulative = request.get_json()['cumulative']
	linked = request.get_json()['linked']

	try:
		consequence = db_integer(Consequence, consequence)
		level_type = db_integer(LevelType, level_type)
		level = db_integer(Levels, level)
		measure_math = db_integer(Math, measure_math)
		measure_rank = db_integer(Rank, measure_rank)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
		
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value = integer(value)
		consequence_action = integer(consequence_action)
		consequence_trait = integer(consequence_trait)
		knowledge_count = integer(knowledge_count)
		circ_value = integer(circ_value)
		circ_turns = integer(circ_turns)
		circ_trait = integer(circ_trait)
		measure_val1 = integer(measure_val1)
		measure_trait = integer(measure_trait)
		measure_value = integer(measure_value)
		condition_damage_value = integer(condition_damage_value)
		condition_damage = integer(condition_damage)
		nullify = integer(nullify)
		
		entry = AdvDegree(advantage_id = advantage_id,
								target = target,
								benefit = benefit,
								value = value,
								deg_mod_type = deg_mod_type,
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
								circ_value = circ_value,
								circ_turns = circ_turns,
								circ_trait_type = circ_trait_type,
								circ_trait = circ_trait,
								measure_type = measure_type,
								measure_val1 = measure_val1,
								measure_math = measure_math,
								measure_trait_type = measure_trait_type,
								measure_trait = measure_trait,
								measure_value = measure_value,
								measure_rank = measure_rank,
								condition_type = condition_type,
								condition_damage_value = condition_damage_value,
								condition_damage = condition_damage,
								condition1 = condition1,
								condition2 = condition2,
								keyword = keyword,
								nullify = nullify,
								cumulative = cumulative,
								linked = linked)

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
				
		body = adv_deg_mod_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/degree_mod/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_deg_mod(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvDegree).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/effort/create', methods=['POST'])
def advantage_post_effort():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_effort_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	effect = request.get_json()['effect']
	condition_type = request.get_json()['condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	benefit_choice = request.get_json()['benefit_choice']
	benefit_turns = request.get_json()['benefit_turns']
	benefit_count = request.get_json()['benefit_count']
	benefit_effort = request.get_json()['benefit_effort']

	try:
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)

		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
		benefit_choice = db_integer(Benefit, benefit_choice)

		condition_damage_value = integer(condition_damage_value)
		condition_damage = integer(condition_damage)
		benefit_turns = integer(benefit_turns)
		benefit_count = integer(benefit_count)
		
		entry = AdvEffort(advantage_id = advantage_id,
								benefit = benefit,
								effect = effect,
								condition_type = condition_type,
								condition_damage_value = condition_damage_value,
								condition_damage = condition_damage,
								condition1 = condition1,
								condition2 = condition2,
								benefit_choice = benefit_choice,
								benefit_turns = benefit_turns,
								benefit_count = benefit_count,
								benefit_effort = benefit_effort)

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
		table_id = 'effort'	
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_effort_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/effort/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_effort(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvEffort).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/minion/create', methods=['POST'])
def advantage_post_minion():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_minion_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	points = request.get_json()['points']
	condition = request.get_json()['condition']
	player_condition = request.get_json()['player_condition']
	link = request.get_json()['link']
	variable_type = request.get_json()['variable_type']
	multiple = request.get_json()['multiple']
	attitude = request.get_json()['attitude']
	resitable = request.get_json()['resitable']
	heroic = request.get_json()['heroic']
	sacrifice = request.get_json()['sacrifice']
	sacrifice_cost = request.get_json()['sacrifice_cost']
	attitude_type = request.get_json()['attitude_type']
	attitude_attitude = request.get_json()['attitude_attitude']
	attitude_trait_type = request.get_json()['attitude_trait_type']
	attitude_trait = request.get_json()['attitude_trait']
	resitable_check = request.get_json()['resitable_check']
	resitable_dc = request.get_json()['resitable_dc']
	multiple_value = request.get_json()['multiple_value']
	horde = request.get_json()['horde']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	try:
		condition = db_integer(Condition, condition)
		player_condition = db_integer(Condition, player_condition)
		attitude_type = db_integer(LevelType, attitude_type)
		attitude_attitude = db_integer(Levels, attitude_attitude)
		resitable_check = db_integer(Defense, resitable_check)
	
		advantage_id = integer(advantage_id)
	
		points = integer(points)
		sacrifice_cost = integer(sacrifice_cost)
		attitude_trait = integer(attitude_trait)
		resitable_dc = integer(resitable_dc)
		multiple_value = integer(multiple_value)

		entry = AdvMinion(advantage_id = advantage_id,
								points = points,
								condition = condition,
								player_condition = player_condition,
								link = link,
								variable_type = variable_type,
								multiple = multiple,
								attitude = attitude,
								resitable = resitable,
								heroic = heroic,
								sacrifice = sacrifice,
								sacrifice_cost = sacrifice_cost,
								attitude_type = attitude_type,
								attitude_attitude = attitude_attitude,
								attitude_trait_type = attitude_trait_type,
								attitude_trait = attitude_trait,
								resitable_check = resitable_check,
								resitable_dc = resitable_dc,
								multiple_value = multiple_value,
								horde = horde)

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
		table_id = 'minion'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []	
		body['font'] = font
				
		body = adv_minion_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/minion/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_minion(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvMinion).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/modifiers/create', methods=['POST'])
def advantage_post_modifiers():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_modifiers_post_errors(data)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
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

		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		environment = db_integer(Environment, environment)
		sense = db_integer(Sense, sense)
		mod_range = db_integer(Ranged, mod_range)
		subsense = db_integer(SubSense, subsense)
		cover = db_integer(Cover, cover)
		conceal = db_integer(Conceal, conceal)
		maneuver = db_integer(Maneuver, maneuver)
		weapon_melee = db_integer(WeaponType, weapon_melee)
		weapon_ranged = db_integer(WeaponType, weapon_ranged)
		condition = db_integer(Condition, condition)
		power = db_integer(Power, power)
		consequence = db_integer(Consequence, consequence)
		creature = db_integer(Creature, creature)
		emotion = db_integer(Emotion, emotion)
		conflict = db_integer(ConflictAction, conflict)
		profession = db_integer(Job, profession)
		bonus_conflict = db_integer(ConflictAction, bonus_conflict)
		penalty_conflict = db_integer(ConflictAction, penalty_conflict)
		bonus_check = db_integer(Check, bonus_check)
		bonus_check_range = db_integer(Ranged, bonus_check_range)
		penalty_check = db_integer(Check, penalty_check)
		penalty_check_range = db_integer(Ranged, penalty_check_range)

		bonus = integer(bonus)
		penalty = integer(penalty)
		bonus_trait = integer(bonus_trait)
		bonus_check = integer(bonus_check)
		bonus_check_range = integer(bonus_check_range)
		penalty_trait = integer(penalty_trait)
		penalty_check = integer(penalty_check)
		penalty_check_range = integer(penalty_check_range)
		multiple_count = integer(multiple_count)
		lasts = integer(lasts)
	
		entry = AdvMod(advantage_id = advantage_id,
							benefit = benefit,
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
							lasts = lasts)

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
				
		body = adv_modifiers_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/modifiers/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_modifiers(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvMod).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/opposed/create', methods=['POST'])
def advantage_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	opponent_trait_type = request.get_json()['opponent_trait_type']
	opponent_trait = request.get_json()['opponent_trait']
	opponent_mod = request.get_json()['opponent_mod']
	player_check = request.get_json()['player_check']
	opponent_check = request.get_json()['opponent_check']
	multiple = request.get_json()['multiple']

	try:
		player_check = db_integer(Check, player_check)
		opponent_check = db_integer(Check, opponent_check)

		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		trait = integer(trait)
		mod = integer(mod)
		opponent_trait = integer(opponent_trait)
		opponent_mod = integer(opponent_mod)

		entry = AdvOpposed(advantage_id = advantage_id,
								benefit = benefit,
								trait_type = trait_type,
								trait = trait,
								mod = mod,
								opponent_trait_type = opponent_trait_type,
								opponent_trait = opponent_trait,
								opponent_mod = opponent_mod,
								player_check = player_check,
								opponent_check = opponent_check,
								multiple = multiple)

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
				
		body = adv_opposed_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/opposed/delete/<advantage_id>', methods=['DELETE'])
def delete_post_opposed(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvOpposed).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/points/create', methods=['POST'])
def advantage_post_points():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_points_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	spend = request.get_json()['spend']
	condition_cost = request.get_json()['condition_cost']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	equipment_points = request.get_json()['equipment_points']
	equipment_vehicles = request.get_json()['equipment_vehicles']
	equipment_headquarters = request.get_json()['equipment_headquarters']
	initiative_cost = request.get_json()['initiative_cost']
	twenty = request.get_json()['twenty']
	check_bonus = request.get_json()['check_bonus']
	check_cost = request.get_json()['check_cost']
	check_turns = request.get_json()['check_turns']
	check_target = request.get_json()['check_target']
	check_all = request.get_json()['check_all']
	benefit_choice = request.get_json()['benefit_choice']
	benefit_count = request.get_json()['benefit_count']
	benefit_cost = request.get_json()['benefit_cost']
	benefit_turns = request.get_json()['benefit_turns']
	ranks_gained = request.get_json()['ranks_gained']
	ranks_max = request.get_json()['ranks_max']
	ranks_lasts = request.get_json()['ranks_lasts']
	ranks_trait_type = request.get_json()['ranks_trait_type']
	ranks_trait = request.get_json()['ranks_trait']

	try:
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)

		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
		benefit_choice = db_integer(Benefit, benefit_choice)

		condition_cost = integer(condition_cost)
		equipment_points = integer(equipment_points)
		initiative_cost = integer(initiative_cost)
		twenty = integer(twenty)
		check_bonus = integer(check_bonus)
		check_cost = integer(check_cost)
		check_turns = integer(check_turns)
		benefit_count = integer(benefit_count)
		benefit_cost = integer(benefit_cost)
		benefit_turns = integer(benefit_turns)
		ranks_gained = integer(ranks_gained)
		ranks_max = integer(ranks_max)
		ranks_lasts = integer(ranks_lasts)
		ranks_trait = integer(ranks_trait)

		entry = AdvPoints(advantage_id = advantage_id,
								benefit = benefit,
								spend = spend,
								condition_cost = condition_cost,
								condition1 = condition1,
								condition2 = condition2,
								equipment_points = equipment_points,
								equipment_vehicles = equipment_vehicles,
								equipment_headquarters = equipment_headquarters,
								initiative_cost = initiative_cost,
								twenty = twenty,
								check_bonus = check_bonus,
								check_cost = check_cost,
								check_turns = check_turns,
								check_target = check_target,
								check_all = check_all,
								benefit_choice = benefit_choice,
								benefit_count = benefit_count,
								benefit_cost = benefit_cost,
								benefit_turns = benefit_turns,
								ranks_gained = ranks_gained,
								ranks_max = ranks_max,
								ranks_lasts = ranks_lasts,
								ranks_trait_type = ranks_trait_type,
								ranks_trait = ranks_trait)

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
		table_id = 'points'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_points_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/points/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_points(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvPoints).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/resist/create', methods=['POST'])
def advantage_post_resist():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_resist_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	which = request.get_json()['which']

	try:
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)

		trait = integer(trait)
		mod = integer(mod)

		entry = AdvResist(advantage_id = advantage_id,
								benefit = benefit,
								trait_type = trait_type,
								trait = trait,
								mod = mod,
								which = which)

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
		table_id = 'resist'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_resist_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/resist/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_resist(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvResist).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/rounds/create', methods=['POST'])
def advantage_post_rounds():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_rounds_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	rounds = request.get_json()['rounds']
	cost = request.get_json()['cost']
	check = request.get_json()['check']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	end = request.get_json()['end']

	try:
		cost = db_integer(Action, cost)
		check = db_integer(Check, check)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
		rounds = integer(rounds)
		trait = integer(trait)

		entry = AdvRounds(advantage_id = advantage_id,
								benefit = benefit,
								rounds = rounds,
								cost = cost,
								check = check,
								trait_type = trait_type,
								trait = trait,
								end = end)

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
		table_id = 'rounds'	
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot	
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_rounds_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/rounds/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_rounds(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvRounds).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/skill/create', methods=['POST'])
def advantage_poat_skill():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_skill_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	replaced_trait_type = request.get_json()['replaced_trait_type']
	replaced_trait = request.get_json()['replaced_trait']
	multiple = request.get_json()['multiple']
	
	try:
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)

		trait = integer(trait)
		replaced_trait = integer(replaced_trait)

		entry = AdvSkill(advantage_id = advantage_id,
								benefit = benefit,
								trait_type = trait_type,
								trait = trait,
								replaced_trait_type = replaced_trait_type,
								replaced_trait = replaced_trait,
								multiple = multiple)

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
		table_id = 'skill'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_skill_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/skill/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_skill(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvSkill).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/time/create', methods=['POST'])
def advantage_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_time_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	time_type = request.get_json()['time_type']
	value_type = request.get_json()['value_type']
	value = request.get_json()['value']
	units = request.get_json()['units']
	time_value = request.get_json()['time_value']
	math = request.get_json()['math']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	dc = request.get_json()['dc']
	check_type = request.get_json()['check_type']
	recovery = request.get_json()['recovery']
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_time = request.get_json()['recovery_time']
	recovery_incurable = request.get_json()['recovery_incurable']

	try:
		units = db_integer(Unit, units)
		math = db_integer(Math, math)
		check_type = db_integer(Check, check_type)

		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value = integer(value)
		time_value = integer(time_value)
		trait = integer(trait)
		dc = integer(dc)
		recovery_penalty = integer(recovery_penalty)
		recovery_time = integer(recovery_time)

		entry = AdvTime(advantage_id = advantage_id,
							benefit = benefit,
							time_type = time_type,
							value_type = value_type,
							value = value,
							units = units,
							time_value = time_value,
							math = math,
							trait_type = trait_type,
							trait = trait,
							dc = dc,
							check_type = check_type,
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
				
		body = adv_time_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/time/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_time(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvTime).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/variable/create', methods=['POST'])
def advantage_post_variable():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_variable_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	active = request.get_json()['active']
	effort = request.get_json()['effort']

	try:
		advantage_id = integer(advantage_id)
		trait = integer(trait)

		entry = AdvVariable(advantage_id = advantage_id,
								trait_type = trait_type,
								trait = trait, 
								active = active,
								effort = effort)

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
		table_id = 'variable'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
				
		body = adv_variable_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/variable/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_post_variable(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvVariable).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/levels/create', methods=['POST'])
def advantage_post_levels():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_levels_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	advantage_id = request.get_json()['advantage_id']
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

	advantage_id = integer(advantage_id)

	level_check = db.session.query(LevelType).filter(LevelType.name == level_type).first()
	if level_check is None:

		try:
			level_add = LevelType(advantage_id=advantage_id,
									name=level_type)

			db.session.add(level_add)
			db.session.commit()

			type_id = level_add.id

			body['level_type_id'] = type_id
			body['level_type'] = level_add.name
			body['created'] = False
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()

		finally:
			db.session.close()
		
	else:
		level_advantage = level_check.advantage_id
		print(advantage_id)
		print(level_advantage)
		if advantage_id != level_advantage:
			body['success'] = False
			body['error_msgs'] = ['There is already a level type with that name.']
			return jsonify(body)

		type_id = level_check.id
		body['created'] = True

	try:
		entry = Levels(advantage_id = advantage_id,
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

		body = adv_levels_post(entry, body, cells)
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
	
	return jsonify(body)


@advantage.route('/advantage/levels/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_levels(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(Levels).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this level. You may have already applied it to another rule.  Delete that rule first.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)