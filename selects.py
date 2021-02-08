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
from models import Levels, LevelType, Light

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

select = Blueprint('select', __name__)
db = SQLAlchemy()

@select.route('/select/skill', methods=['POST'])
def equip_skill_select():
	body = {}
	body['success'] = True
	options = []

	skill_id = request.get_json()['id'] 

	try:
		skill_id = int(skill_id)
		skill = db.session.query(Skill).filter_by(id=skill_id).one()
		bonuses = db.session.query(SkillBonus).filter_by(skill_id=skill_id).order_by(SkillBonus.name).all()
		skill_name = skill.name + ' Skill'
		options.append({'id': '', 'name': skill_name})
		for b in bonuses:
			options.append({'id': b.id, 'name': b.name})
	except:
		options.append({'id': '', 'name': 'Enhanced Skill'})
	
	body['options'] = options

	print(body)
	return jsonify(body)

@select.route('/select/action', methods=['POST'])
def advantage_action_select():
	body = {}
	body['success'] = True

	action = request.get_json()['id'] 

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

@select.route('/select/weapon/type', methods=['POST'])
def equip_weapon_type_select():
	body = {}
	body['success'] = True
	options = []

	cat_id = request.get_json()['id'] 

	try:
		cat_id = int(cat_id)
		cat = db.session.query(WeaponCat).filter_by(id=cat_id).one()
		weapon_type = db.session.query(WeaponType).filter_by(type_id=cat_id).order_by(WeaponType.name).all()
		weapon_name = cat.name + ' Weapon Type'
		options.append({'id': '', 'name': weapon_name})
		for w in weapon_type:
			options.append({'id': w.id, 'name': w.name})
	except:
		options.append({'id': '', 'name': 'Weapon Type'})
	
	body['options'] = options

	print(body)
	return jsonify(body)


@select.route('/select/weapon', methods=['POST'])
def equip_weapon_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 

	try:
		type_id = int(type_id)
		print(type_id)
		weapontype = db.session.query(WeaponType).filter_by(id=type_id).one()
		weapons = db.session.query(Weapon).filter_by(type_id=type_id).order_by(Weapon.name).all()
		weapon_name = weapontype.name + ' Weapons'
		options.append({'id': '', 'name': weapon_name})
		for w in weapons:
			options.append({'id': w.id, 'name': w.name})
	except:
		options.append({'id': '', 'name': 'Weapon'})
	
	body['options'] = options

	print(body)
	return jsonify(body)


@select.route('/select/medium/subtype', methods=['POST'])
def equip_medium_subtype_select():
	body = {}
	body['success'] = True
	options = []
	titles = []
	subtype_options = []
	medium_options = []
	
	id = request.get_json()['id']
	sub = request.get_json()['sub']
	get_titles = request.get_json()['titles']

	print('id ' + medium_type_id)
	

	try:
		medium_type = db.session.query(MediumType).filter_by(id=id).one()
		medium_subtypes = db.session.query(MediumSubType).filter_by(medium_type=id).order_by(MediumSubType.name).all()
		mediums = db.session.query(Medium).filter_by(medium_type=id).order_by(Medium.name).all()
		
		if get_titles !=  False:
			subtype_div = get_titles['title'] 'descriptor-medium-subtype-title'
			description_div = get_titles['description'] 'descriptor-medium-subtype-des-title'

		first_medium = medium_type.name + ' Mediums'
		first_subtype = medium_type.name + 'Subtypes'
		
		subtype_options.append({'id': '', 'name': first_subtype})
		medium_options.append({'id': '', 'name': first_medium})

		if sub == 'power_create':
			title = medium_type.name + ' Type'
			description_title = 'New ' + medium_type.name + ' Type Description'

			titles.append({'div': , 'title': title})
			titles.append({'div': , 'title': description_title})			
			body['titles'] = titles
			
			all_medium_type = 'Any ' + medium_type.name
			subtype_options.append({'id': 'all', 'name': all_medium_type})
			subtype_options.append({'id': 'new', 'name': 'New'})

		for subtype in medium_subtypes:
			subtype_options.append({'id': subtype.id, 'name': subtype.name})

		for medium in mediums:
			medium_options.append({'id': medium.id, 'name': medium.name})

		fields = request.get_json()['fields']
		try:
			subtype_field = fields['subtypes']
			medium_field = fields['mediums']
		except:
			body['success']  = False

		send_subtypes = {'select': subtype_field, 'options': subtype_options}
		send_mediums = {'select': medium_field, 'options': medium_options}

		options.append(send_subtypes)
		options.append(send_mediums)

		body['options'] = options
	except:
		body['success'] = False
		body['options'] = 'no results'

	print(body)
	return jsonify(body)

