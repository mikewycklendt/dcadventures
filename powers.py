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
from models import setup_db, Ability, Power, Extra, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

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

	power_includes = {'base_form': 'power_create/base_form.html', 'range': 'power_create/range.html', 'resisted_by': 'power_create/resisted_by.html', 'reverse_effect': 'power_create/reverse_effect.html', 'move': 'power_create/move.html', 'levels': 'power_create/levels.html', 'category': 'power_create/category.html', 'sense': 'power_create/sense.html', 'ranks': 'power_create/ranks.html', 'circ': 'power_create/circ.html', 'create': 'power_create/create.html', 'damage': 'power_create/damage.html', 'extras': 'power_create/extras.html', 'degree_mod': 'power_create/degree_mod.html', 'defense': 'power_create/defense.html', 'character': 'power_create/character.html', 'environment': 'power_create/environment.html', 'descriptors': 'power_create/descriptors.html', 'resist': 'power_create/resist.html'}
	
	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	positives = []
	for i in range(1, 41, 1):
		positives.append(i)

	die = []
	for i in range(1, 21, 1):
		die.append(i)

	time_numbers = []
	for i in range(1, 61, 1):
		positives.append(i)

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
					{'type': 'rank', 'name': 'Rank Table'}]

	duration_type = [{'type': 'instant', 'name': 'Instant'}, 
						{'type': 'conc', 'name': 'Concentration'}, 
						{'type': 'sustained', 'name': 'Sustained'},
						{'type': 'cont', 'name': 'Continuous'},
						{'type': 'perm', 'name': 'Permanent'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Power Rank'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	distance = db.session.query(Unit).filter_by(type_id=3)

	checks = Check.query.all()

	actions = Action.query.all()

	skills = Skill.query.all()

	abilities = Ability.query.all()

	defenses = Defense.query.all()

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers = sorted(powers_raw)

	check_types = [{'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}]

	base_conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']
	conditions_raw = []
	for condition in base_conditions:
		conditions_raw.append(condition.name)
	for condition in combined_conditions:
		conditions_raw.append(condition)
	conditions = sorted(conditions_raw)

	effects = [{'type': 'condition', 'name': 'Condition'}, {'type': 'damage', 'name': 'Damage'}]

	dc_value = [{'type': '', 'name': 'DC Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]

	whens = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]

	maths = Math.query.all()

	times = db.session.query(Unit).filter_by(type_id=2)

	distances = db.session.query(Unit).filter_by(type_id=3)

	permanence = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	
	partners = [{'type': '', 'name': 'N/A'}, {'type': 'power', 'name': 'Same Power'}, {'type': 'device', 'name': 'Device'}, {'type': 'both', 'name': 'Power or Device'}]

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

	sense_distance = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'rank', 'name': 'By Rank'}]

	darkness = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]

	determined = [{'type': '', 'name': 'Determined By'}, {'type': 'dc', 'name': 'DC'}, {'type': 'target', 'name': 'Target Trait'}, {'type': 'player', 'name': 'Player Trait'}]

	traits = [{'type': '', 'name': 'Trait'}, {'type': 'this', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}]

	object_damage = [{'type': '', 'name': 'Damage Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'effect', 'name': 'Effect Rank'}, {'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}, {'type': 'ability', 'name': 'Player Ability'}]

	solidity = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]

	visibility = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]

	against = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]

	moveable = [{'type': '', 'name': 'Moveable With'}, {'type': None, 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]

	complexity = Complex.query.all()

	deg_mod_type = [{'type': '', 'name': 'Type'}, {'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}]

	value_type = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	use_type = [{'type': '', 'name': 'Use Type'}, {'type': 'add', 'name': 'Add to'}, {'type': 'replace', 'name': 'In Place of'}, {'type': 'gm', 'name': 'GM Choice'}]

	outcome = [{'type': '', 'name': ''}, {'type': '<', 'name': 'Lower'}, {'type': '>', 'name': 'Higher'}]

	circ_type = [{'type': '', 'name': 'Triggered By'}, {'type': 'range', 'name': 'Range'}]

	ranges = Range.query.all()

	bonus_type = [{'type': 'flat', 'name': 'Flat'}, {'type': 'rank', 'name': 'Per Rank'}]

	limited = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]

	emotions = Emotion.query.all()

	temp_type = [{'type': '', 'name': 'Type'}, {'type': 'cold', 'name': 'Cold'}, {'type': 'heat', 'name': 'Heat'}]

	extremity = [{'type': '', 'name': 'Extremity'}, {'type': 'intense', 'name': 'Intense'}, {'type': 'extreme', 'name': 'Extreme'}]

	nature = [{'type': '', 'name': 'Nature'}, {'type': 'ice', 'name': 'Ice'}, {'type': 'rain', 'name': 'Rain'}, {'type': 'snow', 'name': 'Snow'}, {'type': 'wind', 'name': 'Wind'}, {'type': 'other', 'name': 'Other'}]

	grounds = Ground.query.all()

	directions = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]

	character = [{'type': '', 'name': 'Changed Trait'}, {'type': 'size', 'name': 'Size Rank'}, {'type': 'intim', 'name': 'Intimidation'}]

	updown = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	descriptors = Descriptor.query.all()

	origins = Origin.query.all()

	sources = Source.query.all()

	medium = Medium.query.all()

	mediums = MediumType.query.all()

	materials = db.session.query(MediumSubType).filter_by(medium_type=1)
	
	energies = db.session.query(MediumSubType).filter_by(medium_type=2)

	descriptor_type = [{'type': '', 'name': 'Applies To:'}, {'type': 'power', 'name': 'This Power'}, {'type': 'effect', 'name': 'Power Effect'}]

	resistance_type = [{'type': '', 'name': 'Applies to'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'trait', 'name': 'Check Type'}]

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
											materials=materials, energies=energies, descriptor_type=descriptor_type, resistance_type=resistance_type, bonus_type=bonus_type)

