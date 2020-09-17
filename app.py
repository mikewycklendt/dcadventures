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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys

from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs"]

@app.route('/')
def index(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, title=title):
	includehtml = 'home.html'
	title = 'DC Adventures Online: Create a Special Skill'
	stylesheets.append({"style": "/static/css/home.css"})

	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)

@app.route('/skill/create')
def skill_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'special_skill_create.html'
	
	skill_includes = {'base_form': 'special_skill_create/base_form.html','dc_table': 'special_skill_create/dc_table.html', 'levels': 'special_skill_create/levels.html', 'circumstance': 'special_skill_create/circumstance_table.html', 'degree': 'special_skill_create/degree_table.html', 'degree_mod': 'special_skill_create/degree_mod.html', 'movement': 'special_skill_create/movement.html'}

	title = 'DC Adventures Online Roleplqying Game: Create Special Skill'
	stylesheets.append({"style": "/static/css/special_skill_create.css"})

	skills = Skill.query.all()

	checks = Check.query.all()

	conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']

	actions = Action.query.all()

	skilltype = SkillType.query.all()

	dctype = [{"value": "gm", "name": "Set by GM"}, {"value": "table", "name": "DC Table"}]

	level_target = ['Active Player', 'Other Player']

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	char_rank = db.session.query(Rank).filter_by(rank_type='char')

	deg_mod_type = ['damage', 'measure', 'condition']
	
	numbers = []
	for i in range(-20, 21, 1):
		numbers.append(i)

	dcclasses = []
	for i in range(0, 41, 1):
		dcclasses.append(i)

	dc_rank = ['This Skill', 'Parent Skill', 'Parent Ability', 'Defense', 'Distance Rank', 'Speed Rank', 'Time Rank', 'Throwing Rank', 'Opponent Skill', 'Opponent Power', 'Opponent Ability', 'Opponent Advantage', 'Opponent Equipment', 'Opponent Weapon', 'Opponent Defense', 'Opponent Device', 'Opponent Construct', 'Opponent Speed', 'Opponent Throwing']

	maths = Math.query.all()

	value_type =['value', 'math']

	defenses = Defense.query.all()

	units = Unit.query.all()

	ranks = Rank.query.all()

	return render_template('template.html', char_rank=char_rank, combined_conditions=combined_conditions, ranks=ranks, deg_mod_type=deg_mod_type, measure_rank=measure_rank, level_target=level_target, skill_includes=skill_includes, units=units, defenses=defenses, value_type=value_type, maths=maths, dc_rank=dc_rank, dcclasses=dcclasses, dctype=dctype, skilltype=skilltype, actions=actions, conditions=conditions, checks=checks, numbers=numbers, skills=skills, includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)

@app.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h1' 
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
	
	size = 'h1'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skills')
def skills():

	title = 'Skills'
	
	size = 'h1'

	table = Skill.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skill/type')
def skill_type():

	title = 'Skill Type'
	
	size = 'h1'

	table = SkillType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/checks')
def checks():

	title = 'Check Types'
	
	size = 'h1'

	table = Check.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/conditions')
def conditions():

	title = 'Basic Conditions'
	
	size = 'h1'

	table = Condition.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/phases')
def phases():

	title = 'Phases'
	
	size = 'h1'

	table = Phase.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/senses')
def senses():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measuretype')
def measurement_type():

	title = 'Measurement Type'
	
	size = 'h1'

	table = MeasureType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/units')
def unit_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Unit.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/ranks')
def rank_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Rank.query.all()

	return render_template('ranks.html', table=table, title=title, size=size)


@app.route('/math')
def math_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Math.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measurements')
def measurements():

	title = 'Measurements Table'
	
	size = 'h3'

	measurements = Measurement.query.all()

	formatted = [measurement.format() for measurement in measurements]
	
	print (formatted)

	table = measure(formatted)

	return render_template('measurements.html', table=table, title=title, size=size)






'''
@app.route('/debilitated/create')
def debilitated_create():

	entries = []

	entries.append({
		'name': 'Debilitated ',
		'effects': 
		'condition_id': 
		'actions':
		'controlled':
		'ability_id': 
		})
'''


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)