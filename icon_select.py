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
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
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

from posts.skill_posts import skill_ability_post, skill_check_post, skill_circ_post, skill_dc_post, skill_degree_post, skill_levels_post, skill_modifiers_post, skill_opposed_post, skill_time_post
from errors.skill_errors import skill_save_errors, skill_ability_post_errors, skill_check_post_errors, skill_circ_post_errors, skill_dc_post_errors, skill_degree_post_errors, skill_levels_post_errors, skill_modifiers_post_errors, skill_opposed_post_errors, skill_time_post_errors


load_dotenv()

import os

db_path = os.environ.get("db_path")

icon = Blueprint('icon', __name__)
db = SQLAlchemy()

@icon.route('/select/icon/skill', methods=['POST'])
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

@icon.route('/select/icon/ability', methods=['POST'])
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