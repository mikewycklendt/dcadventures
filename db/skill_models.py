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

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}




class SkillAbility(db.Model):
	__tablename__ = 'skill_ability'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	circumstance = db.Column(db.String())


	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'ability': self.ability,
			'circumstance': self.circumstance
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
	trait = db.Column(db.String())
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	conflict_weapon = db.Column(db.Boolean)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	action_type = db.Column(db.String())
	action = db.Column(db.Integer)
	free = db.Column(db.Boolean)

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
			'free': self.free
		}

class SkillCirc(db.Model):
	__tablename__ = 'skill_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	circ_target = db.Column(db.String())
	mod = db.Column(db.Integer)
	effect = db.Column(db.String())
	speed = db.Column(db.Integer)
	temp = db.Column(db.Integer)
	target = db.Column(db.String())
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	time = db.Column(db.Integer)
	condition_type = db.Column(db.String())
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	conditions = db.Column(db.Integer)
	conditions_effect = db.Column(db.Integer)
	measure_effect = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.String())
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	keyword = db.Column(db.String())
	cumulative = db.Column(db.Boolean)
	optional = db.Column(db.Boolean)
	lasts = db.Column(db.String())
	turns = db.Column(db.Integer)
	unit_time = db.Column(db.Integer)
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_rank = db.Column(db.Integer)
	circumstance = db.Column(db.String())

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
			'lasts': self.lasts,
			'turns': self.turns,
			'unit_time': self.unit_time,
			'time_units': self.time_units,
			'time_rank': self.time_rank,
			'circumstance': self.circumstance
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
	math_trait = db.Column(db.String())
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	damage = db.Column(db.Boolean)
	cover = db.Column(db.Boolean)
	complex = db.Column(db.Boolean)
	measure = db.Column(db.Boolean)
	change_action = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action_when = db.Column(db.String())
	damage_type = db.Column(db.String())
	inflict_type = db.Column(db.String())
	inflict_flat = db.Column(db.Integer)
	inflict_trait_type = db.Column(db.String())
	inflict_trait = db.Column(db.String())
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	measure_effect = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.String())
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	condition_turns = db.Column(db.Integer)
	keyword = db.Column(db.String())
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))

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
			'level_type': self.level_type,
			'level': self.level,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'condition_turns': self.condition_turns,
			'keyword': self.keyword,
			'complexity': self.complexity
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
	inflict_trait = db.Column(db.String())
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	consequence_action_type = db.Column(db.String())
	consequence_action = db.Column(db.Integer)
	consequence_trait_type = db.Column(db.String())
	consequence_trait = db.Column(db.String())
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	knowledge = db.Column(db.String())
	knowledge_count = db.Column(db.Integer)
	knowledge_specificity = db.Column(db.String())
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	level_direction = db.Column(db.Integer)
	circumstance = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	circ_target = db.Column(db.String())
	measure_effect = db.Column(db.String())
	measure_rank_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.String())
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_mod = db.Column(db.Integer)
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	condition_turns = db.Column(db.Integer)
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)

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
			'condition_type': self.condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'condition_turns': self.condition_turns,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'cumulative': self.cumulative,
			'linked': self.linked
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
	environment = db.Column(db.Integer)
	environment_other = db.Column(db.String())
	sense = db.Column(db.Integer)
	mod_range = db.Column(db.Integer)
	subsense = db.Column(db.Integer)
	cover = db.Column(db.Integer)
	conceal = db.Column(db.Integer)
	maneuver = db.Column(db.Integer)
	weapon_melee = db.Column(db.Integer)
	weapon_ranged = db.Column(db.Integer)
	tools = db.Column(db.String())
	condition = db.Column(db.String())
	power = db.Column(db.String())
	consequence = db.Column(db.Integer)
	creature = db.Column(db.Integer)
	creature_other = db.Column(db.String())
	emotion = db.Column(db.Integer)
	emotion_other = db.Column(db.String())
	conflict = db.Column(db.Integer)
	profession = db.Column(db.Integer)
	profession_other = db.Column(db.String())
	bonus_trait_type = db.Column(db.String())
	bonus_trait = db.Column(db.String())
	bonus_check = db.Column(db.Integer)
	bonus_check_range = db.Column(db.Integer)
	bonus_conflict = db.Column(db.Integer)
	penalty_trait_type = db.Column(db.String())
	penalty_trait = db.Column(db.String())
	penalty_check = db.Column(db.Integer)
	penalty_check_range = db.Column(db.Integer)
	penalty_conflict = db.Column(db.Integer)
	bonus_active_defense = db.Column(db.Boolean)
	bonus_conflict_defend = db.Column(db.Boolean)
	penalty_active_defense = db.Column(db.Boolean)
	penalty_conflict_defend = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	multiple_count = db.Column(db.Integer)
	lasts = db.Column(db.Integer)
	skill = db.Column(db.Integer)
	light = db.Column(db.Integer)

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

class SkillOpposed(db.Model):
	__tablename__ = 'skill_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	attached = db.Column(db.String())
	frequency = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.String())
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	secret = db.Column(db.Boolean)
	recurring = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	recurring_value = db.Column(db.Integer)
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))

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
			'opponent_check': self.opponent_check,
			'secret': self.secret,
			'recurring': self.recurring,
			'multiple': self.multiple,
			'recurring_value': self.recurring_value,
			'recurring_units': self.recurring_units
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
	trait = db.Column(db.String())
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_value = db.Column(db.Integer)
	recovery = db.Column(db.Boolean)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)

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
			'recovery': self.recovery,
			'recovery_penalty': self.recovery_penalty,
			'recovery_time': self.recovery_time,
			'recovery_incurable': self.recovery_incurable
		}