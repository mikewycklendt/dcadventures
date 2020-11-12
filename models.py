from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv

load_dotenv()

import os


db_path = os.environ.get("db_path")

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = db_path
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
db = SQLAlchemy()

def setup_db(app):
	database_path = db_path
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

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'summary': self.summary,
			'absent': self.absent,
			'modifier_id': self.modifier_id
		}

class Defense(db.Model):
	__tablename__ = 'defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	description = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'ability_id': self.ability_id,
			'modifier_id': self.modifier_id
		}

class Modifier(db.Model):
	__tablename__ = 'modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Integer())
	description = db.Column(db.String())
	table = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cost': self.cost,
			'description': self.description,
			'table': self.table
		}

class ModifierTable(db.Model):
	__tablename__ = 'modifiers_table'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	description = db.Column(db.String())
	value = db.Column(db.Integer())
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))

	def format(self):
		return {
			'id': self.id,
			'description': self.description,
			'value': self.value,
			'modifier_id': self.modifier_id
		}

class Action(db.Model):
	__tablename__ = 'actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cost = db.Column(db.Boolean)
	turn = db.Column(db.Boolean)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cost': self.cost,
			'turn': self.turn,
			'description': self.description
		}

class Skill(db.Model):
	__tablename__ = 'skills'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	untrained = db.Column(db.Boolean)
	tools = db.Column(db.Boolean)
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))
	description = db.Column(db.String())
	table = db.Column(db.Boolean)

	def format(self):
		return {
			'id':  self.id,
			'name': self.name,
			'ability_id': self.ability_id,
			'untrained': self.untrained,
			'tools': self.tools,
			'check_id': self.check_id,
			'action_id': self.action_id,
			'description': self.description,
			'table': self.table
		}

class SkillTable(db.Model):
	__tablename__ = 'skill_tables'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	dc = db.Column(db.Integer)
	description = db.Column(db.String())
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	modifier_id = db.Column(db.Integer, db.ForeignKey('modifiers.id'))
	degree = db.Column(db.Boolean)
	measurement  = db.Column(db.Integer)
	complexity = db.Column(db.String())
	modifier = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	requires_sub = db.Column(db.Boolean)


	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id,
			'dc': self.dc,
			'description': self.description,
			'check_id': self.check_id,
			'modifier_id': self.modifier_id,
			'degree': self.degree,
			'measurement': self.measurement,
			'complexity': self.complexity,
			'modifier': self.modifier,
			'circumstance': self.circumstance,
			'requires_sub': self.requires_sub
		}

class SkillType(db.Model):
	__tablename__ = 'skill_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	group = db.Column(db.Boolean)
	team = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'check_id': self.check_id,
			'group': self.group,
			'team': self.team,
			'gm': self.gm,
			'description': self.description
		}

class SkillBonus(db.Model):
	__tablename__ = 'skill_bonus'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	description = db.Column(db.String())
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	condition = db.Column(db.String())
	speed_mod = db.Column(db.Integer)
	skill_type = db.Column(db.Integer, db.ForeignKey('skill_type.id'))
	dc_set = db.Column(db.String())
	time_type = db.Column(db.String())
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))	
	time_mod = db.Column(db.Integer)
	time_val = db.Column(db.Integer)
	time_val_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	sub_check = db.Column(db.Boolean)
	cover_check = db.Column(db.Boolean)
	materials_check = db.Column(db.Boolean)
	hidden_check = db.Column(db.Boolean)
	hidden_mod = db.Column(db.Integer)
	untrained_check = db.Column(db.Boolean)
	untrained_limit = db.Column(db.Integer)
	untrained_mod = db.Column(db.Integer)
	level_type = db.Column(db.String())
	level_change = db.Column(db.String())
	subskill = db.Column(db.String())
	subskill_description = db.Column(db.String())
	move_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	move_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	move_val = db.Column(db.Integer)
	action_change = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action_mod = db.Column(db.Integer)
	public = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	other = db.Column(db.Boolean)
	other_check = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	round = db.Column(db.Boolean)
	power = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	circ_mod = db.Column(db.Boolean)
	degree_key = db.Column(db.Boolean)
	degree_mod = db.Column(db.Boolean)
	resist_check = db.Column(db.Boolean)
	resist_effect = db.Column(db.Boolean)
	opp_condition = db.Column(db.Boolean)
	char_check = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'skill_id': self.skill_id,
			'description': self.description,
			'action': self.action,
			'check_id': self.check_id,
			'condition': self.condition,
			'speed_mod': self.speed_mod,
			'skill_type': self.skill_type,
			'dc_set': self.dc_set,
			'time_type': self.time_type,
			'time_unit': self.time_unit,
			'time_rank': self.time_rank,
			'time_mod': self.time_mod,
			'time_val': self.time_val,
			'time_val_unit': self.time_val_unit,
			'sub_check': self.sub_check,
			'cover_check': self.cover_check,
			'materials_check': self.materials_check,
			'hidden_check': self.hidden_check,
			'hidden_mod': self.hidden_mod,
			'untrained_check': self.untrained_check,
			'untrained_limit': self.untrained_limit,
			'untrained_mod': self.untrained_mod,
			'level_type': self.level_type,
			'level_change': self.level_change,
			'subskill': self.subskill,
			'subskill_description': self.subskill_description,
			'move_rank': self.move_rank,
			'move_math': self.move_math,
			'move_val': self.move_val,
			'action_change': self.action_change,
			'action_mod': self.action_mod,
			'public': self.public,
			'approved': self.approved,
			'other': self.other,
			'other_check': self.other_check,
			'opposed': self.opposed,
			'round': self.round,
			'power': self.power,
			'levels': self.levels,
			'circ_mod': self.circ_mod,
			'degree_key': self.degree_key,
			'degree_mod': self.degree_mod,
			'resist_check': self.resist_check,
			'resist_effect': self.resist_effect,
			'opp_condition': self.opp_condition,
			'char_check': self.char_check
		}

