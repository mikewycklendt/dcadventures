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
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSense, PowerTime 
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv
from power_errors import integer, extra_convert, alt_check_post_errors, change_action_post_errors, character_post_errors, circ_post_errors, create_post_errors, damage_post_errors, dc_table_post_errors, defense_post_errors, degree_post_errors, degree_mod_post_errors, environment_post_errors, levels_post_errors, minion_post_errors, mod_post_errors, move_post_errors, opposed_post_errors, ranged_post_errors, resist_post_errors, resisted_by_post_errors, reverse_effect_post_errors, sense_post_errors, time_post_errors
from power_posts import alt_check_post, change_action_post, character_post, circ_post, create_post, damage_post, dc_table_post, defense_post, degree_post, degree_mod_post, environment_post, levels_post, minion_post, mod_post, move_post, opposed_post, ranged_post, resist_post, resisted_by_post, reverse_effect_post, sense_post, time_post

load_dotenv()

import os

db_path = os.environ.get("db_path")

powers = Blueprint('powers', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

@powers.route('/power/create')
def power_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'power_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Power'
	stylesheets.append({"style": "/static/css/power_create.css"})

	power_includes = {'base_form': 'power_create/base_form.html', 'range': 'power_create/range.html', 'resisted_by': 'power_create/resisted_by.html', 'reverse_effect': 'power_create/reverse_effect.html', 'move': 'power_create/move.html', 'levels': 'power_create/levels.html', 'category': 'power_create/category.html', 'sense': 'power_create/sense.html', 'ranks': 'power_create/ranks.html', 'circ': 'power_create/circ.html', 'create': 'power_create/create.html', 'damage': 'power_create/damage.html', 'extras': 'power_create/extras.html', 'degree_mod': 'power_create/degree_mod.html', 'defense': 'power_create/defense.html', 'character': 'power_create/character.html', 'environment': 'power_create/environment.html', 'descriptors': 'power_create/descriptors.html', 'resist': 'power_create/resist.html', 'change_action': 'power_create/change_action.html', 'mod': 'power_create/mod.html', 'dc_table': 'power_create/dc_table.html', 'time': 'power_create/time.html', 'alt_check': 'power_create/alt_check.html', 'degree': 'power_create/degree.html', 'opposed': 'power_create/opposed.html', 'ranged': 'power_create/ranged.html', 'minion': 'power_create/minion.html'}
	
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

	power_type = [{'type': 'attack', 'name': 'Attack'}, 
					{'type': 'move', 'name': 'Movement'},  
					{'type': 'sense', 'name': 'Sensory'},
					{'type': 'control', 'name': 'Control'}, 
					{'type': 'defense', 'name': 'Defense'}, 
					{'type': 'general', 'name': 'General'}]

	action_type = [{'type': 'standard', 'name': 'Standard Action'},
					{'type': 'move', 'name': 'Move Action'},
					{'type': 'free', 'name': 'Free Action'},
					{'type': 'reaction', 'name': 'Reaction'},
					{'type': 'none', 'name': 'None'}]

	range_type = [{'type': 'personal', 'name': 'Personal'}, 
					{'type': 'close', 'name': 'Close'}, 
					{'type': 'ranged', 'name': 'Ranged'}, 
					{'type': 'perception', 'name': 'Perception'}, 
					{'type': 'rank', 'name': 'Variable'}]

	duration_type = [{'type': 'instant', 'name': 'Instant'}, 
						{'type': 'conc', 'name': 'Concentration'}, 
						{'type': 'sustained', 'name': 'Sustained'},
						{'type': 'cont', 'name': 'Continuous'},
						{'type': 'perm', 'name': 'Permanent'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Power Rank'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	distance = db.session.query(Unit).filter_by(type_id=3)

	checks = Check.query.all()

	actions = Action.query.all()

	conflicts = db.session.query(ConflictAction).order_by(ConflictAction.name).all()

	skills = Skill.query.all()

	abilities = Ability.query.all()

	defenses = Defense.query.all()

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages = sorted(advantages_raw)

	check_types = [{'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}]

	base_conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	effects = [{'type': 'condition', 'name': 'Condition'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'nullify', 'name': 'Nullifies Opponent Effect'}, {'type': 'trait', 'name': 'Weakened Trait'}, {'type': 'level', 'name': 'Level'}]

	dc_value = [{'type': '', 'name': 'DC Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]

	whens = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]

	maths = Math.query.all()

	times = db.session.query(Unit).filter_by(type_id=2)

	distances = db.session.query(Unit).filter_by(type_id=3)

	permanence = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	
	partners = [{'type': '', 'name': 'N/A'}, {'type': 'power', 'name': 'Same Power'}, {'type': 'device', 'name': 'Device'}, {'type': 'both', 'name': 'Power or Device'}, {'type': 'skill', 'name': 'Skill Check'}]

	senses = Sense.query.all()

	subsenses = SubSense.query.all()

	sense_type =  [{'type': '', 'name': 'Effect Type'}, {'type': 'height', 'name': 'Heightened'}, {'type': 'resist', 'name': 'Resistant'}]

	visual = db.session.query(SubSense).filter_by(sense_id=6)
	
	auditory = db.session.query(SubSense).filter_by(sense_id=7)

	olfactory = db.session.query(SubSense).filter_by(sense_id=8)

	tactile = db.session.query(SubSense).filter_by(sense_id=9)

	radio = db.session.query(SubSense).filter_by(sense_id=10)

	mental = db.session.query(SubSense).filter_by(sense_id=11)

	special = db.session.query(SubSense).filter_by(sense_id=12)

	damages = db.session.query(Descriptor).filter_by(damage=True).order_by(Descriptor.name).all()

	power_sense = ['Accurate', 'Acute', 'Analytical', 'Awareness', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision', 'Detect', 'Direction Sense', 'Distance Sense', 'Extended', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Ranged', 'Rapid', 'Time Sense', 'Tracking', 'Ultra-Hearing', 'Ultravision']

	circumstances = [{'type': '', 'name': 'N/A'}, {'type': 'gm', 'name': 'Set by GM'}, {'type': 'table', 'name': 'Circumstance Table'}]

	required = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	heightened = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	resistant = [{'type': '', 'name': 'Affects'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	value_bonus = [{'type': 'value', 'name': 'Value'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses = sorted(bonuses_raw)

	all_some = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]

	sense_time = [{'type': '', 'name': ''}, {'type': 'value', 'name': 'Value'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]

	sense_distance = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'unit', 'name': 'By Rank (Units)'}, {'type': 'rank', 'name': 'By Rank'}]

	darkness = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]

	determined = [{'type': '', 'name': 'Determined By'}, {'type': 'dc', 'name': 'DC'}, {'type': 'target', 'name': 'Target Trait'}, {'type': 'player', 'name': 'Player Trait'}]

	traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}]

	all_traits = [{'type': '', 'name': 'Trait Type'}, {'type': 'this', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'advantage', 'name': 'Advantage'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	object_damage = [{'type': '', 'name': 'Damage Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'effect', 'name': 'Effect Rank'}, {'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}, {'type': 'ability', 'name': 'Player Ability'}]

	solidity = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]

	visibility = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]

	against = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]

	moveable = [{'type': '', 'name': 'Moveable With'}, {'type': None, 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]

	complexity = Complex.query.all()

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'uncontrolled', 'name': 'Effect Uncontrolled'}, {'type': 'level', 'name': 'Level'}]

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	use_type = [{'type': '', 'name': 'Use Type'}, {'type': 'add', 'name': 'Add to'}, {'type': 'replace', 'name': 'In Place of'}, {'type': 'gm', 'name': 'GM Choice'}]

	outcome = [{'type': '', 'name': ''}, {'type': '<', 'name': 'Lower'}, {'type': '>', 'name': 'Higher'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}]

	ranges = Range.query.all()

	bonus_type = [{'type': 'flat', 'name': 'Flat'}, {'type': 'rank', 'name': 'Per Rank'}]

	limited = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]

	emotions = Emotion.query.all()

	temp_type = [{'type': '', 'name': 'Type'}, {'type': 'all', 'name': 'All'}, {'type': 'cold', 'name': 'Cold'}, {'type': 'heat', 'name': 'Heat'}, {'type': 'pressure', 'name': 'High Pressure'}, {'type': 'radiation', 'name': 'Radiation'}, {'type': 'vaccum', 'name': 'Vaccuum'}]

	extremity = [{'type': '', 'name': 'Extremity'}, {'type': 'intense', 'name': 'Intense'}, {'type': 'extreme', 'name': 'Extreme'}]

	nature = [{'type': '', 'name': 'Nature'}, {'type': 'ice', 'name': 'Ice'}, {'type': 'rain', 'name': 'Rain'}, {'type': 'snow', 'name': 'Snow'}, {'type': 'wind', 'name': 'Wind'}, {'type': 'other', 'name': 'Other'}]

	grounds = Ground.query.all()

	directions = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]

	move_objects = [{'type': '', 'name': 'Direction'}, {'type': 'all', 'name': 'All Directions'}, {'type': 'vertical', 'name': 'Up and Down'}, {'type': 'horizontal', 'name': 'Towards and Away'}, {'type': 'attract', 'name': 'Attraction'}, {'type': 'repel', 'name': 'Repulsion'}]

	character = [{'type': '', 'name': 'Changed Trait'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'intim', 'name': 'Intimidation'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	descriptors = Descriptor.query.order_by(Descriptor.name).all()

	origins = Origin.query.order_by(Origin.name).all()

	sources = Source.query.order_by(Source.name).all()

	medium = Medium.query.order_by(Medium.name).all()

	mediums = MediumType.query.order_by(MediumType.name).all()

	materials = db.session.query(MediumSubType).filter_by(medium_type=1).order_by(MediumSubType.name)
	
	energies = db.session.query(MediumSubType).filter_by(medium_type=2).order_by(MediumSubType.name)

	descriptor_type = [{'type': '', 'name': 'Applies To:'}, {'type': 'power', 'name': 'This Power'}, {'type': 'effect', 'name': 'Power Effect'}]

	resistance_type = [{'type': '', 'name': 'Applies to'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'trait', 'name': 'Check Type'}, {'type': 'harmed', 'name': 'Subject Harmed'}]

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]

	limited_type = [{'type': '', 'name': 'Limited Against'}, {'type': 'task_type', 'name': 'Task Type'}, {'type': 'task', 'name': 'All tasks but One'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'subjects', 'name': 'Subjects'}, {'type': 'language', 'name': 'Different Language'}, {'type': 'extra', 'name': 'Extra Effect'}, {'type': 'degree', 'name': 'Degree of Success'}, {'type': 'sense', 'name': 'Sense'},  {'type': 'range', 'name': 'Range'}, {'type': 'source', 'name': 'Requires Descriptor'}, {'type': 'other', 'name': 'Other'}, {'type': 'level', 'name': 'Level'}]

	possess = [{'type': '', 'name': 'Possession'}, {'type': 'possess', 'name': 'While Possessing'}, {'type': 'oppose', 'name': 'While Opposing'}]

	game_rule = [{'type': '', 'name': 'Game Rule'}, {'type': 'critical', 'name': 'Critical Hits'}, {'type': 'suffocate', 'name': 'Suffocation'}, {'type': 'starve', 'name': 'Starvation'}, {'type': 'thirst', 'name': 'Thirst'}, {'type': 'sleep', 'name': 'Need for Sleep'}, {'type': 'fall', 'name': 'Falling'}]

	damage = Damage.query.order_by(Damage.name).all()

	insub = [{'type': '', 'name': 'Insubstantial Type'}, {'type': 'fluid', 'name': 'Fluid'}, {'type': 'gas', 'name': 'Gaseous'}, {'type': 'energy', 'name': 'Energy'}, {'type': 'incorp', 'name': 'Incorporeal'}]

	openings = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]

	spend = [{'type': '', 'name': 'Effect'}, {'type': 'reroll', 'name': 'Re-roll'}]

	result = [{'type': '', 'name': 'Result'}, {'type': 'high', 'name': 'Higher'}, {'type': 'low', 'name': 'Lower'}]

	side_effects = [{'type': '', 'name': 'Side Effect'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'level', 'name': 'Level'}, {'type': 'other', 'name': 'Other'}]

	check_type = [{'type': '', 'name': 'Check Type'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]

	null_type = [{'type': '', 'name': 'Effect'}, {'type': 'null', 'name': 'Nullifies Effect'}, {'type': 'mod', 'name': 'Modifier to Check'}]

	who_check = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]

	dimensions = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]

	environment_immunity = [{'type': '', 'name': 'Immune From'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'condition', 'name': 'Condition'}]

	environment = [{'type': '', 'name': 'Environment Type'}, {'type': 'underwater', 'name': 'Underwater'}, {'type': 'gravity', 'name': 'Zero Gravity'}, {'type': 'mountains', 'name': 'Mountains'}, {'type': 'jungle', 'name': 'Jungle'}, {'type': 'desert', 'name': 'Desert'}, {'type': 'volcano', 'name': 'Volcano'}, {'type': 'other', 'name': 'Other'}]

	immunity_type = [{'type': '', 'name': 'Immune From'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'damage', 'name': 'Damage Type'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'rule', 'name': 'Game Rule'}]

	circ_null = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'descriptor', 'name': 'From Descriptor'}, {'type': 'condition', 'name': 'From Condition'}]

	travel = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]

	space = [{'type': '', 'name': 'Space Travel Type'}, {'type': 'solar', 'name': 'Planets in Solar System'}, {'type': 'star', 'name': 'Other Star Systems'}, {'type': 'galaxy', 'name': 'Other Galaxies'}]

	time_travel = [{'type': '', 'name': 'Time Travel Type'}, {'type': 'Fixed', 'name': 'Fixed Point in Time'}, {'type': 'past', 'name': 'Any Point in Past'}, {'type': 'future', 'name': 'Any Point in Future'}, {'type': 'timeline', 'name': 'Alternate Timeline'}, {'type': 'any', 'name': 'Any Point in time'}  ]

	aquatic = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}]

	task_type = [{'type': '', 'name': 'Does Not Work On'}, {'type': 'physical', 'name': 'Physical Tasks'}, {'type': 'mental', 'name': 'Mental Tasks'}]

	ranged_type = [{'type': '', 'name': 'Ranged Type'}, {'type': 'flat_units', 'name': 'Flat Units'}, {'type': 'distance_rank', 'name': 'Flat Distance Rank'}, {'type': 'flat_rank_units', 'name': 'Flat Units By Rank'}, {'type': 'flat_rank_distance', 'name': 'Flat Distance Rank By Rank'}, {'type': 'units_rank', 'name': 'Units Per Rank'}, {'type': 'rank_rank', 'name': 'Distance Rank Per Rank'}, {'type': 'effect_mod', 'name': 'Effect Rank Modifier'}, {'type': 'trait_mod', 'name': 'Trait Rank Modifier'}, {'type': 'distance_mod', 'name': 'Distance Rank Modifier'}, {'type': 'check', 'name': 'Check Result'}]

	cover = [{'type': '', 'name': 'Cover Type'}, {'type': 'partial', 'name': 'Partial Cover'}, {'type': 'total', 'name': 'Total Cover'}]

	minion_type = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]

	minion_attitude = [{'type': '', 'name': 'Minion Attitude'}, {'type': 'none', 'name': 'Cooperative'}, {'type': 'Indifferent', 'name': 'Indifferent'}, {'type': 'Unfriendly', 'name': 'Unfriendly'}]

	teleport_change = [{'type': '', 'name': 'Can Change'}, {'type': 'direction', 'name': 'Direction'}, {'type': 'velocity', 'name': 'Velocity'}]

	teleport = [{'type': '', 'name': 'Type'}, {'type': 'know', 'name': 'Know Destination'}, {'type': 'any', 'name': 'Any Destination'}]

	transform = [{'type': '', 'name': 'Transform Type'}, {'type': 'one', 'name': 'One Substance to One Substance'}, {'type': 'result', 'name': 'Group to Single Result'}, {'type': 'broad', 'name': 'Broad Group to Broad Group'}, {'type': 'any', 'name': 'Any Material into Anything Else'}]

	weaken = [{'type': '', 'name': 'Weaken Type'}, {'type': 'trait', 'name': 'Specific'}, {'type': 'type', 'name': 'Broad Trait'}, {'type': 'descriptor', 'name': 'Broad Descriptor'}]

	conceal_type = [{'type': 'reduce', 'name': 'Reduce'}, {'type': 'eliminate', 'name': 'Eliminate'}]

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
											materials=materials, energies=energies, descriptor_type=descriptor_type, resistance_type=resistance_type, bonus_type=bonus_type, time_effect=time_effect, 
											limited_type=limited_type, possess=possess, hundred=hundred, game_rule=game_rule, damage=damage, insub=insub, openings=openings, spend=spend, result=result, 
											all_traits=all_traits, side_effects=side_effects, check_type=check_type, null_type=null_type, damages=damages, conflicts=conflicts, move_objects=move_objects,
											dimensions=dimensions, environment=environment, environment_immunity=environment_immunity, immunity_type=immunity_type, circ_null=circ_null, space=space,
											travel=travel, time_travel=time_travel, aquatic=aquatic, task_type=task_type, distances=distances, ranged_type=ranged_type, who_check=who_check, cover=cover,
											minion_type=minion_type, minion_attitude=minion_attitude, teleport=teleport, teleport_change=teleport_change, transform=transform, weaken=weaken, measure_rank=measure_rank, 
											conceal_type=conceal_type)

