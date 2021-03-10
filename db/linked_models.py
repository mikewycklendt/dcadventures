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


class SkillCircType(db.Model):
	__tablename__ = 'skill_circ_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class SkillDCType(db.Model):
	__tablename__ = 'skill_dc_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class SkillDegreeType(db.Model):
	__tablename__ = 'skill_degree_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class SkillMoveType(db.Model):
	__tablename__ = 'skill_move_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class SkillTimeType(db.Model):
	__tablename__ = 'skill_time_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}


class AdvCircType(db.Model):
	__tablename__ = 'advantage_circ_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class AdvDCType(db.Model):
	__tablename__ = 'advantage_dc_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class AdvDegreeType(db.Model):
	__tablename__ = 'advantage_degree_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class AdvMoveType(db.Model):
	__tablename__ = 'advantage_move_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class AdvTimeType(db.Model):
	__tablename__ = 'advantage_time_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}


class PowerCircType(db.Model):
	__tablename__ = 'power_circ_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	power_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class PowerDCType(db.Model):
	__tablename__ = 'power_dc_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	power_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}
		
class PowerDegreeType(db.Model):
	__tablename__ = 'power_degree_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	power_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class PowerMoveType(db.Model):
	__tablename__ = 'power_move_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	power_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}

class PowerTimeType(db.Model):
	__tablename__ = 'power_time_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	power_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id
		}