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
from power_errors import integer, extra_convert, power_save_errors, alt_check_post_errors, change_action_post_errors, character_post_errors, circ_post_errors, create_post_errors, damage_post_errors, dc_table_post_errors, defense_post_errors, degree_post_errors, degree_mod_post_errors, environment_post_errors, levels_post_errors, minion_post_errors, mod_post_errors, move_post_errors, opposed_post_errors, ranged_post_errors, resist_post_errors, resisted_by_post_errors, reverse_effect_post_errors, sense_post_errors, time_post_errors
from power_posts import delete_row, grid_columns, alt_check_post, change_action_post, character_post, circ_post, create_post, damage_post, dc_table_post, defense_post, degree_post, degree_mod_post, environment_post, levels_post, minion_post, mod_post, move_post, opposed_post, ranged_post, resist_post, resisted_by_post, reverse_effect_post, sense_post, time_post
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal

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

	traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_advantage', 'name': 'This Advantage'}, {'type': 'any', 'name': 'Any Trait'}, {'type': 'speed', 'name': 'Speed Rank'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}]

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	
	modifier_effect = [{'type': '', 'name': 'Affects'}, {'type': 'effect', 'name': 'Effect Modifier'}, {'type': 'attack', 'name': 'Attack Bonus'}, {'type': 'damage', 'name': 'Damage Bonus'}, {'type': 'defense', 'name': 'Active Defenses'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}]

	tools = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]

	bonus_type = [{'type': '', 'name': 'Up to Type'}, {'type': '', 'name': '+1 Per R'}]

	simultaneous = [{'type': '', 'name': 'Type'}, {'type': 'same', 'name': 'At Same Time'}, {'type': 'maintain', 'name': 'While Maintaining Previous'}, {'type': 'both', 'name': 'Either'}]

	multiple = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]

	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'descriptor', 'name': 'From Descriptor'}, {'type': 'condition', 'name': 'From Condition'}, {'type': 'override', 'name': 'Override Trait Circumstance'}]

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

	points = [{'type': '', 'name': 'Spend For'}, {'type': 'ranks', 'name': 'Gain Ranks'}, {'type': 'benefit', 'name': 'Benefit'}, {'type': 'check', 'name': 'Circumstance Modifier'}, {'type': 'equip', 'name': 'Equipment'}, {'type': 'condition', 'name': 'Change Condition'}]

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]

	which = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Value'}, {'type': 'low', 'name': 'Lower Value'}]

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}]

	check_type = [{'type': '', 'name': 'When'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]

	effort = [{'type': '', 'name': 'Effect'}, {'type': 'benefit', 'name': 'Benefit'}]

	rounds_end = [{'type': '', 'name': 'Ends'}, {'type': 'action', 'name': 'Stop Taking Action'}, {'type': 'resist', 'name': 'Successful Resistance'}, {'type': 'danger', 'name': 'Danger'}]

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, advantage_includes=advantage_includes, sidebar=sidebar, meta_content=meta_content, meta_name=meta_name,
							advantage_type=advantage_type, actions=actions, checks=checks, conditions=conditions, dc_type=dc_type, modifier_type=modifier_type, targets=targets, modifier_effect=modifier_effect,
							traits=traits, who_check=who_check, circ_type=circ_type, circ_null=circ_null, permanence=permanence, low_high=low_high, deg_mod_type=deg_mod_type, level_types=level_types, 
							value_type= value_type, maths=maths, measure_rank=measure_rank, condition_type=condition_type, updown=updown, knowledge=knowledge, specificity=specificity, negatives=negatives, 
							positives=positives, hundred=hundred, die=die, time_numbers=time_numbers, points=points, conflicts=conflicts, consequences=consequences, action_type=action_type, ranges=ranges,
							times=times, time_effect=time_effect, advantages=advantages, which=which, check_trigger=check_trigger, check_type=check_type, benefits=benefits, effort=effort, rounds_end=rounds_end,
							environments=environments, senses=senses, subsenses=subsenses, modifier_trigger=modifier_trigger, multiple=multiple, creatures=creatures, professions=professions, powers=powers,
							emotions=emotions, simultaneous=simultaneous, multiple_opposed=multiple_opposed, tools=tools, condition=condition, maneuvers=maneuvers, cover=cover, concealment=concealment)

@advantage.route('/advantage/trait/select', methods=['POST'])
def advantage_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['trait'] 

	this = ['This Power']

	skills_query = db.session.query(Skill).order_by(Skill.name).all()
	skills = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for skill in skills_query:
		skills.append({'id': skill.name, 'name': skill.name})

	abilities_query = db.session.query(Ability).order_by(Ability.name).all()
	abilities = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for a in abilities_query:
		abilities.append({'id': a.name, 'name': a.name})

	defenses_query = db.session.query(Defense).order_by(Defense.name).all()
	defenses = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for d in defenses_query:
		defenses.append({'id': d.name, 'name': d.name})

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers_sorted = sorted(powers_raw)
	powers = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for p in powers_sorted:
		powers.append({'id': p, 'name': p})

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses_sorted = sorted(bonuses_raw)
	bonuses = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for b in bonuses_sorted:
		bonuses.append({'id': b, 'name': b})

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages_sorted = sorted(advantages_raw)
	advantages = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
	for a in advantages_sorted:
		advantages.append({'id': a, 'name': a})

	extras_query = db.session.query(Extra).order_by(Extra.name).all()
	extras = [{'id': 'x', 'name': 'Variable'}, {'id': 'all', 'name': 'All'}]
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

@advantage.route('/power/modifiers/create', methods=['POST'])
def advantage_post_modifiers():

	environment = request.get_json()['environment']
	environment_other = request.get_json()['environment_other']
	creature = request.get_json()['creature']
	creature_other = request.get_json()['creature_other']
	profession = request.get_json()['profession']
	profession_other = request.get_json()['profession_other']
	em0tion = request.get_json()['em0tion']
	em0tion_other = request.get_json()['em0tion_other'] 

	if em0tion == 'other':	
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