@powers.route('/power/trait/select', methods=['POST'])
def power_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['trait'] 

	this = ['This Power']

	skills_query = Skill.query.all()
	skills_raw = []
	for skill in skills_query:
		skills_raw.append(skill.name)
	skills = sorted(skills_raw)

	abilities_query = Ability.query.all()
	abilities_raw = []
	for ability in abilities_query:
		abilities_raw.append(ability.name)
	abilities = sorted(abilities_raw)

	defenses_query = Defense.query.all()
	defenses_raw = []
	for defense in defenses_query:
		defenses_raw.append(defense.name)
	defenses = sorted(defenses_raw)

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses = sorted(bonuses_raw)

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages = sorted(advantages_raw)
	
	extras_query = db.session.query(Extra).order_by(Extra.name).all()
	extras = []
	for extra in extras_query:
		extras.append(extra.name)

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
	else:
		body['success'] = False
		body['options'] = ['']

	print(body)
	return jsonify(body)

@powers.route('/power/descriptor/select', methods=['POST'])
def power_descriptor_select():
	body = {}
	body['success'] = True

	results = request.get_json()
	print('\n\n\n')
	print('descriptor resiults:')
	print(results)

	origin = request.get_json()['origin']
	source = request.get_json()['source']
	medium_type = request.get_json()['medium_type']
	medium_subtype = request.get_json()['medium_subtype']
	medium = request.get_json()['medium']

	options_raw = []
	options = []

	try:
		descriptors_query = Descriptor.query.all()
	except:
		print('\n\n\nERROR\n\n\n')
	descriptors_raw = [descriptor.format() for descriptor in descriptors_query]
	descriptors = []

	print('\n\ndescriptors raw')
	for descriptor in descriptors_raw:
		descriptors.append(descriptor)
		

	print('\n\n')
	print(len(descriptors))

	max_d = len(descriptors)
	print(descriptors[0])
	i = 0

	print('origin id: '+ str(origin))
	if origin != 'all' and origin != 'new' and origin != '':
		origin = int(origin)
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('origin'))
			if descriptors[i].get('origin') == origin:
				print(descriptors[i])
			else:
				del descriptors[i]
	elif origin == 'all':
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('origin'))
			if descriptors[i].get('origin') is not None:
				print(descriptors[i])
			else:
				del descriptors[i]

	for descriptor in descriptors:
		print(descriptor)

	print('\n\n')	

	if source != 'all' and source != 'new' and source != '':
		des_id = int(source)
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('source'))
			if descriptors[i].get('source') == des_id:
				print(descriptors[i])
			else:
				del descriptors[i]
	elif source == 'all':
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('source'))
			if descriptors[i].get('source') is not None:
				print(descriptors[i])
			else:
				del descriptors[i]

	if medium_type != 'all' and medium_type != 'new' and medium_type != '':
		des_id = int(medium_type)
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium_type'))
			if descriptors[i].get('medium_type') == des_id:
				print(descriptors[i])
			else:
				del descriptors[i]
	elif medium_type == 'all':
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium_type'))
			if descriptors[i].get('medium_type') is not None:
				print(descriptors[i])
			else:
				del descriptors[i]

	if medium_subtype != 'all' and medium_subtype != 'new' and medium_subtype != '':
		des_id = int(medium_subtype)
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium_subtype'))
			if descriptors[i].get('medium_subtype') == des_id:
				print(descriptors[i])
			else:
				del descriptors[i]
	elif medium_subtype == 'all':
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium_subtype'))
			if descriptors[i].get('medium_subtype') is not None:
				print(descriptors[i])
			else:
				del descriptors[i]

	if medium != 'all' and medium != 'new' and medium != '':
		des_id = int(medium)
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium'))
			if descriptors[i].get('medium') == des_id:
				print(descriptors[i])
			else:
				del descriptors[i]
	elif medium == 'all':
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('medium'))
			if descriptors[i].get('medium') is not None:
				print(descriptors[i])
			else:
				del descriptors[i]

	print('\n\n')
	for descriptor in descriptors:
		print('results:')
		print(descriptor)


	for descriptor in descriptors:
		options.append({'id': descriptor['id'], 'name': descriptor['name']})

	body['options'] = options

	print('\n\n\n')
	print('options: ')
	for o in options:
		print(o)

	print(body)
	return jsonify(body)

