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


class MeasureType(db.Model):
	__tablename__ = 'measurement_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
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
