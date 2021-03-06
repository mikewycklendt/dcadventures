from io import SEEK_CUR
from db.skill_models import SkillBonus
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import setup_db
from models import db

load_dotenv()

import os

db_path = os.environ.get("db_path")

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = db_path
app.config["SQLALCHEMY_DATABASE_URI"] = database_path

setup_db(app)


migrate = Migrate(app, db)

class Power(db.Model):
	__tablename__ = 'powers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	power_type = db.Column(db.Integer, db.ForeignKey('power_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	power_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)
	flat = db.Column(db.Boolean)
	limit = db.Column(db.Integer)
	dc_type = db.Column(db.String())
	dc_value = db.Column(db.Integer)
	dc_mod = db.Column(db.Integer)
	opponent_dc = db.Column(db.Integer)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	routine = db.Column(db.Boolean)
	routine_trait_type = db.Column(db.String())
	routine_trait = db.Column(db.Integer)
	materials = db.Column(db.Boolean)
	partner = db.Column(db.String())
	partner_trait_type = db.Column(db.String())
	partner_trait = db.Column(db.Integer)
	partner_dc = db.Column(db.Integer)
	circ = db.Column(db.String())
	circ_required = db.Column(db.String())
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill_required = db.Column(db.String())
	skill_when = db.Column(db.String())
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_bonus = db.Column(db.Integer)
	conflict_type = db.Column(db.String())
	target_type = db.Column(db.String())
	target = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	target_type = db.Column(db.String())
	strength_based = db.Column(db.String())
	info = db.Column(db.Boolean)
	gm_trigger = db.Column(db.Boolean)
	req_descriptor = db.Column(db.Boolean)
	damage_descriptor = db.Column(db.Boolean)
	emotion_type = db.Column(db.Boolean)
	emotion =  db.Column(db.String())
	alteration = db.Column(db.Boolean)

	alt_check = db.Column(db.Boolean)
	change_action = db.Column(db.Boolean)
	character = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	create = db.Column(db.Boolean)	
	damage = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	defense = db.Column(db.Boolean)
	degree = db.Column(db.Boolean)
	environment = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	minion = db.Column(db.Boolean)
	modifier = db.Column(db.Boolean)
	move = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	resistance = db.Column(db.Boolean)
	resist_by = db.Column(db.Boolean)
	reverse = db.Column(db.Boolean)
	sense = db.Column(db.Boolean)
	time = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)
	active = db.Column(db.Boolean)
	var_sense = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'power_type': self.power_type,
			'action': self.action,
			'power_range': self.power_range,
			'duration': self.duration,
			'cost': self.cost,
			'ranks': self.ranks,
			'flat': self.flat,
			'limit': self.limit,
			'dc_type': self.dc_type,
			'dc_value': self.dc_value,
			'dc_mod': self.dc_mod,
			'opponent_dc': self.opponent_dc,
			'check_type': self.check_type,
			'routine': self.routine,
			'routine_trait_type': self.routine_trait_type,
			'routine_trait': self.routine_trait,
			'materials': self.materials,
			'partner': self.partner,
			'partner_trait_type': self.partner_trait_type,
			'partner_dc': self.partner_dc,
			'partner_trait': self.partner_trait,
			'circ': self.circ,
			'circ_required': self.circ_required,
			'skill': self.skill,
			'skill_required': self.skill_required,
			'skill_when': self.skill_when,
			'grab': self.grab,
			'grab_type': self.grab_type,
			'condition': self.condition,
			'target_type': self.target_type,
			'strength_based': self.strength_based,
			'req_descriptor': self.req_descriptor,
			'damage_descriptor': self.damage_descriptor,
			'emotion_type': self.emotion_type,
			'emotion': self.emotion,
			'alteration': self.alteration,
			'alt_check': self.alt_check,
			'change_action': self.change_action,
			'character': self.character,
			'circumstance': self.circumstance,
			'create	': self.create,
			'damage': self.damage,
			'dc': self.dc,
			'defense': self.defense,
			'degree': self.degree,
			'environment': self.environment,
			'levels': self.levels,
			'minion': self.minion,
			'modifier': self.modifier,
			'move': self.move,
			'opposed': self.opposed,
			'ranged': self.ranged,
			'resistance': self.resistance,
			'resist_by': self.resist_by,
			'reverse': self.reverse,
			'sense': self.sense,
			'time': self.time,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base,
			'active': self.active,
			'var_sense': self.sense
		}

class PowerType(db.Model):
	__tablename__ = 'power_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

		
class PowerDuration(db.Model):
	__tablename__ = 'power_duration'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Extra(db.Model):
	__tablename__ = 'extras'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	name = db.Column(db.String())
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)
	des = db.Column(db.String())
	inherit = db.Column(db.Integer, db.ForeignKey('powers.id'))
	alternate = db.Column(db.Boolean)
	flat = db.Column(db.Boolean)
	stack = db.Column(db.Boolean)
	power_rank = db.Column(db.Boolean)
	type = db.Column(db.String())
	required_check = db.Column(db.Boolean)
	required = db.Column(db.Integer, db.ForeignKey('extras.id'))
	required_power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	required_power_rank = db.Column(db.Integer)
	extra_effect_count = db.Column(db.Integer)
	extra_effect = db.Column(db.Boolean)
	target_check = db.Column(db.Boolean)
	target = db.Column(db.String())
	target_type = db.Column(db.String())
	action_check = db.Column(db.Boolean)
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action_type = db.Column(db.String())
	action_limit = db.Column(db.Integer)
	routine = db.Column(db.Boolean)
	skill_type = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	range_check = db.Column(db.Boolean)
	range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	auto = db.Column(db.Boolean)
	auto_type = db.Column(db.String())
	auto_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	auto_check_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	auto_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	auto_opposed_type = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	ranks_check = db.Column(db.Boolean)
	ranks_type  = db.Column(db.String())
	rank = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))

	variable = db.Column(db.Boolean)
	character = db.Column(db.Boolean)
	circ = db.Column(db.Boolean)
	create = db.Column(db.Boolean)
	damage = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	defense = db.Column(db.Boolean)
	degree = db.Column(db.Boolean)
	env = db.Column(db.Boolean)
	minion = db.Column(db.Boolean)
	mod = db.Column(db.Boolean)
	move = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	sense = db.Column(db.Boolean)
	time = db.Column(db.Boolean)

	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'name': self.name,
			'cost': self.cost,
			'ranks': self.ranks,
			'des': self.des,
			'inherit': self.inherit,
			'alternate': self.alternate,
			'flat': self.flat,
			'stack': self.stack,
			'routine': self.routine,
			'power_rank': self.power_rank,
			'type': self.type,
			'required_check': self.required_check,
			'required': self.required,
			'required_power': self.required_power,
			'required_power_rank': self.required_power_rank,
			'variable': self.variable,
			'character': self.character,
			'circ': self.circ,
			'create': self.create,
			'damage': self.damage,
			'dc': self.dc,
			'defense': self.defense,
			'degree': self.degree,
			'env': self.env,
			'minion': self.minion,
			'mod': self.mod,
			'move': self.move,
			'opposed': self.opposed,
			'ranged': self.ranged,
			'sense': self.sense,
			'time': self.time,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base,
			'extra_effect_count': self.extra_effect_count,
			'extra_effect': self.extra_effect,
			'target': self.target,
			'target_type': self.target_type,
			'target_check': self.target_check,
			'action_check': self.action_check,
			'action': self.action,
			'action_type': self.action_type,
			'action_limit': self.action_limit,
			'skill_type': self.skill_type,
			'skill': self.skill,
			'range_check': self.range_check,
			'range': self.range,
			'auto': self.auto,
			'auto_type': self.auto_type,
			'auto_check': self.auto_check,
			'auto_check_type': self.auto_check_type,
			'auto_opposed': self.auto_opposed,
			'auto_opposed_type': self.auto_opposed_type,
			'ranks_check': self.ranks_check,
			'ranks_type': self.ranks_type,
			'rank': self.rank
		}

class PowerCost(db.Model):
	__tablename__ = 'power_cost'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	keyword = db.Column(db.String())
	cost = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	flat = db.Column(db.Boolean)
	extra = db.Column(db.Integer, db.ForeignKey('extras.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'keyword': self.keyword,
			'cost': self.cost,
			'rank': self.rank,
			'flat': self.flat,
			'extra': self.extra
		}

class PowerRanks(db.Model):
	__tablename__ = 'power_ranks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer)
	extra = db.Column(db.Integer, db.ForeignKey('extras.id'))
	unique = db.Column(db.Boolean)
	effect = db.Column(db.String())
	required = db.Column(db.Integer, db.ForeignKey('extras.id'))
	required_type = db.Column(db.String())
	exclusive = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'cost': self.cost,
			'ranks': self.ranks,
			'extra': self.extra,
			'unique': self.unique,
			'effect': self.effect,
			'required': self.required,
			'required_type': self.required_type,
			'exclusive': self.exclusive
		}

class PowerCheck(db.Model):
	__tablename__ = 'power_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	mod = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	trigger = db.Column(db.String())
	when = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	conflict_weapon = db.Column(db.Boolean)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	action_type = db.Column(db.String())
	action = db.Column(db.Integer)
	free = db.Column(db.Boolean)
	keyword = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('power_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('power_time_type.id'))
	dc_value = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	move = db.Column(db.Integer, db.ForeignKey('power_move_type.id'))
	ranged = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	attack = db.Column(db.Integer)
	opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	opposed_type = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_target = db.Column(db.String())
	conditions_target = db.Column(db.String())
	opponent = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	variable = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	opponent_type = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	variable_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	chained = db.Column(db.Boolean)
	effect = db.Column(db.Boolean)
	title = db.Column(db.String())
	multiple = db.Column(db.String())
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	sense_type = db.Column(db.String())
	sense_target = db.Column(db.String())
	mental = db.Column(db.Boolean)
	maneuver = db.Column(db.Integer, db.ForeignKey('maneuvers.id'))
	attack_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	consequence_target = db.Column(db.String())
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	consequence_mod = db.Column(db.Integer)
	consequence_null = db.Column(db.Boolean)
	defenseless = db.Column(db.Integer, db.ForeignKey('actions.id'))
	touch = db.Column(db.Boolean)
	target_type = db.Column(db.String())
	damage = db.Column(db.Boolean)
	primary = db.Column(db.Boolean)
	frequency = db.Column(db.String())
	overwrite = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	maintain_concentrate = db.Column(db.Boolean)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'target': self.target,
			'check_type': self.check_type,
			'mod': self.mod,
			'circumstance': self.circumstance,
			'trigger': self.trigger,
			'when': self.when,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'conflict': self.conflict,
			'conflict_range': self.conflict_range,
			'conflict_weapon': self.conflict_weapon,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'action_type': self.action_type,
			'action': self.action,
			'free': self.free,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'dc_value': self.dc_value,
			'time': self.time,
			'move': self.move,
			'ranged': self.ranged,
			'keyword': self.keyword,
			'attack': self.attack,
			'opposed': self.opposed,
			'opposed_type': self.opposed_type,
			'condition': self.condition,
			'condition_target': self.condition_target,
			'conditions_target': self.conditions_target,
			'opponent': self.opponent,
			'varible': self.variable,
			'opponent_type': self.opponent_type,
			'varible_type': self.variable_type,
			'chained': self.chained,
			'effect': self.effect,
			'title': self.title,
			'multiple': self.multiple,
			'sense': self.sense,
			'sense_type': self.sense_type,
			'sense_target': self.sense_target,
			'mental': self.mental,
			'maneuver': self.maneuver,
			'attack_range': self.attack_range,
			'consequence': self.consequence,
			'consequence_target': self.consequence_target,
			'consequence_mod': self.consequence_mod,
			'consequence_null': self.consequence_null,
			'defenseless': self.defenseless,
			'touch': self.touch,
			'target_type': self.target_type,
			'damage': self.damage,
			'primary': self.primary,
			'frequency': self.frequency,
			'overwrite': self.overwrite,
			'maintain_concentrate': self.maintain_concentrate,
			'descriptor': self.descriptor
		}




