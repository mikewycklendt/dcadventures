import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from datetime import datetime
from models import setup_db, Ability
import sys

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc'
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
	stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}]
	includehtml = 'home.html'
	title = 'DC Adventures Online Roleplqying Game'
	stylesheets.append({"style": "/static/css/home.css"})
	meta_name="DC Adventures Online"
	meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content)

@app.route('/defense/create')
def defense_create():

	defenses = []

@app.route('/absent')
def absent():

	absent = []

	absent.append({'id': 1, 'value': 'A creature with no Strength is incapable of exerting any physical force, either because it has no physical form (like an incorporeal ghost) or simply can’t move (like a tree).'})
	absent.append({'id': 2, 'value': 'A creature with no Stamina has no physical body (like a ghost) or is not a living being (such as a robot or other construct). Creatures with no Stamina suffer and recover from damage like inanimate ob-jects (see Damaging Objects under the Damage effect). They are immune to fatigued and exhausted conditions, but cannot exert extra effort. Creatures with no Stamina are often—but not necessarily—immune to many of the other things affecting living beings as well (see the Immunity effect in the Powers chapter). They have no Fortitude defense.'})
	absent.append({'id': 3, 'value': 'A creature with no Agility is unable to move its body under its own power and has no Dodge defense.'})
	absent.append({'id': 4, 'value': 'A creature with no Dexterity cannot manipulate objects and hence cannot make physical attacks.'})
	absent.append({'id': 5, 'value': 'A creature with no Fighting is incapable of making any sort of close attack (but may still be able to launch ranged attacks, if it has Dexterity).'})
	absent.append({'id': 6, 'value': 'A creature with no Intellect is an automaton, lacking free will and operating entirely on simple instinct or pre-programmed instructions. Anything with no Intellect is immune to mental effects and interaction skills and has no Will defense.'})
	absent.append({'id': 7, 'value': 'Anything with no Awareness is completely unaware and also has no Presence. It is an inanimate object, not a creature. Objects are immune to mental effects and interaction skills, and have no defenses apart from Toughness (and Fortitude, if they are alive).'})
	absent.append({'id': 8, 'value': 'Creatures without Presence are unable to interact and are immune to interaction skills. They have no Will defense.'})

	for entry in absent:
		print (entry['id'])
		print (entry['value'])
		ability_id = entry['id']
		value = entry['value']
		'''
		ability = Ability.query.filter_by(id=ability_id).one()
		ability.absent = value
		db.session.commit()
		'''
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)