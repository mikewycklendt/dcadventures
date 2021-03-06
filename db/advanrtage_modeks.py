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


class Advantage(db.Model):
	__tablename__ = 'advantages'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	adv_type = db.Column(db.Integer, db.ForeignKey('advantage_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	ranked = db.Column(db.Boolean)
	ranked_ranks = db.Column(db.Integer)
	ranked_max = db.Column(db.Integer)
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	replaced_trait_type = db.Column(db.String())
	replaced_trait =  db.Column(db.Integer)	
	skill_type = db.Column(db.String())
	skill = db.Column(db.Integer)
	skill_description = db.Column(db.String())
	skill_untrained = db.Column(db.Boolean)
	no_pre_check = db.Column(db.Boolean)
	expertise = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	conflict_immune = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	dc_type = db.Column(db.String())
	dc_value = db.Column(db.Integer)
	dc_mod = db.Column(db.Integer)
	alter_target = db.Column(db.String())
	simultaneous = db.Column(db.Boolean)
	simultaneous_type = db.Column(db.String())
	extra_action = db.Column(db.Boolean)
	action1 = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action2 = db.Column(db.Integer, db.ForeignKey('actions.id'))
	invent = db.Column(db.Boolean)
	invent_permanence = db.Column(db.String())
	invent_trait_type = db.Column(db.String())
	invent_trait = db.Column(db.Integer)
	rituals = db.Column(db.Boolean)
	gm_secret_check = db.Column(db.Boolean)
	gm_trait_type = db.Column(db.String())
	gm_trait = db.Column(db.Integer)
	gm_veto = db.Column(db.Boolean)
	language = db.Column(db.Boolean)
	languages = db.Column(db.Integer)
	language_rank = db.Column(db.Integer)
	multiple = db.Column(db.Boolean)
	groups = db.Column(db.Boolean)
	pressure = db.Column(db.Boolean)
	check_check = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	combined = db.Column(db.Boolean)
	condition = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	degree = db.Column(db.Boolean)
	effort = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	minion = db.Column(db.Boolean)
	mods = db.Column(db.Boolean)
	mods_multiple = db.Column(db.String())
	mods_count = db.Column(db.Integer)
	opposed = db.Column(db.Boolean)
	opposed_multiple = db.Column(db.String())
	points = db.Column(db.Boolean)
	resist = db.Column(db.Boolean)
	resist_multiple = db.Column(db.String())
	rounds = db.Column(db.Boolean)
	swap = db.Column(db.Boolean)
	swap_multiple = db.Column(db.String())
	time = db.Column(db.Boolean)
	variable = db.Column(db.Boolean)
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
			'name': self.name,
			'description': self.description,
			'adv_type': self.adv_type,
			'action': self.action,
			'check_type': self.check_type,
			'ranked': self.ranked,
			'ranked_ranks': self.ranked_ranks,
			'ranked_max': self.ranked_max,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'replaced_trait_type': self.replaced_trait_type,
			'replaced_trait': self.replaced_trait,
			'skill_type': self.skill_type,
			'skill': self.skill,
			'skill_description': self.skill_description,
			'skill_untrained': self.skill_untrained,
			'no_pre_check': self.no_pre_check,
			'expertise': self.expertise,
			'conflict': self.conflict,
			'consequence': self.consequence,
			'conflict_immune': self.conflict_immune,
			'dc_type': self.dc_type,
			'dc_value': self.dc_value,
			'dc_mod': self.dc_mod,
			'alter_target': self.alter_target,
			'simultaneous': self.simultaneous,
			'simultaneous_type': self.simultaneous_type,
			'extra_action': self.extra_action,
			'action1': self.action1,
			'action2': self.action2,
			'invent': self.invent,
			'invent_permanence': self.invent_permanence,	
			'invent_trait_type': self.invent_trait_type,
			'invent_trait': self.invent_trait,
			'rituals': self.rituals,
			'gm_secret_check': self.gm_secret_check,
			'gm_trait_type': self.gm_trait_type,
			'gm_trait': self.gm_trait,
			'gm_veto': self.gm_veto,
			'language': self.language,
			'languages': self.languages,
			'language_rank': self.language_rank,
			'multiple': self.multiple,
			'groups': self.groups,
			'pressure': self.pressure,
			'check_check': self.check_check,
			'circumstance': self.circumstance,
			'combined': self.combined,
			'condition': self.condition,
			'dc': self.dc,
			'degree': self.degree,
			'effort': self.effort,
			'levels': self.levels,
			'minion': self.minion,
			'mods': self.mods,
			'mods_multiple': self.mods_multiple,
			'mods_count': self.mods_count,
			'opposed': self.opposed,
			'opposed_multiple': self.opposed_multiple,
			'points': self.points,
			'resist': self.resist,
			'resist_multiple': self.resist_multiple,
			'rounds': self.rounds,
			'swap': self.swap,
			'swap_multiple': self.swap_multiple,
			'time': self.time,
			'variable': self.variable,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base
		}

class AdvantageType(db.Model):
	__tablename__ = 'advantage_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Benefit(db.Model):
	__tablename__ = 'benefits'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	name = db.Column(db.String())
	description = db.Column(db.String())
	effort = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'name': self.name,
			'description': self.description,
			'effort': self.effort,
			'approved': self.approved,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none
		}

