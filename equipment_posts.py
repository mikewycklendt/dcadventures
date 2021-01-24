from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait



def equip_belt_post(entry, body, cells):

	equip_id = entry.equip_id
	feature = entry.feature
	weapon = entry.weapon
	equipment = entry.equipment

	feature = name(Feature, feature)
	weapon = name(Weapon, weapon)
	equipment = name(Equipment, equipment)
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	cost = integer_convert(cost)

	belt = [{'type': '', 'name': 'Add Item'}, {'type': 'equip', 'name': 'Equipment'}, {'type': 'weapon', 'name': 'Weapon'}, {'type': 'feature', 'name': 'Feature'}]


	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_check_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	when = entry.when
	skill_type = entry.skill_type
	skill = entry.skill
	check_type = entry.check_type
	action = entry.action
	action_time = entry.action_time

	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)
	check_type = name(Check, check_type)
	action = name(Action, action)
	
	when_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]
	when = selects(when, when_select)
	

	body = send(cells, body)
	
	cells.clear()

	return (body)
	
def equip_damaged_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	damage = entry.damage
	skill_type = entry.skill_type
	skill = entry.skill
	toughness = entry.toughness
	penalty = entry.penalty


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)

	damage = name(Descriptor, damage)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)

	toughness = integer_convert(toughness)

	damaged_select = [{'type': '', 'name': 'Damaged Effect'}, {'type': 'feature', 'name': 'Loses a Feature'}, {'type': 'circ', 'name': '-1 Circumstance'}]
	damaged = selects(damaged, damaged_select)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_descriptor_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	descriptor = entry.descriptor


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	descriptor = name(Descriptor, descriptor)
	


	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_effect_post(entry, body, cells):

	equip_id = entry.equip_id
	name = entry.name
	description = entry.description




	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_feature_post(entry, body, cells):

	equip_id = entry.equip_id
	name = entry.name
	description = entry.description


	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_limits_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	time = entry.time
	time_units = entry.time_units
	range = entry.range
	range_units = entry.range_units
	extend = entry.extend
	extendable = entry.extendable
	time_capacity = entry.time_capacity
	time_capacity_units = entry.time_capacity_units
	capacity = entry.capacity
	item = entry.item
	ammo = entry.ammo
	fuel = entry.fuel
	area_long = entry.area_long
	area_wide = entry.area_wide
	area_units = entry.area_units
	recharge = entry.recharge
	refill = entry.refill
	uses = entry.uses
	light = entry.light
	internet = entry.internet
	needs_interneT = entry.needs_internet


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	time_units = name(Unit, time_units)
	range_units = name(Unit, range_units)
	time_capacity_units = name(Unit, time_capacity_units)
	area_units = name(Unit, area_units)
	light = name(Light, light)
	
	
	time = integer_convert(time)
	range = integer_convert(range)
	time_capacity = integer_convert(time_capacity)
	capacity = integer_convert(capacity)
	area_long = integer_convert(area_long)
	area_wide = integer_convert(area_wide)
	uses = integer_convert(uses)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_modifiers_post(entry, body, cells):




def equip_opposed_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	dc = entry.dc
	skill_type = entry.skill_type
	skill = entry.skill
	check = entry.check
	when = entry.when
	condition1 = entry.condition1
	condition2 = entry.condition2


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)
	check = name(Check, check)
	
	dc = integer_convert(dc)

	when_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]
	when = selects(when, when_select)
	
	
	body = send(cells, body)
	
	cells.clear()

	return (body)