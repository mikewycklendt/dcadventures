
from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer, db_check, if_fields, if_field, create_check, db_insert, adv_entry_check, adv_check_multiple, adv_check_multiple_fields, adv_select_entry


def adv_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	description = data['description']
	adv_type = data['adv_type']
	action = data['action']
	check_type = data['check_type']
	ranked = data['ranked']
	ranked_ranks = data['ranked_ranks']
	ranked_max = data['ranked_max']
	trait_type = data['trait_type']
	trait = data['trait']
	replaced_trait_type = data['replaced_trait_type']
	replaced_trait = data['replaced_trait']
	skill_type = data['skill_type']
	skill = data['skill']
	skill_description = data['skill_description']
	skill_untrained = data['skill_untrained']
	no_pre_check = data['no_pre_check']
	expertise = data['expertise']
	conflict = data['conflict']
	consequence = data['consequence']
	conflict_immune = data['conflict_immune']
	dc_type = data['dc_type']
	dc_value = data['dc_value']
	dc_mod = data['dc_mod']
	alter_target = data['alter_target']
	simultaneous = data['simultaneous']
	simultaneous_type = data['simultaneous_type']
	extra_action = data['extra_action']
	action1 = data['action1']
	action2 = data['action2']
	invent = data['invent']
	invent_permanence = data['invent_permanence']
	invent_trait_type = data['invent_trait_type']
	invent_trait = data['invent_trait']
	rituals = data['rituals']
	gm_secret_check = data['gm_secret_check']
	gm_trait_type = data['gm_trait_type']
	gm_trait = data['gm_trait']
	gm_veto = data['gm_veto']
	language = data['language']
	languages = data['languages']
	language_rank = data['language_rank']
	multiple = data['multiple']
	groups = data['groups']
	pressure = data['pressure']
	check_check = data['check_check']
	circumstance = data['circumstance']
	combined = data['combined']
	condition = data['condition']
	dc = data['dc']
	degree = data['degree']
	effort = data['effort']
	levels = data['levels']
	minion = data['minion']
	mods = data['mods']
	mods_multiple = data['mods_multiple']	
	mods_count = data['mods_count']
	opposed = data['opposed']
	opposed_multiple = data['opposed_multiple']
	points = data['points']
	resist = data['resist']
	resist_multiple = data['resist_multiple']
	rounds = data['rounds']
	swap = data['swap']
	swap_multiple = data['swap_multiple']
	time = data['time']
	variable = data['variable']

	errors = adv_entry_check('Variable Trait', AdvVariable, variable, advantage_id, errors)
	errors = adv_entry_check('DC Table', AdvDC, dc, advantage_id, errors)
	errors = adv_entry_check('Bonus/Penalty Modifier', AdvMod, mods, advantage_id, errors)
	errors = adv_entry_check('Opposed Check', AdvOpposed, opposed, advantage_id, errors)
	errors = adv_entry_check('Circumstance', AdvCirc, circumstance, advantage_id, errors)
	errors = adv_entry_check('Degree of Success/Failure', AdvDegree, degree, advantage_id, errors)
	errors = adv_entry_check('Resistance Check', AdvResist, resist, advantage_id, errors)
	errors = adv_entry_check('Bonus Swap', AdvSkill, swap, advantage_id, errors)
	errors = adv_entry_check('Condition', AdvCondition, condition, advantage_id, errors)
	errors = adv_entry_check('Levels', Levels, levels, advantage_id, errors)
	errors = adv_entry_check('Variable Check', AdvAltCheck, check_check, advantage_id, errors)
	errors = adv_entry_check('Multiple Round', AdvRounds, rounds, advantage_id, errors)
	errors = adv_entry_check('Spend Points', AdvPoints, points, advantage_id, errors)
	errors = adv_entry_check('Extra Effort', AdvEffort, effort, advantage_id, errors)
	errors = adv_entry_check('Time Effect', AdvTime, time, advantage_id, errors)
	errors = adv_entry_check('Minions', AdvMinion, minion, advantage_id, errors)
	errors = adv_entry_check('Combined Advantage', AdvCombined, combined, advantage_id, errors)

	errors = adv_check_multiple('Swap Bonus', AdvSkill, swap_multiple, advantage_id, errors)
	errors = adv_check_multiple('Opposed Check', AdvOpposed, opposed_multiple, advantage_id, errors)
	errors = adv_check_multiple('Resistance Check', AdvResist, resist_multiple, advantage_id, errors)
	errors = adv_check_multiple_fields('Bonus/Penalty Modifier', AdvMod, [mods_multiple, mods_count], advantage_id, errors)

	errors = required(adv_type, 'Advantage Type', errors)
	errors = required(action, 'Action Type', errors)
	errors = required(check_type, 'Check Type', errors)

	errors = adv_select_entry('x', 'Variable Trait', 'Trait Type', 'Variable Trait', trait_type, AdvVariable, advantage_id, errors, True)
	errors = if_field('Skill Check', skill_type, skill_description, 'Circumstance', errors)
	errors = adv_select_entry('table', 'DC Table', 'Difficulty Class', 'DC Table', dc_type, AdvDC, advantage_id, errors)

	errors = variable_fields('value', 'DC', dc_type, [dc_value], errors)
	
	errors = variable_fields('value', 'DC', dc_type, [dc_value], errors)
	errors = variable_field('value', dc_type, 'DC Value', dc_value, errors)
	errors = variable_fields('mod', 'DC', dc_type, [dc_mod], errors)
	errors = variable_field('mod', dc_type, 'DC Modifier', dc_mod, errors)

	errors = check_fields(simultaneous, 'Simultaneous Action', [simultaneous_type], errors)
	errors = check_field(simultaneous, 'Simultaneous Action', 'Simultaneous Action Type', simultaneous_type, errors)

	errors = check_fields(extra_action, 'Third Action', [action1, action2], errors)
	errors = check_field(extra_action, 'Third Action', 'First Action', action1, errors)
	errors = check_field(extra_action, 'Third Action', 'Second Action', action2, errors)

	errors = check_fields(invent, 'Invent Devices', [invent_permanence, invent_trait_type, invent_trait], errors)
	errors = check_field(invent, 'Invent Devices', 'Invent Permanenve', invent_permanence, errors)
	errors = check_field(invent, 'Invent Devices', 'Inventing Trait Type', invent_trait_type, errors)
	errors = check_field(invent, 'Invent Devices', 'Inventing Trait', invent_trait, errors)

	errors = check_fields(gm_secret_check, 'Secret GM Check', [gm_trait, gm_trait_type], errors)
	errors = check_field(gm_secret_check, 'Secret GM Check', 'Secret GM Check Trait Type', gm_trait_type, errors)
	errors = check_field(gm_secret_check, 'Secret GM Check', 'Secret GM Check Trait Type', gm_trait, errors)\
	
	errors = check_of(language, 'Languages', [languages, language_rank], errors)

	return (errors)

