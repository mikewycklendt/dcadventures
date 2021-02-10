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









if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
