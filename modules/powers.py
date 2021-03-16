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
from db.power_models import Extra, Power, PowerCost, PowerRanks, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import PowerCircType, PowerDCType, PowerDegreeType, PowerMoveType, PowerRangedType, PowerTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert, db_multiple, id_multiple, get_multiple, var_convert
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, linked_ref, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import send_multiple, one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string, circ_cell

from errors.power_errors import power_save_errors, power_cost_post_errors, power_extra_post_errors, power_check_post_errors, power_circ_post_errors, power_dc_post_errors, power_degree_post_errors, power_move_post_errors, power_opposed_post_errors, power_time_post_errors, change_action_post_errors, character_post_errors, create_post_errors, damage_post_errors, defense_post_errors, environment_post_errors, levels_post_errors, minion_post_errors, mod_post_errors, ranged_post_errors, resist_post_errors, resisted_by_post_errors, reverse_effect_post_errors, sense_post_errors
from posts.power_posts import change_action_post, character_post, create_post, damage_post, defense_post, environment_post, levels_post, minion_post, mod_post, ranged_post, resist_post, resisted_by_post, reverse_effect_post, sense_post, power_check_post, power_circ_post, power_dc_post, power_degree_post, power_move_post, power_opposed_post, power_time_post, power_cost_post, power_extra_post
from create_functions.power_create import power_check, rule_check, rule_select, cost_check, extra_cost, extra_check, extra_convert, field_cost, multiple_cost, variable_cost, sense_cost, power_rules, valid_extra



load_dotenv()

import os

db_path = os.environ.get("db_path")

powers = Blueprint('powers', __name__)
db = SQLAlchemy()