@powers.route('/power/medium/subtype/select', methods=['POST'])
def power_medium_subtype_select():
	body = {}
	body['success'] = True

	medium_type_id = request.get_json()['medium_type']

	print('id ' + medium_type_id)

	try:
		medium_type = db.session.query(MediumType).filter_by(id=medium_type_id).one()
		medium_subtypes = db.session.query(MediumSubType).filter_by(medium_type=medium_type_id).order_by(MediumSubType.name).all()
		mediums = db.session.query(Medium).filter_by(medium_type=medium_type_id).order_by(Medium.name).all()
		
		all_medium_type = 'Any ' + medium_type.name

		title = medium_type.name + ' Type'

		des_title = 'New ' + medium_type.name + ' Type Description'

		medium_type_medium = medium_type.name + ' Mediums'

		options = []

		options_medium = []
		
		options.append({'id': '', 'name': medium_type.name})
		options.append({'id': 'all', 'name': all_medium_type})
		options.append({'id': 'new', 'name': 'New'})

		options_medium.append({'id': '', 'name': medium_type.name})
		options_medium.append({'id': 'all', 'name': all_medium_type})
		options_medium.append({'id': 'new', 'name': 'New'})

		for subtype in medium_subtypes:
			options.append({'id': subtype.id, 'name': subtype.name})

		for medium in mediums:
			options_medium.append({'id': medium.id, 'name': medium.name})

		body['options'] = options
		body['options_medium'] = options_medium
		body['title'] = title
		body['des_title'] = des_title

	except:
		body['success'] = False
		body['options'] = 'no results'

	print(body)
	return jsonify(body)

