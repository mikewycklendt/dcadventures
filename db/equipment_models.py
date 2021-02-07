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
