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

class ConflictAction(db.Model):
	__tablename__ = 'conflict_actions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'action_id': self.action_id
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
	alt_check = db.Column(db.Boolean)

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
			'char_check': self.char_check,
			'alt_check': self.alt_check
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

class SkillAlt(db.Model):
	__tablename__ = 'skill_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	bonus_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	dc = db.Column(db.Integer)
	description = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'bonus_id': self.bonus_id,
			'dc': self.dc,
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
	measure_check = db.Column(db.Boolean)
	damage_check = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	defense_check = db.Column(db.Boolean)
	condition_check = db.Column(db.Boolean)
	action_check = db.Column(db.Boolean)


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
			'description': self.description,
			'measure_check': self.measure_check,
			'damage_check': self.damage_check,
			'keyword_check': self.keyword_check,
			'defense_check': self.defense_check,
			'condition_check': self.condition_check,
			'action_check': self.action_check
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
	noequip = db.Column(db.Boolean)

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
			'description': self.description,
			'noequip': self.noequip
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

class PowerAltCheck(db.Model):
	__tablename__ = 'power_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	mod = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	when = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'check_type': self.check_type,
			'mod': self.mod,
			'circumstance': self.circumstance,
			'when': self.when,
			'trait_type': self.trait_type,
			'trait': self.trait
		}

class PowerAction(db.Model):
	__tablename__ = 'power_change_action'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	mod = db.Column(db.Integer)
	objects = db.Column(db.Boolean)
	circumstance = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'action': self.action,
			'mod': self.mod,
			'objects': self.objects,
			'circumstance': self.circumstance
		}

class PowerChar(db.Model):
	__tablename__ = 'power_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	value = db.Column(db.Integer)
	increase = db.Column(db.Integer)
	limited = db.Column(db.Boolean)
	reduced = db.Column(db.Boolean)
	limbs = db.Column(db.Boolean)
	carry = db.Column(db.Boolean)
	sustained = db.Column(db.Boolean)
	permanent = db.Column(db.Boolean)
	points = db.Column(db.Boolean)
	appear = db.Column(db.Boolean)
	insubstantial = db.Column(db.Boolean)
	weaken = db.Column(db.Boolean)
	weaken_type = db.Column(db.String())
	weaken_trait_type = db.Column(db.String())
	weaken_trait = db.Column(db.String())
	weaken_broad = db.Column(db.String())
	weaken_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	weaken_simultaneous = db.Column(db.Boolean)
	limited_by = db.Column(db.String())
	limited_other = db.Column(db.String())
	limited_emotion = db.Column(db.String())
	limited_emotion_other = db.Column(db.String())
	reduced_trait_type = db.Column(db.String())
	reduced_trait = db.Column(db.String())
	reduced_value = db.Column(db.Integer)
	reduced_full = db.Column(db.Boolean)
	limbs_continuous = db.Column(db.Boolean)
	limbs_sustained = db.Column(db.Boolean)
	limbs_distracting = db.Column(db.Boolean)
	limbs_projection = db.Column(db.Boolean)
	carry_capacity = db.Column(db.Integer)
	points_value = db.Column(db.Integer)
	points_trait_type = db.Column(db.String())
	points_trait = db.Column(db.String())
	points_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	appear_target = db.Column(db.String())
	appear_description = db.Column(db.String())
	insub_type = db.Column(db.String())
	insub_description = db.Column(db.String())
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'value': self.value,
			'increase': self.increase,
			'limited': self.limited,
			'reduced': self.reduced,
			'limbs': self.limbs,
			'carry': self.carry,
			'sustained': self.sustained,
			'permanent': self.permanent,
			'points': self.points,
			'appear': self.appear,
			'insubstantial': self.insubstantial,
			'weaken': self.weaken,
			'weaken_type': self.weaken_type,
			'weaken_trait_type': self.weaken_trait_type,
			'weaken_trait': self.weaken_trait,
			'weaken_broad': self.weaken_broad,
			'weaken_descriptor': self.weaken_descriptor,
			'weaken_simultaneous': self.weaken_simultaneous,
			'limited_by': self.limited_by,
			'limited_other': self.limited_other,
			'limited_emotion': self.limited_emotion,
			'limited_emotion_other': self.limited_emotion_other,
			'reduced_trait_type': self.reduced_trait_type,
			'reduced_trait': self.reduced_trait,
			'reduced_value': self.reduced_value,
			'reduced_full': self.reduced_full,
			'limbs_continuous': self.limbs_continuous,
			'limbs_sustained': self.limbs_sustained,
			'limbs_distracting': self.limbs_distracting,
			'limbs_projection': self.limbs_projection,
			'carry_capacity': self.carry_capacity,
			'points_value': self.points_value,
			'points_trait_type': self.points_trait_type,
			'points_trait': self.points_trait,
			'points_descriptor': self.points_descriptor,
			'appear_target': self.appear_target,
			'appear_description': self.appear_description,
			'insub_type': self.insub_type,
			'insub_description': self.insub_description,
			'cost': self.cost,
			'ranks': self.ranks
		}

