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


class SkillBonus(db.Model):
	__tablename__ = 'skill_bonus'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	type = db.Column(db.Integer, db.ForeignKey('skill_type.id'))
	skill_check = db.Column(db.String())
	dc_type = db.Column(db.String())
	dc_value = db.Column(db.Integer)
	dc_mod = db.Column(db.Integer)
	target = db.Column(db.String())
	targets = db.Column(db.Integer)
	speed_type = db.Column(db.String())
	speed_turns = db.Column(db.Integer)
	speed_direction = db.Column(db.String())
	speed_mod = db.Column(db.Integer)
	speed_value = db.Column(db.Integer)
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	attack = db.Column(db.Integer)
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	concealment_type = db.Column(db.String())
	concealment = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	for_weapon = db.Column(db.Boolean)
	weapon_cat = db.Column(db.Integer, db.ForeignKey('weapon_category.id'))
	weapon_type = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	untrained = db.Column(db.Boolean)
	tools = db.Column(db.Boolean)
	required_tools = db.Column(db.String())
	subskill = db.Column(db.Boolean)
	check_dc = db.Column(db.Boolean)
	gm_circ_value = db.Column(db.Integer)
	gm_circ_type = db.Column(db.String())
	gm_circ = db.Column(db.Boolean)
	secret = db.Column(db.Boolean)
	secret_frequency = db.Column(db.String())
	secret_trait_type = db.Column(db.String())
	secret_trait = db.Column(db.Integer)
	ability_check = db.Column(db.Boolean)
	check_check = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	degree = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	modifiers = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	time = db.Column(db.Boolean)
	move = db.Column(db.Boolean)
	opposed_multiple = db.Column(db.String())
	modifiers_multiple = db.Column(db.String())
	modifiers_multiple_count = db.Column(db.Integer)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)
	time_multiple = db.Column(db.String())
	partner = db.Column(db.Boolean)
	partner_type = db.Column(db.String())
	partner_trait_type = db.Column(db.String())
	partner_trait = db.Column(db.Integer)
	partner_tools = db.Column(db.String())
	partner_materials = db.Column(db.String())
	partner_equip_type = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	partner_equip = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	partner_feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	opponent_turn = db.Column(db.Boolean)
	opponent_turn_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_turn_when = db.Column(db.String())
	
	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'ability': self.ability,
			'skill': self.skill,
			'check_type': self.check_type,
			'action': self.action,
			'type': self.type,
			'skill_check': self.skill_check,
			'dc_type': self.dc_type,
			'dc_value': self.dc_value,
			'dc_mod': self.dc_mod,
			'target': self.target,
			'targets': self.targets,
			'speed_type': self.speed_type,
			'speed_turns': self.speed_turns,
			'speed_direction': self.speed_direction,
			'speed_mod': self.speed_mod,
			'speed_value': self.speed_value,
			'condition': self.condition,
			'attack': self.attack,
			'advantage': self.advantage,
			'concealment_type': self.concealment_type,
			'concealment': self.concealment,
			'for_weapon': self.for_weapon,
			'weapon_cat': self.weapon_cat,
			'weapon_type': self.weapon_type,
			'weapon': self.weapon,
			'untrained': self.untrained,
			'tools': self.tools,
			'required_tools': self.required_tools,
			'subskill': self.subskill,
			'check_dc': self.check_dc,
			'secret': self.secret,
			'secret_frequency': self.secret_frequency,
			'secret_trait_type': self.secret_trait_type,
			'secret_trait': self.secret_trait,
			'gm_circ_value': self.gm_circ_value,
			'gm_circ_type': self.gm_circ_type,
			'gm_circ': self.gm_circ,
			'ability_check': self.ability_check,
			'check_check': self.check_check,
			'circumstance': self.circumstance,
			'dc': self.dc,
			'degree': self.degree,
			'levels': self.levels,
			'modifiers': self.modifiers,
			'move': self.move,
			'opposed': self.opposed,
			'time': self.time,
			'opposed_multiple': self.opposed_multiple,
			'modifiers_multiple': self.modifiers_multiple,
			'modifiers_multiple_count': self.modifiers_multiple_count,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base,
			'time_multiple': self.time_multiple,
			'partner': self.partner,
			'partner_type': self.partner_type,
			'partner_trait_type': self.partner_trait_type,
			'partner_trait': self.partner_trait,
			'partner_tools': self.partner_tools,
			'partner_materials': self.partner_materials,
			'partner_equip_type': self.partner_equip_type,
			'partner_equip': self.partner_equip,
			'partner_feature': self.partner_feature,
			'opponent_turn': self.opponent_turn,
			'opponent_turn_check': self.opponent_turn_check,
			'opponent_turn_when': self.opponent_turn_when
		}




