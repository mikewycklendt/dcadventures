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
	const check_type = select("check_check_type");
	const mod = select("check_mod");
	const circumstance = text("check_circ");
	const when = select("check_when");
	const trait_type = select("check_trait_type");
	const trait = select("check_trait");

class PowerAction(db.Model):
	__tablename__ = 'power_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const extra = select("action_extra");
	const action = select("action_change");
	const mod = select("action_mod");
	const objects = check("mod_objects");
	const circumstance = text("action_circ");

class PowerChar(db.Model):
	__tablename__ = 'power_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const extra = select("char_extra");
	const trait_type = select("char_trait_type");
	const trait = select("char_trait");
	const value = select("char_value");
	const increase = select("char_per");
	const limited = check("char_limited");
	const reduced = check("char_reduced");
	const limbs = check("char_limbs");
	const carry = check("char_carry");
	const sustained = check("char_sustained");
	const permanent = check("char_permanent");
	const points = check("char_points");
	const appear = check("char_appear");
	const insubstantial = check("char_insub");
	const weaken = check("char_weaken");
	const weaken_type = select("char_weaken_type");
	const weaken_trait_type = select("char_weaken_trait_type");
	const weaken_trait = select("char_weaken_trait");
	const weaken_broad = select("char_weaken_broad");
	const weaken_descriptor = select("char_weaken_descriptor");
	const weaken_simultaneous = check("char_simultaneous");
	const limited_by = select("char_limited_by");
	const limited_other = text("char_other");
	const limited_emotion = select("char_emotion");
	const limited_emotion_other = text("char_emotion_other");
	const reduced_trait_type = select("char_reduced_trait_type");
	const reduced_trait = select("char_reduced_trait");
	const reduced_value = select("char_reduced_value");
	const reduced_full = check("char_reduced_full");
	const limbs_continuous = check("char_continuous");
	const limbs_sustained = check("char_sustained");
	const limbs_distracting = check("char_distracting");
	const limbs_projection = check("char_projection");
	const carry_capacity = select("char_carry_capacity");
	const points_value = select("char_points_value");
	const points_trait_type = select("char_points_trait_type");
	const points_trait = select("char_points_trait");
	const points_descriptor = select("char_points_descriptor");
	const appear_target = select("char_appear_target");
	const appear_description = text("char_appear_des");
	const insub_type = select("char_insub_type");
	const insub_description = text("char_insub_des");
	const cost = select("char_cost");
	const ranks = select("char_ranks");

class PowerCirc(db.Model):
	__tablename__ = 'power_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const target = select("circ_target");
	const extra = select("circ_extra");
	const mod = select("circ_mod");
	const rounds = select("circ_rounds");
	const description = text("circ_des");
	const type = select("circ_type");
	const range = select("circ_range");
	const check_who = select("circ_check_who");
	const check_trait_type = select("circ_check_trait_type");
	const check_trait = select("circ_check_trait");
	const null_type = select("circ_null_type");
	const null_condition = select("circ_null_condition");
	const null_descriptor = select("circ_null_descriptor");
	const null_trait_type = select("circ_null_trait_type");
	const null_trait = select("circ_null_trait")