@powers.route('/sense/subsense/select', methods=['POST'])
def get_subsense_select():
	body = {}
	body['success'] = True

	sense_id_str = request.get_json()['sense_id']
	sense_id = int(sense_id_str)

	try:
		sense = db.session.query(Sense).filter_by(id=sense_id).one()
		subsenses = db.session.query(SubSense).filter_by(sense_id=sense_id).order_by(SubSense.name).all()
		
		any_sense = 'Any ' + sense.name
		all_sense = 'All ' + sense.name

		options = []

		options.append({'id': '', 'name': any_sense})
		options.append({'id': 0, 'name': all_sense})

		for subsense in subsenses:
			options.append({'id': subsense.id, 'name': subsense.name})

		body['options'] = options
	except:
		body['success'] = False
		body['options'] = 'no results'

	print(body)
	return jsonify(body)

@powers.route('/power/medium/select', methods=['POST'])
def power_medium_select():
	body = {}
	body['success'] = True
	
	medium_subtype = request.get_json()['medium_subtype']
	options = []

	print('id ' + medium_subtype)

	if medium_subtype != '' and medium_subtype != 'all' and medium_subtype != 'new':
		try:
			subtype = db.session.query(MediumSubType).filter_by(id=medium_subtype).one()
			mediums = db.session.query(Medium).filter_by(medium_subtype=medium_subtype).order_by(Medium.name).all()
			
			all_subtype = 'Any ' + subtype.name

			options.append({'id': '', 'name': subtype.name})
			options.append({'id': 'all', 'name': all_subtype})
			options.append({'id': 'new', 'name': 'New'})

			for medium in mediums:
				options.append({'id': medium.id, 'name': medium.name})

		except:
			db.session.rollback()
			options.append({'id': '', 'name': 'Medium'})
		finally:
			db.session.close()
	else:
		options.append({'id': '', 'name': 'Medium'})

	body['options'] = options
	print(body)
	return jsonify(body)

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
		edit_power = db.session.query(Power).filter(Power.id == edit_power).one()
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


@powers.route('/power/extra/create', methods=['POST'])
def post_extra_create():
	body = {}
	body['success'] = True
	error = False
	error_msgs = []
	

	name = request.get_json()['name'] 
	power_id = request.get_json()['power_id']
	cost = request.get_json()['cost']
	ranks = request.get_json()['ranks'] 
	des = request.get_json()['des'] 
	inherit = request.get_json()['inherit']

	power = db.session.query(Extra).filter(Extra.name == name).first()

	if power is not None:
		error = True
		body['success'] = False
		error_msgs.append('You have already created an extra with that name with that name')
		body['error'] = error_msgs

	if error:
		return jsonify(body)

	try:
		power = Extra(power_id=power_id, name=name, cost=cost, ranks=ranks, des=des, inherit=inherit)
		db.session.add(power)
		db.session.commit()

		body['id'] = power.id
		body['name'] = power.name
		body['power_id'] = power.power_id
		body['cost'] = power.cost
		body['ranks'] = power.ranks
		body['des'] = power.des
		body['inherit'] = power.inherit

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

@powers.route('/power/extra/delete/<power_id>', methods=['DELETE'])
def delete_extra(power_id):
	try:
		db.session.query(Extra).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		return jsonify({'success': True})