def adv_levels_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	level_type = data['level_type']
	level = data['level']
	level_effect = data['level_effect']

	errors = create_check('Advantage', advantage_id, Advantage, errors)

	errors = id_check(Advantage, advantage_id, 'Advantage', errors)

	errors = required(level_type, 'Level Type', errors)
	errors = required(level, 'Level', errors)
	errors = required(level_effect, 'Level Effect', errors)
	

	return (errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(action, 'Action', errors)
	
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
	errors = variable_field('condition', trigger, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', trigger, 'Ending Condition', condition2, errors)
	
	errors = variable_fields('conflict', 'Triggered by Conflict Action', trigger, [conflict], errors)
	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	errors = required(name, 'Name', errors)
	errors = required(description, 'Description', errors)

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
	
	errors = create_check('Advantage', advantage_id, Advantage, errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)
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

	errors = variable_fields('trait', 'Nullified by Trait', null_type, [null_trait_type, null_trait], errors)
	errors = variable_field('trait', null_type, 'Trait Type', null_trait_type, errors)
	errors = variable_field('trait', null_type, 'Trait', null_trait, errors)
	errors = variable_fields('condition', 'Nullified by Condition', null_type, [null_condition], errors)
	errors = variable_field('condition', null_type, 'Condition', null_condition, errors)
	errors = variable_fields('override', 'Override Trait Circumstance', null_type, [null_override_trait_type, null_override_trait], errors)
	errors = variable_field('override', null_type, 'Trait Type', null_override_trait_type, errors)
	errors = variable_field('override', null_type, 'Trait', null_override_trait, errors)

	return(errors)

def adv_combined_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	ranks = data['ranks']
	advantage = data['advantage']

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(ranks, 'Ranks', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	errors = required(ranks, 'Ranks', errors)
	errors = required(advantage, 'Advantage', errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(damage_value, 'Condition Damage', errors)
	errors = int_check(damage, 'Damage Direction', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value_value, 'DC', errors)
	errors = int_check(math_value, 'Math Value', errors)
	errors = int_check(check_mod, 'Check Modifier', errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Math, math_math, 'Math', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)

	errors = required(dc, 'DC Type', errors)
	errors = required(description, 'Description', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('value', 'DC Value', dc, [value_value], errors)
	errors = variable_field('value', dc, 'DC Value', value_value, errors)
	errors = variable_fields('math', 'DC Math', dc, [math_value, math_math, math_trait_type, math_trait], errors)
	errors = variable_field('math', dc, 'DC Math Value', math_value, errors)
	errors = variable_field('math', dc, 'DC Math', math_math, errors)
	errors = variable_field('math', dc, 'DC Math Trait Type', math_trait_type, errors)
	errors = variable_field('math', dc, 'DC Math Trait', math_trait, errors)

	errors = check_fields(condition, 'Condition', [condition1, condition2], errors)
	errors = check_field(condition, 'Condition', 'Starting Condition', condition1, errors)
	errors = check_field(condition, 'Condition', 'Ending Condition', condition2, errors)

	errors = check_field(keyword_check, 'Keyword', 'Keyword', keyword, errors)

	errors = check_fields(check_type, 'Check Type', [check_trait_type, check_trait, check_mod], errors)
	errors = check_field(check_type, 'Check Type', 'Trait Type', check_trait_type, errors)
	errors = check_field(check_type, 'Check Type', 'Trait', check_trait, errors)
	errors = check_field(check_type, 'Check Type', 'Check Modifier', check_mod, errors)

	errors = check_field(levels, 'Level', 'Level', level, errors)


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
	deg_type = data['deg_mod_type']
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value, 'Circumstance Modifier', errors)
	errors = int_check(consequence_action, 'Consequence Action', errors)
	errors = int_check(knowledge_count, 'Knowledge Amount', errors)
	errors = int_check(circ_value, 'Circumstance Value', errors)
	errors = int_check(circ_turns, 'Turns', errors)
	errors = int_check(measure_val1, 'Neasurement Rank', errors)
	errors = int_check(measure_value, 'Measurement Value', errors)
	errors = int_check(condition_damage_value, 'Condition Damage Value', errors)
	errors = int_check(condition_damage, 'Condition Direction', errors)
	errors = int_check(nullify, 'Nullify DC', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Consequence, consequence, 'Consequence', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)
	errors = db_check(Math, measure_math, 'Math', errors)
	errors = db_check(Rank, measure_rank, 'Measurement Rank', errors)

	errors = required(value, 'Degree', errors)
	errors = required(deg_type, 'Result Type', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('measure', 'Measurement', deg_type, [measure_type], errors)
	errors = variable_fields('math', 'Measurement Math', measure_type, [measure_val1, measure_math, measure_trait_type, measure_trait], errors)
	errors = variable_field('math', measure_type, 'Measurement Math Value', measure_val1, errors)
	errors = variable_field('math', measure_type, 'Measurement Math', measure_math, errors)
	errors = variable_field('math', measure_type, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('math', measure_type, 'Measurement Trait', measure_trait, errors)

	errors = variable_fields('value', 'Measurement Value', measure_type, [measure_value, measure_rank], errors)
	errors = variable_field('value', measure_type, 'Measurement Value', measure_value, errors)
	errors = variable_field('value', measure_type, 'Measurement Rank Type', measure_rank, errors)
	
	errors = variable_fields('condition', 'Condition', deg_type, [condition_type], errors)
	errors = variable_fields('condition', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', condition_type, 'Ending Condition', condition2, errors)
	errors = variable_fields('damage', 'Damage Condition',condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Value', condition_damage_value, errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Change', condition_damage, errors)
	errors = variable_fields('circ', 'Circumstance', deg_type, [circ_value, circ_turns, circ_trait_type, circ_trait], errors)
	errors = variable_field('circ', deg_type, 'Circumstance Value', circ_value, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Turns', circ_turns, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait Type', circ_trait_type, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait',  circ_trait, errors)

	errors = variable_fields('level', 'Level', deg_type, [level_type, level], errors)
	
	errors = variable_fields('knowledge' , 'Knowledge', deg_type, [knowledge], errors)
	errors = variable_fields('bonus', 'Learn Bonus', knowledge, [knowledge_count, knowledge_specificity], errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Count', knowledge_count, errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Specificity', knowledge_specificity, errors)

	errors = variable_fields('consequence', 'Consequence', deg_type, [consequence], errors)
	errors = variable_field('consequence', deg_type, 'Consequence', consequence, errors)


	errors = variable_fields('level', 'Level', deg_type, [level], errors)

	errors = required(keyword, 'Keyword', errors)


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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(condition_damage_value, 'Condition Damage Value', errors)
	errors = int_check(condition_damage, 'Condition Damage Direction', errors)
	errors = int_check(benefit_turns, 'Benefit Turns', errors)
	errors = int_check(benefit_count, 'Benefit Count', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Benefit, benefit_choice, 'Benefit', errors)

	errors = required(effect, 'Effect', errors)
	errors  = required(condition_type, 'Condition Type', errors)

	errors = variable_fields('benefit', 'Benefit', effect, [benefit_choice, benefit_turns], errors)
	errors = variable_field('benefit', effect, 'Turns', benefit_turns, errors)
	errors = variable_field('benefit', effect, 'Benefit Choice', benefit_choice, errors)
	errors = variable_fields('x', 'Variable Benefit', benefit_choice, [benefit_count], errors)
	errors = variable_field('x', benefit_choice, 'Count', benefit_count, errors)

	errors = variable_fields('condition', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', condition_type, 'Ending Condition', condition2, errors)
	errors = variable_fields('damage', 'Condition Damage', condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', condition_type, 'Damage Degrees', condition_damage_value, errors)
	errors = variable_field('damage', condition_type, 'Damage Direction', condition_damage, errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(points, 'Points', errors)
	errors = int_check(sacrifice_cost, 'Sacrifice Cost', errors)
	errors = int_check(resitable_dc, 'Sacrifice DC', errors)
	errors = int_check(multiple_value, 'Multiple Value', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(LevelType, attitude_type, 'Attitude Type', errors)
	errors = db_check(Levels, attitude_attitude, 'Attitude', errors)
	errors = db_check(Check, resitable_check, 'Check', errors)
	
	errors = required(points, 'Points', errors)
	errors = required(condition, 'Minion Condition', errors)
	errors = required(player_condition, 'Player Condition While Summoning', errors)
	errors = required(variable_type, 'Minion Type', errors)

	errors = check_fields(multiple, 'Multiple Minions', [multiple_value], errors)
	errors = check_field(multiple, 'Multiple Minions', 'Multiple Value', multiple_value, errors)
	errors = check_fields(attitude, 'Attitude', [attitude_type, attitude_attitude, attitude_trait_type, attitude_trait], errors)
	errors = check_field(attitude, 'Attitude', 'Attitude Level Type', attitude_type, errors)
	errors = check_field(attitude, 'Attitude', 'Attitude Level', attitude_attitude, errors)
	errors = check_field(attitude, 'Attitude', 'Attitude Trait Type to Control', attitude_trait_type, errors)
	errors = check_field(attitude, 'Attitude', 'Attitude Trait to Control', attitude_trait, errors)
	errors = check_fields(resitable, 'Resistable', [resitable_check, resitable_dc], errors)
	errors = check_field(resitable, 'Resistable', 'Resistable Check Type', resitable_check, errors)
	errors = check_field(resitable, 'Resistable', 'Resistable DC', resitable_dc, errors)
	errors = check_fields(sacrifice, 'Sacrifice', [sacrifice_cost], errors)
	errors = check_field(sacrifice, 'Sacrifice', 'Sacrifice Cost', sacrifice_cost, errors)

	return(errors)

def adv_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(bonus, 'Bonus', errors)
	errors = int_check(penalty, 'Penalty', errors)
	errors = int_check(multiple_count, 'Multiple Count', errors)
	errors = int_check(lasts, 'Lasts', errors)

	errors = db_insert('Environment', Environment, environment, environment_other, errors)
	errors = db_insert('Emotion', Emotion, emotion, emotion_other, errors)
	errors = db_insert('Creature', Creature, creature, creature_other, errors)
	errors = db_insert('Profession', Job, profession, profession_other, errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Check, player_check, 'Player Check', errors)
	errors = db_check(Check, opponent_check, 'Opponent Check', errors)

	errors =  required(trait_type, 'Trait Type', errors)
	errors =  required(trait, 'Trait', errors)
	errors =  required(mod, 'Modifier', errors)
	errors =  required(opponent_trait_type, 'Opponent Trqait Type', errors)
	errors =  required(opponent_trait, 'Opponent Trait', errors)
	errors =  required(opponent_mod, 'Opponent Modifier', errors)
	errors =  required(player_check, 'Player Check', errors)
	errors =  required(opponent_check, 'Opponent Check', errors)

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
	condition1 = data['condition1']
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(condition_cost, 'Condition Cost', errors)
	errors = int_check(equipment_points, 'Equipment Points', errors)
	errors = int_check(initiative_cost, 'Initiative Cost', errors)
	errors = int_check(twenty, '20 Cost', errors)
	errors = int_check(check_bonus, 'Check Bonus', errors)
	errors = int_check(check_cost, 'Check Bonus Cost', errors)
	errors = int_check(check_turns, 'Check Bonus Turns', errors)
	errors = int_check(benefit_count, 'Benefit Count', errors)
	errors = int_check(benefit_cost, 'Benefit Cost', errors)
	errors = int_check(benefit_turns, 'Benefit Turns', errors)
	errors = int_check(ranks_gained, 'Ranks Gained', errors)
	errors = int_check(ranks_max, 'Maximum Ranks', errors)
	errors = int_check(ranks_lasts, 'Ranks Last', errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Benefit, benefit_choice, 'Bemefit', errors)

	errors = required(spend, 'Points Type', errors)

	errors = variable_fields('ranks', 'Gain Ranks', spend, [ranks_gained, ranks_lasts, ranks_trait_type, ranks_trait], errors)
	errors = variable_field('ranks', spend, 'Ranks Gained', ranks_gained, errors)
	errors = variable_field('ranks', spend, 'Ranks Duration', ranks_lasts, errors)
	errors = variable_field('ranks', spend, 'Trait Type', ranks_trait_type, errors)
	errors = variable_field('ranks', spend, 'Trait', ranks_trait, errors)
	errors = variable_fields('benefit', 'Benefit', spend, [benefit_choice, benefit_cost, benefit_turns], errors)
	errors = variable_field('x', benefit_choice, 'Benefit Count', benefit_count, errors)
	errors = variable_field('benefit', spend, 'Benefit', benefit_choice, errors)
	errors = variable_field('benefit', spend, 'Benefit Cost', benefit_cost, errors)
	errors = variable_field('benefit', spend, 'Benefit Turns', benefit_turns, errors)
	errors = variable_fields('check', 'Circumstance Modifier', spend, [check_bonus, check_cost, check_turns, check_target], errors)
	errors = variable_field('check', spend, 'Modifier', check_bonus, errors)
	errors = variable_field('check', spend, 'Circumstance Cost', check_cost, errors)
	errors = variable_field('check', spend, 'Circumstance Turns', check_turns, errors)
	errors = variable_field('check', spend, 'Circumstance Target', check_target, errors)
	errors = variable_fields('equip', 'Equipment', spend, [equipment_points], errors)
	errors = variable_field('equip', spend, 'Equipment Cost', equipment_points, errors)
	errors = variable_fields('condition', 'Change Condition', spend, [condition_cost, condition1, condition2], errors)
	errors = variable_field('condition', spend, 'Condition Cost', condition_cost, errors)
	errors = variable_field('condition', spend, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', spend, 'Ending Condition', condition2, errors)
	errors = variable_fields('initiative', 'Gain Initiative', spend, [initiative_cost], errors)
	errors = variable_fields('20', 'Automatic 20', spend, [twenty], errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(mod, 'Modifier', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

	errors = required(trait_type, 'Trait Type', errors)
	errors = required(trait, 'Trait', errors)
	errors = required(mod, 'Modifier', errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(rounds, 'Rounds', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Action, cost, 'Action Cost', errors)
	errors = db_check(Check, check, 'Check Type', errors)

	errors = required(rounds, 'Turns', errors)
	errors = required(cost, 'Action', errors)
	errors = required(end, 'Ends', errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)

	errors = required(trait_type, 'Trait Type to Use', errors)
	errors = required(trait, 'Trait to Use', errors)
	errors = required(replaced_trait_type, 'Replaced by Trait Type', errors)
	errors = required(replaced_trait, 'Replaced by Trait', errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value, 'Time Value', errors)
	errors = int_check(time_value, 'Time Math Value', errors)
	errors = int_check(dc, 'DC', errors)
	errors = int_check(recovery_penalty, 'Recovery Penalty', errors)	
	errors = int_check(recovery_time, 'Recovery Time', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Unit, units, 'Units', errors)
	errors = db_check(Math, math, 'Math', errors)
	errors = db_check(Check, check_type, 'Check Type', errors)

	errors = required(time_type, 'Time Type', errors)
	errors = required(value_type, 'Time Value Type', errors)

	errors = variable_fields('value', 'Time Value', value_type, [value, units], errors)
	errors = variable_field('value', value_type,'Time Value', value, errors)
	errors = variable_field('value', value_type,'Time Units' , units, errors)
	errors = variable_fields('math', 'Time Math', value_type, [time_value, math, trait_type, trait], errors)
	errors = variable_field('math', value_type, 'Time Valuea', time_value, errors)
	errors = variable_field('math', value_type, 'Time Math', math, errors)
	errors = variable_field('math', value_type, 'Trait Type', trait_type, errors)
	errors = variable_field('math', value_type, 'Trait', trait, errors)

	errors = check_fields(recovery, 'Recovery', [recovery_penalty, recovery_time], errors)
	errors = check_field(recovery, 'Recovery', 'Recovery Penalty', recovery_penalty, errors)
	errors = check_field(recovery, 'Recovery', 'Recovery Time', recovery_time, errors)


	return(errors)

def adv_variable_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	trait_type = data['trait_type']
	trait = data['trait']

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)

	errors = required(trait_type, 'Trait Type', errors)
	errors = required(trait, 'Trait', errors)

	return(errors)