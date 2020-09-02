from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc"
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
db = SQLAlchemy()

def setup_db(app):
	database_path = "postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc"
	app.config["SQLALCHEMY_DATABASE_URI"] = database_path
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	db.init_app(app)
	db.create_all()

setup_db(app)
migrate = Migrate(app, db)

class Ability(db.Model):
	__tablename__ = 'abilities'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.ARRAY(db.String))
	summary = db.Column(db.String())
	absent = db.Column(db.String())
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

class Defense(db.Model):
	__tablename__ = 'defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	description = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

class Modifier(db.Model):
	__tablename__ = 'modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Integer())
	description = db.Column(db.String())
	table = db.Column(db.Boolean)

class Action(db.Model):
	__tablename__ = 'actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	description = db.Column(db.String())



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)