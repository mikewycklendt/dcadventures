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
			'feature': self.feature
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


