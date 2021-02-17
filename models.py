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
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

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
	power_circ = db.Column(db.Boolean)
	skill_dc = db.Column(db.Boolean)
	skill_degree = db.Column(db.Boolean)
	bonus_dc = db.Column(db.Boolean)
	bonus_degree = db.Column(db.Boolean)
	bonus_circ = db.Column(db.Boolean)
	advantage_dc = db.Column(db.Boolean)
	advantage_degree = db.Column(db.Boolean)
	advantage_circ = db.Column(db.Boolean)
	
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
			'power_circ': self.power_circ,
			'power_degree': self.power_degree,
			'skill_dc': self.skill_dc,
			'skill_degree': self.skill_degree,
			'bonus_dc': self.bonus_dc,
			'bonus_circ': self.bonus_circ,
			'bonus_degree': self.bonus_degree,
			'advantage_dc': self.advantage_dc,
			'advantage_degree': self.advantage_degree,
			'advantage_circ': self.advantage_circ
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