class AdvCombined(db.Model):
	__tablename__ = 'advantage_combined'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	ranks = db.Column(db.Integer)
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))

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
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_null = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	damage_value = db.Column(db.Integer)
	damage = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
			'condition_type': self.condition_type,
			'condition': self.condition,
			'condition_null': self.condition_null,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'damage_value': self.damage_value,
			'damage': self.damage
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
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	benefit_turns = db.Column(db.Integer)
	benefit_count = db.Column(db.Integer)
	benefit_effort = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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
	horde = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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
	lasts = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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

class AdvPoints(db.Model):
	__tablename__ = 'advantage_points'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	spend = db.Column(db.String())
	condition_cost = db.Column(db.Integer)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
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
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	benefit_count = db.Column(db.Integer)
	benefit_cost = db.Column(db.Integer)
	benefit_turns = db.Column(db.Integer)
	ranks_gained = db.Column(db.Integer)
	ranks_max = db.Column(db.Integer)
	ranks_lasts = db.Column(db.Integer)
	ranks_trait_type = db.Column(db.String())
	ranks_trait = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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
	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	which = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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
	trait = db.Column(db.Integer)
	end = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
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
	trait = db.Column(db.Integer)
	replaced_trait_type = db.Column(db.String())
	replaced_trait = db.Column(db.Integer)
	multiple = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'replaced_trait_type': self.replaced_trait_type,
			'replaced_trait': self.replaced_trait,
			'multiple': self.multiple
		}

class AdvVariable(db.Model):
	__tablename__ = 'advantage_variable'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
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

