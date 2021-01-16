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
from advantage_posts import adv_benefit_post, adv_alt_check_post, adv_circ_post, adv_combined_post, adv_condition_post, adv_dc_post, adv_deg_mod_post, adv_effort_post, adv_minion_post, adv_modifiers_post, adv_opposed_post, adv_points_post, adv_resist_post, adv_rounds_post, adv_skill_post, adv_time_post, adv_variable_post
from advantage_errors import adv_benefit_post_errors, adv_alt_check_post_errors, adv_circ_post_errors, adv_combined_post_errors, adv_condition_post_errors, adv_dc_post_errors, adv_deg_mod_post_errors, adv_effort_post_errors, adv_minion_post_errors, adv_modifiers_post_errors, adv_opposed_post_errors, adv_points_post_errors, adv_resist_post_errors, adv_rounds_post_errors, adv_skill_post_errors, adv_time_post_errors, adv_variable_post_errors
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add


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

	advantage_type = [{'type': '', 'name': 'Advantage Type'}, {'type': 'combat', 'name': 'Combat'}, {'type': 'fortune', 'name': 'Fortune'}, {'type': 'General', 'name': 'General'}, {'type': 'skill', 'name': 'Skill'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Advantaage Rank'}, {'type': 'value', 'name': 'Value'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	actions = db.session.query(Action).all()

	conflicts = db.session.query(ConflictAction).order_by(ConflictAction.name).all()
	
	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	checks = db.session.query(Check).all()

	benefits = db.session.query(Benefit).filter_by(approved=True).order_by(Benefit.name).all()
	
	ranges = Range.query.all()

	cover = Cover.query.all()

	concealment = Conceal.query.all()
	
	times = db.session.query(Unit).filter_by(type_id=2)

	weapon_melee = db.session.query(WeaponType).filter_by(type_id=1)
	
	weapon_ranged = db.session.query(WeaponType).filter_by(type_id=2)

	ranged = db.session.query(Ranged).filter_by(show=True)

	environments = db.session.query(Environment).order_by(Environment.name).all()
	
	senses = db.session.query(Sense).order_by(Sense.name).all()

	subsenses = db.session.query(SubSense).order_by(SubSense.name).all()
	
	creatures = db.session.query(Creature).order_by(Creature.name).all()
	
	professions = db.session.query(Job).order_by(Job.name).all()
	
	maneuvers = db.session.query(Maneuver).order_by(Maneuver.name).all()
	
	emotions = db.session.query(Emotion).order_by(Emotion.name).all()

	base_conditions = Condition.query.all()
	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages = sorted(advantages_raw)

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]

	target = [{'type': '', 'name': 'Target'}, {'type': 'become', 'name': 'Become Target'}, {'type': 'redirect', 'name': 'Redirect From Self'}, {'type': 'setup', 'name': 'Transfer Action Result to Teammate'}]

	traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_advantage', 'name': 'This Advantage'}, {'type': 'any', 'name': 'Any Trait'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}, {'type': 'advantage', 'name': 'Advantage'}]

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
	
	consequences = db.session.query(Consequence).order_by(Consequence.name).all()

	action_type = [{'type': '', 'name': 'Action Type'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'base', 'name': 'Base Action'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	level_types = LevelType.query.order_by(LevelType.name).all()

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	value_type_mod = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'Modifier'}]

	maths = Math.query.all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

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
							ranged=ranged, target=target, weapon_melee=weapon_melee, weapon_ranged=weapon_ranged, minion_type=minion_type)

