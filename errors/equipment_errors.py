
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType, Communication
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from create_functions.equipment_create import equip_entry_check, unsaved, equip_create_check, equip_check_multiple_fields, feature_check

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def feature_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	type_id = data['type_id']
	cost = data['cost']
	description = data['description']
	toughness = data['toughness']
	expertise = data['expertise']
	alternate = data['alternate']
	move = data['move']
	speed_mod = data['speed_mod']
	direction = data['direction']
	locks = data['locks']
	lock_type = data['lock_type']

	fields = [{'val': type_id, 'name': 'Equipment Type'},
		{'val': cost, 'name': 'Cost'},
		{'val': description, 'name': 'Equipment Descriptiomn'},
		{'val': toughness, 'name': 'Toughness'},
		{'val': expertise, 'name': 'Expertise'},
		{'val': speed_mod, 'name': 'Speed Modifier'},
		{'val': direction, 'name': 'Movement Direction'},
		{'val': locks, 'name': 'Locks'},
		{'val': lock_type, 'name': 'Lock Type'}]
	
	errors = unsaved(fields, equip_id, errors)

	return (errors)

def equip_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	type_id = data['type_id']
	cost = data['cost']
	description = data['description']
	toughness = data['toughness']
	expertise = data['expertise']
	alternate = data['alternate']
	move = data['move']
	speed_mod = data['speed_mod']
	direction = data['direction']
	locks = data['locks']
	lock_type = data['lock_type']
	mod_multiple = data['mod_multiple']
	mod_multiple_count = data['mod_multiple_count']
	check = data['check']
	damaged = data['damaged']
	descriptor = data['descriptor']
	feature = data['feature']
	limits = data['limits']
	modifiers = data['modifiers']
	opposed = data['opposed']

	errors = create_check('Equipment', equip_id, Equipment, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	

	errors = check_fields(move, 'Movement Effect', [speed_mod, direction], errors)
	errors = check_field(move, 'Movement Effect', 'Speed Rank Modifier', speed_mod, errors)
	errors = check_field(move, 'Movement Effect', 'Direction', direction, errors)

	errors = check_field(locks, 'Opens Locks', 'Lock Type', lock_type, errors)

	errors = equip_check_multiple_fields('Bonus/Penalty Modifier', EquipMod, [mod_multiple, mod_multiple_count], equip_id, errors)

	errors = feature_check(equip_id, errors)

	errors = equip_entry_check('Add Feature', Feature, feature, equip_id, errors)
	errors = equip_entry_check('Bonus/Penalty Modifier', EquipMod, modifiers, equip_id, errors)
	errors = equip_entry_check('Check', EquipCheck, check, equip_id, errors)
	errors = equip_entry_check('Opposing Check', EquipOpposed, opposed, equip_id, errors)
	errors = equip_entry_check('Limits', EquipLimit, limits, equip_id, errors)
	errors = equip_entry_check('Damaged', EquipDamage, damaged, equip_id, errors)
	errors = equip_entry_check('Counters Descriptor', EquipDescriptor, descriptor, equip_id, errors)
	errors = equip_entry_check('Alternate Effect', EquipEffect, alternate, equip_id, errors)	

	return (errors)

def equip_belt_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	feature = data['feature']
	weapon = data['weapon']
	equipment = data['equipment']

	create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Weapon, weapon, 'Weapon', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)

	errors = of([feature, weapon, equipment], 'You must choose a weapon, feature or equipment to add to the belt', errors)


	return (errors)

def equip_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = equip_create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Skill, skill_type, 'Skill', errors)
	errors = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	errors = id_check(Check, check_type, 'Check', errors)
	errors = id_check(Action, action, 'Action', errors)

	errors = required(when, 'When', errors)
	errors = required(check_type, 'Check Type', errors)
	errors = required(action, 'Action Type', errors)

	return (errors)

def equip_damaged_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = equip_create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Descriptor, damage, 'Damage Type', errors)
	errors = id_check(Skill, skill_type, 'Skill', errors)
	errors = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	
	errors = int_check(toughness, 'Toughness', errors)

	errors = of([damage, skill_type, skill, toughness, penalty], 'You must set ar least one rule for the damaged effect.', errors)
	errors = together_names('a Feature', ['Toughness'], [toughness], errors)


	return (errors)

