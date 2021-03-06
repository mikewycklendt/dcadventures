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