class PowerCirc(db.Model):
	__tablename__ = 'power_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	circ_target = db.Column(db.String())
	mod = db.Column(db.Integer)
	effect = db.Column(db.String())
	speed = db.Column(db.Integer)
	target = db.Column(db.String())
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition_type = db.Column(db.String())
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	conditions = db.Column(db.Integer)
	conditions_effect = db.Column(db.Integer)
	measure_effect = db.Column(db.String())
	measure_type = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.Integer)
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	keyword = db.Column(db.String())
	cumulative = db.Column(db.Boolean)
	optional = db.Column(db.Boolean)
	circumstance = db.Column(db.String())
	time_table = db.Column(db.Boolean)
	move_table = db.Column(db.Boolean)
	lasts = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	title = db.Column(db.Integer, db.ForeignKey('power_circ_type.id'))
	surface = db.Column(db.Boolean)
	tools = db.Column(db.String())
	materials = db.Column(db.String())
	max = db.Column(db.Integer)
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	trait_target = db.Column(db.String())
	environment = db.Column(db.Integer, db.ForeignKey('environments.id')) 
	nature = db.Column(db.Integer, db.ForeignKey('nature.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	ranged = db.Column(db.Boolean)
	descriptor_effect = db.Column(db.String())
	descriptor_target = db.Column(db.String())
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_grab = db.Column(db.String())
	rank = db.Column(db.Boolean)
	apply = db.Column(db.String())
	success = db.Column(db.String())
	success_bonus = db.Column(db.String())
	success_target = db.Column(db.String())
	success_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	success_check_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	success_check_bonus = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	success_check_type_bonus = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	success_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	success_opposed_type = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	success_opposed_bonus = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	success_opposed_type_bonus = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	success_bonus_trait_type = db.Column(db.String())
	success_bonus_trait = db.Column(db.Integer)
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'circ_target': self.circ_target,
			'mod': self.mod,
			'effect': self.effect,
			'speed': self.speed,
			'temp': self.temp,
			'target': self.target,
			'level_type': self.level_type,
			'level': self.level,
			'time': self.time,
			'condition_type': self.condition_type,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'conditions': self.conditions,
			'conditions_effect': self.conditions_effect,
			'measure_effect': self.measure_effect,
			'measure_type': self.measure_type,
			'measure_rank_value': self.measure_rank_value,
			'measure_rank': self.measure_rank,
			'unit_value': self.unit_value,
			'unit_type': self.unit_type,
			'unit': self.unit,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_trait_math': self.measure_trait_math,
			'measure_mod': self.measure_mod,
			'measure_math_rank': self.measure_math_rank,
			'keyword': self.keyword,
			'cumulative': self.cumulative,
			'optional': self.optional,
			'surface': self.surface,
			'circumstance': self.circumstance,
			'time_table': self.time_table,
			'move_table': self.move_table,
			'lasts': self.lasts,
			'title': self.title,
			'tools': self.tools,
			'materials': self.materials,
			'max': self.max,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'trait_target': self.trait_target,
			'environment': self.environment,
			'nature': self.nature,
			'check_type': self.check_type,
			'ranged': self.ranged,
			'descriptor_effect': self.descriptor_effect,
			'descriptor_target': self.descriptor_target,
			'descriptor': self.descriptor,
			'conflict': self.conflict,
			'conflict_grab': self.conflict_grab,
			'rank': self.rank,
			'apply': self.apply,
			'success': self.success,
			'success_bonus': self.success_bonus,
			'success_target': self.success_target,
			'success_check': self.success_check,
			'success_check_type': self.success_check_type,
			'success_check_bonus': self.success_check_bonus,
			'success_check_type_bonus': self.success_check_type_bonus,
			'success_opposed': self.success_opposed,
			'success_opposed_type': self.success_opposed_type,
			'success_opposed_bonus': self.success_opposed_bonus,
			'success_opposed_type_bonus': self.success_opposed_type_bonus,
			'success_bonus_trait_type': self.success_bonus_trait_type,
			'success_bonus_trait': self.success_bonus_trait
		}




class PowerDC(db.Model):
	__tablename__ = 'power_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	dc = db.Column(db.String())
	description = db.Column(db.String())
	value = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_trait_type = db.Column(db.String())
	math_trait = db.Column(db.Integer)
	surface = db.Column(db.Boolean)
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	damage = db.Column(db.Boolean)
	cover = db.Column(db.Boolean)
	complex = db.Column(db.Boolean)
	measure = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	action_no_damage = db.Column(db.Boolean)
	damage_type = db.Column(db.String())
	inflict_type = db.Column(db.String())
	inflict_flat = db.Column(db.Integer)
	inflict_trait_type = db.Column(db.String())
	inflict_trait = db.Column(db.Integer)
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	measure_effect = db.Column(db.String())
	measure_type = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.Integer)
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_trait_type_unit = db.Column(db.String())
	measure_trait_unit = db.Column(db.Integer)
	measure_trait_math_unit = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod_unit = db.Column(db.Integer)
	measure_math_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_turns = db.Column(db.Integer)
	condition_no_damage = db.Column(db.Boolean)
	condition_dead = db.Column(db.Integer)
	keyword = db.Column(db.String())
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))
	time_table = db.Column(db.Boolean)
	move_table = db.Column(db.Boolean)
	tools_check = db.Column(db.Boolean)
	cover_effect = db.Column(db.String())
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))
	conceal_effect = db.Column(db.String())
	conceal_type = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	tools = db.Column(db.String())
	variable_check = db.Column(db.Boolean)
	variable = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	title = db.Column(db.Integer, db.ForeignKey('power_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	effect_target = db.Column(db.String())
	equipment_use = db.Column(db.String())
	equipment_type = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	equip = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	descriptor_effect = db.Column(db.String())
	descriptor_target = db.Column(db.String())
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	descrip = db.Column(db.Boolean)
	ranks = db.Column(db.Boolean)
	rank = db.Column(db.Integer)
	ranks_per = db.Column(db.Integer)


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'target': self.target,
			'dc': self.dc,
			'description': self.description,
			'value': self.value,
			'mod': self.mod,
			'math_value': self.math_value,
			'math': self.math,
			'math_trait_type': self.math_trait_type,
			'math_trait': self.math_trait,
			'surface': self.surface,
			'condition': self.condition,
			'keyword_check': self.keyword_check,
			'levels': self.levels,
			'damage': self.damage,
			'cover': self.cover,
			'complex': self.complex,
			'measure': self.measure,
			'change_action': self.change_action,
			'conceal': self.conceal,
			'action': self.action,
			'action_when': self.action_when,
			'action_no_damage': self.action_no_damage,
			'damage_type': self.damage_type,
			'inflict_type': self.inflict_type,
			'inflict_flat': self.inflict_flat,
			'inflict_trait_type': self.inflict_trait_type,
			'inflict_trait': self.inflict_trait,
			'inflict_math': self.inflict_math,
			'inflict_mod': self.inflict_mod,
			'inflict_bonus': self.inflict_bonus,
			'damage_mod': self.damage_mod,
			'damage_consequence': self.damage_consequence,
			'measure_effect': self.measure_effect,
			'measure_type': self.measure_type,
			'measure_rank_value': self.measure_rank_value,
			'measure_rank': self.measure_rank,
			'unit_value': self.unit_value,
			'unit_type': self.unit_type,
			'unit': self.unit,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_trait_math': self.measure_trait_math,
			'measure_mod': self.measure_mod,
			'measure_math_rank': self.measure_math_rank,
			'measure_trait_type_unit': self.measure_trait_type_unit,
			'measure_trait_unit': self.measure_trait_unit,
			'measure_trait_math_unit': self.measure_trait_math_unit,
			'measure_mod_unit': self.measure_mod_unit,
			'measure_math_rank_unit': self.measure_math_unit,
			'level_type': self.level_type,
			'level': self.level,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'condition_turns': self.condition_turns,
			'condition_no_damage': self.condition_no_damage,
			'condition_dead': self.condition_dead,
			'keyword': self.keyword,
			'complexity': self.complexity,
			'time_table': self.time_table,
			'move_table': self.move_table,
			'tools_check': self.tools_check,
			'cover_effect': self.cover_effect,
			'cover_type': self.cover_type,
			'conceal_effect': self.conceal_effect,
			'conceal_type': self.conceal_type,
			'tools': self.tools,
			'variable_checK': self.variable_check,
			'variable': self.variable,
			'title': self.title,
			'effect_target': self.effect_target,
			'equipment_use': self.equipment_use,
			'equipment_type': self.equipment_type,
			'equipment': self.equipment,
			'equip': self.equip,
			'ranged': self.ranged,
			'descriptor_effect': self.descriptor_effect,
			'descriptor_target': self.descriptor_target,
			'descriptor': self.descriptor,
			'descrip': self.descrip,
			'ranks': self.ranks,
			'rank': self.rank,
			'ranks_per': self.ranks_per
		}

class PowerDegree(db.Model):
	__tablename__ = 'power_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	value = db.Column(db.Integer)
	type = db.Column(db.String())
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	time = db.Column(db.Integer)
	recovery = db.Column(db.Boolean)
	damage_type = db.Column(db.String())
	object = db.Column(db.Integer)
	object_effect = db.Column(db.String())
	inflict_type = db.Column(db.String())
	inflict_flat = db.Column(db.Integer)
	inflict_trait_type = db.Column(db.String())
	inflict_trait = db.Column(db.Integer)
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	consequence_action_type = db.Column(db.String())
	consequence_action = db.Column(db.Integer)
	consequence_trait_type = db.Column(db.String())
	consequence_trait = db.Column(db.Integer)
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	knowledge = db.Column(db.String())
	knowledge_count = db.Column(db.Integer)
	knowledge_specificity = db.Column(db.String())
	knowledge_mind = db.Column(db.String())
	knowledge_mind_count = db.Column(db.Integer)
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	level_direction = db.Column(db.Integer)
	level_time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	circumstance = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	circ_target = db.Column(db.String())
	measure_effect = db.Column(db.String())
	measure_type = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.Integer)
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_trait_type_unit = db.Column(db.String())
	measure_trait_unit = db.Column(db.Integer)
	measure_trait_math_unit = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod_unit = db.Column(db.Integer)
	measure_math_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition_degree = db.Column(db.Boolean)
	condition_incurable = db.Column(db.Boolean)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_turns = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	condition_inflict = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_inflict_descriptor  = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	nullify_type = db.Column(db.String())
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	variable = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	resist_dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.Integer)
	skill_dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	skill_trait_type = db.Column(db.String())
	skill_trait = db.Column(db.Integer)
	routine_trait_type = db.Column(db.String())
	routine_trait = db.Column(db.Integer)
	routine_mod = db.Column(db.Integer)
	attack = db.Column(db.Integer)
	attack_turns = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	compare = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	time_table = db.Column(db.Boolean)
	move_table = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	description = db.Column(db.String())
	effect_target = db.Column(db.String())
	value_type = db.Column(db.String())
	description = db.Column(db.String())
	ranged = db.Column(db.Boolean)
	descriptor_effect = db.Column(db.String())
	descriptor_target = db.Column(db.String())
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	effect = db.Column(db.String())
	effect_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	effect_descriptor_type = db.Column(db.String())
	effect_descriptor_count = db.Column(db.Integer)
	effect_power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	effect_acute = db.Column(db.Boolean)
	fail = db.Column(db.Boolean)
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	weaken_type = db.Column(db.String())
	weaken_max = db.Column(db.Integer)
	weaken_val = db.Column(db.Integer)
	reverse_type = db.Column(db.String())
	reverse = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	communication_acute = db.Column(db.Boolean)
	restore = db.Column(db.String())
	restore_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	restore_val = db.Column(db.Integer)
	no_reattempt_time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	no_reattempt_effort = db.Column(db.Boolean)
	reattempt_effort = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'target': self.target,
			'value': self.value,
			'type': self.type,
			'action': self.action,
			'time': self.time,
			'recovery': self.recovery,
			'damage_type': self.damage_type,
			'object': self.object,
			'object_effect': self.object_effect,
			'inflict_type': self.inflict_type,
			'inflict_flat': self.inflict_flat,
			'inflict_trait_type': self.inflict_trait_type,
			'inflict_trait': self.inflict_trait,
			'inflict_math': self.inflict_math,
			'inflict_mod': self.inflict_mod,
			'inflict_bonus': self.inflict_bonus,
			'damage_mod': self.damage_mod,
			'damage_consequence': self.damage_consequence,
			'consequence_action_type': self.consequence_action_type,
			'consequence_action': self.consequence_action,
			'consequence_trait_type': self.consequence_trait_type,
			'consequence_trait': self.consequence_trait,
			'consequence': self.consequence,
			'knowledge': self.knowledge,
			'knowledge_count': self.knowledge_count,
			'knowledge_specificity': self.knowledge_specificity,
			'knowledge_mind': self.knowledge_mind,
			'knowledge_mind_count': self.knowledge_mind_count,
			'level_type': self.level_type,
			'level': self.level,
			'level_direction': self.level_direction,
			'circumstance': self.circumstance,
			'circ_target': self.circ_target,
			'measure_effect': self.measure_effect,
			'measure_type': self.measure_type,
			'measure_rank_value': self.measure_rank_value,
			'measure_rank': self.measure_rank,
			'unit_value': self.unit_value,
			'unit_type': self.unit_type,
			'unit': self.unit,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_trait_math': self.measure_trait_math,
			'measure_mod': self.measure_mod,
			'measure_math_rank': self.measure_math_rank,
			'measure_trait_type_unit': self.measure_trait_type_unit,
			'measure_trait_unit': self.measure_trait_unit,
			'measure_trait_math_unit': self.measure_trait_math_unit,
			'measure_mod_unit': self.measure_mod_unit,
			'measure_math_rank_unit': self.measure_math_unit,
			'condition_type': self.condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition_degree': self.condition_degree,
			'condition_incurable': self.condition_incurable,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'condition_turns': self.condition_turns,
			'condition_inflict': self.condition_inflict,
			'condition_inflict_descriptor': self.condition_inflict_descriptor,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'nullify_type': self.nullify_type,
			'cumulative': self.cumulative,
			'linked': self.linked,
			'check_type': self.check_type,
			'opposed': self.opposed,
			'variable': self.variable,
			'resist_dc': self.resist_dc,
			'resist_trait_type': self.resist_trait_type,
			'resist_trait': self.resist_trait,
			'skill_dc': self.skill_dc,
			'skill_trait_type': self.skill_trait_type,
			'skill_trait': self.skill_trait,
			'routine_trait_type': self.routine_trait_type,
			'routine_trait': self.routine_trait,
			'routine_mod': self.routine_mod,
			'attack': self.attack,
			'attack_turns': self.attack_turns,
			'compare': self.compare,
			'time_table': self.time_table,
			'move_table': self.move_table,
			'title': self.title,
			'description': self.description,
			'effect_target': self.effect_target,
			'value_type': self.value_type,
			'description': self.description,
			'ranged': self.ranged,
			'descriptor_effect': self.descriptor_effect,
			'descriptor_target': self.descriptor_target,
			'descriptor': self.descriptor,
			'effect': self.effect,
			'effect_descriptor': self.effect_descriptor,
			'effect_descriptor_type': self.effect_descriptor_type,
			'effect_descriptor_count': self.effect_descriptor_count,
			'effect_power': self.effect_power,
			'effect_acute': self.effect_acute,
			'fail': self.fail,
			'null_condition': self.null_condition,
			'weaken_type': self.weaken_type,
			'weaken_val': self.weaken_val,
			'weaken_max': self.weaken_max,
			'reverse_type': self.reverse_type,
			'reverse': self.reverse,
			'communication_acute': self.communication_acute,
			'restore': self.restore,
			'restore_descriptor': self.restore_descriptor,
			'restore_val': self.restore_val,
			'no_reattempt_time': self.no_reattempt_time,
			'no_reattempt_effort': self.no_reattempt_effort,
			'reattempt_effort': self.reattempt_effort
		}




