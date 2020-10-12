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
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck 
from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

skills = Blueprint('skills', __name__)

@app.route('/skill/create')
def skill_create(stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar):
	includehtml = 'special_skill_create.html'
	
	skill_includes = {'base_form': 'special_skill_create/base_form.html','dc_table': 'special_skill_create/dc_table.html', 'levels': 'special_skill_create/levels.html', 'circumstance': 'special_skill_create/circumstance_table.html', 'degree': 'special_skill_create/degree_table.html', 'degree_mod': 'special_skill_create/degree_mod.html', 'movement': 'special_skill_create/movement.html', 'power': 'special_skill_create/power.html', 'rounds': 'special_skill_create/rounds.html', 'subskill': 'special_skill_create/subskill.html', 'action': 'special_skill_create/change_action.html', 'resistance': 'special_skill_create/resistance.html', 'opponent_condition': 'special_skill_create/opponent_condition.html', 'other_char': 'special_skill_create/other_char.html', 'other_checks': 'special_skill_create/other_checks.html', 'resist': 'special_skill_create/resist.html', 'opposed': 'special_skill_create/opposed.html', 'alt_check': 'special_skill_create/alt_check.html', 'pre_check': 'special_skill_create/pre_check.html'}

	title = 'DC Adventures Online Roleplqying Game: Create Special Skill'
	stylesheets.append({"style": "/static/css/special_skill_create.css"})

	skills = Skill.query.all()

	abilities = Ability.query.all()

	opposed_raw = []

	for skill in skills:
		opposed_raw.append(skill.name)

	for ability in abilities:
		opposed_raw.append(ability.name)

	opposed = sorted(opposed_raw)

	checks = Check.query.all()

	base_conditions = Condition.query.all()

	combined_conditions = ['Normal', 'Standing', 'Asleep', 'Blind', 'Bound', 'Deaf', 'Dying', 'Entranced', 'Exhausted', 'Incapactated', 'Paralyzed', 'Prone', 'Restrained', 'Staggered', 'Surprised']

	conditions_raw = []

	for condition in base_conditions:
		conditions_raw.append(condition.name)

	for condition in combined_conditions:
		conditions_raw.append(condition)

	conditions = sorted(conditions_raw)
	
	actions = Action.query.all()

	skilltype = SkillType.query.all()

	times = db.session.query(Unit).filter_by(type_id=2).all()

	dctype = [{"value": "gm", "name": "Set by GM"}, {"value": "table", "name": "DC Table"}]

	level_target = ['Active Player', 'Other Player', 'GM Controlled']

	targets = ['Other Player', 'GM Controlled']

	measure_rank = db.session.query(Rank).filter_by(rank_type='measure')

	char_rank = db.session.query(Rank).filter_by(rank_type='char')

	deg_mod_type = ['damage', 'measure', 'condition']

	opposed_by = [{'id': 'rank_high', 'name': 'Highest Rank'}, {'id': 'bonus_high', 'name': 'Highest Bonus'}, {'id': 'rank_low', 'name': 'Lowest Rank'}, {'id': 'bonus_low', 'name': 'Lowest Bonus'}, {'id': 'gm', 'name': "GM's Choice"}]
	
	numbers = []
	for i in range(-20, 21, 1):
		numbers.append(i)

	negatives = []
	for i in range(-20, 1, 1):
		negatives.append(i)

	dcclasses = []
	for i in range(0, 41, 1):
		dcclasses.append(i)

	dc_rank = []

	char = [rank.format() for rank in char_rank]

	measure = [rank.format() for  rank in measure_rank]

	maths = Math.query.all()

	value_type =['value', 'math']

	defenses = Defense.query.all()

	units = Unit.query.all()

	ranks = Rank.query.all()

	results = ['success', 'failure']

	powers_raw =['Affliction', 'Alternate Form', 'Burrowing', 'Communication', 'Comprehend', 'Concealment', 'Create', 'Damage', 'Deflect', 'Elongation', 'Enhanced Trait', 'Environment', 'Extra Limbs', 'Feature', 'Flight', 'Growth', 'Healing', 'Illusion', 'Immortality', 'Immunity', 'Insubstantial', 'Leaping', 'Luck Control', 'Mind Reading', 'Morph', 'Move Object', 'Movement', 'Dimension Travel', 'Environmental Adaptation', 'Permeate', 'Safe Fall', 'Slithering', 'Space Travel', 'Sure-Footed', 'Swinging', 'Time Travel', 'Trackless', 'Wall-Crawling', 'Water-Walking', 'Nullify', 'Protection', 'Quickness', 'Regeneration', 'Remote Sensing', 'Senses', 'Accurate Sense', 'Acute Sense', 'Analytical Sense', 'Awareness Sense', 'Communication Link', 'Counters Concealment', 'Counters Illusion', 'Danger Sense', 'Darkvision Sense', 'Detect Sense', 'Direction Sense', 'Distance Sense', 'Extended Sense', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Penetrates Concealment', 'Postcognition', 'Precognition', 'Radio', 'Radius', 'Radius', 'Ranged Sense', 'Rapid Sense', 'Time Sense', 'Tracking Sense', 'Ultra-Hearing', 'Ultra-Vision', 'Snare', 'Strike', 'Suffocation', 'Shrinking', 'Speed', 'Summon', 'Swimming', 'Teleport', 'Transform', 'Destructive Transformation', 'Transforming Beings', 'Variable', 'Weaken', 'Cold', 'Heat', 'Impede Movement', 'Light', 'Visibility', 'Strength and Damage', 'Strength-Based Damage', 'Damaging Objects', 'Dazzle', 'Duplication', 'Element Control', 'Energy Absorption', 'Created Objects, Cover and Concealment', 'Trapping with Objects', 'Dropping Objects', 'Supporting Weight', 'Comprehend Animals', 'Comprehend Languages', 'Comprehend Machines', 'Comprehend Objects', 'Comprehend Plants', 'Comprehend Spirits', 'Blast']

	powers = sorted(powers_raw)

	resists_raw = []

	for oppose in opposed:
		resists_raw.append(oppose)

	for power in powers:
		resists_raw.append(power)

	resists = sorted(resists_raw)

	skills_abilities_raw = []

	whens = ['before', 'after']

	checks_two = [{'id': 'skill', 'name': 'Skill Check'}, {'id': 'opposed', 'name': 'Opposed Check'}]

	for skill in skills:
		skills_abilities_raw.append(skill.name)

	for ability in abilities:
		skills_abilities_raw.append(ability.name)

	skills_abilities = sorted(skills_abilities_raw)

	level_type = [{'id': 1, 'name': 'Attitude'}]
	levels = [{'id': 1, 'name': 'Hostile'}, {'id': 1, 'name': 'Unfavorable'}, {'id': 1, 'name': 'Indifferent'}, {'id': 1, 'name': 'Favorable'}, {'id': 1, 'name': 'Helpful'}]

	return render_template('template.html', targets=targets, checks_two=checks_two, whens=whens, skills_abilities=skills_abilities, level_type=level_type, levels=levels, opposed_by=opposed_by, resists=resists, negatives=negatives, times=times, opposed=opposed, results=results, powers=powers, char_rank=char_rank, combined_conditions=combined_conditions, ranks=ranks, deg_mod_type=deg_mod_type, measure_rank=measure_rank, level_target=level_target, skill_includes=skill_includes, units=units, defenses=defenses, value_type=value_type, maths=maths, dc_rank=dc_rank, dcclasses=dcclasses, dctype=dctype, skilltype=skilltype, actions=actions, conditions=conditions, checks=checks, numbers=numbers, skills=skills, includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content, sidebar=sidebar)
