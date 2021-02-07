
from models import Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged 
from models import setup_db, Ability,  ConflictAction, Damage, DamageType, flash
from models import Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense
from models import Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank 
from models import Levels, LevelType, Light

from db.advanrtage_modeks import Advantage, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait, get_description, get_name


def head_feature_post(entry, body, cells):

	head_id = entry.head_id
	feature = entry.feature

	feature_name = name(HeadFeature, feature)
	description = get_description(HeadFeature, feature)

	cells = cell('Feature', 25, [feature_name], cells)
	cells = cell('Description', 70, [description], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def head_addon_post(entry, body, cells):

	
	head_id = entry.head_id
	head_feature = entry.head_feature
	feature = entry.feature
	equipment = entry.equipment
	weapon = entry.weapon
	addon = entry.addon

	head_feature = name(HeadFeature, head_feature)
	feature = name(Feature, feature)
	equipment = name(Equipment, equipment)
	weapon = name(Weapon, weapon)


	cells = cell('Feature', 25, [head_feature])
	vcells = vcell('equipment', 30, [equipment])
	vcells = vcell('weapon', 30, [weapon], vcells)
	vcells = vcell('feature', 30, [feature], vcells)
	cells = vcell_add('Item', addon, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)
