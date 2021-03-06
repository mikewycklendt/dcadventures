
from logging import error
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Element, EnvCondition, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType, Communication
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature, NarrowCreature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerCost, PowerRanks, PowerCondition, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import PowerCircType, PowerCheckType, PowerOpposedType, PowerDCType, PowerDegreeType, PowerMoveType, PowerRangedType, PowerTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert, db_multiple, id_multiple
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import primary_exist, required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_field_of, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, not_required, seperate_checks, checked_invalid_option, variable_fields_of, incompatible, valid_options, extra_option, variable_required_rules, cross_check, variable_field_required, dependent_of, incompatible_multiple, required_subrule
from functions.create_posts import send_multiple, one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string, circ_cell

from create_functions.power_create import power_check, rule_check, rule_select, cost_check, extra_cost, extra_check, extra_convert, field_cost, multiple_cost, variable_cost, sense_cost, power_rules, valid_extra, ranks_error, ranks_function, cost_error, cost_exist, cost_check_table, degree_check, extra_cost_exist, multiple_error, trait_cost, power_sense_condition, power_reflect_immune, extra_rule_select

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def power_save_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	description = data['description']
	power_type = data['power_type']
	action = data['action']
	power_range = data['power_range']
	duration = data['duration']
	cost = data['cost']
	ranks = data['ranks']
	flat = data['flat']
	limit = data['limit']
	dc_type = data['dc_type']
	dc_value = data['dc_value']
	dc_mod = data['dc_mod']
	opponent_dc = data['opponent_dc']
	check_type = data['check_type']
	routine = data['routine']
	routine_trait_type = data['routine_trait_type']
	routine_trait = data['routine_trait']
	materials = data['materials']
	partner = data['partner']
	partner_trait_type = data['partner_trait_type']
	partner_dc = data['partner_dc']
	partner_trait = data['partner_trait']
	circ = data['circ']
	circ_required = data['circ_required']
	skill = data['skill']
	skill_required = data['skill_required']
	skill_when = data['skill_when']
	conflict = data['conflict']
	bonus_conflict = data['bonus_conflict']
	conflict_bonus = data['conflict_bonus']
	conflict_type = data['conflict_type']	
	condition = data['condition']
	alt_check = data['alt_check']
	change_action = data['change_action']
	character = data['character']
	circumstance = data['circumstance']
	create = data['create']
	damage = data['damage']
	dc = data['dc']
	defense = data['defense']
	degree = data['degree']
	environment = data['environment']
	levels = data['levels']
	minion = data['minion']
	modifier = data['modifier']
	move = data['move']
	opposed = data['opposed']
	ranged = data['ranged']
	resistance = data['resistance']
	resist_by = data['resist_by']
	reverse = data['reverse']
	sense = data['sense']
	time = data['time']
	req_descriptor = data['req_descriptor']

	power_id = integer(power_id)

	errors = power_check(power_id, errors)
	error = errors['error']
	if error:
		return (errors)

	errors = power_rules(power_id, errors)

	errors = valid_extra(power_id, errors)

	errors = required(description, 'Description', errors)
	errors = required(power_type, 'Power Type', errors)
	errors = required(action, 'Action Type', errors)
	errors = required(power_range, 'Range', errors)
	errors = required(duration, 'Duration', errors)
	errors = required(cost, 'Cost', errors)
	errors = required(check_type, 'Check Type', errors)
	errors = check_fields(routine, 'Routine Skill Check', [routine_trait_type, routine_trait], errors)
	errors = check_field(routine, 'Routine Skill Check', 'Routine Check Skill Type', routine_trait_type, errors)
	errors = check_field(routine, 'Routine Skill Check', 'Routine Check Skill', routine_trait, errors)
	errors = variable_fields('skill', 'Partner Skill Check', partner, [partner_trait_type, partner_dc, partner_trait], errors)
	errors = variable_field('skill', partner, 'Partner Trait Type', partner_trait_type, errors)
	errors = variable_field('skill', partner, 'Partner Trait', partner_trait, errors)
	errors = variable_field('skill', partner, 'Partner DC', partner_dc, errors)

	errors = rule_check(alt_check, 'Alternate Check', PowerAltCheck, power_id, errors)
	errors = rule_check(change_action, 'Change Action', PowerAction, power_id, errors)
	errors = rule_check(character, 'Changes Character Traits', PowerChar, power_id, errors)
	errors = rule_check(circumstance, 'Circumstance Modifier', PowerCirc, power_id, errors)
	errors = rule_check(create, 'Create', PowerCreate, power_id, errors)
	errors = rule_check(damage, 'Damage Effect', PowerDamage, power_id, errors)
	errors = rule_check(dc, 'DC Table', PowerDC, power_id, errors)
	errors = rule_check(defense, 'Defense Effect', PowerDefense, power_id, errors)
	errors = rule_check(degree, 'Degree of Success/Failure', PowerDegMod, power_id, errors)
	errors = rule_check(environment, 'Environment', PowerEnv, power_id, errors)
	errors = rule_check(levels, 'Levels', Levels, power_id, errors)
	errors = rule_check(minion, 'Minion', PowerMinion, power_id, errors)
	errors = rule_check(modifier, 'Modifiers', PowerMod, power_id, errors)
	errors = rule_check(move, 'Movement Effect', PowerMove, power_id, errors)
	errors = rule_check(opposed, 'Opposed Check', PowerOpposed, power_id, errors)
	errors = rule_check(ranged, 'Ranged Effect', PowerRanged, power_id, errors)
	errors = rule_check(resistance, 'Resistance Modifier', PowerResist, power_id, errors)
	errors = rule_check(resist_by, 'Resisted By', PowerResistBy, power_id, errors)
	errors = rule_check(reverse, 'Reverse Effect', PowerReverse, power_id, errors)
	errors = rule_check(sense, 'Sense Effect', PowerSenseEffect, power_id, errors)
	errors = rule_check(time, 'Time Effect', PowerTime, power_id, errors)

	errors = rule_select('table', circ, 'Circumstance Modifier', PowerCirc, power_id, errors)
	errors = rule_select('table', dc_type, 'DC Table', PowerDC, power_id, errors)
	errors = rule_select('2', action, 'Movement', PowerMove, power_id, errors)
	errors = rule_select('5', power_range, 'Ranked Range', PowerRanged, power_id, errors)
	errors = rule_select('2', power_type, 'Movement', PowerMove, power_id, errors)
	errors = rule_select('2', check_type, 'Opposed Check', PowerOpposed, power_id, errors)
	errors = rule_select('7', check_type, 'Comparison Check', PowerOpposed, power_id, errors)
	errors = rule_select('x', check_type, 'Variable Check', PowerCheck, power_id, errors)

	errors = incompatible('2', check_type, 'An Opposed Check', 'x', action, 'Action Field', 'Variable Action', errors)
	errors = incompatible('7', check_type, 'A Comparison Check', 'x', action, 'Action Field', 'Variable Action', errors)

	errors = variable_field_required('x', check_type, 'Check Type', 'Variable Check', 'Variable Action', 'Action', action, 'x', errors)
	errors = variable_field_required('x', action, 'Action', 'Variable Action', 'Variable Check', 'Check Type', check_type, 'x', errors), 

	errors = primary_exist(check_type, PowerCheck, PowerOpposed, 'power_id', power_id, True)

	errors = extra_rule_select(PowerRanged, 'set the range to ranked', 'Ranged Effect', power_id, 'range', 5, errors)

	errors = power_sense_condition(power_id, errors)

	errors = trait_cost(cost, power_id, errors)

	errors = cost_exist(power_id, cost, errors)
	errors = extra_cost_exist(power_id, errors)

	return (errors)

def change_action_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	action = data['action']
	mod = data['mod']
	objects = data['objects']
	circumstance = data['circumstance']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Action, action, 'Action', errors)
	
	errors = int_check(mod, 'Modifier', errors)

	errors = required(mod, 'Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(action, 'Action Type', errors)


	return (errors)


def character_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	value = data['value']
	increase = data['increase']
	limited = data['limited']
	reduced = data['reduced']
	limbs = data['limbs']
	carry = data['carry']
	sustained = data['sustained']
	permanent = data['permanent']
	points = data['points']
	appear = data['appear']
	insubstantial = data['insubstantial']
	weaken = data['weaken']
	weaken_type = data['weaken_type']
	weaken_opposed_type = data['weaken_opposed_type']
	weaken_degree_type = data['weaken_degree_type']
	weaken_trait_type = data['weaken_trait_type']
	weaken_trait = data['weaken_trait']
	weaken_broad = data['weaken_broad']
	weaken_descriptor = data['weaken_descriptor']
	weaken_simultaneous = data['weaken_simultaneous']
	limited_by = data['limited_by']
	limited_other = data['limited_other']
	limited_emotion = data['limited_emotion']
	limited_emotion_other = data['limited_emotion_other']
	reduced_trait_type = data['reduced_trait_type']
	reduced_trait = data['reduced_trait']
	reduced_value = data['reduced_value']
	reduced_full = data['reduced_full']
	limbs_count = data['limbs_count']
	limbs_continuous = data['limbs_continuous']
	limbs_sustained = data['limbs_sustained']
	limbs_condition = data['limbs_condition']
	limbs_projection = data['limbs_projection']
	limbs_duration = data['limbs_duration']
	carry_capacity = data['carry_capacity']
	carry_internsl = data['carry_internal']
	carry_mass = data['carry_mass']
	points_value = data['points_value']
	points_type = data['points_type']
	points_trait_type = data['points_trait_type']
	points_trait = data['points_trait']
	points_descriptor = data['points_descriptor']
	appear_form = data['appear_form']
	appear_target = data['appear_target']
	appear_description = data['appear_description']
	appear_creature = data['appear_creature']
	appear_creature_narrow = data['appear_creature_narrow']
	insub_type = data['insub_type']
	insub_descriptor = data['insub_descriptor']
	insub_description = data['insub_description']
	cost = data['cost']
	ranks = data['ranks']
	multiple = data['multiple']
	meta = data['meta']
	metamorph = data['metamorph']

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_check(PowerOpposedType, weaken_opposed_type, 'Weaken Opponent Check By Group', errors)
	errors = id_check(PowerDegreeType, weaken_degree_type, 'Weaken Degree by Group', errors)

	errors = int_check(value, 'Increased By', errors)
	errors = int_check(increase, 'Per Rank', errors)
	errors = int_check(reduced_value, 'Reduced', errors)
	errors = int_check(carry_capacity, 'Carry Capacity', errors)
	errors = int_check(points_value, 'Points', errors)
	errors = int_check(limbs_count, 'Limbs Count', errors)
	errors = int_check(metamorph, 'Sets of Traits', errors)

	errors = id_check(Condition, limbs_condition, 'Condition', errors)
	errors = id_check(Creature, appear_creature, 'Broad Form', errors)
	errors = id_check(NarrowCreature, appear_creature_narrow, 'Narrow Form', errors)
	errors = id_check(PowerDes, insub_descriptor, 'Insubstantial Descriptor', errora)

	errors = together('an Increased Trait', [trait_type, value, increase], errors)
	errors = check_field(limited, 'Limited', 'Limited By', limited_by, errors)
	errors = variable_fields('emotion', 'Emotional State', limited_by, [limited_emotion], errors)
	errors = variable_fields('other', 'Other Emotion', limited_emotion, [limited_emotion_other], errors)
	errors = variable_fields('other', 'Other Condition', limited_by, [limited_other], errors)

	errors = check_fields(reduced, 'Reduced Trait', [reduced_trait_type, reduced_value], errors)
	errors = check_field(reduced, 'Reduced Trait', 'Reduced Trait Type', reduced_trait_type, errors)
	errors = check_field(reduced, 'Reduced Trait', 'Reduced By Value', reduced_value, errors)
	errors = variable_fields('ability', 'Reduced Ability', reduced_trait_type, [reduced_trait], errors)
	errors = variable_field('ability', reduced_trait_type, 'Ability', reduced_trait, errors)
	errors = variable_fields('defense', 'Reduced Defense', reduced_trait_type, [reduced_trait], errors)
	errors = variable_field('defense', reduced_trait_type, 'Defense', reduced_trait, errors)

	errors = check_fields(limbs, 'Extra Limbs', [limbs_duration, limbs_count, limbs_condition], errors)
	errors = check_field(limbs, 'Extra Limbs', 'Active Condition', [limbs_condition], errors)
	errors = check_field(limbs, 'Extra Limbs', 'Limbs Duration', [limbs_duration], errors)
	errors = check_field(limbs, 'Extra Limbs', 'Limbs', limbs_count, errors)
	
	errors = check_of(carry, 'Extra Carry', 'Size Modifier or Mass Rank', [carry_mass, carry_capacity], errors)
	errors = check_field(carry_internal, 'Internal', 'Size Modifier', carry_capacity, errors)

	errors = check_fields(points, 'Hero Points', [points_value, points_trait_type, points_trait], errors)
	errors = check_field(points, 'Hero Points', 'Points Value', points_value, errors)
	errors = check_field(points, 'Hero Points', 'Trait Type', points_trait_type, errors)
	errors = check_field(points, 'Hero Points', 'Trait', points_trait, errors)

	errors = check_fields(appear, 'Alters Appearance', [appear_form], errors)
	errors = check_field(appear, 'Alters Appearance', 'Form', appear_form, errors)

	errors = variable_fields('broad', 'Broad Form', appear_form, [appear_creature], errors)
	errors = variable_field('broad', appear_form, 'Broad Form', appear_creature, errors)

	errors = variable_fields('narrow', 'Narrow Form', appear_form, [appear_creature, appear_creature_narrow], errors)
	errors = variable_field('narrow', appear_form, 'Broad Form', appear_creature, errors)
	errors = variable_field('narrow', appear_form, 'Narrow Form', appear_creature_narrow, errors)

	errors = check_fields(insubstantial, 'Insubstantial', [insub_type], errors)
	errors = check_field(insubstantial, 'Insubstantial', 'Insubstantial Type', insub_type, errors)
	errors = variable_fields('energy', 'Insubstantial Energy', insub_type, [insub_descriptor], errors)
	errors = variable_field('energy', insub_type, 'Descriptot', insub_descriptor, errors)

	errors = check_fields(points, 'Hero Points', [points_type, points_value, points_trait, points_trait_type], errors)
	errors = check_field(points, 'Hero Points', 'Points Type', points_type, errors)
	errors = check_field(points, 'Hero Points', 'Points', points_value, errors)
	errors = check_field(points, 'Hero Points', 'Points Trait Type', points_trait_type, errors)
	errors = check_field(points, 'Hero Points', 'Points Trait', points_trait, errors)

	errors = check_fields(weaken, 'Weaken', [weaken_type, weaken_opposed_type, weaken_degree_type], errors)
	errors = check_field(weaken, 'Weaken', 'Weaken Type', weaken_type, errors)
	errors = check_field(weaken, 'Weaken', 'Opponent Check by Group', weaken_opposed_type, errors)
	errors = check_field(weaken, 'Weaken', 'Degree by Group', weaken_degree_type, errors)
	errors = variable_fields('trait', 'Weaken Specific Trait', weaken_type, [weaken_trait_type, weaken_trait], errors)
	errors = variable_fields('type', 'Weaken Broad Trait', weaken_type, [weaken_broad], errors)
	errors = variable_fields('descriptor', 'Weaken Broad Descriptor', weaken_type, [weaken_descriptor], errors)


	errors = variable_fields('trait', 'Specific', weaken_type, [weaken_trait_type, weaken_trait], errors)
	errors = variable_field('trait', weaken_type, 'Trait Type', weaken_trait_type, errors)
	errors = variable_field('trait', weaken_type, 'Trait', weaken_trait, errors) 
	errors = variable_fields('type', weaken_type, 'Broad Trait', [weaken_broad], errors)
	errors = variable_field('type', weaken_type, 'Broad Trait Type', weaken_broad, errors)
	errors = variable_fields('descriptor', 'Broad Descriptor', weaken_type, [weaken_descriptor], errors)
	errors = variable_field('descriptor', weaken_type, 'Descriptor', weaken_descriptor, errors)

	errors = check_fields(meta, 'Metamorph', [metamorph], errors)
	errors = check_field(meta, 'Metamorph', 'Sets of Traits', metamorph, errors)

	errors = required_subrule(meta, appear_form, ['single', 'narrow', 'broad', 'any'], PowerChar, 'appear_form', 'is a Metamorph rule', 'Alters Appearance rule that Alters the Characters Form', 'Power', power_id, 'power_id', errors, False, 'extra_id', None)
	
	errors = db_insert('Emotion', Emotion, limited_emotion, limited_emotion_other, errors)

	return (errors)

def create_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	solidity = data['solidity']
	visibility = data['visibility']
	complexity = data['complexity']
	volume = data['volume']
	toughness = data['toughness']
	mass = data['mass']
	damageable = data['damageable']
	maintained = data['maintained']
	repairable = data['repairable']
	moveable = data['moveable']
	stationary = data['stationary']
	trap = data['trap']
	ranged = data['ranged']
	weapon = data['weapon']
	support = data['support']
	real = data['real']
	cover = data['cover']
	conceal = data['conceal']
	incoming = data['incoming']
	outgoing = data['outgoing']
	transform = data['transform']
	transform_type = data['transform_type']
	transform_start_mass = data['transform_start_mass']
	transfom_mass = data['transfom_mass']
	transform_start_descriptor = data['transform_start_descriptor']
	transform_end_descriptor = data['transform_end_descriptor']
	move_player = data['move_player']
	move_check = data['move_check']
	move_opponent_check = data['move_opponent_check']
	move_opposed = data['move_opposed']
	trap_check = data['trap_check']
	trap_opposed = data['trap_opposed']
	trap_resist = data['trap_resist']
	trap_escape = data['trap_escape']
	weapon_damage = data['weapon_damage']
	support_strength = data['support_strength']
	support_strengthen = data['support_strengthen']
	support_action = data['support_action']
	support_action_rounds = data['support_action_rounds']
	support_effort = data['support_effort']
	support_effort_rounds = data['support_effort_rounds']
	cost = data['cost']
	ranks = data['ranks']
	ranged_damage = data['ranged_damage']
	ranged_check = data['ranged_check']
	duration = data['duration']
	duration_type = data['duration_type']
	duration_innate = data['duration_innate']

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)
	errors = id_check(PowerCheckType, move_check, 'Check to Move', errors)
	errors = id_check(PowerOpposedType, move_opposed, 'Opponent Check to Move', errors)
	errors = id_check(PowerCheckType, trap_check, 'Check to Trap', errors)
	errors = id_check(PowerOpposedType, trap_opposed, 'Check to Escape', errors)
	errors = id_check(PowerCheckType, trap_resist, 'Trap Resistance Check', errors)
	errors = id_check(PowerCheckType, ranged_check, 'Ranged Damage Check', errors)
	errors = id_check(PowerDamage, ranged_damage, 'Ranged Damage', errors)
	errors = id_check(PowerDamage, weapon_damage, 'Weapon Damage', errors)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Complex, complexity, 'complexity', errors)

	errors = int_check(volume, 'Volume', errors)
	errors = int_check(toughness, 'Toughness', errors)
	errors = int_check(mass, 'Mass', errors)
	errors = int_check(transform_start_mass, 'Transform Starting Mass', errors)
	errors = int_check(transfom_mass, 'Transform Ending Mass', errors)

	errors = int_check(support_strength, 'Support Strength Rank', errors)
	errors = int_check(support_action, 'Strengthen With Action Modifier', errors)
	errors = int_check(support_action_rounds, 'Strengthen with Action Number of Rounds', errors)
	errors = int_check(support_effort, 'Strengthen with Extra Effort Bonus', errors)
	errors = int_check(support_effort_rounds, 'Strengthen with Extra Effort Number of Rounds', errors)


	errors = together_names('Creating an object', ['Solidity', 'Visibility', 'Complexity', 'Volume Rank', 'Toughness', 'Mass Rank'], [solidity, visibility, complexity, volume, toughness, mass], errors)
	errors = check_fields(moveable, 'Moveable', [move_player], errors)
	errors = check_field(moveable, 'Moveable', 'Moveable With', move_player, errors)
	errors = variable_fields('check', 'Moveable with Check', move_player, [move_check], errors)
	errors = variable_field('check', move_player, 'Check', move_check, errors)
	errors = check_fields(move_opponent_check, 'Opponent Can Move the Object', [move_opposed], errors)
	errors = check_field(move_opponent_check, 'Opponent Can Move the Object', 'Opponent Check', move_opposed, errors)
	errors = check_fields(stationary, 'Stationary', [move_player], errors)
	errors = check_field(stationary, 'Stationary', 'Moveable With', move_player, errors)
	errors = seperate_checks([moveable, stationary], 'Moveable or Stationary', errors)
	
	errors = check_fields(trap, 'Trap', [trap_check, trap_resist], errors)
	errors = check_field(trap, 'Trap', 'Check to Trap', trap_check, errors)
	errors = check_field(trap, 'Trap', 'Check to Hold', trap_resist, errors)
	errors = check_fields(trap_escape, 'Escape Trap', [trap_opposed], errors)
	errors = check_field(trap_escape, 'Escape Trap', 'Opponent Check', trap_opposed, errors)
	
	errors = check_fields(ranged, 'Ranged Attack', [ranged_check, ranged_damage], errors)
	errors = check_field(ranged, 'Ranged Attack', 'Check', ranged_check, errors)
	errors = check_field(ranged, 'Ranged Attack', 'Damage', ranged_damage, errors)

	errors = check_fields(weapon, 'Weapon', [weapon_damage], errors)
	errors = check_field(weapon, 'Weapon', 'Weapon Damage', weapon_damage, errors)

	errors = check_fields(support, 'Supports Weight', [support_strength], errors)
	errors = check_field(support, 'Supports Weight', 'Supports Weight Strength Rank', support_strength, errors)
	errors = check_together_var(support_strengthen, 'Suupports Weight and Can Strengthen', 'Complete the action fields or extra effort fields (or all)', [[support_action, support_action_rounds], [support_effort, support_effort_rounds]], errors)

	errors = check_fields(transform, 'Transform', [transform_type, transform_start_mass, transfom_mass], errors)
	errors = check_field(transform, 'Transform', 'Transform Type', transform_type, errors)
	errors = check_field(transform, 'Transform', 'Transform Starting Mass', transform_start_mass, errors)
	errors = check_field(transform, 'Transform', 'Transform Ending Mass', transfom_mass, errors)

	errors = together('a Transform Descriptor', [transform_start_descriptor, transform_end_descriptor], errors)

	errors = variable_field_required('prop', volume, 'Volume', 'Proportional', 'Proportional', 'Toughness', 'ptop', toughness, errors)
	errors = variable_field_required('prop', toughness, 'Toughness', 'Proportional', 'Proportional', 'Volume', 'ptop', volume, errors)

	errors = check_fields(duration, 'Object Duration', [duration_type], errors)
	errors = check_field(duration, 'Object Duration', 'Duration', duration_type, errors)

	return (errors)

