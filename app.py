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
from models import setup_db, Ability, Defense, Modifier
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

@app.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h2' 
	table = Ability.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/defense')
def defense():

	title = 'Defense'
	size = 'h2'
	table = Defense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/modifiers')
def modifiers():

	title = 'Modifiers'
	
	size = 'h3'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

	@app.route('/defense/create')
def defense_create():

	defenses = []

	defenses.append({'name': 'Dodge',
						'ability_id': 3,
						'description': 'Dodge defense is based on Agility rank. It includes reaction time, quickness, nimbleness, and overall coordination, used to avoid ranged attacks or other hazards where reflexes and speed are important.'})
	defenses.append({'name': 'Fortitude',
						'ability_id': 2,
						'description': 'Fortitude defense is based on Stamina and measures health and resistance to threats like poison or disease. It incorporates constitution, ruggedness, metabolism, and immunity.'})
	defenses.append({'name': 'Parry',
						'ability_id': 5,
						'description': 'Parry defense is based on Fighting. It is the ability to counter, duck, or otherwise evade a foe’s attempts to strike you in close combat through superior fighting ability.'})
	defenses.append({'name': 'Toughness',
						'ability_id': 2,
						'description': 'Toughness defense is based on Stamina and is resistance to direct damage or harm, and overall durability.'})
	defenses.append({'name': 'Will',
						'ability_id': 7,
						'description': 'Will defense is based on Awareness rank. It measures mental stability, level-headedness, determination, selfconfidence, self-awareness, and willpower, and is used to resist mental or spiritual attacks.'})				

	for defense in defenses:
		name = defense['name']
		ability_id = defense['ability_id']
		description = defense['description']
		modifier_id = 4

		entry = Defense(name=name, ability_id=ability_id, description=description, modifier_id=modifier_id)
		db.session.add(entry)
		db.session.commit()

	additions = Defense.query.all()
	for addition in additions:
		defense_id = addition.id
		name = addition.name
		ability_id = addition.ability_id
		description = addition.description
		modifier = addition.modifier_id

		print (defense_id)
		print (name)
		print (ability_id)
		print (description)
		print (modifier)

	return ('defense')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)