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
	
	trait = db.Column(db.String())
	replaced_trait =  db.Column(db.String())
	
	invent_trait = db.Column(db.String())
	
	gm_trait = db.Column(db.String())

			'trait': self.trait,

			'replaced_trait': self.replaced_trait,

			'invent_trait': self.invent_trait,
	
			'gm_trait': self.gm_trait,
	
	

class AdvAltCheck(db.Model):

	trait = db.Column(db.String())

			'trait': self.trait,


class AdvCirc(db.Model):

	check_trait = db.Column(db.String())

	null_trait = db.Column(db.String())

	null_override_trait = db.Column(db.String())


			'check_trait': self.check_trait,

			'null_trait': self.null_trait,

			'null_override_trait': self.null_override_trait

		
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

	math_trait = db.Column(db.String())

	check_trait = db.Column(db.String())



			'math_trait': self.math_trait,

			'check_trait': self.check_trait,


class AdvDegree(db.Model):
	
	consequence_trait = db.Column(db.String())

	circ_trait = db.Column(db.String())

	measure_trait = db.Column(db.String())

			'consequence_trait': self.consequence_trait,

			'circ_trait': self.circ_trait,

			'measure_trait': self.measure_trait,


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

	attitude_trait = db.Column(db.String())

			'attitude_trait': self.attitude_trait,

class AdvMod(db.Model):
	
	bonus_trait = db.Column(db.String())

	penalty_trait = db.Column(db.String())

			'bonus_trait': self.bonus_trait,

			'penalty_trait': self.penalty_trait,


class AdvOpposed(db.Model):

	trait = db.Column(db.String())

	opponent_trait = db.Column(db.String())

			'trait': self.trait,

			'opponent_trait': self.opponent_trait,


class AdvPoints(db.Model):

	ranks_trait = db.Column(db.String())

			'ranks_trait': self.ranks_trait


class AdvResist(db.Model):

	trait = db.Column(db.String())


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

	trait = db.Column(db.String())


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

	trait = db.Column(db.String())

	replaced_trait = db.Column(db.String())


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


	trait = db.Column(db.String())


	def format(self):
		return {
			'id': self.id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'active': self.active,
			'effort': self.effort
		}