@powers.route('/power/create')
def power_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'power_create/power_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Power'
	stylesheets.append({"style": "/static/css/power_create/power_create.css"})

	power_includes = {'base_form': 'power_create/base_form.html', 'range': 'power_create/range.html', 'resisted_by': 'power_create/resisted_by.html', 'reverse_effect': 'power_create/reverse_effect.html', 'move': 'power_create/move.html', 'levels': 'power_create/levels.html', 'category': 'power_create/category.html', 'sense': 'power_create/sense.html', 'ranks': 'power_create/ranks.html', 'circ': 'power_create/circ.html', 'create': 'power_create/create.html', 'damage': 'power_create/damage.html', 'extras': 'power_create/extras.html', 'degree_mod': 'power_create/degree_mod.html', 'defense': 'power_create/defense.html', 'character': 'power_create/character.html', 'environment': 'power_create/environment.html', 'descriptors': 'power_create/descriptors.html', 'resist': 'power_create/resist.html', 'change_action': 'power_create/change_action.html', 'mod': 'power_create/mod.html', 'dc_table': 'power_create/dc_table.html', 'time': 'power_create/time.html', 'alt_check': 'power_create/alt_check.html', 'degree': 'power_create/degree.html', 'opposed': 'power_create/opposed.html', 'ranged': 'power_create/ranged.html', 'minion': 'power_create/minion.html', 'cost': 'power_create/cost.html', 'ranks': 'power_create/ranks.html'}
	
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

	power_type = PowerType.query.all()

	abilities = db.session.query(Ability).filter(Ability.hide == None).all()

	actions = db.session.query(Action).filter(Action.hide == None).all()

	advantages = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()
	
	auditory = db.session.query(SubSense).filter_by(sense_id=7)

	base_ranged = db.session.query(Ranged).filter(Ranged.hide == None).all()

	bonuses = db.session.query(SkillBonus).filter(SkillBonus.show == True).order_by(SkillBonus.name).all()

	checks = db.session.query(Check).filter(Check.hide == None).all()

	complexity = Complex.query.all()

	concealment = Conceal.query.all()

	conditions = db.session.query(Condition).filter(Condition.hide == None).order_by(Condition.name).all()

	conflicts = db.session.query(ConflictAction).filter(ConflictAction.hide == None).order_by(ConflictAction.name).all()

	consequences = db.session.query(Consequence).filter(Consequence.hide == None).order_by(Consequence.name).all()

	cover = Cover.query.all()

	damage = Damage.query.order_by(Damage.name).all()

	damages = db.session.query(Descriptor).filter(Descriptor.damage == True, Descriptor.show == True).order_by(Descriptor.name).all()

	defenses = db.session.query(Defense).filter(Defense.hide == None).all()

	descriptor_options = db.session.query(PowerDes).filter_by(hidden=True).all()

	descriptors = db.session.query(Descriptor).filter(Descriptor.show == True).order_by(Descriptor.name).all()

	distance = db.session.query(Unit).filter_by(type_id=3)

	distances = db.session.query(Unit).filter_by(type_id=3)

	duration_type = PowerDuration.query.all()

	emotions = db.session.query(Emotion).filter(Emotion.show == True).order_by(Emotion.name).all()
	
	energies = db.session.query(MediumSubType).filter(MediumSubType.medium_type == 2, MediumSubType.show == True).order_by(MediumSubType.name)

	environments = db.session.query(Environment).filter(Environment.show == True).order_by(Environment.name).all()

	equip_type = EquipType.query.all()

	grounds = Ground.query.all()

	level_types = LevelType.query.order_by(LevelType.name).all()

	light = Light.query.all()

	maths = Math.query.all()

	material = db.session.query(MediumSubType).filter(MediumSubType.medium_type == 1, MediumSubType.show == True).order_by(MediumSubType.name)

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	medium = db.session.query(Medium).filter(Medium.show == True).order_by(Medium.name).all()

	mediums = MediumType.query.order_by(MediumType.name).all()

	mental = db.session.query(SubSense).filter_by(sense_id=11)

	nature = db.session.query(Nature).filter(Nature.show == True).order_by(Nature.name).all()

	olfactory = db.session.query(SubSense).filter_by(sense_id=8)

	origins = db.session.query(Origin).filter(Origin.show == True).order_by(Origin.name).all()

	power_sense = db.session.query(Power).filter(Power.power_type == 3, Power.show == True).order_by(Power.name).all()

	powers = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()

	radio = db.session.query(SubSense).filter_by(sense_id=10)

	range_type = db.session.query(Ranged).filter_by(show=True).all()
	
	ranged = db.session.query(Ranged).filter_by(show=True)
	
	ranges = Range.query.all()

	senses = db.session.query(Sense).filter(Sense.hide == None).all()

	skills = db.session.query(Skill).filter(Skill.hide == None).order_by(Skill.name).all()

	sources = db.session.query(Source).filter(Source.show == True).order_by(Source.name).all()

	special = db.session.query(SubSense).filter_by(sense_id=12)

	subsenses = db.session.query(SubSense).filter(SubSense.hide == None).all()

	tactile = db.session.query(SubSense).filter_by(sense_id=9)

	times = db.session.query(Unit).filter_by(type_id=2)

	unit_type = MeasureType.query.all()

	units = Unit.query.all()

	visual = db.session.query(SubSense).filter_by(sense_id=6)


	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	against = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]

	attached = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}, {'type': 'with', 'name': 'With Skill Check'}, {'type': 'before_attack', 'name': 'Before Attack Check'}, {'type': 'after_attack', 'name': 'After Attack Check'}, {'type': 'opp_success', 'name': 'After Opponent Success'}, {'type': 'success', 'name': 'After Player Success'}, {'type': 'opp_fail', 'name': 'After Opponent Failure'}, {'type': 'fail', 'name': 'After Player Failure'}, {'type': 'before_var', 'name': 'Before Variable Check'}, {'type': 'after_var', 'name': 'After Variable Check'}]

	all_some = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	all_traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_power', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'advantage', 'name': 'Advantage'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	aquatic = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}, {'type': 'bpth', 'name': 'Both'}]

	bonus_type = [{'type': 'flat', 'name': 'Flat'}, {'type': 'rank', 'name': 'Per Rank'}]

	circ_effect = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'trait', 'name': 'Applied to other Check'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}, {'type': 'tools', 'name': 'If Tools'}, {'type': 'materials', 'name': 'If Materials'}, {'type': 'env', 'name': 'If Environment'}, {'type': 'nature', 'name': 'If Nature'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'descriptor', 'name': 'From Descriptor'}, {'type': 'condition', 'name': 'From Condition'}]

	circ_targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]

	circ_trait = [{'type': '', 'name': 'Applied to'}, {'type': 'all', 'name': 'All Checks'}, {'type': 'object', 'name': 'This Object'}, {'type': 'character', 'name': 'This Character'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}]
	
	circumstances = [{'type': '', 'name': 'N/A'}, {'type': 'gm', 'name': 'Set by GM'}, {'type': 'table', 'name': 'Circumstance Table'}]

	character = [{'type': 'size', 'name': 'Size Rank'}]

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'change', 'name': 'Condition Change'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}, {'type': 'variable', 'name': 'Variable Check'}, {'type': 'opposed', 'name': 'Opponent Check'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}, {'type': 'success', 'name': 'After Success'}, {'type': 'fail', 'name': 'After Failure'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}]

	check_types = [{'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}]

	conceal_type = [{'type': 'reduce', 'name': 'Reduce'}, {'type': 'eliminate', 'name': 'Eliminate'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Power Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'routine', 'name': 'Routine Check'}, {'type': 'none', 'name': 'No DC'}, {'type': 'choice', 'name': 'Chosen by Player'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	damage_value = [{'type': '', 'name': 'Damage Dealt'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'check', 'name': 'Checked Rank'}, {'type': 'value', 'name': 'Flat Value'}]

	damage_trait = [{'type': '', 'name': 'Rank'}, {'type': 'this_power', 'name': 'This Power'}, {'type': 'this_extra', 'name': 'This Extra'},  {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	darkness = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'check', 'name': 'Check'}, {'type': 'object', 'name': 'Object Destroyed'}, {'type': 'dc', 'name': 'Attach DC to Object'}, {'type': 'descriptor', 'name': 'Descriptor'}]

	degree_type = [{'type': '', 'name': 'Degree Type'}, {'type': '>', 'name': '>'}, {'type': '<', 'name': '<'}, {'type': '>=', 'name': '>='}, {'type': '<=', 'name': '<='} ]

	descriptor_type = [{'type': '', 'name': 'Applies To:'}, {'type': 'power', 'name': 'This Power'}, {'type': 'effect', 'name': 'Power Effect'}]

	descriptor_effect = [{'type': '', 'name': 'Effect'}, {'type': 'apply', 'name': 'Applies'}, {'type': 'remove', 'name': 'Removes'}, {'type': 'if', 'name': 'If'}]

	determined = [{'type': '', 'name': 'Determined By'}, {'type': 'dc', 'name': 'DC'}, {'type': 'target', 'name': 'Target Trait'}, {'type': 'player', 'name': 'Player Trait'}]

	dimensions = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]

	directions = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]

	direction = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]

	move_distance = [{'type': '', 'name': 'Distance Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'unit_math', 'name': 'Unit Math'}, {'type': 'rank_math', 'name': 'Rank Math'}]

	effect_target = [{'type': '', 'name': 'Effect Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'object', 'name': 'Object'}]

	effects = [{'type': 'condition', 'name': 'Condition'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'nullify', 'name': 'Nullifies Opponent Effect'}, {'type': 'trait', 'name': 'Weakened Trait'}, {'type': 'level', 'name': 'Level'}]

	environment = [{'type': '', 'name': 'Environment Type'}, {'type': 'underwater', 'name': 'Underwater'}, {'type': 'gravity', 'name': 'Zero Gravity'}, {'type': 'mountains', 'name': 'Mountains'}, {'type': 'jungle', 'name': 'Jungle'}, {'type': 'desert', 'name': 'Desert'}, {'type': 'volcano', 'name': 'Volcano'}, {'type': 'other', 'name': 'Other'}]

	environment_immunity = [{'type': '', 'name': 'Immune From'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'condition', 'name': 'Condition'}]

	equipment_use = [{'type': '', 'name': 'Use Type'}, {'type': 'use', 'name': 'With Use of'}, {'type': 'resist', 'name': 'Resist'}]

	extremity = [{'type': '', 'name': 'Extremity'}, {'type': 'intense', 'name': 'Intense'}, {'type': 'extreme', 'name': 'Extreme'}]

	frequency = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}, {'type': 'player', 'name': 'Player Choice'}]

	game_rule = [{'type': '', 'name': 'Game Rule'}, {'type': 'critical', 'name': 'Critical Hits'}, {'type': 'suffocate', 'name': 'Suffocation'}, {'type': 'starve', 'name': 'Starvation'}, {'type': 'thirst', 'name': 'Thirst'}, {'type': 'sleep', 'name': 'Need for Sleep'}, {'type': 'fall', 'name': 'Falling'}]

	heightened = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	immunity_type = [{'type': '', 'name': 'Immune From'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'damage', 'name': 'Damage Type'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'rule', 'name': 'Game Rule'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	insub = [{'type': '', 'name': 'Insubstantial Type'}, {'type': 'fluid', 'name': 'Fluid'}, {'type': 'gas', 'name': 'Gaseous'}, {'type': 'energy', 'name': 'Energy'}, {'type': 'incorp', 'name': 'Incorporeal'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	limited = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]

	limited_type = [{'type': '', 'name': 'Limited Against'}, {'type': 'task_type', 'name': 'Task Type'}, {'type': 'task', 'name': 'All tasks but One'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'subjects', 'name': 'Subjects'}, {'type': 'language', 'name': 'Different Language'}, {'type': 'extra', 'name': 'Extra Effect'}, {'type': 'degree', 'name': 'Degree of Success'}, {'type': 'sense', 'name': 'Sense'},  {'type': 'range', 'name': 'Range'}, {'type': 'source', 'name': 'Requires Descriptor'}, {'type': 'other', 'name': 'Other'}, {'type': 'level', 'name': 'Level'}]
	
	materials = [{'type': '', 'name': 'Materials'}, {'type': 'with', 'name': 'With Materials'}, {'type': 'improper', 'name': 'Improper Materials'}, {'type': 'none', 'name': 'No Materials'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill_rank', 'name': 'Skill Rank Modifier'}, {'type': 'skill_unit', 'name': 'Skill Unit Modifier'}]

	measure_effect_circ = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}]
		
	measure_type = [{'type': '', 'name': 'Type'}, {'type': '=', 'name': '='}, {'type': '>', 'name': '>'}, {'type': '<', 'name': '<'}, {'type': '>=', 'name': '>='}, {'type': '<=', 'name': '<='} ]

	minion_attitude = [{'type': '', 'name': 'Minion Attitude'}, {'type': 'none', 'name': 'Cooperative'}, {'type': 'Indifferent', 'name': 'Indifferent'}, {'type': 'Unfriendly', 'name': 'Unfriendly'}]

	minion_type = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]

	move_objects = [{'type': '', 'name': 'Direction'}, {'type': 'all', 'name': 'All Directions'}, {'type': 'vertical', 'name': 'Up and Down'}, {'type': 'horizontal', 'name': 'Towards and Away'}, {'type': 'attract', 'name': 'Attraction'}, {'type': 'repel', 'name': 'Repulsion'}]

	moveable = [{'type': '', 'name': 'Moveable With'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'check', 'name': 'Check'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'success', 'name': 'Successive'}, {'type': 'optional', 'name': 'Successive Optional'}]

	multiple_time = [{'type': '', 'name': 'If Multiple'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'degree', 'name': 'Degree'}, {'type': 'dc', 'name': 'DC'}, {'type': 'gm', 'name': 'GM Choice'}]

	null_type = [{'type': '', 'name': 'Effect'}, {'type': 'null', 'name': 'Nullifies Effect'}, {'type': 'mod', 'name': 'Modifier to Check'}]

	nullify = [{'type': '', 'name': 'Nullify Type'}, {'type': 'dc', 'name': 'DC'}, {'type': 'mod', 'name': 'Modifier'}]

	object_damage = [{'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}]

	offers  = [{'type': '', 'name': 'Effect'}, {'type': 'required', 'name': 'Requires'}, {'type': 'provides', 'name': 'Provides'}]

	openings = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]

	outcome = [{'type': '', 'name': ''}, {'type': '<', 'name': 'Lower'}, {'type': '>', 'name': 'Higher'}]
	
	partners = [{'type': '', 'name': 'N/A'}, {'type': 'power', 'name': 'Same Power'}, {'type': 'device', 'name': 'Device'}, {'type': 'both', 'name': 'Power or Device'}, {'type': 'skill', 'name': 'Skill Check'}]

	permanence = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]

	possess = [{'type': '', 'name': 'Possession'}, {'type': 'possess', 'name': 'While Possessing'}, {'type': 'oppose', 'name': 'While Opposing'}]

	ranged_type = [{'type': '', 'name': 'Ranged Type'}, {'type': 'flat_units', 'name': 'Flat Units'}, {'type': 'distance_rank', 'name': 'Flat Distance Rank'}, {'type': 'flat_rank_units', 'name': 'Flat Units By Rank'}, {'type': 'flat_rank_distance', 'name': 'Flat Distance Rank By Rank'}, {'type': 'units_rank', 'name': 'Units Per Rank'}, {'type': 'rank_rank', 'name': 'Distance Rank Per Rank'}, {'type': 'effect_mod', 'name': 'Effect Rank Modifier'}, {'type': 'trait_mod', 'name': 'Trait Rank Modifier'}, {'type': 'distance_mod', 'name': 'Distance Rank Modifier'}, {'type': 'check', 'name': 'Check Result'}]

	recovery = [{'type': '', 'name': 'Target'}, {'type': 'player', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'either', 'name': 'Either'}]

	repair = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]

	required_tools = [{'type': '', 'name': 'Tools'}, {'type': 'correct', 'name': 'Correct Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'gm', 'name': 'GM Decides'}]

	resistance_type = [{'type': '', 'name': 'Applies to'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'trait', 'name': 'Check Type'}, {'type': 'harmed', 'name': 'Subject Harmed'}]

	resistant = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	result = [{'type': '', 'name': 'Result'}, {'type': 'high', 'name': 'Higher'}, {'type': 'low', 'name': 'Lower'}]

	required = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	sense_distance = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'unit', 'name': 'By Rank (Units)'}, {'type': 'rank', 'name': 'By Rank'}]

	sense_time = [{'type': '', 'name': ''}, {'type': 'value', 'name': 'Value'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	sense_type =  [{'type': '', 'name': 'Effect Type'}, {'type': 'height', 'name': 'Heightened'}, {'type': 'resist', 'name': 'Resistant'}]

	side_effects = [{'type': '', 'name': 'Side Effect'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'level', 'name': 'Level'}, {'type': 'other', 'name': 'Other'}]

	solidity = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]

	space = [{'type': '', 'name': 'Space Travel Type'}, {'type': 'solar', 'name': 'Planets in Solar System'}, {'type': 'star', 'name': 'Other Star Systems'}, {'type': 'galaxy', 'name': 'Other Galaxies'}]

	specificity = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]

	speed = [{'type': '', 'name': 'Speed Type'}, {'type': 'rank', 'name': 'Speed Rank'}, {'type': 'rank_mod', 'name': 'Speed Modifier'}, {'type': 'mod', 'name': 'Math'}]

	spend = [{'type': '', 'name': 'Effect'}, {'type': 'reroll', 'name': 'Re-roll'}]

	target_type = [{'type': '', 'name': 'Target Type'}, {'type': 'language', 'name': 'Any Language'}, {'type': 'animal', 'name': 'Animal'}, {'type': 'machine', 'name': 'Machine'}, {'type': 'object', 'name': 'Objects'}, {'type': 'plant', 'name': 'Plants'}, {'type': 'spirit', 'name': 'Spirits'}, {'type': 'x', 'name': 'Variable'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'opp', 'name': 'Opponent'}]

	targets_object = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'object', 'name': 'Object'}]

	task_type = [{'type': '', 'name': 'Does Not Work On'}, {'type': 'physical', 'name': 'Physical Tasks'}, {'type': 'mental', 'name': 'Mental Tasks'}]

	teleport = [{'type': '', 'name': 'Type'}, {'type': 'know', 'name': 'Know Destination'}, {'type': 'any', 'name': 'Any Destination'}]

	teleport_change = [{'type': '', 'name': 'Can Change'}, {'type': 'direction', 'name': 'Direction'}, {'type': 'velocity', 'name': 'Velocity'}]

	temp_type = [{'type': '', 'name': 'Type'}, {'type': 'all', 'name': 'All'}, {'type': 'cold', 'name': 'Cold'}, {'type': 'heat', 'name': 'Heat'}, {'type': 'pressure', 'name': 'High Pressure'}, {'type': 'radiation', 'name': 'Radiation'}, {'type': 'vaccum', 'name': 'Vaccuum'}]

	time_effect = [{'type': '', 'name': 'Time Effect'}, {'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time Limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}, {'type': 'effect', 'name': 'Time Effect Happens'}, {'type': 'repeat', 'name': 'Time Until Repeat Check'}, {'type': 'recover', 'name': 'Recovery Time'}]
		
	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Rank Marh'}, {'type': 'time', 'name': 'Time Rank'}, {'type': 'mod', 'name': 'Time Rank Modifier'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'gm', 'name': 'Set by GM'}, {'type': 'player', 'name': 'Set by Player'}]

	time_travel = [{'type': '', 'name': 'Time Travel Type'}, {'type': 'Fixed', 'name': 'Fixed Point in Time'}, {'type': 'past', 'name': 'Any Point in Past'}, {'type': 'future', 'name': 'Any Point in Future'}, {'type': 'timeline', 'name': 'Alternate Timeline'}, {'type': 'any', 'name': 'Any Point in time'}  ]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	traits = [{'type': '', 'name': 'Rank'}, {'type': 'this_power', 'name': 'This Power'}, {'type': 'this_extra', 'name': 'This Extra'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Base Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'distance', 'name': 'Distance Rank'}, {'type': 'active', 'name': 'Active Opponent Rank'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'interact', 'name': 'Any Interarction'}, {'type': 'manipulate',  'name': 'Any Manipulation'}]

	transform = [{'type': '', 'name': 'Transform Type'}, {'type': 'one', 'name': 'One Substance to One Substance'}, {'type': 'result', 'name': 'Group to Single Result'}, {'type': 'broad', 'name': 'Broad Group to Broad Group'}, {'type': 'any', 'name': 'Any Material into Anything Else'}]

	travel = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	use_type = [{'type': '', 'name': 'Use Type'}, {'type': 'add', 'name': 'Add to'}, {'type': 'replace', 'name': 'In Place of'}, {'type': 'gm', 'name': 'GM Choice'}]

	value_bonus = [{'type': 'value', 'name': 'Value'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]
	
	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	visibility = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]

	weaken = [{'type': '', 'name': 'Weaken Type'}, {'type': 'trait', 'name': 'Specific'}, {'type': 'type', 'name': 'Broad Trait'}, {'type': 'descriptor', 'name': 'Broad Descriptor'}]

	whens = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]

	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]

	power_circ = linked_options(PowerCirc, Power, 'power_id', 'keyword')

	power_dc = linked_options(PowerDC, Power, 'power_id', 'keyword')
	
	power_degree = linked_options(PowerDegree, Power, 'power_id', 'keyword')
	
	power_opposed = linked_options(PowerOpposed, Power, 'power_id', 'keyword')
	
	power_time = linked_options(PowerTime, Power, 'power_id', 'keyword')

	power_move = linked_options(PowerMove, Power, 'power_id', 'keyword')
	
	power_check = linked_options(PowerCheck, Power, 'power_id', 'keyword')

	power_circ_type = linked_options(PowerCircType, Power, 'power_id', 'name')

	power_dc_type = linked_options(PowerDCType, Power, 'power_id', 'name')
	
	power_degree_type = linked_options(PowerDegreeType, Power, 'power_id', 'name')
	
	power_time_type = linked_options(PowerTimeType, Power, 'power_id', 'name')

	power_move_type = linked_options(PowerMoveType, Power, 'power_id', 'name')
	
	power_ranged = linked_options(PowerRanged, Power, 'power_id', 'name')
	
	power_ranged_type = linked_options(PowerRangedType, Power, 'power_id', 'name')
	
	power_damage = linked_options(PowerDamage, Power, 'power_id', 'name')






	return render_template('template.html', sense_time=sense_time, all_some=all_some, power_sense=power_sense, bonuses=bonuses, sense_type=sense_type, visual=visual, auditory=auditory, olfactory=olfactory, 
											tactile=tactile, radio=radio, mental=mental, special=special, value_bonus=value_bonus, heightened=heightened, resistant=resistant, required=required, circumstances=circumstances, 
											senses=senses, subsenses=subsenses, actions=actions, permanence=permanence, time_numbers=time_numbers, maths=maths, times=times, targets=targets, whens=whens, dc_value=dc_value, 
											effects=effects, conditions=conditions, check_types=check_types, powers=powers, skills=skills, abilities=abilities, defenses=defenses, checks=checks, dc_type=dc_type, 
											distance=distance, negatives=negatives, positives=positives, power_type=power_type, action_type=action_type, range_type=range_type, duration_type=duration_type, 
											power_includes=power_includes, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar, includehtml=includehtml, title=title, 
											sense_distance=sense_distance, against=against, traits=traits, object_damage=object_damage, darkness=darkness, solidity=solidity, partners=partners, visibility=visibility,
											moveable=moveable, complexity=complexity, determined=determined, deg_mod_type=deg_mod_type, value_type=value_type, die=die, use_type=use_type, outcome=outcome,
											circ_type=circ_type, ranges=ranges, limited=limited, emotions=emotions, temp_type=temp_type, extremity=extremity, nature=nature, grounds=grounds, directions=directions,
											character=character, updown=updown, condition_type=condition_type, descriptors=descriptors, origins=origins, sources=sources, mediums=mediums, medium=medium, 
											material=material, energies=energies, descriptor_type=descriptor_type, resistance_type=resistance_type, bonus_type=bonus_type, time_effect=time_effect, 
											limited_type=limited_type, possess=possess, hundred=hundred, game_rule=game_rule, damage=damage, insub=insub, openings=openings, spend=spend, result=result, 
											all_traits=all_traits, side_effects=side_effects, check_type=check_type, null_type=null_type, damages=damages, conflicts=conflicts, move_objects=move_objects,
											dimensions=dimensions, environment=environment, environment_immunity=environment_immunity, immunity_type=immunity_type, circ_null=circ_null, space=space,
											travel=travel, time_travel=time_travel, aquatic=aquatic, task_type=task_type, distances=distances, ranged_type=ranged_type, who_check=who_check, cover=cover,
											minion_type=minion_type, minion_attitude=minion_attitude, teleport=teleport, teleport_change=teleport_change, transform=transform, weaken=weaken, measure_rank=measure_rank, 
											conceal_type=conceal_type, level_types=level_types, environments=environments, light=light, descriptor_options=descriptor_options, 
											check_trigger=check_trigger, ranged=ranged, circ_effect=circ_effect, circ_trait=circ_trait, tools=tools, materials=materials, circ_targets=circ_targets, 
											measure_effect_circ=measure_effect_circ, measure_type=measure_type, unit_type=unit_type, effect_target=effect_target, measure_effect=measure_effect, units=units,
											damage_type=damage_type, inflict=inflict, offers=offers, required_tools=required_tools, equipment_use=equipment_use, equip_type=equip_type, concealment=concealment,
											repair=repair, degree_type=degree_type, nullify=nullify, speed=speed, move_distance=move_distance, attached=attached, frequency=frequency, multiple_opposed=multiple_opposed,
											multiple_time=multiple_time, time_value=time_value, recovery=recovery, power_circ=power_circ, power_circ_type=power_circ_type, power_dc=power_dc, power_dc_type=power_dc_type, 
											power_degree=power_degree, power_degree_type=power_degree_type, power_move=power_move, power_move_type=power_move_type, power_opposed=power_opposed, power_check=power_check,
											power_time=power_time, power_time_type=power_time_type, power_ranged=power_ranged, power_damage=power_damage, power_ranged_type=power_ranged_type, direction=direction,
											targets_object=targets_object, descriptor_effect=descriptor_effect)

@powers.route('/power/create', methods=['POST'])
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

@powers.route('/power/save', methods=['POST'])
def save_power(): 
	body = {}
	body['success'] = True
	error = False
	error_msgs = []

	data = request.get_json()
	
	errors = power_save_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	description = request.get_json()['description']
	power_type = request.get_json()['power_type']
	action = request.get_json()['action']
	power_range = request.get_json()['power_range']
	duration = request.get_json()['duration']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']
	flat = request.get_json()['flat']
	limit = request.get_json()['limit']
	dc_type = request.get_json()['dc_type']
	dc_value = request.get_json()['dc_value']
	dc_mod = request.get_json()['dc_mod']
	opponent_dc = request.get_json()['opponent_dc']
	check_type = request.get_json()['check_type']
	routine = request.get_json()['routine']
	routine_trait_type = request.get_json()['routine_trait_type']
	routine_trait = request.get_json()['routine_trait']
	materials = request.get_json()['materials']
	partner = request.get_json()['partner']
	partner_trait_type = request.get_json()['partner_trait_type']
	partner_dc = request.get_json()['partner_dc']
	partner_trait = request.get_json()['partner_trait']
	target = request.get_json['target']
	target_type = request.get_json['target_type']
	circ = request.get_json()['circ']
	circ_required = request.get_json()['circ_required']
	skill = request.get_json()['skill']
	skill_required = request.get_json()['skill_required']
	skill_when = request.get_json()['skill_when']
	conflict = request.get_json()['conflict']
	conflict_bonus = request.get_json()['conflict_bonus']
	conflict_type = request.get_json()['conflict_type']
	condition = request.get_json()['condition']
	alt_check = request.get_json()['alt_check']
	change_action = request.get_json()['change_action']
	character = request.get_json()['character']
	circumstance = request.get_json()['circumstance']
	create = request.get_json()['create']
	damage = request.get_json()['damage']
	dc = request.get_json()['dc']
	defense = request.get_json()['defense']
	degree = request.get_json()['degree']
	environment = request.get_json()['environment']
	levels = request.get_json()['levels']
	minion = request.get_json()['minion']
	modifier = request.get_json()['modifier']
	move = request.get_json()['move']
	opposed = request.get_json()['opposed']
	ranged = request.get_json()['ranged']
	resistance = request.get_json()['resistance']
	resist_by = request.get_json()['resist_by']
	reverse = request.get_json()['reverse']
	sense = request.get_json()['sense']
	time = request.get_json()['time']

	power_type = integer(power_type)
	action = db_integer(Action, action)
	power_range = db_integer(Ranged, power_range)
	duration = integer(duration)
	check_type = db_integer(Check, check_type)
	skill = db_integer(Skill, skill)
	conflict = db_integer(ConflictAction, conflict)
	condition = db_integer(Condition, condition)
	power = db.session.query(Power).filter(Power.id == power_id).one()

	cost = var_convert(cost)
	limit = integer(limit)
	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	opponent_dc = integer(opponent_dc)
	routine_trait = integer(routine_trait)
	partner_trait = integer(partner_trait)
	partner_dc = integer(partner_dc)
	conflict_bonus = integer(conflict_bonus)
	ranks = var_convert(ranks)

	power.description = description
	power.power_type = power_type
	power.action = action
	power.power_range = power_range
	power.duration = duration
	power.cost = cost
	power.ranks = ranks
	power.flat = flat
	power.limit = limit
	power.dc_type = dc_type
	power.dc_value = dc_value
	power.dc_mod = dc_mod
	power.opponent_dc = opponent_dc
	power.check_type = check_type
	power.routine = routine
	power.routine_trait_type = routine_trait_type
	power.routine_trait = routine_trait
	power.materials = materials
	power.partner = partner
	power.partner_trait_type = partner_trait_type
	power.partner_dc = partner_dc
	power.partner_trait = partner_trait
	power.tsrget = target
	power.target_type = target_type
	power.circ = circ
	power.circ_required = circ_required
	power.skill = skill
	power.skill_required = skill_required
	power.skill_when = skill_when
	power.conflict = conflict
	power.conflict_bonus = conflict_bonus
	power.conflict_type = conflict_type
	power.condition = condition
	power.alt_check = alt_check	
	power.change_action = change_action
	power.character = character	
	power.circumstance = circumstance
	power.create = create
	power.damage = damage
	power.dc = dc
	power.defense = defense
	power.degree = degree
	power.environment = environment
	power.levels = levels
	power.minion = minion
	power.modifier = modifier
	power.move = move
	power.opposed = opposed
	power.ranged = ranged
	power.resistance = resistance
	power.resist_by = resist_by
	power.reverse = reverse
	power.sense = sense
	power.time = time

	db.session.commit()
	body['success'] = True
			
	db.session.close()
	print(body)
	return jsonify(body)

@powers.route('/power/save/success/<power_id>')
def power_save_success(power_id):	
	power = db.session.query(Power).filter_by(id=power_id).one()
	
	flash('Power ' + power.name + ' Successfully Created')
	return redirect(url_for('home'))

@powers.route('/power/edit_name', methods=['POST'])
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
		edit_power = db.session.query(Power).filter(Power.id == power_id).one()
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

@powers.route('/power/extras/create', methods=['POST'])
def power_post_extra():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = power_extra_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	name = request.get_json()['name']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']
	des = request.get_json()['des']
	inherit = request.get_json()['inherit']
	alternate = request.get_json()['alternate']
	flat = request.get_json()['flat']

	power_id = integer(power_id)
	inherit = db_integer(Power, inherit)

	cost = integer(cost)
	ranks = integer(ranks)

	try:
		entry = Extra(power_id = power_id,
						name = name,
						cost = cost,
						ranks = ranks,
						des = des,
						inherit = inherit,
						alternate = alternate,
						flat = flat
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
		table_id = 'extras'
		spot = "extras-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = power_extra_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	
	return jsonify(body)

@powers.route('/power/extras/delete/<power_id>', methods=['DELETE'])
def delete_power_extra(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(Extra).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)


@powers.route('/power/powerdes/delete/<power_id>', methods=['DELETE'])
def delete_powerdes(power_id):
	try:
		db.session.query(PowerDes).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': power_id})


@powers.route('/power/grid', methods=['POST'])
def power_grid():

	data = request.get_json()


	rows = request.get_json()['rows']
	font = request.get_json()['font']

	result = grid_columns(rows, font)

	columns = result['columns']
	grid = result['grid']
	font = result['font']

	body = {'success': True, 'grid': grid, 'font': font, 'columns': columns}

	return jsonify(body)




@powers.route('/power/cost/create', methods=['POST'])
def power_post_cost():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = power_cost_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	keyword = request.get_json()['keyword']
	cost = request.get_json()['cost']
	rank = request.get_json()['rank']
	flat = request.get_json()['flat']
	extra = request.get_json()['extra']

	power_id = integer(power_id)
	cost = integer(cost)
	rank = integer(rank)

	extra = db_integer(Extra, extra)

	try:
		entry = PowerCost(power_id = power_id,
							keyword = keyword,
							cost = cost,
							rank = rank,
							flat = flat,
							extra = extra)

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
		table_id = 'cost'
		spot = "cost-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = power_cost_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	
	return jsonify(body)

@powers.route('/power/cost/delete/<power_id>', methods=['DELETE'])
def delete_power_cost(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerCost).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/ranks/create', methods=['POST'])
def power_post_ranks():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = power_ranks_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	keyword = request.get_json()['keyword']
	cost = request.get_json()['cost']
	rank = request.get_json()['rank']
	flat = request.get_json()['flat']
	extra = request.get_json()['extra']
	base_cost = request.get_json()['base_cost']
	base_ranks = request.get_json()['base_ranks']

	power_id = integer(power_id)
	cost = db_integer(PowerCost, cost)
	ranks = integer(ranks)

	extra = db_integer(Extra, extra)

	try:
		entry = PowerCost(power_id = power_id,
							cost = cost,
							ranks = ranks,
							extra = extra)

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
		table_id = 'ranks'
		spot = "ranks-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = power_ranks_post(entry, body, cells, base_cost, base_ranks)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	
	return jsonify(body)

@powers.route('/power/ranks/delete/<power_id>', methods=['DELETE'])
def delete_power_ranks(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerRanks).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)


@powers.route('/power/change_action/create', methods=['POST'])
def power_post_change_action():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = change_action_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	action = request.get_json()['action']
	mod = request.get_json()['mod']
	objects = request.get_json()['objects']
	circumstance = request.get_json()['circumstance']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	action = db_integer(Action, action)

	mod = integer(mod)

	try:
		entry = PowerAction(power_id = power_id,
							extra_id = extra_id,
							action = action,
							mod = mod,
							objects =objects, 
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
		table_id = 'action'
		spot = "action-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = change_action_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	
	return jsonify(body)

@powers.route('/power/action/delete/<power_id>', methods=['DELETE'])
def delete_power_action(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerAction).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/character/create', methods=['POST'])
def power_post_character():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = character_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	value = request.get_json()['value']
	increase = request.get_json()['increase']
	limited = request.get_json()['limited']
	reduced = request.get_json()['reduced']
	limbs = request.get_json()['limbs']
	carry = request.get_json()['carry']
	sustained = request.get_json()['sustained']
	permanent = request.get_json()['permanent']
	points = request.get_json()['points']
	appear = request.get_json()['appear']
	insubstantial = request.get_json()['insubstantial']
	weaken = request.get_json()['weaken']
	weaken_type = request.get_json()['weaken_type']
	weaken_trait_type = request.get_json()['weaken_trait_type']
	weaken_trait = request.get_json()['weaken_trait']
	weaken_broad = request.get_json()['weaken_broad']
	weaken_descriptor = request.get_json()['weaken_descriptor']
	weaken_simultaneous = request.get_json()['weaken_simultaneous']
	limited_by = request.get_json()['limited_by']
	limited_other = request.get_json()['limited_other']
	limited_emotion = request.get_json()['limited_emotion']
	limited_emotion_other = request.get_json()['limited_emotion_other']
	reduced_trait_type = request.get_json()['reduced_trait_type']
	reduced_trait = request.get_json()['reduced_trait']
	reduced_value = request.get_json()['reduced_value']
	reduced_full = request.get_json()['reduced_full']
	limbs_continuous = request.get_json()['limbs_continuous']
	limbs_sustained = request.get_json()['limbs_sustained']
	limbs_distracting = request.get_json()['limbs_distracting']
	limbs_projection = request.get_json()['limbs_projection']
	carry_capacity = request.get_json()['carry_capacity']
	points_value = request.get_json()['points_value']
	points_trait_type = request.get_json()['points_trait_type']
	points_trait = request.get_json()['points_trait']
	points_descriptor = request.get_json()['points_descriptor']
	appear_target = request.get_json()['appear_target']
	appear_description = request.get_json()['appear_description']
	insub_type = request.get_json()['insub_type']
	insub_description = request.get_json()['insub_description']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)


	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	limited_emotion = db_integer(Emotion, limited_emotion)

	trait = integer(trait)
	value = integer(value)
	increase = integer(increase)
	weaken_trait = integer(weaken_trait)
	weaken_descriptor = integer(weaken_descriptor)
	reduced_trait = integer(reduced_trait)
	reduced_value = integer(reduced_value)
	carry_capacity = integer(carry_capacity)
	points_value = integer(points_value)
	points_trait = integer(points_trait)
	points_descriptor = integer(points_descriptor)

	try:
		body = {}
	
		body['new'] = False
		new_items = []

		if limited_emotion == 'other':	
			entry = Emotion(name=limited_emotion_other)
			db.session.add(entry)
			db.session.commit()
			limited_emotion = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = True
			item['field'] = 'emotion-sml'
			body['new_items'] = new_items
			new_items.append(item)
			db.session.close()


		entry = PowerChar(power_id = power_id,
							extra_id = extra_id,
							trait_type = trait_type,
							trait = trait,
							value = value,
							increase = increase,
							limited = limited,
							reduced = reduced,
							limbs = limbs,
							carry = carry,
							sustained = sustained,
							permanent = permanent,
							points = points,
							appear = appear,
							insubstantial = insubstantial,
							weaken = weaken,
							weaken_type = weaken_type,
							weaken_trait_type = weaken_trait_type,
							weaken_trait = weaken_trait,
							weaken_broad = weaken_broad,
							weaken_descriptor = weaken_descriptor,
							weaken_simultaneous = weaken_simultaneous,
							limited_by = limited_by,
							limited_other = limited_other,
							limited_emotion = limited_emotion,
							limited_emotion_other = limited_emotion_other,
							reduced_trait_type = reduced_trait_type,
							reduced_trait = reduced_trait,
							reduced_value = reduced_value,
							reduced_full = reduced_full,
							limbs_continuous = limbs_continuous,
							limbs_sustained = limbs_sustained,
							limbs_distracting = limbs_distracting,
							limbs_projection = limbs_projection,
							carry_capacity = carry_capacity,
							points_value = points_value,
							points_trait_type = points_trait_type,
							points_trait = points_trait,
							points_descriptor = points_descriptor,
							appear_target = appear_target,
							appear_description = appear_description,
							insub_type = insub_type,
							insub_description = insub_description,
							cost = cost,
							ranks = ranks)

		db.session.add(entry)
		db.session.commit()

		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'char'
		spot = "char-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = character_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/char/delete/<power_id>', methods=['DELETE'])
def delete_power_char(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerChar).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/create/create', methods=['POST'])
def power_post_create():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = create_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	solidity = request.get_json()['solidity']
	visibility = request.get_json()['visibility']
	complexity = request.get_json()['complexity']
	volume = request.get_json()['volume']
	toughness = request.get_json()['toughness']
	mass = request.get_json()['mass']
	damageable = request.get_json()['damageable']
	maintained = request.get_json()['maintained']
	repairable = request.get_json()['repairable']
	moveable = request.get_json()['moveable']
	stationary = request.get_json()['stationary']
	trap = request.get_json()['trap']
	ranged = request.get_json()['ranged']
	weapon = request.get_json()['weapon']
	support = request.get_json()['support']
	real = request.get_json()['real']
	cover = request.get_json()['cover']
	conceal = request.get_json()['conceal']
	incoming = request.get_json()['incoming']
	outgoing = request.get_json()['outgoing']
	transform = request.get_json()['transform']
	transform_type = request.get_json()['transform_type']
	transform_start_mass = request.get_json()['transform_start_mass']
	transfom_mass = request.get_json()['transfom_mass']
	transform_start_descriptor = request.get_json()['transform_start_descriptor']
	transform_end_descriptor = request.get_json()['transform_end_descriptor']
	move_player = request.get_json()['move_player']
	move_check = request.get_json()['move_check']
	move_opposed = request.get_json()['move_opposed']
	move_opponent_check = request.get_json()['move_opponent_check']
	trap_check = request.get_json()['trap_check']
	trap_resist = request.get_json()['trap_resist']
	trap_opposed = request.get_json()['trap_opposed']
	trap_escape = request.get_json()['trap_escape']
	ranged_type = request.get_json()['ranged_type']
	ranged_dc = request.get_json()['ranged_dc']
	ranged_trait_type = request.get_json()['ranged_trait_type']
	ranged_trait = request.get_json()['ranged_trait']
	ranged_damage_type = request.get_json()['ranged_damage_type']
	ranged_damage_value = request.get_json()['ranged_damage_value']
	weapon_trait_type = request.get_json()['weapon_trait_type']
	weapon_trait = request.get_json()['weapon_trait']
	weapon_mod = request.get_json()['weapon_mod']
	weapon_damage_type = request.get_json()['weapon_damage_type']
	weapon_damage = request.get_json()['weapon_damage']
	support_strength = request.get_json()['support_strength']
	support_strengthen = request.get_json()['support_strengthen']
	support_action = request.get_json()['support_action']
	support_action_rounds = request.get_json()['support_action_rounds']
	support_effort = request.get_json()['support_effort']
	support_effort_rounds = request.get_json()['support_effort_rounds']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	complexity = db_integer(Complex, complexity)
	

	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)

	move_check = db_integer(PowerCheck, move_check)
	move_opposed = db_integer(PowerOpposed, move_opposed)
	trap_check = db_integer(PowerCheck, trap_check)
	trap_resist = db_integer(PowerCheck, trap_resist)
	trap_opposed = db_integer(PowerOpposed, trap_opposed)

	volume = integer(volume)
	toughness = integer(toughness)
	mass = integer(mass)
	transform_start_mass = integer(transform_start_mass)
	transfom_mass = integer(transfom_mass)
	transform_start_descriptor = integer(transform_start_descriptor)
	transform_end_descriptor = integer(transform_end_descriptor)
	ranged_dc = integer(ranged_dc)
	ranged_trait = integer(ranged_trait)
	ranged_damage_value = integer(ranged_damage_value)
	weapon_trait = integer(weapon_trait)
	weapon_mod = integer(weapon_mod)
	weapon_damage = integer(weapon_damage)
	support_strength = integer(support_strength)
	support_action = integer(support_action)
	support_action_rounds = integer(support_action_rounds)
	support_effort = integer(support_effort)
	support_effort_rounds = integer(support_effort_rounds)


	try:
		entry = PowerCreate(power_id = power_id,
							extra_id = extra_id,
							solidity = solidity,
							visibility = visibility,
							complexity = complexity,
							volume = volume,
							toughness = toughness,
							mass = mass,
							damageable = damageable,
							maintained = maintained,
							repairable = repairable,
							moveable = moveable,
							stationary = stationary,
							trap = trap,
							ranged = ranged,
							weapon = weapon,
							support = support,
							real = real,
							cover = cover,
							conceal = conceal,
							incoming = incoming,
							outgoing = outgoing,
							transform = transform,
							transform_type = transform_type,
							transform_start_mass = transform_start_mass,
							transfom_mass = transfom_mass,
							transform_start_descriptor = transform_start_descriptor,
							transform_end_descriptor = transform_end_descriptor,
							move_player = move_player,
							move_opponent_check = move_opponent_check,
							move_check = move_check,
							move_opposed = move_opposed,
							trap_check = trap_check,
							trap_resist = trap_resist,
							trap_opposed = trap_opposed,
							trap_escape = trap_escape,
							ranged_type = ranged_type,
							ranged_dc = ranged_dc,
							ranged_trait_type = ranged_trait_type,
							ranged_trait = ranged_trait,
							ranged_damage_type = ranged_damage_type,
							ranged_damage_value = ranged_damage_value,
							weapon_trait_type = weapon_trait_type,
							weapon_trait = weapon_trait,
							weapon_mod = weapon_mod,
							weapon_damage_type = weapon_damage_type,
							weapon_damage = weapon_damage,
							support_strength = support_strength,
							support_strengthen = support_strengthen,
							support_action = support_action,
							support_action_rounds = support_action_rounds,
							support_effort = support_effort,
							support_effort_rounds = support_effort_rounds,
							cost = cost,
							ranks = ranks)

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
		table_id = 'create'
		spot = "create-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = create_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/create/delete/<power_id>', methods=['DELETE'])
def delete_power_create(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerCreate).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/damage/create', methods=['POST'])
def power_post_damage():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = damage_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	strength = request.get_json()['strength']
	damage_type = request.get_json()['damage_type']
	descriptor = request.get_json()['descriptor']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	keyword = request.get_json()['keyword']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	damage_type = db_multiple(Descriptor, damage_type)
	descriptor = db_multiple(PowerDes, descriptor)

	trait = integer(trait)
	mod = integer(mod)

	try:
		entry = PowerDamage(power_id = power_id,
							extra_id = extra_id,
							trait_type = trait_type,
							trait = trait,
							mod = mod,
							strength = strength,
							damage_type = damage_type,
							descriptor = descriptor,
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
		table_id = 'damage'
		spot = "damage-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = damage_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/damage/delete/<power_id>', methods=['DELETE'])
def delete_power_damage(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerDamage).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/defense/create', methods=['POST'])
def power_post_defense():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = defense_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	defense = request.get_json()['defense']
	use = request.get_json()['use']
	mod = request.get_json()['mod']
	roll = request.get_json()['roll']
	outcome = request.get_json()['outcome']
	dodge = request.get_json()['dodge']
	fortitude = request.get_json()['fortitude']
	parry = request.get_json()['parry']
	toughness = request.get_json()['toughness']
	will = request.get_json()['will']
	resist_area = request.get_json()['resist_area']
	resist_perception = request.get_json()['resist_perception']
	reflect = request.get_json()['reflect']
	immunity = request.get_json()['immunity']
	reflect_action = request.get_json()['reflect_action']
	reflect_check = request.get_json()['reflect_check']
	reflect_dc = request.get_json()['reflect_dc']
	reflect_opposed_trait_type = request.get_json()['reflect_opposed_trait_type']
	reflect_opposed_trait = request.get_json()['reflect_opposed_trait']
	reflect_resist_trait_type = request.get_json()['reflect_resist_trait_type']
	reflect_resist_trait = request.get_json()['reflect_resist_trait']
	immunity_type = request.get_json()['immunity_type']
	immunity_trait_type = request.get_json()['immunity_trait_type']
	immunity_trait = request.get_json()['immunity_trait']
	immunity_descriptor = request.get_json()['immunity_descriptor']
	immunity_damage = request.get_json()['immunity_damage']
	immunity_rule = request.get_json()['immunity_rule']
	cover_check = request.get_json()['cover_check']
	cover_type = request.get_json()['cover_type']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	defense = db_integer(Defense, defense)
	reflect_action = db_integer(Action, reflect_action)
	reflect_check = db_integer(Check, reflect_check)
	immunity_damage = db_integer(Descriptor, immunity_damage)
	cover_type = db_integer(Cover, cover_type)

	mod = integer(mod)
	roll = integer(roll)
	reflect_dc = integer(reflect_dc)
	reflect_opposed_trait = integer(reflect_opposed_trait)
	reflect_resist_trait = integer(reflect_resist_trait)
	immunity_trait = integer(immunity_trait)
	immunity_descriptor = integer(immunity_descriptor)

	try:
		entry = PowerDefense(power_id = power_id,
								extra_id = extra_id,
								defense = defense,
								use = use,
								mod = mod,
								roll = roll,
								outcome = outcome,
								dodge = dodge,
								fortitude = fortitude,
								parry = parry,
								toughness = toughness,
								will = will,
								resist_area = resist_area,
								resist_perception = resist_perception,
								reflect = reflect,
								immunity = immunity,
								reflect_action = reflect_action,
								reflect_check = reflect_check,
								reflect_dc = reflect_dc,
								reflect_opposed_trait_type = reflect_opposed_trait_type, 
								reflect_opposed_trait = reflect_opposed_trait,
								reflect_resist_trait_type = reflect_resist_trait_type,
								reflect_resist_trait = reflect_resist_trait,
								immunity_type = immunity_type,
								immunity_trait_type = immunity_trait_type,
								immunity_trait =immunity_trait,
								immunity_descriptor = immunity_descriptor,
								immunity_damage = immunity_damage,
								immunity_rule = immunity_rule,
								cover_check = cover_check,
								cover_type = cover_type)
		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = 'x'
		if cells == 'x':
			cells = []
		table_id = 'defense'
		spot = "defense-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = defense_post(entry, body, cells)

	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/defense/delete/<power_id>', methods=['DELETE'])
def delete_power_defense(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerDefense).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/environment/create', methods=['POST'])
def power_post_environment():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = environment_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	radius = request.get_json()['radius']
	distance = request.get_json()['distance']
	rank = request.get_json()['rank']
	condition_check = request.get_json()['condition_check']
	impede = request.get_json()['impede']
	conceal = request.get_json()['conceal']
	visibility = request.get_json()['visibility']
	selective = request.get_json()['selective']
	immunity = request.get_json()['immunity']
	immunity_type = request.get_json()['immunity_type']
	temp_type = request.get_json()['temp_type']
	immunity_extremity = request.get_json()['immunity_extremity']
	immunity_environment = request.get_json()['immunity_environment']
	immunity_environment_other = request.get_json()['immunity_environment_other']
	no_penalty = request.get_json()['no_penalty']
	no_circumstance = request.get_json()['no_circumstance']
	condition_temp_type = request.get_json()['condition_temp_type']
	temp_extremity = request.get_json()['temp_extremity']
	move_nature = request.get_json()['move_nature']
	move_speed = request.get_json()['move_speed']
	move_cost_circ = request.get_json()['move_cost_circ']
	move_other = request.get_json()['move_other']
	conceal_type = request.get_json()['conceal_type']
	visibility_trait_type = request.get_json()['visibility_trait_type']
	visibility_trait = request.get_json()['visibility_trait']
	visibility_mod = request.get_json()['visibility_mod']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)


	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	immunity_environment = db_integer(Environment, immunity_environment)
	move_nature = db_integer(Nature, move_nature)

	radius = integer(radius)
	distance = integer(distance)
	rank = integer(rank)
	move_speed = integer(move_speed)
	visibility_trait = integer(visibility_trait)
	visibility_mod = integer(visibility_mod)


	try:
		body = {}
	
		body['new'] = False
		new_items = []

		if immunity_environment == 'other':	
			entry = Environment(name=immunity_environment_other)
			db.session.add(entry)
			db.session.commit()
			immunity_environment = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = True
			item['field'] = 'env-sml'
			body['new_items'] = new_items
			new_items.append(item)
			db.session.close()
		
		if move_nature == 'other':	
			entry = Nature(name=move_other)
			db.session.add(entry)
			db.session.commit()
			move_nature = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = True
			item['field'] = 'nature-sml'
			body['new_items'] = new_items
			new_items.append(item)
			db.session.close()

		entry = PowerEnv(power_id = power_id,
							extra_id = extra_id,
							radius = radius,
							distance = distance,
							rank = rank,
							condition_check = condition_check,
							impede = impede,
							conceal = conceal,
							visibility = visibility,
							selective = selective,
							immunity = immunity,
							immunity_type = immunity_type,
							temp_type = temp_type,
							immunity_extremity = immunity_extremity,
							immunity_environment = immunity_environment,
							no_penalty = no_penalty,
							no_circumstance = no_circumstance,
							condition_temp_type = condition_temp_type,
							temp_extremity = temp_extremity,
							move_nature = move_nature,
							move_speed = move_speed,
							move_cost_circ = move_cost_circ,
							move_other = move_other,
							conceal_type = conceal_type,
							visibility_trait_type = visibility_trait_type,
							visibility_trait = visibility_trait,
							visibility_mod = visibility_mod,
							cost = cost,
							ranks = ranks)

		db.session.add(entry)
		db.session.commit()

		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'env'
		spot = "env-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = environment_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/env/delete/<power_id>', methods=['DELETE'])
def delete_power_env(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerEnv).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/levels/create', methods=['POST'])
def power_post_levels():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = levels_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)

	level_check = db.session.query(LevelType).filter(LevelType.name == level_type).first()
	if level_check is None:

		try:
			level_add = LevelType(power_id=power_id,
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
		level_power = level_check.power_id
		print(power_id)
		print(level_power)
		if power_id != level_power:
			body['success'] = False
			body['error_msgs'] = ['There is already a level type with that name.']
			return jsonify(body)

		type_id = level_check.id
		body['created'] = True

	try:
		entry = Levels(power_id = power_id,
							extra_id = extra_id,
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
		body['circ'] = []

		body = levels_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	
	return jsonify(body)


@powers.route('/power/levels/delete/<power_id>', methods=['DELETE'])
def delete_power_levels(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(Levels).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this level.  You may have already used it on another rule.  Delete that rule first.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/minion/create', methods=['POST'])
def power_post_minion():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = minion_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	condition = db_integer(Condition, condition)
	player_condition = db_integer(Condition, player_condition)
	attitude_type = db_integer(LevelType, attitude_type)
	attitude_attitude = db_integer(Levels, attitude_attitude)
	resitable_check = db_integer(Defense, resitable_check)

	points = integer(points)
	sacrifice_cost = integer(sacrifice_cost)
	attitude_trait = integer(attitude_trait)
	resitable_dc = integer(resitable_dc)
	multiple_value = integer(multiple_value)

	try:
		entry = PowerMinion(power_id = power_id,
							extra_id = extra_id,
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
							attitude_attitude = attitude_attitude,
							attitude_type = attitude_type,
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
		spot = "minion-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = minion_post(entry, body, cells)

	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()

	return jsonify(body)


@powers.route('/power/minion/delete/<power_id>', methods=['DELETE'])
def delete_power_minion(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerMinion).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/mod/create', methods=['POST'])
def power_post_mod():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = mod_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	affects_objects = request.get_json()['affects_objects']
	area = request.get_json()['area']
	persistent = request.get_json()['persistent']
	incurable = request.get_json()['incurable']
	selective = request.get_json()['selective']
	limited = request.get_json()['limited']
	innate = request.get_json()['innate']
	others = request.get_json()['others']
	sustained = request.get_json()['sustained']
	reflect = request.get_json()['reflect']
	redirect = request.get_json()['redirect']
	half = request.get_json()['half']
	affects_corp = request.get_json()['affects_corp']
	continuous = request.get_json()['continuous']
	vulnerable = request.get_json()['vulnerable']
	precise = request.get_json()['precise']
	progressive = request.get_json()['progressive']
	subtle = request.get_json()['subtle']
	permanent = request.get_json()['permanent']
	points = request.get_json()['points']
	ranks_check = request.get_json()['ranks_check']
	action = request.get_json()['action']
	side_effect = request.get_json()['side_effect']
	concentration = request.get_json()['concentration']
	simultaneous = request.get_json()['simultaneous']
	effortless = request.get_json()['effortless']
	noticeable = request.get_json()['noticeable']
	unreliable = request.get_json()['unreliable']
	radius = request.get_json()['radius']
	accurate = request.get_json()['accurate']
	acute = request.get_json()['acute']
	objects_alone = request.get_json()['objects_alone']
	objects_character = request.get_json()['objects_character']
	effortless_degree = request.get_json()['effortless_degree']
	effortless_retries = request.get_json()['effortless_retries']
	simultaneous_descriptor = request.get_json()['simultaneous_descriptor']
	area_mod = request.get_json()['area_mod']
	area_range = request.get_json()['area_range']
	area_per_rank = request.get_json()['area_per_rank']
	area_descriptor = request.get_json()['area_descriptor']
	limited_type = request.get_json()['limited_type']
	limited_mod = request.get_json()['limited_mod']
	limited_level = request.get_json()['limited_level']
	limited_source = request.get_json()['limited_source']
	limited_task_type = request.get_json()['limited_task_type']
	limited_task = request.get_json()['limited_task']
	limited_trait_type = request.get_json()['limited_trait_type']
	limited_trait = request.get_json()['limited_trait']
	limited_description = request.get_json()['limited_description']
	limited_subjects = request.get_json()['limited_subjects']
	limited_extra = request.get_json()['limited_extra']
	limited_language_type = request.get_json()['limited_language_type']
	limited_degree = request.get_json()['limited_degree']
	limited_sense = request.get_json()['limited_sense']
	limited_subsense = request.get_json()['limited_subsense']
	limited_descriptor = request.get_json()['limited_descriptor']
	limited_range = request.get_json()['limited_range']
	side_effect_type = request.get_json()['side_effect_type']
	side_level = request.get_json()['side_level']
	side_other = request.get_json()['side_other']
	reflect_check = request.get_json()['reflect_check']
	reflect_dc = request.get_json()['reflect_dc']
	reflect_trait_type = request.get_json()['reflect_trait_type']
	reflect_trait = request.get_json()['reflect_trait']
	reflect_descriptor = request.get_json()['reflect_descriptor']
	subtle_opponent_trait_type = request.get_json()['subtle_opponent_trait_type']
	subtle_opponent_trait = request.get_json()['subtle_opponent_trait']
	subtle_dc = request.get_json()['subtle_dc']
	subtle_null_trait_type = request.get_json()['subtle_null_trait_type']
	subtle_null_trait = request.get_json()['subtle_null_trait']
	others_carry = request.get_json()['others_carry']
	others_touch = request.get_json()['others_touch']
	others_touch_continuous = request.get_json()['others_touch_continuous']
	ranks_trait_type = request.get_json()['ranks_trait_type']
	ranks_trait = request.get_json()['ranks_trait']
	ranks_ranks = request.get_json()['ranks_ranks']
	ranks_mod = request.get_json()['ranks_mod']
	points_type = request.get_json()['points_type']
	points_reroll_target = request.get_json()['points_reroll_target']
	points_reroll_cost = request.get_json()['points_reroll_cost']
	points_rerolls = request.get_json()['points_rerolls']
	points_reroll_result = request.get_json()['points_reroll_result']
	ranks = request.get_json()['ranks']
	cost = request.get_json()['cost']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)


	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	objects_alone = db_integer(Defense, objects_alone)
	objects_character = db_integer(Defense, objects_character)
	limited_level = db_integer(Levels, limited_level)
	limited_extra = db_integer(Extra, limited_extra)
	limited_sense = db_integer(Sense, limited_sense)
	limited_range = db_integer(Range, limited_range)
	side_level = db_integer(Levels, side_level)
	reflect_check = db_integer(Check, reflect_check)

	effortless_degree = integer(effortless_degree)
	effortless_retries = integer(effortless_retries)
	simultaneous_descriptor = integer(simultaneous_descriptor)
	area_mod = integer(area_mod)
	area_range = integer(area_range)
	area_descriptor = integer(area_descriptor)
	limited_mod = integer(limited_mod)
	limited_source = integer(limited_source)
	limited_trait = integer(limited_trait)
	limited_subjects = integer(limited_subjects)
	limited_degree = integer(limited_degree)
	limited_descriptor = integer(limited_descriptor)
	reflect_dc = integer(reflect_dc)
	reflect_trait = integer(reflect_trait)
	reflect_descriptor = integer(reflect_descriptor)
	subtle_opponent_trait = integer(subtle_opponent_trait)
	subtle_dc = integer(subtle_dc)
	subtle_null_trait = integer(subtle_null_trait)
	ranks_trait = integer(ranks_trait)
	ranks_ranks = integer(ranks_ranks)
	ranks_mod = integer(ranks_mod)
	points_reroll_cost = integer(points_reroll_cost)
	points_rerolls = integer(points_rerolls)


	try:
		entry = PowerMod(power_id = power_id,
							extra_id = extra_id,
							affects_objects = affects_objects,
							area = area,
							persistent = persistent,
							incurable = incurable,
							selective = selective,
							limited = limited,
							innate = innate,
							others = others,
							sustained = sustained,
							reflect = reflect,
							redirect = redirect,
							half = half,
							affects_corp = affects_corp,
							continuous = continuous,
							vulnerable = vulnerable,
							precise = precise,
							progressive = progressive,
							subtle = subtle,
							permanent = permanent,
							points = points,
							ranks_check = ranks_check,
							action = action,
							side_effect = side_effect,
							concentration = concentration,
							simultaneous = simultaneous,
							effortless = effortless,
							noticeable = noticeable,
							unreliable = unreliable,
							radius = radius,
							accurate = accurate,
							acute = acute,
							objects_alone = objects_alone,
							objects_character = objects_character,
							effortless_degree = effortless_degree,
							effortless_retries = effortless_retries,
							simultaneous_descriptor = simultaneous_descriptor,
							area_mod = area_mod,
							area_range = area_range,
							area_per_rank = area_per_rank,
							area_descriptor = area_descriptor,
							limited_type = limited_type,
							limited_mod = limited_mod,
							limited_level = limited_level,
							limited_source = limited_source,
							limited_task_type = limited_task_type,
							limited_task = limited_task,
							limited_trait_type = limited_trait_type,
							limited_trait = limited_trait,
							limited_description = limited_description,
							limited_subjects = limited_subjects,
							limited_extra = limited_extra,
							limited_language_type = limited_language_type,
							limited_degree = limited_degree,
							limited_sense = limited_sense,
							limited_subsense = limited_subsense,
							limited_descriptor = limited_descriptor,
							limited_range = limited_range,
							side_effect_type = side_effect_type,
							side_level = side_level,
							side_other = side_other,
							reflect_check = reflect_check,
							reflect_dc = reflect_dc,
							reflect_trait_type = reflect_trait_type,
							reflect_trait = reflect_trait,
							reflect_descriptor = reflect_descriptor,
							subtle_opponent_trait_type = subtle_opponent_trait_type,
							subtle_opponent_trait = subtle_opponent_trait,
							subtle_dc = subtle_dc,
							subtle_null_trait_type = subtle_null_trait_type,
							subtle_null_trait = subtle_opponent_trait,
							others_carry = others_carry,
							others_touch = others_touch,
							others_touch_continuous = others_touch_continuous,
							ranks_trait_type = ranks_trait_type,
							ranks_trait = ranks_trait,
							ranks_ranks = ranks_ranks,
							ranks_mod = ranks_mod,
							points_type = points_type,
							points_reroll_target = points_reroll_target,
							points_reroll_cost = points_reroll_cost,
							points_rerolls = points_rerolls,
							points_reroll_result = points_reroll_result,
							ranks = ranks,
							cost = cost)

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
		table_id = 'modifiers'
		spot = 'mod-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = mod_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()

	return jsonify(body)


@powers.route('/power/mod/delete/<power_id>', methods=['DELETE'])
def delete_power_mod(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerMod).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/ranged/create', methods=['POST'])
def power_post_ranged():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = ranged_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	range_type = request.get_json()['range_type']
	flat_value = request.get_json()['flat_value']
	flat_units = request.get_json()['flat_units']
	flat_rank = request.get_json()['flat_rank']
	flat_rank_value = request.get_json()['flat_rank_value']
	flat_rank_units = request.get_json()['flat_rank_units']
	flat_rank_rank = request.get_json()['flat_rank_rank']
	flat_rank_distance = request.get_json()['flat_rank_distance']
	flat_rank_distance_rank = request.get_json()['flat_rank_distance_rank']
	units_rank_start_value = request.get_json()['units_rank_start_value']
	units_rank_value = request.get_json()['units_rank_value']
	units_rank_units = request.get_json()['units_rank_units']
	units_rank_rank = request.get_json()['units_rank_rank']
	rank_distance_start = request.get_json()['rank_distance_start']
	rank_distance = request.get_json()['rank_distance']
	rank_effect_rank = request.get_json()['rank_effect_rank']
	effect_mod_math = request.get_json()['effect_mod_math']
	effect_mod = request.get_json()['effect_mod']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_math = request.get_json()['check_math']
	check_mod = request.get_json()['check_mod']
	trait_trait_type = request.get_json()['trait_trait_type']
	trait_trait = request.get_json()['trait_trait']
	trait_math = request.get_json()['trait_math']
	trait_mod = request.get_json()['trait_mod']
	distance_mod_rank = request.get_json()['distance_mod_rank']
	distance_mod_math = request.get_json()['distance_mod_math']
	distance_mod_trait_type = request.get_json()['distance_mod_trait_type']
	distance_mod_trait = request.get_json()['distance_mod_trait']
	dc = request.get_json()['dc']
	circ = request.get_json()['circ']
	degree = request.get_json()['degree']
	damage = request.get_json()['damage']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	keyword = request.get_json()['keyword']
	title = request.get_json()['title']
	rank = request.get_json()['rank']

	dc = db_integer(PowerDC, dc)
	circ = db_integer(PowerCirc, circ)
	degree = db_integer(PowerDegree, degree)
	damage = db_integer(PowerDamage, damage)

	body = {}
	body['success'] = True
	body['error_msgs'] = []

	body = linked_ref(PowerCirc, circ, 'Circumstance', 'ranged', body)
	body = linked_ref(PowerDamage, damage, 'Damage Effect', 'ranged', body)
	body = linked_ref(PowerDC, dc, 'DC', 'ranged', body)
	body = linked_ref(PowerDegree, degree, 'Degree', 'ranged', body)

	body = link_add(PowerRanged, PowerRangedType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)
 
	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	flat_units = db_integer(Unit, flat_units)
	flat_rank_units = db_integer(Unit, flat_rank_units)
	units_rank_units = db_integer(Unit, units_rank_units)
	effect_mod_math = db_integer(Math, effect_mod_math)
	check_math = db_integer(Math, check_math)
	trait_math = db_integer(Math, trait_math)
	distance_mod_math = db_integer(Math, distance_mod_math)

	flat_value = integer(flat_value)
	flat_rank = integer(flat_rank)
	flat_rank_value = integer(flat_rank_value)
	flat_rank_rank = integer(flat_rank_rank)
	flat_rank_distance = integer(flat_rank_distance)
	flat_rank_distance_rank = integer(flat_rank_distance_rank)
	units_rank_start_value = integer(units_rank_start_value)
	units_rank_value = integer(units_rank_value)
	units_rank_rank = integer(units_rank_rank)
	rank_distance_start = integer(rank_distance_start)
	rank_distance = integer(rank_distance)
	rank_effect_rank = integer(rank_effect_rank)
	effect_mod = integer(effect_mod)
	check_trait = integer(check_trait)
	check_mod = integer(check_mod)
	trait_trait = integer(trait_trait)
	trait_mod = integer(trait_mod)
	distance_mod_rank = integer(distance_mod_rank)
	distance_mod_trait = integer(distance_mod_trait)



	try:
		entry = PowerRanged(power_id = power_id,
							extra_id = extra_id,
							range_type = range_type,
							flat_value = flat_value,
							flat_units = flat_units,
							flat_rank = flat_rank,
							flat_rank_value = flat_rank_value,
							flat_rank_units = flat_rank_units,
							flat_rank_rank = flat_rank_rank,
							flat_rank_distance = flat_rank_distance,
							flat_rank_distance_rank = flat_rank_distance_rank,
							units_rank_start_value = units_rank_start_value,
							units_rank_value = units_rank_value,
							units_rank_units = units_rank_units,
							units_rank_rank = units_rank_rank,
							rank_distance_start = rank_distance_start,
							rank_distance = rank_distance,
							rank_effect_rank = rank_effect_rank,
							effect_mod_math = effect_mod_math,
							effect_mod = effect_mod,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							check_math = check_math,
							check_mod = check_mod,
							trait_trait_type = trait_trait_type,
							trait_trait = trait_trait,
							trait_math = trait_math,
							trait_mod = trait_mod,
							distance_mod_rank = distance_mod_rank,
							distance_mod_math = distance_mod_math,
							distance_mod_trait_type = distance_mod_trait_type,
							distance_mod_trait = distance_mod_trait,
							dc = dc,
							circ = circ,
							degree = degree,
							damage = damage,
							keyword = keyword,
							title = title,
							rank = rank)

		db.session.add(entry)
		db.session.commit()

		body['id'] = entry.id
		error = False
		error_msg = []

		rows = columns
		mods = []
		cells = []
		table_id = 'ranged'
		spot = "ranged-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = ranged_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/ranged/delete/<power_id>', methods=['DELETE'])
def delete_power_ranged(power_id):
	
	body = delete_link(PowerRanged, PowerRangedType, power_id)
	return jsonify(body)

@powers.route('/power/resist/create', methods=['POST'])
def power_post_resist():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = resist_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	mod = request.get_json()['mod']
	rounds = request.get_json()['rounds']
	circumstance = request.get_json()['circumstance']
	resist_check_type = request.get_json()['resist_check_type']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	descriptor = request.get_json()['descriptor']
	requires_check = request.get_json()['requires_check']
	check_type = request.get_json()['check_type']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	check_type = db_integer(Check, check_type)

	mod = integer(mod)
	rounds = integer(rounds)
	trait = integer(trait)
	descriptor = integer(descriptor)
	check_trait = integer(check_trait)

	try:
		entry = PowerResist(power_id = power_id,
							extra_id = extra_id,
							target = target,
							mod = mod,
							rounds = rounds,
							circumstance = circumstance,
							resist_check_type = resist_check_type,
							trait_type = trait_type,
							trait = trait,
							descriptor = descriptor,
							requires_check = requires_check,
							check_type = check_type,
							check_trait_type = check_trait_type,
							check_trait = check_trait)

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
		table_id = 'resistance'
		spot = "resistance-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []
			
		body = resist_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/resistance/delete/<power_id>', methods=['DELETE'])
def delete_power_resistance(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerResist).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/resisted_by/create', methods=['POST'])
def power_post_resisted_by():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = resisted_by_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	trait_type = request.get_json()['trait_type']
	dc = request.get_json()['dc']
	mod = request.get_json()['mod']
	description = request.get_json()['description']
	trait = request.get_json()['trait']
	effect = request.get_json()['effect']
	level = request.get_json()['level']
	degree = request.get_json()['degree']
	descriptor = request.get_json()['descriptor']
	weaken_max = request.get_json()['weaken_max']
	weaken_restored = request.get_json()['weaken_restored']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	damage = request.get_json()['damage']
	strength = request.get_json()['strength']
	nullify_descriptor = request.get_json()['nullify_descriptor']
	nullify_alternate = request.get_json()['nullify_alternate']
	extra_effort = request.get_json()['extra_effort']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	nullify_alternate = db_integer(Defense, nullify_alternate)

	trait = integer(trait)
	dc = integer(dc)
	mod = integer(mod)
	degree = integer(degree)
	descriptor = integer(descriptor)
	weaken_max = integer(weaken_max)
	weaken_restored = integer(weaken_restored)
	damage = integer(damage)
	nullify_descriptor = integer(nullify_descriptor)

	try:
		entry = PowerResistBy(power_id = power_id,
								extra_id = extra_id,
								trait_type = trait_type,
								dc = dc,
								mod = mod,
								description = description,
								trait = trait,
								effect = effect,
								level = level,
								degree = degree,
								descriptor = descriptor,
								weaken_max = weaken_max,
								weaken_restored = weaken_restored,
								condition1 = condition1,
								condition2 = condition2,
								damage =  damage,
								strength = strength,
								nullify_descriptor = nullify_descriptor,
								nullify_alternate = nullify_alternate,
								extra_effort = extra_effort)

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
		spot = "resist-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = resisted_by_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/resist/delete/<power_id>', methods=['DELETE'])
def delete_power_resist(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerResistBy).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/reverse_effect/create', methods=['POST'])
def power_post_reverse_effect():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = reverse_effect_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	degree = request.get_json()['degree']
	when = request.get_json()['when']
	check_check = request.get_json()['check_check']
	time_check = request.get_json()['time_check']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	value_type = request.get_json()['value_type']
	value_dc = request.get_json()['value_dc']
	math_dc = request.get_json()['math_dc']
	math = request.get_json()['math']
	time_value = request.get_json()['time_value']
	time_unit = request.get_json()['time_unit']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	time_unit = db_integer(Unit, time_unit)

	degree = integer(degree)
	trait = integer(trait)
	value_dc = integer(value_dc)
	math_dc = integer(math_dc)
	time_value = integer(time_value)


	try:
		entry = PowerReverse(power_id = power_id,
								extra_id = extra_id,
								target = target,
								degree = degree,
								when = when,
								check_check = check_check,
								time_check = time_check,
								trait_type = trait_type,
								trait = trait,
								value_type = value_type,
								value_dc = value_dc,
								math_dc = math_dc,
								math = math,
								time_value = time_value,
								time_unit = time_unit)

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
		table_id = 'reverse'
		spot = "reverse-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = reverse_effect_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/reverse/delete/<power_id>', methods=['DELETE'])
def delete_power_reverse(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerReverse).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/sense/create', methods=['POST'])
def power_post_sense():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = sense_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	sense = request.get_json()['sense']
	subsense = request.get_json()['subsense']
	skill = request.get_json()['skill']
	sense_type = request.get_json()['sense_type']
	height_trait_type = request.get_json()['height_trait_type']
	height_trait = request.get_json()['height_trait']
	height_power_required = request.get_json()['height_power_required']
	height_ensense = request.get_json()['height_ensense']
	resist_trait_type = request.get_json()['resist_trait_type']
	resist_trait = request.get_json()['resist_trait']
	resist_immune = request.get_json()['resist_immune']
	resist_permanent = request.get_json()['resist_permanent']
	resist_circ = request.get_json()['resist_circ']
	objects = request.get_json()['objects']
	exclusive = request.get_json()['exclusive']
	gm = request.get_json()['gm']
	dark = request.get_json()['dark']
	lighting = request.get_json()['lighting']
	time = request.get_json()['time']
	dimensional = request.get_json()['dimensional']
	radius = request.get_json()['radius']
	accurate = request.get_json()['accurate']
	acute = request.get_json()['acute']
	time_value = request.get_json()['time_value']
	time_type = request.get_json()['time_type']
	distance = request.get_json()['distance']
	distance_dc = request.get_json()['distance_dc']
	distance_mod = request.get_json()['distance_mod']
	distance_value = request.get_json()['distance_value']
	distance_unit = request.get_json()['distance_unit']
	distance_factor = request.get_json()['distance_factor']
	dimensional_type = request.get_json()['dimensional_type']
	ranks = request.get_json()['ranks']
	cost = request.get_json()['cost']
	created = request.get_json()['created']
	columns = request.get_json()['columns']
	font = request.get_json()['font']
	circ = request.get_json()['circ']

	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)
	skill = db_integer(PowerCheck, skill)
	time_value = db_integer(PowerTime, time_value)
	time_type = db_integer(PowerTimeType, time_type)
	circ = db_integer(PowerCirc, circ)

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	sense = db_integer(Sense, sense)
	subsense = db_integer(SubSense, subsense)
	skill = db_integer(Skill, skill)
	height_ensense = db_integer(Power, height_ensense)
	lighting = db_integer(Light, lighting)
	time_bonus = db_integer(SkillBonus, time_bonus)
	distance_unit = db_integer(Unit, distance_unit)

	height_trait = integer(height_trait)
	resist_trait = integer(resist_trait)
	resist_circ = integer(resist_circ)
	time_value = integer(time_value)
	time_factor = integer(time_factor)
	distance_dc = integer(distance_dc)
	distance_mod = integer(distance_mod)
	distance_value = integer(distance_value)
	distance_factor = integer(distance_factor)



	try:
		entry = PowerSenseEffect(power_id = power_id,
									extra_id = extra_id,
									target = target,
									sense = sense,
									subsense = subsense,
									skill = skill,
									sense_type = sense_type,
									height_trait_type = height_trait_type,
									height_trait = height_trait,
									height_power_required = height_power_required,
									height_ensense = height_ensense,
									resist_trait_type = resist_trait_type,
									resist_trait = resist_trait,
									resist_immune = resist_immune,
									resist_permanent = resist_permanent,
									resist_circ = resist_circ,
									objects = objects,
									exclusive = exclusive,
									gm = gm,
									dark = dark,
									lighting = lighting,
									time = time,
									dimensional = dimensional,
									radius = radius,
									accurate = accurate,
									acute = acute,
									time_value = time_value,
									time_type = time_type,
									distance = distance,
									distance_dc = distance_dc,
									distance_mod = distance_mod,
									distance_value = distance_value,
									distance_unit = distance_unit,
									distance_factor = distance_factor,
									dimensional_type = dimensional_type,
									ranks = ranks,
									cost = cost,
									circ = circ)

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
		table_id = 'sense'
		spot = "sense-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = sense_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/sense/delete/<power_id>', methods=['DELETE'])
def delete_power_sense(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerSenseEffect).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)



@powers.route('/power/check/create', methods=['POST'])
def power_post_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = power_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	ranged = request.get_json()['ranged']
	variable = request.get_json()['variable']
	opponent = request.get_json()['opponent']

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

	degree = db_integer(PowerDegreeType, degree)
	circ = db_integer(PowerCircType, circ)
	dc = db_integer(PowerDCType, dc)
	time = db_integer(PowerTimeType, time)
	move = db_integer(PowerMoveType, move)
	opposed = db_integer(PowerOpposed, opposed)
	dc_value = db_integer(PowerDC, dc_value)
	ranged = db_integer(PowerRangedType, ranged)
	variable = db_integer(PowerCheck, variable)
	opponent = db_integer(PowerOpposed, opponent)

	attack = integer(attack)

	check_type = db_integer(Check, check_type)
	conflict = db_integer(ConflictAction, conflict)
	conflict_range = db_integer(Ranged, conflict_range)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	condition = db_integer(Condition, condition)

	trait = integer(trait)
	action = integer(action)

	body['error_msgs'] = []
	body = linked_ref(PowerOpposed, opponent, 'Opponent Check Trigger', 'chained', body)
	body = linked_ref(PowerCheck, variable, 'Opponent Check Trigger', 'chained', body)

	if body['success'] == False:
		return jsonify(body)

	entry = PowerCheck(power_id = power_id,
						extra_id = extra_id,
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
						conditions_target = conditions_target,
						ranged = ranged,
						variable = variable,
						opponent = opponent
					)

	db.session.add(entry)
	db.session.commit()

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

	body = power_check_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/check/delete/<id>', methods=['DELETE'])
def delete_power_check(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(PowerCheck).filter_by(id=id).delete()
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

@powers.route('/power/circ/create', methods=['POST'])
def power_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	descriptor_effect = request.get_json()['descriptor_effect']
	descriptor_target = request.get_json()['descriptor_target']
	descriptor = request.get_json()['descriptor']

	errors = power_circ_post_errors(data)

	errors = level_reference('power_circ', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

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
	descriptor = descriptor(PowerDes, descriptor)

	lasts = db_integer(PowerTime, lasts)


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

	body = link_add(PowerCirc, PowerCircType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)


	entry = PowerCirc(power_id = power_id,
						extra_id = extra_id,
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
						check_type = check_type,
						descriptor_effect = descriptor_effect,
						descriptor_target = descriptor_target,
						descriptor = descriptor
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
	
	body = power_circ_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/circ/delete/<id>', methods=['DELETE'])
def delete_power_circ(id):
	
	body = delete_link(PowerCirc, PowerCircType, id)
	return jsonify(body)

@powers.route('/power/dc/create', methods=['POST'])
def power_post_dc():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	descriptor_effect = request.get_json()['descriptor_effect']
	descriptor_target = request.get_json()['descriptor_target']
	descriptor = request.get_json()['descriptor']
	descrip = request.get_json()['descrip']


	errors = power_dc_post_errors(data)

	errors = level_reference('power_dc', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

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
	descriptor = descriptor(PowerDes, descriptor)

	time = db_integer(PowerTime, time)
	variable = db_integer(PowerCheck, variable)

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


	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(PowerDC, PowerDCType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = PowerDC(power_id = power_id,
					extra_id = extra_id,
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
					equip = equip,
					descriptor_effect = descriptor_effect,
					descriptor_target = descriptor_target,
					descriptor = descriptor,
					descrip = descrip
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
	
	body = power_dc_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/dc/delete/<id>', methods=['DELETE'])
def delete_power_dc(id):
	
	body = delete_link(PowerDC, PowerDCType, id)
	return jsonify(body)

@powers.route('/power/degree/create', methods=['POST'])
def power_post_degree():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	descriptor_effect = request.get_json()['descriptor_effect']
	descriptor_target = request.get_json()['descriptor_target']
	descriptor = request.get_json()['descriptor']

	errors = power_degree_post_errors(data)

	errors = level_reference('power_degree', level, errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

	action = db_integer(Action, action)
	inflict_math = db_integer(Math, inflict_math)
	damage_consequence = db_integer(Consequence, damage_consequence)
	consequence = db_integer(Consequence, consequence)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
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
	descriptor = descriptor(PowerDes, descriptor)

	opposed = db_integer(PowerOpposed, opposed)
	resist_dc = db_integer(PowerDC, resist_dc)
	skill_dc = db_integer(PowerDC, skill_dc)
	compare = db_integer(PowerOpposed, compare)
	variable = db_integer(PowerCheck, variable)
	attack_turns = db_integer(PowerTime, attack_turns)
	condition_turns = db_integer(PowerTime, condition_turns)
	level_time = db_integer(PowerTime, level_time)
	linked = db_integer(PowerDegree, linked)
	circumstance = db_integer(PowerCirc, circumstance)

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

	body = link_add(PowerDegree, PowerDegreeType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = PowerDegree(power_id = power_id,
						extra_id = extra_id,
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
						description = description,
						descriptor_effect = descriptor_effect,
						descriptor_target = descriptor_target,
						descriptor = descriptor)

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
	
	body = power_degree_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/degree/delete/<id>', methods=['DELETE'])
def delete_power_degree(id):
		
	body = delete_link(PowerDegree, PowerDegreeType, id)
	return jsonify(body)

@powers.route('/power/move/create', methods=['POST'])
def power_post_move():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	degree_type = request.get_json()['degree_type']
	circ_type = request.get_json()['circ_type']
	dc_type = request.get_json()['dc_type']
	time_type = request.get_json()['time_type']
	keyword = request.get_json()['keyword']
	title = request.get_json()['title']

	speed_per = request.get_json()['speed_per']
	distance_per = request.get_json()['distance_per']
	flight = request.get_json()['flight']
	aquatic = request.get_json()['aquatic']
	ground = request.get_json()['ground']
	special = request.get_json()['special']
	condition_check = request.get_json()['condition_check']
	obstacles = request.get_json()['obstacles']
	objects = request.get_json()['objects']
	permeate = request.get_json()['permeate']
	prone = request.get_json()['prone']
	equip = request.get_json()['equip']
	concealment = request.get_json()['concealment']
	extended = request.get_json()['extended']
	mass = request.get_json()['mass']
	flight_resist = request.get_json()['flight_resist']
	flight_resist_check = request.get_json()['flight_resist_check']
	flight_equip = request.get_json()['flight_equip']
	flight_equip_type = request.get_json()['flight_equip_type']
	flight_equipment = request.get_json()['flight_equipment']
	flight_conditions = request.get_json()['flight_conditions']
	acquatic_type = request.get_json()['acquatic_type']
	ground_type = request.get_json()['ground_type']
	ground_perm = request.get_json()['ground_perm']
	ground_time = request.get_json()['ground_time']
	ground_ranged = request.get_json()['ground_ranged']
	ground_range = request.get_json()['ground_range']
	special_type = request.get_json()['special_type']
	teleport_type = request.get_json()['teleport_type']
	teleport_change = request.get_json()['teleport_change']
	teleport_portal = request.get_json()['teleport_portal']
	teleport_obstacles = request.get_json()['teleport_obstacles']
	dimension_type = request.get_json()['dimension_type']
	dimension_mass_rank = request.get_json()['dimension_mass_rank']
	dimension_descriptor = request.get_json()['dimension_descriptor']
	special_space = request.get_json()['special_space']
	special_time = request.get_json()['special_time']
	special_time_carry = request.get_json()['special_time_carry']
	condition = request.get_json()['condition']
	objects_check = request.get_json()['objects_check']
	objects_direction = request.get_json()['objects_direction']
	objects_damage = request.get_json()['object_damage']
	object_damage = request.get_json()['object_damage']
	permeate_type = request.get_json()['permeate_type']
	permeate_speed = request.get_json()['permeate_speed']
	permeate_cover = request.get_json()['permeate_cover']
	equip_type = request.get_json()['equip_type']
	equipment = request.get_json()['equipment']
	concealment_sense = request.get_json()['concealment_sense']
	conceal_opposed = request.get_json()['conceal_opposed']
	extended_actions = request.get_json()['extended_actions']
	mass_value = request.get_json()['mass_value']

	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks']


	errors = power_move_post_errors(data)

	errors = linked_move(PowerCirc, circ, 'Circumstance', errors)
	errors = linked_move(PowerDC, dc, 'DC', errors)
	errors = linked_move(PowerDegree, degree, 'Degree', errors)

	errors = linked_move(PowerCircType, circ_type, 'Circumstance Group', errors)
	errors = linked_move(PowerDCType, dc_type, 'DC Group', errors)
	errors = linked_move(PowerDegreeType, degree_type, 'Degree Group', errors)
	errors = linked_move(PowerDegreeType, degree_type, 'Time Group', errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)
	

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

	degree = db_integer(PowerDegree, degree)
	circ = db_integer(PowerCirc, circ)
	dc = db_integer(PowerDC, dc)
	time = db_integer(PowerTime, time)

	degree_type = db_integer(PowerDegreeType, degree_type)
	circ_type = db_integer(PowerCircType, circ_type)
	dc_type = db_integer(PowerDCType, dc_type)
	time_type = db_integer(PowerTimeType, time_type)

	flight_resist_check = db_integer(PowerCheck, flight_resist_check)
	ground_time = db_integer(PowerTime, ground_time)
	ground_range = db_integer(PowerRangedType, ground_range)
	objects_check = db_integer(PowerCheck, objects_check)
	object_damage = db_integer(PowerDamage, object_damage)
	conceal_opposed = db_integer(PowerOpposed, conceal_opposed)
	cost = db_integer(PowerCost, cost)
	ranks = db_integer(PowerRanks, ranks)

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
	dimension_mass_rank = integer(dimension_mass_rank)
	special_time_carry = integer(special_time_carry)
	permeate_speed = integer(permeate_speed)
	extended_actions = integer(extended_actions)
	mass_value = integer(mass_value)

	speed_math1 = db_integer(Math, speed_math1)
	speed_math2 = db_integer(Math, speed_math2)
	distance_units = db_integer(Unit, distance_units)
	distance_rank_math1 = db_integer(Math, distance_rank_math1)
	distance_rank_math2 = db_integer(Math, distance_rank_math2)
	distance_unit_math1 = db_integer(Math, distance_unit_math1)
	distance_unit_math2 = db_integer(Math, distance_unit_math2)
	distance_math_units = db_integer(Unit, distance_math_units)

	flight_conditions = db_multiple(Condition, flight_conditions)

	flight_equip_type = db_integer(EquipType, flight_equip_type)
	flight_equipment = db_integer(Equipment, flight_equipment)
	ground_type = db_integer(Ground, ground_type)
	dimension_descriptor = db_integer(PowerDes, dimension_descriptor)
	condition = db_integer(Condition, condition)
	equip_type = db_integer(EquipType, equip_type)
	equipment = db_integer(Equipment, equipment)
	concealment_sense = db_integer(Sense, concealment_sense)

	body = {}
	body['success'] = True
	body['created'] = created

	body = link_add(PowerMove, PowerMoveType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	body = linked_ref(PowerRanged, ground_ranged, 'Ranged Effect', 'movement', body)
	body = linked_ref(PowerDamage, object_damage, 'Damage Effect', 'movement', body)

	if body['success'] == False:
		return jsonify(body)
	
	entry = PowerMove(power_id = power_id,
						extra_id = extra_id,
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
						time = time,												
						degree_type = degree_type,
						dc_type = dc_type,
						circ_type = circ_type,
						time_type = time_type,												
						speed_per = speed_per,
						distance_per = distance_per,
						flight = flight,
						aquatic = aquatic,
						ground = ground,
						special = special,
						condition_check = condition_check,
						obstacles = obstacles,
						objects = objects,
						permeate = permeate,
						prone = prone,
						equip = equip,
						concealment = concealment,
						extended = extended,
						mass = mass,
						flight_resist = flight_resist,
						flight_resist_check = flight_resist_check,
						flight_equip = flight_equip,
						flight_equip_type = flight_equip_type,
						flight_equipment = flight_equipment,
						flight_conditions = flight_conditions,
						acquatic_type = acquatic_type,
						ground_type = ground_type,
						ground_perm = ground_perm,
						ground_time = ground_time,
						ground_ranged = ground_ranged,
						ground_range = ground_range,
						special_type = special_type,
						teleport_type = teleport_type,
						teleport_change = teleport_change,
						teleport_portal = teleport_portal,
						teleport_obstacles = teleport_obstacles,
						dimension_type = dimension_type,
						dimension_mass_rank = dimension_mass_rank,
						dimension_descriptor = dimension_descriptor,
						special_space = special_space,
						special_time = special_time,
						special_time_carry = special_time_carry,
						condition = condition,
						objects_check = objects_check,
						objects_direction = objects_direction,
						objects_damage = objects_damage,
						object_damage = object_damage,
						permeate_type = permeate_type,
						permeate_speed = permeate_speed,
						permeate_cover = permeate_cover,
						equip_type = equip_type,
						equipment = equipment,
						concealment_sense = concealment_sense,
						conceal_opposed = conceal_opposed,
						extended_actions = extended_actions,
						mass_value = mass_value,
						cost = cost,
						ranks =  ranks
					)			


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
	
	body = power_move_post(entry, body, cells)
	
	db.session.close()

	return jsonify(body)

@powers.route('/power/move/delete/<id>', methods=['DELETE'])
def delete_power_move(id):
		
	body = delete_link(PowerMove, PowerMoveType, id)
	return jsonify(body)


@powers.route('/power/opposed/create', methods=['POST'])
def power_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = power_opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	variable = request.get_json()['variable']

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)

	degree = db_integer(PowerDegreeType, degree)
	circ = db_integer(PowerCircType, circ)
	dc = db_integer(PowerDC, dc)
	time = db_integer(PowerTime, dc)
	recurring_value = db_integer(PowerTime, recurring_value)
	degree_value = db_integer(PowerDegree, degree_value)
	dc_type = db_integer(PowerDCType, dc_type)
	dc_player = db_integer(PowerDC, dc_player)
	circ_value = db_integer(PowerCirc, circ_value)
	time_type = db_integer(PowerTimeType, time_type)
	recurring_type = db_integer(PowerTimeType, recurring_type)
	variable = db_integer(PowerCheck, variable)

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)

	body['error_msgs'] = []
	body = linked_ref(PowerCheck, variable, 'Opponent Check Trigger', 'chained', body)

	if body['success'] == False:
		return jsonify(body)

	entry = PowerOpposed(power_id = power_id,
						extra_id = extra_id,
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
						recurring_type = recurring_type,
						variable = variable
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
	
	body = power_opposed_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/opposed/delete/<id>', methods=['DELETE'])
def delete_power_opposed(id):
	body = {}
	body['success'] = True
	try:
		db.session.query(PowerOpposed).filter_by(id=id).delete()
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

@powers.route('/power/time/create', methods=['POST'])
def power_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
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
	maintain = preset_convert('maintain', value_type)
	scene = preset_convert('scene', value_type)
	turn = preset_convert('turn', value_type)
	time = request.get_json()['time']
	mod = request.get_json()['mod']
	mod = request.get_json()['mod']
	recovery_target = request.get_json()['recovery_target']
	rank = request.get_json()['rank']

	errors = power_time_post_errors(data)
	
	errors = linked_time(PowerCirc, circ, 'Circumstance', errors)
	errors = linked_time(PowerDC, dc, 'DC', errors)
	errors = linked_time(PowerDegree, degree, 'Degree', errors)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	power_id = db_integer(Power, power_id)
	extra_id = db_integer(Extra, extra_id)

	rank1 = db_integer(Rank, rank1)
	rank_math = db_integer(Math, rank_math)
	rank2 = db_integer(Rank, rank2)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)

	degree = db_integer(PowerDegree, degree)
	circ = db_integer(PowerCirc, circ)
	dc = db_integer(PowerDC, dc)
	circ_type = db_integer(PowerCircType, circ_type)
	degree_type = db_integer(PowerDegreeType, degree_type)
	dc_type = db_integer(PowerDCType, dc_type)	

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

	body = link_add(PowerTime, PowerTimeType, 'power_id', power_id, title, keyword, body)
	title = body['title_id']

	if body['success'] == False:
		return jsonify(body)

	entry = PowerTime(power_id = power_id,
						extra_id = extra_id,
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
						maintain = maintain,
						scene = scene,
						time = time,
						mod = mod,
						rank = rank
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
	
	body = power_time_post(entry, body, cells)

	db.session.close()

	return jsonify(body)

@powers.route('/power/time/delete/<id>', methods=['DELETE'])
def delete_power_time(id):
		
	body = delete_link(PowerTime, PowerTimeType, id)
	return jsonify(body)