class SkillOther(db.Model):
	__tablename__ = 'skill_other'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'skill_id': self.skill_id,
			'description': self.description
		}

class SkillOtherCheck(db.Model):
	__tablename__ = 'skill_other_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.String())
	when = db.Column(db.String())
	check = db.Column(db.String())
	opposed_check = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'check_type': self.check_type,
			'when': self.when,
			'check': self.check,
			'opposed_check': self.opposed_check,
			'description': self.description
		}

class SkillOpposed(db.Model):
	__tablename__ = 'skill_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	priority = db.Column(db.String())
	opposed = db.Column(db.String())
	mod = db.Column(db.Integer)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'priority': self.priority,
			'opposed': self.opposed,
			'mod': self.mod,
			'description': self.description
		}

class SkillRound(db.Model):
	__tablename__ = 'skill_round'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	dc = db.Column(db.Integer)
	degree = db.Column(db.Integer)
	rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'dc': self.dc,
			'degree': self.degree,
			'rank': self.rank,
			'mod': self.mod,
			'rounds': self.rounds
		}

class SkillPower(db.Model):
	__tablename__ = 'skill_power'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	power = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'power': self.power,
			'description': self.description
		}

class SkillDC(db.Model):
	__tablename__ = 'skill_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	type = db.Column(db.String())
	val = db.Column(db.Integer)
	math_val = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_type = db.Column(db.String())
	measure_val = db.Column(db.Integer)
	measure_val_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_math_val = db.Column(db.Integer)
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	damage = db.Column(db.Integer)
	keyword = db.Column(db.String())
	condition_one = db.Column(db.String())
	condition_two = db.Column(db.String())
	defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	description = db.Column(db.String())


	def format(self):
		return {	
			'id': self.id,
			'bonus_id': self.bonus_id,
			'type': self.type,
			'val': self.val,
			'math_val': self.math_val,
			'math': self.math,
			'math_rank': self.math_rank,
			'measure_type': self.measure_type,
			'measure_val': self.measure_val,
			'measure_val_unit': self.measure_val_unit,
			'measure_math_val': self.measure_math_val,
			'measure_math': self.measure_math,
			'measure_rank': self.measure_rank,
			'damage': self.damage,
			'keyword': self.keyword,
			'condition_one': self.condition_one,
			'condition_two': self.condition_two,
			'defense': self.defense,
			'action': self.action,
			'description': self.description
		}

class SkillLevels(db.Model):
	__tablename__ = 'skill_levels'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	type = db.Column(db.String())
	target = db.Column(db.String())
	degree = db.Column(db.Integer) 
	keyword = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'type': self.type,
			'target': self.target,
			'degree': self.degree,
			'keyword': self.keyword,
			'description': self.description
		}

class SkillLevelsType(db.Model):
	__tablename__ = 'skill_levels_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'type': self.type
		}

class SkillCircMod(db.Model):
	__tablename__ = 'skill_circ_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	target = db.Column(db.String())
	type = db.Column(db.String())
	mod = db.Column(db.Integer)
	unit_mod = db.Column(db.Integer)
	unit_value = db.Column(db.Integer)
	unit_type = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	adjust_check_mod = db.Column(db.Integer)
	adjust_mod = db.Column(db.Integer)
	adjust_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	equip_mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'skill': self.skill,
			'target': self.target,
			'type': self.type,
			'mod': self.mod,
			'unit_mod': self.unit_mod,
			'unit_value': self.unit_value,
			'unit_type': self.unit_type,
			'adjust_check_mod': self.adjust_check_mod,
			'adjust_mod': self.adjust_mod,
			'adjust_rank': self.adjust_rank,
			'equip_mod': self.equip_mod,
			'rounds': self.rounds,
			'description': self.description
		}


