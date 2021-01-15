
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer


def adv_alt_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
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

	errors = int_check(mod, 'Modifier', errprs)
	errors = int_check(action, 'Action', errprs)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Check, check_type, 'Check Type', errors)
	errors = db_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = db_check(Ranged, conflict_range, 'Range', errors)

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]


	errors = required(check_type, 'Check Type', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(when, 'When', errors)
	errors = required(action_type, 'Action Type', errors)
	errors = required(action, 'Action', errors)

	errors = variable_fields('condition', 'Triggered by Condition', trigger, [condition1, condition2], errors)
	errors = variable_field('condition', trigger, 'Starting Condition', ondition1, errors)
	errors = variable_field('condition', trigger, 'Ending Condition', ondition2, errors)

 	errors = variable_fields('conflict', 'Triggered by Conflict Action', trigger, [conflict], errors)
 	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)

``

	return(errors)

def adv_benefit_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	name = data['name']
	description = data['description']
	effort = data['effort']

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	errors = required(name, 'Name', errors)
	errors = required(description, 'Description')

	return(errors)

def adv_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	mod = data['mod']
	rounds = data['rounds']
	circumstance = data['circumstance']
	circ_type = data['circ_type']
	circ_range = data['circ_range']
	conflict = data['conflict']
	check_who = data['check_who']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	null_type = data['null_type']
	null_condition = data['null_condition']
	null_trait_type = data['null_trait_type']
	null_trait = data['null_trait']
	null_override_trait_type = data['null_override_trait_type']
	null_override_trait = data['null_override_trait']
	
	errors = int_check(mod, 'Modifier', errprs)
	errors = int_check(rounds, 'Rounds', errprs)
	errors = int_check(ranks, 'Ranks', errprs)
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Range, circ_range, 'Range', errors)
	errors = db_check(ConflictAction, conflict, 'Conflict Action', errors)
	
	errors = required(target, 'Target', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Lasts', errors)
	errors = required(circumstance, 'Circumstance', errors)
	
	errors = variable_fields('range', 'Triggered by Range', circ_type, [circ_range], errors)
	errors = variable_field('range', circ_type, 'Range', circ_range, errors)
	errors = variable_fields('check', 'Triggered by Check Type', circ_type, [check_who, check_trait_type, check_trait], errors)
	errors = variable_field('check', circ_type, 'Whose Check', check_who, errors)
	errors = variable_field('check', circ_type, 'Trait Type', check_trait_type, errors)
	errors = variable_field('check', circ_type, 'Trait', check_trait, errors)
	errors = variable_fields('conflict', 'Triggered by Conflict Action', circ_type, [conflict], errors)
	errors = variable_field('conflict', circ_type, 'Conflict Action', conflict, errors)

	return(errors)

def adv_combined_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	ranks = data['ranks']
	advantage = data['advantage']

	errors = int_check(ranks, 'Ranks', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	return(errors)


def adv_condition_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	benefit = data['benefit']
	condition_type = data['condition_type']
	condition = data['condition']
	condition_null = data['condition_null']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage_value = data['damage_value']
	damage = data['damage']

	errors = int_check(damage_value, 'Condition Damage', errprs)
	errors = int_check(damage, 'Damage Direction', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

	return(errors)

def adv_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	dc = data['dc']
	description = data['description']
	value_value = data['value_value']
	math_value = data['math_value']
	math_math = data['math_math']
	math_trait_type = data['math_trait_type']
	math_trait = data['math_trait']
	condition = data['condition']
	keyword_check = data['keyword_check']
	check_type = data['check_type']
	levels = data['levels']
	level_type = data['level_type']
	level = data['level']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_mod = data['check_mod']

	errors = int_check(dc, 'DC', errprs)
	errors = int_check(math_value, 'Math Value', errprs)
	errors = int_check(check_mod, 'Check Modifier', errprs)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Math, math_math, 'Math', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)


	return(errors)

def adv_deg_mod_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	value = data['value']
	deg_mod_type = data['deg_mod_type']
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
	circ_value = data['circ_value']
	circ_turns = data['circ_turns']
	circ_trait_type = data['circ_trait_type']
	circ_trait = data['circ_trait']
	measure_type = data['measure_type']
	measure_val1 = data['measure_val1']
	measure_math = data['measure_math']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_value = data['measure_value']
	measure_rank = data['measure_rank']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']

	errors = int_check(value, 'Circumstance Modifier', errprs)
	errors = int_check(consequence_action, 'Consequence Action', errprs)
	errors = int_check(knowledge_count, 'Knowledge Amount', errprs)
	errors = int_check(circ_value, 'Circumstance Value', errprs)
	errors = int_check(circ_turns, 'Turns', errprs)
	errors = int_check(measure_val1, 'Neasurement Rank', errprs)
	errors = int_check(measure_value, 'Measurement Value', errprs)
	errors = int_check(condition_damage_value, 'Condition Damage Value', errprs)
	errors = int_check(condition_damage, 'Condition Direction', errprs)
	errors = int_check(nullify, 'Nullify DC', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Consequence, consequence, 'Consequence', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)
	errors = db_check(Math, measure_math, 'Math', errors)
	errors = db_check(Rank, measure_rank, 'Measurement Rank', errors)

	return(errors)

def adv_effort_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	effect = data['effect']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	benefit_choice = data['benefit_choice']
	benefit_turns = data['benefit_turns']
	benefit_count = data['benefit_count']
	benefit_effort = data['benefit_effort']

	errors = int_check(condition_damage_value, 'Condition Damage Value', errprs)
	errors = int_check(condition_damage, 'Condition Damage Direction', errprs)
	errors = int_check(benefit_turns, 'Benefit Turns', errprs)
	errors = int_check(benefit_count, 'Benefit Count', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Benefit, benefit_choice, 'Benefit', errors)

	return(errors)

def adv_minion_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	points = data['points']
	condition = data['condition']
	player_condition = data['player_condition']
	link = data['link']
	variable_type = data['variable_type']
	multiple = data['multiple']
	attitude = data['attitude']
	resitable = data['resitable']
	heroic = data['heroic']
	sacrifice = data['sacrifice']
	sacrifice_cost = data['sacrifice_cost']
	attitude_type = data['attitude_type']
	attitude_attitude = data['attitude_attitude']
	attitude_trait_type = data['attitude_trait_type']
	attitude_trait = data['attitude_trait']
	resitable_check = data['resitable_check']
	resitable_dc = data['resitable_dc']
	multiple_value = data['multiple_value']
	horde = data['horde']
	columns = data['columns']
	created = data['created']
	font = data['font']

	errors = int_check(points, 'Points', errprs)
	errors = int_check(sacrifice_cost, 'Sacrifice Cost', errprs)
	errors = int_check(resitable_dc, 'Sacrifice DC', errprs)
	errors = int_check(multiple_value, 'Multiple Value', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(LevelType, attitude_type, 'Attitude Type', errors)
	errors = db_check(Levels, attitude_attitude, 'Attitude', errors)
	errors = db_check(Check, resitable_check, 'Check', errors)

	return(errors)

def adv_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	Benefit = data['benefit']
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

	errors = int_check(bonus, 'Bonus', errprs)
	errors = int_check(penalty, 'Penalty', errprs)
	errors = int_check(multiple_count, 'Multiple Count', errprs)
	errors = int_check(lasts, 'Lasts', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
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

	return(errors)

def adv_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	opponent_trait_type = data['opponent_trait_type']
	opponent_trait = data['opponent_trait']
	opponent_mod = data['opponent_mod']
	player_check = data['player_check']
	opponent_check = data['opponent_check']
	multiple = data['multiple']

	errors = int_check(mod, 'Modifier', errprs)
	errors = int_check(opponent_mod, 'Opponent Modifier', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Check, player_check, 'Player Check', errors)
	errors = db_check(Check, opponent_check, 'Opponent Check', errors)

	return(errors)

def adv_points_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	spend = data['spend']
	condition_cost = data['condition_cost']
	condition1 = data['conditioon1']
	condition2 = data['condition2']
	equipment_points = data['equipment_points']
	equipment_vehicles = data['equipment_vehicles']
	equipment_headquarters = data['equipment_headquarters']
	initiative_cost = data['initiative_cost']
	twenty = data['twenty']
	check_bonus = data['check_bonus']
	check_cost = data['check_cost']
	check_turns = data['check_turns']
	check_target = data['check_target']
	check_all = data['check_all']
	benefit_choice = data['benefit_choice']
	benefit_count = data['benefit_count']
	benefit_cost = data['benefit_cost']
	benefit_turns = data['benefit_turns']
	ranks_gained = data['ranks_gained']
	ranks_max = data['ranks_max']
	ranks_lasts = data['ranks_lasts']
	ranks_trait_type = data['ranks_trait_type']
	ranks_trait = data['ranks_trait']

	errors = int_check(condition_cost, 'Condition Cost', errprs)
	errors = int_check(equipment_points, 'Equipment Points', errprs)
	errors = int_check(initiative_cost, 'Initiative Cost', errprs)
	errors = int_check(twenty, '20 Cost', errprs)
	errors = int_check(check_bonus, 'Check Bonus', errprs)
	errors = int_check(check_cost, 'Check Bonus Cost', errprs)
	errors = int_check(check_turns, 'Check Bonus Turns', errprs)
	errors = int_check(benefit_count, 'Benefit Count', errprs)
	errors = int_check(benefit_cost, 'Benefit Cost', errprs)
	errors = int_check(benefit_turns, 'Benefit Turns', errprs)
	errors = int_check(ranks_gained, 'Ranks Gained', errprs)
	errors = int_check(ranks_max, 'Maximum Ranks', errprs)
	errors = int_check(ranks_lasts, 'Ranks Last', errprs)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Benefit, benefit_choice, 'Bemefit', errors)

	return(errors)

def adv_resist_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	which = data['which']

	errors = int_check(mod, 'Modifier', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

	return(errors)

def adv_rounds_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	rounds = data['rounds']
	cost = data['cost']
	check = data['check']
	trait_type = data['trait_type']
	trait = data['trait']
	end = data['end']

	errors = int_check(rounds, 'Rounds', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Action, cost, 'Action Cost', errors)
	errors = db_check(Check, check, 'Check Type', errors)

	return(errors)

def adv_skill_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	replaced_trait_type = data['replaced_trait_type']
	replaced_trait = data['replaced_trait']
	multiple = data['multiple']

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

	return(errors)

def adv_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	time_type = data['time_type']
	value_type = data['value_type']
	value = data['value']
	units = data['units']
	time_value = data['time_value']
	math = data['math']
	trait_type = data['trait_type']
	trait = data['trait']
	dc = data['dc']
	check_type = data['check_type']
	recovery = data['recovery']
	recovery_penalty = data['recovery_penalty']
	recovery_time = data['recovery_time']
	recovery_incurable = data['recovery_incurable']

	errors = int_check(value, 'Time Value', errprs)
	errors = int_check(time_value, 'Time Math Value', errprs)
	errors = int_check(dc, 'DC', errprs)
	errors = int_check(recovery_penalty, 'Recovery Penalty', errprs)	
	errors = int_check(recovery_time, 'Recovery Time', errprs)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Unit, units, 'Units', errors)
	errors = db_check(Math, math, 'Math', errors)
	errors = db_check(Check, check_type, 'Check Type', errors)

	return(errors)

def adv_variable_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	trait_type = data['trait_type']
	trait = data['trait']

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	return(errors)