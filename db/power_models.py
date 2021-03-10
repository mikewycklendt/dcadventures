from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import setup_db
from models import db

load_dotenv()

import os

db_path = os.environ.get("db_path")

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = db_path
app.config["SQLALCHEMY_DATABASE_URI"] = database_path

setup_db(app)


migrate = Migrate(app, db)

class Power(db.Model):
	__tablename__ = 'powers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	description = db.Column(db.String())
	power_type = db.Column(db.Integer, db.ForeignKey('power_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	power_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	cost = db.Column(db.Integer)
	limit = db.Column(db.Integer)
	dc_type = db.Column(db.String())
	dc_value = db.Column(db.Integer)
	dc_mod = db.Column(db.Integer)
	opponent_dc = db.Column(db.Integer)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	routine = db.Column(db.Boolean)
	routine_trait_type = db.Column(db.String())
	routine_trait = db.Column(db.Integer)
	materials = db.Column(db.Boolean)
	partner = db.Column(db.String())
	partner_trait_type = db.Column(db.String())
	partner_trait = db.Column(db.Integer)
	partner_dc = db.Column(db.Integer)
	circ = db.Column(db.String())
	circ_required = db.Column(db.String())
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill_required = db.Column(db.String())
	skill_when = db.Column(db.String())
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_bonus = db.Column(db.Integer)
	conflict_type = db.Column(db.String())
	target_type = db.Column(db.String())
	target = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	alt_check = db.Column(db.Boolean)
	change_action = db.Column(db.Boolean)
	character = db.Column(db.Boolean)
	circumstance = db.Column(db.Boolean)
	create = db.Column(db.Boolean)	
	damage = db.Column(db.Boolean)
	dc = db.Column(db.Boolean)
	defense = db.Column(db.Boolean)
	degree = db.Column(db.Boolean)
	environment = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	minion = db.Column(db.Boolean)
	modifier = db.Column(db.Boolean)
	move = db.Column(db.Boolean)
	opposed = db.Column(db.Boolean)
	ranged = db.Column(db.Boolean)
	resistance = db.Column(db.Boolean)
	resist_by = db.Column(db.Boolean)
	reverse = db.Column(db.Boolean)
	sense = db.Column(db.Boolean)
	time = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)
	active = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'power_type': self.power_type,
			'action': self.action,
			'power_range': self.power_range,
			'duration': self.duration,
			'cost': self.cost,
			'limit': self.limit,
			'dc_type': self.dc_type,
			'dc_value': self.dc_value,
			'dc_mod': self.dc_mod,
			'opponent_dc': self.opponent_dc,
			'check_type': self.check_type,
			'routine': self.routine,
			'routine_trait_type': self.routine_trait_type,
			'routine_trait': self.routine_trait,
			'materials': self.materials,
			'partner': self.partner,
			'partner_trait_type': self.partner_trait_type,
			'partner_dc': self.partner_dc,
			'partner_trait': self.partner_trait,
			'circ': self.circ,
			'circ_required': self.circ_required,
			'skill': self.skill,
			'skill_required': self.skill_required,
			'skill_when': self.skill_when,
			'grab': self.grab,
			'grab_type': self.grab_type,
			'condition': self.condition,
			'alt_check': self.alt_check,
			'change_action': self.change_action,
			'character': self.character,
			'circumstance': self.circumstance,
			'create	': self.create,
			'damage': self.damage,
			'dc': self.dc,
			'defense': self.defense,
			'degree': self.degree,
			'environment': self.environment,
			'levels': self.levels,
			'minion': self.minion,
			'modifier': self.modifier,
			'move': self.move,
			'opposed': self.opposed,
			'ranged': self.ranged,
			'resistance': self.resistance,
			'resist_by': self.resist_by,
			'reverse': self.reverse,
			'sense': self.sense,
			'time': self.time,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base,
			'active': self.active
		}

class PowerType(db.Model):
	__tablename__ = 'power_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

		
class PowerDuration(db.Model):
	__tablename__ = 'power_duration'
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
	inherit = db.Column(db.Integer, db.ForeignKey('powers.id'))
	alternate = db.Column(db.Boolean)
	all = db.Column(db.Boolean)
	current = db.Column(db.Boolean)
	any = db.Column(db.Boolean)
	var = db.Column(db.Boolean)
	none = db.Column(db.Boolean)
	show = db.Column(db.Boolean)
	approved = db.Column(db.Boolean)
	base = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'name': self.name,
			'cost': self.cost,
			'ranks': self.ranks,
			'des': self.des,
			'inherit': self.inherit,
			'alternate': self.alternate,
			'all': self.all,
			'current': self.current,
			'any': self.any,
			'var': self.var,
			'none': self.none,
			'show': self.show,
			'approved': self.approved,
			'base': self.base
		}