class PowerMove(db.Model):
	__tablename__ = 'power_movement'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	speed = db.Column(db.String())
	speed_rank = db.Column(db.Integer)
	speed_max = db.Column(db.Integer)
	speed_mod = db.Column(db.String())
	speed_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	speed_rank_mod = db.Column(db.Integer)
	speed_penalty = db.Column(db.Integer)
	speed_trait_type = db.Column(db.String())
	speed_trait = db.Column(db.Integer)
	speed_math1 = db.Column(db.Integer, db.ForeignKey('math.id'))
	speed_value1 = db.Column(db.Integer)
	speed_math2 = db.Column(db.Integer, db.ForeignKey('math.id'))
	speed_value2 = db.Column(db.Integer)
	speed_description = db.Column(db.String())
	distance = db.Column(db.String())
	distance_rank = db.Column(db.Integer)
	distance_value = db.Column(db.Integer)
	distance_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	distance_rank_trait_type = db.Column(db.String())
	distance_rank_trait = db.Column(db.Integer)
	distance_rank_math1 = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_rank_value1 = db.Column(db.Integer)
	distance_rank_math2 = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_rank_value2 = db.Column(db.Integer)
	distance_unit_trait_type = db.Column(db.String())
	distance_unit_trait = db.Column(db.Integer)
	distance_unit_math1 = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_unit_value1 = db.Column(db.Integer)
	distance_unit_math2 = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_unit_value2 = db.Column(db.Integer)
	distance_math_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	distance_description = db.Column(db.String())
	distance_max = db.Column(db.Boolean)
	direction = db.Column(db.String())
	turns = db.Column(db.Integer)
	degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	keyword = db.Column(db.String())
	title = db.Column(db.Integer, db.ForeignKey('power_move_type.id'))

	speed_per = db.Column(db.Boolean)
	distance_per = db.Column(db.Boolean)
	flight = db.Column(db.Boolean)
	aquatic = db.Column(db.Boolean)
	ground = db.Column(db.Boolean)
	special = db.Column(db.Boolean)
	condition_check = db.Column(db.Boolean)
	obstacles = db.Column(db.Boolean)
	objects = db.Column(db.Boolean)
	permeate = db.Column(db.Boolean)
	prone = db.Column(db.Boolean)
	equip = db.Column(db.Boolean)
	concealment = db.Column(db.Boolean)
	extended = db.Column(db.Boolean)
	mass = db.Column(db.Boolean)
	flight_resist = db.Column(db.Boolean)
	flight_resist_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	flight_equip = db.Column(db.Boolean)
	flight_equip_type = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	flight_equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	flight_conditions = db.Column(db.ARRAY(db.Integer))
	acquatic_type = db.Column(db.String())
	acquatic_prone = db.Column(db.Boolean)
	ground_type = db.Column(db.Integer, db.ForeignKey('ground.id'))
	ground_perm = db.Column(db.String())
	ground_time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	ground_ranged = db.Column(db.Boolean)
	ground_range = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	special_type = db.Column(db.String())
	teleport_type = db.Column(db.String())
	teleport_change = db.Column(db.String())
	teleport_portal = db.Column(db.Boolean)
	teleport_obstacles = db.Column(db.Boolean)
	dimension_type = db.Column(db.String())
	dimension_mass_rank = db.Column(db.Integer)
	dimension_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	special_space = db.Column(db.String())
	special_time = db.Column(db.String())
	special_time_carry = db.Column(db.Integer)
	condition = db.Column(db.ARRAY(db.Integer))
	condition_circ = db.Column(db.Boolean)
	condition_circ_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	objects_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	objects_direction = db.Column(db.String())
	objects_damage = db.Column(db.Boolean)
	object_damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	objects_strength = db.Column(db.Integer)
	permeate_type = db.Column(db.String())
	permeate_speed = db.Column(db.Integer)
	permeate_cover = db.Column(db.Boolean)
	permeate_condition_solid = db.Column(db.Boolean)
	equip_type = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	equip_improvise = db.Column(db.Boolean)
	concealment_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	conceal_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	extended_actions = db.Column(db.Integer)
	mass_value = db.Column(db.Integer)
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	trackless = db.Column(db.Boolean)
	multiple = db.Column(db.String())

	
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'speed': self.speed,
			'speed_rank': self.speed_rank,
			'speed_max': self.speed_max,
			'speed_mod': self.speed_mod,
			'speed_math': self.speed_math,
			'speed_rank_mod': self.speed_rank_mod,
			'speed_penalty': self.speed_penalty,
			'speed_trait_type': self.speed_trait_type,
			'speed_trait': self.speed_trait,
			'speed_math1': self.speed_math1,
			'speed_value1': self.speed_value1,
			'speed_math2': self.speed_math2,
			'speed_value2': self.speed_value2,
			'speed_description': self.speed_description,
			'distance': self.distance,
			'distance_rank': self.distance_rank,
			'distance_value': self.distance_value,
			'distance_units': self.distance_units,
			'distance_rank_trait_type': self.distance_rank_trait_type,
			'distance_rank_trait': self.distance_rank_trait,
			'distance_rank_math1': self.distance_rank_math1,
			'distance_rank_value1': self.distance_rank_value1,
			'distance_rank_math2': self.distance_rank_math2,
			'distance_rank_value2': self.distance_rank_value2,
			'distance_unit_trait_type': self.distance_unit_trait_type,
			'distance_unit_trait': self.distance_unit_trait,
			'distance_unit_math1': self.distance_unit_math1,
			'distance_unit_value1': self.distance_unit_value1,
			'distance_unit_math2': self.distance_unit_math2,
			'distance_unit_value2': self.distance_unit_value2,
			'distance_math_units': self.distance_math_units,
			'distance_description': self.distance_description,
			'distance_max': self.distance_max,
			'direction': self.direction,
			'turns': self.turns,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'time': self.time,
			'keyword': self.keyword,
			'title': self.title,
			'speed_per': self.speed_per,
			'distance_per': self.distance_per,
			'flight': self.flight,
			'aquatic': self.aquatic,
			'ground': self.ground,
			'special': self.special,
			'condition_check': self.condition_check,
			'obstacles': self.obstacles,
			'objects': self.objects,
			'permeate': self.permeate,
			'prone': self.prone,
			'equip': self.equip,
			'concealment': self.concealment,
			'extended': self.extended,
			'mass': self.mass,
			'flight_resist': self.flight_resist,
			'flight_resist_check': self.flight_resist_check,
			'flight_equip': self.flight_equip,
			'flight_equip_type': self.flight_equip_type,
			'flight_equipment': self.flight_equipment,
			'flight_conditions': self.flight_conditions,
			'acquatic_type': self.acquatic_type,
			'acquatic_prone': self.acquatic_prone,
			'ground_type': self.ground_type,
			'ground_perm': self.ground_perm,
			'ground_time': self.ground_time,
			'ground_ranged': self.ground_ranged,
			'ground_range': self.ground_range,
			'special_type': self.special_type,
			'teleport_type': self.teleport_type,
			'teleport_change': self.teleport_change,
			'teleport_portal': self.teleport_portal,
			'teleport_obstacles': self.teleport_obstacles,
			'dimension_type': self.dimension_type,
			'dimension_mass_rank': self.dimension_mass_rank,
			'dimension_descriptor': self.dimension_descriptor,
			'special_space': self.special_space,
			'special_time': self.special_time,
			'special_time_carry': self.special_time_carry,
			'condition': self.condition,
			'condition_circ': self.condition_circ,
			'condition_circ_check': self.condition_circ_check,
			'objects_check': self.objects_check,
			'objects_direction': self.objects_direction,
			'objects_damage': self.object_damage,
			'object_damage': self.object_damage,
			'objects_strength': self.objects_strength,
			'permeate_type': self.permeate_type,
			'permeate_speed': self.permeate_speed,
			'permeate_cover': self.permeate_cover,
			'permeate_condition_solid': self.permeate_condition_solid,
			'equip_type': self.equip_type,
			'equipment': self.equipment,
			'equip_improvise': self.equip_improvise,
			'concealment_sense': self.concealment_sense,
			'conceal_opposed': self.conceal_opposed,
			'extended_actions': self.extended_actions,
			'mass_value': self.mass_value,
			'cost': self.cost,
			'ranks': self.ranks,
			'trackless': self.trackless,
			'multiple': multiple
		}