@powers.route('/descriptor/create', methods=['POST'])
def post_descriptor(): 
	body = {}
	body['success'] = True
	body['descriptor'] = False
	body['add_select'] = False
	new_selects = []
	error = False
	error_msgs = []
	descriptor = {}

	results = request.get_json()

	print('\n\n\nCreate Descriptor input:\n')
	print(results)

	origin = request.get_json()['origin']
	origin_name = request.get_json()['origin_name']
	origin_des = request.get_json()['origin_des']
	source = request.get_json()['source']
	source_name = request.get_json()['source_name']
	source_des = request.get_json()['source_des']
	medium_type = request.get_json()['medium_type']
	medium_subtype = request.get_json()['medium_subtype']
	medium_subtype_name = request.get_json()['medium_subtype_name']
	medium_subtype_des = request.get_json()['medium_subtype_des']
	medium = request.get_json()['medium']
	medium_name = request.get_json()['medium_name']
	medium_des = request.get_json()['medium_des']
	descriptor_field = request.get_json()['descriptor']
	descriptor_name = request.get_json()['descriptor_name']
	descriptor_result = request.get_json()['descriptor_result']
	descriptor_type = request.get_json()['descriptor_type']
	damage = request.get_json()['damage']
	power_id = request.get_json()['power_id']

	name = ''
	one_medium_name = ''

	if descriptor_type == 'power':
		is_descriptor = True
		body['type'] = 'power'
	elif descriptor_type == 'effect':
		is_descriptor = False
		body['type'] = 'effect'
	else:
		error = True
		body['success'] = False
		error_msgs.append('You must specify whether or not this descriptor is assigned to this power.')
		body['error'] = error_msgs

	if power_id == '':
		error = True
		body['success'] = False
		error_msgs.append('You Must create a power first ')
		body['error'] = error_msgs

	if error:
		print('body: ')
		print(body)
		errors = body['error']
		for err in errors:
			print(err)
		return jsonify(body)

	if origin == 'new':
		process = True
		try:
			origin_check = db.session.query(Origin).filter(Origin.name == origin_name).first()
			if origin_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already an origin with that name')
				body['error'] = error_msgs
			if process:
				entry = Origin(name=origin_name, description=origin_des)
				db.session.add(entry)
				db.session.commit()
				origin_id = entry.id
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_origin', 'id': entry.id, 'name': entry.name})
				if name == '':
					name = name + entry.name
				else:
					name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that origin')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif origin == '':
		origin_id = None
	else:
		try:
			print('\n\norigin')
			print(origin)
			print(type(origin))			
			input_id = int(origin)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Origin).filter(Origin.id == input_id).one()
			origin_id = entry.id
			if name == '':	
				name = name + entry.name
			else:
				name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that origin')
			db.session.rollback()
		
	if source == 'new':
		process = True
		try:
			source_check = db.session.query(Source).filter(Source.name == source_name).first()
			if source_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a source with that name')
				body['error'] = error_msgs
			if process:
				entry = Source(name=source_name, description=source_des)
				db.session.add(entry)
				db.session.commit()
				source_id = entry.id
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_source', 'id': entry.id, 'name': entry.name})
				if name == '':
					name = name + entry.name
				else:
					name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that source')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif source == '':
		source_id = None
	else:
		try:
			print('\n\nsource')
			print(source)
			print(type(source))	
			input_id = int(source)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Source).filter(Source.id == input_id).one()
			source_id = entry.id
			if name == '':
				name = name + entry.name
			else:
				name = name + ', ' + entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that source')
			db.session.rollback()
		
	if medium_type != '':
		try:
			print('\n\nsource')
			print(medium_type)
			print(type(medium_type))	
			input_id = int(medium_type)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(MediumType).filter(MediumType.id == input_id).one()
			medium_type_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium type')
			db.session.rollback()
	else:
		medium_type_id = None

	if medium_subtype == 'new':
		process = True
		try:
			medium_subtype_check = db.session.query(MediumSubType).filter(MediumSubType.name == medium_subtype_name).first()
			if medium_subtype_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a medium subtype with that name')
				body['error'] = error_msgs
			if process:
				entry = MediumSubType(name=medium_subtype_name, medium_type=medium_type_id, description=medium_subtype_des)
				db.session.add(entry)
				db.session.commit()
				medium_subtype_id = entry.id
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_medium_subtype', 'id': entry.id, 'name': entry.name})
				one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium subtype')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif medium_subtype == '':
		medium_subtype_id = None
	elif medium_subtype == 'all':
		medium_subtype_id = None
	else:
		try:
			print('\n\nmedium_subtype')
			print(medium_subtype)
			print(type(medium_subtype))	
			input_id = int(medium_subtype)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(MediumSubType).filter(MediumSubType.id == input_id).one()
			medium_subtype_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium subtype')
			db.session.rollback()

	if medium == 'new':
		process = True
		try:
			medium_check = db.session.query(Medium).filter(Medium.name == medium_name).first()
			if medium_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a medium with that name')
				body['error'] = error_msgs
			if process:
				entry = Medium(name=medium_name, medium_type=medium_type_id, medium_subtype=medium_subtype_id, description=medium_des)
				db.session.add(entry)
				db.session.commit()
				medium_id = entry.id
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_medium', 'id': entry.id, 'name': entry.name})
				one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif medium == '':
		medium_id = None
	elif medium == 'all':
		medium_id = None
	else:
		try:
			print('\n\nmedium')
			print(medium)
			print(type(medium))	
			input_id = int(medium)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Medium).filter(Medium.id == input_id).one()
			medium_id = entry.id
			one_medium_name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that medium')
			body['error'] = error_msgs
			db.session.rollback()

	if one_medium_name != '':
		if name == '':
			name = name + one_medium_name
		else:
			name = name + ', ' + one_medium_name

	if descriptor_field == 'new':
		process = True
		try:
			descriptor_check = db.session.query(Descriptor).filter(Descriptor.name == descriptor_name).first()
			if descriptor_check is not None:
				process = False
				error = True
				body['success'] = False
				error_msgs.append('There is already a descriptor with that name')
				body['error'] = error_msgs
			if process:
				entry = Descriptor(name=descriptor_name, origin=origin_id, source=source_id, medium_type=medium_type_id, medium_subtype=medium_subtype_id, medium=medium_id, result=descriptor_result, damage=damage)
				db.session.add(entry)
				db.session.commit()
				descriptor_id = entry.id
				body['descriptor'] = True
				body['add_select'] = True
				new_selects.append({'select': 'descriptor_field', 'id': entry.id, 'name': entry.name})
				name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that descriptor')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()
	elif descriptor_field == '':
		descriptor_id = None
	elif descriptor_field == 'all':
		descriptor_id = None
	else:
		try:
			print('\n\ndescriptor_field')
			print(descriptor_field)
			print(type(descriptor_field))	
			input_id = int(descriptor_field)
			print(input_id)
			print(type(input_id))
			entry = db.session.query(Descriptor).filter(Descriptor.id == input_id).one()
			descriptor_id = entry.id
			body['descriptor'] = True
			name = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not find that descriptor')
			body['error'] = error_msgs
			db.session.rollback()

	if error:
		body['error'] = error_msgs
		print('body: ')
		print(body)
		errors = body['error']
		for err in errors:
			print(err)
		return jsonify(body)

	try:
		power_id = int(power_id)
		power_descriptor = PowerDes(name=name, power_id=power_id, des_id=descriptor_id, origin=origin_id, source=source_id, medium=medium_id, medium_type=medium_type_id, medium_subtype=medium_subtype_id, descriptor=is_descriptor, damage=damage)
		db.session.add(power_descriptor)
		db.session.commit()
	
		body['id'] = power_descriptor.id	
		body['name'] = power_descriptor.name
		body['selects'] = new_selects
	except:
		error = True
		body['success'] = False
		error_msgs.append('Could Not find that descriptor')
		body['error'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()

	db.session.close()
	print('\n\nbody: \n')
	print(body)
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


@powers.route('/power/alt_check/create', methods=['POST'])
def power_post_alt_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = alt_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	check_type = request.get_json()['check_type']
	mod = request.get_json()['mod']
	circumstance = request.get_json()['circumstance']
	when = request.get_json()['when']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	check_type = integer(check_type)
	mod = integer(mod)


	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']

	entry = PowerAltCheck(power_id = power_id,
							extra_id = extra_id,
							check_type = check_type,
							mod = mod,
							circumstance = circumstance,
							when = when,
							trait_type = trait_type,
							trait = trait)

	body = alt_check_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	action = integer(action)
	mod = integer(mod)

	entry = PowerAction(power_id = power_id,
						extra_id = extra_id,
						action = action,
						mod = mod,
						objects =objects, 
						circumstance = circumstance)

	body = change_action_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	value = integer(value)
	increase = integer(increase)
	weaken_descriptor = integer(weaken_descriptor)
	reduced_value = integer(reduced_value)
	carry_capacity = integer(carry_capacity)
	points_value = integer(points_value)
	points_descriptor = integer(points_descriptor)
	cost = integer(cost)
	ranks = integer(ranks)	 

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

	body = character_post(entry)
	return jsonify(body)

@powers.route('/power/circ/create', methods=['POST'])
def power_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = circ_post_errors(data)

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
	description = request.get_json()['description']
	circ_type = request.get_json()['circ_type']
	circ_range = request.get_json()['circ_range']
	check_who = request.get_json()['check_who']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	null_type = request.get_json()['null_type']
	null_condition = request.get_json()['null_condition']
	null_descriptor = request.get_json()['null_descriptor']
	null_trait_type = request.get_json()['null_trait_type']
	null_trait = request.get_json()['null_trait']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	mod = integer(mod)
	rounds = integer(rounds)
	circ_range = integer(circ_range)
	null_descriptor = integer(null_descriptor)

	entry = PowerCirc(power_id = power_id,
						extra_id = extra_id,
						target = target,
						mod = mod,
						rounds = rounds,
						description = description,
						circ_type = circ_type,
						circ_range = circ_range,
						check_who = check_who,
						check_trait_type = check_trait_type,
						check_trait = check_trait,
						null_type = null_type,
						null_condition = null_condition,
						null_descriptor = null_descriptor,
						null_trait_type = null_trait_type,
						null_trait = null_trait)

	body = circ_post(entry)
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
	move_player_trait = request.get_json()['move_player_trait']
	move_opponent_check = request.get_json()['move_opponent_check']
	move_opponent_ability = request.get_json()['move_opponent_ability']
	move_opponent_rank = request.get_json()['move_opponent_rank']
	trap_type = request.get_json()['trap_type']
	trap_dc = request.get_json()['trap_dc']
	trap_trait_type = request.get_json()['trap_trait_type']
	trap_trait = request.get_json()['trap_trait']
	trap_resist_check = request.get_json()['trap_resist_check']
	trap_resist_trait = request.get_json()['trap_resist_trait']
	trap_resist_dc = request.get_json()['trap_resist_dc']
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	complexity = integer(complexity)
	volume = integer(volume)
	toughness = integer(toughness)
	mass = integer(mass)
	transform_start_mass = integer(transform_start_mass)
	transfom_mass = integer(transfom_mass)
	transform_start_descriptor = integer(transform_start_descriptor)
	transform_end_descriptor = integer(transform_end_descriptor)
	move_opponent_ability = integer(move_opponent_ability)
	move_opponent_rank = integer(move_opponent_rank)
	trap_dc = integer(trap_dc)
	trap_resist_dc = integer(trap_resist_dc)
	ranged_dc = integer(ranged_dc)
	ranged_damage_value = integer(ranged_damage_value)
	weapon_mod = integer(weapon_mod)
	weapon_damage = intege(weapon_damage)
	support_strength = integer(support_strength)
	support_action = integer(support_action)
	support_action_rounds = integer(support_action_rounds)
	support_effort = integer(support_effort)
	support_effort_rounds = integer(support_effort_rounds)
	cost = integer(cost)
	ranks = integer(ranks)

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
						move_player_trait = move_player_trait,
						move_opponent_check = move_opponent_check,
						move_opponent_ability = move_opponent_ability,
						move_opponent_rank = move_opponent_rank,
						trap_type = trap_type,
						trap_dc = trap_dc,
						trap_trait_type = trap_trait_type,
						trap_trait = trap_trait,
						trap_resist_check = trap_resist_check,
						trap_resist_trait = trap_resist_check,
						trap_resist_dc = trap_resist_dc,
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

	body = create_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	mod = integer(mod)
	damage_type = integer(damage_type)
	descriptor = integer(descriptor)


	entry = PowerDamage(power_id = power_id,
						extra_id = extra_id,
						trait_type = trait_type,
						trait = trait,
						mod = mod,
						strength = strength,
						damage_type = damage_type,
						descriptor = descriptor)

	body = damage_post(entry)
	return jsonify(body)


@powers.route('/power/dc_table/create', methods=['POST'])
def power_post_dc_table():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = dc_table_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	dc = request.get_json()['dc']
	description = request.get_json()['description']
	value = request.get_json()['value']
	math_value = request.get_json()['math_value']
	math = request.get_json()['math']
	math_trait_type = request.get_json()['math_trait_type']
	math_trait = request.get_json()['math_trait']
	descriptor_check = request.get_json()['descriptor_check']
	condition = request.get_json()['condition']
	keyword_check = request.get_json()['keyword_check']
	check_type = request.get_json()['check_type']
	descriptor = request.get_json()['descriptor']
	descriptor_possess = request.get_json()['descriptor_possess']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_mod = request.get_json()['check_mod']
	levels = request.get_json()['levels']
	level = request.get_json()['level']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	value = integer(value)
	math_value = integer(math_value)
	math = integer(math)
	descriptor = integer(descriptor)
	check_mod = integer(check_mod)
	level = integer(level)


	entry = PowerDC(power_id = power_id,
					extra_id = extra_id,
					target = target,
					dc = dc,
					description = description,
					value = value,
					math_value = math_value,
					math = math,
					math_trait_type = math_trait_type,
					math_trait = math_trait,
					descriptor_check = descriptor_check,
					condition = condition,
					keyword_check = keyword_check,
					check_type = check_type,
					descriptor = descriptor,
					descriptor_possess = descriptor_possess,
					condition1 = condition1,
					condition2 = condition2,
					keyword = keyword,
					check_trait_type = check_trait_type,
					check_trait = check_trait,
					check_mod = check_mod,
					levels = levels,
					level = level)

	body = dc_table_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	mod = integer(mod)
	roll = integer(roll)
	reflect_action = integer(reflect_action)
	reflect_check = integer(reflect_check)
	reflect_dc = integer(reflect_dc)
	immunity_descriptor = integer(immunity_descriptor)
	immunity_damage = integer(immunity_damage)

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

	body = defense_post(entry)
	return jsonify(body)


@powers.route('/power/degree_mod/create', methods=['POST'])
def power_post_degree_mod():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = degree_mod_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	value = request.get_json()['value']
	deg_type = request.get_json()['deg_type']
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
	deg_condition_type = request.get_json()['deg_condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	nullify = request.get_json()['nullify']
	cumulative = request.get_json()['cumulative']
	linked = request.get_json()['linked']
	level = request.get_json()['level']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	value = integer(value)
	circ_value = integer(circ_value)
	circ_turns = integer(circ_turns)
	measure_val1 = integer(measure_val1)
	measure_math = integer(measure_math)
	measure_value = integer(measure_value)
	measure_rank = integer(measure_rank)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	nullify = integer(nullify)
	level = integer(level)

	entry = PowerDegMod(power_id = power_id,
						extra_id = extra_id,
						target = target,
						value = value,
						deg_type = deg_type,
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
						deg_condition_type = deg_condition_type,
						condition_damage_value = condition_damage_value,
						condition_damage = condition_damage,
						condition1 = condition1,
						condition2 = condition2,
						keyword = keyword,
						nullify = nullify,
						cumulative = cumulative,
						linked = linked,
						level = level)

	body = degree_mod_post(entry)
	return jsonify(body)


@powers.route('/power/degree/create', methods=['POST'])
def power_post_degree():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = degree_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	degree_type = request.get_json()['degree_type']
	degree = request.get_json()['degree']
	keyword = request.get_json()['keyword']
	desscription = request.get_json()['desscription']
	extra_effort = request.get_json()['extra_effort']
	cumulative = request.get_json()['cumulative']
	target = request.get_json()['target']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	degree = integer(degree)

	entry = PowerDegree(power_id = power_id,
						extra_id = extra_id,
						degree_type = degree_type,
						degree = degree,
						keyword = keyword,
						desscription = desscription,
						extra_effort = extra_effort,
						cumulative = cumulative,
						target = target)

	body = degree_post(entry)
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
	no_penalty = request.get_json()['no_penalty']
	no_circumstance = request.get_json()['no_circumstance']
	immunity_other = request.get_json()['immunity_other']
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	radius = integer(radius)
	distance = integer(distance)
	rank = integer(rank)
	move_speed = integer(move_speed)
	visibility_mod = integer(visibility_mod)
	cost = integer(cost)
	ranks = integer(ranks)


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
						immunity_other = immunity_other,
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

	body = environment_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)


	entry = PowerLevels(power_id = power_id,
						extra_id = extra_id,
						level_type = level_type,
						level = level,
						level_effect = level_effect)

	body = levels_post(entry)
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
	attitude_trait_type = request.get_json()['attitude_trait_type']
	attitude_trait = request.get_json()['attitude_trait']
	resitable_check = request.get_json()['resitable_check']
	resitable_dc = request.get_json()['resitable_dc']
	multiple_value = request.get_json()['multiple_value']
	horde = request.get_json()['horde']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	points = integer(points)
	sacrifice_cost = integer(sacrifice_cost)
	attitude_type = integer(attitude_type)
	resitable_check = integer(resitable_check)
	resitable_dc = integer(resitable_dc)
	multiple_value = integer(multiple_value)


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
						attitude_type = attitude_type,
						attitude_trait_type = attitude_trait_type,
						attitude_trait = attitude_trait,
						resitable_check = resitable_check,
						resitable_dc = resitable_dc,
						multiple_value = multiple_value,
						horde = horde)

	body = minion_post(entry)
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
	ranks = request.get_json()['ranks']
	action = request.get_json()['action']
	side_effect = request.get_json()['side_effect']
	concentration = request.get_json()['concentration']
	simultaneous = request.get_json()['simultaneous']
	effortless = request.get_json()['effortless']
	noticeable = request.get_json()['noticeable']
	unreliable = request.get_json()['unreliable']
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
	ranks_cost = request.get_json()['ranks_cost']
	cost = request.get_json()['cost']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	objects_alone = integer(objects_alone)
	objects_character = integer(objects_character)
	effortless_degree = integer(effortless_degree)
	simultaneous_descriptor = integer(simultaneous_descriptor)
	area_mod = integer(area_mod)
	area_range = integer(area_range)
	area_descriptor = integer(area_descriptor)
	limited_mod = integer(limited_mod)
	limited_level = integer(limited_level)
	limited_source = integer(limited_source)
	limited_subjects = integer(limited_subjects)
	limited_extra = integer(limited_extra)
	limited_degree = integer(limited_degree)
	limited_sense = integer(limited_sense)
	limited_descriptor = integer(limited_descriptor)
	limited_range = integer(limited_range)
	side_level = integer(side_level)
	reflect_check = integer(reflect_check)
	reflect_descriptor = integer(reflect_descriptor)
	subtle_dc = integer(subtle_dc)
	ranks_ranks = integer(ranks_ranks)
	ranks_mod = integer(ranks_mod)
	points_reroll_cost = integer(points_reroll_cost)
	points_rerolls = integer(points_rerolls)
	points_reroll_result = integer(points_reroll_result)
	ranks_cost = integer(ranks_cost)
	cost = integer(cost)

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
						ranks = ranks,
						action = action,
						side_effect = side_effect,
						concentration = concentration,
						simultaneous = simultaneous,
						effortless = effortless,
						noticeable = noticeable,
						unreliable = unreliable,
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
						reflect_check = reflect,
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
						ranks_cost = ranks_cost,
						cost = cost)

	body = mod_post(entry)
	return jsonify(body)


