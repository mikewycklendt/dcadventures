from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait


def veh_feature_post(entry, body, cells):

	vehicle_id = entry.vehicle_id
	feature = entry.feature
	cost = entry.cost
	equipment = entry.equipment
	weapon = entry.weapon
	addon = entry.addon

	feature = name(Feature, feature)
	equipment = name(Equipment, equipment)
	weapon = name(Weapon, weapon)

	vcells = vcell('equipment', 30, [equipment])
	vcells = vcell('weapon', 30, [weapon], vcells)
	vcells = vcell('feature', 30, [feature], vcells)
	cells = vcell_add('Item', addon, vcells, cells) 
	cells = cell('Cost', 10, [cost], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def veh_powers_post(entry, body, cells):

	vehicle_id = entry.vehicle_id
	cost = entry.cost
	ranks  = entry.ranks
	power = entry.power

	power = name(Power, power)

	cells = cell('Power', 35, [power])
	cells = cell('Cost', 12, [cost], cells)
	cells = cell('Ranks', 12, [ranks], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)