class PowerCirc(db.Model):
	__tablename__ = 'power_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	description = db.Column(db.String())
	circ_type = db.Column(db.String())
	circ_range = db.Column(db.Integer, db.ForeignKey('range.id'))
	check_who = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	null_type = db.Column(db.String())
	null_condition = db.Column(db.String())
	null_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	null_trait_type = db.Column(db.String())
	null_trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'mod': self.mod,
			'rounds': self.rounds,
			'description': self.description,
			'circ_type': self.circ_type,
			'circ_range': self.circ_range,
			'check_who': self.check_who,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'null_type': self.null_type,
			'null_condition': self.null_condition,
			'null_descriptor': self.null_descriptor,
			'null_trait_type': self.null_trait_type,
			'null_trait': self.null_trait
		}

class PowerCreate(db.Model):
	__tablename__ = 'power_create'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	solidity = db.Column(db.String())
	visibility = db.Column(db.String())
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))
	volume = db.Column(db.Integer)
	toughness = db.Column(db.Integer)
	mass = db.Column(db.Integer)
	damageable = db.Column(db.Boolean)
	maintained = db.Column(db.Boolean)
	repairable = db.Column(db.Boolean)
	moveable = db.Column(db.Boolean)
	stationary = db.Column(db.Boolean)
	trap = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	weapon = db.Column(db.Boolean)
	support = db.Column(db.Boolean)
	real = db.Column(db.Boolean)
	cover = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	incoming = db.Column(db.Boolean)
	outgoing = db.Column(db.Boolean)
	transform = db.Column(db.Boolean)
	transform_type = db.Column(db.String())
	transform_start_mass = db.Column(db.Integer)
	transfom_mass = db.Column(db.Integer)
	transform_start_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	transform_end_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	move_player = db.Column(db.String())
	move_player_trait = db.Column(db.String())
	move_opponent_check = db.Column(db.Boolean)
	move_opponent_ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	move_opponent_rank = db.Column(db.Integer)
	trap_type = db.Column(db.String())
	trap_dc = db.Column(db.Integer)
	trap_trait_type = db.Column(db.String())
	trap_trait = db.Column(db.String())
	trap_resist_check = db.Column(db.String())
	trap_resist_trait = db.Column(db.String())
	trap_resist_dc = db.Column(db.Integer)
	trap_escape = db.Column(db.Boolean)
	ranged_type = db.Column(db.String())
	ranged_dc = db.Column(db.Integer)
	ranged_trait_type = db.Column(db.String())
	ranged_trait = db.Column(db.String())
	ranged_damage_type = db.Column(db.String())
	ranged_damage_value = db.Column(db.Integer)
	weapon_trait_type = db.Column(db.String())
	weapon_trait = db.Column(db.String())
	weapon_mod = db.Column(db.Integer)
	weapon_damage_type = db.Column(db.String())
	weapon_damage = db.Column(db.Integer)
	support_strength = db.Column(db.Integer)
	support_strengthen = db.Column(db.Boolean)
	support_action = db.Column(db.Integer)
	support_action_rounds = db.Column(db.Integer)
	support_effort = db.Column(db.Integer)
	support_effort_rounds = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'solidity': self.solidity,
			'visibility': self.visibility,
			'complexity': self.complexity,
			'volume': self.volume,
			'toughness': self.toughness,
			'mass': self.mass,
			'damageable': self.damageable,
			'maintained': self.maintained,
			'repairable': self.repairable,
			'moveable': self.moveable,
			'stationary': self.stationary,
			'trap': self.trap,
			'ranged': self.ranged,
			'weapon': self.weapon,
			'support': self.support,
			'real': self.real,
			'cover': self.cover,
			'conceal': self.conceal,
			'incoming': self.incoming,
			'outgoing': self.outgoing,
			'transform': self.transform,
			'transform_type': self.transform_type,
			'transform_start_mass': self.transform_start_mass,
			'transfom_mass': self.transfom_mass,
			'transform_start_descriptor': self.transform_start_descriptor,
			'transform_end_descriptor': self.transform_end_descriptor,
			'move_player': self.move_player,
			'move_player_trait': self.move_player_trait,
			'move_opponent_check': self.move_opponent_check,
			'move_opponent_ability': self.move_opponent_ability,
			'move_opponent_rank': self.move_opponent_rank,
			'trap_type': self.trap_type,
			'trap_dc': self.trap_dc,
			'trap_trait_type': self.trap_trait_type,
			'trap_trait': self.trap_trait,
			'trap_resist_check': self.trap_resist_check,
			'trap_resist_trait': self.trap_resist_trait,
			'trap_resist_dc': self.trap_resist_dc,
			'trap_escape': self.trap_escape,
			'ranged_type': self.ranged_type,
			'ranged_dc': self.ranged_dc,
			'ranged_trait_type': self.ranged_trait_type,
			'ranged_trait': self.ranged_trait,
			'ranged_damage_type': self.ranged_damage_type,
			'ranged_damage_value': self.ranged_damage_value,
			'weapon_trait_type': self.weapon_trait_type,
			'weapon_trait': self.weapon_trait,
			'weapon_mod': self.weapon_mod,
			'weapon_damage_type': self.weapon_damage_type,
			'weapon_damage': self.weapon_damage,
			'support_strength': self.support_strength,
			'support_strengthen': self.support_strengthen,
			'support_action': self.support_action,
			'support_action_rounds': self.support_action_rounds,
			'support_effort': self.support_effort,
			'support_effort_rounds': self.support_effort_rounds,
			'cost': self.cost,
			'ranks': self.ranks
		}

class PowerDamage(db.Model):
	__tablename__ = 'power_damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	mod = db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	damage_type = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'strength': self.strength,
			'damage_type': self.damage_type,
			'descriptor': self.descriptor
		}