@powers.route('/power/trait/select', methods=['POST'])
def power_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['trait'] 

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
	else:
		body['success'] = False
		body['options'] = 'no match'

	print(body)
	return jsonify(body)

@powers.route('/power/descriptor/select', methods=['POST'])
def power_descriptor_select():
	body = {}
	body['success'] = True

	origin = request.get_json()['origin']
	source = request.get_json()['source']
	medium_type = request.get_json()['medium_type']
	medium_subtype = request.get_json()['medium_subtype']
	medium = request.get_json()['medium']

	descriptors_query = Descriptor.query.all()

	descriptors = [descriptor.format() for descriptor in descriptors_query]
		
	options = []

	options.append({'id': '', 'name': 'Descriptor'})
	options.append({'id': 'all', 'name': 'All Matching'})
	options.append({'id': 'new', 'name': 'New'})

	try:
		if origin != 'all' or origin != 'new' or origin != '':
			for descriptor in descriptors:
				if descriptor['origin'] != origin:
					descriptors.remove(descriptor)

		if source != 'all' or source != 'new' or source != '':
			for descriptor in descriptors:
				if descriptor['source'] != source:
					descriptors.remove(descriptor)

		if medium_type != 'all' or medium_type != 'new' or medium_type != '':
			for descriptor in descriptors:
				if descriptor['medium_type'] != medium_type:
					descriptors.remove(descriptor)

		if medium_subtype != 'all' or medium_subtype != 'new' or medium_subtype != '':
			for descriptor in descriptors:
				if descriptor['medium_subtype'] != medium_subtype:
					descriptors.remove(descriptor)

		if medium != 'all' or medium != 'new' or medium != '':
			for descriptor in descriptors:
				if descriptor['medium'] != medium:
					descriptors.remove(descriptor)

		for descriptor in descriptors:
			options.append({'id': descriptor['id'], 'name': descriptor['name']})
	
	except:
		body['success'] = True
		options.append({'id': '', 'name': 'No Descriptors'})

	body['options'] = options

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
		
		all_medium_type = 'Any ' + medium_type.name

		title = medium_type.name + ' Type'

		des_title = 'New ' + medium_type.name + ' Type Description'

		options = []

		options.append({'id': '', 'name': medium_type.name})
		options.append({'id': 'all', 'name': all_medium_type})
		options.append({'id': 'new', 'name': 'New'})

		for subtype in medium_subtypes:
			options.append({'id': subtype.id, 'name': subtype.name})

		body['options'] = options	
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

	sense_id = request.get_json()['sense_id']


	try:
		sense = db.session.query(Sense).filter_by(id=sense_id)
		subsenses = db.session.query(SubSense).filter_by(sense_id=sense_id).order_by(name).all()
		
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

	subtype = db.session.query(MediumSubType).filter_by(id=medium_subtype)
	mediums = db.session.query(Medium).filter_by(medium_subtype=medium_subtype).order_by(Medium.name).all()
		
	all_subtype = 'Any ' + subtype.name

	options = []

	options.append({'id': '', 'name': subtype.name})
	options.append({'id': 'all', 'name': all_subtype})
	options.append({'id': 'new', 'name': 'New'})

	for medium in mediums:
		options.append({'id': medium.id, 'name': medium.name})

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
	error = False
	error_msgs = []
	descriptor = {}

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
	power_id = request.get_json()['power_id']

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
				descriptor['origin'] = {'id': entry.id, 'name': entry.name}
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that origin')
			db.session.rollback()
		finally:
			db.session.close()
	elif origin == '':
		descriptor['origin'] = {'id': None, 'name': ''}
	else:
		entry = db.session.query(Origin).filter_by(id=origin)
		descriptor['origin'] = {'id': entry.id, 'name': entry.name}

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
				descriptor['source'] = {'id': entry.id, 'name': entry.name}
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that source')
			db.session.rollback()
		finally:
			db.session.close()
	elif source == '':
		descriptor['source'] = {'id': None, 'name': ''}
	else:
		entry = db.session.query(Source).filter_by(id=source)
		descriptor['source'] = {'id': entry.id, 'name': entry.name}

	if medium_type != '':
		entry = db.session.query(MediumType).filter_by(id=medium_type)
		descriptor['medium_type'] = {'id': entry.id, 'name': entry.name}
	else:
		descriptor['medium_type'] = {'id': None, 'name': ''}

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
				entry = MediumSubType(name=medium_subtype_name, description=medium_subtype_des)
				db.session.add(entry)
				db.session.commit()
				descriptor['medium_subtype'] = {'id': entry.id, 'name': entry.name}
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium subtype')
			db.session.rollback()
		finally:
			db.session.close()
	elif medium_subtype == '':
		descriptor['medium_type'] = {'id': None, 'name': ''}
	elif medium_subtype == 'all':
		descriptor['medium_type'] = {'id': None, 'name': 'all'}
	else:
		entry = db.session.query(MediumSubType).filter_by(id=medium_subtype)
		descriptor['medium_subtype'] = {'id': entry.id, 'name': entry.name}

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
				entry = Medium(name=medium_name, description=medium_des)
				db.session.add(entry)
				db.session.commit()
				descriptor['medium'] = {'id': entry.id, 'name': entry.name}
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that medium')
			db.session.rollback()
		finally:
			db.session.close()
	elif medium == '':
		descriptor['medium'] = {'id': None, 'name': ''}
	elif medium == 'all':
		descriptor['medium'] = {'id': None, 'name': 'all'}
	else:
		entry = db.session.query(Medium).filter_by(id=medium)
		descriptor['medium'] = {'id': entry.id, 'name': entry.name}
	
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
				entry = Descriptor(name=descriptor_name, result=descriptor_result)
				db.session.add(entry)
				db.session.commit()
				descriptor['descriptor'] = {'id': entry.id, 'name': entry.name}
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could Not Add that descriptor')
			db.session.rollback()
		finally:
			db.session.close()
	elif descriptor_field == '':
		descriptor['descriptor'] = {'id': None, 'name': ''}
	elif descriptor == 'all':
		descriptor['descriptor'] = {'id': None, 'name': 'all'}
	else:
		entry = db.session.query(Descriptor).filter_by(id=descriptor)
		descriptor['descriptor'] = {'id': entry.id, 'name': entry.name}

	origin = descriptor['origin']
	origin_id = origin['id']
	origin_name = origin['name']
	
	source = descriptor['source']
	source_id = source['id']
	source_name = source['name']

	medium_type = descriptor['medium_type']
	medium_type_id = medium_type['id']
	medium_type_name = medium_type['name']

	medium_subtype = descriptor['medium_subtype']
	medium_subtype_id = medium_subtype['id']
	medium_subtype_name = medium_subtype['name']
	
	medium = descriptor['medium']
	medium_id = medium['id']
	medium_name = medium['name']

	descriptor = descriptor['descriptor']
	descriptor_id = descriptor['id']
	descriptor_name = descriptor['name']

	count = 0

	names = []
	one_medium_name = ''

	if descriptor_id is not None:
		body['descriptor'] = True
		name = descriptor_name
	else:
		if origin_id is not None:
			names.append(origin_name)
			count = count + 1
		if source_id is not None:
			names.append(source_name)
			count = count + 1
		if medium_type_id is not None:
			one_medium_name = medium_type_name 
		if medium_subtype_id is not None:
			one_medium_name = medium_subtype_name
		if medium_id is not None:
			one_medium_name = medium_name
		if one_medium_name != '':
			names.append(one_medium_name)
			count = count + 1
		if count > 1:
			name = names[0]
			i = 1
			while i < len(names):
				name = name + ', ' + names[i]
		else:
			for only_name in names:
				name = only_name

	if descriptor_type == 'power':
		is_descriptor = True
		body['type'] = 'power'
	elif descriptor_type == 'effect':
		is_descriptor = False
		body['type'] = 'effect'
	else:
		error = True
		body['success'] = False
		error_msgs.append('You must choose if this descriptor is for this power or if this power interacts with this descriptor')
		body['error'] = error_msgs


	if error:
		return jsonify(body)
	else:
		try:
			entry = PowerDes(name = name,	
							power_id = power_id,
							des_id = descriptor_id,
							origin = origin_id,
							source = source_id,
							medium = medium_id,
							medium_type = medium_type_id,
							medium_subtype = medium_subtype,
							descriptor = is_descriptor)
			db.session.commit()

			body['id'] = entry.id
			body['name'] = entry.name
		except:
			error = True
			body['success'] = False
			error_msgs.append('Could not complete the process')
			body['error'] = error_msgs
			db.session.rollback()
		finally:
			db.session.close()

		if descriptor_field == 'new':
			try:
				descriptor_new = db.sesssion.query(Descriptor).filter(Descriptor.id == descriptor_id).one()
				descriptor_new.origin = origin_id
				descriptor_new.source = source_id
				descriptor_new.medium = medium_id
				descriptor_new.medium_type = medium_type_id
				descriptor_new.medium_subtype = medium_subtype_id
				descriptor_new.result =  descriptor_result
				db.session.commit()
			except:
				error = True
				body['success'] = False
				error_msgs.append('There could not fill out all descriptor information')
				body['error'] = error_msgs
				db.session.rollback()
			finally:
				db.session.close()

