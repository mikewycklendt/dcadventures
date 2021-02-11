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



class Headquarters(db.Model):
	__tablename__ = 'headquarters'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	size = db.Column(db.Integer, db.ForeignKey('headquarters_size.id'))
	toughness = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	shared = db.Column(db.Boolean)
	addon = db.Column(db.Boolean)
	feature = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'size': self.size,
			'toughness': self.toughness,
			'cost': self.cost,
			'shared': self.shared,
			'addon': self.addon,
			'feature': self.feature,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base
		}

class HeadSize(db.Model):
	__tablename__ = 'headquarters_size'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	size = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'size': self.size
		}


class HeadFeature(db.Model):
	__tablename__ = 'headquarters_features'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}


class HeadCharFeat(db.Model):
	__tablename__ = 'headquarters_character_features'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	head_id = db.Column(db.Integer, db.ForeignKey('headquarters.id'))
	feature = db.Column(db.Integer, db.ForeignKey('headquarters_features.id'))
	def format(self):
		return {
			'id': self.id,
			'head_id': self.head_id,
			'feature': self.feature
		}


class HeadFeatAddon(db.Model):
	__tablename__ = 'headquarters_feature_addon'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	head_id = db.Column(db.Integer, db.ForeignKey('headquarters.id'))
	head_feature = db.Column(db.Integer, db.ForeignKey('headquarters_features.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	addon = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'head_id': self.head_id,
			'head_feature': self.head_feature,
			'feature': self.feature,
			'equipment': self.equipment,
			'weapon': self.weapon,
			'addon': self.addon
		}