class PowerDC(db.Model):
	__tablename__ = 'power_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	dc = db.Column(db.String())
	description = db.Column(db.String())
	value = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_trait_type = db.Column(db.String())
	math_trait = db.Column(db.String())
	descriptor_check = db.Column(db.Boolean)
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	descriptor_possess = db.Column(db.String())
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	keyword = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	check_mod = db.Column(db.Integer)
	levels = db.Column(db.Boolean)
	level = db.Column(db.Integer, db.ForeignKey('power_levels.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'dc': self.dc,
			'description': self.description,
			'value': self.value,
			'math_value': self.math_vqlue,
			'math': self.math,
			'math_trait_type': self.math_trait_type,
			'math_trait': self.math_trait,
			'descriptor_check': self.descriptor_check,
			'condition': self.condition,
			'keyword_check': self.keyword_check,
			'check_type': self.check_type,
			'descriptor': self.descriptor,
			'descriptor_possess': self.descriptor_possess,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_mod': self.check_mod,
			'levels': self.levels,
			'level': self.level
		}

class PowerDefense(db.Model):
	__tablename__ = 'power_defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	defense = db.Column(db.String())
	use = db.Column(db.String())
	mod = db.Column(db.Integer)
	roll = db.Column(db.Integer)
	outcome = db.Column(db.String())
	dodge = db.Column(db.Boolean)
	fortitude = db.Column(db.Boolean)
	parry = db.Column(db.Boolean)
	toughness = db.Column(db.Boolean)
	will = db.Column(db.Boolean)
	resist_area = db.Column(db.Boolean)
	resist_perception = db.Column(db.Boolean)
	reflect = db.Column(db.Boolean)
	immunity = db.Column(db.Boolean)
	reflect_action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	reflect_dc = db.Column(db.Integer)
	reflect_opposed_trait_type = db.Column(db.String())
	reflect_opposed_trait = db.Column(db.String())
	reflect_resist_trait_type = db.Column(db.String())
	reflect_resist_trait = db.Column(db.String())
	immunity_type = db.Column(db.String())
	immunity_trait_type = db.Column(db.String())
	immunity_trait = db.Column(db.String())
	immunity_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	immunity_damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	immunity_rule = db.Column(db.String())
	cover_check = db.Column(db.Boolean)
	cover_type = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'defense': self.defense,
			'use': self.use,
			'mod': self.mod,
			'roll': self.roll,
			'outcome': self.outcome,
			'dodge': self.dodge,
			'fortitude': self.fortitude,
			'parry': self.parry,
			'toughness': self.toughness,
			'will': self.will,
			'resist_area': self.resist_area,
			'resist_perception': self.resist_perception,
			'reflect': self.reflect,
			'immunity': self.immunity,
			'reflect_action': self.reflect_action,
			'reflect_check': self.reflect_check,
			'reflect_dc': self.reflect_dc,
			'reflect_opposed_trait_type': self.reflect_opposed_trait_type,
			'reflect_opposed_trait': self.reflect_opposed_trait,
			'reflect_resist_trait_type': self.reflect_resist_trait_type,
			'reflect_resist_trait': self.reflect_resist_trait,
			'immunity_type': self.immunity_type,
			'immunity_trait_type': self.immunity_trait_type,
			'immunity_trait': self.immunity_trait,
			'immunity_descriptor': self.immunity_descriptor,
			'immunity_damage': self.immunity_damage,
			'immunity_rule': self.immunity_rule,
			'cover_check': self.cover_check,
			'cover_type': self.cover_type
		}

class PowerDegMod(db.Model):
	__tablename__ = 'power_degree_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	value = db.Column(db.Integer)
	deg_type = db.Column(db.String())
	circ_value = db.Column(db.Integer)
	circ_turns = db.Column(db.Integer)
	circ_trait_type = db.Column(db.String())
	circ_trait = db.Column(db.String())
	measure_type = db.Column(db.String())
	measure_val1 = db.Column(db.Integer)
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.String())
	measure_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	deg_condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.String())	
	condition2 = db.Column(db.String())
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)
	level = db.Column(db.Integer, db.ForeignKey('power_levels.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'value': self.value,
			'deg_type': self.deg_type,
			'circ_value': self.circ_value,
			'circ_turns': self.circ_turns,
			'circ_trait_type': self.circ_trait_type,
			'circ_trait': self.circ_trait,
			'measure_type': self.measure_type,
			'measure_val1': self.measure_val1,
			'measure_math': self.measure_math,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_value': self.measure_value,
			'measure_rank': self.measure_rank,
			'deg_condition_type': self.deg_condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'cumulative': self.cumulative,
			'linked': self.linked,
			'level': self.level
		}

class PowerDegree(db.Model):
	__tablename__ = 'power_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	degree_type = db.Column(db.String())
	degree = db.Column(db.Integer)
	keyword = db.Column(db.String())
	desscription = db.Column(db.String())
	extra_effort = db.Column(db.Boolean)
	cumulative = db.Column(db.Boolean)
	target = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'degree_type': self.degree_type,
			'degree': self.degree,
			'keyword': self.keyword,
			'desscription': self.desscription,
			'extra_effort': self.extra_effort,
			'cumulative': self.cumulative,
			'target': self.target
		}