class AdvMove(db.Model):
	__tablename__ = 'advantage_move'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	degree = db.Column(db.Integer, db.ForeignKey('advantage_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('advantage_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	keyword = db.Column(db.String())
	title = db.Column(db.Integer, db.ForeignKey('advantage_move_type.id'))
	
	
	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
		
class AdvCheck(db.Model):
	__tablename__ = 'advantage_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	degree = db.Column(db.Integer, db.ForeignKey('advantage_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('advantage_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('advantage_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('advantage_time_type.id'))
	dc_value = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	move = db.Column(db.Integer, db.ForeignKey('advantage_move_type.id'))
	attack = db.Column(db.Integer)
	opposed = db.Column(db.Integer, db.ForeignKey('advantage_opposed.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_target = db.Column(db.String())
	conditions_target = db.Column(db.String())
	
	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
			'opposed': self.opposed,
			'condition': self.condition,
			'condition_target': self.condition_target,
			'conditions_target': self.conditions_target
		}

class AdvCirc(db.Model):
	__tablename__ = 'advantage_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	lasts = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	time = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	title = db.Column(db.Integer, db.ForeignKey('advantage_circ_type.id'))
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
	
	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
			'check_type': self.check_type
		}

class AdvDC(db.Model):
	__tablename__ = 'advantage_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	variable = db.Column(db.Integer, db.ForeignKey('advantage_check.id'))
	title = db.Column(db.Integer, db.ForeignKey('advantage_dc_type.id'))
	time = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	effect_target = db.Column(db.String())
	equipment_use = db.Column(db.String())
	equipment_type = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	equip = db.Column(db.Boolean)
	
	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
			'effect_target': self.effect_target,
			'equipment_use': self.equipment_use,
			'equipment_type': self.equipment_type,
			'equipment': self.equipment,
			'equip': self.equip
		}

class AdvDegree(db.Model):
	__tablename__ = 'advantage_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	level_time = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	circumstance = db.Column(db.Integer, db.ForeignKey('advantage_circ.id'))
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
	condition_turns = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	nullify_type = db.Column(db.String())
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Integer, db.ForeignKey('advantage_degree.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opposed = db.Column(db.Integer, db.ForeignKey('advantage_opposed.id'))
	variable = db.Column(db.Integer, db.ForeignKey('advantage_check.id'))
	resist_dc = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.Integer)
	skill_dc = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	skill_trait_type = db.Column(db.String())
	skill_trait = db.Column(db.Integer)
	routine_trait_type = db.Column(db.String())
	routine_trait = db.Column(db.Integer)
	routine_mod = db.Column(db.Integer)
	attack = db.Column(db.Integer)
	attack_turns = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	compare = db.Column(db.Integer, db.ForeignKey('advantage_opposed.id'))
	time_table = db.Column(db.Boolean)
	move_table = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('advantage_degree_type.id'))
	description = db.Column(db.String())
	effect_target = db.Column(db.String())
	value_type = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
			'value_type': self.value_type,
			'description': self.description
		}


class AdvOpposed(db.Model):
	__tablename__ = 'advantage_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	recurring_value = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	description = db.Column(db.String())
	keyword = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('advantage_degree_type.id'))
	circ = db.Column(db.Integer, db.ForeignKey('advantage_circ_type.id'))
	dc = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	time = db.Column(db.Integer, db.ForeignKey('advantage_time.id'))
	degree_check = db.Column(db.Boolean)
	circ_check = db.Column(db.Boolean)
	dc_check = db.Column(db.Boolean)
	time_check = db.Column(db.Boolean)
	degree_value = db.Column(db.Integer, db.ForeignKey('advantage_degree.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('advantage_dc_type.id'))
	dc_player = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	circ_value = db.Column(db.Integer, db.ForeignKey('advantage_circ.id'))
	time_type = db.Column(db.Integer, db.ForeignKey('advantage_time_type.id'))
	recurring_type = db.Column(db.Integer, db.ForeignKey('advantage_time_type.id'))


	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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

class AdvTime(db.Model):
	__tablename__ = 'advantage_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
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
	recovery_target = db.Column(db.String())
	degree = db.Column(db.Integer, db.ForeignKey('advantage_degree.id'))
	circ = db.Column(db.Integer, db.ForeignKey('advantage_circ.id'))
	dc = db.Column(db.Integer, db.ForeignKey('advantage_dc.id'))
	turns = db.Column(db.Integer)
	keyword = db.Column(db.String)
	perm = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	round = db.Column(db.Boolean)
	next = db.Column(db.Boolean)
	scene = db.Column(db.Boolean)
	instant = db.Column(db.Boolean)
	player = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	title = db.Column(db.Integer, db.ForeignKey('advantage_time_type.id'))
	circ_type = db.Column(db.Integer, db.ForeignKey('advantage_circ_type.id'))
	degree_type = db.Column(db.Integer, db.ForeignKey('advantage_degree_type.id'))
	dc_type = db.Column(db.Integer, db.ForeignKey('advantage_dc_type.id'))
	time = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	
	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'benefit': self.benefit,
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
			'hide': self.hidden,
			'title': self.title,
			'circ_type': self.circ_type,
			'degree_type': self.degree_type,
			'dc_type': self.dc_type,
			'time': self.time,
			'mod': self.mod
		}