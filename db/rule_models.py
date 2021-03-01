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


class Ability(db.Model):
	__tablename__ = 'abilities'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.ARRAY(db.String))
	summary = db.Column(db.String())
	absent = db.Column(db.String())
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))
	icon = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	power = db.Column(db.Boolean)
	extra = db.Column(db.Boolean)
	skill = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'summary': self.summary,
			'absent': self.absent,
			'modifier_id': self.modifier_id,
			'icon': self.icon,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'power': self.power,
			'extra': self.extra,
			'skill': self.skill,
			'hide': self.hide
		}

class Defense(db.Model):
	__tablename__ = 'defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	description = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))
	all = db.Column(db.Boolean)	
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'ability_id': self.ability_id,
			'modifier_id': self.modifier_id,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
		}

class Action(db.Model):
	__tablename__ = 'actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	description = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cost': self.cost,
			'turn': self.turn,
			'description': self.description,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
		}

class ConflictAction(db.Model):
	__tablename__ = 'conflict_actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'action_id': self.action_id,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
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
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

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
			'icon': self.icon,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
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
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	free = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

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
			'fail': self.fail,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'free': self.free,
			'hide': self.hide
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
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	linked_first = db.Column(db.Boolean)
	linked_second = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

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
			'description': self.description,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'linked_first': self.linked_first,
			'linked_second': self.linked_second,
			'hide': self.hide
		}

class Maneuver(db.Model):
	__tablename__ = 'maneuvers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
		}

class Ranged(db.Model):
	__tablename__ = 'ranged'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	show = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'show': self.show,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
		}

class Sense(db.Model):
	__tablename__ = 'senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
		}

class SubSense(db.Model):
	__tablename__ = 'sub_senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	sense_id = db.Column(db.Integer, db.ForeignKey('senses.id'))
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'sense_id': self.sense_id,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide
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

class Consequence(db.Model):
	__tablename__ = 'consequences'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	
	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'linked': self.linked,
			'hide': self.hide
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

class Cover(db.Model):
	__tablename__ = 'cover'
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



class Phase(db.Model):
	__tablename__ = 'phases'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
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