class PowerCreate(db.Model):
	__tablename__ = 'power_create'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const solidity = select("create_solidity");
	const visibility = select("create_visibility");
	const complexity = select("create_complexity");
	const volume = select("create_volume");
	const toughness = select("create_toughness");
	const mass = select("create_mass");
	const damageable = check("create_damageable");
	const maintained = check("create_maintained");
	const repairable = check("create_repairable");
	const moveable = check("create_moveable");
	const stationary = check("create_stationary");
	const trap = check("create_trap");
	const ranged = check("create_ranged");
	const weapon = check("create_weapon");
	const support = check("create_support");
	const real = check("create_real");
	const cover = check("create_cover");
	const conceal = check("create_conceal");
	const incoming = check("create_incoming");
	const outgoing = check("create_outgoing");
	const transform = check("create_transform");
	const transform_type = select("create_transform_type");
	const transform_start_mass = select("create_transform_start_mass");
	const transfom_mass = select("create_transfom_mass");
	const transform_start_descriptor = select("create_transform_start_descriptor");
	const transform_end_descriptor = select("create_transform_end_descriptor");
	const move_player = select("create_move_player");
	const move_player_trait = select("create_move_player_trait");
	const move_opponent_check = check("create_move_opponent_check");
	const move_opponent_ability = select("create_move_opponent_ability");
	const move_opponent_rank = select("create_move_opponent_rank");
	const trap_type = select("create_trap_type")
	const trap_dc = select("create_trap_dc");
	const trap_trait_type = select("create_trap_trait_type");
	const trap_trait = select("create_trap_trait");
	const trap_resist_check = select("create_trap_resist_check");
	const trap_resist_trait = select("create_trap_resist_trait");
	const trap_resist_dc = select("create_trap_resist_dc");
	const trap_escape = check("create_trap_escape");
	const ranged_type = select("create_ranged_type");
	const ranged_dc = select("create_ranged_dc");
	const ranged_trait_type = select("create_ranged_trait_type");
	const ranged_trait = select("create_ranged_trait");
	const ranged_damage_type = select("create_ranged_damage_type");
	const ranged_damage_value = select("create_ranged_damage_value");
	const weapon_trait_type = select("create_weapon_trait_type");
	const weapon_trait = select("create_weapon_trait");
	const weapon_mod = select("create_weapon_mod");
	const weapon_damage_type = select("create_weapon_damage_type");
	const weapon_damage = select("create_weapon_damage");
	const support_strength = select("create_support_strength");
	const support_strengthen = check("create_support_strengthen");
	const support_action = select("create_support_action");
	const support_action_rounds = select("create_support_action_rounds");
	const support_effort = select("create_support_effort");
	const support_effort_rounds = select("create_support_effort_rounds");
	const cost = select("create_cost_per_rank");
	const ranks = select("create_ranks");

class PowerDamage(db.Model):
	__tablename__ = 'power_damage'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const trait_type = select("dam_trait_type");
	const trait = select("dam_trait");
	const mod = select("dam_mod");
	const strength = check("dam_strength");
	const damage_type = select("damage_damage_type");
	const descriptor = select("damage_descriptor");

class PowerDC(db.Model):
	__tablename__ = 'power_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const target = select("dc_target");
	const extra = select("dc_extra");
	const dc = select("dc_dc");
	const description = text("dc_description");
	const value = select("dc_value_value");
	const math_vqlue = select("dc_math_vqlue");
	const math = select("dc_math_math");
	const math_trait_type = select("dc_math_trait_type");
	const math_trait = select("dc_math_trait");
	const descriptor_check = check("dc_descriptor_check");
	const condition = check("dc_condition");
	const keyword_check = check("dc_keyword_check");
	const check_type = check("dc_check_type");
	const descriptor = select("dc_descriptor");
	const descriptor_possess = select("dc_descriptor_possess");
	const condition1 = select("dc_condition1");
	const condition2 = select("dc_condition2");
	const keyword = text("dc_keyword");
	const check_trait_type = select("dc_check_trait_type");
	const check_trait = select("dc_check_trait");
	const check_mod = select("dc_check_mod");

class PowerDefense(db.Model):
	__tablename__ = 'power_defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const extra = select("defense_extra");
	const defense = select("defense_defense");
	const use = select("defense_use");
	const mod = select("defense_mod");
	const roll = select("defense_roll");
	const outcome = select("defense_outcome");
	const dodge = check("defense_dodge");
	const fortitude = check("defense_fortitude");
	const parry = check("defense_parry");
	const toughness = check("defense_toughness");
	const will = check("defense_will");
	const resist_area = check("defense_resist_area");
	const resist_perception = check("defense_resist_perc");
	const reflect = check("defense_reflect");
	const immunity = check("defense_immunity");
	const reflect_action = select("defense_reflect_action");
	const reflect_check = select("defense_reflect_check");
	const reflect_dc = select("defense_reflect_dc");
	const reflect_opposed_trait_type = select("defense_reflect_opposed_trait_type");
	const reflect_opposed_trait = select("defense_reflect_opposed_trait");
	const reflect_resist_trait_type = select("defense_reflect_resist_trait_type");
	const reflect_resist_trait = select("defense_reflect_resist_trait");
	const immunity_type = select("defense_immunity_type");
	const immunity_trait_type = select("defense_immunity_trait_type");
	const immunity_trait = select("defense_immunity_trait");
	const immunity_descriptor = select("defense_immunity_descriptor");
	const immunity_damage = select("defense_immunity_damage");
	const immunity_rule = select("defense_immunity_rule");
	const cover_check = check("defense_cover_check");
	const cover_type = select("defense_cover_type");

