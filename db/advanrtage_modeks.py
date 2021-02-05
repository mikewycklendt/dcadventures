from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import setup_db
from models import SkillBonus, db

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


class AdvAltCheck(db.Model):
	__tablename__ = 'advantage_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	check_trigger = db.Column(db.String())
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
			'benefit': self.benefit,
			'check_trigger': self.check_trigger,
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

class AdvCirc(db.Model):
	__tablename__ = 'advantage_circumstance'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	target = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	circ_type = db.Column(db.String())
	circ_range = db.Column(db.Integer, db.ForeignKey('range.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	check_who = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	null_type = db.Column(db.String())
	null_condition = db.Column(db.String())
	null_trait_type = db.Column(db.String())
	null_trait = db.Column(db.String())
	null_override_trait_type = db.Column(db.String())
	null_override_trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'target': self.target,
			'benefit': self.benefit,
			'mod': self.mod,
			'rounds': self.rounds,
			'circumstance': self.circumstance,
			'circ_type': self.circ_type,
			'circ_range': self.circ_range,
			'conflict': self.conflict,
			'check_who': self.check_who,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'null_type': self.null_type,
			'null_condition': self.null_condition,
			'null_trait_type': self.null_trait_type,
			'null_trait': self.null_trait,
			'null_override_trait_type': self.null_override_trait_type,
			'null_override_trait': self.null_override_trait
		}
		
class AdvCombined(db.Model):
	__tablename__ = 'advantage_combined'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	ranks = db.Column(db.Integer)
	advantage = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'ranks': self.ranks,
			'advantage': self.advantage
		}

class AdvCondition(db.Model):
	__tablename__ = 'advantage_condition'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	condition_type = db.Column(db.String())
	condition = db.Column(db.String())
	condition_null = db.Column(db.String())
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	damage_value = db.Column(db.Integer)
	damage = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'condition_type': self.condition_type,
			'condition': self.condition,
			'condition_null': self.condition_null,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'damage_value': self.damage_value,
			'damage': self.damage
		}

class AdvDC(db.Model):
	__tablename__ = 'advantage_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	target = db.Column(db.String())
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	dc = db.Column(db.String())
	description = db.Column(db.String())
	value_value = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_trait_type = db.Column(db.String())
	math_trait = db.Column(db.String())
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	keyword = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	check_mod = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'target': self.target,
			'benefit': self.benefit,
			'dc': self.dc,
			'description': self.description,
			'value_value': self.value_value,
			'math_value': self.math_value,
			'math_math': self.math_math,
			'math_trait_type': self.math_trait_type,
			'math_trait': self.math_trait,
			'condition': self.condition,
			'keyword_check': self.keyword_check,
			'check_type': self.check_type,
			'levels': self.levels,
			'level_type': self.level_type,
			'level': self.level,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_mod': self.check_mod
		}

class AdvDegree(db.Model):
	__tablename__ = 'advantage_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	target = db.Column(db.String())
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	value = db.Column(db.Integer)
	deg_mod_type = db.Column(db.String())
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
	circ_value = db.Column(db.Integer)
	circ_turns = db.Column(db.Integer)
	circ_trait_type = db.Column(db.String())
	circ_trait = db.Column(db.String())
	measure_type = db.Column(db.String())
	measure_val1 = db.Column(db.Integer)
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.String())
	measure_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'target': self.target,
			'benefit': self.benefit,
			'value': self.value,
			'deg_mod_type': self.deg_mod_type,
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
			'circ_value': self.circ_value,
			'circ_turns': self.circ_turns,
			'circ_trait_type': self.circ_trait_type,
			'circ_trait': self.circ_trait,
			'measure_type': self.measure_type,
			'measure_val1': self.measure_val1,
			'measure_math': self.measure_math,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_value': self.measure_value,
			'measure_rank': self.measure_rank,
			'condition_type': self.condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'cumulative': self.cumulative,
			'linked': self.linked
		}

class AdvEffort(db.Model):
	__tablename__ = 'advantage_effort'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	effect = db.Column(db.String())
	condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	benefit_choice = db.Column(db.Integer)
	benefit_turns = db.Column(db.Integer)
	benefit_count = db.Column(db.Integer)
	benefit_effort = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'effect': self.effect,
			'condition_type': self.condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'benefit_choice': self.benefit_choice,
			'benefit_turns': self.benefit_turns,
			'benefit_count': self.benefit_count,
			'benefit_effort': self.benefit_effort
		}