def equip_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	effect = data['effect']
	feature = data['feature']
	descriptor = data['descriptor']

	errors = equip_create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	errors = id_check(Feature, feature, 'Feature', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)



	return (errors)

def equip_effect_post_errors(data):	

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	name = data['name']
	description = data['description']

	create_check('Equipment Name', equip_id, Equipment, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)

	errors = required(name, 'Name', errors)
	description = required(description, 'Description', errors)
	
	return (errors)

def equip_feature_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	name = data['name']
	description = data['description']
	feature = data['feature']

	errors = id_check(Feature, feature, 'Feature', errors)

	errors = of([feature, name], 'You must create a new feature or select an existing one.', errors)
	errors = either([feature, name], 'You must add a new feature and and existing feature seperately.', errors)
	errors = dependent('New Feature', name, [description], errors)

	if name != '':
		errors = name_exist('Feature', Feature, name, errors)

	return (errors)

def equip_limits_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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
	needs_internet = data['needs_internet']

	errors = equip_create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	errors = id_check(Feature, feature, 'Feature', errors)

	errors = id_check(Unit, time_units, 'Time Unit Type', errors)
	errors = id_check(Unit, range_units, 'Range Unit Type', errors)
	errors = id_check(Unit, time_capacity_units, 'Time Capacity Unit Type', errors)
	errors = id_check(Unit, area_units, 'Area Unit Type', errors)
	errors = id_check(Light, light, 'Light Type', errors)

	errors = int_check(time, 'Time Value', errors)
	errors = int_check(range, 'Range Value', errors)
	errors = int_check(time_capacity, 'Time Capacity Value', errors)
	errors = int_check(capacity, 'Capacity Value', errors)
	errors = int_check(area_long, 'Area Long Value', errors)
	errors = int_check(area_wide, 'Area Wide Value', errors)
	errors = int_check(uses, 'Uses Value', errors)

	errors = together('Duration', [time, time_units], errors)
	errors = together('Range', [range, range_units], errors)
	errors = together('Time Capacity', [time_capacity, time_capacity_units], errors)
	errors = together('Capacity', [capacity, item], errors)
	errors = together('Area Effect', [area_long, area_wide, area_units], errors)
	errors = of([time, range, time_capacity, capacity, extend, extendable, ammo, fuel, area_long, recharge, refill, uses, light, internet, needs_internet], 'You must specify at least one limit', errors)




	return (errors)

def equip_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	equip_id = data['equip_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	feature = data['feature']
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
	effect = data['effect']
	feature = data['feature']

	errors = equip_create_check(equip_id, feature, errors)
	
	errors = id_check(Equipment, equip_id, 'Equipment', errors)

	errors = int_check(bonus, 'Bonus', errors)
	errors = int_check(penalty, 'Penalty', errors)
	errors = int_check(multiple_count, 'Multiple Count', errors)
	errors = int_check(lasts, 'Lasts', errors)

	errors = db_insert('Environment', Environment, environment, environment_other, errors)
	errors = db_insert('Emotion', Emotion, emotion, emotion_other, errors)
	errors = db_insert('Creature', Creature, creature, creature_other, errors)
	errors = db_insert('Profession', Job, profession, profession_other, errors)

	errors = db_check(Feature, feature, 'Feature', errors)
	errors = db_check(EquipEffect, effect, 'Alternate Effect', errors)
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

def equip_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = equip_create_check(equip_id, feature, errors)

	errors = id_check(Equipment, equip_id, 'Equipment', errors)
	errors = id_check(EquipEffect, effect, 'Alternate Effect', errors)
	errors = id_check(Feature, feature, 'Feature', errors)

	errors = id_check(Skill, skill_type, 'Skill', errors)
	errors = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	errors = id_check(Check, check, 'Check Type', errors)

	errors = int_check(dc, 'DC Value', errors)

	errors = required(skill_type, 'Skill', errors)
	errors = required(check, 'Check Type', errors)
	errors = required(when, 'When', errors)

	return (errors)