class PowerDegMod(db.Model):
	__tablename__ = 'power_degree_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const target = select("deg_mod_target");
	const extra = select("deg_mod_extra");
	const value = select("deg_value");
	const type = select("deg_mod_type");
	const circ_value = select("deg_mod_circ_value");
	const circ_turns = select("deg_mod_circ_turns");
	const circ_trait_type = select("deg_mod_circ_trait_type");
	const circ_trait = select("deg_mod_circ_trait");
	const measure_type = select("deg_mod_measure_type");
	const measure_val1 = select("deg_mod_measure_val1");
	const measure_math = select("deg_mod_measure_math");
	const measure_val2 = select("deg_mod_measure_val2");
	const measure_math_rank = select("deg_mod_measure_math_rank");
	const measure_value = select("deg_mod_measure_value");
	const measure_rank = select("deg_mod_measure_rank");
	const deg_condition_type = select("deg_mod_condition_type");
	const condition_damage_value = select("deg_mod_condition_damage_value");
	const condition_damage = select("deg_mod_condition_damage");
	const condition1 = select("deg_mod_condition1");	
	const condition2 = select("deg_mod_condition2");
	const keyword = text("deg_mod_keyword");
	const nullify = select("deg_mod_nullify");
	const cumulative = check("deg_mod_cumulative");
	const linked = check("deg_mod_linked");

class PowerDegree(db.Model):
	__tablename__ = 'power_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const degree_type = text("degree_type");
	const extra = select("degree_extra");
	const degree = select("degree_degree");
	const keyword = text("degree_keyword");
	const desscription = text("degree_desscription");
	const extra_effort = check("mod_extra_effort");
	const cumulative = check("mod_cumulative");
	const target = select("degree_target");

class PowerEnv(db.Model):
	__tablename__ = 'power_environment'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const extra = select("env_extra");
	const radius = text("env_radius");
	const distance = select("env_distance");
	const rank = select("env_rank");
	const condition_check = check("env_condition");
	const impede = check("env_impede");
	const conceal = check("env_conceal");
	const visibility = check("env_visibility");
	const selective = check("env_selective");
	const immunity = check("env_immunity");
	const immunity_type = select("env_immunity_type");
	const temp_type = select("env_temp_type");
	const immunity_extremity = select("env_immunity_extremity");
	const immunity_environment = select("env_immunity_environment");
	const no_penalty = check("env_no_penalty");
	const no_circumstance = check("env_no_circumstance");
	const immunity_other = text("env_immunity_other");
	const condition_temp_type = select("env_condition_temp_type");
	const temp_extremity = select("env_temp_extremity");
	const temp_cost = select("env_temp_cost");
	const condition_rank = select("env_condition_rank");
	const move_nature = select("env_move_nature");
	const move_speed = select("env_move_speed");
	const move_cost = select("env_move_cost");
	const move_cost_circ = check("env_move_cost_circ");
	const move_other = text("env_move_other");
	const conceal_reduce = select("env_conceal_reduce");
	const conceal_eliminate = select("env_conceal_eliminate");
	const visibility_trait_type = select("env_visibility_trait_type");
	const visibility_trait = select("env_visibility_trait");
	const visibility_mod = select("env_visibility_mod");
	const visibility_cost = select("env_visibility_cost");

class PowerLevels(db.Model):
	__tablename__ = 'power_levels'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const level_type = text("level_type");
	const extra = select("levels_extra");
	const level = text("level");
	const level_effect = text("level_effect");

class PowerMinion(db.Model):
	__tablename__ = 'power_minions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	const extra = select("minion_extra");
	const points = select("mod_minion_points");
	const condition = select("mod_minion_condition");
	const player_condition = select("mod_minion_player_condition");
	const link = check("mod_minion_link");
	const variable_type = select("mod_minion_variable_type");
	const multiple = check("minion_multiple");
	const attitude = check("minion_attitude");
	const resitable = check("minion_resitable");
	const heroic = check("minion_heroic");
	const sacrifice = check("minion_sacrifice");
	const sacrifice_cost = select("mod_minion_sacrifice_cost");
	const attitude_type = select("minion_attitude_type");
	const attitude_trait_type = select("minion_attitude_trait_type");
	const attitude_trait = select("minion_attitude_trait");
	const resitable_checkc = select("minion_resitable_checkc");
	const resitable_dc = select("minion_resitable_dc");
	const multiple_value = select("mod_minion_multiple_value");
	const horde = check("mod_minion_horde");