@powers.route('/power/move/create', methods=['POST'])
def power_post_move():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = move_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	rank = request.get_json()['rank']
	math = request.get_json()['math']
	mod = request.get_json()['mod']
	per_rank = request.get_json()['per_rank']
	flight = request.get_json()['flight']
	aquatic = request.get_json()['aquatic']
	ground = request.get_json()['ground']
	condition = request.get_json()['condition']
	direction = request.get_json()['direction']
	distance_type = request.get_json()['distance_type']
	distance_value = request.get_json()['distance_value']
	distance_math_value = request.get_json()['distance_math_value']
	distance_math = request.get_json()['distance_math']
	distance_math_value2 = request.get_json()['distance_math_value2']
	distance_mod = request.get_json()['distance_mod']
	dc = request.get_json()['dc']
	others = request.get_json()['others']
	continuous = request.get_json()['continuous']
	subtle = request.get_json()['subtle']
	concentration = request.get_json()['concentration']
	obstacles = request.get_json()['obstacles']
	objects = request.get_json()['objects']
	permeate = request.get_json()['permeate']
	special = request.get_json()['special']
	prone = request.get_json()['prone']
	check_type = request.get_json()['check_type']
	obstacles_check = request.get_json()['obstacles_check']
	concealment = request.get_json()['concealment']
	extended = request.get_json()['extended']
	mass = request.get_json()['mass']
	mass_value = request.get_json()['mass_value']
	extended_actions = request.get_json()['extended_actions']
	acquatic_type = request.get_json()['acquatic_type']
	concealment_sense = request.get_json()['concealment_sense']
	concealment_trait_type = request.get_json()['concealment_trait_type']
	concealment_trait = request.get_json()['concealment_trait']
	permeate_type = request.get_json()['permeate_type']
	permeate_speed = request.get_json()['permeate_speed']
	permeate_cover = request.get_json()['permeate_cover']
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
	ground_type = request.get_json()['ground_type']
	ground_permanence = request.get_json()['ground_permanence']
	ground_time = request.get_json()['ground_time']
	ground_units = request.get_json()['ground_units']
	ground_ranged = request.get_json()['ground_ranged']
	subtle_trait_type = request.get_json()['subtle_trait_type']
	subtle_trait = request.get_json()['subtle_trait']
	subtle_mod = request.get_json()['subtle_mod']
	flight_resist = request.get_json()['flight_resist']
	flight_equip = request.get_json()['flight_equip']
	flight_conditions = request.get_json()['flight_conditions']
	objects_check = request.get_json()['objects_check']
	objects_attack = request.get_json()['objects_attack']
	objects_skill_type = request.get_json()['objects_skill_type']
	objects_skill = request.get_json()['objects_skill']
	objects_direction = request.get_json()['objects_direction']
	objects_damage = request.get_json()['objects_damage']
	damage_type = request.get_json()['damage_type']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_free = request.get_json()['check_free']
	ranks = request.get_json()['ranks']
	cost = request.get_json()['cost']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	rank = integer(rank)
	math = integer(math)
	mod = integer(mod)
	distance_value = integer(distance_value)
	distance_math_value = integer(distance_math_value)
	distance_math = integer(distance_math)
	distance_math_value2 = integer(distance_math_value2)
	distance_mod = integer(distance_mod)
	dc = integer(dc)
	mass_value = integer(mass_value)
	extended_actions = integer(extended_actions)
	concealment_sense = integer(concealment_sense)
	permeate_speed = integer(permeate_speed)
	dimension_mass_rank = integer(dimension_mass_rank)
	dimension_descriptor = integer(dimension_descriptor)
	special_time_carry = integer(special_time_carry)
	ground_type = integer(ground_type)
	ground_time = integer(ground_time)
	ground_units = integer(ground_units)
	subtle_mod = integer(subtle_mod)
	objects_check = integer(objects_check)
	objects_attack = integer(objects_attack)
	ranks = integer(ranks)
	cost = integer(cost)

	entry = PowerMove(power_id = power_id,
						extra_id = extra_id,
						rank = rank,
						math = math,
						mod = mod,
						per_rank = per_rank,
						flight = flight,
						aquatic = aquatic,
						ground = ground,
						condition = condition,
						direction = direction,
						distance_type = distance_type,
						distance_value = distance_value,
						distance_math_value = distance_math_value,
						distance_math = distance_math,
						distance_math_value2 = distance_math_value2,
						distance_mod = distance_mod,
						dc = dc,
						others = others,
						continuous = continuous,
						subtle = subtle,
						concentration = concentration,
						obstacles = obstacles,
						objects = objects,
						permeate = permeate,
						special = special,
						prone = prone,
						check_type = check_type,
						obstacles_check = obstacles_check,
						concealment = concealment,
						extended = extended,
						mass = mass,
						mass_value = mass_value,
						extended_actions = extended_actions,
						acquatic_type = acquatic_type,
						concealment_sense = concealment_sense,
						concealment_trait_type = concealment_trait_type,
						concealment_trait = concealment_trait,
						permeate_type = permeate_type,
						permeate_speed = permeate_speed,
						permeate_cover = permeate_cover,
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
						ground_type = ground_type,
						ground_permanence = ground_permanence,
						ground_time = ground_time,
						ground_units = ground_units,
						ground_ranged = ground_ranged,
						subtle_trait_type = subtle_trait_type,
						subtle_trait = subtle_trait,
						subtle_mod = subtle_mod,
						flight_resist = flight_resist,
						flight_equip = flight_equip,
						flight_conditions = flight_conditions,
						objects_check = objects_check,
						objects_attack = objects_attack,
						objects_skill_type = objects_skill_type,
						objects_skill = objects_skill,
						objects_direction = objects_direction,
						objects_damage = objects_damage,
						damage_type = damage_type,
						check_trait_type = check_trait_type,
						check_trait = check_trait,
						check_free = check_free,
						ranks = ranks,
						cost = cost)

	body = move_post(entry)
	return jsonify(body)

	
