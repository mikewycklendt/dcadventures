from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait

def weap_condition_post(entry, body, cells):

	weapon_id = entry.weapon_id
	condition_type = entry.condition_type
	condition = entry.condition
	condition_null = entry.condition_null
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage_value = entry.damage_value
	damage = entry.damage

	damage_value = integer_convert(damage_value)

	updown_select = [{'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	damage = selects(damage, updown_select)

	vcells = vcell('active', 40, [condition, 'Active'])
	vcells = vcell('change', 60, [condition1, 'to', condition2], vcells)
	vcells = vcell('damage', 40, [damage_value, 'Condition', damage], vcells)
	vcells = vcell('null', 40, [condition_null, 'Nullified'], vcells)
	cells = vcell_add('Condition Effect', condition_type, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def weap_descriptor_post(entry, body, cells):

	weapon_id = entry.weapon_id
	descriptor = entry.descriptor

	descriptor = name(Descriptor, descriptor)
	
	cells = cell('Descriptor', 25, [descriptor], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def weap_benefit_post(entry, body, cells):

	weapon_id = entry.weapon_id
	benefit = entry.benefit

	benefit = name(benefit, descriptor)
	
	cells = cell('Benefit', 25, [benefit], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)
