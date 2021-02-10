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


class Descriptor(db.Model):
	__tablename__ = 'descriptors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	origin = db.Column(db.Integer, db.ForeignKey('origin.id'))
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	medium = db.Column(db.Integer, db.ForeignKey('medium.id'))
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	result = db.Column(db.String())
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)
	rarity = db.Column(db.String())
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'origin': self.origin,
			'source': self.source,
			'medium': self.medium,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'result': self.result,
			'description': self.description,
			'damage': self.damage,
			'rarity': self.rarity
		}

class Origin(db.Model):
	__tablename__ = 'origin'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}

class Source(db.Model):
	__tablename__ = 'source'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'damage': self.damage
		}

class MediumType(db.Model):
	__tablename__ = 'medium_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'damage': self.damage
		}

class MediumSubType(db.Model):
	__tablename__ = 'medium_subtype'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'description': self.description,
			'damage': self.damage
		}

class Medium(db.Model):
	__tablename__ = 'medium'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'description': self.description,
			'damage': self.damage
		}