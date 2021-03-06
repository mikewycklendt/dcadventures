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

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import AdvCircType, AdvDCType, AdvDegreeType, AdvMoveType, AdvTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, value_limit, select_check, check_of, multiple_effect_check, multiple_link_check, required_setting, linked_group_check, required_link_field, linked_field, required_rule
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from posts.advantage_posts import adv_benefit_post, adv_move_post, adv_check_post, adv_circ_post, adv_combined_post, adv_condition_post, adv_dc_post, adv_degree_post, adv_effort_post, adv_minion_post, adv_modifiers_post, adv_opposed_post, adv_points_post, adv_resist_post, adv_rounds_post, adv_skill_post, adv_time_post, adv_variable_post
from errors.advantage_errors import adv_benefit_post_errors, adv_check_post_errors, adv_move_post_errors, adv_circ_post_errors, adv_combined_post_errors, adv_condition_post_errors, adv_dc_post_errors, adv_degree_post_errors, adv_effort_post_errors, adv_minion_post_errors, adv_modifiers_post_errors, adv_opposed_post_errors, adv_points_post_errors, adv_resist_post_errors, adv_rounds_post_errors, adv_skill_post_errors, adv_time_post_errors, adv_variable_post_errors, adv_save_errors
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

	advantage_includes = {'base_form': 'advantage_create/base_form.html', 'dc_table': 'advantage_create/dc_table.html', 'modifiers': 'advantage_create/modifiers.html', 'skill': 'advantage_create/skill.html', 'opposed': 'advantage_create/opposed.html', 'circ': 'advantage_create/circ.html', 'degree_mod': 'advantage_create/degree_mod.html', 'levels': 'advantage_create/levels.html', 'points': 'advantage_create/points.html', 'time': 'advantage_create/time.html', 'combined': 'advantage_create/combined.html', 'resist': 'advantage_create/resist.html', 'variable': 'advantage_create/variable.html', 'alt_check': 'advantage_create/alt_check.html', 'effort': 'advantage_create/effort.html', 'benefit': 'advantage_create/benefit.html', 'rounds': 'advantage_create/rounds.html', 'condition': 'advantage_create/condition.html', 'minion': 'advantage_create/minion.html', 'move': 'advantage_create/move.html'}

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

	actions = db.session.query(Action).filter(Action.hide == None).all()

	advantage_type = AdvantageType.query.all()

	advantages = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()

	benefits = db.session.query(Benefit).filter_by(approved=True).order_by(Benefit.name).all()
	benefits_all = db.session.query(Benefit).order_by(Benefit.name).all()

	checks = db.session.query(Check).filter(Check.hide == None).all()

	complexity = Complex.query.all()

	concealment = Conceal.query.all()

	conditions = db.session.query(Condition).filter(Condition.hide == None).order_by(Condition.name).all()

	conflicts = db.session.query(ConflictAction).filter(ConflictAction.hide == None).order_by(ConflictAction.name).all()

	consequences = db.session.query(Consequence).filter(Consequence.hide == None).order_by(Consequence.name).all()

	cover = Cover.query.all()
	
	creatures = db.session.query(Creature).filter(Creature.show == True).order_by(Creature.name).all()

	defenses = db.session.query(Defense).filter(Defense.hide == None).all()

	distances = db.session.query(Unit).filter_by(type_id=3)
		
	emotions = db.session.query(Emotion).filter(Emotion.show == True).order_by(Emotion.name).all()
	
	environments = db.session.query(Environment).filter(Environment.show == True).order_by(Environment.name).all()
	
	equip_type = EquipType.query.all()

	expertise = db.session.query(SkillBonus).filter_by(skill=5).all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	maths = Math.query.all()
	
	maneuvers = db.session.query(Maneuver).filter(Maneuver.hide == None).order_by(Maneuver.name).all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	nature = db.session.query(Nature).filter_by(show=True).all()
	
	powers = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()
	
	professions = db.session.query(Job).filter(Job.show == True).order_by(Job.name).all()

	ranged = db.session.query(Ranged).filter_by(show=True)
	
	ranges = Range.query.all()
	
	senses = db.session.query(Sense).filter(Sense.hide == None).order_by(Sense.name).all()

	subsenses = db.session.query(SubSense).filter(SubSense.hide == None).order_by(SubSense.name).all()
	
	times = db.session.query(Unit).filter_by(type_id=2).all()

	unit_type = MeasureType.query.all()

	units = Unit.query.all()

	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1).all()
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2).all()


	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	attached = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}, {'type': 'with', 'name': 'With Skill Check'}, {'type': 'before_attack', 'name': 'Before Attack Check'}, {'type': 'after_attack', 'name': 'After Attack Check'}, {'type': 'opp_success', 'name': 'After Opponent Success'}, {'type': 'success', 'name': 'After Player Success'}, {'type': 'opp_fail', 'name': 'After Opponent Failure'}, {'type': 'fail', 'name': 'After Player Failure'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	circ_effect = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'trait', 'name': 'Applied to other Check'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}, {'type': 'tools', 'name': 'If Tools'}, {'type': 'materials', 'name': 'If Materials'}, {'type': 'env', 'name': 'If Environment'}, {'type': 'nature', 'name': 'If Nature'}]

	circ_targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]

	circ_trait = [{'type': '', 'name': 'Applied to'}, {'type': 'all', 'name': 'All Checks'}, {'type': 'object', 'name': 'This Object'}, {'type': 'character', 'name': 'This Character'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'condition', 'name': 'From Condition'}, {'type': 'override', 'name': 'Override Trait Circumstance'}]

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'change', 'name': 'Condition Change'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	condition = [{'type': '', 'name': 'Condition Type'}, {'type': 'active', 'name': 'Active Condition'}, {'type': 'change', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}, {'type': 'null', 'name': 'Nullify Condition'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Advantaage Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'routine', 'name': 'Routine Check'}, {'type': 'none', 'name': 'No DC'}, {'type': 'choice', 'name': 'Chosen by Player'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'check', 'name': 'Check'}, {'type': 'object', 'name': 'Object Destroyed'}, {'type': 'dc', 'name': 'Attach DC to Object'}]

	degree_type = [{'type': '', 'name': 'Degree Type'}, {'type': '>', 'name': '>'}, {'type': '<', 'name': '<'}, {'type': '>=', 'name': '>='}, {'type': '<=', 'name': '<='} ]

	direction = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]

	distance = [{'type': '', 'name': 'Distance Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'unit_math', 'name': 'Unit Math'}, {'type': 'rank_math', 'name': 'Rank Math'}]

	effect_target = [{'type': '', 'name': 'Effect Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	effort = [{'type': '', 'name': 'Effect'}, {'type': 'benefit', 'name': 'Benefit'}]

	equipment_use = [{'type': '', 'name': 'Use Type'}, {'type': 'use', 'name': 'With Use of'}, {'type': 'resist', 'name': 'Resist'}]

	frequency = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}, {'type': 'player', 'name': 'Player Choice'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	low_high = [{'type': '', 'name': 'Lower or Higher'}, {'type': 'lower', 'name': 'Lower'}, {'type': 'high', 'name': 'Higher'}, {'type': 'equal', 'name': 'Equal'}]
	
	materials = [{'type': '', 'name': 'Materials'}, {'type': 'with', 'name': 'With Materials'}, {'type': 'improper', 'name': 'Improper Materials'}, {'type': 'none', 'name': 'No Materials'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill_rank', 'name': 'Skill Rank Modifier'}, {'type': 'skill_unit', 'name': 'Skill Unit Modifier'}]

	measure_effect_circ = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}]
		
	measure_type = [{'type': '', 'name': 'Type'}, {'type': '=', 'name': '='}, {'type': '>', 'name': '>'}, {'type': '<', 'name': '<'}, {'type': '>=', 'name': '>='}, {'type': '<=', 'name': '<='} ]

	minion_type = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'success', 'name': 'Successive'}, {'type': 'optional', 'name': 'Successive Optional'}]

	multiple_time = [{'type': '', 'name': 'If Multiple'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'degree', 'name': 'Degree'}, {'type': 'dc', 'name': 'DC'}, {'type': 'gm', 'name': 'GM Choice'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	nullify = [{'type': '', 'name': 'Nullify Type'}, {'type': 'dc', 'name': 'DC'}, {'type': 'mod', 'name': 'Modifier'}]

	offers  = [{'type': '', 'name': 'Effect'}, {'type': 'required', 'name': 'Requires'}, {'type': 'provides', 'name': 'Provides'}]

	permanence = [{'type': '', 'name': 'Permanence'}, {'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]

	points = [{'type': '', 'name': 'Spend For'}, {'type': 'ranks', 'name': 'Gain Ranks'}, {'type': 'benefit', 'name': 'Benefit'}, {'type': 'check', 'name': 'Circumstance Modifier'}, {'type': 'equip', 'name': 'Equipment'}, {'type': 'condition', 'name': 'Change Condition'}, {'type': 'initiative', 'name': 'Gain Initiative'}, {'type': '20', 'name': 'Automatic 20'}]

	recovery = [{'type': '', 'name': 'Target'}, {'type': 'player', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'either', 'name': 'Either'}]

	repair = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]

	required_tools = [{'type': '', 'name': 'Tools'}, {'type': 'correct', 'name': 'Correct Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'gm', 'name': 'GM Decides'}]

	rounds_end = [{'type': '', 'name': 'Ends'}, {'type': 'action', 'name': 'Stop Taking Action'}, {'type': 'resist', 'name': 'Successful Resistance'}, {'type': 'danger', 'name': 'Danger'}]

	simultaneous = [{'type': '', 'name': 'Type'}, {'type': 'same', 'name': 'At Same Time'}, {'type': 'maintain', 'name': 'While Maintaining Previous'}, {'type': 'both', 'name': 'Either'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]

	speed = [{'type': '', 'name': 'Speed Type'}, {'type': 'rank', 'name': 'Speed Rank'}, {'type': 'rank_mod', 'name': 'Speed Modifier'}, {'type': 'mod', 'name': 'Math'}]

	target = [{'type': '', 'name': 'Target'}, {'type': 'become', 'name': 'Become Target'}, {'type': 'redirect', 'name': 'Redirect From Self'}, {'type': 'setup', 'name': 'Transfer Action Result to Teammate'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	time_effect = [{'type': '', 'name': 'Time Effect'}, {'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time Limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}, {'type': 'effect', 'name': 'Time Effect Happens'}, {'type': 'recover', 'name': 'Recovery Time'}]
	
	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Rank Marh'}, {'type': 'time', 'name': 'Time Rank'}, {'type': 'mod', 'name': 'Time Rank Modifier'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'gm', 'name': 'Set by GM'}, {'type': 'player', 'name': 'Set by Player'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_Advantage', 'name': 'This Advantage'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'active', 'name': 'Active Opponent Rank'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}, {'type': 'any', 'name': 'Any Trait'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]
	
	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	value_type_mod = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'Modifier'}]

	which = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Value'}, {'type': 'low', 'name': 'Lower Value'}]

	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]



	advantage_circ = linked_options(AdvCirc, Advantage, 'advantage_id', 'keyword')

	advantage_dc = linked_options(AdvDC, Advantage, 'advantage_id', 'keyword')
	
	advantage_degree = linked_options(AdvDegree, Advantage, 'advantage_id', 'keyword')
	
	advantage_opposed = linked_options(AdvOpposed, Advantage, 'advantage_id', 'keyword')
	
	advantage_time = linked_options(AdvTime, Advantage, 'advantage_id', 'keyword')

	advantage_move = linked_options(AdvMove, Advantage, 'advantage_id', 'keyword')
	
	advantage_check = linked_options(AdvCheck, Advantage, 'advantage_id', 'keyword')

	advantage_circ_type = linked_options(AdvCircType, Advantage, 'advantage_id', 'name')

	advantage_dc_type = linked_options(AdvDCType, Advantage, 'advantage_id', 'name')
	
	advantage_degree_type = linked_options(AdvDegreeType, Advantage, 'advantage_id', 'name')
	
	advantage_time_type = linked_options(AdvTimeType, Advantage, 'advantage_id', 'name')

	advantage_move_type = linked_options(AdvMoveType, Advantage, 'advantage_id', 'name')



	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, advantage_includes=advantage_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							advantage_type=advantage_type, actions=actions, checks=checks, conditions=conditions, dc_type=dc_type, modifier_type=modifier_type, targets=targets, modifier_effect=modifier_effect,
							traits=traits, who_check=who_check, circ_type=circ_type, circ_null=circ_null, permanence=permanence, low_high=low_high, deg_mod_type=deg_mod_type, level_types=level_types, 
							value_type= value_type, maths=maths, measure_rank=measure_rank, condition_type=condition_type, updown=updown, knowledge=knowledge, specificity=specificity, negatives=negatives, 
							positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, points=points, conflicts=conflicts, consequences=consequences, action_type=action_type, ranges=ranges,
							times=times, time_effect=time_effect, advantages=advantages, which=which, check_trigger=check_trigger, check_type=check_type, benefits=benefits, effort=effort, rounds_end=rounds_end,
							environments=environments, senses=senses, subsenses=subsenses, modifier_trigger=modifier_trigger, multiple=multiple, creatures=creatures, professions=professions, powers=powers,
							emotions=emotions, simultaneous=simultaneous, multiple_opposed=multiple_opposed, tools=tools, condition=condition, maneuvers=maneuvers, cover=cover, concealment=concealment,
							ranged=ranged, target=target, weapon_melee=weapon_melee, weapon_ranged=weapon_ranged, minion_type=minion_type, benefits_all=benefits_all, defenses=defenses, expertise=expertise,
							circ_effect=circ_effect, nature=nature, circ_trait=circ_trait, materials=materials, circ_targets=circ_targets, measure_effect_circ=measure_effect_circ, measure_type=measure_type,
							unit_type=unit_type, units=units, effect_target=effect_target, dc_value=dc_value, measure_effect=measure_effect, damage_type=damage_type, inflict=inflict, offers=offers, 
							required_tools=required_tools, complexity=complexity, equipment_use=equipment_use, equip_type=equip_type, repair=repair, degree_type=degree_type, nullify=nullify, direction=direction,
							speed=speed, distance=distance, distances=distances, attached=attached, frequency=frequency, multiple_time=multiple_time, time_value=time_value, recovery=recovery)

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
		body['circ'] = []
				
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
		body['circ'] = []
				
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
		body['circ'] = []
						
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
		body['circ'] = []
				
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
		body['circ'] = []
				
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
	body['new'] = False
	body['new_items'] = []
	body['error_msgs'] = []
	body['success'] = True

	body = user_item(Emotion, 'Emotion', emotion, emotion_other, 'modifiers_emotion', body)
	emotion = body['output']
	
	body = user_item(Environment, 'Environment', environment, environment_other, 'modifiers_environment', body)
	environment = body['output']
	
	body = user_item(Creature, 'Creature', creature, creature_other, 'modifiers_creature', body)
	creature = body['output']
	
	body = user_item(Job, 'Profession', profession, profession_other, 'modifiers_profession', body)
	creature = body['output']

	if body['success'] == False:
		return jsonify(body)

	try:
		
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
		body['circ'] = []
				
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
		body['circ'] = []
				
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
		body['circ'] = []
				
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
		body['circ'] = []
				
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
	benefit = request.get_json()['benefit']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
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
		body['circ'] = []
				
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
		body['circ'] = []
				
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




@advantage.route('/advantage/check/create', methods=['POST'])
def advantage_post_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	check_type = request.get_json()['check_type']
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
	degree = request.get_json()['degree']
	circ = request.get_json()['circ']
	dc = request.get_json()['dc']
	dc_value = request.get_json()['dc_value']
	time = request.get_json()['time']
	move = request.get_json()['move']
	keyword = request.get_json()['keyword']
	attack = request.get_json()['attack']
	opposed = request.get_json()['opposed']
	condition = request.get_json()['condition']
	condition_target = request.get_json()['condition_target']
	conditions_target = request.get_json()['conditions_target']

	degree = db_integer(AdvDegreeType, degree)
	circ = db_integer(AdvCircType, circ)
	dc = db_integer(AdvDCType, dc)
	time = db_integer(AdvTimeType, time)
	move = db_integer(AdvMoveType, move)
	opposed = db_integer(AdvOpposed, opposed)
	dc_value = db_integer(AdvDC, dc_value)

	attack = integer(attack)

	check_type = db_integer(Check, check_type)
	conflict = db_integer(ConflictAction, conflict)
	conflict_range = db_integer(Ranged, conflict_range)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	condition = db_integer(Condition, condition)

	trait = integer(trait)
	action = integer(action)

	entry = AdvCheck(advantage_id = advantage_id,
						benefit = benefit,
						check_type = check_type,
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
						free = free,
						degree = degree,
						circ = circ,
						dc = dc,
						dc_value = dc_value,
						time = time,
						move = move,
						keyword = keyword,
						attack = attack,
						opposed = opposed,
						condition = condition,
						condition_target = condition_target,
						conditions_target = conditions_target


					)

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
	body['circ'] = []

	body = adv_check_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/check/delete/<id>', methods=['DELETE'])
def delete_advantage_check(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(AdvCheck).filter_by(id=id).delete()
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

@advantage.route('/advantage/circ/create', methods=['POST'])
def advantage_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	circ_target = request.get_json()['circ_target']
	mod = request.get_json()['mod']
	effect = request.get_json()['effect']
	speed = request.get_json()['speed']
	target = request.get_json()['target']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	condition_type = request.get_json()['condition_type']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	conditions = request.get_json()['conditions']
	conditions_effect = request.get_json()['conditions_effect']
	measure_effect = request.get_json()['measure_effect']
	measure_type = request.get_json()['measure_type']
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
	surface = request.get_json()['surface']
	circumstance = request.get_json()['circumstance']
	lasts = request.get_json()['lasts']
	title = request.get_json()['title']
	tools = request.get_json()['tools']
	materials = request.get_json()['materials']
	max = request.get_json()['max']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	trait_target = request.get_json()['trait_target']
	environment = request.get_json()['environment']
	nature = request.get_json()['nature']
	check_type = request.get_json()['check_type']

	errors = adv_circ_post_errors(data)

	errors = level_reference('advantage_circ', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)



	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	environment = db_integer(Environment, environment)
	nature = db_integer(Nature, nature)
	check_type = db_integer(Check, check_type)

	lasts = db_integer(AdvTime, lasts)


	mod = integer(mod)
	speed = integer(speed)
	conditions = integer(conditions)
	conditions_effect = integer(conditions_effect)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	max = integer(max)
	trait = integer(trait)

	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(AdvCirc, AdvCircType, 'advantage_id', advantage_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)


	entry = AdvCirc(advantage_id = advantage_id,
						benefit = benefit,
						circ_target = circ_target,
						mod = mod,
						effect = effect,
						speed = speed,
						target = target,
						level_type = level_type,
						level = level,
						condition_type = condition_type,
						condition1 = condition1,
						condition2 = condition2,
						conditions = conditions,
						conditions_effect = conditions_effect,
						measure_effect = measure_effect,
						measure_type = measure_type,
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
						surface = surface,
						circumstance = circumstance,
						lasts = lasts,
						title = title,
						tools = tools,
						materials = materials,
						max = max,
						trait_type = trait_type,
						trait = trait,
						trait_target = trait_target,
						environment = environment,
						nature = nature,
						check_type = check_type
					)

	db.session.add(entry)
	db.session.commit()

	body['id'] = entry.id
	error = False
	error_msg = []

	rows = columns	
	mods = []
	cells = []
	table_id = 'circ'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['circ'] = []	
	
	body = adv_circ_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/circ/delete/<id>', methods=['DELETE'])
def delete_advantage_circ(id):
	
	body = delete_link(AdvCirc, AdvCircType, id)
	return jsonify(body)

@advantage.route('/advantage/dc/create', methods=['POST'])
def advantage_post_dc():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
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
	surface = request.get_json()['surface']
	condition = request.get_json()['condition']
	levels = request.get_json()['levels']
	damage = request.get_json()['damage']
	cover = request.get_json()['cover']
	complex = request.get_json()['complex']
	measure = request.get_json()['measure']
	conceal = request.get_json()['conceal']
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
	measure_type = request.get_json()['measure_type']
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
	tools_check = request.get_json()['tools_check']
	cover_effect = request.get_json()['cover_effect']
	cover_type = request.get_json()['cover_type']
	conceal_effect = request.get_json()['conceal_effect']
	conceal_type = request.get_json()['conceal_type']
	tools = request.get_json()['tools']
	variable_check = request.get_json()['variable_check']
	variable = request.get_json()['variable']
	time = request.get_json()['time']
	title = request.get_json()['title']
	effect_target = request.get_json()['effect_target']
	equipment_use = request.get_json()['equipment_use']
	equipment_type = request.get_json()['equipment_type']
	equipment = request.get_json()['equipment']
	equip = request.get_json()['equip']


	errors = adv_dc_post_errors(data)

	errors = level_reference('advantage_dc', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	math = db_integer(Math, math)
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
	equipment_type = db_integer(EquipType, equipment_type)
	equipment = db_integer(Equipment, equipment)

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

	cover_type = db_integer(Cover, cover_type)
	conceal_type = db_integer(Conceal, conceal_type)

	variable = db_integer(AdvCheck, variable)
	time = db_integer(AdvTime, time)

	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(AdvDC, AdvDCType, 'advantage_id', advantage_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = AdvDC(advantage_id = advantage_id,
					benefit = benefit,
					target = target,
					dc = dc,
					description = description,
					value = value,
					mod = mod,
					math_value = math_value,
					math = math,
					math_trait_type = math_trait_type,
					math_trait = math_trait,
					surface = surface,
					condition = condition,
					levels = levels,
					damage = damage,
					cover = cover,
					complex = complex,
					measure = measure,
					conceal = conceal,
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
					measure_type = measure_type,
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
					keyword = keyword,
					action_no_damage = action_no_damage,
					condition_no_damage = condition_no_damage,
					complexity = complexity,
					tools_check = tools_check,
					cover_effect = cover_effect,
					cover_type = cover_type,
					conceal_effect = conceal_effect,
					conceal_type = conceal_type,
					tools = tools,
					variable_check = variable_check,
					variable = variable,
					time = time,
					title = title,
					effect_target = effect_target,
					equipment_use = equipment_use,
					equipment_type = equipment_type,
					equipment = equipment,
					equip = equip
				)

	db.session.add(entry)
	db.session.commit()

	body['id'] = entry.id
	error = False
	error_msgs = []

	rows = columns	
	mods = []
	cells = []
	table_id = 'dc'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['circ'] = []
	
	body = adv_dc_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/dc/delete/<id>', methods=['DELETE'])
def delete_advantage_dc(id):
	
	body = delete_link(AdvDC, AdvDCType, id)
	return jsonify(body)

@advantage.route('/advantage/degree/create', methods=['POST'])
def advantage_post_degree():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
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
	level_time = request.get_json()['level_time']
	circumstance = request.get_json()['circumstance']
	circ_target = request.get_json()['circ_target']
	measure_effect = request.get_json()['measure_effect']
	measure_type = request.get_json()['measure_type']
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
	variable = request.get_json()['variable']
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
	duration = request.get_json()['duration']
	title = request.get_json()['title']
	effect_target = request.get_json()['effect_target']
	value_type = request.get_json()['value_type']
	description = request.get_json()['description']

	errors = adv_degree_post_errors(data)

	errors = level_reference('advantage_degree', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	
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

	opposed = db_integer(AdvOpposed, opposed)
	resist_dc = db_integer(AdvDC, resist_dc)
	skill_dc = db_integer(AdvDC, skill_dc)
	compare = db_integer(AdvOpposed, compare)
	variable = db_integer(AdvCheck, variable)
	attack_turns = db_integer(AdvTime, attack_turns)
	condition_turns = db_integer(AdvTime, condition_turns)
	level_time = db_integer(AdvTime, level_time)
	linked = db_integer(AdvDegree, linked)

	resist_trait = integer(resist_trait)
	skill_trait = integer(skill_trait)
	routine_trait = integer(routine_trait)
	routine_mod = integer(routine_mod)
	attack = integer(attack)
	attack_turns = integer(attack_turns)
	duration = integer(duration)

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
	nullify = integer(nullify)
	
	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(AdvDegree, AdvDegreeType, 'advantage_id', advantage_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = AdvDegree(advantage_id = advantage_id,
						benefit = benefit,
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
						level_time = level_time,
						circumstance = circumstance,
						circ_target = circ_target,
						measure_effect = measure_effect,
						measure_type = measure_type,
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
						variable = variable,
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
						compare = compare,
						title = title,
						effect_target = effect_target,
						value_type = value_type,
						description = description)

	db.session.add(entry)
	db.session.commit()

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
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['circ'] = []
	
	body = adv_degree_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/degree/delete/<id>', methods=['DELETE'])
def delete_advantage_degree(id):
		
	body = delete_link(AdvDegree, AdvDegreeType, id)
	return jsonify(body)

@advantage.route('/advantage/move/create', methods=['POST'])
def advantage_post_move():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	speed = request.get_json()['speed']
	speed_rank = request.get_json()['speed_rank']
	speed_rank_mod = request.get_json()['speed_rank_mod']
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
	degree = request.get_json()['degree']
	circ = request.get_json()['circ']
	dc = request.get_json()['dc']
	time = request.get_json()['time']
	keyword = request.get_json()['keyword']
	title = request.get_json()['title']

	errors = adv_move_post_errors(data)

	errors = linked_move(AdvCirc, circ, 'Circumstance', errors)
	errors = linked_move(AdvDC, dc, 'DC', errors)
	errors = linked_move(AdvDegree, degree, 'Circumstance', errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)
	
	degree = db_integer(AdvDegree, degree)
	circ = db_integer(AdvCirc, circ)
	dc = db_integer(AdvDC, dc)
	time = db_integer(AdvTime, time)

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
	speed_rank_mod = integer(speed_rank_mod)

	speed_math1 = db_integer(Math, speed_math1)
	speed_math2 = db_integer(Math, speed_math2)
	distance_units = db_integer(Unit, distance_units)
	distance_rank_math1 = db_integer(Math, distance_rank_math1)
	distance_rank_math2 = db_integer(Math, distance_rank_math2)
	distance_unit_math1 = db_integer(Math, distance_unit_math1)
	distance_unit_math2 = db_integer(Math, distance_unit_math2)
	distance_math_units = db_integer(Unit, distance_math_units)

	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(AdvMove, AdvMoveType, 'advantage_id', advantage_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)
	
	entry = AdvMove(advantage_id = advantage_id,
						benefit = benefit,
						speed = speed,
						speed_rank = speed_rank,
						speed_rank_mod = speed_rank_mod,
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
						degree = degree,
						dc = dc,
						circ = circ,
						title = title,
						keyword = keyword, 
						time = time)			


	db.session.add(entry)

	db.session.commit()

	body['id'] = entry.id
	error = False
	error_msg = []

	rows = columns	
	mods = []
	cells = []
	table_id = 'move'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['circ'] = []
	
	body = adv_move_post(entry, body, cells)
	
	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/move/delete/<id>', methods=['DELETE'])
def delete_advantage_move(id):
		
	body = delete_link(AdvMove, AdvMoveType, id)
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
	benefit = request.get_json()['benefit']
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
	description = request.get_json()['description']
	keyword = request.get_json()['keyword']
	degree = request.get_json()['degree']
	circ = request.get_json()['circ']
	dc = request.get_json()['dc']
	time = request.get_json()['time']
	degree_check = request.get_json()['degree_check']
	circ_check = request.get_json()['circ_check']
	dc_check = request.get_json()['dc_check']
	time_check = request.get_json()['time_check']
	degree_value = request.get_json()['degree_value']
	dc_type = request.get_json()['dc_type']
	dc_player = request.get_json()['dc_player']
	circ_value = request.get_json()['circ_value']
	time_type = request.get_json()['time_type']
	recurring_type = request.get_json()['recurring_type']


	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)

	degree = db_integer(AdvDegreeType, degree)
	circ = db_integer(AdvCircType, circ)
	dc = db_integer(AdvDC, dc)
	time = db_integer(AdvTime, dc)
	recurring_value = db_integer(AdvTime, recurring_value)
	degree_value = db_integer(AdvDegree, degree_value)
	dc_type = db_integer(AdvDCType, dc_type)
	dc_player = db_integer(AdvDC, dc_player)
	circ_value = db_integer(AdvCirc, circ_value)
	time_type = db_integer(AdvTimeType, time_type)
	recurring_type = db_integer(AdvTimeType, recurring_type)

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)

	entry = AdvOpposed(advantage_id = advantage_id,
						benefit = benefit,
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
						description = description,
						keyword = keyword,
						degree = degree,
						circ = circ,
						dc = dc,
						time = time,
						degree_check = degree_check,
						circ_check = circ_check,
						dc_check = dc_check,
						time_check = time_check,
						degree_value = degree_value,
						dc_type = dc_type,
						dc_player = dc_player,
						circ_value = circ_value,
						time_type = time_type,
						recurring_type = recurring_type
					)			

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
	body['circ'] = []
	
	body = adv_opposed_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/opposed/delete/<id>', methods=['DELETE'])
def delete_advantage_opposed(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(AdvOpposed).filter_by(id=id).delete()
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

@advantage.route('/advantage/time/create', methods=['POST'])
def advantage_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	advantage_id = request.get_json()['advantage_id']
	benefit = request.get_json()['benefit']
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
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_incurable = request.get_json()['recovery_incurable']
	degree = request.get_json()['degree']
	circ = request.get_json()['circ']
	dc = request.get_json()['dc']
	turns = request.get_json()['turns']
	keyword = request.get_json()['keyword']
	title = request.get_json()['title']
	circ_type = request.get_json()['circ_type']
	degree_type = request.get_json()['degree_type']
	dc_type = request.get_json()['dc_type']
	instant = preset_convert('instant', value_type)
	player = preset_convert('player', value_type)
	gm = preset_convert('gm', value_type)
	perm = preset_convert('perm', value_type)
	round = preset_convert('round', value_type)
	next = preset_convert('next', value_type)
	scene = preset_convert('scene', value_type)
	turn = preset_convert('turn', value_type)
	time = request.get_json()['time']
	mod = request.get_json()['mod']
	mod = request.get_json()['mod']
	recovery_target = request.get_json()['recovery_target']

	errors = adv_time_post_errors(data)
	
	errors = linked_time(AdvCirc, circ, 'Circumstance', errors)
	errors = linked_time(AdvDC, dc, 'DC', errors)
	errors = linked_time(AdvDegree, degree, 'Degree', errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	rank1 = db_integer(Rank, rank1)
	rank_math = db_integer(Math, rank_math)
	rank2 = db_integer(Rank, rank2)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)

	degree = db_integer(AdvDegree, degree)
	circ = db_integer(AdvCirc, circ)
	dc = db_integer(AdvDC, dc)
	circ_type = db_integer(AdvCircType, circ_type)
	degree_type = db_integer(AdvDegreeType, degree_type)
	dc_type = db_integer(AdvDCType, dc_type)	

	rank1_value = integer(rank1_value)
	rank2_value = integer(rank2_value)
	value = integer(value)
	trait = integer(trait)
	math_value = integer(math_value)
	recovery_penalty = integer(recovery_penalty)
	time = integer(time)
	mod = integer(mod)

	turns = integer(turns)

	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(AdvTime, AdvTimeType, 'advantage_id', advantage_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = AdvTime(advantage_id = advantage_id,
						benefit = benefit,
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
						recovery_penalty = recovery_penalty,
						recovery_incurable = recovery_incurable,
						recovery_target = recovery_target,
						degree = degree,
						circ = circ,
						dc = dc,
						turns = turns,
						keyword = keyword,
						title = title,
						circ_type = circ_type,
						degree_type = degree_type,
						dc_type = dc_type,
						instant = instant,
						turn = turn,
						perm = perm,
						player = player,
						gm = gm,
						round = round,
						next = next,
						scene = scene,
						time = time,
						mod = mod
					)

	db.session.add(entry)
	db.session.commit()

	body['id'] = entry.id
	error = False
	error_msg = []

	rows = columns	
	mods = []
	cells = []
	table_id = 'time'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['title'] = ''
	body['rows'] = rows
	body['mods'] = []
	body['font'] = font
	body['circ'] = []
	
	body = adv_time_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@advantage.route('/advantage/time/delete/<id>', methods=['DELETE'])
def delete_advantage_time(id):
		
	body = delete_link(AdvTime, AdvTimeType, id)
	return jsonify(body)