class AdvMinion(db.Model):
	__tablename__ = 'advantage_minion'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	points = db.Column(db.Integer)
	condition = db.Column(db.String())
	player_condition = db.Column(db.String())
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
	attitude_trait = db.Column(db.String())
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))
	resitable_dc = db.Column(db.Integer)
	multiple_value = db.Column(db.Integer)
	horde = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
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
			'horde': self.horde
		}

class AdvMod(db.Model):
	__tablename__ = 'advantage_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
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

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
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
			'lasts': self.lasts
		}

class AdvOpposed(db.Model):
	__tablename__ = 'advantage_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.String())
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	multiple = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'opponent_trait_type': self.opponent_trait_type,
			'opponent_trait': self.opponent_trait,
			'opponent_mod': self.opponent_mod,
			'player_check': self.player_check,
			'opponent_check': self.opponent_check,
			'multiple': self.multiple
		}

class AdvPoints(db.Model):
	__tablename__ = 'advantage_points'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	spend = db.Column(db.String())
	condition_cost = db.Column(db.Integer)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	equipment_points = db.Column(db.Integer)
	equipment_vehicles = db.Column(db.Boolean)
	equipment_headquarters = db.Column(db.Boolean)
	initiative_cost = db.Column(db.Integer)
	twenty = db.Column(db.Integer)
	check_bonus = db.Column(db.Integer)
	check_cost = db.Column(db.Integer)
	check_turns = db.Column(db.Integer)
	check_target = db.Column(db.String())
	check_all = db.Column(db.Boolean)
	benefit_choice = db.Column(db.Integer)
	benefit_count = db.Column(db.Integer)
	benefit_cost = db.Column(db.Integer)
	benefit_turns = db.Column(db.Integer)
	ranks_gained = db.Column(db.Integer)
	ranks_max = db.Column(db.Integer)
	ranks_lasts = db.Column(db.Integer)
	ranks_trait_type = db.Column(db.String())
	ranks_trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'spend': self.spend,
			'condition_cost': self.condition_cost,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'equipment_points': self.equipment_points,
			'equipment_vehicles': self.equipment_vehicles,
			'equipment_headquarters': self.equipment_headquarters,
			'initiative_cost': self.initiative_cost,
			'twenty': self.twenty,
			'check_bonus': self.check_bonus,
			'check_cost': self.check_cost,
			'check_turns': self.check_turns,
			'check_target': self.check_target,
			'check_all': self.check_all,
			'benefit_choice': self.benefit_choice,
			'benefit_count': self.benefit_count,
			'benefit_cost': self.benefit_cost,
			'benefit_turns': self.benefit_turns,
			'ranks_gained': self.ranks_gained,
			'ranks_max': self.ranks_max,
			'ranks_lasts': self.ranks_lasts,
			'ranks_trait_type': self.ranks_trait_type,
			'ranks_trait': self.ranks_trait
		}

class AdvResist(db.Model):
	__tablename__ = 'advantage_resist'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	mod = db.Column(db.Integer)
	which = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'which': self.which
		}

class AdvRounds(db.Model):
	__tablename__ = 'advantage_rounds'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	rounds = db.Column(db.Integer)
	cost = db.Column(db.Integer, db.ForeignKey('actions.id'))
	check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	end = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'rounds': self.rounds,
			'cost': self.cost,
			'check': self.check,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'end': self.end
		}


class AdvSkill(db.Model):
	__tablename__ = 'advantage_skill'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	replaced_trait_type = db.Column(db.String())
	replaced_trait = db.Column(db.String())
	multiple = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'replaced_trait_type': self.replaced_trait_type,
			'replaced_trait': self.replaced_trait,
			'multiple': self.multiple
		}

class AdvTime(db.Model):
	__tablename__ = 'advantage_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	time_type = db.Column(db.String())
	value_type = db.Column(db.String())
	value = db.Column(db.Integer)
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	dc = db.Column(db.Integer)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recovery = db.Column(db.Boolean)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'time_type': self.time_type,
			'value_type': self.value_type,
			'value': self.value,
			'units': self.units,
			'time_value': self.time_value,
			'math': self.math,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'dc': self.dc,
			'check_type': self.check_type,
			'recovery': self.recovery,
			'recovery_penalty': self.recovery_penalty,
			'recovery_time': self.recovery_time,
			'recovery_incurable': self.recovery_incurable
		}

class AdvVariable(db.Model):
	__tablename__ = 'advantage_variable'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	active = db.Column(db.Boolean)
	effort = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'active': self.active,
			'effort': self.effort
		}