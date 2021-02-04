from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature

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