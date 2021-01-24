
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry


def equip_belt_post_errors(data):

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	feature = data['feature']
	weapon = data['weapon']
	equipment = data['equipment']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	feature = id_check(Feature, feature, 'Feature', errors)
	weapon = id_check(Weapon, weapon, 'Weapon', errors)
	equipment = id_check(Equipment, equipment, 'Equipment', errors)
	cost = int_check(cost, 'Cost', errors)


	return (errors)

def equip_check_post_errors(data):

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	effect = data['effect']
	feature = data['feature']
	when = data['when']
	skill_type = data['skill_type']
	skill = data['skill']
	check_type = data['check_type']
	action = data['action']
	action_time = data['action_time']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	effect = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	feature = id_check(Feature, feature, 'Feature', errors)
	skill_type = id_check(Skill, skill_type, 'Skill', errors)
	skill = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	check_type = id_check(Check, check_type, 'Check', errors)
	action = id_check(Action, action, 'Action', errors)

	return (errors)

def equip_damaged_post_errors(data):

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	effect = data['effect']
	feature = data['feature']
	damage = data['damage']
	skill_type = data['skill_type']
	skill = data['skill']
	toughness = data['toughness']
	penalty = data['penalty']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	effect = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	feature = id_check(Feature, feature, 'Feature', errors)
	damage = id_check(Descriptor, damage, 'Damage Type', errors)
	skill_type = id_check(Skill, skill_type, 'Skill', errors)
	skill = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	
	toughness = int_check(toughness, 'Toughness', errors)
	


	return (errors)

def equip_descriptor_post_errors(data):


	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	effect = data['effect']
	feature = data['feature']
	descriptor = data['descriptor']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	effect = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	feature = id_check(Feature, feature, 'Feature', errors)
	descriptor = id_check(Descriptor, descriptor, 'Descriptor', errors)



	return (errors)

def equip_effect_post_errors(data):	

	equip_id = data['equip_id']
	name = data['name']
	description = data['description']



	return (errors)

def equip_feature_post_errors(data):

	equip_id = data['equip_id']
	name = data['name']
	description = data['description']


	return (errors)

def equip_limits_post_errors(data):

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	effect = data['effect']
	feature = data['feature']
	time = data['time']
	time_units = data['time_units']
	range = data['range']
	range_units = data['range_units']
	extend = data['extend']
	extendable = data['extendable']
	time_capacity = data['time_capacity']
	time_capacity_units = data['time_capacity_units']
	capacity = data['capacity']
	item = data['item']
	ammo = data['ammo']
	fuel = data['fuel']
	area_long = data['area_long']
	area_wide = data['area_wide']
	area_units = data['area_units']
	recharge = data['recharge']
	refill = data['refill']
	uses = data['uses']
	light = data['light']
	internet = data['internet']
	needs_interneT = data['needs_internet']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	effect = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	feature = id_check(Feature, feature, 'Feature', errors)

	time_units = id_check(Unit, time_units, 'Time Unit Type', errors)
	range_units = id_check(Unit, range_units, 'Range Unit Type', errors)
	time_capacity_units = id_check(Unit, time_capacity_units, 'Time Capacity Unit Type', errors)
	area_units = id_check(Unit, area_units, 'Area Unit Type', errors)
	light = id_check(Light, light, 'Light Type', errors)


	time = int_check(time, 'Time Value', errors)
	range = int_check(range, 'Range Value', errors)
	time_capacity = int_check(time_capacity, 'Time Capacity Value', errors)
	capacity = int_check(capacity, 'Capacity Value', errors)
	area_long = int_check(area_long, 'Area Long Value', errors)
	area_wide = int_check(area_wide, 'Area Wide Value', errors)
	uses = int_check(uses, 'Uses Value', errors)



	return (errors)

def equip_modifiers_post_errors(data):



	return (errors)

def equip_opposed_post_errors(data):


	equip_id = data['equip_id']
	effect = data['effect']
	feature = data['feature']
	dc = data['dc']
	skill_type = data['skill_type']
	skill = data['skill']
	check = data['check']
	when = data['when']
	condition1 = data['condition1']
	condition2 = data['condition2']

	equip_id = id_check(Equipment, equip_id, 'Equipment', errors)
	effect = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	feature = id_check(Feature, feature, 'Feature', errors)

	skill_type = id_check(Skill, skill_type, 'Skill', errors)
	skill = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	check = id_check(Check, check, 'Check Type', errors)

	dc = int_check(dc, 'DC Value', errors)


	return (errors)