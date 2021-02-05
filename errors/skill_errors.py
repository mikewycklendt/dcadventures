
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


	skill_id skill_id

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_ability_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	ability = data['ability']
	circumstance = data['circumstance']

	errors = id_check(Ability, ability, 'Ability', errors)

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	check_type = data['check_type']
	mod = data['mod']
	circumstance = data['circumstance']
	trigger = data['trigger']
	when = data['when']
	trait_type = data['trait_type']
	trait = data['trait']
	conflict = data['conflict']
	conflict_range = data['conflict_range']
	conflict_weapon = data['conflict_weapon']
	condition1 = data['condition1']
	condition2 = data['condition2']
	action_type = data['action_type']
	action = data['action']
	free = data['free']
	
	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)	
	errors = id_check(Check, check_type, 'Check', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = id_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = id_check(Ranged, conflict_range, 'Conflict Range', errors)
	errors = int_check(action, 'Action', errors)

	
	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]



	return (errors)

def skill_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	circ_target = data['circ_target']
	mod = data['mod']
	effect = data['effect']
	speed = data['speed']
	temp = data['temp']
	target = data['target']
	level_type = data['level_type']
	level = data['level']
	time = data['time']
	condition_type = data['condition_type']
	condition1 = data['condition1']
	condition2 = data['condition2']
	conditions = data['conditions']
	conditions_effect = data['conditions_effect']
	measure_effect = data['measure_effect']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	keyword = data['keyword']
	cumulative = data['cumulative']
	optional = data['optional']
	lasts = data['lasts']
	turns = data['turns']
	unit_time = data['unit_time']
	time_units = data['time_units']
	time_rank = data['time_rank']
	circumstance = data['circumstance']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(speed, 'Speed', errors)
	errors = int_check(temp, 'Temporary Turns', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(time, 'Time Value', errors)
	errors = int_check(conditions, 'Condition Degree', errors)
	errors = int_check(conditions_effect, 'Condition Effect', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Unit', errors)
	errors = id_check(Math, measure_trait_math, 'Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(turns, 'Turns', errors)
	errors = int_check(unit_time, 'Time Value', errors)
	errors = id_check(Unit, time_units, 'Time Units', errors)
	errors = int_check(time_rank, 'Time Rank', errors)


	circ_effect_select = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'temp', 'name': 'Effect Temporary'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]

	lasts = [{'type': '', 'name': 'Lasts'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'time', 'name': 'Time'}, {'type': 'rank', 'name': 'Time Rank'}]



	return (errors)

def skill_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	target = data['target']
	dc = data['dc']
	description = data['description']
	value = data['value']
	mod = data['mod']
	math_value = data['math_value']
	math = data['math']
	math_trait_type = data['math_trait_type']
	math_trait = data['math_trait']
	condition = data['condition']
	keyword_check = data['keyword_check']
	levels = data['levels']
	damage = data['damage']
	cover = data['cover']
	complex = data['complex']
	measure = data['measure']
	change_action = data['change_action']
	conceal = data['conceal']
	action = data['action']
	action_when = data['action_when']
	damage_type = data['damage_type']
	inflict_type = data['inflict_type']
	inflict_flat = data['inflict_flat']
	inflict_trait_type= data[' inflict_trait_type']
	inflict_trait = data['inflict_trait']
	inflict_math = data['inflict_math']
	inflict_mod = data['inflict_mod']
	inflict_bonus = data['inflict_bonus']
	damage_mod = data['damage_mod']
	damage_consequence = data['damage_consequence']
	measure_effect = data['measure_effect']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	level_type = data['level_type']
	level = data['level']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	keyword = data['keyword']
	complexity = data['complexity']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(value, 'DC', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(math_value, 'Math Value', errors)
	errors = id_check(Math, math, 'Math', errors)
	errors = id_check(Action, action, 'Action', errors)
	errors = int_check(inflict_flat, 'Infllict Damage Value', errors)
	errors = id_check(Math, inflict_math, 'Math', errors)
	errors = int_check(inflict_mod, 'Inflict Damage Modifier', errors)
	errors = int_check(inflict_bonus, 'Inflict Damage Bonus', errors)
	errors = int_check(damage_mod, 'Damage Modifier', errors)
	errors = id_check(Consequence, damage_consequence, 'Consequence Damage Modifier', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Vslue', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Unit Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Unit', errors)
	errors = id_check(Math, measure_trait_math, 'MeaSurement Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(condition_turns, 'Condition Turns', errors)
	errors = id_check(Complex, complexity, 'Complexity', errors)



	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'choice', 'name': 'Chosen by Player'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]






	return (errors)

def skill_degree_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	target = data['target']
	value = data['value']
	type = data['type']
	action = data['action']
	time = data['time']
	recovery = data['recovery']
	damage_type = data['damage_type']
	object = data['object']
	object_effect = data['object_effect']
	inflict_type = data['inflict_type']
	inflict_flat = data['inflict_flat']
	inflict_trait_type = data['inflict_trait_type']
	inflict_trait = data['inflict_trait']
	inflict_math = data['inflict_math']
	inflict_mod = data['inflict_mod']
	inflict_bonus = data['inflict_bonus']
	damage_mod = data['damage_mod']
	damage_consequence = data['damage_consequence']
	consequence_action_type = data['consequence_action_type']
	consequence_action = data['consequence_action']
	consequence_trait_type = data['consequence_trait_type']
	consequence_trait = data['consequence_trait']
	consequence = data['consequence']
	knowledge = data['knowledge']
	knowledge_count = data['knowledge_count']
	knowledge_specificity = data['knowledge_specificity']
	level_type = data['level_type']
	level = data['level']
	level_direction = data['level_direction']
	circumstance = data['circumstance']
	circ_target = data['circ_target']
	measure_effect = data['measure_effect']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(value, 'Degree Value', errors)
	errors = id_check(Action, action, 'Action', errors)
	errors = int_check(time, 'Time Value', errors)
	errors = int_check(object, 'Object Damage', errors)
	errors = int_check(inflict_flat, 'Inflict Damage Value', errors)
	errors = id_check(Math, inflict_math, 'Inflict Damage Math', errors)
	errors = int_check(inflict_mod, 'Inflict Damage Modifier', errors)
	errors = int_check(inflict_bonus, 'Inflict Damage Bonus', errors)
	errors = int_check(damage_mod, 'Damage Modifier', errors)
	errors = id_check(Consequence, damage_consequence, 'Consequence', errors)
	errors = int_check(consequence_action, 'Consequence Action', errors)
	errors = id_check(Consequence, consequence, 'Consequence', errors)
	errors = int_check(knowledge_count, 'Knowledge Count', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(level_direction, 'Level Change', errors)
	errors = id_check(SkillCirc, circumstance, 'Circumstance Modifier Keyword', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Unit Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Units', errors)
	errors = id_check(Math, measure_trait_math, 'Measurement Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(condition_damage_value, 'Condition Degrees', errors)
	errors = int_check(condition_damage, 'Condition Damage', errors)
	errors = int_check(condition_turns, 'Condition Turns', errors)
	errors = int_check(nullify, 'Nullify DC', errors)
	

	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]



	return (errors)

def skill_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	attached = data['attached']
	frequency = data['frequency']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	opponent_trait_type = data['opponent_trait_type']
	opponent_trait = data['opponent_trait']
	opponent_mod = data['opponent_mod']
	player_check = data['player_check']
	opponent_check = data['opponent_check']
	secret = data['secret']
	recurring = data['recurring']
	multiple = data['multiple']
	recurring_value = data['recurring_value']
	recurring_units = data['recurring_units']

	errors = int_check(mod, 'Player Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)
	errors = id_check(Check, player_check, 'Player Check', errors)
	errors = id_check(Check, opponent_check, 'Opponent Check', errors)
	errors = int_check(recurring_value, 'Recurring Value', errors)
	errors = id_check(Unit, recurring_units, 'Recurring Units', errors)




	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)


	return (errors)

def skill_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	type = data['type']
	value_type = data['value_type']
	rank1 = data['rank1']
	rank1_value = data['rank1_value']
	rank_math = data['rank_math']
	rank2 = data['rank2']
	rank2_value = data['rank2_value']
	value = data['value']
	units = data['units']
	trait_type = data['trait_type']
	trait = data['trait']
	math = data['math']
	math_value = data['math_value']
	recovery = data['recovery']
	recovery_penalty = data['recovery_penalty']
	recovery_time = data['recovery_time']
	recovery_incurable = data['recovery_incurable']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)	
	errors = id_check(Rank, rank1, 'First Rank', errors)
	errors = int_check(rank1_value, 'First Rank Value', errors)
	errors = id_check(Math, rank_math, 'Rank Math', errors)
	errors = id_check(Rank, rank2, 'Second Rank', errors)
	errors = int_check(rank2_value, 'Second Rank Value', errors)
	errors = int_check(value, 'Time Value', errors)
	errors = id_check(Unit, units, 'Units', errors)
	errors = id_check(Math, math, 'Msth', errors)
	errors = int_check(math_value, 'Time Math Value', errors)
	errors = int_check(recovery_penalty, 'Recovery Penalty Modifier', errors)
	errors = int_check(recovery_time, 'Recovery Time', errors)
	


	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Measurement'}, {'type': 'gm', 'name': 'Set by GM'}]


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