def damage_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	strength = data['strength']
	strength_based = data['strength_based']
	damage_type = data['damage_type']
	descriptor = data['descriptor']
	keyword = data['keyword']
	value_type = data['value_type']
	math = data['math']
	check_type = data['check_type']
	check = data['check_type']
	applied = data['applied']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_multiple(Descriptor, damage_type, 'Damage Type', errors)
	errors = id_multiple(PowerDes, descriptor, 'Descriptor', errors)

	errors = id_check(PowerCheck, check, 'Check', errors)
	errors = id_check(PowerCheckType, check_type, 'Check By Group', errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = id_check(Math, math, 'Math', errors)

	errors = variable_fields('rank', 'Rank Value', value_type, [trait], errors)
	errors = variable_field('rank', value_type, 'Trait', trait, errors)
	errors = variable_fields('check', 'Checked Rank', value_type, [trait], errors)
	errors = variable_field('check', value_type, 'Trait', trait, errors)

	errors = variable_fields('value', 'Flat Value', value_type, [mod], errors)
	errors = variable_fields('value', value_type, 'Value', mod, errors)

	errors = dependent('Math', math, [mod], errors)

	errors = required(value_type, 'Determined By', errors)

	errors = required(keyword, 'Keyword', errors)

	errors = check_fields(strength, 'Strength Based Damage', [strength_based], errors)
	errors = check_field(strength, 'Strength Based Damage', 'Strength Based Type', strength_based, errors)

	errors = seperate([check, check_type], 'Check', errors)

	errors = if_field('Check', check, applied, 'Applied', errors)
	errors = if_field('Check Group', check_type, applied, 'Applied', errors)

	return (errors)

def defense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	defense = data['defense']
	use = data['use']
	mod = data['mod']
	roll = data['roll']
	outcome = data['outcome']
	dodge = data['dodge']
	fortitude = data['fortitude']
	parry = data['parry']
	toughness = data['toughness']
	will = data['will']
	active = data['active']
	resist_area = data['resist_area']
	resist_perception = data['resist_perception']
	reflect = data['reflect']
	immunity = data['immunity']
	reflect_check = data['reflect_check']
	reflect_immune = data['reflect_immune']
	immunity_type = data['immunity_type']
	immunity_trait_type = data['immunity_trait_type']
	immunity_trait = data['immunity_trait']
	immunity_descriptor = data['immunity_descriptor']
	immunity_descriptor_type = data['immunity_descriptor_type']
	immunity_descriptor_count = data['immunity_descriptor_count']
	immunity_damage = data['immunity_damage']
	immunity_rule = data['immunity_rule']
	cover_check = data['cover_check']
	cover_type = data['cover_type']
	immunity_consequence = data['immunity_consequence']
	immunity_suffocate = data['immunity_suffocate']
	immunity_env = data['immunity_env']
	immunity_temp = data['immunity_temp']
	immunity_extremity = data['immunity_extremity']
	immunity_environment = data['immunity_environment']
	immunity_env_penalty = data['immunity_env_penalty']
	immunity_env_circumstance = data['immunity_env_circumstance']
	immunity_condition = data['immunity_condition']
	immunity_except = data['immunity_except']
	immunity_emotion = data['immunity_emotion']
	multiple = data['multiple']
	cost = data['cost']
	ranks = data['ranks']
	force = data['force']
	force_imperv = data['force_imperv']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)

	errors = id_check(PowerCheck, reflect_check, 'Reflect Check', errors)
	errors = id_check(Descriptor, immunity_damage, 'Descriptor', errors)
	errors = id_check(Consequence, immunity_consequence, 'Consequence', errors)
	errors = id_check(Environment, immunity_environment, 'Environment', errors)
	errors = id_check(EnvCondition, immunity_temp, 'Environment Condition', errors)
	errors = id_check(Emotion, immunity_emotion, 'Emotion', errors)

	errors = int_check(immunity_descriptor_count, 'Effect Count', errors)

	errors = variable_field_of('add', use, 'Works With', [dodge, fortitude, parry, toughness, will, active], errors)
	errors = variable_field_of('replace', use, 'Works With', [dodge, fortitude, parry, toughness, will, active], errors)
	errors = variable_field_of('power', defense, 'Works With', [dodge, fortitude, parry, toughness, will, active], errors)
	errors = required_if_any(defense, 'If this rule ihvolves a defense, the Use Type field', use, errors)
	errors = variable_field('mod', use, 'Modifier', mod, errors)
	errors = variable_field('mod_rank', use, 'Modifier', mod, errors)


	errors = together('a die roll', [roll, outcome], errors)
	errors = check_fields(reflect, 'Reflects Attacks', [reflect_check], errors)
	errors = check_field(reflect, 'Reflects Attacks', 'Reflect Check', reflect_check, errors)

	errors = check_fields(immunity, 'immunity', [immunity_type], errors)

	value = immunity_type
	fields = field('Trait Type', immunity_trait_type)
	fields = field('Trait', immunity_trait, fields)
	errors = variable('Trait Immunity', 'trait', value, fields, errors)
	fields = field('Damage Type', immunity_damage)
	errors = variable('Damage Immunity', 'damage', value, fields, errors)
	fields = field('Descriptor', immunity_descriptor)
	errors = variable('Descriptor Immunity', 'descriptor', value, fields, errors)
	fields = field('Rule', immunity_rule)
	errors = variable('Game Rule Immunity', 'rule', value, fields, errors)


	errors = variable_field('descriptor', immunity_type, 'Immune from Descriptor Type', immunity_descriptor_type, errors)

	errors = variable_fields('condition_effect', 'Condition Immunity', immunity_type, [immunity_condition], errors)
	errors = variable_field('condition_effect', immunity_type, 'Condition', immunity_condition, errors)

	errors = variable_fields('condition_attack', 'Condition Immunity', immunity_type, [immunity_condition], errors)
	errors = variable_field('condition_attack', immunity_type, 'Condition', immunity_condition, errors)

	errors = variable_fields('consequence', 'Immune to Consequence', immunity_type, [immunity_consequence], errors)
	errors = variable_field('consequence', immunity_type, 'Consequence', immunity_type, immunity_consequence, errors)
	errors = variable_fields('5', 'Suffocation', immunity_consequence, [immunity_suffocate], errors)
	errors = variable_field('5', immunity_consequence, 'Suffocation Type', immunity_suffocate, errors)

	errors = variable_fields('emotion', 'Immune From Emotion', immunity_type, [immunity_emotion], errors)
	errors = variable_field('emotion', immunity_type, 'Emotion', immunity_emotion, errors)
	
	errors = checked_invalid_option(immunity_except, 'life', immunity_type, 'is an immunity exception', 'immunity exception type', 'life support', errors)

	errors = variable_fields('env', 'Environment Immunity', immunity_type, [immunity_env], errors)
	errors = variable_field('env', immunity_type, 'Environment Immunity Type', immunity_env, errors)
	errors = variable_fields('condition', 'Environment Condition Immunity', immunity_env, [immunity_temp, immunity_extremity], errors)
	errors = variable_field('condition', immunity_env, 'Environment Condition', immunity_temp, errors)
	errors = variable_field('condition', immunity_env, 'Extremity', immunity_extremity, errors)
	errors = variable_fields('env', 'Environment Immunity', immunity_env, [immunity_environment], errors)
	errors = variable_fields('env', immunity_env, 'Environment', immunity_environment, errors)

	errors = power_reflect_immune(power_id, reflect_immune, errors)

	errors = check_fields(cover_check, 'cover', [cover_type], errors)

	return (errors)

def environment_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	radius = data['radius']
	distance = data['distance']
	rank = data['rank']
	condition_check = data['condition_check']
	impede = data['impede']
	conceal = data['conceal']
	visibility = data['visibility']
	immunity = data['immunity']
	immunity_type = data['immunity_type']
	temp_type = data['temp_type']
	immunity_extremity = data['immunity_extremity']
	immunity_environment = data['immunity_environment']
	immunity_environment_other = data['immunity_environment_other']
	no_penalty = data['no_penalty']
	no_circumstance = data['no_circumstance']
	condition_temp_type = data['condition_temp_type']
	temp_extremity = data['temp_extremity']
	move_nature = data['move_nature']
	move_speed = data['move_speed']
	move_cost_circ = data['move_cost_circ']
	move_other = data['move_other']
	conceal_type = data['conceal_type']
	darkness_descriptor = data['darkness_descriptor']
	light_check = data['light_check']
	visibility_trait_type = data['visibility_trait_type']
	visibility_trait = data['visibility_trait']
	visibility_mod = data['visibility_mod']
	cost = data['cost']
	ranks = data['ranks']
	elements = data['elements']
	element = data['element']
	element_strength = data['element_strength']
	element_mass = data['element_mass']

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)
	errors = id_check(PowerCheckType, light_check, 'Counters Darkness Effects Check by Group', errors)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(radius, 'Starting Radius', errors)
	errors = int_check(distance, 'Distance', errors)
	errors = int_check(rank, 'Per Rank', errors)
	errors = int_check(move_speed, 'Movement Speed', errors)
	errors = int_check(visibility_mod, 'Visibility Modifier', errors)
	errors = int_check(element_mass, 'Mass Rank', errors)
	errors = int_check(element_strength, 'Strength Rank', errors)

	errors = id_check(Element, element)

	errors = together_names('an Environmental Effect Range', ['Starting Radius', 'Distance Rank', 'Cost Per Rank'], [radius, distance, rank], errors)

	errors = dependent_of('affects an area of the environment', 'create an Environment Condition, Impede Movement, Create Light or Affects Visibility rule', radius, [condition_check, impede, conceal, visibility], errors)

	errors = check_fields(condition_check, 'Environmental Condition', [condition_temp_type], errors)
	errors = check_field(condition_check, 'Environmental Condition', 'Temperature Type', condition_temp_type, errors)

	errors = variable_fields('1', 'Environmental Condition', condition_temp_type, [temp_extremity], errors)
	errors = variable_field('1', condition_temp_type, 'Extremity', temp_extremity, errors)
	errors = variable_fields('2', 'Environmental Condition', condition_temp_type, [temp_extremity], errors)
	errors = variable_field('2', condition_temp_type, 'Extremity', temp_extremity, errors)
	errors = variable_fields('3', 'Environmental Condition', condition_temp_type, [temp_extremity], errors)
	errors = variable_field('3', condition_temp_type, 'Extremity', temp_extremity, errors)


	errors = check_fields(impede, 'Impedes Movement', [move_nature, move_speed], errors)
	errors = check_field(impede, 'Impedes Movement', 'Impedes Movement Nature Type', move_nature, errors)
	errors = check_field(impede, 'Impedes Movement', 'Impedes Movement Speed Modifier', move_speed, errors)
	errors = select_variable('other', move_nature, 'another nature type for impeding movement', 'other', move_other, errors)

	errors = check_fields(conceal, 'Light', [conceal_type], errors)
	errors = check_field(conceal, 'Light', 'Counters Concealment Type', conceal_type, errors)
	errors = check_fields(darkness_descriptor, 'Counters Darkness Descriptor Effects', [light_check], errors)
	errors = check_field(darkness_descriptor, 'Counters Darkness Descriptor Effects', 'Counter Check by Group', light_check, errors)

	errors = check_fields(visibility, 'Visibility', [visibility_trait_type, visibility_trait, visibility_mod], errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Trait Type', visibility_trait_type, errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Trait', visibility_trait, errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Modifier', visibility_mod, errors)
	
	errors =  check_fields(elements, 'Element Control', [element, element_mass, element_strength], errors)
	errors =  check_field(elements, 'Element Control', 'Element', element, errors)
	errors =  check_field(elements, 'Element Control', 'Mass Eank', element_mass, errors)
	errors =  check_field(elements, 'Element Control', 'Strength Rank',  element_strength, errors)

	errors = check_fields(immunity, 'Immunity', [immunity_type], errors)
	errors = check_field(immunity, 'Immunity', 'Immunity Type', immunity_type, errors)

	errors = variable_fields('environment', 'Environment Immunity', immunity_type, [immunity_environment], errors)
	errors = variable_field('environment', immunity_type, 'Environment Type', immunity_environment, errors)
	errors = variable_fields('other', 'Other Environment', immunity_environment, [immunity_environment_other], errors)
	errors = variable_fields('condition', 'Condition Immunity', immunity_type, [temp_type, immunity_extremity], errors)
	errors = variable_field('condition', immunity_type, 'Condition Type', temp_type, errors)
	errors = variable_fields('condition', immunity_type, 'Condition Extremity', immunity_extremity, errors)

	errors = db_insert('Environment', Environment, immunity_environment, immunity_environment_other, errors)






	return (errors)

def levels_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	level_type = data['level_type']
	level = data['level']
	level_effect = data['level_effect']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = required(level_type, 'Level Type', errors)
	errors = required(level, 'Level', errors)
	errors = required(level_effect, 'Level Effect', errors)
	

	return (errors)

def minion_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	attitude_attitude = data['attitude_attitude']
	attitude_type = data['attitude_type']
	attitude_trait_type = data['attitude_trait_type']
	attitude_trait = data['attitude_trait']
	resitable_check = data['resitable_check']
	resitable_dc = data['resitable_dc']
	multiple_value = data['multiple_value']
	multiple_type = data['multiple_type']
	horde = data['horde']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Levels, attitude_type, 'level', errors)
	errors = id_check(Defense, resitable_check, 'defense', errors)
	
	errors  = int_check(points, 'Points', errors)
	errors  = int_check(sacrifice_cost, 'Sacrifice Cost', errors)
	errors  = int_check(resitable_dc, 'Resistable DC', errors)
	errors  = int_check(multiple_value, 'Multiple Minion Value', errors)

	errors = required(points, 'Points', errors)
	errors = required(condition, 'Minion Condition', errors)
	errors = required(player_condition, 'Player Condition While Summoning', errors)
	errors = required(variable_type, 'Minion Type', errors)

	errors = check_fields(multiple, 'Multiple Minions', [multiple_value, multiple_type], errors)
	errors = check_field(multiple, 'Multiple Minions', 'Multiple Value', multiple_value, errors)
	errors = check_field(multiple, 'Multiple Minions', 'Rank Type', multiple_type, errors)
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

	return (errors)