class PowerOpposed(db.Model):
	__tablename__ = 'power_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	attached = db.Column(db.String())
	frequency = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.Integer)
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	player_secret = db.Column(db.Boolean)
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	secret = db.Column(db.Boolean)
	recurring = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	recurring_value = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	description = db.Column(db.String())
	keyword = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	degree_check = db.Column(db.Boolean)
	circ_check = db.Column(db.Boolean)
	dc_check = db.Column(db.Boolean)
	time_check = db.Column(db.Boolean)
	degree_value = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('power_dc_type.id'))
	dc_player = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	circ_value = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	time_type = db.Column(db.Integer, db.ForeignKey('power_time_type.id'))
	recurring_type = db.Column(db.Integer, db.ForeignKey('power_time_type.id'))
	recurring_degree_type = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	recurring_fail = db.Column(db.Boolean)
	variable = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	chained = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	opponent = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	opposed = db.Column(db.Integer, db.ForeignKey('power_opposed.id'))
	variable_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	before = db.Column(db.String())
	after = db.Column(db.String())
	primary = db.Column(db.Boolean)
	attack_player = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	attack_opp = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	turn = db.Column(db.String())


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'attached': self.attached,
			'frequency': self.frequency,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'opponent_trait_type': self.opponent_trait_type,
			'opponent_trait': self.opponent_trait,
			'opponent_mod': self.opponent_mod,
			'player_check': self.player_check,
			'player_secret': self.player_secret,
			'opponent_check': self.opponent_check,
			'secret': self.secret,
			'recurring': self.recurring,
			'multiple': self.multiple,
			'recurring_value': self.recurring_value,
			'recurring_units': self.recurring_units,
			'description': self.description,
			'keyword': self.keyword,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'time': self.time,
			'degree_check': self.degree_check,
			'circ_check': self.circ_check,
			'dc_check': self.dc_check,
			'time_check': self.time_check,
			'degree_value': self.degree_value,
			'dc_type': self.dc_type,
			'dc_player': self.dc_player,
			'circ_value': self.circ_value,
			'time_type': self.time_type,
			'recurring_type': self.recurring_type,
			'recurring_degree_type': self.recurring_degree_type,
			'recurring_fail': self.recurring_fail,
			'variable': self.variable,
			'chained': self.chained,
			'title': self.title,
			'opponent': self.opponent,
			'opposed': self.opposed,
			'variable_type': self.variable_type,
			'before': self.before,
			'after': self.after,
			'primary': self.primary,
			'attack_player': self.attack_player,
			'attack_opp': self.attack_opp,
			'turn': self.turn
		}



class PowerTime(db.Model):
	__tablename__ = 'power_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	type = db.Column(db.String())
	value_type = db.Column(db.String())
	rank1 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	rank1_value = db.Column(db.Integer)
	rank_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	rank2 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	rank2_value = db.Column(db.Integer)
	value = db.Column(db.Integer)
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_value = db.Column(db.Integer)
	math_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	recovery_penalty = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)
	recovery_target = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	turns = db.Column(db.Integer)
	keyword = db.Column(db.String)
	perm = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	round = db.Column(db.Boolean)
	next = db.Column(db.Boolean)
	scene = db.Column(db.Boolean)
	instant = db.Column(db.Boolean)
	never = db.Column(db.Boolean)
	player = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	maintain = db.Column(db.Boolean)
	check = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('power_time_type.id'))
	circ_type = db.Column(db.Integer, db.ForeignKey('power_circ_type.id'))
	degree_type = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('power_dc_type.id'))
	time = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	measure_type = db.Column(db.String())
	rank = db.Column(db.Boolean)
	factor = db.Column(db.Integer)
	reattempt_effort = db.Column(db.Boolean)
	check_type = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	on_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	points = db.Column(db.Integer)
	value_rank = db.Column(db.Boolean)
	
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id':self.extra_id,
			'type': self.type,
			'value_type': self.value_type,
			'rank1': self.rank1,
			'rank1_value': self.rank1_value,
			'rank_math': self.rank_math,
			'rank2': self.rank2,
			'rank2_value': self.rank2_value,
			'value': self.value,
			'units': self.units,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'math': self.math,
			'math_value': self.math_value,
			'math_units': self.math_units,
			'recovery_penalty': self.recovery_penalty,
			'recovery_incurable': self.recovery_incurable,
			'recovery_target': self.recovery_target,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'turns': self.turns,
			'keyword': self.keyword,
			'perm': self.perm,
			'turn': self.turn,
			'round': self.round,
			'next': self.next,
			'scene': self.scene,
			'instant': self.instant,
			'player': self.player,
			'gm': self.gm,
			'maintain': self.maintain,
			'check': self.check,
			'hide': self.hidden,
			'title': self.title,
			'circ_type': self.circ_type,
			'degree_type': self.degree_type,
			'dc_type': self.dc_type,
			'time': self.time,
			'mod': self.mod,
			'measure_type': self.measure_type,
			'rank': self.rank,
			'factor': self.factor,
			'reattempt_effort': self.reattempt_effort,
			'check_type': self.check_type,
			'action': self.action,
			'on_check': self.on_check,
			'points': self.points,
			'value_rank': self.value_rank,
			'never': self.never
		}


class PowerAction(db.Model):
	__tablename__ = 'power_change_action'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	mod = db.Column(db.Integer)
	objects = db.Column(db.Boolean)
	circumstance = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'action': self.action,
			'mod': self.mod,
			'objects': self.objects,
			'circumstance': self.circumstance
		}