class PowerEnv(db.Model):
	__tablename__ = 'power_environment'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	radius = db.Column(db.Integer)
	distance = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	condition_check = db.Column(db.Boolean)
	impede = db.Column(db.Boolean)
	conceal = db.Column(db.Boolean)
	visibility = db.Column(db.Boolean)
	selective = db.Column(db.Boolean)
	immunity = db.Column(db.Boolean)
	immunity_type = db.Column(db.String())
	temp_type = db.Column(db.String())
	immunity_extremity = db.Column(db.String())
	immunity_environment = db.Column(db.String())
	no_penalty = db.Column(db.Boolean)
	no_circumstance = db.Column(db.Boolean)
	immunity_other = db.Column(db.String())
	condition_temp_type = db.Column(db.String())
	temp_extremity = db.Column(db.String())
	move_nature = db.Column(db.String())
	move_speed = db.Column(db.Integer)
	move_cost_circ = db.Column(db.Boolean)
	move_other = db.Column(db.String())
	conceal_type = db.Column(db.String())
	visibility_trait_type = db.Column(db.String())
	visibility_trait = db.Column(db.String())
	visibility_mod = db.Column(db.Integer)
	cost = db.Column(db.Integer)
	ranks = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'radius': self.radius,
			'distance': self.distance,
			'rank': self.rank,
			'condition_check': self.condition_check,
			'impede': self.impede,
			'conceal': self.conceal,
			'visibility': self.visibility,
			'selective': self.selective,
			'immunity': self.immunity,
			'immunity_type': self.immunity_type,
			'temp_type': self.temp_type,
			'immunity_extremity': self.immunity_extremity,
			'immunity_environment': self.immunity_environment,
			'no_penalty': self.no_penalty,
			'no_circumstance': self.no_circumstance,
			'immunity_other': self.immunity_other,
			'condition_temp_type': self.condition_temp_type,
			'temp_extremity': self.temp_extremity,
			'move_nature': self.move_nature,
			'move_speed': self.move_speed,
			'move_cost_circ': self.move_cost_circ,
			'move_other': self.move_other,
			'conceal_type': self.conceal_type,
			'visibility_trait_type': self.visibility_trait_type,
			'visibility_trait': self.visibility_trait,
			'visibility_mod': self.visibility_mod,
			'cost': self.cost,
			'ranks': self.ranks
		}

class PowerLevels(db.Model):
	__tablename__ = 'power_levels'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	level_type = db.Column(db.String())
	level = db.Column(db.String())
	level_effect = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'level_type': self.level_type,
			'level': self.level,
			'level_effect': self.level_effect
		}

class PowerMinion(db.Model):
	__tablename__ = 'power_minions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	points = db.Column(db.Integer)
	condition = db.Column(db.String())
	player_condition = db.Column(db.String())
	link = db.Column(db.Boolean)
	variable_type = db.Column(db.String())
	multiple = db.Column(db.Boolean)
	attitude = db.Column(db.Boolean)
	resitable = db.Column(db.Boolean)
	heroic = db.Column(db.Boolean)
	sacrifice = db.Column(db.Boolean)
	sacrifice_cost = db.Column(db.Integer)
	attitude_type = db.Column(db.Integer, db.ForeignKey('power_levels.id'))
	attitude_trait_type = db.Column(db.String())
	attitude_trait = db.Column(db.String())
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))
	resitable_dc = db.Column(db.Integer)
	multiple_value = db.Column(db.Integer)
	horde = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'points': self.points,
			'condition': self.condition,
			'player_condition': self.player_condition,
			'link': self.link,
			'variable_type': self.variable_type,
			'multiple': self.multiple,
			'attitude': self.attitude,
			'resitable': self.resitable,
			'heroic': self.heroic,
			'sacrifice': self.sacrifice,
			'sacrifice_cost': self.sacrifice_cost,
			'attitude_type': self.attitude_type,
			'attitude_trait_type': self.attitude_trait_type,
			'attitude_trait': self.attitude_trait,
			'resitable_check': self.resitable_check,
			'resitable_dc': self.resitable_dc,
			'multiple_value': self.multiple_value,
			'horde': self.horde
		}