@powers.route('/power/opposed/create', methods=['POST'])
def power_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = opposed_post_errors(data)

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
	opponent_trait_type = request.get_json()['opponent_trait_type']
	opponent_trait = request.get_json()['opponent_trait']
	opponent_mod = request.get_json()['opponent_mod']
	player_check = request.get_json()['player_check']
	opponent_check = request.get_json()['opponent_check']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	mod = integer(mod)
	opponent_mod = integer(opponent_mod)
	player_check = integer(player_check)
	opponent_check = integer(opponent_check)

	entry = PowerOpposed(power_id = power_id,
							extra_id = extra_id,
							trait_type = trait_type,
							trait = trait,
							mod = mod,
							opponent_trait_type = opponent_trait_type,
							opponent_trait = opponent_trait,
							opponent_mod = opponent_mod,
							player_check = player_check,
							opponent_check = opponent_check)

	body = opposed_post(entry)
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
	dc_value = request.get_json()['dc_value']
	dc_trait_type = request.get_json()['dc_trait_type']
	dc_trait = request.get_json()['dc_trait']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	flat_value = integer(flat_value)
	flat_units = integer(flat_units)
	flat_rank = integer(flat_rank)
	flat_rank_value = integer(flat_rank_value)
	flat_rank_units = integer(flat_rank_units)
	flat_rank_rank = integer(flat_rank_rank)
	flat_rank_distance = inter(flat_rank_distance)
	flat_rank_distance_rank = integer(flat_rank_distance_rank)
	units_rank_start_value = integer(units_rank_start_value)
	units_rank_value = integer(units_rank_value)
	units_rank_units = integer(units_rank_units)
	units_rank_rank = integer(units_rank_rank)
	rank_distance_start = integer(rank_distance_start)
	rank_distance = integer(rank_distance)
	rank_effect_rank = integer(rank_effect_rank)
	effect_mod_math = integer(effect_mod_math)
	effect_mod = integer(effect_mod)
	check_math = integer(check_math)
	check_mod = integer(check_mod)
	trait_math = integer(trait_math)
	trait_mod = integer(trait_mod)
	distance_mod_rank = integer(distance_mod_rank)
	distance_mod_math = integer(distance_mod_math)
	dc_value = integer(dc_value)

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
						dc_value = dc_value,
						dc_trait_type = dc_trait_type,
						dc_trait = dc_trait)

	body = ranged_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	mod = integer(mod)
	rounds = integer(rounds)
	descriptor = integer(descriptor)
	check_type = integer(check_type)

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

	body = resist_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	dc = integer(dc)
	mod = integer(mod)
	level = integer(level)
	degree = integer(degree)
	descriptor = integer(descriptor)
	weaken_max = integer(weaken_max)
	weaken_restored = integer(weaken_restored)
	damage =  integer(damage)
	nullify_descriptor = integer(nullify_descriptor)
	nullify_alternate = integer(nullify_alternate)

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

	body = resisted_by_post(entry)
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

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	degree = integer(degree)
	value_dc = integer(value_dc)
	math_dc = integer(math_dc)
	math = integer(math)
	time_value = integer(time_value)
	time_unit = integer(time_unit)

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

	body = reverse_effect_post(entry)
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
	sense_cost = request.get_json()['sense_cost']
	subsense_cost = request.get_json()['subsense_cost']
	skill = request.get_json()['skill']
	skill_required = request.get_json()['skill_required']
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
	time_set = request.get_json()['time_set']
	time_value = request.get_json()['time_value']
	time_unit = request.get_json()['time_unit']
	time_skill = request.get_json()['time_skill']
	time_bonus = request.get_json()['time_bonus']
	time_factor = request.get_json()['time_factor']
	distance = request.get_json()['distance']
	distance_dc = request.get_json()['distance_dc']
	distance_mod = request.get_json()['distance_mod']
	distance_value = request.get_json()['distance_value']
	distance_unit = request.get_json()['distance_unit']
	distance_factor = request.get_json()['distance_factor']
	dimensional_type = request.get_json()['dimensional_type']
	ranks = request.get_json()['ranks']
	cost = request.get_json()['cost']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	sense = db.Column(db.Integer)
	subsense = db.Column(db.Integer)
	sense_cost = db.Column(db.Integer)
	subsense_cost = db.Column(db.Integer)
	skill = integer(skill)
	resist_circ = integer(resist_circ)
	time_value = integer(time_value)
	time_unit = integer(time_unit)
	time_skill = integer(time_skill)
	time_factor = integer(time_factor)
	distance_dc = integer(distance_dc)
	distance_mod = integer(distance_mod)
	distance_value = integer(distance_value)
	distance_unit = integer(distance_unit)
	distance_factor = integer(distance_factor)
	ranks = integer(ranks)
	cost = integer(cost)

	entry = PowerSense(power_id = power_id,
						extra_id = extra_id,
						target = target,
						sense = sense,
						subsense = subsense,
						sense_cost = sense_cost,
						subsense_cost = subsense_cost,
						skill = skill,
						skill_required = skill_required,
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
						time_set = time_set,
						time_value = time_value,
						time_unit = time_unit,
						time_skill = time_skill,
						time_bonus = time_bonus,
						time_factor = time_factor,
						distance = distance,
						distance_dc = distance_dc,
						distance_mod = distance_mod,
						distance_value = distance_value,
						distance_unit = distance_unit,
						distance_factor = distance_factor,
						dimensional_type = dimensional_type,
						ranks = ranks,
						cost = cost)

	body = sense_post(entry)
	return jsonify(body)