@select.route('/select/medium', methods=['POST'])
def equip_medium_select():
	body = {}
	body['success'] = True
	
	medium_subtype = request.get_json()['id']
	options = []
	sub = request.get_json()['sub']
	body['titles'] = False
	titles = []
	print('id ' + medium_subtype)

	if medium_subtype != '' and medium_subtype != 'all' and medium_subtype != 'new':
		try:
			subtype = db.session.query(MediumSubType).filter_by(id=medium_subtype).one()
			mediums = db.session.query(Medium).filter_by(medium_subtype=medium_subtype).order_by(Medium.name).all()
			first = subtype.name + ' Mediums'
			
			options.append({'id': '', 'name': first})

			if sub == 'power_create':
				all_subtype = 'Any ' + subtype.name
				ooptions.append({'id': 'all', 'name': all_subtype})
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


@select.route('/select/equipment', methods=['POST'])
def vehicle_equipment_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id']
	sub = request.get_json()['sub']
	add = False

	if sub != False:
		if sub == 'feature':
			options.append({'id': 'all', 'name': 'All Features'})

	try:
		type_id = int(type_id)
		equip_type = db.session.query(EquipType).filter_by(id=type_id).one()
		equipment = db.session.query(Equipment).filter_by(type_id=type_id).order_by(Equipment.name).all()
		options.append({'id': '', 'name': equip_type.name})
		if add:
			for special in add_options:
				options.append(special)
		for e in equipment:
			options.append({'id': e.id, 'name': e.name})
	except:
		options.append({'id': '', 'name': 'No Equipment of that Type'})
		options.append(add)
	
	body['options'] = options

	print(body)
	return jsonify(body)

@select.route('/select/feature', methods=['POST'])
def vehicle_feature_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 
	
	try:
		type_id = int(type_id)
		print(type_id)
		equipment = db.session.query(Equipment).filter_by(id=type_id).one()
		features = db.session.query(Feature).filter(Feature.equip_id==type_id).order_by(Feature.name).first()
		if features is None:
			options.append({'id': '', 'name': 'Equipment has no Features'})
		else:
			features = db.session.query(Feature).filter(Feature.equip_id==type_id, Feature.name != '').order_by(Feature.name).all()
			equipment_name = equipment.name + "'s Features"
			options.append({'id': '', 'name': equipment_name})
			for f in features:
				options.append({'id': f.id, 'name': f.name})
	except:
		options.append({'id': '', 'name': 'All Features'})
		features = db.session.query(Feature).filter(Feature.name != '').order_by(Feature.name).all()
		for f in features:
			options.append({'id': f.id, 'name': f.name})

	body['options'] = options

	print(body)
	return jsonify(body)

@select.route('/select/unit', methods=['POST'])
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

@select.route('/select/level', methods=['POST'])
def power_level_select():
	body = {}
	success = False
	options = []
	level_type_id = request.get_json()['id']

	try:
		level_type_id = int(level_type_id)
	except:
		print('not an int')
		options.append({'id': '', 'name': ''})

	try:
		levels = db.session.query(Levels).filter_by(type_id=level_type_id).all()
		for level in levels:
			options.append({'id': level.id, 'name': level.name})
		success = True
	except:
		print('no matching level type')
		options.append({'id': '', 'name': ''})

	body['success'] = success
	body['options'] = options

	print(body)
	return jsonify(body)

@select.route('/select/sense/subsense', methods=['POST'])
def get_subsense_select():
	body = {}
	body['success'] = True

	sense_id_str = request.get_json()['id']

	print(sense_id_str)

	options = []

	if sense_id_str == '':
		options.append({'id': '', 'name': 'Any'})
		body['options'] = options
		return jsonify(body)

	if sense_id_str == '0':
		options.append({'id': '', 'name': 'Any'})
		options.append({'id': 0, 'name': 'All'})
		body['options'] = options
		return jsonify(body)

	try:
		sense_id = int(sense_id_str)
		sense = db.session.query(Sense).filter_by(id=sense_id).one()
		subsenses = db.session.query(SubSense).filter_by(sense_id=sense_id).order_by(SubSense.name).all()
		
		any_sense = 'Any ' + sense.name
		all_sense = 'All ' + sense.name


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