def mod_post_errors(data):

	errors = {'error': False, 'error_msgs': []}
	
	power_id = data['power_id']
	extra_id = data['extra_id']
	affects_objects = data['affects_objects']
	area = data['area']
	persistent = data['persistent']
	incurable = data['incurable']
	selective = data['selective']
	limited = data['limited']
	innate = data['innate']
	others = data['others']
	sustained = data['sustained']
	reflect = data['reflect']
	redirect = data['redirect']
	half = data['half']
	affects_corp = data['affects_corp']
	continuous = data['continuous']
	vulnerable = data['vulnerable']
	precise = data['precise']
	progressive = data['progressive']
	subtle = data['subtle']
	permanent = data['permanent']
	points = data['points']
	ranks_check = data['ranks_check']
	action = data['action']
	side_effect = data['side_effect']
	concentration = data['concentration']
	simultaneous = data['simultaneous']
	effortless = data['effortless']
	noticeable = data['noticeable']
	unreliable = data['unreliable']
	objects_alone = data['objects_alone']
	objects_character = data['objects_character']
	effortless_degree_type = data['effortless_degree_type']
	effortless_degree = data['effortless_degree']
	effortless_retries = data['effortless_retries']
	simultaneous_descriptor = data['simultaneous_descriptor']
	area_type = data['area_type']
	area_damage = data['area_damage']
	area_ranged = data['area_ranged']
	area_descriptor = data['area_descriptor']
	limited_type = data['limited_type']
	limited_mod = data['limited_mod']
	limited_level_degree = data['limited_level_degree']
	limited_level = data['limited_level']
	limited_source_type = data['limited_source_type']
	limited_source = data['limited_source']
	limited_task_type = data['limited_task_type']
	limited_task = data['limited_task']
	limited_trait_type = data['limited_trait_type']
	limited_trait = data['limited_trait']
	limited_description = data['limited_description']
	limited_subjects = data['limited_subjects']
	limited_extra = data['limited_extra']
	limited_language_type = data['limited_language_type']
	limited_degree_type = data['limited_degree_type']
	limited_degree = data['limited_degree']
	limited_degree_effect = data['limited_degree_effect']
	limited_sense = data['limited_sense']
	limited_subsense = data['limited_subsense']
	limited_descriptor = data['limited_descriptor']
	limited_range_type = data['limited_range_type']
	limited_range = data['limited_range']
	limited_ground = data['limited_ground']
	limited_creature = data['limited_creature']
	limited_creature_narrow = data['limited_creature_narrow']
	limited_creature_other = data['limited_creature_other']
	limited_env_other = data['limited_env_other']
	limited_env = data['limited_env']
	limited_emotion = data['limited_emotion']
	limited_emotion_other = data['limited_emotion_other']
	limited_material = data['limited_material']
	side_effect_type = data['side_effect_type']
	side_level = data['side_level']
	side_other = data['side_other']
	reflect_check = data['reflect_check']
	reflect_descriptor = data['reflect_descriptor']
	subtle_type = data['subtle_type']
	subtle_opposed = data['subtle_opposed']
	subtle_null_trait_type = data['subtle_null_trait_type']
	subtle_null_trait = data['subtle_null_trait']
	others_type = data['others_type']
	others_req = data['others_type']
	others_opposed = data['others_opposed']
	others_check = data['others_check']
	others_carry = data['others_carry']
	others_touch = data['others_touch']
	others_touch_continuous = data['others_touch_continuous']
	ranks_trait_type = data['ranks_trait_type']
	ranks_trait = data['ranks_trait']
	ranks_ranks = data['ranks_ranks']
	ranks_mod = data['ranks_mod']
	points_type = data['points_type']
	points_reroll_target = data['points_reroll_target']
	points_reroll_cost = data['points_reroll_cost']
	points_rerolls = data['points_rerolls']
	points_reroll_result = data['points_reroll_result']
	points_give = data['points_give']
	points_negate = data['points_negate']
	ranks = data['ranks']
	cost = data['cost']
	extra = data['extra']
	extra_count = data['extra_count']
	extra_degree = data['extra_degree']
	extra_dc = data['extra_dc']
	extra_circ = data['extra_circ']
	feedback_mod = data['feedback_mod']
	feedback = data['feedback']
	feedback_effect = data['feedback_effect']
	feedback_type = data['feedback_type']
	feedback_cover = data['feedback_cover']
	feedback_defense = data['feedback_defense']
	adv = data['adv']
	advantage = data['advantage']
	advantage_rank = data['advantage_rank']
	advantage_rank_per = data['advantage_rank_per']
	advantage_bonus = data['advantage_bonus']
	advantage_damage = data['advantage_damage']
	advantage_damage_bonus = data['advantage_damage_bonus']
	advantage_damage_bonus_rank = data['advantage_damage_bonus_rank']
	precise_type = data['precise_type']
	sustained_action = data['sustained_action']
	concentration_type = data['concentration_type']
	concentration_check = data['concentration_check']
	concentration_check_type = data['concentration_check_type']
	concentration_opposed = data['concentration_opposed']
	unreliable_type = data['unreliable_type']
	incurable_type = data['incurable_type']
	progressive_type = data['progressive_type']
	progressive_degree = data['progressive_degree']
	progressive_degree_type = data['progressive_degree_type']
	cumulative = data['cumulative']
	cumulative_degree = data['cumulative_degree']
	persistent_type = data['persistent_type']
	persistent_degree = data['persistent_degree']

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)
	errors = id_check(PowerDamage, area_damage, 'Damage Effect', errors)
	errors = id_check(PowerRangedType, area_ranged, 'Ranged by Group', errors)
	errors = id_check(PowerCheck, reflect_check, 'check', errors)
	errors = id_check(PowerOpposedType, subtle_opposed, 'Opponent Check', errors)
	errors = id_check(PowerCircType, extra_circ, 'Extra Circumstance', errors)
	errors = id_check(PowerDCType, extra_dc, 'Extra DC', errors)
	errors = id_check(PowerDegreeType, extra_degree, 'Extra Degree', errors)
	errors = id_check(PowerDegree, limited_degree, 'Degree'. errors)
	errors = id_check(PowerCheck, concentration_check, 'Concentration Check', errors)
	errors = id_check(PowerCheckType, concentration_check_type, 'Concentration Check by Group', errors)
	errors = id_check(PowerOpposedType, concentration_opposed, 'Concentration Opponent Check Group', errors)
	errors = id_check(PowerDegree, progressive_degree, 'Progressive Degree', errors)
	errors = id_check(PowerDegreeType, progressive_degree_type, 'Progressive Degree by Group', errors)
	errors = id_check(PowerDegreeType, cumulative_degree, 'Cumulative Degree Group', errors)
	errors = id_check(PowerDegreeType, persistent_degree, 'Persistent Degree Group', errors)
	errors = id_check(PowerCheckType, others_check, 'Affects Others Variable Check Group', errors)
	errors = id_check(PowerOpposedType, others_opposed, 'Affects Others Opponent Check Group', errors)
	errors = id_check(PowerDamage, advantage_damage, 'Advantage Damage', errors)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Defense, objects_alone, 'defense', errors)
	errors = id_check(Defense, objects_character, 'defense', errors)
	errors = id_check(Levels, limited_level, 'level', errors)
	errors = id_check(Extra, limited_extra, 'extra', errors)
	errors = id_check(Sense, limited_sense, 'sense', errors)
	errors = id_check(PowerRsnged, limited_range, 'range', errors)
	errors = id_check(Levels, side_level, 'level', errors)
	errors = id_check(Ground, limited_ground, 'Ground Type', errors)
	errors = id_check(Creature, limited_creature, 'Creature', errors)
	errors = id_check(NarrowCreature, limited_creature_narrow, 'Narrow Creature', errors)
	errors = id_check(Environment, limited_env, 'Environment', errors)
	errors = id_check(Emotion, limited_emotion, 'Emotion', errors)
	errors = id_check(Material, limited_material, 'Material', errors)
	errors = id_check(Advantage, advantage, 'Advantage', errors)
	errors = id_check(Action, sustained_action, 'Sustained Action', errors)
	errors = id_check(Cover, feedback_cover, 'Feedback Cover', errors)
	errors = id_check(Defense, feedback_defense, 'Feedback Defense', errors)

	errors = id_check(PowerDegree, effortless_degree, 'Effortless Degree', errors)

	errors = int_check(limited_mod, 'Limited Modifier', errors)
	errors = int_check(limited_subjects, 'limited by Number of Subjects', errors)
	errors = int_check(limited_degree, 'limited by Degree', errors)
	errors = int_check(ranks_ranks, 'Number of Ranks', errors)
	errors = int_check(ranks_mod, 'Ranks Modifier', errors)
	errors = int_check(points_reroll_cost, 'Reroll Cost', errors)
	errors = int_check(points_rerolls, 'Number of Rerolls', errors)
	errors = int_check(extra_count, 'Extra Effect Count', errors)
	errors = int_check(points_give, 'Points Given Per Round', errors)
	errors = int_check(feedback_mod, 'Feedback Resistance Modifier', errors)
	errors = int_check(advantage_rank, 'Advantage Ranks', errors)
	errors = int_check(points_negate, 'Negate Reroll Cost', errors)
	errors = int_check(advantage_damage_bonus, 'Advantage Damage Bonus', errors)

	errors = check_fields(affects_objects, 'Affects Objects', [objects_alone, objects_character], errors)
	errors = check_field(affects_objects, 'Affects Objects', 'Affect Object Alone', objects_alone, errors)
	errors = check_field(affects_objects, 'Affects Objects', 'Affect Object with Character', objects_character, errors)
	
	errors = check_fields(area, 'Area', [area_type], errors)
	errors = check_field(area, 'Area', 'Area Type', area_type, errors)
	errors = variable_fields('descriptor', 'Affects All Targets in Area with Descriptor', area_type, [area_descriptor], errors)
	errors = variable_field('descriptor', area_type, 'Area Descriptor', area_descriptor, errors)
	errors = variable_fields('attach_descriptor', 'Attsches to All Targets in Area with Descriptor', area_type, [area_descriptor], errors)
	errors = variable_field('attach_descriptor', area_type, 'Area Descriptor', area_descriptor, errors)
	errors = variable_fields('range', 'Works with all Targets in Range', area_type, [area_ranged], errors)
	errors = variable_field('range', area_type, 'Range by Group', area_ranged, errors)

	errors = check_fields(limited, 'Limited', [limited_type, limited_mod], errors)
	errors = check_field(limited, 'Limited', 'Limited Type', limited_type, errors)
	errors = check_field(limited, 'Limited', 'Limited Modifier', limited_mod, errors)


	errors = variable_fields('task_type', 'Limited by Task Type', limited_type, [limited_task_type], errors)
	errors = variable_field('task_type', limited_type, 'Task Type', limited_task_type, errors)

	errors = variable_fields('task', 'Limited to All tasks but One', limited_type, [limited_task], errors)
	errors = variable_field('task', limited_type, 'Task', limited_task, errors)

	errors = variable_fields('trait', 'Limited by Trait', limited_type, [limited_trait_type, limited_trait], errors)
	errors = variable_field('trait', limited_type, 'Trait Type', limited_trait_type, errors)
	errors = variable_field('trait',  limited_type,'Trait', limited_trait, errors)

	errors = variable_fields('descriptor', 'Limited by Descriptor', limited_type, [limited_descriptor], errors)
	errors = variable_field('descriptor', limited_type, 'Descriptor', limited_descriptor, errors)

	errors = variable_fields('subjects', 'Limited by Number of Subjects', limited_type, [limited_subjects], errors)
	errors = variable_field('subjects', limited_type, 'Number of Subjects', limited_subjects, errors)

	errors = variable_fields('language', 'Limited by Different Language', limited_type, [limited_language_type], errors)
	errors = variable_field('language', limited_type, 'Different Language Effect', limited_language_type, errors)

	errors = variable_fields('extra', 'Limited to Extra Effect', limited_type, [limited_extra], errors)
	errors = variable_field('extra', limited_type, 'Extra', limited_extra, errors)

	errors = variable_fields('degree', 'Limited by Degree of Success', limited_type, [limited_degree, limited_degree_type, limited_degree_effect], errors)
	errors = variable_field('degree', limited_type, 'Degree of Success', limited_degree, errors)
	errors = variable_field('degree', limited_type, 'Degree Type', limited_degree_type, errors)
	errors = variable_field('degree', limited_type, 'Effects', limited_degree_effect, errors)
	errors = incompatible_multiple('this', limited_degree_effect, ['>', '>=', '<', '<='], limited_degree_tpe, 'is limited to this degrees effect', 'degree type', '=', errors)

	errors = variable_fields('sense', 'Limited by Sense', limited_type, [limited_sense], errors)
	errors = variable_field('sense', limited_type, 'Sense', limited_sense, errors)

	errors = variable_fields('range', 'Limited by Range', limited_type, [limited_range, limited_range_type], errors)
	errors = variable_field('range', limited_type, 'Range', limited_range, errors)
	errors = variable_field('range', limited_type, 'Range', limited_range_type, errors)

	errors = variable_fields('source', 'Requires Descriptor', limited_type, [limited_source_type, limited_source], errors)
	errors = variable_field('source', limited_type, 'Descriptor Type', limited_source_type, errors)
	errors = variable_field('source', limited_type, 'Required Descriptor', limited_source, errors)

	errors = variable_fields('other', 'Limited by Other', limited_type, [limited_description], errors)
	errors = variable_field('other', limited_type, 'Other Factor', limited_description, errors)

	errors = variable_fields('level', 'Limited by Level', limited_type, [limited_mod, limited_level_degree, limited_level], errors)
	errors = variable_field('level', limited_type, 'Level', limited_level, errors)
	errors = variable_field('level', limited_type, 'Level Degree', limited_level_degree, errors)
	errors = variable_field('level', limited_type, 'Modifier', limited_mod, errors)
	
	errors = variable_fields('to_level', 'Limited to Level', limited_type, [limited_level_degree, limited_level], errors)
	errors = variable_field('level', limited_type, 'Level', limited_level, errors)
	errors = variable_field('level', limited_type, 'Level Degree', limited_level_degree, errors)

	errors = variable_fields('ground', 'Limited by Ground Type', limited_type, [limited_ground], errors)
	errors = variable_field('ground', limited_type, 'Ground Type', limited_ground, errors)

	errors = variable_fields('ground', 'Limited by Material Type', limited_type, [limited_material], errors)
	errors = variable_field('ground', limited_type, 'Material Type', limited_material, errors)

	errors = variable_fields('creature', 'Limited to Creature', limited_type, [limited_creature], errors)
	errors = variable_field('creature', limited_type, 'Creature Type', limited_creature, errors)
	errors = variable_fields('other', 'Other Creature', limited_creature, [limited_creature_other], errors)
	errors = variable_field('other', limited_creature, 'Other Creature', limited_creature_other, errors)
	errors = variable_fields('other', 'Other Nsrrow Creature', limited_creature_narrow, [limited_creature_other], errors)
	errors = variable_field('other', limited_creature_narrow, 'Other Creature', limited_creature_other, errors)

	errors = variable_fields('env', 'Limited to Environment', limited_type, [limited_env], errors)
	errors = variable_field('env', limited_type, 'Environment', limited_env, errors)
	errors = variable_fields('other', 'Other Environment', limited_env, [limited_env_other], errors)
	errors = variable_field('other', limited_env, 'Other Environment', limited_env_other, errors)

	errors = variable_fields('emotion', 'Limited to Emotion', limited_type, [limited_emotion], errors)
	errors = variable_field('emotion', limited_type, 'Emotion', limited_emotion, errors)
	errors = variable_fields('other', 'Other Emotion', limited_emotion, [limited_emotion_other], errors)
	errors = variable_field('other', limited_emotion, 'Other Emotion', limited_emotion_other, errors)

	errors = check_of(others, 'Affects Others', [others_carry, others_touch], errors)

	errors = check_fields(reflect, 'Reflect', [reflect_check, reflect_descriptor], errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Check Type', reflect_check, errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Descriptor', reflect_descriptor, errors)

	errors = check_fields(subtle, 'Subtle', [subtle_type], errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Type', subtle_type, errors)
	errors = variable_fields('detect', 'Detectable', subtle_type, [subtle_opposed], errors)
	errors = variable_field('detect', subtle_type, 'Subtle Opponent Check', subtle_opposed, errors)
	errors = variable_fields('detect_trait', 'Detectable Only With Nullifying Trait', subtle_type, [subtle_opposed, subtle_null_trait_type, subtle_null_trait], errors)
	errors = variable_field('detect_trait', subtle_type, 'Trait Type', subtle_null_trait_type, errors)
	errors = variable_field('detect_trait', subtle_type, 'Trait', subtle_null_trait, errors)
	errors = variable_field('detect_trait', subtle_type, 'Subtle Opponent Check', subtle_opposed, errors)

	
	errors = check_fields(points, 'Spend Points', [points_type], errors)
	errors = check_field(points, 'Spend Points', 'Spend Points Type', points_type, errors)
	errors = variable_fields('reroll', 'Re-roll', points_type, [points_reroll_target, points_reroll_cost, points_rerolls], errors)
	errors = variable_field('reroll', points_type, 'Number of Rerolls', points_rerolls, errors)
	errors = variable_field('reroll', points_type, 'Re-roll Cost', points_reroll_cost, errors)
	errors = variable_field('reroll', points_type, 'Re-roll Target', points_reroll_target, errors)
	errors = variable_fields('give', 'Give Points', points_type, [points_give], errors)
	errors = variable_field('give', points_type, 'Points Given Per Round', points_give, errors)
	errors = variable_fields('negate', 'Negate Reroll', points_type, [points_negate], errors)
	errors = variable_field('negate', points_type, 'Negate Reroll Cost', points_negate, errors)
	
	errors = check_fields(ranks_check, 'Gain Trait', [ranks_trait_type, ranks_trait, ranks_ranks, ranks_mod], errors)
	errors = check_field(ranks_check, 'Gain Trait', 'Trait Type', ranks_trait_type, errors)
	errors = check_field(ranks_check, 'Gain Trait', 'Trait', ranks_trait, errors)
	errors = check_field(ranks_check, 'Gain Trait', 'Ranks', ranks_ranks, errors)
	errors = check_field(ranks_check, 'Gain Trait', Modifier, ranks_mod, errors)
	
	errors = check_fields(side_effect, 'Side Effect', [side_effect_type], errors)
	errors = check_field(side_effect, 'Side Effect', 'Side Effect Type', side_effect_type, errors)
	errors = variable_fields('level', 'Side Effect Level', side_effect_type, [side_level], errors) 
	errors = variable_field('other', 'Side Effect Other', side_effect_type, [side_other], errors)

	errors = check_fields(simultaneous, 'Simultaneous', [simultaneous_descriptor], errors)
	errors = check_field(simultaneous, 'Simultaneous', 'Descriptor', simultaneous_descriptor, errors)
	
	errors = check_fields(effortless, 'Effortless', [ effortless_degree,  effortless_degree_type], errors)
	errors = check_field(effortless, 'Effortless', 'Degree Type',  effortless_degree_type, errors)
	errors = check_field(effortless, 'Effortless', 'Degree',  effortless_degree, errors)

	errors = check_fields(extra, 'Extra Effect', [extra_count], errors)
	errors = check_field(extra, 'Extra Effect', 'Count', extra_count, errors)
	errors = check_of(extra, 'Extra Effect', 'a degree, circumstance or dc', [extra_dc, extra_degree, extra_circ], errors)
	
	errors = check_fields(feedback, 'Feedback', [feedback_effect, feedback_type, feedback_cover], errors)
	errors = check_field(feedback, 'Feedback', 'Feedback Type', feedback_effect, errors, True)
	errors = check_field(feedback, 'Feedback', 'Resistance', feedback_type, errors)
	errors = check_field(feedback, 'Feedback', 'Feedbacl Cover', feedback_cover, errors)

	errors = check_fields(persistent, 'Persistent', [persistent_type], errors)
	errors = check_field(persistent, 'Persistent', 'Persistent Type', persistent_type, errors, True)
	errors = variable_fields('degree', 'Degree Effect Works on Incurable', persistent_type, [persistent_degree], errors)
	errors = variable_field('degree', persistent_type, 'Persaistent Degree Group', persistent_degree, errors)

	errors = variable_fields('mod', 'Feedback', feedback_type, [feedback_mod], errors)
	errors = variable_field('mod', feedback_type, 'Feedback Resistance Modifier', feedback_mod, errors)
	errors = variable_fields('defense', 'Feedback', feedback_type, [feedback_defense], errors)
	errors = variable_field('defense', feedback_type, 'Feedback Defense', feedback_defense, errors)
	
	errors = check_fields(adv, 'Advantage Ranks', [advantage, advantage_rank], errors)
	errors = check_field(adv, 'Advantage Ranks', 'Advantage', advantage, errors)
	errors = check_field(adv, 'Advantage Ranks', 'Rsnks', advantage_rank, errors)
	errors = check_fields(advantage_bonus, 'Advantage Damage Bonus', [advantage_damage, advantage_damage_bonus], errors)
	errors = check_field(advantage_bonus, 'Advantage Damage Bonus', 'Damage Effect', advantage_damage, errors)
	errors = check_field(advantage_bonus, 'Advantage Damage Bonus', 'Damage Bonus', advantage_damage_bonus, errors)

	errors = check_fields(precise, 'Precise', [precise_type], errors)
	errors = check_field(precise, 'Precise', 'Precise Type', precise_type, errors)

	errors = check_fields(sustained, 'Sustained', [sustained_action], errors)
	errors = check_field(sustained, 'Sustained', 'Action to Sustain', sustained_action, errors)

	errors = check_fields(concentration_check, 'Concentration', [concentration_type], errors)
	errors = variable_fields('opposed', 'Success on Opponent Check', concentration_type, [concentration_opposed], errors)
	errors = variable_field('opposed', concentration_type, 'Opponent Check by Group', concentration_opposed, errors)
	errors = variable_fields_of('check', concentration_type, 'Success on Check', [concentration_check, concentration_check_type], errors)	
	errors = seperate([concentration_check, concentration_check_type, concentration_opposed], 'Concentration', errors)
	errors = check_of(concentration, 'Concentration', 'Concentration Check', [concentration_check, concentration_check_type, concentration_opposed], errors)
	
	errors = check_fields(unreliable, 'Unreliable', [unreliable_type], errors)
	errors = check_field(unreliable, 'Unreliable', 'Unreliable Type', unreliable_type, errors)
	
	errors = check_fields(incurable, 'Incurable', [incurable_type], errors)
	errors = check_field(incurable, 'Incurable', 'Incurable Type', incurable_type, errors)

	errors = check_fields(progressive, 'Progressive', [progressive_type], errors)
	errors = check_field(progressive, 'Progressive', 'Progressive Type', progressive_type, errors)
	errors = variable_fields('increase', 'Increase Effect Degree', progressive_type, [progressive_degree_type], errors)
	errors = variable_field('increase', progressive_type, 'Degree by Group', progressive_degree_type, errors)
	errors = variable_fields('repeat', 'Repeat Degree Effect', progressive_type, [progressive_degree], errors)
	errors = variable_field('repeat', progressive_type, 'Repeat Degree Effect', progressive_degree, errors)
	errors = required_entry_multiple('rank', progressive_type, 'Power', 'Progressive Effect Through the Powers Rank Effects', 'Variable Rank', PowerRanks, 'power_id', power_id, errors, None, 'extra')

	errors = check_fields(cumulative, 'Cumulative', [cumulative_degree], errors)
	errors = check_field(cumulative, 'Cumulative', 'Degree of Success/Failure Group', cumulative_degree, errors)
	
	errors = check_fields(others, 'Affects Others', [others_type], errors)
	errors = check_field(others, 'Affects Others', 'Affects Others Type', others_type, errors)
	errors = variable_fields('attack_check', others_type, 'Impose Effect with Variable Check', [others_check], errors)
	errors = variable_field('attack_check', others_type, 'Variable Check Group', others_check, errors)
	errors = variable_fields('attack_opposed', others_type, 'Impose Effect with Opponent Check', [others_opposed], errors)
	errors = variable_field('attack_opposed', others_type, 'Variable Check Group', others_opposed, errors)

	return (errors)

	

def ranged_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	range_type = data['range_type']
	flat_value = data['flat_value']
	flat_units = data['flat_units']
	flat_rank = data['flat_rank']
	flat_rank_value = data['flat_rank_value']
	flat_rank_units = data['flat_rank_units']
	flat_rank_rank = data['flat_rank_rank']
	flat_rank_distance = data['flat_rank_distance']
	flat_rank_distance_rank = data['flat_rank_distance_rank']
	units_rank_start_value = data['units_rank_start_value']
	units_rank_value = data['units_rank_value']
	units_rank_units = data['units_rank_units']
	units_rank_rank = data['units_rank_rank']
	rank_distance_start = data['rank_distance_start']
	rank_distance = data['rank_distance']
	rank_effect_rank = data['rank_effect_rank']
	effect_mod_math = data['effect_mod_math']
	effect_mod = data['effect_mod']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_math = data['check_math']
	check_mod = data['check_mod']
	trait_trait_type = data['trait_trait_type']
	trait_trait = data['trait_trait']
	trait_math = data['trait_math']
	trait_mod = data['trait_mod']
	distance_mod_rank = data['distance_mod_rank']
	distance_mod_math = data['distance_mod_math']
	distance_mod_trait_type = data['distance_mod_trait_type']
	distance_mod_trait = data['distance_mod_trait']
	dc = data['dc']
	circ = data['circ']
	degree = data['degree']
	damage = data['damage']
	keyword = data['keyword']
	title = data['title']
	general = data['general']
	penalty_math = data['penalty_math']
	penalty_mod = data['penalty_mod']
	penalty_trait_type = data['penalty_trait_type']
	penalty_trait = data['penalty_trait']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Unit, flat_units, 'unit', errors)
	errors = id_check(Unit, flat_rank_units, 'unit', errors)
	errors = id_check(Unit, units_rank_units, 'unit', errors)
	errors = id_check(Math, effect_mod_math, 'math', errors)
	errors = id_check(Math, check_math, 'math', errors)
	errors = id_check(Math, trait_math, 'math', errors)
	errors = id_check(Math, distance_mod_math, 'math', errors)
	errors = id_check(Range, general, 'General Range', errors)
	errors = id_check(Math, penalty_math, 'Math', errors)

	errors = id_check(PowerCirc, circ, 'Circumstance Modifier', errors)
	errors = id_check(PowerDamage, damage, 'Damage', errors)
	errors = id_check(PowerDC, dc, 'DC', errors)
	errors = id_check(PowerDegree, degree, 'Degree of Success/Failure', errors)

	errors = int_check(flat_value, 'Flat Value', errors)
	print(errors)
	errors = int_check(flat_rank, 'Rank', errors)
	errors = int_check(flat_rank_value, 'Value', errors)
	errors = int_check(flat_rank_rank, 'Rank', errors)
	errors = int_check(flat_rank_distance, 'Distance', errors)
	errors = int_check(flat_rank_distance_rank, 'Rank', errors)
	errors = int_check(units_rank_start_value, 'Start Value', errors)
	errors = int_check(units_rank_value, 'Value', errors)
	errors = int_check(units_rank_rank, 'Rank', errors)
	errors = int_check(rank_distance_start, 'Start Distance', errors)
	errors = int_check(rank_distance, 'Distance', errors)
	errors = int_check(rank_effect_rank, 'Rank', errors)
	errors = int_check(effect_mod, 'Mod Value', errors)
	errors = int_check(check_mod, 'Mod Value', errors)
	errors = int_check(trait_mod, 'Mod Value', errors)
	errors = int_check(distance_mod_rank, 'Rank', errors)
	errors = int_check(dc_value, 'DC Value', errors)
	
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = variable_fields('flat_units', 'Flat Units', range_type, [flat_value, flat_units], errors)
	errors = variable_field('flat_units', range_type, 'Distance',  flat_value, errors)
	errors = variable_field('flat_units', range_type, 'Units', flat_units, errors)

	errors = variable_fields('distance_rank', 'Flat Distance Rank', range_type, [flat_rank], errors)
	errors = variable_field('distance_rank', range_type, 'Distance Rank', flat_rank, errors)

	errors = variable_fields('flat_rank_units', 'Flat Units By Rank', range_type, [flat_rank_value, flat_rank_units, flat_rank_rank], errors)
	errors = variable_field('flat_rank_units', range_type, 'Distance', flat_rank_value, errors)
	errors = variable_field('flat_rank_units', range_type, 'Units', flat_rank_units, errors)
	errors = variable_field('flat_rank_units', range_type, 'Rank', flat_rank_rank, errors)

	errors = variable_fields('flat_rank_distance', 'Flat Distance Rank By Rank', range_type, [flat_rank_distance, flat_rank_distance_rank], errors)
	errors = variable_field('flat_rank_distance', range_type, 'Distance Rank', flat_rank_distance, errors)
	errors = variable_field('flat_rank_distance', range_type, 'Effect Rank', flat_rank_distance_rank, errors)

	errors = variable_fields('units_rank', 'Units Per Rank', range_type, [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank], errors)
	errors = variable_field('units_rank', range_type, 'Starting Distance', units_rank_start_value, errors)
	errors = variable_field('units_rank', range_type, 'Distance', units_rank_value, errors)
	errors = variable_field('units_rank', range_type, 'Units', units_rank_units, errors)
	errors = variable_field('units_rank', range_type, 'Effect Rank', units_rank_rank, errors)

	errors = variable_fields('rank_rank', 'Distance Rank Per Rank', range_type, [rank_distance_start, rank_distance, rank_effect_rank], errors)
	errors = variable_field('rank_rank', range_type, 'Starting Distance', rank_distance_start, errors)
	errors = variable_field('rank_rank', range_type, 'Distance Rank', rank_distance, errors)
	errors = variable_field('rank_rank', range_type, 'Effect Rank', rank_effect_rank, errors)

	errors = variable_fields('effect_mod', 'Effect Rank Modifier', range_type, [effect_mod_math, effect_mod], errors)
	errors = variable_field('effect_mod', range_type, 'Math', effect_mod_math, errors)
	errors = variable_field('effect_mod', range_type, 'Modifier', effect_mod, errors)

	errors = variable_fields('trait_mod', 'Trait Rank Modifier', range_type, [trait_trait_type, trait_trait, trait_math, trait_mod], errors)
	errors = variable_field('trait_mod', range_type, 'Trait Type', trait_trait_type, errors)
	errors = variable_field('trait_mod', range_type, 'Trait', trait_trait, errors)
	errors = variable_field('trait_mod', range_type, 'Math', trait_math, errors)
	errors = variable_field('trait_mod', range_type, 'Modifier', trait_mod, errors)

	errors = variable_fields('distance_mod', 'Distance Rank Modifier', range_type, [distance_mod_rank, distance_mod_math, distance_mod_trait_type, distance_mod_trait], errors)
	errors = variable_field('distance_mod', range_type, 'Distance', distance_mod_rank, errors)
	errors = variable_field('distance_mod', range_type, 'Math', distance_mod_math, errors)
	errors = variable_field('distance_mod', range_type, 'Trait Type', distance_mod_trait_type, errors)
	errors = variable_field('distance_mod', range_type, 'Trait', distance_mod_trait, errors)

	errors = variable_fields('check', 'Check Result', range_type, [check_trait_type, check_trait, check_math, check_mod], errors)
	errors = variable_field('check', range_type, 'Trait Type', check_trait_type, errors)
	errors = variable_field('check', range_type, 'Trait', check_trait, errors)
	errors = variable_field('check', range_type, 'Math', check_math, errors)
	errors = variable_field('check', range_type, 'Modifier', check_mod, errors)

	errors = variable_fields('penalty', 'Range Penalty Modifier', range_type, [penalty_math, penalty_mod, penalty_trait_type, penalty_trait], errors)
	errors = variable_field('penalty', range_type, 'Math', penalty_math, errors)
	errors = variable_field('penalty', range_type, 'Modifier', penalty_mod, errors)
	errors = variable_field('penalty', range_type, 'Trsit Type', penalty_trait_type, errors)
	errors = variable_field('penalty', range_type, 'Trait', penalty_trait, errors)

	errors = variable_fields('general', 'General Range', range_type, [general], errors)




	return (errors)


