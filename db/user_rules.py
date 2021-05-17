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


class Nature(db.Model):
	__tablename__ = 'nature'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show
		}



class Emotion(db.Model):
	__tablename__ = 'emotions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show
		}

class Environment(db.Model):
	__tablename__ = 'environments'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	outdoors = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show,
			'outdoors': self.outdoora
		}

class Job(db.Model):
	__tablename__ = 'jobs'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show
		}
		
class Organization(db.Model):
	__tablename__ = 'organizations'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show
		}

class Creature(db.Model):
	__tablename__ = 'creature'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	machine = db.Column(db.Boolean)
	human = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show,
			'machine': self.machine,
			'human': self.human
		}	

class NarrowCreature(db.Model):
	__tablename__ = 'creature_narrow'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	creature = db.Column(db.Integer, db.ForeignKey('creature.id'))
	name = db.Column(db.String())
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	hide = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	show = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'creature': self.creature,
			'name': self.name,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'hide': self.hide,
			'approved': self.approved,
			'show': self.show
		}	