class PowerChar(db.Model):
	__tablename__ = 'power_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	value = db.Column(db.Integer)
	increase = db.Column(db.Integer)
	limited = db.Column(db.Boolean)
	reduced = db.Column(db.Boolean)
	limbs = db.Column(db.Boolean)
	carry = db.Column(db.Boolean)
	sustained = db.Column(db.Boolean)
	permanent = db.Column(db.Boolean)
	points = db.Column(db.Boolean)
	appear = db.Column(db.Boolean)
	insubstantial = db.Column(db.Boolean)
	weaken = db.Column(db.Boolean)
	weaken_type = db.Column(db.String())
	weaken_opposed_type = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	weaken_degree_type = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	weaken_trait_type = db.Column(db.String())
	weaken_trait = db.Column(db.Integer)
	weaken_broad = db.Column(db.String())
	weaken_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))	
	weaken_simultaneous = db.Column(db.Boolean)
	limited_by = db.Column(db.String())
	limited_other = db.Column(db.String())
	limited_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	limited_emotion_other = db.Column(db.String())
	reduced_trait_type = db.Column(db.String())
	reduced_trait = db.Column(db.Integer)
	reduced_value = db.Column(db.Integer)
	reduced_rank = db.Column(db.Integer)
	reduced_full = db.Column(db.Boolean)
	limbs_count = db.Column(db.Integer)
	limbs_rank = db.Column(db.Boolean)
	limbs_continuous = db.Column(db.Boolean)
	limbs_sustained = db.Column(db.Boolean)
	limbs_projection = db.Column(db.Boolean)
	limbs_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	limbs_duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	carry_capacity = db.Column(db.Integer)
	carry_internal = db.Column(db.Boolean)
	carry_mass = db.Column(db.Integer)
	points_type = db.Column(db.String())
	points_value = db.Column(db.Integer)
	points_trait_type = db.Column(db.String())
	points_trait = db.Column(db.Integer)
	points_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	appear_form = db.Column(db.String())
	appear_target = db.Column(db.String())
	appear_description = db.Column(db.String())
	appear_creature = db.Column(db.Integer, db.ForeignKey('creature.id'))
	appear_creature_narrow = db.Column(db.Integer, db.ForeignKey('creature_narrow.id'))
	appear_costume = db.Column(db.Boolean)
	insub_type = db.Column(db.String())
	insub_description = db.Column(db.String())
	insub_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))	
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	multiple = db.Column(db.String())
	meta = db.Column(db.Boolean)
	metamorph = db.Column(db.Integer)
	penalty = db.Column(db.Boolean)
	bonus = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'value': self.value,
			'increase': self.increase,
			'limited': self.limited,
			'reduced': self.reduced,
			'limbs': self.limbs,
			'carry': self.carry,
			'sustained': self.sustained,
			'permanent': self.permanent,
			'points': self.points,
			'appear': self.appear,
			'insubstantial': self.insubstantial,
			'weaken': self.weaken,
			'weaken_type': self.weaken_type,
			'weaken_opposed_type': self.weaken_opposed_type,
			'weaken_degree_type': self.weaken_degree_type,
			'weaken_trait_type': self.weaken_trait_type,
			'weaken_trait': self.weaken_trait,
			'weaken_broad': self.weaken_broad,
			'weaken_descriptor': self.weaken_descriptor,
			'weaken_simultaneous': self.weaken_simultaneous,
			'limited_by': self.limited_by,
			'limited_other': self.limited_other,
			'limited_emotion': self.limited_emotion,
			'limited_emotion_other': self.limited_emotion_other,
			'reduced_trait_type': self.reduced_trait_type,
			'reduced_trait': self.reduced_trait,
			'reduced_value': self.reduced_value,
			'reduced_rank': self.reduced_rank,
			'reduced_full': self.reduced_full,
			'limbs_count': self.limbs_count,
			'limbs_rank': self.limbs_rank,
			'limbs_condition': self.limbs_condition,
			'limbs_continuous': self.limbs_continuous,
			'limbs_sustained': self.limbs_sustained,
			'limbs_projection': self.limbs_projection,
			'limbs_duration': self.limbs_duration,
			'carry_capacity': self.carry_capacity,
			'carry_internal': self.carry_internal,
			'carry_mass': self.carry_mass,
			'points_type': self.points_type,
			'points_value': self.points_value,
			'points_trait_type': self.points_trait_type,
			'points_trait': self.points_trait,
			'points_descriptor': self.points_descriptor,
			'appear_form': self.appear_form,
			'appear_target': self.appear_target,
			'appear_description': self.appear_description,
			'appear_creature': self.appear_creature,
			'appear_creature_narrow': self.appear_creature_narrow,
			'appear_costume': self.appear_costume,
			'insub_type': self.insub_type,
			'insub_descriptor': self.insub_descriptor,
			'insub_description': self.insub_description,
			'cost': self.cost,
			'ranks': self.ranks,
			'multiple': self.multiple,
			'meta': self.meta,
			'metamorph': self.metamorph,
			'penalty': self.penalty,
			'bonus': self.bonus
		}

class PowerCondition(db.Model):
	__tablename__ = 'power_condition'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target =  db.Column(db.String())
	condition_type = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_null = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	damage_value = db.Column(db.Integer)
	damage = db.Column(db.Integer)
	time_effect = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	time_last = db.Column(db.Integer, db.ForeignKey('power_time.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'condition_type': self.condition_type,
			'condition': self.condition,
			'condition_null': self.condition_null,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'damage_value': self.damage_value,
			'damage': self.damage,
			'time_effect': self.time_effect,
			'time_last': self.time_last
		}

class PowerCreate(db.Model):
	__tablename__ = 'power_create'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	solidity = db.Column(db.String())
	visibility = db.Column(db.String())
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))
	volume = db.Column(db.Integer)
	toughness = db.Column(db.Integer)
	mass = db.Column(db.Integer)
	damageable = db.Column(db.Boolean)
	maintained = db.Column(db.Boolean)
	repairable = db.Column(db.Boolean)
	moveable = db.Column(db.Boolean)
	stationary = db.Column(db.Boolean)
	trap = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	weapon = db.Column(db.Boolean)
	support = db.Column(db.Boolean)
	real = db.Column(db.Boolean)
	cover = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	incoming = db.Column(db.Boolean)
	outgoing = db.Column(db.Boolean)
	transform = db.Column(db.Boolean)
	transform_type = db.Column(db.String())
	transform_start_mass = db.Column(db.Integer)
	transfom_mass = db.Column(db.Integer)
	transform_start_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	transform_end_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	move_player = db.Column(db.String())
	move_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	move_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	move_opponent_check = db.Column(db.Boolean)
	trap_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	trap_resist = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	trap_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	trap_escape = db.Column(db.Boolean)
	support_strength = db.Column(db.Integer)
	support_strengthen = db.Column(db.Boolean)
	support_action = db.Column(db.Integer)
	support_action_rounds = db.Column(db.Integer)
	support_effort = db.Column(db.Integer)
	support_effort_rounds = db.Column(db.Integer)
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	ranged_damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	ranged_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	weapon_damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	multiple = db.Column(db.String())
	duration = db.Column(db.Boolean)
	duration_type = db.Column(db.String())
	duration_innate = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'solidity': self.solidity,
			'visibility': self.visibility,
			'complexity': self.complexity,
			'volume': self.volume,
			'toughness': self.toughness,
			'mass': self.mass,
			'damageable': self.damageable,
			'maintained': self.maintained,
			'repairable': self.repairable,
			'moveable': self.moveable,
			'stationary': self.stationary,
			'trap': self.trap,
			'ranged': self.ranged,
			'weapon': self.weapon,
			'support': self.support,
			'real': self.real,
			'cover': self.cover,
			'conceal': self.conceal,
			'incoming': self.incoming,
			'outgoing': self.outgoing,
			'transform': self.transform,
			'transform_type': self.transform_type,
			'transform_start_mass': self.transform_start_mass,
			'transfom_mass': self.transfom_mass,
			'transform_start_descriptor': self.transform_start_descriptor,
			'transform_end_descriptor': self.transform_end_descriptor,
			'move_player': self.move_player,
			'move_check': self.move_check,
			'move_opponent_check': self.move_opponent_check,
			'move_opposed': self.move_opposed,
			'trap_check': self.trap_check,
			'trap_resist': self.trap_resist,
			'trap_opposed': self.trap_opposed,
			'trap_escape': self.trap_escape,
			'weapon_damage': self.weapon_damage,
			'support_strength': self.support_strength,
			'support_strengthen': self.support_strengthen,
			'support_action': self.support_action,
			'support_action_rounds': self.support_action_rounds,
			'support_effort': self.support_effort,
			'support_effort_rounds': self.support_effort_rounds,
			'cost': self.cost,
			'ranks': self.ranks,
			'ranged_damage': self.ranged_damage,
			'ranged_check': self.ranged_check,
			'duration': self.duration,
			'duration_type': self.duration_type,
			'duration_innate': self.duration_innate
		}

class PowerDamage(db.Model):
	__tablename__ = 'power_damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	keyword = db.Column(db.String())
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	strength_based = db.Column(db.String())
	damage_type = db.Column(db.ARRAY(db.Integer))
	descriptor = db.Column(db.ARRAY(db.Integer))
	ranged = db.Column(db.Boolean)
	movement = db.Column(db.Boolean)
	value_type = db.Column(db.String())
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	effect = db.Column(db.Boolean)
	check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	applied = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'keyword': self.keyword,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'strength': self.strength,
			'strength_based': self.strength_based,
			'damage_type': self.damage_type,
			'descriptor': self.descriptor,
			'ranged': self.ranged,
			'movement': self.movement,
			'value_type': self.value_type,
			'math': self.math,
			'effect': self.effect,
			'multiple': self.multiple,
			'check': self.check,
			'check_type': self.check_type,
			'applied': applied
		}


class PowerDefense(db.Model):
	__tablename__ = 'power_defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
	use = db.Column(db.String())
	mod = db.Column(db.Integer)
	roll = db.Column(db.Integer)
	outcome = db.Column(db.String())
	dodge = db.Column(db.Boolean)
	fortitude = db.Column(db.Boolean)
	parry = db.Column(db.Boolean)
	toughness = db.Column(db.Boolean)
	will = db.Column(db.Boolean)
	resist_area = db.Column(db.Boolean)
	resist_perception = db.Column(db.Boolean)
	reflect = db.Column(db.Boolean)
	immunity = db.Column(db.Boolean)
	reflect_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	redirect = db.Column(db.Boolean)
	reflect_immune = db.Column(db.Boolean)
	immunity_type = db.Column(db.String())
	immunity_trait_type = db.Column(db.String())
	immunity_trait = db.Column(db.Integer)
	immunity_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	immunity_descriptor_type = db.Column(db.String())
	immunity_descriptor_count = db.Column(db.Integer)
	immunity_damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	immunity_rule = db.Column(db.String())
	cover_check = db.Column(db.Boolean)
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))
	immunity_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	immunity_suffocate = db.Column(db.String())
	immunity_fall_surface = db.Column(db.Boolean)
	immunity_fall_stop = db.Column(db.Boolean)
	immunity_env = db.Column(db.String())
	immunity_temp = db.Column(db.Integer, db.ForeignKey('environment_condition.id'))
	immunity_extremity = db.Column(db.String())
	immunity_environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	immunity_env_penalty = db.Column(db.Boolean)
	immunity_env_circumstance = db.Column(db.Boolean)
	immunity_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	immunity_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	immunity_toxic = db.Column(db.Boolean)
	immunity_except = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	force = db.Column(db.Boolean)
	force_imperv = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'defense': self.defense,
			'use': self.use,
			'mod': self.mod,
			'roll': self.roll,
			'outcome': self.outcome,
			'dodge': self.dodge,
			'fortitude': self.fortitude,
			'parry': self.parry,
			'toughness': self.toughness,
			'will': self.will,
			'resist_area': self.resist_area,
			'resist_perception': self.resist_perception,
			'reflect': self.reflect,
			'immunity': self.immunity,
			'reflect_check': self.reflect_check,
			'redirect': self.redirect,
			'reflect_immune': self.reflect_immune,
			'immunity_type': self.immunity_type,
			'immunity_trait_type': self.immunity_trait_type,
			'immunity_trait': self.immunity_trait,
			'immunity_descriptor': self.immunity_descriptor,
			'immunity_descriptor_type': self.immunity_descriptor_type,
			'immunity_descriptor_count': self.immunity_descriptor_count,
			'immunity_damage': self.immunity_damage,
			'immunity_rule': self.immunity_rule,
			'cover_check': self.cover_check,
			'cover_type': self.cover_type,
			'immunity_consequence': self.immunity_consequence,
			'immunity_suffocate': self.immunity_suffocate,
			'immunity_fall_surface': self.immunity_fall_surface,
			'immunity_fall_stop': self.immunity_fall_stop,
			'immunity_env': self.immunity_env,
			'immunity_temp': self.immunity_temp,
			'immunity_extremity': self.immunity_extremity,
			'immunity_environment': self.immunity_environment,
			'immunity_env_penalty': self.immunity_env_penalty,
			'immunity_env_circumstance': self.immunity_env_circumstance,
			'immunity_condition': self.immunity_condition,
			'immunity_emotion': self.immunity_emotion,
			'immunity_toxic': self.immunity_toxic,
			'immunity_except': self.immunity_except,
			'multiple': self.multiple,
			'cost': self.cost,
			'ranks': self.ranks,
			'force_imperv': self.force_imperv,
			'force': self.force
		}