class PowerCheck(db.Model):
	__tablename__ = 'power_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))




class PowerCirc(db.Model):
	__tablename__ = 'power_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))




class PowerDC(db.Model):
	__tablename__ = 'power_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))



class PowerDegree(db.Model):
	__tablename__ = 'power_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))




class PowerMove(db.Model):
	__tablename__ = 'power_movement'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))



class PowerOpposed(db.Model):
	__tablename__ = 'power_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))



class PowerTime(db.Model):
	__tablename__ = 'power_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))



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
	trait = db.Column(db.Integer)
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
	weaken_trait = db.Column(db.Integer)
	weaken_broad = db.Column(db.String())
	weaken_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))	
	weaken_simultaneous = db.Column(db.Boolean)
	limited_by = db.Column(db.String())
	limited_other = db.Column(db.String())
	limited_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	limited_emotion_other = db.Column(db.String())
	reduced_trait_type = db.Column(db.String())
	reduced_trait = db.Column(db.Integer)
	reduced_value = db.Column(db.Integer)
	reduced_full = db.Column(db.Boolean)
	limbs_continuous = db.Column(db.Boolean)
	limbs_sustained = db.Column(db.Boolean)
	limbs_distracting = db.Column(db.Boolean)
	limbs_projection = db.Column(db.Boolean)
	carry_capacity = db.Column(db.Integer)
	points_value = db.Column(db.Integer)
	points_trait_type = db.Column(db.String())
	points_trait = db.Column(db.Integer)
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
	move_player_trait = db.Column(db.Integer)
	move_opponent_check = db.Column(db.Boolean)
	move_opponent_ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	move_opponent_rank = db.Column(db.Integer)
	trap_type = db.Column(db.String())
	trap_dc = db.Column(db.Integer)
	trap_trait_type = db.Column(db.String())
	trap_trait = db.Column(db.Integer)
	trap_resist_check = db.Column(db.String())
	trap_resist_trait = db.Column(db.Integer)
	trap_resist_dc = db.Column(db.Integer)
	trap_escape = db.Column(db.Boolean)
	ranged_type = db.Column(db.String())
	ranged_dc = db.Column(db.Integer)
	ranged_trait_type = db.Column(db.String())
	ranged_trait = db.Column(db.Integer)
	ranged_damage_type = db.Column(db.String())
	ranged_damage_value = db.Column(db.Integer)
	weapon_trait_type = db.Column(db.String())
	weapon_trait = db.Column(db.Integer)
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
	trait = db.Column(db.Integer)
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


class PowerDefense(db.Model):
	__tablename__ = 'power_defense'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
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
	reflect_opposed_trait = db.Column(db.Integer)
	reflect_resist_trait_type = db.Column(db.String())
	reflect_resist_trait = db.Column(db.Integer)
	immunity_type = db.Column(db.String())
	immunity_trait_type = db.Column(db.String())
	immunity_trait = db.Column(db.Integer)
	immunity_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	immunity_damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	immunity_rule = db.Column(db.String())
	cover_check = db.Column(db.Boolean)
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))

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
	immunity_environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	immunity_environment_other = db.Column(db.String())
	no_penalty = db.Column(db.Boolean)
	no_circumstance = db.Column(db.Boolean)
	immunity_other = db.Column(db.String())
	condition_temp_type = db.Column(db.String())
	temp_extremity = db.Column(db.String())
	move_nature = db.Column(db.Integer, db.ForeignKey('nature.id'))
	move_speed = db.Column(db.Integer)
	move_cost_circ = db.Column(db.Boolean)
	move_other = db.Column(db.String())
	conceal_type = db.Column(db.String())
	visibility_trait_type = db.Column(db.String())
	visibility_trait = db.Column(db.Integer)
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
			'immunity_environment_other': self.immunity_environment_other,
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