class PowerMod(db.Model):
	__tablename__ = 'power_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	affects_objects = db.Column(db.Boolean)
	area = db.Column(db.Boolean)
	persistent = db.Column(db.Boolean)
	incurable = db.Column(db.Boolean)
	selective = db.Column(db.Boolean)
	limited = db.Column(db.Boolean)
	innate = db.Column(db.Boolean)
	others = db.Column(db.Boolean)
	sustained = db.Column(db.Boolean)
	reflect = db.Column(db.Boolean)
	redirect = db.Column(db.Boolean)
	half = db.Column(db.Boolean)
	affects_corp = db.Column(db.Boolean)
	continuous = db.Column(db.Boolean)
	vulnerable = db.Column(db.Boolean)
	precise = db.Column(db.Boolean)
	progressive = db.Column(db.Boolean)
	subtle = db.Column(db.Boolean)
	permanent = db.Column(db.Boolean)
	points = db.Column(db.Boolean)
	ranks = db.Column(db.Boolean)
	action = db.Column(db.Boolean)
	side_effect = db.Column(db.Boolean)
	concentration = db.Column(db.Boolean)
	simultaneous = db.Column(db.Boolean)
	effortless = db.Column(db.Boolean)
	noticeable = db.Column(db.Boolean)
	unreliable = db.Column(db.Boolean)
	objects_alone = db.Column(db.Integer, db.ForeignKey('defense.id'))
	objects_character = db.Column(db.Integer, db.ForeignKey('defense.id'))
	effortless_degree = db.Column(db.Integer)
	effortless_retries = db.Column(db.Boolean)
	simultaneous_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	area_mod =db.Column(db.Integer)
	area_range = db.Column(db.Integer)
	area_per_rank = db.Column(db.Boolean)
	area_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_type = db.Column(db.String())
	limited_mod = db.Column(db.Integer)
	limited_level = db.Column(db.Integer, db.ForeignKey('power_levels.id'))
	limited_source = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_task_type = db.Column(db.String())
	limited_task = db.Column(db.String())
	limited_trait_type = db.Column(db.String())
	limited_trait = db.Column(db.String())
	limited_description = db.Column(db.String())
	limited_subjects = db.Column(db.Integer)
	limited_extra = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_language_type = db.Column(db.String())
	limited_degree = db.Column(db.Integer)
	limited_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	limited_subsense = db.Column(db.String())
	limited_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_range = db.Column(db.Integer, db.ForeignKey('range.id'))
	side_effect_type = db.Column(db.String())
	side_level = db.Column(db.Integer, db.ForeignKey('power_levels.id'))
	side_other = db.Column(db.String())
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	reflect_trait_type = db.Column(db.String())
	reflect_trait = db.Column(db.String())
	reflect_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	subtle_opponent_trait_type = db.Column(db.String())
	subtle_opponent_trait = db.Column(db.String())
	subtle_dc = db.Column(db.Integer)
	subtle_null_trait_type = db.Column(db.String())
	subtle_null_trait = db.Column(db.String())
	others_carry = db.Column(db.Boolean)
	others_touch = db.Column(db.Boolean)
	others_touch_continuous = db.Column(db.Boolean)
	ranks_trait_type = db.Column(db.String())
	ranks_trait = db.Column(db.String())
	ranks_ranks = db.Column(db.Integer)
	ranks_mod = db.Column(db.Integer)
	points_type = db.Column(db.String())
	points_reroll_target = db.Column(db.String())
	points_reroll_cost = db.Column(db.Integer)
	points_rerolls = db.Column(db.Integer)
	points_reroll_result = db.Column(db.String())
	ranks_cost = db.Column(db.Integer)
	cost = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'affects_objects': self.affects_objects,
			'area': self.area,
			'persistent': self.persistent,
			'incurable': self.incurable,
			'selective': self.selective,
			'limited': self.limited,
			'innate': self.innate,
			'others': self.others,
			'sustained': self.sustained,
			'reflect': self.reflect,
			'redirect': self.redirect,
			'half': self.half,
			'affects_corp': self.affects_corp,
			'continuous': self.continuous,
			'vulnerable': self.vulnerable,
			'precise': self.precise,
			'progressive': self.progressive,
			'subtle': self.subtle,
			'permanent': self.permanent,
			'points': self.points,
			'ranks': self.ranks,
			'action': self.action,
			'side_effect': self.side_effect,
			'concentration': self.concentration,
			'simultaneous': self.simultaneous,
			'effortless': self.effortless,
			'noticeable': self.noticeable,
			'unreliable': self.unreliable,
			'objects_alone': self.objects_alone,
			'objects_character': self.objects_character,
			'effortless_degree': self.effortless_degree,
			'effortless_retries': self.effortless_retries,
			'simultaneous_descriptor': self.simultaneous_descriptor,
			'area_mod': self.area_mod,
			'area_range': self.area_range,
			'area_per_rank': self.area_per_rank,
			'area_descriptor': self.area_descriptor,
			'limited_type': self.limited_type,
			'limited_mod': self.limited_mod,
			'limited_level': self.limited_level,
			'limited_source': self.limited_source,
			'limited_task_type': self.limited_task_type,
			'limited_task': self.limited_task,
			'limited_trait_type': self.limited_trait_type,
			'limited_trait': self.limited_trait,
			'limited_description': self.limited_description,
			'limited_subjects': self.limited_subjects,
			'limited_extra': self.limited_extra,
			'limited_language_type': self.limited_language_type,
			'limited_degree': self.limited_degree,
			'limited_sense': self.limited_sense,
			'limited_subsense': self.limited_subsense,
			'limited_descriptor': self.limited_descriptor,
			'limited_range': self.limited_range,
			'side_effect_type': self.side_effect_type,
			'side_level': self.side_level,
			'side_other': self.side_other,
			'reflect_check': self.reflect_check,
			'reflect_trait_type': self.reflect_trait_type,
			'reflect_trait': self.reflect_trait,
			'reflect_descriptor': self.reflect_descriptor,
			'subtle_opponent_trait_type': self.subtle_opponent_trait_type,
			'subtle_opponent_trait': self.subtle_opponent_trait,
			'subtle_dc': self.subtle_dc,
			'subtle_null_trait_type': self.subtle_null_trait_type,
			'subtle_null_trait': self.subtle_null_trait,
			'others_carry': self.others_carry,
			'others_touch': self.others_touch,
			'others_touch_continuous': self.others_touch_continuous,
			'ranks_trait_type': self.ranks_trait_type,
			'ranks_trait': self.ranks_trait,
			'ranks_ranks': self.ranks_ranks,
			'ranks_mod': self.ranks_mod,
			'points_type': self.points_type,
			'points_reroll_target': self.points_reroll_target, 
			'points_reroll_cost': self.points_reroll_cost,
			'points_rerolls': self.points_rerolls,
			'points_reroll_result': self.points_reroll_result,
			'ranks_cost': self.ranks_cost,
			'cost': self.cost
		}