class SkillDegreeKey(db.Model):
	__tablename__ = 'skill_degree_key'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
	target = db.Column(db.String())
	degree = db.Column(db.Integer)
	keyword = db.Column(db.String())
	description = db.Column(db.String())
	type = db.Column(db.String())
	

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'skill_id': self.skill_id,
			'target': self.target,
			'degree': self.degree,
			'keyword': self.keyword,
			'description': self.description,
			'type': self.type			
		}

class SkillDegreeType(db.Model):
	__tablename__ = 'skill_degree_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	type = db.Column(db.String())
	

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'type': self.type			
		}

class SkillDegreeMod(db.Model):
	__tablename__ = 'skill_degree_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	target = db.Column(db.String())
	degree = db.Column(db.Integer)
	type = db.Column(db.String())
	damage_value_degree = db.Column(db.Integer)
	damage_value_value = db.Column(db.Integer)
	damage_math_damage = db.Column(db.Integer)
	damage_math_math1 = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_math_value = db.Column(db.Integer)
	damage_math_math2 = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_value = db.Column(db.Integer)
	measure_value_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_math_value = db.Column(db.Integer)
	measure_math_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	measure_math_measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition_1 = db.Column(db.String())
	condition_2 = db.Column(db.String())
	keyword = db.Column(db.String())
	description = db.Column(db.String())
	nullify = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'target': self.target,
			'degree': self.degree,
			'type': self.type,
			'damage_value_degree': self.damage_value_degree,
			'damage_value_value': self.damage_value_value,
			'damage_math_damage': self.damage_math_damage,
			'damage_math_math1': self.damage_math_math1,
			'damage_math_value': self.damage_math_value,
			'damage_math_math2': self.damage_math_math2,
			'damage_math_rank': self.damage_math_rank,
			'measure_value': self.measure_value,
			'measure_value_rank': self.measure_value_rank,
			'measure_math_value': self.measure_math_value,
			'measure_math_math': self.measure_math_math,
			'measure_math_rank': self.measure_math_rank,
			'measure_math_measure_rank': self.measure_math_measure_rank,
			'condition_1': self.condition_1,
			'condition_2': self.condition_2,
			'keyword': self.keyword,
			'description': self.description,
			'nullify': self.nullify
		}

class SkillResistCheck(db.Model):
	__tablename__ = 'skill_resist_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	target = db.Column(db.String())
	mod = db.Column(db.Integer)
	description = db.Column(db.String())


	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'target': self.target,
			'mod': self.mod,
			'description': self.description
		}

class SkillResistEffect(db.Model):
	__tablename__ = 'skill_resist_effect'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	effect = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'effect': self.effect,
			'description': self.description
		}

class SkillOppCondition(db.Model):
	__tablename__ = 'skill_opp_condition'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	degree = db.Column(db.Integer)
	condition = db.Column(db.String())
	rounds = db.Column(db.Integer)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'degree': self.degree,
			'condition': self.condition,
			'rounds': self.rounds,
			'description': self.description
		}

class SkillCharCheck(db.Model):
	__tablename__ = 'skill_char_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
	target = db.Column(db.String())
	degree = db.Column(db.Integer)
	rank = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'check_id': self.check_id,
			'target': self.target,
			'degree': self.degree,
			'rank': self.rank,
			'description': self.description
		}

class Power(db.Model):
	__tablename__ = 'powers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Extra(db.Model):
	__tablename__ = 'extras'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	name = db.Column(db.String())
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)
	des = db.Column(db.String())
	inherit = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'name': self.name,
			'cost': self.cost,
			'ranks': self.ranks,
			'des': self.des,
			'inherit': self.inherit
		}

class PowerDes(db.Model):
	__tablename__ = 'power_descriptors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())	
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	des_id = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	origin = db.Column(db.Integer, db.ForeignKey('origin.id'))
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	medium = db.Column(db.Integer, db.ForeignKey('medium.id'))
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	result = db.Column(db.String())
	descriptor = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'power_id': self.power_id,
			'des_id': self.des_id,
			'origin': self.origin,
			'source': self.source,
			'medium': self.medium,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'result': self.result,
			'descriptor': self.descriptor
		}

class Descriptor(db.Model):
	__tablename__ = 'descriptors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	origin = db.Column(db.Integer, db.ForeignKey('origin.id'))
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	medium = db.Column(db.Integer, db.ForeignKey('medium.id'))
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	result = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'origin': self.origin,
			'source': self.source,
			'medium': self.medium,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'result': self.result,
			'description': self.description
		}

class Origin(db.Model):
	__tablename__ = 'origin'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}

