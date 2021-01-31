
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
from models import WeapBenefit, WeapCondition, WeapDescriptor
from models import Armor, ArmorType, ArmDescriptor, ArmDefense
from models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature
from models import Headquarters, HeadFeature, HeadFeatAddon, HeadSize, HeadCharFeat

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check, arm_entry_check, no_zero

def head_save_errors(data):

	errors = {'error': False, 'error_msgs': []}



	return (errors)

def head_addon_post_errors(data):
	
	errors = {'error': False, 'error_msgs': []}

	head_id = data['head_id']
	head_feature = data['head_feature']
	feature = data['feature']
	equipment = data['equipment']
	weapon = data['weapon']

	create_check('HHeadquarters Name', head_id, Headquarters, errors)

	errors = id_check(Headquarters, head_id, 'Headquarters', errors)
	errors = id_check(HeadFeature, head_feature, 'Headquarters', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)
	errors = id_check(Weapon, weapon, 'Weapon', errors)

	errors = required(head_feature, 'Headquarters Feature', errors)
	errors = of([feature, weapon, equipment], 'You must choose a weapon, feature or equipment to add to the vehicle', errors)

	return (errors)


def head_feature_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	head_id = data['head_id']
	name = data['name']
	description = data['description']
	feature = data['feature']

	errors = of([feature, name], 'You must create a new feature or select an existing one.', errors)
	errors = either([feature, name], 'You must add a new feature and and existing feature seperately.', errors)
	errors = dependent('New Feature', name, [description], errors)

	if name != '':
		errors = name_exist('Headquarters Feature', HeadFeature, name, errors)

	return (errors)