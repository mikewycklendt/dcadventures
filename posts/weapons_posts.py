
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from create_functions.weapon_create import weap_entry_check

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()


def weap_condition_post(entry, body, cells):

	weapon_id = entry.weapon_id
	condition_type = entry.condition_type
	condition = entry.condition
	condition_null = entry.condition_null
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage_value = entry.damage_value
	damage = entry.damage

	condition = get_name(Condition, condition)
	condition_null = get_name(Condition, condition_null)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

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

	benefit = name(Benefit, benefit)
	
	cells = cell('Benefit', 25, [benefit], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)