class PowerMove(db.Model):
	__tablename__ = 'power_movement'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	rank = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	mod = db.Column(db.Integer)
	per_rank = db.Column(db.Boolean)
	flight = db.Column(db.Boolean)
	aquatic = db.Column(db.Boolean)
	ground = db.Column(db.Boolean)
	condition = db.Column(db.String())
	direction = db.Column(db.String())
	distance_type = db.Column(db.String())
	distance_value = db.Column(db.Integer)
	distance_math_value = db.Column(db.Integer)
	distance_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_math_value2 = db.Column(db.Integer)
	distance_mod = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	others = db.Column(db.Boolean)
	continuous = db.Column(db.Boolean)
	subtle = db.Column(db.Boolean)
	concentration = db.Column(db.Boolean)
	obstacles = db.Column(db.Boolean)
	objects = db.Column(db.Boolean)
	permeate = db.Column(db.Boolean)
	special = db.Column(db.Boolean)
	prone = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	obstacles_check = db.Column(db.Boolean)
	concealment = db.Column(db.Boolean)
	extended = db.Column(db.Boolean)
	mass = db.Column(db.Boolean)
	mass_value = db.Column(db.Integer)
	extended_actions = db.Column(db.Integer)
	acquatic_type = db.Column(db.String())
	concealment_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	concealment_trait_type = db.Column(db.String())
	concealment_trait = db.Column(db.String())
	permeate_type = db.Column(db.String())
	permeate_speed = db.Column(db.Integer)
	permeate_cover = db.Column(db.Boolean)
	special_type = db.Column(db.String())
	teleport_type = db.Column(db.String())
	teleport_change = db.Column(db.String())
	teleport_portal = db.Column(db.Boolean)
	teleport_obstacles = db.Column(db.Boolean)
	dimension_type = db.Column(db.String())
	dimension_mass_rank = db.Column(db.Integer)
	dimension_descriptor = db.Column(db.Integer)
	special_space = db.Column(db.String())
	special_time = db.Column(db.String())
	special_time_carry = db.Column(db.Integer)
	ground_type = db.Column(db.Integer, db.ForeignKey('ground.id'))
	ground_permanence = db.Column(db.String())
	ground_time = db.Column(db.Integer)
	ground_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	ground_ranged = db.Column(db.Boolean)
	subtle_trait_type = db.Column(db.String())
	subtle_trait = db.Column(db.String())
	subtle_mod = db.Column(db.Integer)
	flight_resist = db.Column(db.Boolean)
	flight_equip = db.Column(db.Boolean)
	flight_conditions = db.Column(db.ARRAY(db.String))
	objects_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	objects_attack = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	objects_skill_type = db.Column(db.String())
	objects_skill = db.Column(db.String())
	objects_direction = db.Column(db.String())
	objects_damage = db.Column(db.Boolean)
	damage_type = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	check_free = db.Column(db.Boolean)
	ranks = db.Column(db.Integer)
	cost = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'rank': self.rank,
			'math': self.math,
			'mod': self.mod,
			'per_rank': self.per_rank,
			'flight': self.flight,
			'aquatic': self.aquatic,
			'ground': self.ground,
			'condition': self.condition,
			'direction': self.direction,
			'distance_type': self.distance_type,
			'distance_value': self.distance_value,
			'distance_math_value': self.distance_math_value,
			'distance_math': self.distance_math,
			'distance_math_value2': self.distance_math_value2,
			'distance_mod': self.distance_mod,
			'dc': self.dc,
			'others': self.others,
			'continuous': self.continuous,
			'subtle': self.subtle,
			'concentration': self.concentration,
			'obstacles': self.obstacles,
			'objects': self.objects,
			'permeate': self.permeate,
			'special': self.special,
			'prone': self.prone,
			'check_type': self.check_type,
			'obstacles_check': self.obstacles_check,
			'concealment': self.concealment,
			'extended': self.extended,
			'mass': self.mass,
			'mass_value': self.mass_value,
			'extended_actions': self.extended_actions,
			'acquatic_type': self.acquatic_type,
			'concealment_sense': self.concealment_sense,
			'concealment_trait_type': self.concealment_trait_type,
			'concealment_trait': self.concealment_trait,
			'permeate_type': self.permeate_type,
			'permeate_speed': self.permeate_speed,
			'permeate_cover': self.permeate_cover,
			'special_type': self.special_type,
			'teleport_type': self.teleport_type,
			'teleport_change': self.teleport_change,
			'teleport_portal': self.teleport_portal,
			'teleport_obstacles': self.teleport_obstacles,
			'dimension_type': self.dimension_type,
			'dimension_mass_rank': self.dimension_mass_rank,
			'dimension_descriptor': self.dimension_descriptor,
			'special_space': self.special_space,
			'special_time': self.special_time,
			'special_time_carry': self.special_time_carry,
			'ground_type': self.ground_type,
			'ground_permanence': self.ground_permanence,
			'ground_time': self.ground_time,
			'ground_units': self.ground_units,
			'ground_ranged': self.ground_ranged,
			'subtle_trait_type': self.subtle_trait_type,
			'subtle_trait': self.subtle_trait,
			'subtle_mod': self.subtle_mod,
			'flight_resist': self.flight_resist,
			'flight_equip': self.flight_equip,
			'flight_conditions': self.flight_conditions,
			'objects_check': self.objects_check,
			'objects_attack': self.objects_attack,
			'objects_skill_type': self.objects_skill_type,
			'objects_skill': self.objects_skill,
			'objects_direction': self.objects_direction,
			'objects_damage': self.objects_damage,
			'damage_type': self.damage_type,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_free': self.check_free,
			'ranks': self.ranks,
			'cost': self.cost
		}

