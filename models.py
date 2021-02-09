from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv

load_dotenv()

import os


db_path = os.environ.get("db_path")

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = db_path
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
db = SQLAlchemy()

def setup_db(app):
	database_path = db_path
	app.config["SQLALCHEMY_DATABASE_URI"] = database_path
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	db.init_app(app)
	db.create_all()

setup_db(app)
migrate = Migrate(app, db)



class Ability(db.Model):
	__tablename__ = 'abilities'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.ARRAY(db.String))
	summary = db.Column(db.String())
	absent = db.Column(db.String())
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))
	icon = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'summary': self.summary,
			'absent': self.absent,
			'modifier_id': self.modifier_id,
			'icon': self.icon
		}

class Defense(db.Model):
	__tablename__ = 'defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	description = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'ability_id': self.ability_id,
			'modifier_id': self.modifier_id
		}

class Modifier(db.Model):
	__tablename__ = 'modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Integer())
	description = db.Column(db.String())
	table = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cost': self.cost,
			'description': self.description,
			'table': self.table
		}

class ModifierTable(db.Model):
	__tablename__ = 'modifiers_table'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	description = db.Column(db.String())
	value = db.Column(db.Integer())
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

	def format(self):
		return {
			'id': self.id,
			'description': self.description,
			'value': self.value,
			'modifier_id': self.modifier_id
		}

class Action(db.Model):
	__tablename__ = 'actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cost': self.cost,
			'turn': self.turn,
			'description': self.description
		}

class ConflictAction(db.Model):
	__tablename__ = 'conflict_actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'action_id': self.action_id
		}


class LevelType(db.Model):
	__tablename__ = 'level_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'name': self.name
		}

class Levels(db.Model):
	__tablename__ = 'levels'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	type_id = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level_type = db.Column(db.String())
	name = db.Column(db.String())
	level_effect = db.Column(db.String())
	power_dc = db.Column(db.Boolean)
	power_degree = db.Column(db.Boolean)
	skill_dc = db.Column(db.Boolean)
	skill_degree = db.Column(db.Boolean)
	bonus_dc = db.Column(db.Boolean)
	bonus_degree = db.Column(db.Boolean)
	advantage_dc = db.Column(db.Boolean)
	advantage_degree = db.Column(db.Boolean)
	
	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'skill_id': self.skill_id,
			'extra_id': self.extra_id,
			'type_id': self.type_id,
			'level_type': self.level_type,
			'name': self.name,
			'level_effect': self.level_effect,
			'power_dc': self.power_dc,
			'power_degree': self.power_degree,
			'skill_dc': self.skill_dc,
			'skill_degree': self.skill_degree,
			'bonus_dc': self.bonus_dc,
			'bonus_degree': self.bonus_degree
		}


class Skill(db.Model):
	__tablename__ = 'skills'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	untrained = db.Column(db.Boolean)
	tools = db.Column(db.Boolean)
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))
	description = db.Column(db.String())
	table = db.Column(db.Boolean)
	icon = db.Column(db.String())

	def format(self):
		return {
			'id':  self.id,
			'name': self.name,
			'ability_id': self.ability_id,
			'untrained': self.untrained,
			'tools': self.tools,
			'check_id': self.check_id,
			'action_id': self.action_id,
			'description': self.description,
			'table': self.table,
			'icon': self.icon
		}

class SkillTable(db.Model):
	__tablename__ = 'skill_tables'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	dc = db.Column(db.Integer)
	description = db.Column(db.String())
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))
	degree = db.Column(db.Boolean)
	measurement  = db.Column(db.Integer)
	complexity = db.Column(db.String())
	modifier = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	requires_sub = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'dc': self.dc,
			'description': self.description,
			'check_id': self.check_id,
			'modifier_id': self.modifier_id,
			'degree': self.degree,
			'measurement': self.measurement,
			'complexity': self.complexity,
			'modifier': self.modifier,
			'circumstance': self.circumstance,
			'requires_sub': self.requires_sub
		}

class SkillType(db.Model):
	__tablename__ = 'skill_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	group = db.Column(db.Boolean)
	team = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'check_id': self.check_id,
			'group': self.group,
			'team': self.team,
			'gm': self.gm,
			'description': self.description
		}


class Benefit(db.Model):
	__tablename__ = 'benefits'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	name = db.Column(db.String())
	description = db.Column(db.String())
	effort = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'name': self.name,
			'description': self.description,
			'effort': self.effort,
			'approved': self.approved
		}


class Consequence(db.Model):
	__tablename__ = 'consequences'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	
	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}


class Check(db.Model):
	__tablename__ = 'checks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	critical = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	automatic = db.Column(db.Boolean)
	routine = db.Column(db.Boolean)
	graded = db.Column(db.Boolean)
	roll = db.Column(db.Boolean)
	compare = db.Column(db.Boolean)
	fail = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'critical': self.critical,
			'dc': self.dc,
			'opposed': self.opposed,
			'automatic': self.automatic,
			'routine': self.routine,
			'graded': self.graded,
			'roll': self.roll,
			'compare': self.compare,	
			'fail': self.fail
		}