class SkillAbility(db.Model):
	__tablename__ = 'skill_ability'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	circumstance = db.Column(db.String())
	variable = db.Column(db.Integer, db.ForeignKey('skill_check.id'))


	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'ability': self.ability,
			'circumstance': self.circumstance,
			'variable': self.variable
		}

class SkillCheck(db.Model):
	__tablename__ = 'skill_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	degree = db.Column(db.Integer, db.ForeignKey('skill_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('skill_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('skill_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('skill_time_type.id'))
	dc_value = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	move = db.Column(db.Integer, db.ForeignKey('skill_move_type.id'))
	attack = db.Column(db.Integer)
	opposed = db.Column(db.Integer, db.ForeignKey('skill_opposed.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'keyword': self.keyword,
			'attack': self.attack,
			'opposed': self.opposed
		}

class SkillCirc(db.Model):
	__tablename__ = 'skill_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	lasts = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	time = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	title = db.Column(db.Integer, db.ForeignKey('skill_circ_type.id'))
	surface = db.Column(db.Boolean)
	tools = db.Column(db.String())
	materials = db.Column(db.String())
	
	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'materials': self.materials
		}

class SkillDC(db.Model):
	__tablename__ = 'skill_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	variable = db.Column(db.Integer, db.ForeignKey('skill_check.id'))
	title = db.Column(db.Integer, db.ForeignKey('skill_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	effect_target = db.Column(db.String())
	
	
	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'effect_target': self.effect_target
		}

class SkillDegree(db.Model):
	__tablename__ = 'skill_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	level_direction = db.Column(db.Integer)
	level_time = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	circumstance = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
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
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_turns = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	nullify_type = db.Column(db.String())
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Integer, db.ForeignKey('skill_degree.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opposed = db.Column(db.Integer, db.ForeignKey('skill_opposed.id'))
	variable = db.Column(db.Integer, db.ForeignKey('skill_check.id'))
	resist_dc = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.Integer)
	skill_dc = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	skill_trait_type = db.Column(db.String())
	skill_trait = db.Column(db.Integer)
	routine_trait_type = db.Column(db.String())
	routine_trait = db.Column(db.Integer)
	routine_mod = db.Column(db.Integer)
	attack = db.Column(db.Integer)
	attack_turns = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	compare = db.Column(db.Integer, db.ForeignKey('skill_opposed.id'))
	time_table = db.Column(db.Boolean)
	move_table = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('skill_degree_type.id'))
	description = db.Column(db.String())
	effect_target = db.Column(db.String())
	value_type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'condition1': self.condition1,
			'condition2': self.condition2,
			'condition_turns': self.condition_turns,
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
			'value_type': self.value_type
		}