class PowerEnv(db.Model):
	__tablename__ = 'power_environment'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	radius = db.Column(db.Integer)
	distance = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	condition_check = db.Column(db.Boolean)
	impede = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	visibility = db.Column(db.Boolean)
	selective = db.Column(db.Boolean)
	immunity = db.Column(db.Boolean)
	immunity_type = db.Column(db.String())
	temp_type = db.Column(db.String())
	immunity_extremity = db.Column(db.String())
	immunity_environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	immunity_environment_other = db.Column(db.String())
	no_penalty = db.Column(db.Boolean)
	no_circumstance = db.Column(db.Boolean)
	immunity_other = db.Column(db.String())
	condition_temp_type = db.Column(db.String())
	condition_selective = db.Column(db.Boolean)
	temp_extremity = db.Column(db.String())
	move_nature = db.Column(db.Integer, db.ForeignKey('nature.id'))
	move_speed = db.Column(db.Integer)
	move_cost_circ = db.Column(db.Boolean)
	move_other = db.Column(db.String())
	conceal_type = db.Column(db.String())
	darkness_descriptor = db.Column(db.Boolean)
	light_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	visibility_trait_type = db.Column(db.String())
	visibility_trait = db.Column(db.Integer)
	visibility_mod = db.Column(db.Integer)
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	elements = db.Column(db.Boolean)
	element = db.Column(db.Integer, db.ForeignKey('elements.id'))
	element_strength = db.Column(db.Integer)
	element_mass  =  db.Column(db.Integer)
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'radius': self.radius,
			'distance': self.distance,
			'rank': self.rank,
			'condition_check': self.condition_check,
			'impede': self.impede,
			'conceal': self.conceal,
			'visibility': self.visibility,
			'selective': self.selective,
			'immunity': self.immunity,
			'immunity_type': self.immunity_type,
			'temp_type': self.temp_type,
			'immunity_extremity': self.immunity_extremity,
			'immunity_environment': self.immunity_environment,
			'immunity_environment_other': self.immunity_environment_other,
			'no_penalty': self.no_penalty,
			'no_circumstance': self.no_circumstance,
			'immunity_other': self.immunity_other,
			'condition_temp_type': self.condition_temp_type,
			'condition_selective': self.condition_selective,
			'temp_extremity': self.temp_extremity,
			'move_nature': self.move_nature,
			'move_speed': self.move_speed,
			'move_cost_circ': self.move_cost_circ,
			'move_other': self.move_other,
			'conceal_type': self.conceal_type,
			'darkness_descriptor': self.darkness_descriptor,
			'light_check': self.light_check,
			'visibility_trait_type': self.visibility_trait_type,
			'visibility_trait': self.visibility_trait,
			'visibility_mod': self.visibility_mod,
			'cost': self.cost,
			'ranks': self.ranks,
			'elements': self.elements,
			'element': self.element,
			'element_strength': self.element_strength,
			'element_mass': self.element_mass,
			'multiple': self.multiple
		}

class PowerMinion(db.Model):
	__tablename__ = 'power_minions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	points = db.Column(db.Integer)
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	link = db.Column(db.Boolean)
	variable_type = db.Column(db.String())
	multiple = db.Column(db.Boolean)
	attitude = db.Column(db.Boolean)
	resitable = db.Column(db.Boolean)
	heroic = db.Column(db.Boolean)
	sacrifice = db.Column(db.Boolean)
	sacrifice_cost = db.Column(db.Integer)
	attitude_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	attitude_attitude = db.Column(db.Integer, db.ForeignKey('levels.id'))
	attitude_trait_type = db.Column(db.String())
	attitude_trait = db.Column(db.Integer)
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))
	resitable_dc = db.Column(db.Integer)
	multiple_value = db.Column(db.Integer)
	multiple_type = db.Column(db.String())
	horde = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'points': self.points,
			'condition': self.condition,
			'player_condition': self.player_condition,
			'link': self.link,
			'variable_type': self.variable_type,
			'multiple': self.multiple,
			'attitude': self.attitude,
			'resitable': self.resitable,
			'heroic': self.heroic,
			'sacrifice': self.sacrifice,
			'sacrifice_cost': self.sacrifice_cost,
			'attitude_type': self.attitude_type,
			'attitude_attitude': self.attitude_attitude,
			'attitude_trait_type': self.attitude_trait_type,
			'attitude_trait': self.attitude_trait,
			'resitable_check': self.resitable_check,
			'resitable_dc': self.resitable_dc,
			'multiple_value': self.multiple_value,
			'multiple_type': self.multiple_type,
			'horde': self.horde
		}

