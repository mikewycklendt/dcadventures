
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check, arm_entry_check


def arm_save_errors(data):

	errors = {'error': False, 'error_msgs': []}
	armor_id = data['armor_id']
	description = data['description']
	type_id = data['type_id']
	cost = data['cost']
	material = data['material']
	toughness = data['toughness']
	active = data['active']
	subtle = data['subtle']
	perception = data['perception']
	impervious = data['impervious']
	defense = data['defense']
	descriptor = data['descriptor']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(ArmorType, type_id, 'Armor Type', errors)
	errors = int_check(cost, 'Cost', errors)
	errors = id_check(Material, material, 'Material', errors)
	errors = int_check(toughness, 'Toughness Bonus', errors)
	errors = int_check(active, 'Active Defense Bonus', errors)
	errors = int_check(perception, 'Perception DC', errors)

	errors = required(type_id, 'Armor Type', errors)
	errors = required(cost, 'Cost', errors)
	errors = required(material, 'Msterial', errors)
	errors = of([toughness, active, defense], 'You must set a toughness bonus, active defense bonus or at least one defense bonus', errors)

	arm_entry_check('Armor Descriptors', ArmDescriptor, descriptor, armor_id, errors)
	arm_entry_check('Defense Bonus', ArmDefense, defense, armor_id, errors)

	return (errors)

def arm_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	armor_id = data['armor_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	descriptor = data['descriptor']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)

	return (errors)
	
def arm_defense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	armor_id = data['armor_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	defense = data['defense']
	bonus = data['bonus']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(Defense, defense, 'Defense', errors)

	errors = required(defense, 'Defense', errors)
	errors = required(bonus, 'Bonus', errors)

	return (errors)