class SkillMod(db.Model):
	__tablename__ = 'skill_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	bonus = db.Column(db.Integer)
	bonus_type = db.Column(db.String())
	penalty = db.Column(db.Integer)
	penalty_type = db.Column(db.String())
	trigger = db.Column(db.String())
	bonus_effect = db.Column(db.String())
	penalty_effect = db.Column(db.String())
	environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	environment_other = db.Column(db.String())
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	mod_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	cover = db.Column(db.Integer, db.ForeignKey('cover.id'))
	conceal = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	maneuver = db.Column(db.Integer, db.ForeignKey('maneuvers.id'))
	weapon_melee = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon_ranged = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	tools = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	creature = db.Column(db.Integer, db.ForeignKey('creature.id'))
	creature_other = db.Column(db.String())
	emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	emotion_other = db.Column(db.String())
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	profession = db.Column(db.Integer, db.ForeignKey('jobs.id'))
	profession_other = db.Column(db.String())
	bonus_trait_type = db.Column(db.String())
	bonus_trait = db.Column(db.Integer)
	bonus_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	bonus_check_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	bonus_conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	penalty_trait_type = db.Column(db.String())
	penalty_trait = db.Column(db.Integer)
	penalty_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	penalty_check_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	penalty_conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	bonus_active_defense = db.Column(db.Boolean)
	bonus_conflict_defend = db.Column(db.Boolean)
	penalty_active_defense = db.Column(db.Boolean)
	penalty_conflict_defend = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	multiple_count = db.Column(db.Integer)
	lasts = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	light = db.Column(db.Integer, db.ForeignKey('light.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'bonus': self.bonus,
			'bonus_type': self.bonus_type,
			'penalty': self.penalty,
			'penalty_type': self.penalty_type,
			'trigger': self.trigger,
			'bonus_effect': self.bonus_effect,
			'penalty_effect': self.penalty_effect,
			'environment': self.environment,
			'environment_other': self.environment_other,
			'sense': self.sense,
			'mod_range': self.mod_range,
			'subsense': self.subsense,
			'cover': self.cover,
			'conceal': self.conceal,
			'maneuver': self.maneuver,
			'weapon_melee': self.weapon_melee,
			'weapon_ranged': self.weapon_ranged,
			'tools': self.tools,
			'condition': self.condition,
			'power': self.power,
			'consequence': self.consequence,
			'creature': self.creature,
			'creature_other': self.creature_other,
			'emotion': self.emotion,
			'emotion_other': self.emotion_other,
			'conflict': self.conflict,
			'profession': self.profession,
			'profession_other': self.profession_other,
			'bonus_trait_type': self.bonus_trait_type,
			'bonus_trait': self.bonus_trait,
			'bonus_check': self.bonus_check,
			'bonus_check_range': self.bonus_check_range,
			'bonus_conflict': self.bonus_conflict,
			'penalty_trait_type': self.penalty_trait_type,
			'penalty_trait': self.penalty_trait,
			'penalty_check': self.penalty_check,
			'penalty_check_range': self.penalty_check_range,
			'penalty_conflict': self.penalty_conflict,
			'bonus_active_defense': self.bonus_active_defense,
			'bonus_conflict_defend': self.bonus_conflict_defend,
			'penalty_active_defense': self.penalty_active_defense,
			'penalty_conflict_defend': self.penalty_conflict_defend,
			'multiple': self.multiple,
			'multiple_count': self.multiple_count,
			'lasts': self.lasts,
			'skill': self.skill,
			'light': self.light
		}

class SkillMove(db.Model):
	__tablename__ = 'skill_move'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	speed = db.Column(db.String())
	speed_rank = db.Column(db.Integer)
	speed_rank_mod = db.Column(db.Integer)
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
	direction = db.Column(db.String())
	turns = db.Column(db.Integer)
	degree = db.Column(db.Integer, db.ForeignKey('skill_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	keyword = db.Column(db.String())
	title = db.Column(db.Integer, db.ForeignKey('skill_move_type.id'))
	
	
	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'speed': self.speed,
			'speed_rank': self.speed_rank,
			'speed_rank_mod': self.speed_rank_mod,
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
			'direction': self.direction,
			'turns': self.turns,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'time': self.time,
			'keyword': self.keyword,
			'title': self.title
		}

class SkillOpposed(db.Model):
	__tablename__ = 'skill_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	recurring_value = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	description = db.Column(db.String())
	keyword = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('skill_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('skill_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('skill_time.id'))
	degree_check = db.Column(db.Boolean)
	circ_check = db.Column(db.Boolean)
	dc_check = db.Column(db.Boolean)
	time_check = db.Column(db.Boolean)
	degree_value = db.Column(db.Integer, db.ForeignKey('skill_degree.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('skill_dc_type.id'))
	dc_player = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	circ_value = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	time_type = db.Column(db.Integer, db.ForeignKey('skill_time_type.id'))
	recurring_type = db.Column(db.Integer, db.ForeignKey('skill_time_type.id'))


	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'recurring_type': self.recurring_type
		}

class SkillTime(db.Model):
	__tablename__ = 'skill_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	recovery_penalty = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)
	degree = db.Column(db.Integer, db.ForeignKey('skill_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('skill_dc.id'))
	turns = db.Column(db.Integer)
	keyword = db.Column(db.String)
	perm = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	round = db.Column(db.Boolean)
	scene = db.Column(db.Boolean)
	instant = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('skill_time_type.id'))
	circ_type = db.Column(db.Integer, db.ForeignKey('skill_circ_type.id'))
	degree_type = db.Column(db.Integer, db.ForeignKey('skill_degree_type.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('skill_dc_type.id'))
	
	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
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
			'recovery_penalty': self.recovery_penalty,
			'recovery_incurable': self.recovery_incurable,
			'degree': self.degree,
			'circ': self.circ,
			'dc': self.dc,
			'turns': self.turns,
			'keyword': self.keyword,
			'perm': self.perm,
			'turn': self.turn,
			'round': self.round,
			'scene': self.scene,
			'instant': self.instant,
			'hide': self.hidden,
			'title': self.title,
			'circ_type': self.circ_type,
			'degree_type': self.degree_type,
			'dc_type': self.dc_type
		}