@advantage.route('/advantage/trait/select', methods=['POST'])
def advantage_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['trait'] 

	this = ['This Power']

	skills_query = db.session.query(Skill).order_by(Skill.name).all()
	skills = [{'id': 'x_skill', 'name': 'Variable Skill'}, {'id': 'all', 'name': 'All'}]
	for skill in skills_query:
		skills.append({'id': skill.name, 'name': skill.name})

	abilities_query = db.session.query(Ability).order_by(Ability.name).all()
	abilities = [{'id': 'x_ability', 'name': 'Variable Ability'}, {'id': 'all', 'name': 'All'}]
	for a in abilities_query:
		abilities.append({'id': a.name, 'name': a.name})

	defenses_query = db.session.query(Defense).order_by(Defense.name).all()
	defenses = [{'id': 'x_defense', 'name': 'Variable Defense'}, {'id': 'all', 'name': 'All'}]
	for d in defenses_query:
		defenses.append({'id': d.name, 'name': d.name})

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers_sorted = sorted(powers_raw)
	powers = [{'id': 'x_power', 'name': 'Variable Power'}, {'id': 'all', 'name': 'All'}]
	for p in powers_sorted:
		powers.append({'id': p, 'name': p})

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses_sorted = sorted(bonuses_raw)
	bonuses = [{'id': 'x_bonus', 'name': 'Variable Enhanced Skill'}, {'id': 'all', 'name': 'All'}]
	for b in bonuses_sorted:
		bonuses.append({'id': b, 'name': b})

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages_sorted = sorted(advantages_raw)
	advantages = [{'id': 'x_advantage', 'name': 'Variable Advantage'}, {'id': 'all', 'name': 'All'}]
	for a in advantages_sorted:
		advantages.append({'id': a, 'name': a})

	extras_query = db.session.query(Extra).order_by(Extra.name).all()
	extras = [{'id': 'x_extra', 'name': 'Variable Extra'}, {'id': 'all', 'name': 'All'}]
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
		body['options'] = [{'id': 'Trait', 'name': 'Trait'}]
	elif trait == 'immoveable':
		body['options'] = [{'id': 'Immoveable', 'name': 'Immoveable'}]
	else:
		body['success'] = False
		body['options'] = [{'id': '', 'name': ''}]


	print(body)
	return jsonify(body)


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


@advantage.route('/advantage/action/select', methods=['POST'])
def advantage_action_select():
	body = {}
	body['success'] = True

	action = request.get_json()['action'] 

	base = []
	actions = db.session.query(Action).all()
	for a in actions:
		base.append({'id': a.id, 'name': a.name})
		
	conflict = []
	conflicts = db.session.query(ConflictAction).order_by(ConflictAction.name).all()
	for c in conflicts:
		conflict.append({'id': c.id, 'name': c.name})


	if action == 'auto':
		body['options'] = [{'id': 'auto', 'name': 'Automatic'}]
	elif action == 'base':
		body['options'] = base
	elif action == 'conflict':
		body['options'] = conflict

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

	conflict = db_integer(conflict)
	conflict_range = db_integer(conflict_range)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	mod = integer(mod)
	conflict = integer(conflict)
	conflict_range = integer(conflict_range)
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/alt_check/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_alt_check(advantage_id):
	try:
		db.session.query(AdvAltCheck).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/benefit/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_benefit(advantage_id):
	try:
		db.session.query(Benefit).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	circ_range = db_integer(circ_range)
	conflict = db_integer(conflict)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	mod = integer(mod)
	rounds = integer(rounds)
	ranks = integer(ranks)
	circ_range = integer(circ_range)
	conflict = integer(conflict)
	
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
						null_override_trait_type = null_trait_type,
						null_override_trait = null_trait)

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
	
	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/circ/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_circ(advantage_id):
	try:
		db.session.query(AdvCirc).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	advantage_id = request.get_json()['advantage_id']
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


	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/combined/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_combined(advantage_id):
	try:
		db.session.query(AdvCombined).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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
	Created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	condition_type = request.get_json()['condition_type']
	condition = request.get_json()['condition']
	condition_null = request.get_json()['condition_null']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	damage_value = request.get_json()['damage_value']
	damage = request.get_json()['damage']

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	damage_value = integer(damage_value)

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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/condition/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_condition(advantage_id):
	try:
		db.session.query(AdvCondition).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	math_math = db_integer(math_math)
	level_type = db_integer(level_type)
	level = db_integer(level)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	dc = integer(dc)
	value_value = integer(value_value)
	math_value = integer(math_value)
	math_math = integer(math_math)
	level_type = integer(level_type)
	level = integer(level)
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/dc/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_dc(advantage_id):
	try:
		db.session.query(AdvDC).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
@advantage.route('/advantage/deg_mod/create', methods=['POST'])
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
	Created = request.get_json()['created']
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
	
	consequence = db_integer(consequence)
	level_type = db_integer(level_type)
	level = db_integer(level)
	measure_math = db_integer(measure_math)
	measure_rank = db_integer(measure_rank)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	value = integer(value)
	consequence_action = integer(consequence_action)
	consequence = integer(consequence)
	knowledge_count = integer(knowledge_count)
	level_type = integer(level_type)
	level = integer(level)
	circ_value = integer(circ_value)
	circ_turns = integer(circ_turns)
	measure_val1 = integer(measure_val1)
	measure_math = integer(measure_math)
	measure_value = integer(measure_value)
	measure_rank = integer(measure_rank)
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/deg_mod/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_deg_mod(advantage_id):
	try:
		db.session.query(AdvDegree).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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


	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	benefit_choice = integer(benefit_choice)
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

	db.session.close()
	return jsonify(body)