class PowerMod(db.Model):
	__tablename__ = 'power_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	affects_objects = check("mod_affects_objects");
	area = check("mod_area");
	persistent = check("mod_persistent");
	incurable = check("mod_incurable");
	selective = check("mod_selective");
	limited = check("mod_limited");
	innate = check("mod_innate");
	others = check("mod_others");
	sustained = check("mod_sustained");
	reflect = check("mod_reflect");
	redirect = check("mod_redirect");
	half = check("mod_half");
	affects_corp = check("mod_affects_corp");
	continuous = check("mod_continuous");
	vulnerable = check("mod_vulnerable");
	precise = check("mod_precise");
	progressive = check("mod_progressive");
	subtle = check("mod_subtle");
	permanent = check("mod_permanent");
	points = check("mod_points");
	ranks = check("mod_ranks");
	action = check("mod_action");
	side_effect = check("mod_side_effect");
	concentration = check("mod_concentration");
	simultaneous = check("mod_simultaneous");
	effortless = check("mod_effortless");
	noticeable = check("mod_noticeable");
	unreliable = check("mod_unreliable");
	bjects_alone = select("mod_objects_alone");
	objects_character = select("mod_objects_character");
	effortless_degree = select("mod_effortless_degree");
	effortless_retries = select("mod_effortless_retries");
	simultaneous_descriptor = select("mod_simultaneous_descriptor");
	area_mod = select("mod_area_mod");
	area_range = select("mod_area_range");
	area_per_rank = check("mod_area_per_rank");
	area_descriptor = select("mod_area_descriptor");
	limited_type = select("mod_limited_type");
	limited_mod = select("mod_limited_mod");
	limited_source = select("mod_limited_source");
	limited_task_type = select("mod_limited_task_type");
	limited_task = text("mod_limited_task");
	limited_trait_type = select("mod_limited_trait_type");
	_limited_trait = select("mod_limited_trait");
	limited_description = text("mod_limited_description");
	limited_subjects = select("mod_limited_subjects");
	limited_extra = select("mod_limited_extra");
	limited_language_type = select("mod_limited_language_type");
	limited_degree = select("mod_limited_degree");
	limited_sense = select("mod_limited_sense");
	imited_subsense = select("mod_limited_subsense");
	limited_descriptor = select("mod_limited_descriptor");
	limited_range = select("mod_limited_range");
	side_effect_type = select("mod_side_effect_type");
	side_other = text("mod_side_other");
	reflect_check = select("mod_reflect_check");
	reflect_trait_type = select("mod_reflect_trait_type");
	reflect_trait = select("mod_reflect_trait");
	reflect_descriptor = select("mod_reflect_descriptor");
	subtle_opponent_trait_type = select("mod_subtle_opponent_trait_type");
	subtle_opponent_trait = select("mod_subtle_opponent_trait");
	subtle_dc = select("mod_subtle_dc");
	subtle_null_trait_type = select("mod_subtle_null_trait_type");
	subtle_null_trait = select("mod_subtle_null_trait");
	others_carry = check("mod_others_carry");
	others_touch = check("mod_others_touch");
	others_touch_continuous = check("mod_others_touch_continuous");
	ranks_trait_type = select("mod_ranks_trait_type");
	ranks_trait = select("mod_ranks_trait");
	ranks_ranks = select("mod_ranks_ranks");
	ranks_mod = select("mod_ranks_mod");
	points_type = select("mod_points_type");
	points_reroll_target = select("mod_points_reroll_target");
	points_reroll_cost = select("mod_points_reroll_cost");
	points_rerolls = select("mod_points_rerolls");
	points_reroll_result = select("mod_points_reroll_result");
	ranks_cost = select("mod_ranks");
	cost = select("mod_cost");

