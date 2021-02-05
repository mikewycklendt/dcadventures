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

from models import Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged 
from models import setup_db, Ability,  ConflictAction, Damage, DamageType, flash
from models import Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense
from models import Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank 
from models import Levels, LevelType

from db.advanrtage_modeks import Advantage, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from posts.skill_posts import skill_ability_post, skill_check_post, skill_circ_post, skill_dc_post, skill_degree_post, skill_levels_post, skill_modifiers_post, skill_opposed_post, skill_time_post
from errors.skill_errors import skill_save_errors, skill_ability_post_errors, skill_check_post_errors, skill_circ_post_errors, skill_dc_post_errors, skill_degree_post_errors, skill_levels_post_errors, skill_modifiers_post_errors, skill_opposed_post_errors, skill_time_post_errors


load_dotenv()

import os

db_path = os.environ.get("db_path")

skill = Blueprint('skill', __name__)
db = SQLAlchemy()

@skill.route('/skill/create')
def headquarters_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'skill_create/skill_create.html'

	skill_includes = {'base_form': 'skill_create/base_form.html', 'dc': 'skill_create/dc_table.html', 'levels': 'skill_create/levels.html', 'degree_mod': 'skill_create/degree_mod.html', 'circ': 'skill_create/circ.html', 'alt_check': 'skill_create/alt_check.html', 'opposed': 'skill_create/opposed.html', 'modifiers': 'skill_create/modifiers.html', 'time': 'skill_create/time.html', 'ability': 'skill_create/ability.html'}
	
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
	
	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages = sorted(advantages_raw)

	abilities = Ability.query.all()

	complexity = Complex.query.all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	skills = Skill.query.all()

	weapon_cat = WeaponCat.query.all()

	environments = db.session.query(Environment).order_by(Environment.name).all()
	
	senses = db.session.query(Sense).order_by(Sense.name).all()
	
	ranged = db.session.query(Ranged).filter_by(show=True)

	subsenses = db.session.query(SubSense).order_by(SubSense.name).all()

	cover = Cover.query.all()

	concealment = Conceal.query.all()

	maneuvers = db.session.query(Maneuver).order_by(Maneuver.name).all()
	
	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1).all()
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2).all()

	creatures = db.session.query(Creature).order_by(Creature.name).all()
		
	emotions = db.session.query(Emotion).order_by(Emotion.name).all()

	professions = db.session.query(Job).order_by(Job.name).all()
	
	conflicts = db.session.query(ConflictAction).order_by(ConflictAction.name).all()
	
	damages = db.session.query(Descriptor).filter_by(damage=True).order_by(Descriptor.name).all()
	
	light = Light.query.all()

	checks = Check.query.all()

	actions = Action.query.all()

	defenses = Defense.query.all()

	skill_type = SkillType.query.all()

	maths = Math.query.all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	unit_type = MeasureType.query.all()

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Skill Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'choice', 'name': 'Chosen by Player'}]
	
	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Measurement'}, {'type': 'gm', 'name': 'Set by GM'}]

	value_mod = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Modifier'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_bonus', 'name': 'This Skill'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'active', 'name': 'Active Opponent Rank'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	circ_targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'distance', 'name': 'Distance Penalty'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'bonus', 'name': 'This Enhanced Skill'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}, {'type': 'skill', 'name': 'Skill Check'}, {'type': 'light', 'name': 'Lighting'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}]

	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	updown = [{'id': '', 'name': 'Direction'}, {'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	circ_effect = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'temp', 'name': 'Effect Temporary'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]
	
	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	repair = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	direction = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]

	frequency = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}]

	attached = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}]

	lasts = [{'type': '', 'name': 'Lasts'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'time', 'name': 'Time'}, {'type': 'rank', 'name': 'Time Rank'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, skill_includes=skill_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							negatives=negatives, positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, skills=skills, checks=checks, actions=actions, skill_type=skill_type, maths=maths,
							value_type=value_type, traits=traits, level_types=level_types, conditions=conditions, targets=targets, deg_mod_type=deg_mod_type, action_type=action_type, knowledge=knowledge,
							consequences=consequences, specificity=specificity, measure_rank=measure_rank, condition_type=condition_type, updown=updown, circ_effect=circ_effect, measure_effect=measure_effect,
							unit_type=unit_type, check_trigger=check_trigger, check_type=check_type, conflicts=conflicts, ranged=ranged, multiple_opposed=multiple_opposed, dc_type=dc_type, damage_type=damage_type,
							inflict=inflict, direction=direction, value_mod=value_mod, modifier_effect=modifier_effect, modifier_trigger=modifier_trigger, modifier_type=modifier_type, multiple=multiple, tools=tools,
							environments=environments, senses=senses, subsenses=subsenses, cover=cover, concealment=concealment, maneuvers=maneuvers, weapon_ranged=weapon_ranged, weapon_melee=weapon_melee,
							creatures=creatures, emotions=emotions, professions=professions, damages=damages, light=light, powers=powers, weapon_cat=weapon_cat, times=times, time_effect=time_effect,
							abilities=abilities, frequency=frequency, lasts=lasts, attached=attached, complexity=complexity, repair=repair, advantages=advantages, time_value=time_value, circ_targets=circ_targets,
							dc_value=dc_value)


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

	skill_id = db_integer(skill_id)

	entry = SkillAbility(skill_id = skill_id)

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
	try:
		db.session.query(SkillAbility).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillCheck(skill_id = skill_id)

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
	try:
		db.session.query(SkillCheck).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillCirc(skill_id = skill_id)

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
	try:
		db.session.query(SkillCirc).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillDC(skill_id = skill_id)

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
	try:
		db.session.query(SkillDC).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillDegree(skill_id = skill_id)

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
	try:
		db.session.query(SkillDegree).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillOpposed(skill_id = skill_id)

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
	try:
		db.session.query(SkillOpposed).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

	skill_id = db_integer(skill_id)

	entry = SkillTime(skill_id = skill_id)

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
	try:
		db.session.query(SkillTime).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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
		skill_id = db_integer(skill_id)
	

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
	try:
		db.session.query(SkillMod).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'feature': False })


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

		try:
			level_add = LevelType(bonus_id=skill_id,
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
		level_skill = level_check.bonus_id
		print(skill_id)
		print(level_skill)
		if skill_id != level_skill:
			body['success'] = False
			body['error_msgs'] = ['There is already a level type with that name.']
			return jsonify(body)

		type_id = level_check.id
		body['created'] = True

	try:
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
	except:
		error = True
		body['success'] = False
		body['error'] = 'There was an error processing the request'
		db.session.rollback()
	
	finally:
		db.session.close()
	
	return jsonify(body)


@skill.route('/skill/levels/delete/<id>', methods=['DELETE'])
def delete_skill_levels(id):
	try:
		db.session.query(Levels).filter_by(id=id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': id, 'level': True})



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
	elif trait == 'active':
		body['options'] = [{'id': 'Active Opponent Rank', 'name': 'Active Opponent Rank'}]
	elif trait == 'choice':
		body['options'] = [{'id': "Players Chosen DC", 'name': "Players Chosen DC"}]
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


@skill.route('/skill/icon/select', methods=['POST'])
def skill_icon_select():
	body = {}
	body['success'] = True

	id = request.get_json()['id']
	options = []

	try:
		id = int(id)
		get = db.session.query(Skill).filter_by(id=id).one()
		icon = get.icon
		body['icon'] = icon
	except:
		body['success'] = False

	print(body)
	return jsonify(body)

@skill.route('/ability/icon/select', methods=['POST'])
def ability_icon_select():
	body = {}
	body['success'] = True

	id = request.get_json()['id']
	options = []

	try:
		id = int(id)
		get = db.session.query(Ability).filter_by(id=id).one()
		icon = get.icon
		body['icon'] = icon
	except:
		body['success'] = False

	print(body)
	return jsonify(body)