class PowerOpposed(db.Model):
	__tablename__ = 'power_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.String())
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'opponent_trait_type': self.opponent_trait_type,
			'opponent_trait': self.opponent_trait,
			'opponent_mod': self.opponent_mod,
			'player_check': self.player_check,
			'opponent_check': self.opponent_check
		}

class PowerRanged(db.Model):
	__tablename__ = 'power_ranged'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	range_type = db.Column(db.String())
	flat_value = db.Column(db.Integer)
	flat_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank = db.Column(db.Integer)
	flat_rank_value = db.Column(db.Integer)
	flat_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank_rank = db.Column(db.Integer)
	flat_rank_distance = db.Column(db.Integer)
	flat_rank_distance_rank = db.Column(db.Integer)
	units_rank_start_value = db.Column(db.Integer)
	units_rank_value = db.Column(db.Integer)
	units_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	units_rank_rank = db.Column(db.Integer)
	rank_distance_start = db.Column(db.Integer)
	rank_distance = db.Column(db.Integer)
	rank_effect_rank = db.Column(db.Integer)
	effect_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	effect_mod = db.Column(db.Integer)
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())
	check_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_mod = db.Column(db.Integer)
	trait_trait_type = db.Column(db.String())
	trait_trait = db.Column(db.String())
	trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_mod = db.Column(db.Integer)
	distance_mod_rank = db.Column(db.Integer)
	distance_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_mod_trait_type = db.Column(db.String())
	distance_mod_trait = db.Column(db.String())
	dc = db.Column(db.Boolean)
	dc_value = db.Column(db.Integer)
	dc_trait_type = db.Column(db.String())
	dc_trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'range_type': self.range_type,
			'flat_value': self.flat_value,
			'flat_units': self.flat_units,
			'flat_rank': self.flat_rank,
			'flat_rank_value': self.flat_rank_value,
			'flat_rank_units': self.flat_rank_units,
			'flat_rank_rank': self.flat_rank_rank,
			'flat_rank_distance': self.flat_rank_distance,
			'flat_rank_distance_rank': self.flat_rank_distance_rank,
			'units_rank_start_value': self.units_rank_start_value,
			'units_rank_value': self.units_rank_value,
			'units_rank_units': self.units_rank_units,
			'units_rank_rank': self.units_rank_rank,
			'rank_distance_start': self.rank_distance_start,
			'rank_distance': self.rank_distance,
			'rank_effect_rank': self.rank_effect_rank,
			'effect_mod_math': self.effect_mod_math,
			'effect_mod': self.effect_mod,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_math': self.check_math,
			'check_mod': self.check_mod,
			'trait_trait_type': self.trait_trait_type,
			'trait_trait': self.trait_trait,
			'trait_math': self.trait_math,
			'trait_mod': self.trait_mod,
			'distance_mod_rank': self.distance_mod_rank,
			'distance_mod_math': self.distance_mod_math,
			'distance_mod_trait_type': self.distance_mod_trait_type,
			'distance_mod_trait': self.distance_mod_trait,
			'dc': self.dc,
			'dc_value': self.dc_value,
			'dc_trait_type': self.dc_trait_type,
			'dc_trait': self.dc_trait
		}

class PowerResist(db.Model):
	__tablename__ = 'power_resistance_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	resist_check_type = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	descriptor = db.Column(db.Integer)
	requires_check = db.Column(db.Boolean)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'mod': self.mod,
			'rounds': self.rounds,
			'circumstance': self.circumstance,
			'resist_check_type': self.resist_check_type,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'descriptor': self.descriptor,
			'requires_check': self.requires_check,
			'check_type': self.check_type,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait
		}

class PowerResistBy(db.Model):
	__tablename__ = 'power_resisted_by'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	dc = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	description = db.Column(db.String())
	trait = db.Column(db.String())
	effect = db.Column(db.String())
	level = db.Column(db.Integer, db.ForeignKey('power_levels.id'))
	degree = db.Column(db.Integer)
	descriptor = db.Column(db.Integer)
	weaken_max = db.Column(db.Integer)
	weaken_restored = db.Column(db.Integer)
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	damage =  db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	nullify_descriptor = db.Column(db.Integer)
	nullify_alternate = db.Column(db.Integer, db.ForeignKey('defense.id'))
	extra_effort = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'dc': self.dc,
			'mod': self.mod,
			'description': self.description,
			'trait': self.trait,
			'effect': self.effect,
			'level': self.level,
			'degree': self.degree,
			'descriptor': self.descriptor,
			'weaken_max': self.weaken_max,
			'weaken_restored': self.weaken_restored,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'damage': self.damage,
			'strength': self.strength,
			'nullify_descriptor': self.nullify_descriptor,
			'nullify_alternate': self.nullify_alternate,
			'extra_effort': self.extra_effort
		}