class PowerMove(db.Model):
	__tablename__ = 'power_movement'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	rank = select("move_rank");
	math = select("move_math");
	mod = select("move_mod");
	per_rank = check("move_per_rank");
	flight = check("move_flight");
	aquatic = check("move_aquatic");
	ground = check("move_ground");
	condition = select("move_condition");
	direction = select("move_direction");
	distance_type = select("move_distance_type");
	distance_value = select("move_distance_value");
	distance_math_value = select("move_distance_math_value");
	distance_math = select("move_distance_math");
	distance_math_value2 = select("move_distance_math_value2");
	distance_mod = select("move_distance_mod");
	dc = select("move_dc");
	others = check("move_others");
	continuous = check("move_continuous");
	subtle = check("move_subtle");
	concentration = check("move_concentration");
	bstacles = check("move_obstacles");
	objects = check("move_objects");
	permeate = check("move_permeate");
	special = check("move_special");
	prone = check("move_prone");
	check_type = check("move_check_type");
	obstacles_check = check("move_obstacles");
	concealment = check("move_concealment");
	extended = check("move_extended");
	mass = check("move_mass");
	mass_value = select("move_mass_value");
	extended_actions = select("move_extended_actions");
	acquatic_type = select("move_acquatic_type");
	concealment_sense = select("move_concealment_sense");
	concealment_trait_type = select("move_concealment_trait_type");
	concealment_trait = select("move_concealment_trait");
	permeate_type = select("move_permeate_type");
	ermeate_speed = select("move_permeate_speed");
	permeate_cover = check("move_permeate_cover");
	special_type = select("move_special_type");
	teleport_type = select("move_teleport_type");
	teleport_change = select("move_teleport_change");
	teleport_portal = check("move_teleport_portal");
	teleport_obstacles = check("move_teleport_obstacles");
	dimension_type = select("move_dimension_type");
	dimension_mass_rank = select("move_dimension_mass_rank");
	dimension_descriptor = select("move_dimension_descriptor");
	special_space = select("move_special_space");
	special_time = select("move_special_time");
	special_time_carry = select("move_special_time_carry");
	ground_type = select("move_ground_type");
	ground_permanence = select("move_ground_perm");
	ground_time = select("move_ground_time");
	ground_units = select("move_ground_units");
	ground_ranged = check("move_ground_ranged");
	subtle_trait_type = select("move_subtle_trait_type");
	subtle_trait = select("move_subtle_trait");
	subtle_mod = select("move_subtle_mod");
	flight_resist = check("move_flight_resist");
	flight_equip = check("move_flight_equip");
	flight_conditions = multiple("move_flight_conditions");
	objects_check = select("move_objects_check");
	objects_attack = select("move_objects_attack");
	objects_skill_type = select("move_objects_skill_type");
	objects_skill = select("move_objects_skill");
	objects_direction = select("move_objects_direction");
	objects_damage = check("move_objects_damage");
	damage_type = select("move_objects_damage_type");
	check_trait_type = select("move_check_trait_type");
	check_trait = select("move_check_trait");
	check_free = check("move_check_free");
	ranks = select("move_ranks");

class PowerOpposed(db.Model):
	__tablename__ = 'power_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = select("opposed_trait_type");
	trait = select("opposed_trait");
	mod = select("opposed_mod");
	opponent_trait_type = select("opposed_opponent_trait_type");
	opponent_trait = select("opposed_opponent_trait");
	opponent_mod = select("opposed_opponent_mod");
	player_check = select("opposed_player_check");
	opponent_check = select("opposed_opponent_check");

class PowerRanged(db.Model):
	__tablename__ = 'power_ranged'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	type = select("ranged_type");
	flat_value = text("ranged_flat_value");
	flat_units = select("ranged_flat_units");
	flat_rank = select("ranged_flat_rank");
	flat_rank_value = text("ranged_flat_rank_value");
	flat_rank_units = select("ranged_flat_rank_units");
	flat_rank_rank = select("ranged_flat_rank_rank");
	flat_rank_distance = select("ranged_flat_rank_distance");
	flat_rank_distance_rank = select("ranged_flat_rank_distance_rank");
	units_rank_start_value = text("ranged_units_rank_start_value");
	units_rank_value = text("ranged_units_rank_value");
	units_rank_units = select("ranged_units_rank_units");
	units_rank_rank = select("ranged_units_rank_rank");
	rank_distance_start = select("ranged_rank_distance_start");
	rank_distance = select("ranged_rank_distance");
	rank_effect_rank = select("ranged_rank_effect_rank");
	effect_mod_math = select("ranged_effect_mod_math");
	effect_mod = select("ranged_effect_mod");
	check_trait_type = select("ranged_check_trait_type");
	check_trait = select("ranged_check_trait");
	check_math = select("ranged_check_math");
	check_mod = select("ranged_check_mod");
	trait_trait_type = select("ranged_trait_trait_type");
	trait_trait = select("ranged_trait_trait");
	trait_math = select("ranged_trait_math");
	trait_mod = select("ranged_trait_mod");
	distance_mod_rank = select("ranged_distance_mod_rank");
	distance_mod_math = select("ranged_distance_mod_math");
	distance_mod_trait_type = select("ranged_distance_mod_trait_type");
	distance_mod_trait = select("ranged_distance_mod_trait");
	dc = check("ranged_dc");
	dc_value = select("ranged_dc_value");
	dc_trait_type = select("ranged_dc_trait_type");
	dc_trait = select("ranged_dc_trait");

