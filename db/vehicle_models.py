from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import setup_db
from models import SkillBonus, db

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

class Vehicle(db.Model):
	__tablename__ = 'vehicles'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.id'))
	size = db.Column(db.Integer, db.ForeignKey('vehicle_size.id'))
	strength = db.Column(db.Integer)
	speed = db.Column(db.Integer)
	toughness = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	feature = db.Column(db.Boolean)
	power = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'type_id': self.type_id,
			'size': self.size,
			'strength': self.strength,
			'speed': self.speed,
			'toughness': self.toughness,
			'defense': self.defense,
			'cost': self.cost,
			'feature': self.feature,
			'power': self.power
		}
		
class VehicleType(db.Model):
	__tablename__ = 'vehicle_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}
		
class VehicleSize(db.Model):
	__tablename__ = 'vehicle_size'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	strength = db.Column(db.Integer)
	toughness = db.Column(db.Integer)
	defense = db.Column(db.Integer)
	size = db.Column(db.Integer)
	cost = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'size': self.size,
			'strength': self.strength,
			'toughness': self.toughness,
			'defense': self.defense,
			'cost': self.cost
		}

class VehPower(db.Model):
	__tablename__ = 'vehicle_powers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'vehicle_id': self.vehicle_id,
			'power': self.power,
			'cost': self.cost,
			'ranks': self.ranks
		}

class VehFeature(db.Model):
	__tablename__ = 'vehicle_features'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	cost = db.Column(db.Integer)
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	addon = db.Column(db.String())


	def format(self):
		return {
			'id': self.id,
			'vehicle_id': self.vehicle_id,
			'feature': self.feature,
			'cost': self.cost,
			'equipment': self.equipment,
			'weapon': self.weapon,
			'addon': self.addon
		}