class PowerMinion(db.Model):
	__tablename__ = 'power_minions'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	points = db.Column(db.Integer)
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	link = db.Column(db.Boolean)
	variable_type = db.Column(db.String())
	multiple = db.Column(db.Boolean)
	attitude = db.Column(db.Boolean)
	resitable = db.Column(db.Boolean)
	heroic = db.Column(db.Boolean)
	sacrifice = db.Column(db.Boolean)
	sacrifice_cost = db.Column(db.Integer)
	attitude_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	attitude_attitude = db.Column(db.Integer, db.ForeignKey('levels.id'))
	attitude_trait_type = db.Column(db.String())
	attitude_trait = db.Column(db.Integer)
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
			'attitude_attitude': self.attitude_attitude,
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
	radius = db.Column(db.Boolean)
	accurate = db.Column(db.Boolean)
	acute = db.Column(db.Boolean)
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
	limited_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	limited_source = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	limited_task_type = db.Column(db.String())
	limited_task = db.Column(db.String())
	limited_trait_type = db.Column(db.String())
	limited_trait = db.Column(db.Integer)
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
	side_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	side_other = db.Column(db.String())
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	reflect_dc = db.Column(db.Integer)
	reflect_trait_type = db.Column(db.String())
	reflect_trait = db.Column(db.Integer)
	reflect_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	subtle_opponent_trait_type = db.Column(db.String())
	subtle_opponent_trait = db.Column(db.Integer)
	subtle_dc = db.Column(db.Integer)
	subtle_null_trait_type = db.Column(db.String())
	subtle_null_trait = db.Column(db.Integer)
	others_carry = db.Column(db.Boolean)
	others_touch = db.Column(db.Boolean)
	others_touch_continuous = db.Column(db.Boolean)
	ranks_trait_type = db.Column(db.String())
	ranks_trait = db.Column(db.Integer)
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
			'radius': self.radius,
			'accurate': self.accurate,
			'acute': self.acute,
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
			'reflect_dc': self.reflect_dc,
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
	check_trait = db.Column(db.Integer)
	check_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_mod = db.Column(db.Integer)
	trait_trait_type = db.Column(db.String())
	trait_trait = db.Column(db.Integer)
	trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_mod = db.Column(db.Integer)
	distance_mod_rank = db.Column(db.Integer)
	distance_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_mod_trait_type = db.Column(db.String())
	distance_mod_trait = db.Column(db.Integer)
	dc = db.Column(db.Boolean)
	dc_value = db.Column(db.Integer)
	dc_trait_type = db.Column(db.String())
	dc_trait = db.Column(db.Integer)
	
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
	trait = db.Column(db.Integer)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	requires_check = db.Column(db.Boolean)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)

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
	trait = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	description = db.Column(db.String())
	effect = db.Column(db.String())
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	degree = db.Column(db.Integer)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	weaken_max = db.Column(db.Integer)
	weaken_restored = db.Column(db.Integer)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	damage =  db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	nullify_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
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


class PowerSenseEffect(db.Model):
	__tablename__ = 'power_sense_effect'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	sense_cost = db.Column(db.Integer)
	subsense_cost = db.Column(db.Integer)
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill_required = db.Column(db.Boolean)
	sense_type = db.Column(db.String())
	height_trait_type = db.Column(db.String())
	height_trait = db.Column(db.Integer)
	height_power_required = db.Column(db.Boolean)
	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))
	resist_trait_type = db.Column(db.String())
	resist_trait = db.Column(db.Integer)
	resist_immune = db.Column(db.Boolean)
	resist_permanent = db.Column(db.String())
	resist_circ = db.Column(db.Integer)
	objects = db.Column(db.Boolean)
	exclusive = db.Column(db.Boolean)
	gm = db.Column(db.Boolean)
	dark = db.Column(db.Boolean)
	lighting = db.Column(db.Integer, db.ForeignKey('light.id'))
	time = db.Column(db.Boolean)
	dimensional = db.Column(db.Boolean)
	radius = db.Column(db.Boolean)
	accurate = db.Column(db.Boolean)
	acute = db.Column(db.Boolean)
	time_set = db.Column(db.String())
	time_value = db.Column(db.Integer)
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	time_bonus = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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
	trait = db.Column(db.Integer)
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
	hidden = db.Column(db.Boolean)
	rare = db.Column(db.Boolean)
	uncommon = db.Column(db.Boolean)
	common = db.Column(db.Boolean)
	very = db.Column(db.Boolean)
	any_damage = db.Column(db.Boolean)
	any_origin = db.Column(db.Boolean)
	any_source = db.Column(db.Boolean)
	any_medium_type = db.Column(db.Boolean)
	any_medium_subtype = db.Column(db.Boolean)
	any_medium = db.Column(db.Boolean)
	any_descriptor = db.Column(db.Boolean)

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
			'damage': self.damage,
			'hidden': self.hidden,
			'rare': self.rare,
			'uncommon': self.uncommon,
			'common': self.common,
			'very': self.very,
			'any_damage': self.any_damage,
			'any_origin': self.any_origin,
			'any_source': self.any_source,
			'any_medium_type': self.any_medium_type,
			'any_medium_subtype': self.any_medium_subtype,
			'any_medium': self.any_medium,
			'any_descriptor': self.any_descriptor
		}