class PowerResist(db.Model):
	__tablename__ = 'power_resistance_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = select("resistance_target");
	mod = select("resistance_mod");
	rounds = select("resistance_rounds");
	circumstance = text("resistance_circ");
	resist_check_type = select("resistance_resist_check_type");
	trait_type = select("resistance_trait_type");
	trait = select("resistance_trait");
	descriptor = select("resistance_descriptor");
	requires_check = check("resistance_requires_check");
	check_type = select("resistance_check_type");
	check_trait_type = select("resistance_check_trait_type");
	check_trait = select("resistance_check_trait");

class PowerResistBy(db.Model):
	__tablename__ = 'power_resisted_by'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = select("resist_trait_type");
	dc = select("resist_dc");
	mod = select("resist_mod");
	description = text("range_desc");
	trait = select("resist_trait");
	effect = select("resist_eft");
	degree = select("resist_deg");
	descriptor = select("resist_descriptor");
	weaken_max = select("resist_weaken_max");
	weaken_restored = select("resist_weaken_restored");
	condition1 = select("resist_con1");
	condition2 = select("resist_con2");
	damage =  select("resist_dam");
	strength = check("resist_strength");
	nullify_descriptor = select("resist_nullify_descriptor");
	nullify_alternate = select("resist_nullify_alternate");
	extra_effort = check("resist_extra_effort");

class PowerReverse(db.Model):
	__tablename__ = 'power_reverse'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = select("reverse_target");
	degree = select("reverse_degree");
	when = select("reverse_when");
	check_check = check("reverse_check_check");
	time_check = check("reverse_time_check");
	trait_type = select("reverse_trait_type");
	trait = select("reverse_trait");
	value_type = select("reverse_value_type");
	value_dc = select("reverse_value_dc");
	math_dc = select("reverse_math_dc");
	math = select("reverse_math");
	time_value = text("reverse_time");
	time_unit = select("reverse_time_unit");

class PowerSense(db.Model):
	__tablename__ = 'power_sense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = select("sense_target");
	sense = select("sense_sense");
	subsense = select("sense_subsense");
	sense_cost = select("sense_sense_cost");
	subsense_cost = select("sense_subsense_cost");
	skill = select("sense_skill");
	skill_required = check("sense_skill_req");
	type = select("sense_type");
	height_trait_type = select("sense_height_trait_type");
	height_trait = select("sense_height_trait");
	height_power_required = check("sense_height_power_req");
	height_ensense = select("sense_height_ensense");
	resist_trait_type = select("sense_resist_trait_type");
	resist_trait = select("sense_resist_trait");
	resist_immune = check("sense_resist_immune");
	resist_permanent = select("sense_resist_perm");
	resist_circ = select("sense_resist_circ");
	objects = check("sense_objects");
	exclusive = check("sense_exclusive");
	gm = check("sense_gm");
	dark = check("sense_dark");
	lighting = select("sense-lighting");
	time = check("sense_time");
	dimensional = check("sense_dimensional");
	radius = check("sense_radius");
	accurate = check("sense_accurate");
	acute = check("sense_acute");
	time_set = select("sense_time_set");
	time_value = text("sense_time_value");
	time_unit = select("sense_time_unit");
	time_skill = select("sense_time_skill");
	time_bonus = select("sense_time_bonus");
	time_factor = select("sense_time_factor");
	distance = select("sense_distance");
	distance_dc = select("sense_dis_dc");
	distance_mod = select("sense_dis_mod");
	distance_value= text("sense_dis_value");
	distance_unit = select("sense_dis_unit");
	distance_factor = select("sense_dis_factor");
	dimensional_type = select("sense_dimensional_type");
	ranks = select("sense_ranks");

class PowerTime(db.Model):
	__tablename__ = 'power_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	type = select("time_type");
	value_type = select("time_value_type");
	value = text("time_value");
	units = select("time_units");
	time_value = select("dc_time_value");
	math = select("time_math");
	trait_type = select("time_trait_type");
	trait = select("time_trait");
	dc = select("time_dc");
	descriptor = select("time_descriptor");
	check_type = select("time_check_type");
	recovery = check("time_recovery");
	recovery_penalty = select("time_recovery_penalty");
	recovery_time = select("time_recovery_time");
	recovery_incurable = check("time_recovery_incurable");

















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