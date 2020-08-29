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
from db import *
import sys

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc'
db = SQLAlchemy(app)

@app.route('/')
def index():
	stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}]
	includehtml = 'home.html'
	title = 'DC Adventures Online Roleplqying Game'
	stylesheets.append({"style": "/static/css/home.css"})
	meta_name="DC Adventures Online"
	meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content)

@app.route('/abilities/create', methods=['POST'])
def abilities_create():
	abilities = [{"name": "Strength",
					"description": ['Damage dealt by your unarmed and strength-based attacks.',
									'How far you can jump.',
									'The amount of weight you can lift, carry, and throw.',
									'Athletics skill checks.'],
					"summary": 'Strength measures sheer muscle power and the ability to apply it. Your Strength rank applies to:'}, 
					{"name": "Stamina",
					"description": ['Toughness defense, for resisting damage.',
									'Fortitude defense, for resisting effects targeting your character’s health.',
									'Stamina checks to resist or recover from things af-fecting your character’s health when a specific de-fense doesn’t apply.'],
					"summary": 'Stamina is health, endurance, and overall physical resil-ience. Stamina is important because it affects a charac-ter’s ability to resist most forms of damage. Your Stamina modifier applies to:'},
					{"name": "Agility",
					"description": ['Dodge defense, for avoiding ranged attacks and oth-er hazards.',
									'Initiative bonus, for acting first in combat.',
									'Acrobatics and Stealth skill checks.',
									'Agility checks for feats of coordination, gross move-ment, and quickness when a specific skill doesn’t apply.'],
					"summary": 'Agility is balance, grace, speed, and overall physical coor-dination. Your Agility rank applies to:'}, 
					{"name": "Dexterity",
					"description": ['Attack checks for ranged attacks.',
									'Sleight of Hand and Vehicles skill checks.',
									'Dexterity checks for feats of fine control and preci-sion when a specific skill doesn’t apply.'],
					"summary": 'Dexterity is a measure of hand-eye coordination, precision, and manual dexterity. Your Dexterity rank applies to:'}, 
					{"name": "Fighting",
					"description": ['Attack checks for close attacks.',
									'Parry defense, for avoiding close attacks'],
					"summary": 'Fighting measures your character’s ability in close com-bat, from hitting a target to ducking and weaving around any counter-attacks. Your Fighting rank applies to:'}, 
					{"name": "Intellect",
					"description": ['Expertise, Investigation, Technology, and Treatment skill checks.',
									'Intellect checks to solve problems using sheer brain-power when a specific skill doesn’t apply.'],
					"summary": 'Intellect covers reasoning ability and learning. A character with a high Intellect rank tends to be knowledgeable and well educated. Your Intellect modifier applies to:'}, 
					{"name": "Awareness",
					"description": ['Will defense, for resisting attacks on your mind.',
									'Insight and Perception skill checks.',
									'Awareness checks to resolve matters of intuition when a specific skill doesn’t apply.'],
					"summary": 'While Intellect covers reasoning, Awareness describes common sense and intuition, what some might call “wis-dom.” A character with a high Intellect and a low Aware-ness may be an “absent-minded professor” type, smart but not always aware of what’s going on. On the other hand, a not so bright (low Intellect) character may have a great deal of common sense (high Awareness). Your Awareness modifier applies to:'},
					{"name": "Presence",
					"description": ['Deception, Intimidation, and Persuasion skill checks.',
									'Presence checks to influence others through force of personality when a specific skill doesn’t apply.'],
					"summary": 'Presence is force of personality, persuasiveness, leader-ship ability and (to a lesser degree) attractiveness. Pres-ence is useful for heroes who intend to be leaders as well as those who strike fear into the hearts of criminals with their presence. Your Presence modifier applies to:'}]
	print (abilities)

	for ability in abilities:
		print(ability)
		name = ability.name
		description = ability.description
		summary = ability.summary
		newEntry = Ability(name=name, description=description, summary=summary)
		db.session.add(newEntry)
		db.session.commit()

	return redirect(url_for('venues_results'))

@app.route('/venues/results')
def venues_results():
	abilities = Ability.query.all()
	data = [ability.format() for ability in abilities]

	print (data)

	return 'results'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)