class PowerReverse(db.Model):
	__tablename__ = 'power_reverse'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	degree = db.Column(db.Integer)
	when = db.Column(db.String())
	check_check = db.Column(db.Boolean)
	time_check = db.Column(db.Boolean)
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	value_type = db.Column(db.String())
	value_dc = db.Column(db.Integer)
	math_dc = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	time_value = db.Column(db.Integer)
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'degree': self.degree,
			'when': self.when,
			'check_check': self.check_check,
			'time_check': self.time_check,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'value_type': self.value_type,
			'value_dc': self.value_dc,
			'math_dc': self.math_dc,
			'math': self.math,
			'time_value': self.time_value,
			'time_unit': self.time_unit
		}

class PowerSense(db.Model):
	__tablename__ = 'power_sense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	sense = db.Column(db.Integer)
	subsense = db.Column(db.Integer)
	sense_cost = db.Column(db.Integer)
	subsense_cost = db.Column(db.Integer)
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill_required = db.Column(db.Boolean)
	sense_type = db.Column(db.String())
	height_trait_type = db.Column(db.String())
	height_trait = db.Column(db.String())
	height_power_required = db.Column(db.Boolean)
	height_ensense = db.Column(db.String())
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.String())
	resist_immune = db.Column(db.Boolean)
	resist_permanent = db.Column(db.String())
	resist_circ = db.Column(db.Integer)
	objects = db.Column(db.Boolean)
	exclusive = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	dark = db.Column(db.Boolean)
	lighting = db.Column(db.String())
	time = db.Column(db.Boolean)
	dimensional = db.Column(db.Boolean)
	radius = db.Column(db.Boolean)
	accurate = db.Column(db.Boolean)
	acute = db.Column(db.Boolean)
	time_set = db.Column(db.String())
	time_value = db.Column(db.Integer)
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	time_bonus = db.Column(db.String())
	time_factor = db.Column(db.Integer)
	distance = db.Column(db.String())
	distance_dc = db.Column(db.Integer)
	distance_mod = db.Column(db.Integer)
	distance_value = db.Column(db.Integer)
	distance_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	distance_factor = db.Column(db.Integer)
	dimensional_type = db.Column(db.String())
	ranks = db.Column(db.Integer)
	cost = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'sense': self.sense,
			'subsense': self.subsense,
			'sense_cost': self.sense_cost,
			'subsense_cost': self.subsense_cost,
			'skill': self.skill,
			'skill_required': self.skill_required,
			'sense_type': self.sense_type,
			'height_trait_type': self.height_trait_type,
			'height_trait': self.height_trait,
			'height_power_required': self.height_power_required,
			'height_ensense': self.height_ensense,
			'resist_trait_type': self.resist_trait_type,
			'resist_trait': self.resist_trait,
			'resist_immune': self.resist_immune,
			'resist_permanent': self.resist_permanent,
			'resist_circ': self.resist_circ,
			'objects': self.objects,
			'exclusive': self.exclusive,
			'gm': self.gm,
			'dark': self.dark,
			'lighting': self.lighting,
			'time': self.time,
			'dimensional': self.dimensional,
			'radius': self.radius,
			'accurate': self.accurate,
			'acute': self.acute,
			'time_set': self.time_set,
			'time_value': self.time_value,
			'time_unit': self.time_unit,
			'time_skill': self.time_skill,
			'time_bonus': self.time_bonus,
			'time_factor': self.time_factor,
			'distance': self.distance,
			'distance_dc': self.distance_dc,
			'distance_mod': self.distance_mod,
			'distance_value': self.distance_value,
			'distance_unit': self.distance_unit,
			'distance_factor': self.distance_factor,
			'dimensional_type': self.dimensional_type,
			'ranks': self.ranks,
			'cost': self.cost
		}

class PowerTime(db.Model):
	__tablename__ = 'power_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	time_type = db.Column(db.String())
	value_type = db.Column(db.String())
	value = db.Column(db.Integer)
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.String())
	dc = db.Column(db.Integer)
	descriptor = db.Column(db.Integer)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recovery = db.Column(db.Boolean)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'time_type': self.time_type,
			'value_type': self.value_type,
			'value': self.value,
			'units': self.units,
			'time_value': self.time_value,
			'math': self.math,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'dc': self.dc,
			'descriptor': self.descriptor,
			'check_type': self.check_type,
			'recovery': self.recovery,
			'recovery_penalty': self.recovery_penalty,
			'recovery_time': self.recovery_time,
			'recovery_incurable': self.recovery_incurable
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
	damage = db.Column(db.Boolean)

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
			'descriptor': self.descriptor,
			'damage': self.damage
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
	damage = db.Column(db.Boolean)

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
			'description': self.description,
			'damage': self.damage
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
	damage = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'damage': self.damage
		}

class MediumType(db.Model):
	__tablename__ = 'medium_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'damage': self.damage
		}

class MediumSubType(db.Model):
	__tablename__ = 'medium_subtype'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'description': self.description,
			'damage': self.damage
		}

class Medium(db.Model):
	__tablename__ = 'medium'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	description = db.Column(db.String())
	damage = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'description': self.description,
			'damage': self.damage
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

class DamageType(db.Model):
	__tablename__ = 'damage_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
		}
		
class Damage(db.Model):
	__tablename__ = 'damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	damage_type = db.Column(db.Integer, db.ForeignKey('damage_type.id'))

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
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