class Source(db.Model):
	__tablename__ = 'source'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}

class MediumType(db.Model):
	__tablename__ = 'medium_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}

class MediumSubType(db.Model):
	__tablename__ = 'medium_subtype'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'description': self.description
		}

class Medium(db.Model):
	__tablename__ = 'medium'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'description': self.description
		}

class Check(db.Model):
	__tablename__ = 'checks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	critical = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	automatic = db.Column(db.Boolean)
	routine = db.Column(db.Boolean)
	graded = db.Column(db.Boolean)
	roll = db.Column(db.Boolean)
	compare = db.Column(db.Boolean)
	fail = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'critical': self.critical,
			'dc': self.dc,
			'opposed': self.opposed,
			'automatic': self.automatic,
			'routine': self.routine,
			'graded': self.graded,
			'roll': self.roll,
			'compare': self.compare,	
			'fail': self.fail
		}

class Condition(db.Model):
	__tablename__ = 'conditions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	phase = db.Column(db.Integer)
	supercede = db.Column(db.String())
	specific = db.Column(db.Boolean)
	multiple = db.Column(db.Boolean)
	time = db.Column(db.Integer)
	unit = db.Column(db.String())
	effects = db.Column(db.String())
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'phase': self.phase,
			'supercede': self.supercede,
			'specific': self.specific,
			'multiple': self.multiple,
			'time': self.time,
			'unit': self.unit,
			'effects': self.effects,
			'description': self.description
		}

class Phase(db.Model):
	__tablename__ = 'phases'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class MeasureType(db.Model):
	__tablename__ = 'measurement_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Emotion(db.Model):
	__tablename__ = 'emotions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Ground(db.Model):
	__tablename__ = 'ground'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Range(db.Model):
	__tablename__ = 'range'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	distance = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'distance': self.distance
		}

class Unit(db.Model):
	__tablename__ = 'unit_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'type_id': self.type_id
		}

class Material(db.Model):
	__tablename__ = 'materials'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	toughness = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'toughness': self.toughness
		}

class Complex(db.Model):
	__tablename__ = 'complexity'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	dc = db.Column(db.Integer)
	time = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'dc': self.dc,
			'time': self.time
		}

class Sense(db.Model):
	__tablename__ = 'senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class SubSense(db.Model):
	__tablename__ = 'sub_senses'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	sense_id = db.Column(db.Integer, db.ForeignKey('senses.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'sense_id': self.sense_id
		}

class Math(db.Model):
	__tablename__ = 'math'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	symbol = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'symbol': self.symbol
		}

class Rank(db.Model):
	__tablename__ = 'ranks'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	rank_type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'rank_type': self.rank_type
		}

class Measurement(db.Model):
	__tablename__ = 'measurements'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	rank = db.Column(db.Integer)
	mass = db.Column(db.Float(asdecimal=True))
	mass_unit = db.Column(db.String())
	time = db.Column(db.Float(asdecimal=True))
	time_unit =db.Column(db.String())
	distance = db.Column(db.Float(asdecimal=True))
	distance_unit = db.Column(db.String())
	volume = db.Column(db.Float(asdecimal=True))
	volume_unit = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'rank': self.rank,
			'mass': self.mass,
			'mass_unit': self.mass_unit,
			'time': self.time,
			'time_unit': self.time_unit,
			'distance': self.distance,
			'distance_unit': self.distance_unit,
			'volume': self.volume,
			'volume_unit': self.volume_unit
		}

class MassCovert(db.Model):
	__tablename__ = 'mass_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	pound = db.Column(db.Integer)
	tons = db.Column(db.Integer)
	kilotons = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'pound': self.pound,
			'tons': self.tons,
			'kilotons': self.kilotons
		}

class TimeCovert(db.Model):
	__tablename__ = 'time_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	seconds = db.Column(db.Integer)
	minutes = db.Column(db.Integer)
	hours = db.Column(db.Integer)
	days = db.Column(db.Integer)
	weeks = db.Column(db.Integer)
	months = db.Column(db.Integer)
	years = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'seconds': self.seconds,
			'minutes': self.minutes,
			'hours': self.hours,
			'days': self.days,
			'weeks': self.weeks,
			'months': self.months,
			'years': self.years
		}

class DistanceCovert(db.Model):
	__tablename__ = 'distance_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	inches = db.Column(db.Integer)
	feet = db.Column(db.Integer)
	mile = db.Column(db.Integer)
	lightyear = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'inches': self.inches,
			'feet': self.feet,
			'mile': self.mile,
			'lightyear': self.lightyear 
		}

class VolumeCovert(db.Model):
	__tablename__ = 'volume_convert'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cft = db.Column(db.Integer)
	million = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cft': self.cft,
			'million': self.million 
		}

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)