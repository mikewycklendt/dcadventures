
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

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check, arm_entry_check, no_zero


def veh_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	vehicle_id = data['vehicle_id']
	description = data['description']
	type_id = data['type_id']
	size = data['size']
	strength = data['strength']
	speed = data['speed']
	toughness = data['toughness']
	defense = data['defense']
	cost = data['cost']
	feature = data['feature']
	power = data['power']

	create_check('vehicle Name', vehicle_id, Vehicle, errors)

	errors = id_check(Vehicle, vehicle_id, 'Vehicle', errors)
	errors = id_check(VehicleType, type_id, 'Vehicle Type', errors)
	errors = id_check(VehicleSize, size, 'Vehicle Size', errors)

	errors = int_check(type_id, 'Vehicle Type', errors)
	errors = int_check(size, 'Vehicle Size', errors)
	errors = int_check(strength, 'Strength', errors)
	errors = int_check(speed, 'Speed', errors)
	errors = int_check(toughness, 'Toughness', errors)
	errors = int_check(defense, 'Defense', errors)
	errors = int_check(cost, 'Cost', errors)

	errors = required(type_id, 'Vehicle Type', errors)
	errors = required(size, 'Vehicle Size', errors)

	errors = no_zero(cost, 'Cost', errors)
	
	return (errors)



def veh_feature_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	vehicle_id = data['vehicle_id']
	feature = data['feature']
	cost = data['cost']
	equipment = data['equipment']
	weapon = data['weapon']

	create_check('vehicle Name', vehicle_id, Vehicle, errors)

	errors = id_check(Vehicle, vehicle_id, 'Vehicle', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)
	errors = id_check(Weapon, weapon, 'Weapon', errors)
	
	errors = of([feature, weapon, equipment], 'You must choose a weapon, feature or equipment to add to the vehicle', errors)

	return (errors)


def veh_powers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	vehicle_id = data['vehicle_id']
	cost = data['cost']
	ranks  = data['ranks']
	power = data['power']

	create_check('vehicle Name', vehicle_id, Vehicle, errors)

	errors = id_check(Vehicle, vehicle_id, 'Vehicle', errors)
	errors = id_check(Power, power, 'Power', errors)

	errors = no_zero(cost, 'Cost', errors)
	errors = no_zero(ranks, 'Ranks', errors)

	return (errors)