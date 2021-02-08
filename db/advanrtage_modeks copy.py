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


class Advantage(db.Model):
	
	trait = db.Column(db.Integer)

	replaced_trait =  db.Column(db.Integer)
	
	skill = db.Column(db.Integer)
	
	invent_trait = db.Column(db.Integer)
	
	gm_trait = db.Column(db.Integer)



	
	
	

class AdvAltCheck(db.Model):

	trait = db.Column(db.Integer)



class AdvCirc(db.Model):

	check_trait = db.Column(db.Integer)

	null_trait = db.Column(db.Integer)

	null_override_trait = db.Column(db.Integer)


	
			'null_trait': self.null_trait,

			'null_override_trait': self.null_override_trait


class AdvDC(db.Model):

	math_trait = db.Column(db.Integer)

	check_trait = db.Column(db.Integer)



			'math_trait': self.math_trait,

			'check_trait': self.check_trait,


class AdvDegree(db.Model):
	
	consequence_trait = db.Column(db.Integer)

	circ_trait = db.Column(db.Integer)

	measure_trait = db.Column(db.Integer)


class AdvMinion(db.Model):

	attitude_trait = db.Column(db.Integer)


class AdvMod(db.Model):
	
	bonus_trait = db.Column(db.Integer)

	penalty_trait = db.Column(db.Integer)


class AdvOpposed(db.Model):

	trait = db.Column(db.Integer)

	opponent_trait = db.Column(db.Integer)



class AdvPoints(db.Model):

	ranks_trait = db.Column(db.Integer)

			'ranks_trait': self.ranks_trait


class AdvResist(db.Model):

	trait = db.Column(db.Integer)


class AdvRounds(db.Model):

	trait = db.Column(db.Integer)



class AdvSkill(db.Model):

	trait = db.Column(db.Integer)

	replaced_trait = db.Column(db.Integer)



class AdvTime(db.Model):

	trait = db.Column(db.Integer)

class AdvVariable(db.Model):


	trait = db.Column(db.Integer)