@powers.route('/power/time/create', methods=['POST'])
def power_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = time_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	time_type = request.get_json()['time_type']
	value_type = request.get_json()['value_type']
	value = request.get_json()['value']
	units = request.get_json()['units']
	time_value = request.get_json()['time_value']
	math = request.get_json()['math']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	dc = request.get_json()['dc']
	descriptor = request.get_json()['descriptor']
	check_type = request.get_json()['check_type']
	recovery = request.get_json()['recovery']
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_time = request.get_json()['recovery_time']
	recovery_incurable = request.get_json()['recovery_incurable']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	value = integer(value)
	units = integer(units)
	time_value = integer(time_value)
	math = integer(math)
	trait = integer(trait)
	dc = integer(descriptor)
	descriptor = integer(descriptor)
	check_type = integer(check_type)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)


	entry = PowerTime(power_id = power_id,
						extra_id = extra_id,
						time_type = time_type,
						value_type = value_type,
						value = value,
						units = units,
						time_value = time_value,
						math = math,
						trait_type = trait_type,
						trait = trait,
						dc = dc,
						descriptor = descriptor,
						check_type = check_type,
						recovery = recovery,
						recovery_penalty = recovery_penalty,
						recovery_time = recovery_time,
						recovery_incurable = recovery_incurable)

	body = time_post(entry)
	return jsonify(body)
