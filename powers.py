from flask import Blueprint
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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

powers = Blueprint('powers', __name__)
db = SQLAlchemy()

stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}, {"style": "/static/css/font-awesome.min.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplqying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

@powers.route('/power/create')
def power_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'power_create.html'

	title = 'DC Adventures Online Roleplqying Game: Create Power'
	stylesheets.append({"style": "/static/css/power_create.css"})

	power_includes = {'base_form': 'power_create/base_form.html', 'range': 'power_create/range.html'}
	
	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	positives = []
	for i in range(1, 41, 1):
		positives.append(i)

	power_type = [{'type': 'attack', 'name': 'Attack'}, 
					{'type': 'move', 'name': 'Movement'},  
					{'type': 'sense', 'name': 'Sensory'},
					{'type': 'control', 'name': 'Control'}, 
					{'type': 'defense', 'name': 'Defense'}, 
					{'type': 'general', 'name': 'General'}]

	action_type = [{'type': 'standard', 'name': 'Standard Action'},
					{'type': 'move', 'name': 'Move Action'},
					{'type': 'free', 'name': 'Free Action'},
					{'type': 'reaction', 'name': 'Reaction'},
					{'type': 'none', 'name': 'None'}]

	range_type = [{'type': 'personal', 'name': 'Personal'}, 
					{'type': 'close', 'name': 'Close'}, 
					{'type': 'ranged', 'name': 'Ranged'}, 
					{'type': 'perception', 'name': 'Perception'}, 
					{'type': 'rank', 'name': 'Rank Table'}]

	duration_type = [{'type': 'instant', 'name': 'Instant'}, 
						{'type': 'conc', 'name': 'Concentration'}, 
						{'type': 'sustained', 'name': 'Sustained'},
						{'type': 'cont', 'name': 'Continuous'},
						{'type': 'perm', 'name': 'Permanent'}]

	dc_type = [{'type': None, 'name': 'None'}, {'type': 'gm', 'name': 'Set By GM'}, {'type': 'rank', 'name': 'Power Rank'}, {'type': 'mod', 'name': 'Rank + Modifier'}, {'type': 'table', 'name': 'DC Table'}]

	distance = db.session.query(Unit).filter_by(type_id=3)

	return render_template('template.html', dc_type=dc_type, distance=distance, negatives=negatives, positives=positives, power_type=power_type, action_type=action_type, range_type=range_type, duration_type=duration_type, power_includes=power_includes, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar, includehtml=includehtml, title=title)