def resist_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	mod = data['mod']
	rounds = data['rounds']
	circumstance = data['circumstance']
	resist_check_type = data['resist_check_type']
	trait_type = data['trait_type']
	trait = data['trait']
	descriptor = data['descriptor']
	requires_check = data['requires_check']
	check_type = data['check_type']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Check, check_type, 'check', errors)
	
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)
	
	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Rounds', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('descriptor', 'Descriptor', resist_check_type, [descriptor], errors)
	errors = variable_fields('trait', 'Check Type', resist_check_type, [trait_type, trait], errors)
	errors = variable_field('trait', resist_check_type, 'Trait Type', trait_type, errors)
	errors = variable_field('trait', resist_check_type, 'Trait', trait, errors)
	errors = check_fields(requires_check, 'Requires Check', [check_type, check_trait_type, check_trait], errors)
	errors = check_field(requires_check, 'Requires Check', 'Check Type', check_type, errors)
	errors = check_field(requires_check, 'Requires Check', 'Check Trait Type', check_trait_type, errors)
	errors = check_field(requires_check, 'Requires Check', 'Check Trait', check_trait, errors)


	return (errors)

def resisted_by_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	dc = data['dc']
	mod = data['mod']
	description = data['description']
	trait = data['trait']
	effect = data['effect']
	level = data['level']
	degree = data['degree']
	descriptor = data['descriptor']
	weaken_max = data['weaken_max']
	weaken_restored = data['weaken_restored']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage = data['damage']
	strength = data['strength']
	nullify_descriptor = data['nullify_descriptor']
	nullify_alternate = data['nullify_alternate']
	extra_effort = data['extra_effort']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Levels, level, 'level', errors)
	errors = id_check(Defense, nullify_alternate, 'defense', errors)

	errors = int_check(dc, 'DC', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(degree, 'Degree', errors)
	errors = int_check(weaken_max, 'Weaken Maximum', errors)
	errors = int_check(weaken_restored, 'Weaken Restored', errors)
	errors = int_check(damage, 'Damage', errors)

	errors = required(dc, 'DC', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(description, 'Circumstance', errors)
	errors = required(trait_type, 'Resisted by Trait Type', errors)
	errors = required(trait, 'Resisted by Trait', errors)
	errors = required(degree, 'Degree', errors)

	errors = variable_fields('condition', 'Condition', effect, [condition1, condition2], errors)
	errors = variable_field('condition', effect, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', effect, 'Ending Condition', condition2, errors) 
	errors = variable_fields('damage', 'Damage', effect, [damage], errors) 
	errors = variable_field('damage', effect, 'Damage Type', damage, errors)
	errors = select_of('nullify', 'Nullifies an Opponent Effect', 'Effect Type', effect, [nullify_descriptor, nullify_alternate], ['Nullified by Descriptor', 'Alternate Resistance'], errors)
	errors = variable_fields('trait', 'Weakened Trait', effect, [weaken_max, weaken_restored], errors)
	errors = variable_field('trait', effect, 'Maximum Lost Points', weaken_max, errors)
	errors = variable_field('trait', effect, 'Restored Points Rate', weaken_restored, errors)
	errors = variable_fields('level', 'Level', effect, [level], errors)

	return (errors)


def reverse_effect_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	degree = data['degree']
	when = data['when']
	check_check = data['check_check']
	time_check = data['time_check']
	trait_type = data['trait_type']
	trait = data['trait']
	value_type = data['value_type']
	value_dc = data['value_dc']
	math_dc = data['math_dc']
	math = data['math']
	time_value = data['time_value']
	time_unit = data['time_unit']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	
	errors = int_check(degree, 'Degree', errors)
	errors = int_check(value_dc, 'DC', errors)
	errors = int_check(math_dc, 'DC', errors)
	errors = int_check(time_value, 'Time', errors)

	errors = required(degree, 'Degree', errors)
	errors = required(when, 'When', errors)
	errors = required(target, 'Target', errors)

	errors = of([check_check, time_check], 'You must choose if this effect is reversed by a check or time or both', errors)
	errors = check_fields(check_check, 'Reversed by Check', [trait_type, trait, value_type], errors)
	errors = check_field(check_check, 'Reversed by Check', 'Trait Type', trait_type, errors)
	errors = check_field(check_check, 'Reversed by Check', 'Trait', trait, errors)
	errors = check_field(check_check, 'Reversed by Check', 'DC Type', value_type, errors)
	errors = variable_fields('value', 'DC Value', value_type, [value_dc], errors)
	errors = variable_fields('math', 'DC Math', value_type, [math_dc, math], errors)
	errors = variable_fields('math', value_type, 'DC', math_dc, errors)
	errors = variable_fields('math', value_type, ' Math', math, errors)
	errors = check_fields(time_check, 'Reversed by Time', [time_value, time_unit], errors)
	errors = check_field(time_check, 'Reversed by Time', 'Time', time_value, errors)
	errors = check_field(time_check, 'Reversed by Time', 'Time Units', time_unit, errors)

	return (errors)


def sense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	sense = data['sense']
	subsense = data['subsense']
	visual = data['visual']
	mental = data['mental']
	tactile = data['tactile']
	skill = data['skill']
	sense_type = data['sense_type']
	height_trait_type = data['height_trait_type']
	height_trait = data['height_trait']
	height_power_required = data['height_power_required']
	height_ensense = data['height_ensense']
	resist_trait_type = data['resist_trait_type']
	resist_trait = data['resist_trait']
	resist_immune = data['resist_immune']
	resist_permanent = data['resist_permanent']
	resist_circ = data['resist_circ']
	objects = data['objects']
	exclusive = data['exclusive']
	gm = data['gm']
	dark = data['dark']
	lighting = data['lighting']
	time = data['time']
	dimensional = data['dimensional']
	radius = data['radius']
	accurate = data['accurate']
	acute = data['acute']
	time_set = data['time_set']
	time_value = data['time_value']
	time_type = data['time_type']
	distance = data['distance']
	distance_dc = data['distance_dc']
	distance_mod = data['distance_mod']
	distance_value = data['distance_value']
	distance_unit = data['distance_unit']
	distance_factor = data['distance_factor']
	dimensional_type = data['dimensional_type']
	dimensional_descriptor = data['dimensional_descriptor']
	ranks = data['ranks']
	cost = data['cost']
	power_cost = data['power_cost']
	circ = data['circ']
	comprehend = data['comprehend']
	comprehend_type = data['comprehend_type']
	comprehend_language = data['comprehend_language']
	comprehend_animal = data['comprehend_animal']
	comprehend_spirit = data['comprehend_spirit']
	concealment = data['concealment']
	conceal_power_sense = data['conceal_power_sense']
	conceal_power = data['conceal_power']
	awareness = data['awareness']
	awareness_descriptor = data['awareness_descriptor']
	awareness_subtle = data['awareness_subtle']
	awareness_subtle_ranks = data['awareness_subtle_ranks']
	counter_conceal_descriptor  = data['counter_conceal_descriptor']
	counter_conceal = data['counter_conceal']
	ranged = data['ranged']
	range = data['range']
	ranged_type = data['ranged_type']
	light_penalty = data['light_penalty']
	light_penalty_trait_type = data['light_penalty_trait_type']
	light_penalty_trait = data['light_penalty_trait']
	illusion_range = data['illusion_range']
	illusion_unit = data['illusion_unit']
	illusion_opposed = data['illusion_opposed']
	condition = data['condition']
	condition_degree = data['condition_degree']
	remote_ranged = data['remote_ranged']
	micro = data['micro']
	micro_expertise = data['micro_expertise']
	track_speed = data['track_speed']
	track_speed_type = data['track_speed_type']
	counter_conceal_uv = data['counter_conceal_uv']
	communication = data['communication']
	communication_other = data['communication_other']
	communication_range = data['communication_range']

	errors = id_check(PowerCost, cost, 'Cost', errors)
	errors = id_check(PowerRanks, ranks, 'Ranks', errors)
	errors = id_check(PowerCheck, skill, 'Variable Check', errors)
	errors = id_check(PowerTimeType, time_type, 'Time by Group', errors)
	errors = id_check(PowerTime, time_value, 'Time', errors)
	errors = id_check(PowerCirc, circ,  'Circumstance', errors)
	errors = id_check(PowerRanged, range, 'Range', errors)
	errors = id_check(PowerRangedType, ranged_type, 'Range by Group', errors)
	errors = id_check(PowerDegree, condition_degree, 'Degree of Succeaa/Failure', errors)
	errors = id_check(PowerMove, track_speed, 'Tracking Speed', errors)
	errors = id_check(PowerMoveType, track_speed_type, 'Tracking Speed by Group', errors)
	errors = id_check(PowerRangedType, communication_range, 'Communication Range by Gtoup', errors)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Skill, skill, 'skill', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	errors = id_check(Skill, time_skill, 'skill', errors)
	errors = id_check(Unit, distance_unit, 'unit', errors)
	errors = id_check(Conceal, concealment, 'Concealment', errors)
	errors = id_check(PowerDes, dimensional_descriptor, 'Dimensional Descriptor', errors)
	errors = id_check(PowerDes, awareness_descriptor, 'Awareness Descriptor', errors)
	errors = id_check(PowerDes, counter_conceal_descriptor, 'Counters Concealment Descriptor', errors)
	errors = id_check(Light, light_penalty, 'Light Type', errors)
	errors = id_check(Unit, illusion_unit, 'Unit', errors)
	errors = id_check(Condition, condition, 'Condition', errors)
	errors = id_check(Communication, communication, 'Communication Medium', errors)

	errors = int_check(sense_cost, 'Sense Cost', errors)
	errors = int_check(subsense_cost, 'Subsense Cost', errors)
	errors = int_check(resist_circ, 'Resistance Circumstance Modifier', errors)
	errors = int_check(time_value, 'Time', errors)
	errors = int_check(time_factor, 'Time Factor', errors)
	errors = int_check(distance_dc, 'Distance DC', errors)
	errors = int_check(distance_mod, 'Distance Modifier', errors)
	errors = int_check(distance_value, 'Distance', errors)
	errors = int_check(distance_factor, 'Distance Factor', errors)
	errors = int_check(illusion_range, 'Illusion Diameter', errors)
	errors = int_check(awareness_subtle_ranks, 'Subtle Ranks', errors)

	errors = required(sense_type, 'Sense Effect Type', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('height', 'Heightened Sense', sense_type, [height_trait_type, height_trait], errors)
	errors = variable_field('height', sense_type, 'Heightened Sense Trait Type', height_trait_type, errors)
	errors = variable_field('height', sense_type, 'Heightened Sense Trait', height_trait, errors)
	errors = check_field(height_power_required, 'Needs Sense Power', 'Enhanced Sense', height_ensense, errors)
	errors = variable_fields('resist', 'Resistant Sense', sense_type, [resist_trait_type, resist_trait], errors)
	errors = variable_field('resist', sense_type, 'Resistant Trait Type', resist_trait_type, errors)
	errors = variable_field('resist', sense_type, 'Resistant Trait', resist_trait, errors)
	errors = check_field(resist_immune, 'Immunity', 'Immunity Type', resist_permanent, errors)

	errors = variable_fields('conceal', 'Concealment', sense_type, [concealment], errors)
	errors = variable_field('conceal', sense_type, 'Concealment', concealment, errors)
	errors = check_fields(conceal_power, 'Concealed from Power', [conceal_power_sense], errors)
	errors = check_field(conceal_power, 'Concealed from Power', 'Sense Power', conceal_power_sense, errors)

	errors = variable_fields('6', 'Microscopic Vision', subsense, [micro, micro_expertise], errors)
	errors = variable_field('6', subsense, 'Object Size', micro, errors)
	errors = variable_field('6', subsense, 'Expertise to Understand', micro_expertise, errors)

	errors = variable_fields('light', 'No Light Penalties', sense_type, [light_penalty, light_penalty_trait_type, light_penalty_trait], errors)
	errors = variable_field('light', sense_type, 'Light Type', light_penalty, errors)
	errors = variable_field('light', sense_type, 'Trait Type', light_penalty_trait_type, errors)
	errors = variable_field('light', sense_type, 'Trait', light_penalty_trait, errors)

	errors = variable_fields('illusion', 'Illusion', sense_type, [illusion_range, illusion_unit, illusion_opposed], errors)
	errors = variable_field('illusion', sense_type, 'Illusion Units', illusion_unit, errors)
	errors = variable_field('illusion', sense_type, 'Illusion Diameter', illusion_range, errors)
	errors = variable_field('illusion', sense_type, 'Interaction Check Group', illusion_opposed, errors)

	errors = variable_fields('condition', 'Sense Condition', sense_type, [condition_degree, condition], errors)
	errors = variable_field('condition', sense_type, 'Degree of Succesa/Failure', condition_degree, errors)
	errors = variable_field('condition', sense_type, 'Condition', condition, errors)

	errors = variable_fields('remote', 'Remote Sensing', sense_type, [remote_ranged], errors)
	errors = variable_field('remote', sense_type, 'Remote Sensing', remote_ranged, errors)

	errors = variable_fields('communicate', 'Communication', sense_type, [sense, communication, communication_range], errors)
	errors = variable_field('communicate', sense_type, 'Sense', sense, errors)
	errors = variable_field('communicate', sense_type, 'Communication Medium', communication, errors)
	errors = variable_field('communicate', sense_type, 'Communication Range by Group', communication_range, errors)
	errors = variable_field('other', communication, 'Other Communication Medium', communication_other, errors)

	errors = check_field(dark, 'Counters Darkness', 'Lighting', lighting, errors)
	errors = check_of(time, 'Time Effect', 'a Time Effect or Time Effect by Group', [time_value, time_type], errors)
	errors = seperate([time_value, time_type], 'the Time Effect', errors)
	errors = check_field(dimensional, 'Dimensional', 'Dimensional Type', dimensional_type, errors)
	errors = check_field(comprehend, 'Comprehend', 'Comprehend Type', comprehend_type, errors)

	errors = checked_invalid_option(mental, '11', sense, 'Excludes Mental Senses', 'Sense', 'Mental', errors)
	errors = checked_invalid_option(visual, '6', sense, 'Excludes Visual Senses', 'Sense', 'Visual', errors)
	errors = checked_invalid_option(tactile, '9', sense, 'Excludes Tactile Senses', 'Sense', 'Tactile', errors)

	errors = check_fields(awareness, 'Awareness', [awareness_descriptor], errors)
	errors = check_field(awareness, 'Awareness', 'Descriptor', awareness_descriptor, errors)
	errors = check_fields(awareness_subtle, 'Detects Subtle', [awareness_subtle_ranks], errors)
	errors = check_field(awareness_subtle, 'Detects Subtle', 'Subtle Ranks', awareness_subtle_ranks, errors)

	errors = variable_fields('descriptor', 'Descriptor Dimension', dimensional_type, [dimensional_descriptor], errors)
	errors = variable_field('descriptor', dimensional_type, 'Descriptor', dimensional_descriptor, errors)

	errors = variable_fields('descriptor', 'Counters Descriptor Concealment', counter_conceal, [counter_conceal_descriptor], errors)
	errors = variable_field('descriptor', counter_conceal, 'Descriptor', counter_conceal_descriptor, errors)

	errors = check_fields(comprehend, 'Comprehend', [comprehend_type], errors)
	errors = check_field(comprehend, 'Comprehend', 'Comprehend Type', comprehend_type, errors)

	errors = variable_fields('animal', 'Comprehend', comprehend_type, [comprehend_animal], errors)
	errors = variable_field('animal', comprehend_type, 'Comprehend Animals', comprehend_animal, errors)
	errors = variable_fields('language', 'Comprehend', comprehend_type, [comprehend_language], errors)
	errors = variable_field('language', comprehend_type, 'Comprehend Languages', comprehend_language, errors)
	errors = variable_fields('spirit', 'Comprehend', comprehend_type, [comprehend_spirit], errors)
	errors = variable_field('spirit', comprehend_type, 'Comprehend Spirits', comprehend_spirit, errors)

	errors = variable_fields_of('track', 'Tracking', sense_type, [track_speed, track_speed_type], errors)
	errors = seperate([track_speed, track_speed_type], 'Tracking Speed or Speed by Group', errors)

	errors = check_of(ranged, 'Extended', 'Range or Range by Group', [range, ranged_type], errors)

	errors = valid_options(mental, 'Excludes a Mental Sense', ['all', 'x'], 'All Senses or Variable Sense', sense, 'Sense', errors)
	errors = valid_options(tactile, 'Excludes a Tactile Sense', ['all', 'x'], 'All Senses or Variable Sense', sense, 'Sense', errors)
	errors = valid_options(special, 'Excludes a Special Sense', ['all', 'x'], 'All Senses or Variable Sense', sense, 'Sense', errors)
	errors = valid_options(visual, 'Excludes a Visual Sense', ['all', 'x'], 'All Senses or Variable Sense', sense, 'Sense', errors)


	return (errors)


def power_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	check_type = data['check_type']
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
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	dc_value = data['dc_value']
	time = data['time']
	move = data['move']
	ranged = data['ranged']
	keyword = data['keyword']
	attack = data['attack']
	opposed = data['opposed']
	opposed_type = data['opposed_type']
	condition = data['condition']
	condition_target = data['condition_target']
	conditions_target = data['conditions_target']
	variable = data['variable']
	opponent = data['opponent']
	opponent_type = data['opponent_type']
	variable_type = data['variable_type']
	title = data['title']
	multiple = data['multiple']
	sense = data['sense']
	sense_type = data['sense_type']
	sense_target = data['sense_target']
	mental = data['mental']
	attack_range = data['attack_range']
	consequence = data['consequence']
	consequence_target = data['consequence_target']
	target_type = data['target_type']
	primary = data['primary']
	frequency = data['frequency']
	overwrite = data['overwrite']
	descriptor = data['descriptor']
	power_check = data['power_check']
	power_action = data['power_action']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_check(Check, check_type, 'Check', errors)
	errors = id_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = id_check(Ranged, conflict_range, 'Conflict Range', errors)
	errors = int_check(action, 'Action', errors)
	errors = id_check(Condition, condition1, 'Start Condition', errors)
	errors = id_check(Condition, condition2, 'End Condition', errors)
	errors = id_check(Condition, condition, 'Condition', errors)
	errors = id_check(Sense, sense, 'Sense', errors)
	errors = id_check(Consequence, consequence)

	errors = id_check(PowerDegreeType, degree, 'Degree', errors)
	errors = id_check(PowerCircType, circ, 'Circumstance', errors)
	errors = id_check(PowerDCType, dc, 'DC', errors)
	errors = id_check(PowerTimeType, time, 'Time Effect', errors)
	errors = id_check(PowerMoveType, move, 'Movement Effect', errors)
	errors = id_check(PowerOpposed, opposed, 'Opponent Check', errors)
	errors = id_check(PowerOpposedType, opposed_type, 'Opponent Check by Group', errors)
	errors = id_check(PowerRangedType, ranged, 'Ranged', errors)
	errors = id_check(PowerCheck, overwrite, 'Check to Overwrite', errors)
	errors = id_check(PowerCheck, variable, 'Linked Variable Check', errors)
	errors = id_check(PowerCheckType, variable_type, 'Linked Variable Check by Group', errors)
	errors = id_check(PowerOpposed, opponent, 'Linked Opponent Check', errors)
	errors = id_check(PowerOpposedType, opponent_type, 'Linked Opponent Check by Group', errors)
	errors = id_check(PowerDes, descriptor, 'Descriptor', errors)


	errors = int_check(attack, 'Attack Check Modifier', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(check_type, 'Check Type', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(when, 'When', errors)
	errors = required(action_type, 'Action Type', errors)
	errors = required(action, 'Action', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(trait_type, 'Rank', errors)
	errors = required(trait, 'Trait', errors)	
	errors = required(title, 'Title', errors)
	errors = required(target, 'Check Target', errors)
	errors = required(frequency, 'Frequency', errors)

	errors = variable_fields('change', 'Attached to Condition Change', trigger, [condition1, condition2, conditions_target], errors)
	errors = variable_field('change', trigger, 'Starting Condition', condition1, errors)
	errors = variable_field('change', trigger, 'Ending Condition', condition2, errors)
	errors = variable_field('change', trigger, 'Condition Target', conditions_target, errors)
	errors = variable_fields('condition', 'Attached to Condition', trigger, [condition, condition_target], errors)
	errors = variable_field('condition', trigger, 'Condition', condition, errors)
	errors = variable_field('condition', trigger, 'Condition Target', condition_target, errors)
	errors = variable_fields('conflict', 'Attached to Conflict Action', trigger, [conflict], errors)
	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)
	errors = variable_fields('sense', 'Attached to Sense Use', trigger, [sense, sense_type, sense_target], errors)
	errors = variable_field('sense', trigger, 'Sense', sense, errors)
	errors = variable_field('sense', trigger, 'Sense User', sense_target, errors)
	errors = variable_field('sense', trigger, 'Sense Use Type', sense_type, errors)
	errors = valid_options(mental, 'Excludes Mental Senses', ['any', 'x'], 'Variable Sense or Any Senae', sense, 'Sense', errors)
	
	errors = variable_fields('target', 'Trigger', trigger, [target_type], errors)
	errors = variable_field('target', trigger, 'Target Type', target_type, errors)
	errors = select_of('opposed', 'is attached to an Opponent Check', 'Trigger', trigger, [opponent, opponent_type], ['Opponent Check'], errors)
	errors = seperate([opponent_type, opponent], 'Opponent Check', errors)
	errors = select_of('variable', trigger, 'is attatched to a Variable Check', 'Trigger', trigger, [variable, variable_type], ['Variable Check'], errors)
	errors = seperate([variable_type, variable], 'Variable Check', errors)
	errors = variable_fields('descriptor', 'Attached to Opponent Use of Descriptor', trigger, [descriptor], errors)
	errors = variable_fields('descriptor', trigger, 'Descriptor', descriptor, errors)

	errors = variable_fields('consequence', 'Trigger', trigger, [consequence_target, consequence], errors)
	errors = variable_field('consequence', trigger, 'Consequence Target', consequence_target, errors)
	errors = variable_field('consequence', trigger, 'Consequence', consequence, errors)	

	errors = variable_fields('5', 'Attack Check', check_type, [attack_range], errors)
	errors = variable_field('5', check_type, 'Range', attack_range, errors)

	errors = variable_field_of('2', check_type, 'Opponent Check or Opponent Check by Group', [opposed, opposed_type], errors)
	errors = variable_field_of('7', check_type, 'Opponent Check or Opponent Check by Group', [opposed, opposed_type], errors)
	errors = seperate([opposed_type, opposed_type], 'Opponent Check or Opponent Check by Group', errors)

	errors = select_of('1', 'uses a skill check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = select_of('6', 'uses a resistance check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = seperate([dc, dc_value], 'DC or DC by Group', errors)

	errors = incompatible('2', check_type, 'an Opposed Check', 'object', frequency, 'Frequency', 'Inanimate Object', errors)
	errors = incompatible('7', check_type, 'a Comparison Check', 'object', frequency, 'Frequency', 'Inanimate Object', errors)

	errors = variable_field('overwrite', multiple, 'Check to Overwrite', overwrite, errors)

	return (errors)

def power_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	circ_target = data['circ_target']
	mod = data['mod']
	effect = data['effect']
	speed = data['speed']
	target = data['target']
	level_type = data['level_type']
	level = data['level']
	condition_type = data['condition_type']
	condition1 = data['condition1']
	condition2 = data['condition2']
	conditions = data['conditions']
	conditions_effect = data['conditions_effect']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	keyword = data['keyword']
	cumulative = data['cumulative']
	optional = data['optional']
	circumstance = data['circumstance']
	lasts = data['lasts']
	title = data['title']
	tools = data['tools']
	materials = data['materials']
	trait_type = data['trait_type']
	trait = data['trait']
	trait_target = data['trait_target']
	environment = data['environment']
	nature = data['nature']
	check_type = data['check_type']
	descriptor_effect = data['descriptor_effect']
	descriptor_target = data['descriptor_target']
	descriptor = data['descriptor']
	conflict = data['conflict']
	conflict_grab = data['conflict_grab']
	apply = data['apply']
	success = data['success_target']
	success_bonus = data['success_bonus']
	success_target = data['success_target']
	success_check = data['success_check']
	success_check_type = data['success_check_type']
	success_check_bonus = data['success_check_bonus']
	success_check_type_bonus = data['success_check_type_bonus']
	success_opposed = data['success_opposed']
	success_opposed_type = data['success_opposed_type']
	success_opposed_bonus = data['success_opposed_bonus']
	success_opposed_type_bonus = data['success_opposed_type_bonus']
	success_bonus_trait_type = data['success_bonus_trait_type']
	success_bonus_trait = data['success_bonus_trait']
 

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_check(PowerCheckType, success_check_type_bonus, 'Bonus On Check Group', errors)
	errors = id_check(PowerCheck, success_check_bonus, 'Bonus On Check', errors)
	errors = id_check(PowerCheckType, success_check_type, 'If Successful On Check Group', errors)
	errors = id_check(PowerCheck, success_check, 'If Successful On Check', errors)
	errors = id_check(PowerOpposedType, success_opposed_type_bonus, 'Bonus On Opponent Check Group', errors)
	errors = id_check(PowerOpposed, success_opposed_bonus, 'Bonus On Opponent Check', errors)
	errors = id_check(PowerOpposed, success_opposed, 'If Successful On Opponent Check', errors)
	errors = id_check(PowerOpposedType, success_opposed_type, 'If Successful On Opponent Check Group', errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(speed, 'Speed', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(conditions, 'Condition Degree', errors)
	errors = int_check(conditions_effect, 'Condition Effect', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Unit', errors)
	errors = id_check(Math, measure_trait_math, 'Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(trait, 'Trait', errors)
	errors = id_check(Check, check_type, 'Check Type', errors)
	errors = id_check(PowerDes, descriptor, 'Descriptor', errors)
	errors = id_check(ConflictAction, conflict_grab, 'Conflict Action', errors)

	errors = id_check(Environment, environment, 'Environment', errors)
	errors = id_check(Nature, nature, 'Nature', errors)

	errors = id_check(PowerTime, lasts, 'Circumsrance Duration', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)	
	errors = required(mod, 'Circumstance Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = required(circ_target, 'Target', errors)
	errors = required(apply, 'Applies', errors)

	errors = variable_fields('success', 'If Success', effect, [success, success_bonus, success_target], errors)
	errors = variable_field('success', effect, 'Success On', success, errors)
	errors = variable_field('success', effect, 'Applied To', success_bonus, errors)
	errors = variable_field('success', effect, 'Bonus Target', success_target, errors)

	errors = variable_fields('check_type', 'Applied To', success_bonus, [success_check_type_bonus], errors)
	errors = variable_field('check_type', success_bonus, 'Variable Check Group', success_check_type_bonus, errors)	
	errors = variable_fields('check', 'Applied To', success_bonus, [success_check_bonus], errors)	
	errors = variable_field('check', success_bonus, 'Vaariable Check', success_check_bonus, errors)
	errors = variable_fields('opposed_type', 'Applied To', success_bonus, [success_opposed_type_bonus], errors)
	errors = variable_field('opposed_type', success_bonus, 'Variable Check Group', success_opposed_type_bonus, errors)	
	errors = variable_fields('opposed', 'Applied To', success_bonus, [success_opposed_bonus], errors)	
	errors = variable_field('opposed', success_bonus, 'Opponent Check', success_opposed_bonus, errors)
	errors = variable_fields('trait', 'Applied To', success_bonus, [success_bonus_trait_type, success_bonus_trait], errors)
	errors = variable_field('trait', success_bonus, 'Trait Type', success_bonus_trait_type, errors)
	errors = variable_field('trait', success_bonus, 'Trait', success_bonus_trait, errors)
	

	errors = variable_fields('opposed_type', 'Success On', success, [success_opposed_type], errors)
	errors = variable_field('opposed_type', success, 'Success On Opponent Check Group', success_opposed_type, errors)
	errors = variable_fields('opposed', 'Success On', success, [success_opposed], errors)
	errors = variable_field('opposed', success, 'Success On Opponent Check', success_opposed, errors)
	errors = variable_fields('check_type', 'Success On', success, [success_check_type], errors)
	errors = variable_field('check_type', success, 'Success On Variable Check Group', success_check_type, errors)
	errors = variable_fields('check', 'Success On', success, [success_check], errors)
	errors = variable_field('check', success, 'Success On Variable Check', success_check, errors)


	errors = variable_fields('condition', 'Circumstance Effect', effect, [condition_type], errors)
	errors = variable_field('condition', effect, 'Condition Type', condition_type, errors)
	errors = variable_fields('condition', 'Condition Type', condition_type, [], errors)

	errors = variable_fields('damage', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('damage', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('damage', condition_type, 'Ending Condition', condition2, errors)

	errors = variable_fields('damage', 'Condition Damage', condition_type, [conditions, conditions_effect], errors)
	errors = variable_field('damage', condition_type, 'Conditions', conditions, errors)
	errors = variable_field('damage', condition_type, 'Condition Effect', conditions_effect, errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors)

	errors = variable_fields('rank', 'Measurement Rank', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Measurement Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Units', unit, errors)

	errors = variable_fields('skill', 'Measurement Skill Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill', measure_effect, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('skill', measure_effect, 'Measurement Trait', measure_trait, errors)
	errors = variable_field('skill', measure_effect, 'Math', measure_trait_math, errors)
	errors = variable_field('skill', measure_effect, 'Measuremet Modifier', measure_mod, errors)
	errors = variable_field('skill', measure_effect, 'Rank', measure_math_rank, errors)
	
	errors = variable_fields('level', 'Circumstance Effect', effect, [level_type, level], errors)
	errors = variable_field('level', effect, 'Level Type', level_type, errors)
	errors = variable_field('level', effect, 'Level', level, errors)
	
	errors = variable_fields('speed', 'Circumstance Effect', effect, [speed], errors)
	errors = variable_field('speed', effect, 'Speed Rank', speed, errors)
	
	errors = variable_fields('target', 'Circumstance Effect', effect, [target], errors)
	errors = variable_field('target', effect, 'If Target', target, errors)
	
	errors = variable_fields('tools', 'Circumstance Effect', effect, [tools], errors)
	errors = variable_field('tools', effect, 'Tool Type', tools, errors)
	
	errors = select_of('trait', 'affects another check', 'circumstance effect', effect, [trait, check_type], ['Trait', 'Check Type'], errors)
	errors = variable_field('trait', effect, 'Check Target', trait_target, errors)

	errors = variable_fields('env', 'Environment', effect, [environment], errors)

	errors = variable_fields('nature', 'Nature', effect, [nature], errors)

	errors = variable_fields('descriptor', 'Descriptor', effect, [descriptor_effect, descriptor_target, descriptor], errors)
	errors = variable_field('descriptor', effect, 'Descriptor', descriptor, errors)
	errors = variable_field('descriptor', effect, 'Descriptor Target', descriptor_target, errors)
	errors = variable_field('descriptor', effect, 'Descriptor Effect', descriptor_effect, errors)

	errors = variable_fields('conflict', 'Conflict Action', effect, [conflict], errors)
	errors = variable_field('conflict', effect, 'Conflict Action', conflict, errors)
	errors = variable_fields('7', 'Grab', conflict, [conflict_grab], errors)
	errors = variable_fields('7', conflict, 'Grab Type', conflict_grab, errors)


	errors = variable_fields('materials', 'Circumstance Effect', effect, [materials], errors)
	errors = variable_field('materials', effect, 'Material Type', materials, errors)


	return (errors)

def power_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	levels = data['levels']
	damage = data['damage']
	cover = data['cover']
	complex = data['complex']
	measure = data['measure']
	conceal = data['conceal']
	damage_type = data['damage_type']
	inflict_type = data['inflict_type']
	inflict_flat = data['inflict_flat']
	inflict_trait_type= data['inflict_trait_type']
	inflict_trait = data['inflict_trait']
	inflict_math = data['inflict_math']
	inflict_mod = data['inflict_mod']
	inflict_bonus = data['inflict_bonus']
	damage_mod = data['damage_mod']
	damage_consequence = data['damage_consequence']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	measure_trait_type_unit = data['measure_trait_type_unit']
	measure_trait_unit = data['measure_trait_unit']
	measure_trait_math_unit = data['measure_trait_math_unit']
	measure_mod_unit = data['measure_mod_unit']
	measure_math_unit = data['measure_math_unit']
	level_type = data['level_type']
	level = data['level']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	condition_dead = data['condition_dead']
	keyword = data['keyword']
	complexity = data['complexity']
	tools_check = data['tools_check']
	cover_effect = data['cover_effect']
	cover_type = data['cover_type']
	conceal_effect = data['conceal_effect']
	conceal_type = data['conceal_type']
	tools = data['tools']
	variable_check = data['variable_check']
	variable = data['variable']
	time = data['time']
	title = data['title']
	equipment_use = data['equipment_use']
	equipment_type = data['equipment_type']
	equipment = data['equipment']
	equip = data['equip']
	descriptor_effect = data['descriptor_effect']
	descriptor_target = data['descriptor_target']
	descriptor = data['descriptor']
	descrip = data['descrip']
	ranks = data['ranks']
	rank = data['rank']
	ranks_per = data['ranks_per']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(value, 'DC', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(math_value, 'Math Value', errors)
	errors = id_check(Math, math, 'Math', errors)
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
	errors = id_check(Rank, measure_math_rank, 'Measurement Rank', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = id_check(Complex, complexity, 'Complexity', errors)
	errors = id_check(EquipType, equipment_type, 'Equipment Type', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)
	errors = id_check(PowerDes, descriptor, 'Descriptor', errors)
	errors = int_check(rank, 'Ranks', errors)
	errors - int_check(ranks_per, 'Result Over DC', errors)


	errors = id_check(Cover, cover_type, 'Cover', errors)
	errors = id_check(Conceal, conceal_type, 'Concealment', errors)
	
	errors = id_check(PowerCheck, variable, 'Variable Check', errors)
	errors = id_check(PowerTime, time, 'Duration of Effect', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(target, 'Target', errors)
	errors = required(dc, 'DC Type', errors)
	errors = required(description, 'Description', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('value', 'DC Value', dc, [value], errors) 
	errors = variable_field('value', dc, 'DC', value, errors) 

	errors = variable_fields('math', 'DC Math', dc, [math_value, math, math_trait_type, math_trait], errors)
	errors = variable_field('math', dc, 'DC Math Value', math_value, errors)
	errors = variable_field('math', dc, 'DC Math', math, errors)
	errors = variable_field('math', dc, 'DC Math Trait Type', math_trait_type, errors)
	errors = variable_field('math', dc, 'DC Math Trait', math_trait, errors)
	
	errors = variable_fields('mod', 'DC Modifier', dc, [mod], errors)
	errors = variable_field('mod', dc, 'Modifier', mod, errors)

	errors = check_fields(condition, 'Condition', [condition1, condition2], errors)
	errors = check_field(condition, 'Condition', 'Starting Condition', condition1, errors)
	errors = check_field(condition, 'Condition', 'Ending Condtion', condition2, errors)

	errors = variable_fields('dead', 'Dead Condition', condition1, [condition_dead], errors)
	errors = variable_field('dead', condition1, 'Minutes', condition_dead, errors)

	errors = check_fields(descrip, 'Descriptor', [descriptor_effect, descriptor_target, descriptor], errors)
	errors = check_field(descrip, 'Descriptor', 'Descriptor', descriptor, errors)
	errors = check_field(descrip, 'Descriptor', 'Descriptor Target', descriptor_target, errors)
	errors = check_field(descrip, 'Descriptor', 'Descriptor Effect', descriptor_effect, errors)
	
	errors = check_fields(levels, 'Levels', [level_type, level], errors)
	errors = check_field(levels, 'Levels', ':evel Type', level_type, errors)
	errors = check_field(levels, 'Levels', 'Level', level, errors)

	errors = check_fields(damage, 'Damage', [damage_type], errors)
	errors = check_field(damage, 'Damage', 'Damage Type', damage_type, errors)

	errors = variable_fields('inflict', 'Inflict Damage', damage_type, [inflict_type], errors)
	errors = variable_field('inflict', damage_type, 'Inflict Damage Type', inflict_type, errors)

	errors = variable_fields('flat', 'Flat Damage Value', inflict_type, [inflict_flat], errors)
	errors = variable_field('flat', inflict_type, 'Damage', inflict_flat, errors)

	errors = variable_fields('bonus', 'Flat Damage Bonus', inflict_type, [inflict_bonus], errors)
	errors = variable_fields('bonus', inflict_type, 'Bonus', inflict_bonus, errors)
	
	errors = variable_fields('math', 'Math Damage', inflict_type, [inflict_trait_type, inflict_trait, inflict_math, inflict_mod], errors)
	errors = variable_field('math', inflict_type, 'Math Damage Trait Type', inflict_trait_type, errors)
	errors = variable_field('math', inflict_type, 'Math Damage Trait', inflict_trait, errors)
	errors = variable_field('math', inflict_type, 'Math', inflict_math, errors)
	errors = variable_field('math', inflict_type, 'Math Damage Modifier', inflict_mod, errors)

	errors = variable_fields('reduce', 'Reduce Damage', damage_type, [damage_mod], errors)
	errors = variable_field('reduce', damage_type, 'Damage Modifier', damage_mod, errors)
	
	errors = check_fields(complex, 'Complexity', [complexity], errors)
	errors = check_field(complex, 'Complexity', 'Complexity', complexity, errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors)

	errors = variable_fields('rank', 'Measurement Rank Value', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Rank Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit Value', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Measurement UnitS', unit, errors)

	errors = variable_fields('skill_rank', 'Measurement Skill Rank Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Trait', measure_trait, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Skill Modifier Math', measure_trait_math, errors)
	errors = variable_field('skill_rank', measure_effect, 'Skill Modifier', measure_mod, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Rank', measure_math_rank, errors)
	
	errors = variable_fields('skill_unit', 'Measurement Skill Unit Modifier', measure_effect, [measure_trait_type_unit, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait Type', measure_trait_type_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait', measure_trait_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Math', measure_trait_math_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Skill Modifier', measure_mod_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Measurement Rank', measure_math_unit, errors)

	errors = check_fields(conceal, 'Concealment', [conceal_effect, conceal_type], errors)
	errors = check_field(conceal, 'Concealment', 'Concealment Type', conceal_type, errors)
	errors = check_field(conceal, 'Concealment', 'Concealment Effect', conceal_effect, errors)
	
	errors = check_fields(cover, 'Cover', [cover_effect, cover_type], errors)
	errors = check_field(cover, 'Cover', 'Cover Type', cover_type, errors)
	errors = check_field(cover, 'Cover', 'Cover Effect', cover_effect, errors)

	errors = check_fields(equip, 'Equipment', [equipment_use, equipment_type, equipment], errors)
	errors = check_field(equip, 'Equipment', 'Equipment Use Type', equipment_use, errors)
	errors = check_field(equip, 'Equipment', 'Equipment Type', equipment_type, errors)
	errors = check_field(equip, 'Equipment', 'Equipment', equipment, errors)

	errors = check_fields(rank, 'Ranks', [rank, ranks_per], errors)
	errors = check_field(rank, 'Ranks', 'Ranks', rank, errors)
	errors = check_field(rank, 'Ranks', 'Result Over DC', ranks_per, errors)

	errors = check_fields(variable_check, 'Variable Check', [variable], errors)

	return (errors)

def power_degree_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	knowledge_mind = data['knowledge_mind']
	knowledge_mind_count = data['knowledge_mind_count']
	level_type = data['level_type']
	level = data['level']
	level_direction = data['level_direction']
	level_time = data['level_time']
	circumstance = data['circumstance']
	circ_target = data['circ_target']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	measure_trait_type_unit = data['measure_trait_type_unit']
	measure_trait_unit = data['measure_trait_unit']
	measure_trait_math_unit = data['measure_trait_math_unit']
	measure_mod_unit = data['measure_mod_unit']
	measure_math_unit = data['measure_math_unit']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	condition_inflict = data['condition_inflict']
	condition_inflict_descriptor = data['condition_inflict_descriptor']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']
	check_type = data['check_type']
	opposed = data['opposed']
	variable = data['variable']
	resist_dc = data['resist_dc']
	resist_trait_type = data['resist_trait_type']
	resist_trait = data['resist_trait']
	skill_dc = data['skill_dc']
	skill_trait_type = data['skill_trait_type']
	skill_trait = data['skill_trait']
	routine_trait_type = data['routine_trait_type']
	routine_trait = data['routine_trait']
	routine_mod = data['routine_mod']
	attack = data['attack']
	attack_turns = data['attack_turns']
	compare = data['compare']
	duration = data['duration']
	title = data['title']
	descriptor_effect = data['descriptor_effect']
	descriptor_target = data['descriptor_target']
	descriptor = data['descriptor']
	multiple = data['multiple']
	effect = data['effect']
	effect_descriptor = data['effect_descriptor']
	effect_descriptor_type = data['effect_descriptor_type']
	effect_descriptor_count = data['effect_descriptor_count']
	effect_power = data['effect_power']
	null_condition = data['null_condition']
	weaken_type = data['weaken_type']
	weaken_max = data['weaken_max']
	weaken_val = data['weaken_val']
	reverse_type = data['reverse_type']
	reverse = data['reverse']
	restore = data['restore']
	restore_descriptor = data['restore_descriptor']
	restore_val = data['restore_val']
	no_reattempt_time = data['no_reattempt_time']


	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = degree_check(title, value, multiple, power_id, extra_id, errors)


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
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Unit Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Units', errors)
	errors = id_check(Math, measure_trait_math, 'Measurement Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(condition_damage_value, 'Condition Degrees', errors)
	errors = int_check(condition_damage, 'Condition Damage', errors)
	errors = int_check(nullify, 'Nullify DC', errors)
	errors = id_check(Check, check_type, 'Check Tyoe', errors)
	errors = id_check(PowerDes, descriptor, 'Descriptor', errors)
	errors = int_check(knowledge_mind_count, 'Mind Reading Count', errors)
	errors = int_check(effect_descriptor_count, 'Effect Count', errors)
	errors = int_check(weaken_max, 'Maximum Points Lost', errors)
	errors = int_check(weaken_val, 'Points Lost', errors)
	errors = id_check(Condition, condition_inflict, 'Inflict Condition', errors)
	errors = id_check(PowerDes, condition_inflict_descriptor, 'Inflict Condition Descriptor', errors)

	errors = id_check(PowerOpposed, opposed, 'Opposed Check', errors)
	errors = id_check(PowerDC, resist_dc, 'Resistance Check DC', errors)
	errors = id_check(PowerDC, skill_dc, 'Skilll Check DC', errors)
	errors = id_check(PowerOpposed, compare, 'Comparison Check', errors)
	errors = id_check(PowerCheck, variable, 'Variable Check', errors)
	errors = id_check(PowerTime, level_time, 'Level Duration', errors)
	errors = id_check(PowerTime, attack_turns, 'Attack Bonus Duration', errors)
	errors = id_check(PowerTime, condition_turns, 'Condition Duration', errors)
	errors = id_check(PowerDegree, linked, 'Linked Degree', errors)
	errors = id_check(PowerCirc, circumstance, 'Circumstance Modifier Keyword', errors)
	errors = id_check(PowerDegree, reverse, 'Reversed Degree', errors)
	errors = id_check(PowerTime, no_reattempt_time, 'Reattempt Time', errors)

	errors = id_check(PowerDes, effect_descriptor, 'Effect Descriptor', errors)
	errors = id_check(Power, effect_power, 'Power Effect', errors)
	errors = id_check(Condition, null_condition, 'Nullified Condition', errors)
	errors = id_check(PowerDes, restore_descriptor, 'Restore Descriptor', errors)

	errors = int_check(resist_trait, 'Resistance Trait', errors)
	errors = int_check(skill_trait, 'Skill Check Trait', errors)
	errors = int_check(routine_trait, 'Routine Check Trait', errors)
	errors = int_check(routine_mod, 'Routine Check Modifier', errors)
	errors = int_check(attack, 'Attack Check Modifier', errors)
	
	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(target, 'Target', errors)
	errors = required(value, 'Degree', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors)

	errors = variable_fields('no_reattempt', "Can't Reattempt", type, [no_reattempt_time], errors)
	errors = variable_field('no_reattempt', type, "Reattempt Time", no_reattempt_time, errors) 

	errors = variable_fields('descriptor', 'Descriptor', type, [descriptor_effect, descriptor_target, descriptor], errors)
	errors = variable_field('descriptor', type, 'Descriptor', descriptor, errors)
	errors = variable_field('descriptor', type, 'Descriptor Target', descriptor_target, errors)
	errors = variable_field('descriptor', type, 'Descriptor Effect', descriptor_effect, errors)

	errors = variable_fields('rank', 'Measurement Rank Value', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit Value', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Units', unit, errors)

	errors = variable_fields('skill_rank', 'Measurement Skill Rank Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill_rank', measure_effect, 'Trait Type', measure_trait_type, errors)
	errors = variable_field('skill_rank', measure_effect, 'Trait', measure_trait, errors)
	errors = variable_field('skill_rank', measure_effect, 'Math', measure_trait_math, errors)
	errors = variable_field('skill_rank', measure_effect, 'Skill Modifier', measure_mod, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Rank', measure_math_rank, errors)

	errors = variable_fields('skill_unit', 'Measurement Skill Unit Modifier', measure_effect, [measure_trait_type_unit, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait Type', measure_trait_type_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait', measure_trait_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Math', measure_trait_math_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Skill Modifier', measure_mod_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Measurement Rank', measure_math_unit, errors)

	errors = variable_fields('condition', 'Condition Effect', type, [condition_type], errors)
	errors = variable_field('condition', type, 'Condition Type', condition_type, errors)

	errors = variable_fields('condition', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', condition_type, 'Ending Condition Change', condition2, errors)

	errors = variable_fields('damage', 'Damage Condition', condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', condition_type, 'Damage Value', condition_damage_value, errors)
	errors = variable_field('damage', condition_type, 'Damage Direction', condition_damage, errors)

	errors = variable_fields('inflict', 'Inflict Condition', condition_type, [condition_inflict, condition_inflict_descriptor], errors)
	errors = variable_fields('inflict', condition_type, 'Condition', condition_inflict, errors)
	errors = variable_fields('inflict', condition_type, 'Descriptor', condition_inflict_descriptor, errors)

	errors = variable_fields('action', 'Action Change Effect', type, [action], errors)
	errors = variable_field('action', type, 'Changed Action', action, errors)
	
	errors = variable_fields('circ', 'Circumstance Effect', type, [circumstance, circ_target], errors)
	errors = variable_field('circ', type, 'Circumstance', circumstance, errors)
	errors = variable_field('circ', type, 'Circumstance Target', circ_target, errors)
	
	errors = variable_fields('time', 'Time Modifier Effect', type, [time], errors)
	errors = variable_field('time', type, 'Time Modifier', time, errors)
	
	errors = variable_fields('damage', 'Damage Effect', type, [damage_type], errors)
	errors = variable_field('damage', type, 'Damage Type', damage_type, errors)

	errors = variable_fields('inflict', 'Inflict Damage', damage_type, [inflict_type], errors)
	errors = variable_field('inflict', damage_type, 'Inflict Damage Type', inflict_type, errors)
	
	errors = variable_fields('flat', 'Flat Damage', inflict_type, [inflict_flat], errors)
	errors = variable_field('flat', inflict_type, 'Flat vALUE', inflict_flat, errors)

	errors = variable_fields('bonus', 'Flat Damage Bonus', inflict_type, [inflict_bonus], errors)
	errors = variable_field('bonus', inflict_type, 'Bonus', inflict_bonus, errors)

	errors = variable_fields('math', 'Math Damage', inflict_type, [inflict_trait_type, inflict_trait, inflict_math, inflict_mod], errors)
	errors = variable_field('math', inflict_type, 'Trait Type', inflict_trait_type, errors)
	errors = variable_field('math', inflict_type, 'Trait', inflict_trait, errors)
	errors = variable_field('math', inflict_type, 'Math', inflict_math, errors)
	errors = variable_field('math', inflict_type, 'Math Value', inflict_mod, errors)


	errors = variable_fields('reduce', 'Reduce Damage', damage_type, [damage_mod], errors)
	errors = variable_field('reduce', damage_type, 'Modifier', damage_mod, errors)

	errors = variable_fields('object', 'Damage Object', damage_type, [object, object_effect], errors)
	errors = variable_field('object', damage_type, 'Degrees', object, errors)
	errors = variable_field('object', damage_type, 'Object Condition', object_effect, errors)
	
	errors = variable_fields('level', 'Level Effect', type, [level_type], errors)
	errors = variable_field('level', type, 'Level Type', level_type, errors)
	errors = if_or('Level', level_type, [level, level_direction], 'Level or Level Change', errors)
	errors = seperate([level, level_direction], 'Level or Level Change', errors)
	
	errors = variable_fields('knowledge', 'Gain Knowledge Effect', type, [knowledge], errors)
	errors = variable_field('knowledge', type, 'Knowledge Type', knowledge, errors)

	errors = variable_fields('mind', 'Mind Reading', knowledge, [knowledge_mind], errors)
	errors = variable_field('mind', knowledge, 'Read Mind', knowledge_mind, errors)

	errors = variable_fields('personal', 'Personal Thoughts', knowledge_mind, [knowledge_mind_count], errors)
	errors = variable_field('personal', knowledge_mind, 'Personal Thoughts Count', knowledge_mind_count, errors)
	errors = variable_fields('memory', 'Memory', knowledge_mind, [knowledge_mind_count], errors)
	errors = variable_field('memory', knowledge_mind, 'Memory Count', knowledge_mind_count, errors)
	errors = variable_fields('sub', 'Subconscious Thoughts', knowledge_mind, [knowledge_mind_count], errors)
	errors = variable_field('sub', knowledge_mind, 'Subconscious Thoughts Count', knowledge_mind_count, errors)
	
	errors = variable_fields('bonus', 'Learn Bonus', knowledge, [knowledge_count, knowledge_specificity], errors)
	errors = variable_field('bonus', knowledge, 'Amount', knowledge_count, errors)
	errors = variable_field('bonus', knowledge, 'Specificity', knowledge_specificity, errors)
	
	errors = variable_fields('consequence', 'Consequence Effect', type, [consequence_action_type, consequence_action, consequence], errors)
	errors = variable_field('consequence', type, 'Consequence Action Type', consequence_action_type, errors)
	errors = variable_field('consequence', type, 'Consequence Action', consequence_action, errors)
	errors = variable_field('consequence', type, 'Consequence', consequence, errors)

	errors = variable_fields('check', 'Check', type, [check_type], errors)
	errors = variable_field('check', type, 'Check Type', check_type, errors)

	errors = variable_fields('1', 'Skill Check', check_type, [skill_trait_type, skill_trait, skill_dc], errors)
	errors = variable_field('1', check_type, 'Trait Type', skill_trait_type, errors)
	errors = variable_field('1', check_type, 'Trait', skill_trait, errors)
	errors = variable_field('1', check_type, 'DC', skill_dc, errors)

	errors = variable_fields('2', 'Opposed Check', check_type, [opposed], errors)
	errors = variable_field('2', check_type, 'Opposed', opposed, errors)
	
	errors = variable_fields('5', 'Arrack Check', check_type, [attack, attack_turns], errors)
	errors = variable_field('5', check_type, 'Arrack Modifier', attack, errors)
	errors = variable_field('5', check_type, 'Turns', attack_turns, errors)

	errors = variable_fields('6', 'Resistance Check', check_type, [resist_dc, resist_trait_type, resist_trait], errors)
	errors = variable_field('6', check_type, 'DC', resist_dc, errors)
	errors = variable_field('6', check_type, 'Trait Type', resist_trait_type, errors)
	errors = variable_field('6', check_type, 'Trait', resist_trait, errors)

	errors = variable_fields('3', 'Routine Check', check_type, [routine_trait_type, routine_trait, routine_mod], errors)
	errors = variable_field('3', check_type, 'Trait Type', routine_trait_type, errors)
	errors = variable_field('3', check_type, 'Trait', routine_trait, errors)
	errors = variable_field('3', check_type, 'Modifier', routine_mod, errors)

	errors = variable_fields('7', 'Comparison Check', check_type, [compare], errors)

	errors = variable_fields('duration', 'Effect Duration', type, [duration], errors)

	errors = variable_fields('null', 'Effect Nullified', type, [effect], errors)
	errors = variable_field('null', type, 'Effect Type', effect, errors)
	errors = variable_fields('uncontrol', 'Effect Uncontrolled', type, [effect], errors)
	errors = variable_field('uncontrol', type, 'Effect Type', effect, errors)
	errors = variable_fields('detect', 'Detect Effect', type, [effect], errors)
	errors = variable_field('detect', type, 'Effect Type', effect, errors)

	errors = variable_fields('descriptor', 'Descriptor', effect, [effect_descriptor], errors)
	errors = variable_field('descriptor', effect, 'Descriptor', effect_descriptor, errors)
	errors = variable_fields('count', 'Effect Count', effect_descriptor_type, [effect_descriptor_count], errora)
	errors = variable_field('count', effect_descriptor_type, 'Count', effect_descriptor_count, errora)

	errors = variable_fields('power', 'Power Effect', effect, [effect_power], errors)
	errors = variable_field('power', effect, 'Power', effect_power, errors)

	errors = variable_fields('null_condition', 'Nullify Condition', effect, [null_condition], errors)
	errors = variable_field('null_condition', effect, 'Nullified Condition', null_condition, errors)

	errors = variable_fields('weaken', 'Weaken', type, [weaken_type, weaken_max], errors)
	errors = variable_fields('weaken', type, 'Points Type', weaken_type, errors)
	errors = variable_fields('weaken', type, 'Maximum Points Lost', weaken_max, errors)
	
	errors = variable_field('val', weaken_type, 'Points Lost', weaken_val, errors)
	errors = variable_field('degree', weaken_type, 'Points Lost Per Degree', weaken_val, errors)
	
	errors = variable_fields('reverse', 'Reverse Degree Effect', type, [reverse_type, reverse], errors)
	errors = variable_field('reverse', type, 'Degree Type', reverse_type, errors)
	errors = variable_field('reverse', type, 'Degree', reverse, errors)

	errors = variable_fields('restore', 'Restore Points', type, [restore, restore_descriptor], errors)
	errors = variable_field('restore', type, 'Restore Points Type', restore, errors)
	errors = variable_field('restore', type, 'Restore Descriptor', restore_descriptor, errors)
	errors = variable_field('degree', restore, 'Points', restore_val, errors)
	errors = variable_field('points', restore, 'Points', restore_val, errors)

	errors = linked_field(condition1, linked, PowerDegree, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)
	errors = linked_field(condition2, linked, PowerDegree, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_field(consequence, linked, PowerDegree, 'Consequence', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_group_check(PowerDC, 'other', target, 'other', 'target', power_id, 'power_id', 'a degree of success or failure for another character', 'DC', 'the target field to Other Character', errors)

	return (errors)

def power_move_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	speed = data['speed']
	speed_rank = data['speed_rank']
	speed_max = data['speed_max']
	speed_mod = data['speed_mod']
	speed_math = data['speed_math']
	speed_rank_mod = data['speed_rank_mod']
	speed_penalty = data['speed_penalty']
	speed_trait_type = data['speed_trait_type']
	speed_trait = data['speed_trait']
	speed_math1 = data['speed_math1']
	speed_value1 = data['speed_value1']
	speed_math2 = data['speed_math2']
	speed_value2 = data['speed_value2']
	distance = data['distance']
	distance_rank = data['distance_rank']
	distance_value = data['distance_value']
	distance_units = data['distance_units']
	distance_rank_trait_type = data['distance_rank_trait_type']
	distance_rank_trait = data['distance_rank_trait']
	distance_rank_math1 = data['distance_rank_math1']
	distance_rank_value1 = data['distance_rank_value1']
	distance_rank_math2 = data['distance_rank_math2']
	distance_rank_value2 = data['distance_rank_value2']
	distance_unit_trait_type = data['distance_unit_trait_type']
	distance_unit_trait = data['distance_unit_trait']
	distance_unit_math1 = data['distance_unit_math1']
	distance_unit_value1 = data['distance_unit_value1']
	distance_unit_math2 = data['distance_unit_math2']
	distance_unit_value2 = data['distance_unit_value2']
	distance_math_units = data['distance_math_units']
	direction = data['direction']
	distance_description = data['distance_description']
	speed_description = data['speed_description']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	time = data['time']
	degree_type = data['degree_type']
	circ_type = data['circ_type']
	dc_type = data['dc_type']
	time_type = data['time_type']
	keyword = data['keyword']
	title = data['title']

	speed_per = data['speed_per']
	distance_per = data['distance_per']
	flight = data['flight']
	aquatic = data['aquatic']
	ground = data['ground']
	special = data['special']
	condition_check = data['condition_check']
	obstacles = data['obstacles']
	objects = data['objects']
	permeate = data['permeate']
	prone = data['prone']
	equip = data['equip']
	concealment = data['concealment']
	extended = data['extended']
	mass = data['mass']
	flight_resist = data['flight_resist']
	flight_resist_check = data['flight_resist_check']
	flight_equip = data['flight_equip']
	flight_equip_type = data['flight_equip_type']
	flight_equipment = data['flight_equipment']
	flight_conditions = data['flight_conditions']
	acquatic_type = data['acquatic_type']
	ground_type = data['ground_type']
	ground_perm = data['ground_perm']
	ground_time = data['ground_time']
	ground_ranged = data['ground_ranged']
	ground_range = data['ground_range']
	special_type = data['special_type']
	teleport_type = data['teleport_type']
	teleport_change = data['teleport_change']
	teleport_portal = data['teleport_portal']
	teleport_obstacles = data['teleport_obstacles']
	dimension_type = data['dimension_type']
	dimension_mass_rank = data['dimension_mass_rank']
	dimension_descriptor = data['dimension_descriptor']
	special_space = data['special_space']
	special_time = data['special_time']
	special_time_carry = data['special_time_carry']
	condition = data['condition']
	condition_circ = data['condition_circ']
	condition_circ_check = data['condition_circ_check']
	objects_check = data['objects_check']
	objects_direction = data['objects_direction']
	objects_damage = data['object_damage']
	object_damage = data['object_damage']
	objects_strength = data['objects_strength']
	permeate_type = data['permeate_type']
	permeate_speed = data['permeate_speed']
	permeate_cover = data['permeate_cover']
	permeate_condition_solid = data['permeate_condition_solid']
	equip_type = data['equip_type']
	equipment = data['equipment']
	concealment_sense = data['concealment_sense']
	conceal_opposed = data['conceal_opposed']
	extended_actions = data['extended_actions']
	mass_value = data['mass_value']
	multiple = data['multiple']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_check(PowerDegree, degree, 'Degree', errors)
	errors = id_check(PowerCirc, circ, 'Circumstance', errors)
	errors = id_check(PowerDC, dc, 'DC', errors)
	errors = id_check(PowerTime, time, 'Time', errors)

	errors = id_check(PowerDegreeType, degree_type, 'Degree Group', errors)
	errors = id_check(PowerCircType, circ_type, 'Circumstance Group', errors)
	errors = id_check(PowerDCType, dc_type, 'DC Group', errors)
	errors = id_check(PowerTimeType, time_type, 'Time Group', errors)

	errors = id_check(PowerCheck, flight_resist_check, 'Variable Check', errors)
	errors = id_check(PowerTime, ground_time, 'Time Effect', errors)
	errors = id_check(PowerRangedType, ground_range, 'Ranged', errors)
	errors = id_check(PowerCheck, objects_check, 'Variable Check', errors)
	errors = id_check(PowerDamage, object_damage, 'Damage', errors)
	errors = id_check(PowerOpposed, conceal_opposed, 'Opposed Check', errors)

	errors = int_check(speed_rank, 'Speed Rank', errors)
	errors = int_check(speed_trait, 'Speed Trait', errors)
	errors = int_check(speed_value1, 'First Speed Value', errors)
	errors = int_check(speed_value2, 'Second Speed Value', errors)
	errors = int_check(distance_rank, 'Distance Rank', errors)
	errors = int_check(distance_value, 'Distance Value', errors)
	errors = int_check(distance_rank_trait, 'Trait', errors)
	errors = int_check(distance_rank_value1, 'Distance Furst Value', errors)
	errors = int_check(distance_rank_value2, 'Distance Second Value', errors)
	errors = int_check(distance_unit_trait, 'Distance Trait', errors)
	errors = int_check(distance_unit_value1, 'Distance Furst Value', errors)
	errors = int_check(distance_unit_value2, 'Distance Second Value', errors)
	errors = int_check(speed_rank_mod, 'Speed Rank Modifier', errors)
	errors = int_check(objects_strength, 'Strength Rank', errors)
	errors = int_check(speed_penalty, 'Penalty Modifier', errors)

	errors = int_check(dimension_mass_rank, 'Mass Rank', errors)
	errors = int_check(special_time_carry, 'Carry Mass', errors)
	errors = int_check(permeate_speed, 'Speed Rank', errors)
	errors = int_check(extended_actions, 'Extebded Actions', errors)
	errors = int_check(mass_value, 'Mass Rank', errors)

	errors = id_check(Math, speed_math1, 'Speed Msth 1', errors)
	errors = id_check(Math, speed_math2, 'Speed Msth 2', errors)
	errors = id_check(Unit, distance_units, 'Distance Units', errors)
	errors = id_check(Math, distance_rank_math1, 'Distance Msth 1', errors)
	errors = id_check(Math, distance_rank_math2, 'Distance Msth 2', errors)
	errors = id_check(Math, distance_unit_math1, 'Distance Msth 1', errors)
	errors = id_check(Math, distance_unit_math2, 'Distance Msth 2', errors)
	errors = id_check(Unit, distance_math_units, 'Distance Units', errors)

	errors = id_multiple(Condition, condition, 'Conditions', errors)
	errors = id_multiple(Condition, flight_conditions, 'Flight Conditions', errors)
	
	errors = id_check(EquipType, flight_equip_type, 'Equipment Type', errors, True)
	errors = id_check(Equipment, flight_equipment, 'Equipment', errors)
	errors = id_check(Ground, ground_type, 'Ground Type', errors)
	errors = id_check(PowerDes, dimension_descriptor, 'Dimension Descriptor', errors)
	errors = id_check(EquipType, equip_type, 'Equipment Type', errors, True)
	errors = id_check(Equipment, equipment, 'Equipment', errors)
	errors = id_check(Sense, concealment_sense, 'Sense', errors)
	errors = id_check(Check, condition_circ_check, 'No Circumstance Check', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = required(direction, 'Direction', errors)

	errors = of([speed, distance], 'You must set the effect speed or distance', errors)

	errors = variable_fields('rank', 'Speed Rank', speed, [speed_rank], errors)
	errors = variable_field('rank', speed, 'Rank', speed_rank, errors)

	errors = variable_fields('rank_mod', 'Speed Rank Modifier', speed, [speed_mod, speed_math, speed_rank_mod], errors)
	errors = variable_fields('rank_mod', speed, 'Modified Rank', speed_mod, errors)
	errors = variable_fields('rank_mod', speed, 'Math', speed_math, errors)
	errors = variable_fields('rank_mod', speed, 'Modifier', speed_rank_mod, errors)
	
	errors = variable_fields('penalty', 'Speed Penalty Modifier', speed, [speed_penalty], errors)

	errors = variable_fields('mod', 'Speed Modifier', speed, [speed_trait, speed_math1, speed_value1], errors)
	errors = variable_field('mod', speed, 'Trait', speed_trait, errors)
	errors = variable_field('mod', speed, 'First Math', speed_math1, errors)
	errors = variable_field('mod', speed, 'First Modifier', speed_value1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [speed_value2, speed_math2], errors)

	errors = variable_fields('max', 'Maximum Speed', speed, [speed_max], errors)
	errors = variable_field('max', speed, 'Maximum Speed Rank', speed_max, errors)

	errors = required_if_any(speed, 'Speed Description', speed_description, errors)

	errors = variable_fields('rank', 'Distance Rank', distance, [distance_rank], errors)
	errors = variable_field('rank', distance, 'Rank', distance_rank, errors)

	errors = variable_fields('unit', 'Distance Value', distance, [distance_value, distance_units], errors)
	errors = variable_field('unit', distance, 'Value', distance_value, errors)
	errors = variable_field('unit', distance, 'Units', distance_units, errors)

	errors = variable_fields('unit_math', 'Unit Modifier', distance, [distance_unit_trait, distance_unit_value1, distance_unit_math1, distance_math_units], errors)
	errors = variable_field('unit_math', distance, 'Trait', distance_unit_trait, errors)
	errors = variable_field('unit_math', distance, 'First Modifier', distance_unit_value1, errors)
	errors = variable_field('unit_math', distance, 'First Math', distance_unit_math1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [distance_unit_value2, distance_unit_math2], errors)
	errors = variable_field('unit_math', distance, 'Unit', distance_math_units, errors)

	errors = variable_fields('rank_math', 'Rank Modifier', distance, [distance_rank_trait, distance_rank_value1, distance_rank_math1], errors)
	errors = variable_field('rank_math', distance, 'Trait', distance_rank_trait, errors)
	errors = variable_field('rank_math', distance, 'First Modifier', distance_rank_value1, errors)
	errors = variable_field('rank_math', distance, 'First Math', distance_rank_math1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [distance_rank_value2, distance_rank_math2], errors)

	errors = required_if_any(distance, 'Distance Description', distance_description, errors)

	errors = check_fields(flight_resist, 'Flight Resistance Check', [flight_resist_check], errors)
	errors = check_field(flight_resist, 'Flight Resistance Check', 'Variable Check', flight_resist_check, errors)

	errors = check_fields(flight_equip, 'Flight Equipment', [flight_equipment], errors)
	errors = check_field(flight_equip, 'Flight Equipment', 'Equipment', flight_equipment, errors)
	
	errors = check_fields(aquatic, 'Aquatic', [acquatic_type], errors)
	errors = check_field(aquatic, 'Aquatic Type','Aquatic', acquatic_type, errors)

	errors = check_fields(ground, 'Through Ground', [ground_type, ground_perm], errors)
	errors = check_field(ground, 'Through Ground', 'Through Ground Type', ground_type, errors)
	errors = check_field(ground, 'Through Ground', 'Ground Permanance', ground_perm, errors)
	errors = variable_fields('temp', 'Temporary Ground Permanace', ground_permanence, [ground_time], errors)
	errors = variable_field('temp', ground_permanence, 'Time', ground_time, errors)
	errors = check_fields(ground_ranged, 'Ranged Through Ground', [ground_range], errors)
	errors = check_field(ground_ranged, 'Ranged Through Ground', 'Range', ground_range, errors)

	errors = check_fields(special, 'Special Travel', [special_type], errors)
	errors = variable_fields('dimension', 'Dimension Travel', special_type, [dimension_type, dimension_mass_rank], errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Type', dimension_type, errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Carry Mass', dimension_mass_rank, errors)
	errors = variable_fields('descriptor', 'Dimension Descriptor', dimension_type, [dimension_descriptor], errors)
	errors = variable_fields('space', 'Space Travel', special_type, [special_space], errors)
	errors = variable_field('space', special_type, 'Space Travel Type', special_space, errors) 
	errors = variable_fields('time', 'Time Travel', special_type, [special_time, special_time_carry], errors)
	errors = variable_field('time', special_type, 'Time Travel Type', special_time, errors)
	errors = variable_field('time', special_type, 'Time Travel Carry Mass', special_time_carry, errors)
	errors = variable_fields('teleport', 'Teleport', special_type, [teleport_type], errors)
	errors = variable_field('teleport',  special_type, 'Teleport Type', teleport_type, errors)

	errors = check_fields(condition_check, 'Movement Condition', [condition], errors)
	errors = check_field(condition_check, 'Movement Condition', 'Condition', condition, errors)
	errors = check_fields(condition_circ, 'No Movement Condition Circumstance', [condition_circ_check], errors)
	errors = check_field(condition_circ, 'No Movement Condition Circumstance', 'Check Type', condition_circ_check, errors)

	errors = check_fields(objects, 'Move Objects', [objects_check, objects_direction, objects_strength], errors)
	errors = check_field(objects, 'Move Objects', 'Move Objects Check', objects_check, errors)
	errors = check_field(objects, 'Move Objects', 'Move Objects Direction', objects_direction, errors)
	errors = check_field(objects, 'Move Objects', 'Strength Rank', objects_strength, errors)
	
	errors = check_fields(objects_damage, 'Move Objects Damage', [object_damage], errors)
	errors = check_field(objects_damage, 'Move Objects Damage', 'Damage', object_damage, errors)

	errors = check_fields(permeate, 'Permeate', [permeate_type, permeate_speed], errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Type', permeate_type, errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Speed Rank Modifier', permeate_speed, errors)
	errors = check_fields(permeate_condition_solid, 'Conditions', [condition], errors)
	errors - check_field(permeate_condition_solid, 'Conditions', 'Movement Conditions Only Through Solids', condition, errors)

	errors = check_fields(equip, 'Movement Equipment', [equipment], errors)
	errors = check_field(equip, 'Movement Equipment', 'Equipment', equipment, errors)

	errors = check_fields(concealment, 'Concealment', [concealment_sense, conceal_opposed], errors)
	errors = check_field(concealment, 'Concealment', 'Concealed from Sense', concealment_sense, errors)
	errors = check_fields(concealment, 'Concealment', 'Opponent Check', conceal_opposed, errors)

	errors = check_fields(extended, 'Extended', [extended_actions], errors)
	errors = check_field(extended, 'Extended', 'Extended Actions', extended_actions, errors)

	errors = check_fields(mass, 'Increased Mass', [mass_value], errors)
	errors = check_field(mass, 'Increased Mass', 'Increased Mass Amount', mass_value, errors)

	errors = seperate([dc, dc_type], 'DC', errors)
	errors = seperate([circ, circ_type], 'Circumstance', errors)
	errors = seperate([degree, degree_type], 'Degree', errors)
	errors = seperate([time, time_type], 'Time', errors)

	return (errors)

def power_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	description = data['description']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	time = data['time']
	keyword = data['keyword']
	degree_check = data['degree_check']
	circ_check = data['circ_check']
	dc_check = data['dc_check']
	time_check = data['time_check']
	degree_value = data['degree_value']
	dc_type = data['dc_type']
	dc_player = data['dc_player']
	circ_value = data['circ_value']
	time_type = data['time_type']
	recurring_type = data['recurring_type']
	recurring_degree_type = data['recurring_degree_type']
	variable = data['variable']
	title = data['title']
	opponent = data['opponent']
	opposed = data['opposed']
	variable_type = data['variable_type']
	before = data['before']
	after = data['after']
	power_check = data['power_check']
	power_action = data['power_action']
	attack_player = data['attack_player']
	attack_opp = data['attack_opp']
	turn = data['turn']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(mod, 'Player Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)
	errors = id_check(Check, player_check, 'Player Check', errors)
	errors = id_check(Check, opponent_check, 'Opponent Check', errors)
	errors = id_check(Ranged, attack_player, 'Player Attack Range', errors)
	errors = id_check(Ranged, attack_opp, 'Opponent Attack Range', errors)

	errors = id_check(PowerDegreeType, degree, 'Degree Group', errors)
	errors = id_check(PowerCircType, circ, 'Circumstance Group', errors)
	errors = id_check(PowerDC, dc, 'DC', errors)
	errors = id_check(PowerTime, time, 'DC', errors)
	errors = id_check(PowerTime, recurring_value, 'Recurring Time', errors)
	errors = id_check(PowerDegree, degree_value, 'Degree', errors)
	errors = id_check(PowerDCType, dc_type, 'DC Group', errors)
	errors = id_check(PowerDC, dc_player, 'Player DC', errors)
	errors = id_check(PowerCirc, circ_value, 'Degree', errors)
	errors = id_check(PowerTimeType, time_type, 'Time Group', errors)
	errors = id_check(PowerTimeType, recurring_type, 'Recurring Time Group', errors)
	errors = id_check(PowerCheck, variable, 'Vsriable Check', errors)
	errors = id_check(PowerDegreeType, recurring_degree_type, 'Recurring Degree Effect Group', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(attached, 'Attsched', errors)
	errors = required(opponent_trait_type, 'Opponent Check Trait Typr', errors)
	errors = required(opponent_trait, 'Opponent Check Trait', errors)
	errors = required(opponent_check, 'Opponennt Check', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(description, 'Description', errors)
	errors = required(title, 'Title', errors)

	errors = check_fields(recurring, 'Recurring', [recurring_value, turn], errors)
	errors = check_field(recurring, 'Recurring', 'Time Betweem Checks', recurring_value, errors)
	errors = check_field(recurring, 'Recurring', 'Turn', turn, errors)

	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC', errors)
	
	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC value', errors)
	errors = select_check('6', player_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', player_check, dc_check, 'Skill Check', 'a DC value', errors)

	errors = variable_field('5', opponent_check, 'Opponent Attack Check Range', attack_opp, errors)
	errors = variable_field('5', player_check, 'Player Attack Check Range', attack_player, errors)

	errors = check_of(circ_check, 'Circumstance', 'a circums6ance modifier or circumstance group', [circ_value, circ], errors)
	errors = check_of(dc_check, 'DC', ' a dc value or dc group', [dc_player, dc_type, dc], errors)
	errors = check_of(degree_check, 'Degree', 'a degree value or degree group', [degree_value, degree], errors)
	errors = check_of(time_check, 'Time', 'a time effect or time effect group', [time, time_type], errors)
	errors = check_of(recurring, 'Recurring', 'recurring time or time effect group', [recurring_value, recurring_type], errors)
	errors = seperate([recurring_value, recurring_type], 'recurring', errors)

	errors = variable_field('before', attached, 'Before Check', before, errors) 
	errors = variable_field('after', attached, 'After Check', after, errors)
	errors = variable_field('before_var', attached, 'Before Check', before, errors)
	errors = variable_field('before_opponent', attached, 'Before Check', before, errors)
	errors = variable_field('after_var', attached, 'After Check', after, errors)
	errors = variable_field('after_opponent', attached, 'After Check', after, errors)
	errors = variable_field('primary', attached, 'Frequency', frequency, errors)
	errors = variable_field('after_opponent', attached, 'After Check', turn, errors)
	errors = variable_field('after_var', attached, 'After Check', turn, errors)
	errors = variable_field('after', attached, 'After Check', turn, errors)

	errors = select_of('opponent', 'Happens After an Opponent Check', 'Attached', attached, [opponent, opposed], ['Opponent Check'], errors)
	errors = seperate([opposed, opponent], 'Opponent Check', errors)

	errors = select_of('before_var', 'Before Variable Check', 'Attached', attached, [variable, variable_type], ['Variable Check'], errors)
	errors = seperate([variable, variable_type], 'Variable Check', errors)
	
	errors = select_of('after_var', 'After Variable Check', 'Attached', attached, [variable, variable_type], ['Variable Check'], errors)
	errors = seperate([variable, variable_type], 'Variable Check', errors)

	errors = linked_group_check(PowerDC, '1', opponent_check, 'opp', 'target', dc_type, 'title', 'an Opponent Skill Check', 'DC', 'Opponent DC', errors, True)
	errors = linked_group_check(PowerDC, '6', opponent_check, 'opp', 'target', dc_type, 'title', 'an Opponent Resistance Check Check', 'DC', 'Opponent DC', errors, True)

	return (errors)

def power_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	math_units = data['math_units']
	recovery_penalty = data['recovery_penalty']
	recovery_incurable = data['recovery_incurable']
	turns = data['turns']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	keyword = data['keyword']
	title = data['title']
	circ_type = data['circ_type']
	degree_type = data['degree_type']
	dc_type = data['dc_type']
	time = data['time']
	mod = data['mod']
	recovery_target = data['recovery_target']
	factor = data['factor']
	check_type = data['check_type']
	action = data['action']
	points = data['points']
	value_rank = data['value_rank']



	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

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
	errors = int_check(time, 'Time Rank', errors)
	errors = int_check(mod, 'Time Rank Modifier', errors)
	errors = int_check(factor,  'Factor', errors)

	errors = int_check(turns, 'Turns', errors)
	errors = id_check(PowerDegree, degree, 'Degree', errors)
	errors = id_check(PowerCirc, circ, 'Circumstance', errors)
	errors = id_check(PowerDC, dc, 'DC', errors)
	errors = id_check(PowerDegreeType, degree_type, 'Degree Group', errors)
	errors = id_check(PowerCircType, circ_type, 'Circumstance Group', errors)
	errors = id_check(PowerDCType, dc_type, 'DC Group', errors)
	errors = id_check(PowerCheck, check_type, 'Check', errors)

	errors = id_check(Action, action)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(type, 'Time Type', errors)
	errors = required(value_type, 'Type', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('value', 'Time Value', value_type, [units, value], errors)
	errors = variable_field('value', value_type, 'Time Value', value, errors)
	errors = variable_field('value', value_type, 'Units', units, errors)

	errors = variable_fields('math', 'Time Math', value_type, [trait_type, trait, math, math_value, math_units], errors)
	errors = variable_field('math', value_type, 'Trait Type', trait_type, errors)
	errors = variable_field('math', value_type, 'Trait', trait, errors)
	errors = variable_field('math', value_type, 'Math', math, errors)
	errors = variable_field('math', value_type, 'Value', math_value, errors)
	errors = variable_field('math', value_type, 'Units', math_units, errors)

	errors = variable_fields('rank', 'Time Measurement', value_type, [rank_math], errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank1, rank1_value], ['first rank', 'first value'], errors)
	errors = variable_field('rank', value_type, 'Math', rank_math, errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank2, rank2_value], ['second rank', 'second value'], errors)

	errors = variable_fields('turns', 'Turns', value_type, [turns], errors)

	errors = variable_fields('time', 'Time Rank', value_type, [time], errors)

	errors = variable_fields('mod', 'Time Rank Modifier', value_type, [mod], errors)
	
	errors = variable_fields('factor', 'Factor Modifier', value_type, [factor], errors)

	errors = variable_fields('recover', 'Recovery Time', type, [recovery_target], errors)
	errors = variable_field('recover', type, 'Recovery Target', recovery_target, errors)

	errors = variable_fields('check', 'Time Until Next Check', type, [check_type], errors)
	errors = variable_field('check', type, 'Check', check_type, errors)
	
	errors = variable_fields('action', 'Time Until Take New Action', type, [action], errors)
	errors = variable_field('action', type, 'Action Type', action, errors)

	errors = variable_fields('points', 'Points Restored', type, [points], errors)
	errors = variable_field('points', type, 'Points', points, errors)

	errors = seperate([dc, dc_type], 'DC', errors)
	errors = seperate([circ, circ_type], 'Circumstance', errors)
	errors = seperate([degree, degree_type], 'Degree', errors)

	return (errors)


def power_condition_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	condition_type = data['condition_type']
	condition = data['condition']
	condition_null = data['condition_null']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage_value = data['damage_value']
	damage = data['damage']
	time_effect = data['time_effect']
	time_last = data['time_last']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(damage_value, 'Condition Damage', errors)
	errors = int_check(damage, 'Damage Direction', errors)

	errors = id_check(Advantage, advantage_id, 'Advantage', errors)
	errors = id_check(Benefit, benefit, 'Benefit', errors)
	errors = id_check(PowerTime, time_effect, 'Time Until Condition Takes Effect', errors)
	errors = id_check(PowerTime, time_last, 'Time Condition Lasts', errors)

	errors = required(condition_type, 'Condition Type', errors)

	errors = required(extra_id, 'Base Power or Extra', errors)
	errors = required(target, 'Target', errors)
	errors = required(time_effect, 'Time Until Condition Takes Effect', errors)

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



def power_cost_post_errors(data):
	
	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	keyword = data['keyword']
	cost = data['cost']
	rank = data['rank']
	flat = data['flat']
	extra = data['extra']
	base_flat = data['base_flat']
	base_cost = data['base_cost']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(cost, 'Cost', errors)
	errors =  int_check(rank, 'Per Rank', errors)
	
	errors = required(keyword, 'Keyword', errors)
	errors = required(cost, 'Cost', errors)
	errors = required(rank, 'Per Rank', errors)

	errors = cost_error(cost, power_id, extra, base_cost, base_flat)

	return (errors)

def power_ranks_post_errors(data):
	
	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	cost = data['cost']
	ranks = data['ranks']
	extra = data['extra']
	base_ranks = data['base_ranks']
	base_cost = data['base_cost']
	base_flat = data['base_flat']
	effect = data['effect']
	required =  data['required']
	required_type = data['required_type']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors =  int_check(ranks, 'Ranks', errors)
	
	errors = required(ranks, 'Ranks', errors)
	errors = required(effect, 'Effect', errors)

	errors = dependent('Required Extra', required_type, [required], errors)
	errors = dependent('Required Extra', required, [required_type], errors)

	errors = ranks_error(cost, ranks, base_cost, base_ranks, base_flat, extra)

	return (errors)

def power_extra_post_errors(data):
	
	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	name = data['name']
	cost = data['cost']
	ranks = data['ranks']
	des = data['des']
	inherit = data['inherit']
	alternate = data['alternate']
	flat = data['flat']
	type = data['type']
	required_check = data['required_check']
	required = data['required']
	required_power = data['required_power']
	required_power_rank = data['required_power_rank']
	extra_effect = data['extra_effect']
	extra_effect_count = data['extra_effect_count']
	variable = data['variable']
	character = data['character']
	circ = data['circ']
	create = data['create']
	damage = data['damage']
	dc = data['dc']
	defense = data['defense']
	degree = data['degree']
	env = data['env']
	minion = data['minion']
	mod = data['mod']
	move = data['move']
	opposed = data['opposed']
	ranged = data['ranged']
	sense = data['sense']
	time = data['time']
	target_type = data['target_type']
	target = data['target']
	target_check = data['target_check']
	action_check = data['action_check']
	action = data['action']
	action_type = data['action_type']
	routine = data['routine']
	skill_type = data['skill_type']
	skill = data['skill']
	range_check = data['range_check']
	range = data['range']
	auto = data['auto']
	auto_type = data['auto_type']
	auto_check = data['auto_check']
	auto_check_type = data['auto_check_type']
	auto_opposed = data['auto_opposed']
	auto_opposed_type = data['auto_opposed_type']
	ranks_check = data['ranks_check']
	ranks_type = data['ranks_type']
	rank = data['rank']

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)

	errors = int_check(cost, 'Cost', errors)
	errors = int_check(ranks, 'Ranks', errors)

	errors = id_check(Power, inherit, 'Inherited Power', errors)
	errors = id_check(Action, action, 'Action', errors)
	errors = id_check(Ranged, range, 'Range', errors)
	errors = id_check(Skill, skill_type, 'Skill', errors)
	errors = id_check(SkillBonus, skill, 'Enhanced Skill', errors)
	errors = id_check(Extra, required, 'Required Extra', errors)
	errors = id_check(PowerCheck, auto_check, 'Automatic Check', errors)
	errors = id_check(PowerCheckType, auto_check_type, 'Automatic Check Group', errors)
	errors = id_check(PowerOpposed, auto_opposed, 'Automatic Opponent Check', errors)
	errors = id_check(PowerOpposedType, auto_opposed_type, 'Automatic Opponent Check Group', errors)

	errors = id_check(Power, required_power, 'Required Power', errors)

	errors = required(name, 'Name', errors)
	errors = not_required(alternate, cost, 'Cost', errors)
	errors = not_required(alternate, ranks, 'Ranks', errors, 'x', cost)
	errors = required(des, 'Description', errors)
	errors = required(type, 'Effect Type', errors)
	errors = check_fields(extra_effect, 'Extra Effect', [extra_effect_count], errors)
	errors = check_field(extra_effect, 'Extra Effect', 'Extra Effects Count', extra_effect_count, errors)

	errors = check_of(required_check, 'Required', 'a Required Extra or Required Power', [required, required_power], errors)
	errors = required_if_any(required_power, 'Required Power Ranks', required_power_rank, errors)

	errors = check_fields(auto, 'Automatic Check', [auto_type], errors)
	errors = check_field(auto, 'Automatic Check', 'Check Type', auto_type, errors)
	errors = variable_fields('check', 'Automatic Check', auto_type, [auto_check], errors)
	errors = variable_field('check', auto_type, 'Check', auto_check, errors)
	errors = variable_fields('check_type', 'Automatic Check Group', auto_type, [auto_check_type], errors)
	errors = variable_field('check_type', auto_type, 'Check Group', auto_check_type, errors)
	errors = variable_fields('opposed', 'Automatic Opponent Check', auto_type, [auto_opposed], errors)
	errors = variable_field('opposed', auto_type, 'Opponent Check', auto_opposed, errors)
	errors = variable_fields('opposed_type', 'Automatic Opponent Check Group', auto_type, [auto_opposed_type], errors)
	errors = variable_field('opposed_type', auto_type, 'Opponent Check Group', auto_opposed_type, errors)


	errors = check_fields(target_check, 'Changes Target', [target, target_type], errors)
	errors = check_field(target_check, 'Changes Target', 'Changes Target Type', target_type, errors)
	errors = check_field(target_check, 'Changes Target', 'Tsrget', target, errors)

	errors = check_fields(action_check, 'Changes Action', [action, action_type], errors)
	errors = check_field(action_check, 'Changes Action', 'Action', action, errors)
	errors = check_field(action_check, 'Changes Action', 'Action Change Type', action_type, errors)

	errors = check_fields(routine, 'Routine Skill Check', [skill_type], errors)
	errors = check_field(routine, 'Routine Skill Check', 'Skill', skill_type, errors)

	errors = check_fields(range_check, 'Changes Range', [range], errors)
	errors = check_field(range_check, 'Changes Range', 'Range', range, errors)

	errors = check_fields(ranks_check, 'Rank Only', [ranks_type, rank], errors)
	errors = check_field(ranks_check, 'Rank Only', 'Rank Type', ranks_type, errors)
	errors = check_field(ranks_check, 'Rank Only', 'Rank', rank, errors)

	errors = variable_fields('required', 'Overwrites Required', effect, [required], errors)
	errors = variable_fields('required', effect, 'Overwrites Required', required, errors)

	errors = multiple_error(degree, 'Degree of Success/Failure Effect', PowerDegree, power_id, errors, PowerDegreeType, 'value')
	errors = multiple_error(mod, 'Modifiers', PowerMod, power_id, errors)
	errors = multiple_error(variable, 'Variable Checks', PowerCheck, power_id, errors, PowerCheckType)
	errors = multiple_error(opposed, 'Opponent Checks', PowerOpposed, power_id, errors, PowerOpposedType)
	errors = multiple_error(character, 'Changes Character Traits', PowerChar, power_id, errors)
	errors = multiple_error(defense, 'Defensive Effect', PowerDefense, power_id, errors)
	errors = multiple_error(sense, 'Sense Effect', PowerSenseEffect, power_id, errors)
	errors = multiple_error(create, 'Create Effect', PowerCreate, power_id, errors)
	errors = multiple_error(move, 'Movement Effect', PowerMove, power_id, errors)
	
	

	return (errors)
