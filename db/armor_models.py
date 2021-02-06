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


class Armor(db.Model):
	__tablename__ = 'armor'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('armor_type.id'))
	cost = db.Column(db.Integer)
	material = db.Column(db.Integer, db.ForeignKey('materials.id'))
	toughness = db.Column(db.Integer)
	active = db.Column(db.Integer)
	subtle = db.Column(db.Boolean)
	perception = db.Column(db.Integer)
	impervious = db.Column(db.Boolean)
	defense = db.Column(db.Boolean)
	descriptor = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'type_id': self.type_id,
			'cost': self.cost,
			'material': self.material,
			'toughness': self.toughness,
			'active': self.active,
			'subtle': self.subtle,
			'perception': self.perception,
			'impervious': self.impervious,
			'defense': self.defense,
			'descriptor': self.descriptor
		}
