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
from db.equipment_models import Equipment, EquipFeature, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item



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
		bonuses = db.session.query(SkillBonus).filter(SkillBonus.skill == skill_id, SkillBonus.show == True).order_by(SkillBonus.name).all()
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
	actions = db.session.query(Action).filter(Action.hide == None).all()
	for a in actions:
		base.append({'id': a.id, 'name': a.name})
		
	conflict = []
	conflicts = db.session.query(ConflictAction).filter(ConflictAction.hide == None).order_by(ConflictAction.name).all()
	for c in conflicts:
		conflict.append({'id': c.id, 'name': c.name})


	if action == 'auto':
		body['options'] = [{'id': 0, 'name': 'Automatic'}]
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
	sub = request.get_json()['sub']

	try:
		type_id = int(type_id)
		print(type_id)
		weapontype = db.session.query(WeaponType).filter_by(id=type_id).one()
		weapons = db.session.query(Weapon).filter(Weapon.type_id == type_id, Weapon.show == True).order_by(Weapon.name).all()
		weapon_name = weapontype.name + ' Weapons'
		variable_name = 'Variable ' + weapontype.name
		options.append({'id': '', 'name': weapon_name})
		if sub == 'skill_create':
			options.append({'id': 'x', 'name': variable_name})
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
		medium_subtypes = db.session.query(MediumSubType).filter(MediumSubType.medium_type == id, MediumSubType.show == True).order_by(MediumSubType.name).all()
		mediums = db.session.query(Medium).filter(Medium.medium_type == id, Medium.show == True).order_by(Medium.name).all()
		
		if get_titles !=  False:
			subtype_div = get_titles['title']

		first_medium = medium_type.name + ' Mediums'
		first_subtype = medium_type.name + 'Subtypes'
		
		subtype_options.append({'id': '', 'name': first_subtype})
		medium_options.append({'id': '', 'name': first_medium})

		if sub == 'power_create':
			description_div = get_titles['description']
			title = medium_type.name + ' Type'
			description_title = 'New ' + medium_type.name + ' Type Description'

			titles.append({'div': subtype_div, 'title': title})
			titles.append({'div': description_div, 'title': description_title})			
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
			mediums = db.session.query(Medium).filter(Medium.medium_subtype == medium_subtype, Medium.show == True).order_by(Medium.name).all()
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
		equipment = db.session.query(Equipment).filter(Equipment.type_id == type_id, Equipment.show == True).order_by(Equipment.name).all()
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
		features = db.session.query(EquipFeature).filter(EquipFeature.equip_id==type_id).order_by(Feature.name).first()
		if features is None:
			options.append({'id': '', 'name': 'Equipment has no Features'})
		else:
			equipment_name = equipment.name + "'s Features"
			options.append({'id': '', 'name': equipment_name})
			for f in features:
				id = f.feature
				feature = db.session.query(Feature).filter_by(id=id).one()
				options.append({'id': id, 'name': feature.name})
	except:
		options.append({'id': '', 'name': 'All Features'})
		features = db.session.query(Feature).filter(Feature.show == True).order_by(Feature.name).all()
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
	sub - request.get_json()['sub']

	print(sense_id_str)

	options = []

	if sense_id_str == 'any':
		options.append({'id': 'any', 'name': 'Any'})
		body['options'] = options
		return jsonify(body)

	if sense_id_str == 'all':
		options.append({'id': 'any', 'name': 'Any'})
		options.append({'id': 'all', 'name': 'All'})
		
		body['options'] = options
		return jsonify(body)

	try:
		sense_id = int(sense_id_str)
		sense = db.session.query(Sense).filter_by(id=sense_id).one()
		subsenses = db.session.query(SubSense).filter_by(sense_id=sense_id).order_by(SubSense.name).all()
		
		any_sense = 'Any ' + sense.name
		all_sense = 'All ' + sense.name
		variable_sense = 'Variable' + sense.name

		options.append({'id': 'any', 'name': any_sense})
		options.append({'id': 'all', 'name': all_sense})
		options.append({'id': 'x', 'name': variable_sense})

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

	skills_query = db.session.query(Skill).filter(Skill.hide == None).order_by(Skill.name).all()
	skills = [{'id': '', 'name': 'Skill'}]
	if sub == 'variable':
		skills.append({'id': 'x', 'name': 'Variable'})
	for skill in skills_query:
		skills.append({'id': skill.id, 'name': skill.name})

	abilities_query = db.session.query(Ability).filter(Ability.hide == None).order_by(Ability.name).all()
	abilities = [{'id': '', 'name': 'Ability'}]
	if sub == 'variable':
		abilities.append({'id': 'x', 'name': 'Variable'})
	for a in abilities_query:
		abilities.append({'id': a.id, 'name': a.name})

	defenses_query = db.session.query(Defense).filter(Defense.hide == None).order_by(Defense.name).all()
	defenses = [{'id': '', 'name': 'Defense'}]
	if sub == 'variable':
		defenses.append({'id': 'x', 'name': 'Variable'})
	for d in defenses_query:
		defenses.append({'id': d.id, 'name': d.name})

	powers_query = db.session.query(Power).filter(Power.show == True).order_by(Power.name).all()
	powers = [{'id': '', 'name': 'Power'}]
	if sub == 'variable':
		powers.append({'id': 'x', 'name': 'Variable'})
	for p in powers_query:
		powers.append({'id': p.id, 'name': p.name})

	bonuses_query = db.session.query(SkillBonus).filter(SkillBonus.show == True).order_by(SkillBonus.name).all()
	bonuses = [{'id': '', 'name': 'Enhanced Skill'}]
	if sub == 'variable':
		bonuses.append({'id': 'x', 'name': 'Variable Enhanced Skill'})
	for b in bonuses_query:
		bonuses.append({'id': b.id, 'name': b.name})

	
	advantage_query = db.session.query(Advantage).filter(Advantage.show == True).order_by(Advantage.name).all()
	advantages = [{'id': '', 'name': 'Advantage'}]
	if sub == 'variable':
		advantages.append({'id': 'x', 'name': 'Variable Advantage'})
	for a in advantage_query:
		advantages.append({'id': a.id, 'name': a.name})

	extras_query = db.session.query(Extra).filter(Extra.show == True).order_by(Extra.name).all()
	extras = [{'id': '', 'name': 'Extra'}]
	if sub == 'variable':
		extras.append({'id': 'x', 'name': 'Variable'})
	for e in extras_query:
		try:
			power = db.session.query(Power).filter_by(id=e.power_id).one()
			name = e.name + ' (' + power.name + ')'
			extras.append({'id': e.id, 'name': name})
		except:
			print('no power')
			body['success'] = False

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
		body['options'] = [{'id': '0', 'name': 'Any Interarction'}]
	elif trait == 'manipulate':
		body['options'] = [{'id': '0', 'name': 'Any Manipulation'}]
	elif trait == 'this_power':
		body['options'] = [{'id': '0', 'name': 'This Power'}]
	elif trait == 'this_advantage':
		body['options'] = [{'id': '0', 'name': 'This Advantage'}]
	elif trait == 'sense':
		body['options'] = [{'id': '0', 'name': 'Sense'}]
	elif trait == 'size':	
		body['options'] = [{'id': '0', 'name': 'Size Rank'}]
	elif trait == 'speed':	
		body['options'] = [{'id': '0', 'name': 'Speed Rank'}] 
	elif trait == 'intim':
		body['options'] = [{'id': '0', 'name': 'Intimidation Rank'}]
	elif trait == 'any':
		body['options'] = [{'id': '0', 'name': 'Any Trait'}]
	elif trait == 'x':
		body['options'] = [{'id': '0', 'name': 'Variable'}]
	elif trait == 'auto':
		body['options'] = [{'id': '0', 'name': 'Automatic'}]
	elif trait == '':
		body['options'] = [{'id': '0', 'name': 'Trait'}]
	elif trait == 'immoveable':
		body['options'] = [{'id': '0', 'name': 'Immoveable'}]
	elif trait == 'this_bonus':
		body['options'] = [{'id': '0', 'name': 'This Skill'}]
	elif trait == 'active':
		body['options'] = [{'id': '0', 'name': 'Active Opponent Rank'}]
	elif trait == 'choice':
		body['options'] = [{'id': "0", 'name': "Players Chosen DC"}]
	elif trait == 'attack':
		body['options'] = [{'id': "0", 'name': "Attack Bonus"}]
	else:
		body['success'] = False
		body['options'] = [{'id': '', 'name': 'Trait'}]


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
		descriptors_query = db.session.query(Descriptor).filter(Descriptor.show == True).order_by(Descriptor.name).all()
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