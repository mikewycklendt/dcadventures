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

from posts.skill_posts import skill_ability_post, skill_check_post, skill_circ_post, skill_dc_post, skill_degree_post, skill_levels_post, skill_modifiers_post, skill_opposed_post, skill_time_post
from errors.skill_errors import skill_save_errors, skill_ability_post_errors, skill_check_post_errors, skill_circ_post_errors, skill_dc_post_errors, skill_degree_post_errors, skill_levels_post_errors, skill_modifiers_post_errors, skill_opposed_post_errors, skill_time_post_errors


load_dotenv()

import os

db_path = os.environ.get("db_path")

info = Blueprint('info', __name__)
db = SQLAlchemy()

@info.route('/info/equipment', methods=['POST'])
def equip_equipment_info_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 

	try:
		type_id = int(type_id)
		equipment = db.session.query(Equipment).filter_by(id=type_id).one()
		name = equipment.name
		cost = equipment.cost
		description = equipment.description
	except:
		name = 'Unavailable'
		cost = 'Unavailable'
		description = 'Unavailable'
		body['success'] = False

	body['name'] = name
	body['description'] = description
	body['cost'] = cost

	print(body)
	return jsonify(body)

@info.route('/info/weapon', methods=['POST'])
def equip_weapon_info_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id'] 

	try:
		type_id = int(type_id)
		weapon = db.session.query(Weapon).filter_by(id=type_id).order_by(Weapon.name).one()
		name = weapon.name
		cost = weapon.cost
		description = weapon.description
	except:
		name = 'Unavailable'
		cost = 'Unavailable'
		description = 'Unavailable'
		body['success'] = False

	body['name'] = name
	body['description'] = description
	body['cost'] = cost

	print(body)
	return jsonify(body)

@info.route('/info/feature', methods=['POST'])
def vehicle_feature_info():
	body = {}
	body['success'] = True
	
	feature_id = request.get_json()['id'] 

	try:
		feature_id = int(feature_id)
		feature = db.session.query(Feature).filter_by(id=feature_id).one()
		body['cost'] = 1
		body['name'] = feature.name 
		body['description'] = feature.description
	except:
		body['success'] = False

	print(body)
	return jsonify(body)


@info.route('/info/headquarters/feature', methods=['POST'])
def head_feature_info_select():
	body = {}
	body['success'] = True
	options = []

	type_id = request.get_json()['id']

	try:
		type_id = int(type_id)	
		item = db.session.query(HeadFeature).filter_by(id=type_id).one()
		items = db.session.query(HeadFeatAddon).filter_by(head_feature=type_id).all()
		weapons = []
		weapon_check = False
		equipment = []
		equipment_check = False
		features = []
		feature_check = False
		for i in items:
			if i.weapon is not None:
				weapon_check = True
				weapon = db.session.query(Weapon).filter_by(id=i.weapon).one()
				weapons.append(weapon.name)
			if i.equipment is not None:	
				equipment_check = True
				equip = db.session.query(Equipment).filter_by(id=i.equipment).one()
				equipment.append(equip.name)
			if i.feature is not None:
				feature_check = True
				feature = db.session.query(Feature).filter_by(id=i.feature).one()
				features.append(feature.name)
		if weapon_check == False:
			weapons.append('No Weaopons')
		if equipment_check == False:	
			equipment.append('No Equipment')
		if feature_check == False:
			features.append('No Features')
		name = item.name
		cost = 1	
		description = item.description
		body['name'] = name
		body['description'] = description
		body['cost'] = cost
		body['weapons'] = weapons
		body['equipment'] = equipment
		body['features'] = features
	except:
		body['success'] = False

	print(body)
	return jsonify(body)
	