class PowerMod(db.Model):
	__tablename__ = 'power_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	affects_objects = db.Column(db.Boolean)
	area = db.Column(db.Boolean)
	persistent = db.Column(db.Boolean)
	incurable = db.Column(db.Boolean)
	selective = db.Column(db.Boolean)
	limited = db.Column(db.Boolean)
	innate = db.Column(db.Boolean)
	others = db.Column(db.Boolean)
	sustained = db.Column(db.Boolean)
	reflect = db.Column(db.Boolean)
	redirect = db.Column(db.Boolean)
	half = db.Column(db.Boolean)
	affects_corp = db.Column(db.Boolean)
	continuous = db.Column(db.Boolean)
	vulnerable = db.Column(db.Boolean)
	precise = db.Column(db.Boolean)
	progressive = db.Column(db.Boolean)
	subtle = db.Column(db.Boolean)
	permanent = db.Column(db.Boolean)
	points = db.Column(db.Boolean)
	ranks_check = db.Column(db.Boolean)
	action = db.Column(db.Boolean)
	side_effect = db.Column(db.Boolean)
	concentration = db.Column(db.Boolean)
	simultaneous = db.Column(db.Boolean)
	effortless = db.Column(db.Boolean)
	noticeable = db.Column(db.Boolean)
	unreliable = db.Column(db.Boolean)
	radius = db.Column(db.Boolean)
	accurate = db.Column(db.Boolean)
	acute = db.Column(db.Boolean)
	extra = db.Column(db.Boolean)
	objects_alone = db.Column(db.Integer, db.ForeignKey('defense.id'))
	objects_character = db.Column(db.Integer, db.ForeignKey('defense.id'))
	effortless_type = db.Column(db.String())
	effortless_degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	effortless_degree_type = db.Column(db.String())
	effortless_retries = db.Column(db.Boolean)
	simultaneous_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	area_type = db.Column(db.String())
	area_damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	area_ranged = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	area_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	area_attach = db.Column(db.Boolean)
	limited_type = db.Column(db.String())
	limited_mod = db.Column(db.Integer)
	limited_level_degree = db.Column(db.String())
	limited_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	limited_source_type = db.Column(db.String())
	limited_source = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_task_type = db.Column(db.String())
	limited_task = db.Column(db.String())
	limited_trait_type = db.Column(db.String())
	limited_trait = db.Column(db.Integer)
	limited_description = db.Column(db.String())
	limited_subjects = db.Column(db.Integer)
	limited_extra = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_language_type = db.Column(db.String())
	limited_degree_type = db.Column(db.String())
	limited_degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	limited_degree_effect = db.Column(db.String())
	limited_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	limited_subsense = db.Column(db.String())
	limited_sense_depend = db.Column(db.Boolean)
	limited_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_range_type = db.Column(db.String())
	limited_range = db.Column(db.Integer, db.ForeignKey('power_ranged.id'))
	limited_ground = db.Column(db.Integer, db.ForeignKey('ground.id'))
	limited_creature =  db.Column(db.Integer, db.ForeignKey('creature.id'))
	limited_creature_narrow =  db.Column(db.Integer, db.ForeignKey('creature_narrow.id'))
	limited_creature_other =  db.Column(db.String())
	limited_env_other = db.Column(db.String())
	limited_env =  db.Column(db.Integer, db.ForeignKey('environments.id'))
	limited_emotion_other = db.Column(db.String())
	limited_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	limited_org_other = db.Column(db.String())
	limited_org = db.Column(db.Integer, db.ForeignKey('organizations.id'))
	limited_material = db.Column(db.Integer, db.ForeignKey('materials.id'))
	side_effect_type = db.Column(db.String())
	side_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	side_other = db.Column(db.String())
	reflect_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	reflect_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	subtle_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	subtle_null_trait_type = db.Column(db.String())
	subtle_null_trait = db.Column(db.Integer)
	others_type = db.Column(db.String())
	others_req = db.Column(db.String())
	others_check = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	others_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	others_carry = db.Column(db.Boolean)
	others_touch = db.Column(db.Boolean)
	others_touch_continuous = db.Column(db.Boolean)
	ranks_trait_type = db.Column(db.String())
	ranks_trait = db.Column(db.Integer)
	ranks_ranks = db.Column(db.Integer)
	ranks_mod = db.Column(db.Integer)
	points_type = db.Column(db.String())
	points_reroll_target = db.Column(db.String())
	points_reroll_cost = db.Column(db.Integer)
	points_rerolls = db.Column(db.Integer)
	points_reroll_result = db.Column(db.String())
	points_give = db.Column(db.Integer)
	points_negate = db.Column(db.Integer)
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	extra_count = db.Column(db.Integer)
	extra_degree = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	extra_dc = db.Column(db.Integer, db.ForeignKey('power_dc_type.id'))
	extra_circ = db.Column(db.Integer, db.ForeignKey('power_circ_type.id'))
	multiple = db.Column(db.String())
	feedback = db.Column(db.Boolean)
	feedback_effect = db.Column(db.String())
	feedback_type = db.Column(db.String())
	feedback_cover = db.Column(db.Integer, db.ForeignKey('cover.id'))
	feedback_mod = db.Column(db.Integer)
	feedback_defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
	passive = db.Column(db.Boolean)
	adv = db.Column(db.Boolean)
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	advantage_rank = db.Column(db.Integer)
	advantage_rank_per = db.Column(db.Boolean)
	advantage_effect = db.Column(db.Boolean)
	advantage_bonus = db.Column(db.Boolean)
	advantage_damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	advantage_damage_bonus = db.Column(db.Integer)
	advantage_damage_bonus_rank = db.Column(db.Boolean)
	precise_type = db.Column(db.Boolean)
	sustained_action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	sustained_no_move = db.Column(db.Boolean)
	concentration_type = db.Column(db.String())
	concentration_check = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	concentration_check_type = db.Column(db.Integer, db.ForeignKey('power_check_type.id'))
	concentration_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	concentration_effort = db.Column(db.Boolean)
	unreliable_type = db.Column(db.String())
	incurable_type = db.Column(db.String())
	progressive_type = db.Column(db.String())
	progressive_degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	progressive_degree_all = db.Column(db.Boolean)
	progressive_degree_type = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	cumulative = db.Column(db.Boolean)
	cumulative_degree = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))
	persistent_type = db.Column(db.String())
	persistent_degree = db.Column(db.Integer, db.ForeignKey('power_degree_type.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'affects_objects': self.affects_objects,
			'area': self.area,
			'persistent': self.persistent,
			'incurable': self.incurable,
			'selective': self.selective,
			'limited': self.limited,
			'innate': self.innate,
			'others': self.others,
			'sustained': self.sustained,
			'reflect': self.reflect,
			'redirect': self.redirect,
			'half': self.half,
			'affects_corp': self.affects_corp,
			'continuous': self.continuous,
			'vulnerable': self.vulnerable,
			'radius': self.radius,
			'accurate': self.accurate,
			'acute': self.acute,
			'precise': self.precise,
			'progressive': self.progressive,
			'subtle': self.subtle,
			'extra': self.extra,
			'permanent': self.permanent,
			'points': self.points,
			'ranks': self.ranks,
			'action': self.action,
			'side_effect': self.side_effect,
			'concentration': self.concentration,
			'simultaneous': self.simultaneous,
			'effortless': self.effortless,
			'noticeable': self.noticeable,
			'unreliable': self.unreliable,
			'objects_alone': self.objects_alone,
			'objects_character': self.objects_character,
			'effortless_type': self.effortless_type,
			'effortless_degree_type': self.effortless_degree_type,
			'effortless_degree': self.effortless_degree,
			'effortless_retries': self.effortless_retries,
			'simultaneous_descriptor': self.simultaneous_descriptor,
			'area_type': self.area_type,
			'area_damage': self.area_damage,
			'area_ranged': self.area_ranged,
			'area_descriptor': self.area_descriptor,
			'area_attach': self.area_attach,
			'limited_type': self.limited_type,
			'limited_mod': self.limited_mod,
			'limited_level_degree': self.limited_level_degree,
			'limited_level': self.limited_level,
			'limited_source_type': self.limited_source_type,
			'limited_source': self.limited_source,
			'limited_task_type': self.limited_task_type,
			'limited_task': self.limited_task,
			'limited_trait_type': self.limited_trait_type,
			'limited_trait': self.limited_trait,
			'limited_description': self.limited_description,
			'limited_subjects': self.limited_subjects,
			'limited_extra': self.limited_extra,
			'limited_language_type': self.limited_language_type,
			'limited_degree_type': self.limited_degree_type,
			'limited_degree': self.limited_degree,
			'limited_degree_effect': self.limited_degree_effect,
			'limited_sense': self.limited_sense,
			'limited_subsense': self.limited_subsense,
			'limited_sense_depend': self.limited_sense_depend,
			'limited_descriptor': self.limited_descriptor,
			'limited_range_type': self.limited_range_type,
			'limited_range': self.limited_range,
			'limited_ground': self.limited_ground,
			'limited_creature': self.limited_creature,
			'limited_creature_narroq': self.limited_creature_narrow,
			'limited_creature_other': self.limited_creature_other,
			'limited_env_other': self.limited_env_other,
			'limited_env': self.limited_env,
			'limited_org': self.limited_org,
			'limited_org_other': self.limited_org_other,
			'limited_emotion_other': self.limited_emotion_other,
			'limited_emotion': self.limited_emotion,
			'limited_material': self.limited_material,
			'side_effect_type': self.side_effect_type,
			'side_level': self.side_level,
			'side_other': self.side_other,
			'reflect_check': self.reflect_check,
			'reflect_descriptor': self.reflect_descriptor,
			'subtle_opposed': self.subtle_opposed,
			'subtle_null_trait_type': self.subtle_null_trait_type,
			'subtle_null_trait': self.subtle_null_trait,
			'others_type': self.others_type,
			'others_req': self.others_req,
			'others_check': self.others_check,
			'others_opposed': self.others_opposed,
			'others_carry': self.others_carry,
			'others_touch': self.others_touch,
			'others_touch_continuous': self.others_touch_continuous,
			'ranks_trait_type': self.ranks_trait_type,
			'ranks_trait': self.ranks_trait,
			'ranks_ranks': self.ranks_ranks,
			'ranks_mod': self.ranks_mod,
			'points_type': self.points_type,
			'points_reroll_target': self.points_reroll_target, 
			'points_reroll_cost': self.points_reroll_cost,
			'points_rerolls': self.points_rerolls,
			'points_reroll_result': self.points_reroll_result,
			'points_give': self.points_give,
			'points_negate': self.points_negate,
			'ranks_cost': self.ranks_cost,
			'cost': self.cost,
			'extra_count': self.extra_count,
			'extra_degree': self.extra_degree,
			'extra_dc': self.extra_dc,
			'extra_circ': self.extra_circ,
			'multiple': self.multiple,
			'feedback': self.feedback,
			'feedback_effect': self.feedback_effect,
			'feedback_type': self.feedback_type,
			'feedback_cover': self.feedback_cover,
			'feedback_mod': self.feedback_mod,
			'feedback_defense': self.feedback_defense,
			'passive': self.passive,
			'adv': self.adv,
			'advantage:': self.advantage,
			'advantage_rank': self.advantage_rank,
			'advantage_rank_per': self.advantage_rank_per,
			'advantage_effect': self.advantage_effect,
			'advantage_bonus': self.advantage_bonus,
			'advantage_damage': self.advantage_damage,
			'advantage_damage_bonus': self.advantage_damage_bonus,
			'advantage_damage_bonus_rank': self.advantage_damage_bonus_rank,
			'precise_type': self.precise_type,
			'sustained_action': self.sustained_action,
			'sustained_no_move': self.sustained_no_move,
			'concentration_type': self.concentration_type,
			'concentration_check': self.concentration_check,
			'concentration_check_type': self.concentration_check_type,
			'concentration_opposed': self.concentration_opposed,
			'concentration_effort': self.concentration_effort,
			'unreliable_type': self.unreliable_type,
			'incurable_type': self.incurable_type,
			'progressive_type': self.progressive_type,
			'progressive_degree': self.progressive_degree,
			'progressive_degree_all': self.progressive_degree_all,
			'progressive_degree_type': self.progressive_degree_type,
			'cumulative_degree': self.cumulative_degree,
			'persistent_type': self.persistent_type,
			'persistent_degree': self.persistent_degree
		}

class PowerRanged(db.Model):
	__tablename__ = 'power_ranged'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	range_type = db.Column(db.String())
	flat_value = db.Column(db.Integer)
	flat_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank = db.Column(db.Integer)
	flat_rank_value = db.Column(db.Integer)
	flat_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank_rank = db.Column(db.Integer)
	flat_rank_distance = db.Column(db.Integer)
	flat_rank_distance_rank = db.Column(db.Integer)
	units_rank_start_value = db.Column(db.Integer)
	units_rank_value = db.Column(db.Integer)
	units_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	units_rank_rank = db.Column(db.Integer)
	rank_distance_start = db.Column(db.Integer)
	rank_distance = db.Column(db.Integer)
	rank_effect_rank = db.Column(db.Integer)
	effect_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	effect_mod = db.Column(db.Integer)
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	check_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_mod = db.Column(db.Integer)
	trait_trait_type = db.Column(db.String())
	trait_trait = db.Column(db.Integer)
	trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_mod = db.Column(db.Integer)
	distance_mod_rank = db.Column(db.Integer)
	distance_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_mod_trait_type = db.Column(db.String())
	distance_mod_trait = db.Column(db.Integer)
	dc = db.Column(db.Integer, db.ForeignKey('power_dc.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	damage = db.Column(db.Integer, db.ForeignKey('power_damage.id'))
	keyword = db.Column(db.String())
	title = db.Column(db.String())
	movement = db.Column(db.Boolean)
	rank = db.Column(db.Boolean)
	effect = db.Column(db.Boolean)
	general = db.Column(db.Integer, db.ForeignKey('range.id'))
	perception = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	penalty_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	penalty_mod = db.Column(db.Integer)
	penalty_trait_type = db.Column(db.String())
	penalty_trait = db.Column(db.Integer)
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'range_type': self.range_type,
			'flat_value': self.flat_value,
			'flat_units': self.flat_units,
			'flat_rank': self.flat_rank,
			'flat_rank_value': self.flat_rank_value,
			'flat_rank_units': self.flat_rank_units,
			'flat_rank_rank': self.flat_rank_rank,
			'flat_rank_distance': self.flat_rank_distance,
			'flat_rank_distance_rank': self.flat_rank_distance_rank,
			'units_rank_start_value': self.units_rank_start_value,
			'units_rank_value': self.units_rank_value,
			'units_rank_units': self.units_rank_units,
			'units_rank_rank': self.units_rank_rank,
			'rank_distance_start': self.rank_distance_start,
			'rank_distance': self.rank_distance,
			'rank_effect_rank': self.rank_effect_rank,
			'effect_mod_math': self.effect_mod_math,
			'effect_mod': self.effect_mod,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_math': self.check_math,
			'check_mod': self.check_mod,
			'trait_trait_type': self.trait_trait_type,
			'trait_trait': self.trait_trait,
			'trait_math': self.trait_math,
			'trait_mod': self.trait_mod,
			'distance_mod_rank': self.distance_mod_rank,
			'distance_mod_math': self.distance_mod_math,
			'distance_mod_trait_type': self.distance_mod_trait_type,
			'distance_mod_trait': self.distance_mod_trait,
			'dc': self.dc,
			'circ': self.circ,
			'degree': self.degree,
			'damage': self.damage,
			'keyword': self.keyword,
			'movement': self.movement,
			'title': self.title,
			'rank': self.rank,
			'effect': self.effect,
			'general': self.general,
			'perception': self.perception,
			'hide': self.hide,
			'penalty_math': self.penalty_math,
			'penalty_mod': self.penalty_mod,
			'penalty_trait_type': self.penalty_trait_type,
			'penalty_trait': self.penalty_trait,
			'cost': self.cost,
			'ranks': self.ranks
		}

class PowerResist(db.Model):
	__tablename__ = 'power_resistance_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	resist_check_type = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	requires_check = db.Column(db.Boolean)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'mod': self.mod,
			'rounds': self.rounds,
			'circumstance': self.circumstance,
			'resist_check_type': self.resist_check_type,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'descriptor': self.descriptor,
			'requires_check': self.requires_check,
			'check_type': self.check_type,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait
		}

class PowerResistBy(db.Model):
	__tablename__ = 'power_resisted_by'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	description = db.Column(db.String())
	effect = db.Column(db.String())
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	degree = db.Column(db.Integer)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	weaken_max = db.Column(db.Integer)
	weaken_restored = db.Column(db.Integer)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	damage =  db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	nullify_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	nullify_alternate = db.Column(db.Integer, db.ForeignKey('defense.id'))
	extra_effort = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'dc': self.dc,
			'mod': self.mod,
			'description': self.description,
			'trait': self.trait,
			'effect': self.effect,
			'level': self.level,
			'degree': self.degree,
			'descriptor': self.descriptor,
			'weaken_max': self.weaken_max,
			'weaken_restored': self.weaken_restored,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'damage': self.damage,
			'strength': self.strength,
			'nullify_descriptor': self.nullify_descriptor,
			'nullify_alternate': self.nullify_alternate,
			'extra_effort': self.extra_effort
		}


