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

class EquipType(db.Model):
	__tablename__ = 'equipment_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Equipment(db.Model):
	__tablename__ = 'equipment'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	cost = db.Column(db.Integer)
	description = db.Column(db.String())
	toughness = db.Column(db.Integer)
	expertise = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	alternate = db.Column(db.Boolean)
	move = db.Column(db.Boolean)
	speed_mod = db.Column(db.Integer)
	direction = db.Column(db.String())
	locks = db.Column(db.Boolean)
	lock_type = db.Column(db.String())
	mod_multiple = db.Column(db.String())
	mod_multiple_count = db.Column(db.Integer)
	check = db.Column(db.Boolean)
	damaged = db.Column(db.Boolean)
	descriptor = db.Column(db.Boolean)
	feature = db.Column(db.Boolean)
	limits = db.Column(db.Boolean)
	modifiers = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'type_id': self.type_id,
			'cost': self.cost,
			'description': self.description,
			'toughness': self.toughness,
			'expertise': self.expertise,
			'alternate': self.alternate,
			'move': self.move,
			'speed_mod': self.speed_mod,
			'direction': self.direction,
			'locks': self.locks,
			'lock_type': self.lock_type,
			'mod_multiple': self.mod_multiple,
			'mod_multiple_count': self.mod_multiple_count,
			'check': self.check,
			'damaged': self.damaged,
			'descriptor': self.descriptor,
			'feature': self.feature,
			'limits': self.limits,
			'modifiers': self.modifiers,
			'opposed': self.opposed
		}

class Feature(db.Model):
	__tablename__ = 'features'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	name = db.Column(db.String())
	description = db.Column(db.String())
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	toughness = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'name': self.name,
			'description': self.description,
			'feature': self.feature,
			'toughness': self.toughness
		}

class EquipEffect(db.Model):
	__tablename__ = 'equipment_effect'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	name = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'name': self.name,
			'description': self.description
		}
	
class EquipBelt(db.Model):
	__tablename__ = 'equipment_belt'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	cost = db.Column(db.Integer)
	belt_item_type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'feature': self.feature,
			'weapon': self.weapon,
			'equipment': self.equipment,
			'cost': self.cost,
			'belt_item_type': self.belt_item_type
		}
	
class EquipCheck(db.Model):
	__tablename__ = 'equipment_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	when = db.Column(db.String())
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action_time = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
			'when': self.when,
			'skill_type': self.skill_type,
			'skill': self.skill,
			'check_type': self.check_type,
			'action': self.action,
			'action_time': self.action_time
		}	

class EquipDamage(db.Model):
	__tablename__ = 'equipment_damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	toughness = db.Column(db.Integer)
	penalty = db.Column(db.String())
	
	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
			'damage': self.damage,
			'skill_type': self.skill_type,
			'skill': self.skill,
			'toughness': self.toughness,
			'penalty': self.penalty
		}	
	
class EquipDescriptor(db.Model):
	__tablename__ = 'equipment_descriptor'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	descriptor = db.Column(db.Integer, db.ForeignKey('descriptors.id'))

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
			'descriptor': self.descriptor
		}	
	
class EquipLimit(db.Model):
	__tablename__ = 'equipment_limits'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	time = db.Column(db.Integer)
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	range = db.Column(db.Integer)
	range_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	extend = db.Column(db.Boolean)
	extendable = db.Column(db.Boolean)
	time_capacity = db.Column(db.Integer)
	time_capacity_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	capacity = db.Column(db.Integer)
	item = db.Column(db.String())
	ammo = db.Column(db.Boolean)
	fuel = db.Column(db.Boolean)
	area_long = db.Column(db.Integer)
	area_wide = db.Column(db.Integer)
	area_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	recharge = db.Column(db.Boolean)
	refill = db.Column(db.Boolean)
	uses = db.Column(db.Integer)
	light = db.Column(db.Integer, db.ForeignKey('light.id'))
	internet = db.Column(db.Boolean)
	needs_internet = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
			'time': self.time,
			'time_units': self.time_units,
			'range': self.range,
			'range_units': self.range_units,
			'extend': self.extend,
			'extendable': self.extendable,
			'time_capacity': self.time_capacity,
			'time_capacity_units': self.time_capacity_units,
			'capacity': self.capacity,
			'item': self.item,
			'ammo': self.ammo,
			'fuel': self.fuel,
			'area_long': self.area_long,
			'area_wide': self.area_wide,
			'area_units': self.area_units,
			'recharge': self.recharge,
			'refill': self.refill,
			'uses': self.uses,
			'light': self.light,
			'internet': self.internet,
			'needs_interneT': self.needs_internet
		}	
	
class EquipMod(db.Model):
	__tablename__ = 'equipment_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
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
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
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
	
class EquipOpposed(db.Model):
	__tablename__ = 'equipment_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	dc = db.Column(db.Integer)
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	when = db.Column(db.String())
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'equip_id': self.equip_id,
			'effect': self.effect,
			'feature': self.feature,
			'dc': self.dc,
			'skill_type': self.skill_type,
			'skill': self.skill,
			'check': self.check,
			'when': self.when,
			'condition1': self.condition1,
			'condition2': self.condition2
		}	