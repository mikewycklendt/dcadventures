
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

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check, arm_entry_check, no_zero, head_feature_duplicate

def head_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	head_id = data['head_id']
	description = data['description']
	size = data['size']
	toughness = data['toughness']
	cost = data['cost']
	shared = data['shared']
	addon = data['addon']
	feature = data['feature']

	create_check('HHeadquarters Name', head_id, Headquarters, errors)

	errors = id_check(Headquarters, head_id, 'Headquarters', errors)

	errors = required(size, 'Size', errors)

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
	errors = id_check(HeadFeature, head_feature, 'Headquarters Feature', errors)
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

	create_check('HHeadquarters Name', head_id, Headquarters, errors)

	errors = id_check(Headquarters, head_id, 'Headquarters', errors)
	errors = id_check(HeadFeature, feature, 'Headquarters Feature', errors)

	errors = of([feature, name], 'You must create a new feature or select an existing one.', errors)
	errors = either([feature, name], 'You must add a new feature and and existing feature seperately.', errors)
	errors = dependent('New Feature', name, [description], errors)
	errors = head_feature_duplicate(feature, head_id, HeadCharFeat, errors)

	if name != '':
		errors = name_exist('Headquarters Feature', HeadFeature, name, errors)

	return (errors)