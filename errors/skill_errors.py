
from models import Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged 
from models import setup_db, Ability,  ConflictAction, Damage, DamageType, flash
from models import Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense
from models import Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank 
from models import Levels, LevelType

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
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry, name_exist, dependent, either, feature_check, equip_entry_check, equip_check_multiple_fields, required_multiple, weap_entry_check, arm_entry_check, no_zero, head_feature_duplicate


def skill_save_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_ability_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)
s
def skill_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_degree_post_errors(data):

	errors = {'error': False, 'error_msgs': []}



	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}



	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	bonus = data['bonus']
	bonus_type = data['bonus_type']
	penalty = data['penalty']
	penalty_type = data['penalty_type']
	trigger = data['trigger']
	bonus_effect = data['bonus_effect']
	penalty_effect = data['penalty_effect']
	environment = data['environment']
	environment_other = data['environment_other']
	sense = data['sense']
	mod_range = data['mod_range']
	subsense = data['subsense']
	cover = data['cover']
	conceal = data['conceal']
	maneuver = data['maneuver']
	weapon_melee = data['weapon_melee']
	weapon_ranged = data['weapon_ranged']
	tools = data['tools']
	condition = data['condition']
	power = data['power']
	consequence = data['consequence']
	creature = data['creature']
	creature_other = data['creature_other']
	emotion = data['emotion']
	emotion_other = data['emotion_other']
	conflict = data['conflict']
	profession = data['profession']
	profession_other = data['profession_other']
	bonus_trait_type = data['bonus_trait_type']
	bonus_trait = data['bonus_trait']
	bonus_check = data['bonus_check']
	bonus_check_range = data['bonus_check_range']
	bonus_conflict = data['bonus_conflict']
	penalty_trait_type = data['penalty_trait_type']
	penalty_trait = data['penalty_trait']
	penalty_check = data['penalty_check']
	penalty_check_range = data['penalty_check_range']
	penalty_conflict = data['penalty_conflict']
	bonus_active_defense = data['bonus_active_defense']
	bonus_conflict_defend = data['bonus_conflict_defend']
	penalty_active_defense = data['penalty_active_defense']
	penalty_conflict_defend = data['penalty_conflict_defend']
	multiple = data['multiple']
	multiple_count = data['multiple_count']
	lasts = data['lasts']
	skill = data['skill']
	light = data['light']


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = int_check(bonus, 'Bonus', errors)
	errors = int_check(penalty, 'Penalty', errors)
	errors = int_check(multiple_count, 'Multiple Count', errors)
	errors = int_check(lasts, 'Lasts', errors)

	errors = db_insert('Environment', Environment, environment, environment_other, errors)
	errors = db_insert('Emotion', Emotion, emotion, emotion_other, errors)
	errors = db_insert('Creature', Creature, creature, creature_other, errors)
	errors = db_insert('Profession', Job, profession, profession_other, errors)

	errors = db_check(Skill, skill, 'Skill', errors)
	errors = db_check(Light, light, 'Light', errors)
	errors = db_check(Environment, environment, 'Environment', errors)
	errors = db_check(Sense, sense, 'Sense', errors)
	errors = db_check(Ranged, mod_range, 'Range', errors)
	errors = db_check(SubSense, subsense, 'Subsense', errors)
	errors = db_check(Cover, cover, 'Cover', errors)
	errors = db_check(Conceal, conceal, 'Concealment', errors)
	errors = db_check(Maneuver, maneuver, 'Maneuver', errors)
	errors = db_check(WeaponType, weapon_melee, 'Melee Weapon Type', errors)
	errors = db_check(WeaponType, weapon_ranged, 'Ranged Weapon Type', errors)
	errors = db_check(Consequence, consequence, 'Consequence', errors)
	errors = db_check(Creature, creature, 'Creature', errors)
	errors = db_check(Emotion, emotion, 'Emotion', errors)
	errors = db_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = db_check(Job, profession, 'Profession', errors)
	errors = db_check(Check, bonus_check, 'Bonus Check Type', errors)
	errors = db_check(Ranged, bonus_check_range, 'Bonus Check Range', errors)
	errors = db_check(ConflictAction, bonus_conflict, 'Bonus Conflict Action', errors)
	errors = db_check(Check, penalty_check, 'Penalty Check Type', errors)
	errors = db_check(Ranged, penalty_check_range, 'Penalty Check Range', errors)
	errors = db_check(ConflictAction, penalty_conflict, 'Penalty Conflict Action', errors)

	errors = of([bonus, penalty], 'You must set a value for either a bonus or a penalty.', errors)

	errors = if_fields('Bonus', bonus, [bonus_type, bonus_effect], errors)
	errors = if_field('Bonus', bonus, bonus_type, 'Bonus Type', errors)
	errors = if_field('Bonus', bonus, bonus_effect, 'Bonus Effect', errors)
	errors = if_fields('Penalty', penalty, [penalty_type, penalty_effect], errors)
	errors = if_field('Penalty', penalty, penalty_type, 'Penalty Type', errors)
	errors = if_field('Penalty', penalty, penalty_effect, 'Penalty Effect', errors)

	errors = variable_fields('trait', 'Bonus Trait', bonus_effect, [bonus_trait_type, bonus_trait], errors)
	errors = variable_fields('check', 'Bonus Check', bonus_effect, [bonus_check], errors)
	errors = variable_fields('conflict', 'Bonus Conflict Action', bonus_effect, [bonus_conflict], errors)

	errors = variable_fields('trait', 'Penalty Trait', penalty_effect, [penalty_trait_type, penalty_trait], errors)
	errors = variable_fields('check', 'Penalty Check', penalty_effect, [penalty_check], errors)
	errors = variable_fields('conflict', 'Penalty Conflict Action', penalty_effect, [penalty_conflict], errors)

	errors = variable_fields('environment', 'Environment', trigger, [environment], errors)
	errors = variable_fields('cover', 'Cover', trigger, [cover], errors)
	errors = variable_fields('conceal', 'Concealment', trigger, [conceal], errors)
	errors = variable_fields('sense', 'Sense', trigger, [sense], errors)
	errors = variable_fields('subsense', 'Subsense', trigger, [subsense], errors)
	errors = variable_fields('condition', 'Condition', trigger, [condition], errors)
	errors = variable_fields('profession', 'Characters Profession', trigger, [profession], errors)
	errors = variable_fields('creature', 'Creature', trigger, [creature], errors)
	errors = variable_fields('power', 'Power', trigger, [power], errors)
	errors = variable_fields('emotion', 'Emotion', trigger, [emotion], errors)
	errors = variable_fields('consequence', 'Consequence', trigger, [consequence], errors)
	errors = variable_fields('range', 'Range', trigger, [mod_range], errors)
	errors = variable_fields('conflict', 'Conflict Action', trigger, [conflict], errors)
	errors = variable_fields('maneuver', 'Maneuver', trigger, [maneuver], errors)
	errors = variable_fields('tools', 'Tool Requirement', trigger, [tools], errors)
	errors = variable_fields('ranged', 'Ranged Weapon', trigger, [weapon_ranged], errors)
	errors = variable_fields('melee', 'Melee Weapon', trigger, [weapon_melee], errors)
	errors = variable_fields('skill', 'Skill', trigger, [skill], errors)
	errors = variable_fields('light', 'Light', trigger, [light], errors)

	return (errors)

def skill_levels_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	level_type = data['level_type']
	level = data['level']
	level_effect = data['level_effect']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = required(level_type, 'Level Type', errors)
	errors = required(level, 'Level', errors)
	errors = required(level_effect, 'Level Effect', errors)
	

	return (errors)