@advantage.route('/advantage/effort/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_effort(advantage_id):
	try:
		db.session.query(AdvEffort).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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

	attitude_type = db_integer(attitude_type)
	attitude_attitude = db_integer(attitude_attitude)
	resitable_check = db_integer(resitable_check)

	advantage_id = integer(advantage_id)
	points = integer(points)
	sacrifice_cost = integer(sacrifice_cost)
	attitude_type = integer(attitude_type)
	attitude_attitude = integer(attitude_attitude)
	resitable_check = integer(resitable_check)
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
							horde = horde,
							columns = columns,
							created = created,
							font = font)

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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/minion/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_minion(advantage_id):
	try:
		db.session.query(AdvMinion).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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
	Benefit = request.get_json()['benefit']
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

	environment = db_integer(environment)
	sense = db_integer(sense)
	mod_range = db_integer(mod_range)
	subsense = db_integer(subsense)
	cover = db_integer(cover)
	conceal = db_integer(Conceal)
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

	if emotion == 'other':	
		entry = Emotion(name=em0tion_other)
		db.session.add(entry)
		db.session.commit()
		em0tion = entry.id
		db.session.close()

	if environment == 'other':	
		entry = Environment(name=environment_other)
		db.session.add(entry)
		db.session.commit()
		environment = entry.id
		db.session.close()

	if creature == 'other':	
		entry = Creature(name=creature_other)
		db.session.add(entry)
		db.session.commit()
		creature = entry.id
		db.session.close()

	if profession == 'other':	
		entry = Job(name=profession_other)
		db.session.add(entry)
		db.session.commit()
		profession = entry.id
		db.session.close()
	error = errors['error']


	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	bonus = integer(bonus)
	environment = integer(environment)
	sense = integer(sense)
	mod_range = mod_range(mod_range)
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
	multiple = integer(multiple)
	multiple_count = integer(multiple_count)
	lasts = integer(lasts)

	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

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
	
	body = {}
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/modifiers/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_modifiers(advantage_id):
	try:
		db.session.query(AdvMod).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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

	player_check = db_integer(opponent_check)
	opponent_check = db_integer(opponent_check)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	mod = integer(mod)
	opponent_mod = integer(opponent_mod)
	player_check = integer(player_check)
	opponent_check = integer(opponent_check)



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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/opposed/delete/<advantage_id>', methods=['DELETE'])
def delete_post_opposed(advantage_id):
	try:
		db.session.query(AdvOpposed).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})


	
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
	condition1 = request.get_json()['conditioon1']
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

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition_cost = integer(condition_cost)
	equipment_points = integer(equipment_points)
	initiative_cost = integer(initiative_cost)
	twenty = integer(twenty)
	check_bonus = integer(check_bonus)
	check_cost = integer(check_cost)
	check_turns = integer(check_turns)
	benefit_choice = integer(benefit_choice)
	benefit_count = integer(benefit_count)
	benefit_cost = integer(benefit_cost)
	benefit_turns = integer(benefit_turns)
	ranks_gained = integer(ranks_gained)
	ranks_max = integer(ranks_max)
	ranks_lasts = integer(ranks_lasts)


	entry = AdvPoints(advantage_id = advantage_id,
							benefit = benefit,
							spend = spend,
							condition_cost = condition_cost,
							condition1 = conditioon1,
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/points/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_points(advantage_id):
	try:
		db.session.query(AdvPoints).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/resist/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_resist(advantage_id):
	try:
		db.session.query(AdvResist).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	cost = db_integer(cost)
	check = db_integer(check)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	rounds = integer(rounds)
	cost = integer(cost)
	check = integer(check)



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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/rounds/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_rounds(advantage_id):
	try:
		db.session.query(AdvRounds).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)


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
	Xells = []
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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/skill/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_skill(advantage_id):
	try:
		db.session.query(AdvSkill).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	units = db_integer(units)
	math = db_integer(units)
	check_type = db_integer(units)

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	value = integer(value)
	units = integer(units)
	time_value = integer(time_value)
	math = integer(math)
	dc = integer(dc)
	check_type = integer(check_type)
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
	table_id = 'timr'
	spot = table_id + '-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows	
	body['mods'] = []
	body['font'] = font
			
	body = adv_time_post(entry, body, cells)

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/time/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_time(advantage_id):
	try:
		db.session.query(AdvTime).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})

	
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

	advantage_id = integer(advantage_id)


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

	db.session.close()

	return jsonify(body)


@advantage.route('/advantage/variable/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_post_variable(advantage_id):
	try:
		db.session.query(AdvVariable).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': advantage_id})