@select.route('/select/trait', methods=['POST'])
def skill_trait_select():
	body = {}
	body['success'] = True

	trait = request.get_json()['id'] 
	sub = request.get_json()['sub']

	this = ['This Power']

	skills_query = db.session.query(Skill).order_by(Skill.name).all()
	skills = [{'id': '', 'name': 'Skill'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for skill in skills_query:
		skills.append({'id': skill.name, 'name': skill.name})

	abilities_query = db.session.query(Ability).order_by(Ability.name).all()
	abilities = [{'id': '', 'name': 'Ability'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for a in abilities_query:
		abilities.append({'id': a.name, 'name': a.name})

	defenses_query = db.session.query(Defense).order_by(Defense.name).all()
	defenses = [{'id': '', 'name': 'Defense'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for d in defenses_query:
		defenses.append({'id': d.name, 'name': d.name})

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']
	powers_sorted = sorted(powers_raw)
	powers = [{'id': '', 'name': 'Power'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for p in powers_sorted:
		powers.append({'id': p, 'name': p})

	bonuses_raw = ['Balancing', 'Maneuvering', 'Standing', 'Tumbling', 'Climbing', 'Jumping', 'Running', 'Swimming', 'Bluffing', 'Disguise', 'Feinting', 'Innuendo', 'Tricking', 'Detect Illusion', 'Detect Influence', 'Evaluate', 'Innuendo', 'Resist Influence', 'Coercing', 'Demoralizing', 'Intimidating Minions', 'Search', 'Gather Evidence', 'Analyze Evidence', 'Gather Information', 'Surveillance', 'Hearing', 'Seeing', 'Other Senses', 'Concealing', 'Contorting', 'Escaping', 'Legerdemain', 'Stealing', 'Hiding', 'Tailing', 'Operating', 'Building', 'Repairing', 'Jury-Rigging', 'Demolitions', 'Inventing', 'Security', 'Diagnosis', 'Provide Care', 'Revive', 'Stabalize', 'Treat Disease and Poison']
	bonuses_sorted = sorted(bonuses_raw)
	bonuses = [{'id': '', 'name': 'Enhanced Skill'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for b in bonuses_sorted:
		bonuses.append({'id': b, 'name': b})

	advantages_raw = ['Accurate Attack', 'Agile Feint', 'All-out Attack', 'Animal Empathy', 'Artificer', 'Assessment', 'Attractive', "Beginner's Luck", 'Benefit', 'Chokehold', 'Close Attack', 'Connected', 'Contacts', 'Daze', 'Defensive Attack', 'Defensive Roll', 'Diehard', 'Eidetic Memory', 'Equipment', 'Evasion', 'Extraordinary Effort', 'Fascinate', 'Fast Grab', 'Favored Environment', 'Favored Foe', 'Fearless', 'Grabbing Finesse', 'Great Endurance', 'Hide in Plain Sight', 'Improved Aim', 'Improved Critical', 'Improved Defense', 'Improved Disarm', 'Improved Grab', 'Improved Initiative', 'Improved Hold', 'Improved Smash', 'Improved Trip', 'Improvised Tools', 'Improvised Weapon', 'Inspire', 'Instant Up', 'Interpose', 'Inventor', 'Jack-of-all-Trades', 'Languages', 'Leadership', 'Luck', 'Minion', 'Move-by Action', 'Power Attack', 'Precise Attack', 'Prone Fighting', 'Quick Draw', 'Ranged Attack', 'Redirect', 'Ritualist', 'Second Chance', 'Seize Initiative', 'Set-Up', 'Sidekick', 'Skill Mastery', 'Startle', 'Takedown', 'Taunt', 'Teamwork', 'Throwing Mastery', 'Tracking', 'Trance', 'Ultimate Effort', 'Uncanny Dodge', 'Weapon Bind', 'Weapon Break', 'Well-Informed']
	advantages_sorted = sorted(advantages_raw)
	advantages = [{'id': '', 'name': 'Advantage'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for a in advantages_sorted:
		advantages.append({'id': a, 'name': a})

	extras_query = db.session.query(Extra).order_by(Extra.name).all()
	extras = [{'id': '', 'name': 'Extra'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
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
	elif trait == 'manipulate':
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

@select.route('/select/descriptor', methods=['POST'])
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
	rarity = request.get_json()['rarity']

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

	if rarity != False:
		des_id = rarity
		for i in range(len(descriptors) - 1, -1, -1):
			print(descriptors[i].get('rarity'))
			if descriptors[i].get('rarity') == des_id:
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