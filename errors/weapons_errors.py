
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_table import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from functions.create.weapon_create import weap_entry_check

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check

def weap_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	cat_id = data['cat_id']
	type_id = data['type_id']
	cost = data['cost']
	description = data['description']
	critical = data['critical']
	damage = data['damage']
	toughness = data['toughness']
	material = data['material']
	length = data['length']
	length_units = data['length_units']
	resist_dc = data['resist_dc']
	resistance = data['resistance']
	power_rank = data['power_rank']
	power = data['power']
	hands = data['hands']
	strength = data['strength']
	thrown = data['thrown']
	unarmed = data['unarmed']
	reach = data['reach']
	ranged_attack_bonus = data['ranged_attack_bonus']
	protect = data['protect']
	ranged_area = data['ranged_area']
	ranged_burst = data['ranged_burst']
	ranged_area_damage = data['ranged_area_damage']
	penetrate = data['penetrate']
	attack_bonus = data['attack_bonus']
	subtle = data['subtle']
	perception_dc = data['perception_dc']
	advantage = data['advantage']
	grenade_area = data['grenade_area']
	grenade_burst = data['grenade_burst']
	grenade_area_damage = data['grenade_area_damage']
	conceal = data['conceal']
	sense = data['sense']
	double = data['double']
	double_mod = data['double_mod']
	benefit = data['benefit']
	condition = data['condition']
	descriptor = data['descriptor']

	errors = create_check('Weapon Name', weapon_id, Weapon, errors)

	errors = id_check(Weapon, weapon_id, 'Weapon', errors)

	errors = id_check(WeaponCat, cat_id, 'Weapon Category', errors)
	errors = id_check(WeaponType, type_id, 'Weapon Type', errors)
	errors = int_check(cost, 'Cost', errors)
	errors = int_check(critical, 'Critical Hit', errors)
	errors = int_check(damage, 'Damage', errors)
	errors = int_check(toughness, 'Toughness', errors)
	errors = id_check(Material, material, 'Material', errors)
	errors = int_check(length, 'Length', errors)
	errors = id_check(Unit, length_units, 'Length Units', errors)
	errors = int_check(resist_dc, 'Resistance DC', errors)
	errors = id_check(Defense, resistance, 'Resistance Defense', errors)
	errors = int_check(power_rank, 'Power Rank', errors)
	errors = int_check(hands, 'Held With', errors)
	errors = int_check(reach, 'Reach', errors)
	errors = int_check(ranged_attack_bonus, 'Attack Bonus', errors)
	errors = int_check(protect, 'Protection Modifier', errors)
	errors = int_check(ranged_burst, 'Burst Rank', errors)
	errors = int_check(ranged_area_damage, 'Area Damage', errors)
	errors = int_check(attack_bonus, 'Attack Bonus', errors)
	errors = int_check(perception_dc, 'Perception DC', errors)
	errors = int_check(grenade_burst, 'Burst Rank', errors)
	errors = int_check(grenade_area_damage, 'Area Damage', errors)
	errors = id_check(Conceal, conceal, 'Concealment', errors)
	errors = id_check(Sense, sense, 'Sense', errors)
	errors = int_check(double_mod, 'Doubling Modifier', errors)

	errors = required(cat_id, 'Weapon Category', errors)
	errors = required(type_id, 'Weapon Type', errors)
	errors = required(cost, 'Weapon Cost', errors)
	errors = required(description, 'Description', errors)
	errors = required_multiple(damage, ['1', '2', '3'], cat_id, 'Damage', errors)
	errors = required_multiple(toughness, ['1', '2', '3'], cat_id, 'Toughness', errors)
	errors = required_multiple(material, ['1'], cat_id, 'Material', errors)
	errors = required_multiple(length, ['1', '2'], cat_id, 'Length', errors)
	errors = together('a Ranged Weapon or Melee Weapon', [length, length_units], errors)
	errors = required_multiple(hands, ['1', '2'], cat_id, 'Held With', errors)
	errors = variable_fields('burst', 'Burst Area Effect', ranged_area, [ranged_burst], errors)
	errors = variable_field('burst', ranged_area, 'Burst Rank', ranged_burst, errors)
	errors = together_names('Area Effect', ['Area Effect', 'Area Damage'], [ranged_area, ranged_area_damage], errors)
	errors = variable_fields('burst', 'Burst Area Effect', grenade_area, [grenade_burst], errors)
	errors = variable_field('burst', grenade_area, 'Burst Rank', grenade_burst, errors)
	errors = together_names('Area Effect', ['Area Effect', 'Area Damage'], [grenade_area, grenade_area_damage], errors)
	errors = check_field(double, 'Doubling Effect', 'Damage Per x2', double_mod, errors)
	
	weap_entry_check('Conditions', WeapCondition, condition, weapon_id, errors)
	weap_entry_check('Benefits', WeapBenefit, benefit, weapon_id, errors)
	weap_entry_check('Effect Descriptors', WeapDescriptor, descriptor, weapon_id, errors)

	return (errors)

def weap_condition_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	condition_type = data['condition_type']
	condition = data['condition']
	condition_null = data['condition_null']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage_value = data['damage_value']
	damage = data['damage']

	errors = create_check('Weapon', weapon_id, Weapon, errors)
	
	errors = id_check(Weapon, weapon_id, 'Weapon', errors)

	errors = int_check(damage_value, 'Condition Damage', errors)
	errors = int_check(damage, 'Damage Direction', errors)

	errors = db_check(Weapon, weapon_id, 'Weapon', errors)

	errors = required(condition_type, 'Condition Type', errors)

	errors = variable_fields('active', 'Active Condition', condition_type, [condition], errors)
	errors = variable_field('active', condition_type, 'Condition', condition, errors)
	errors = variable_fields('change', 'CondItion Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('change', condition_type, 'Starting CondItion', condition1, errors)
	errors = variable_field('change', condition_type, 'Ending CondItion', condition2, errors)
	errors = variable_fields('damage', 'Condition Damage', condition_type, [damage_value, damage], errors)
	errors = variable_field('damage', condition_type, 'Damage Degrees', damage_value, errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Direction ', damage, errors)
	errors = variable_fields('null', 'Nullify Condition', condition_type, [condition_null], errors)
	errors = variable_field('null', condition_type, 'Nullified Condition', condition_null, errors)


	return(errors)

def weap_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	descriptor = data['descriptor']

	errors = create_check('Weapon', weapon_id, Weapon, errors)

	errors = id_check(Weapon, weapon_id, 'Weapon', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)

	return (errors)

def weap_benefit_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']

	errors = create_check('Weapon', weapon_id, Weapon, errors)

	errors = id_check(Weapon, weapon_id, 'Weapon', errors)
	errors = id_check(Benefit, benefit, 'Benefit', errors)

	errors = required(benefit, 'Benefit', errors)

	return (errors)