class Condition(db.Model):
	__tablename__ = 'conditions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	phase = db.Column(db.Integer)
	supercede = db.Column(db.String())
	specific = db.Column(db.Boolean)
	multiple = db.Column(db.Boolean)
	time = db.Column(db.Integer)
	unit = db.Column(db.String())
	effects = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'phase': self.phase,
			'supercede': self.supercede,
			'specific': self.specific,
			'multiple': self.multiple,
			'time': self.time,
			'unit': self.unit,
			'effects': self.effects,
			'description': self.description
		}

class DamageType(db.Model):
	__tablename__ = 'damage_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
		}
		
class Damage(db.Model):
	__tablename__ = 'damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	damage_type = db.Column(db.Integer, db.ForeignKey('damage_type.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
		}



class Phase(db.Model):
	__tablename__ = 'phases'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Cover(db.Model):
	__tablename__ = 'cover'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Nature(db.Model):
	__tablename__ = 'nature'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}


class Conceal(db.Model):
	__tablename__ = 'concealment'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Maneuver(db.Model):
	__tablename__ = 'maneuvers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class MeasureType(db.Model):
	__tablename__ = 'measurement_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Emotion(db.Model):
	__tablename__ = 'emotions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Ground(db.Model):
	__tablename__ = 'ground'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Range(db.Model):
	__tablename__ = 'range'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	distance = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'distance': self.distance
		}

class Ranged(db.Model):
	__tablename__ = 'ranged'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'show': self.show
		}

class Unit(db.Model):
	__tablename__ = 'unit_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'type_id': self.type_id
		}

class Material(db.Model):
	__tablename__ = 'materials'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	toughness = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'toughness': self.toughness
		}

class Complex(db.Model):
	__tablename__ = 'complexity'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	dc = db.Column(db.Integer)
	time = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'dc': self.dc,
			'time': self.time
		}

class Sense(db.Model):
	__tablename__ = 'senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class SubSense(db.Model):
	__tablename__ = 'sub_senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	sense_id = db.Column(db.Integer, db.ForeignKey('senses.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'sense_id': self.sense_id
		}

class Math(db.Model):
	__tablename__ = 'math'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	symbol = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'symbol': self.symbol
		}

class Rank(db.Model):
	__tablename__ = 'ranks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	rank_type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'rank_type': self.rank_type
		}

class Measurement(db.Model):
	__tablename__ = 'measurements'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	rank = db.Column(db.Integer)
	mass = db.Column(db.Float(asdecimal=True))
	mass_unit = db.Column(db.String())
	time = db.Column(db.Float(asdecimal=True))
	time_unit =db.Column(db.String())
	distance = db.Column(db.Float(asdecimal=True))
	distance_unit = db.Column(db.String())
	volume = db.Column(db.Float(asdecimal=True))
	volume_unit = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'rank': self.rank,
			'mass': self.mass,
			'mass_unit': self.mass_unit,
			'time': self.time,
			'time_unit': self.time_unit,
			'distance': self.distance,
			'distance_unit': self.distance_unit,
			'volume': self.volume,
			'volume_unit': self.volume_unit
		}

class MassCovert(db.Model):
	__tablename__ = 'mass_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	pound = db.Column(db.Integer)
	tons = db.Column(db.Integer)
	kilotons = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'pound': self.pound,
			'tons': self.tons,
			'kilotons': self.kilotons
		}

class TimeCovert(db.Model):
	__tablename__ = 'time_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	seconds = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	hours = db.Column(db.Integer)
	days = db.Column(db.Integer)
	weeks = db.Column(db.Integer)
	months = db.Column(db.Integer)
	years = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'seconds': self.seconds,
			'minutes': self.minutes,
			'hours': self.hours,
			'days': self.days,
			'weeks': self.weeks,
			'months': self.months,
			'years': self.years
		}

class DistanceCovert(db.Model):
	__tablename__ = 'distance_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	inches = db.Column(db.Integer)
	feet = db.Column(db.Integer)
	mile = db.Column(db.Integer)
	lightyear = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'inches': self.inches,
			'feet': self.feet,
			'mile': self.mile,
			'lightyear': self.lightyear 
		}

class VolumeCovert(db.Model):
	__tablename__ = 'volume_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cft = db.Column(db.Integer)
	million = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cft': self.cft,
			'million': self.million 
		}

class Environment(db.Model):
	__tablename__ = 'environments'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Job(db.Model):
	__tablename__ = 'jobs'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Creature(db.Model):
	__tablename__ = 'creature'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}	

class Light(db.Model):
	__tablename__ = 'light'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