class PowerSenseEffect(db.Model):
	__tablename__ = 'power_sense_effect'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	visual = db.Column(db.Boolean)
	mental = db.Column(db.Boolean)
	tactile = db.Column(db.Boolean)
	sense_cost = db.Column(db.Integer)
	subsense_cost = db.Column(db.Integer)
	skill = db.Column(db.Integer, db.ForeignKey('power_check.id'))
	skill_required = db.Column(db.Boolean)
	sense_type = db.Column(db.String())
	height_trait_type = db.Column(db.String())
	height_trait = db.Column(db.Integer)
	height_power_required = db.Column(db.Boolean)
	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.Integer)
	resist_immune = db.Column(db.Boolean)
	resist_permanent = db.Column(db.String())
	resist_circ = db.Column(db.Integer)
	objects = db.Column(db.Boolean)
	exclusive = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	dark = db.Column(db.Boolean)
	lighting = db.Column(db.Integer, db.ForeignKey('light.id'))
	time = db.Column(db.Boolean)
	dimensional = db.Column(db.Boolean)
	radius = db.Column(db.Boolean)
	accurate = db.Column(db.Boolean)
	acute = db.Column(db.Boolean)
	distance = db.Column(db.String())
	distance_dc = db.Column(db.Integer)
	distance_mod = db.Column(db.Integer)
	distance_value = db.Column(db.Integer)
	distance_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	distance_factor = db.Column(db.Integer)
	dimensional_type = db.Column(db.String())
	dimensional_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	ranks = db.Column(db.Integer, db.ForeignKey('power_ranks.id'))
	cost = db.Column(db.Integer, db.ForeignKey('power_cost.id'))
	time_value = db.Column(db.Integer, db.ForeignKey('power_time.id'))
	time_type = db.Column(db.Integer, db.ForeignKey('power_time_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('power_circ.id'))
	comprehend = db.Column(db.Boolean)
	comprehend_type = db.Column(db.String())
	comprehend_animal = db.Column(db.String())
	comprehend_language = db.Column(db.String())
	comprehend_spirit = db.Column(db.String())
	concealment = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	conceal_precise = db.Column(db.Boolean)
	conceal_power = db.Column(db.Boolean)
	conceal_power_sense = db.Column(db.Integer, db.ForeignKey('powers.id'))
	multiple = db.Column(db.String())
	analytical = db.Column(db.Boolean)
	acute_req = db.Column(db.Boolean)
	awareness = db.Column(db.Boolean)
	awareness_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	awareness_subtle = db.Column(db.Boolean)
	awareness_subtle_ranks = db.Column(db.Integer)
	counter_conceal = db.Column(db.String())
	counter_conceal_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	counter_conceal_heat = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	range = db.Column(db.Integer, db.ForeignKey('power_ranged.id'))
	ranged_type = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	light_penalty = db.Column(db.Integer, db.ForeignKey('light.id'))
	light_penalty_trait_type = db.Column(db.String())
	light_penalty_trait = db.Column(db.Integer)
	ranged_sense = db.Column(db.Boolean)
	illusion_range = db.Column(db.Integer)
	illusion_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	illusion_opposed = db.Column(db.Integer, db.ForeignKey('power_opposed_type.id'))
	illusion_selective = db.Column(db.Boolean)
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_degree = db.Column(db.Integer, db.ForeignKey('power_degree.id'))
	remote_ranged = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	remote_simultaneous = db.Column(db.Boolean)
	sense_aware_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	micro = db.Column(db.String())
	micro_expertise = db.Column(db.String())
	cognition_inactive = db.Column(db.Boolean)
	cognition_self = db.Column(db.Boolean)
	track_speed = db.Column(db.Integer, db.ForeignKey('power_movement.id'))
	track_speed_type = db.Column(db.Integer, db.ForeignKey('power_move_type.id'))
	counter_conceal_uv = db.Column(db.Boolean)
	communication = db.Column(db.Integer, db.ForeignKey('communication.id'))
	communication_range = db.Column(db.Integer, db.ForeignKey('power_ranged_type.id'))
	

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'sense': self.sense,
			'subsense': self.subsense,
			'visual': self.visual,
			'mental': self.mental,
			'sense_cost': self.sense_cost,
			'subsense_cost': self.subsense_cost,
			'skill': self.skill,
			'skill_required': self.skill_required,
			'sense_type': self.sense_type,
			'height_trait_type': self.height_trait_type,
			'height_trait': self.height_trait,
			'height_power_required': self.height_power_required,
			'height_ensense': self.height_ensense,
			'resist_trait_type': self.resist_trait_type,
			'resist_trait': self.resist_trait,
			'resist_immune': self.resist_immune,
			'resist_permanent': self.resist_permanent,
			'resist_circ': self.resist_circ,
			'objects': self.objects,
			'exclusive': self.exclusive,
			'gm': self.gm,
			'dark': self.dark,
			'lighting': self.lighting,
			'time': self.time,
			'dimensional': self.dimensional,
			'radius': self.radius,
			'accurate': self.accurate,
			'acute': self.acute,
			'time_value': self.time_value,
			'time_type': self.time_type,
			'distance': self.distance,
			'distance_dc': self.distance_dc,
			'distance_mod': self.distance_mod,
			'distance_value': self.distance_value,
			'distance_unit': self.distance_unit,
			'distance_factor': self.distance_factor,
			'dimensional_type': self.dimensional_type,
			'dimensional_descriptor': self.dimensional_descriptor,
			'ranks': self.ranks,
			'cost': self.cost,
			'circ': self.circ,
			'comprehend': self.comprehend,
			'comprehend_type': self.comprehend_type,
			'comprehend_animal': self.comprehend_animal,
			'comprehend_language': self.comprehend_language,
			'comprehend_spirit': self.comprehend_spirit,
			'concealment': self.concealment,
			'conceal_precise': self.conceal_precise,
			'conceal_power': self.conceal_power,
			'conceal_power_sense': self.conceal_power_sense,
			'multiple': self.multiple,
			'analytical': self.analytical,
			'acute_req': self.acute_req,
			'awareness': self.awareness,
			'awareness_descriptor': self.awareness_descriptor,
			'awareness_subtle': self.awareness_subtle,
			'awareness_subtle_ranks': self.awareness_subtle_ranks,
			'counter_conceal_descriptor': self.counter_conceal_descriptor,
			'counter_conceal': self.counter_conceal,
			'counter_conceal_heat': self.counter_conceal_heat,
			'ranged': self.ranged,
			'range': self.range,
			'ranged_type': self.ranged_type,
			'light_penalty': self.light_penalty,
			'light_penalty_trait_type': self.light_penalty_trait_type,
			'light_penalty_trait': self.light_penalty_trait,
			'ranged_sense': self.ranged_sense,
			'condition': self.condition,
			'condition_degree': self.condition_degree,
			'illusion_range': self.illusion_range,
			'illusion_unit': self.illusion_unit,
			'illusion_selective': self.illusion_selective,
			'remote_ranged': self.remote_ranged,
			'remote_simultaneous': self.remote_simultaneous,
			'micro': self.micro,
			'micro_expertise': self.micro_expertise,
			'cognition_inactive': self.cognition_inactive,
			'cognition_self': self.cognition_self,
			'track_speed': self.track_speed,
			'track_speed_type': self.track_speed_type,
			'counter_conceal_uv': self.counter_conceal_uv,
			'communication': self.communication,
			'communication_range': self.communication_range
		}

class PowerReverse(db.Model):
	__tablename__ = 'power_reverse'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	degree = db.Column(db.Integer)
	when = db.Column(db.String())
	check_check = db.Column(db.Boolean)
	time_check = db.Column(db.Boolean)
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	value_type = db.Column(db.String())
	value_dc = db.Column(db.Integer)
	math_dc = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	time_value = db.Column(db.Integer)
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'degree': self.degree,
			'when': self.when,
			'check_check': self.check_check,
			'time_check': self.time_check,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'value_type': self.value_type,
			'value_dc': self.value_dc,
			'math_dc': self.math_dc,
			'math': self.math,
			'time_value': self.time_value,
			'time_unit': self.time_unit
		}



class PowerDes(db.Model):
	__tablename__ = 'power_descriptors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())	
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	des_id = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	origin = db.Column(db.Integer, db.ForeignKey('origin.id'))
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	medium = db.Column(db.Integer, db.ForeignKey('medium.id'))
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	result = db.Column(db.String())
	descriptor = db.Column(db.Boolean)
	damage = db.Column(db.Boolean)
	hidden = db.Column(db.Boolean)
	rare = db.Column(db.Boolean)
	uncommon = db.Column(db.Boolean)
	common = db.Column(db.Boolean)
	very = db.Column(db.Boolean)
	any_damage = db.Column(db.Boolean)
	any_origin = db.Column(db.Boolean)
	any_source = db.Column(db.Boolean)
	any_medium_type = db.Column(db.Boolean)
	any_medium_subtype = db.Column(db.Boolean)
	any_medium = db.Column(db.Boolean)
	any_material = db.Column(db.Boolean)
	any_energy = db.Column(db.Boolean)
	any_descriptor = db.Column(db.Boolean)
	hidden_name = db.Column(db.String())
	power = db.Column(db.Boolean)
	all = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'power_id': self.power_id,
			'des_id': self.des_id,
			'origin': self.origin,
			'source': self.source,
			'medium': self.medium,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'result': self.result,
			'descriptor': self.descriptor,
			'damage': self.damage,
			'hidden': self.hidden,
			'rare': self.rare,
			'uncommon': self.uncommon,
			'common': self.common,
			'very': self.very,
			'any_damage': self.any_damage,
			'any_origin': self.any_origin,
			'any_source': self.any_source,
			'any_medium_type': self.any_medium_type,
			'any_medium_subtype': self.any_medium_subtype,
			'any_medium': self.any_medium,
			'any_material': self.any_material,
			'any_energy': self.any_energy,
			'any_descriptor': self.any_descriptor,
			'hidden_name': self.hidden_name,
			'power': self.power,
			'all': self.all
		}