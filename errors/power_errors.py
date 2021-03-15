
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerCost, PowerRanks, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import PowerCircType, PowerDCType, PowerDegreeType, PowerMoveType, PowerRangedType, PowerTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert, db_multiple, id_multiple
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, not_required
from functions.create_posts import send_multiple, one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string, circ_cell

from create_functions.power_create import power_check, rule_check, rule_select, cost_check, extra_cost, extra_check, extra_convert, field_cost, multiple_cost, variable_cost, sense_cost, power_rules, valid_extra, ranks_error, ranks_function, cost_error, cost_exist, cost_check_table

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
	errors = rule_select('rank', power_range, 'Ranged', PowerRanged, power_id, errors)
	errors = rule_select('sense', power_type, 'Sense', PowerSenseEffect, power_id, errors)
	errors = rule_select('move', power_type, 'Movement', PowerMove, power_id, errors)
	errors = rule_select('2', check_type, 'Opposed Check', PowerOpposed, power_id, errors)


	errors = cost_exist(power_id, cost)

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
	limbs_continuous = data['limbs_continuous']
	limbs_sustained = data['limbs_sustained']
	limbs_distracting = data['limbs_distracting']
	limbs_projection = data['limbs_projection']
	carry_capacity = data['carry_capacity']
	points_value = data['points_value']
	points_trait_type = data['points_trait_type']
	points_trait = data['points_trait']
	points_descriptor = data['points_descriptor']
	appear_target = data['appear_target']
	appear_description = data['appear_description']
	insub_type = data['insub_type']
	insub_description = data['insub_description']
	cost = data['cost']
	ranks = data['ranks']

	errors = id_check(PowerCost, cost)
	errors = id_check(PowerRanks, ranks)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(value, 'Increased By', errors)
	errors = int_check(increase, 'Per Rank', errors)
	errors = int_check(reduced_value, 'Reduced', errors)
	errors = int_check(carry_capacity, 'Carry Capacity', errors)
	errors = int_check(points_value, 'Points', errors)


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

	errors = check_of(limbs, 'Extra Limbs', [limbs_continuous, limbs_sustained, limbs_distracting, limbs_projection], errors)
	errors = check_field(carry, 'Extra Carry', 'Carry Capacity', carry_capacity, errors)
	errors = check_fields(points, 'Hero Points', [points_value, points_trait_type, points_trait], errors)
	errors = check_field(points, 'Hero Points', 'Points Value', points_value, errors)
	errors = check_field(points, 'Hero Points', 'Trait Type', points_trait_type, errors)
	errors = check_field(points, 'Hero Points', 'Trait', points_trait, errors)

	errors = check_fields(appear, 'Alters Appearance', [appear_target, appear_description], errors)
	errors = check_field(appear, 'Alters Appearance', 'Target', appear_target, errors)
	errors = check_field(appear, 'Alters Appearance', 'Description', appear_description, errors)

	errors = check_fields(insubstantial, 'Insubstantial', [insub_type, insub_description], errors)
	errors = check_field(insubstantial, 'Insubstantial', 'Insubstantial Type', insub_type, errors)
	errors = check_field(insubstantial, 'Insubstantial', 'Insubstantial Description', insub_description, errors)

	errors = check_fields(weaken, 'Weaken', [weaken_type], errors)
	errors = check_field(weaken, 'Weaken', 'Weaken Type', weaken_type, errors)
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
	move_player_trait = data['move_player_trait']
	move_opponent_check = data['move_opponent_check']
	move_opponent_ability = data['move_opponent_ability']
	move_opponent_rank = data['move_opponent_rank']
	trap_type = data['trap_type']
	trap_dc = data['trap_dc']
	trap_trait_type = data['trap_trait_type']
	trap_trait = data['trap_trait']
	trap_resist_check = data['trap_resist_check']
	trap_resist_trait = data['trap_resist_trait']
	trap_resist_dc = data['trap_resist_dc']
	trap_escape = data['trap_escape']
	ranged_type = data['ranged_type']
	ranged_dc = data['ranged_dc']
	ranged_trait_type = data['ranged_trait_type']
	ranged_trait = data['ranged_trait']
	ranged_damage_type = data['ranged_damage_type']
	ranged_damage_value = data['ranged_damage_value']
	weapon_trait_type = data['weapon_trait_type']
	weapon_trait = data['weapon_trait']
	weapon_mod = data['weapon_mod']
	weapon_damage_type = data['weapon_damage_type']
	weapon_damage = data['weapon_damage']
	support_strength = data['support_strength']
	support_strengthen = data['support_strengthen']
	support_action = data['support_action']
	support_action_rounds = data['support_action_rounds']
	support_effort = data['support_effort']
	support_effort_rounds = data['support_effort_rounds']
	cost = data['cost']
	ranks = data['ranks']

	errors = id_check(PowerCost, cost)
	errors = id_check(PowerRanks, ranks)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Complex, complexity, 'complexity', errors)
	errors = id_check(Ability, move_opponent_ability, 'ability', errors)

	errors = int_check(volume, 'Volume', errors)
	errors = int_check(toughness, 'Toughness', errors)
	errors = int_check(mass, 'Mass', errors)
	errors = int_check(transform_start_mass, 'Transform Starting Mass', errors)
	errors = int_check(transfom_mass, 'Transform Ending Mass', errors)
	errors = int_check(move_opponent_rank, 'Rank for Opponent to Move', errors)
	errors = int_check(trap_dc, 'Trap DC', errors)
	errors = int_check(trap_resist_dc, 'Trap Resistance DC', errors)
	errors = int_check(ranged_dc, 'Ranged DC', errors)
	errors = int_check(ranged_damage_value, 'Ranged Damage Value', errors)
	errors = int_check(weapon_mod, 'Weapon Modifier', errors)
	errors = int_check(weapon_damage, 'Weapon Damage', errors)
	errors = int_check(support_strength, 'Support Strength Rank', errors)
	errors = int_check(support_action, 'Strengthen With Action Modifier', errors)
	errors = int_check(support_action_rounds, 'Strengthen with Action Number of Rounds', errors)
	errors = int_check(support_effort, 'Strengthen with Extra Effort Bonus', errors)
	errors = int_check(support_effort_rounds, 'Strengthen with Extra Effort Number of Rounds', errors)


	errors = together_names('Creating an object', ['Solidity', 'Visibility', 'Complexity', 'Volume Rank', 'Toughness', 'Mass Rank'], [solidity, visibility, complexity, volume, toughness, mass], errors)
	errors = check_fields(moveable, 'Moveable', [move_player], errors)
	errors = check_field(moveable, 'Moveable', 'Moveable With', move_player, errors)
	errors = select_variable('ability', move_player,  'an Ability', 'Trait', move_player_trait, errors)
	errors = select_variable('skill', move_player, 'a Skill', 'Trait',  move_player_trait, errors)
	errors = select_variable('bonus', move_player, 'an Enhanced Skill', 'Trait',  move_player_trait, errors)
	errors = select_variable('defense', move_player, 'a Defense', 'Trait',  move_player_trait, errors)
	errors = select_variable('power', move_player, 'a Power', 'Trait',  move_player_trait, errors)
	errors = check_fields(move_opponent_check, 'Opponent Can Move the Object', [move_opponent_ability, move_opponent_rank, errors], errors)
	errors = check_field(move_opponent_check, 'Opponent Can Move the Object', 'Ability', move_opponent_ability, errors)
	errors = check_field(move_opponent_check, 'Opponent Can Move the Object', 'Rank', move_opponent_rank, errors)
	errors = check_fields(stationary, 'Stationary', [move_player], errors)
	errors = check_field(stationary, 'Stationary', 'Moveable With', move_player, errors)
	
	errors = check_fields(trap, 'Trap', [trap_type, trap_resist_check, trap_resist_trait, trap_resist_dc], errors)
	errors = check_field(trap, 'Trap', 'Trap Check Type', trap_type, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance Trait Type', trap_resist_check, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance Trait', trap_resist_trait, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance DC', trap_resist_dc, errors)
	errors = variable_fields('dc', 'Trap DC', trap_type, [trap_dc], errors)
	errors = variable_fields('trait', 'Trap Check Against Trait', trap_type, [trap_trait_type, trap_trait], errors)
	errors = variable_field('trait', trap_type, 'Trap Check Against Trait Type', trap_trait_type, errors)
	errors = variable_field('trait', trap_type, 'Trap Check Against Trait', trap_trait, errors)

	errors = check_fields(ranged, 'Ranged Attack', [ranged_type, ranged_damage_type], errors)
	errors = check_field(ranged, 'Ranged Attack', 'Ranged Check Type', ranged_type, errors)
	errors = check_field(ranged, 'Ranged Attack', 'Ranged Damage Type', ranged_damage_type, errors)
	errors = variable_fields('dc', 'Ranged DC', ranged_type, [ranged_dc], errors)
	errors = variable_fields('target', 'Ranged Target Trait', ranged_type, [ranged_trait_type, ranged_trait], errors)
	errors = variable_fields('player', 'Ranged Player Trait', ranged_type, [ranged_trait_type, ranged_trait], errors)
	errors = variable_field('target', ranged_type, 'Ranged Target Trait Type', ranged_trait_type, errors)
	errors = variable_field('target', ranged_type, 'Ranged Target Trait', ranged_trait, errors)
	errors = variable_field('player', ranged_type, 'Ranged Player Trait Type', ranged_trait_type, errors)
	errors = variable_field('player', ranged_type, 'Ranged Player Trait', ranged_trait, errors)
	errors = variable_fields('value', 'Ranged Damage Value', ranged_damage_type, [ranged_damage_value], errors)

	errors = check_fields(weapon, 'Weapon', [weapon_trait_type, weapon_trait, weapon_mod, weapon_damage_type], errors)
	errors = check_field(weapon, 'Weapon', 'Weapon Trait Type', weapon_trait_type, errors)
	errors = check_field(weapon, 'Weapon', 'Wespon Trait', weapon_trait, errors)
	errors = check_field(weapon, 'Weapon', 'Weapon Modifier', weapon_mod, errors)
	errors = check_field(weapon, 'Weapon', 'Weapon Damage Type', weapon_damage_type, errors)
	errors = variable_fields('value', 'Weapon Damage Value', weapon_damage_type, [weapon_damage], errors)

	errors = check_fields(support, 'Supports Weight', [support_strength], errors)
	errors = check_field(support, 'Supports Weight', 'Supports Weight Strength Rank', support_strength, errors)
	errors = check_together_var(support_strengthen, 'Suupports Weight and Can Strengthen', 'Complete the action fields or extra effort fields (or all)', [[support_action, support_action_rounds], [support_effort, support_effort_rounds]], errors)

	errors = check_fields(transform, 'Transform', [transform_type, transform_start_mass, transfom_mass], errors)
	errors = check_field(transform, 'Transform', 'Transform Type', transform_type, errors)
	errors = check_field(transform, 'Transform', 'Transform Starting Mass', transform_start_mass, errors)
	errors = check_field(transform, 'Transform', 'Transform Ending Mass', transfom_mass, errors)

	errors = together('a Transform Descriptor', [transform_start_descriptor, transform_end_descriptor], errors)

	return (errors)

def damage_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	strength = data['strength']
	damage_type = data['damage_type']
	descriptor = data['descriptor']
	keyword = data['keyword']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = id_multiple(Descriptor, damage_type, 'Damage Type', errors)
	errors = id_multiple(PowerDes, descriptor, 'Descriptor', errors)

	errors = int_check(mod, 'Modifier', errors)

	errors = required(trait_type, 'Trait Type', errors)
	errors = required(trait, 'Trait', errors)
	errors = required(mod, 'Mod', errors)
	errors = required(keyword, 'Keyword', errors)

	errors = of([damage_type, descriptor], 'You must choose a damage type or descriptor for the damage effect.', errors)


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
	resist_area = data['resist_area']
	resist_perception = data['resist_perception']
	reflect = data['reflect']
	immunity = data['immunity']
	reflect_action = data['reflect_action']
	reflect_check = data['reflect_check']
	reflect_dc = data['reflect_dc']
	reflect_opposed_trait_type = data['reflect_opposed_trait_type']
	reflect_opposed_trait = data['reflect_opposed_trait']
	reflect_resist_trait_type = data['reflect_resist_trait_type']
	reflect_resist_trait = data['reflect_resist_trait']
	immunity_type = data['immunity_type']
	immunity_trait_type = data['immunity_trait_type']
	immunity_trait = data['immunity_trait']
	immunity_descriptor = data['immunity_descriptor']
	immunity_damage = data['immunity_damage']
	immunity_rule = data['immunity_rule']
	cover_check = data['cover_check']
	cover_type = data['cover_type']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	print('\n\n\n\n\n')
	print(reflect_action)
	
	errors = id_check(Action, reflect_action, 'Action', errors)

	print(reflect_check)
	errors = id_check(Check, reflect_check, 'Check', errors)
	errors = id_check(Descriptor, immunity_damage, 'Descriptor', errors)

	errors = together('a die roll', [roll, outcome], errors)
	errors = check_fields(reflect, 'Reflects Attacks', [reflect_action, reflect_check], errors)
	errors = check_field(reflect, 'Reflects Attacks', 'Reflect Action Type', reflect_action, errors)
	errors = check_field(reflect, 'Reflects Attacks', 'Reflect Check Type', reflect_check, errors)

	value = reflect_check
	fields = field('Trait Type', reflect_opposed_trait_type)
	fields = field('Trait', reflect_opposed_trait, fields)
	errors = variable('Opposed Check', '2', value, fields, errors)
	fields = field('DC', reflect_dc)
	errors = variable('Skill Check', '1', value, fields, errors)
	fields = field('Trait Type', reflect_resist_trait)
	fields = field('Trait', reflect_resist_trait_type, fields)
	errors = variable('Resistance Check', '6', value, fields, errors)

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
	selective = data['selective']
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
	visibility_trait_type = data['visibility_trait_type']
	visibility_trait = data['visibility_trait']
	visibility_mod = data['visibility_mod']
	cost = data['cost']
	ranks = data['ranks']

	errors = id_check(PowerCost, cost)
	errors = id_check(PowerRanks, ranks)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(radius, 'Starting Radius', errors)
	errors = int_check(distance, 'Distance', errors)
	errors = int_check(rank, 'Per Rank', errors)
	errors = int_check(move_speed, 'Movement Speed', errors)
	errors = int_check(visibility_mod, 'Visibility Modifier', errors)


	errors = together_names('an Environmental Effect Range', ['Starting Radius', 'Distance Rank', 'Cost Per Rank'], [radius, distance, rank], errors)
	errors = check_fields(condition_check, 'Environmental Condition', [condition_temp_type, temp_extremity], errors)
	errors = check_field(condition_check, 'Environmental Condition', 'Temperature Type', condition_temp_type, errors)
	errors = check_field(condition_check, 'Environmental Condition', 'Temperature Extremity', temp_extremity, errors)
	errors = check_fields(impede, 'Impedes Movement', [move_nature, move_speed], errors)
	errors = check_field(impede, 'Impedes Movement', 'Impedes Movement Nature Type', move_nature, errors)
	errors = check_field(impede, 'Impedes Movement', 'Impedes Movement Speed Modifier', move_speed, errors)
	errors = select_variable('other', move_nature, 'another nature type for impeding movement', 'other', move_other, errors)
	errors = check_fields(conceal, 'Light', [conceal_type], errors)
	errors = check_field(conceal, 'Light', 'Counters Concealment Type', conceal_type, errors)
	errors = check_fields(visibility, 'Visibility', [visibility_trait_type, visibility_trait, visibility_mod], errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Trait Type', visibility_trait_type, errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Trait', visibility_trait, errors)
	errors = check_field(visibility, 'Visibility', 'Visibility Modifier', visibility_mod, errors)
	
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
	effortless_degree = data['effortless_degree']
	effortless_retries = data['effortless_retries']
	simultaneous_descriptor = data['simultaneous_descriptor']
	area_mod = data['area_mod']
	area_range = data['area_range']
	area_per_rank = data['area_per_rank']
	area_descriptor = data['area_descriptor']
	limited_type = data['limited_type']
	limited_mod = data['limited_mod']
	limited_level = data['limited_level']
	limited_source = data['limited_source']
	limited_task_type = data['limited_task_type']
	limited_task = data['limited_task']
	limited_trait_type = data['limited_trait_type']
	limited_trait = data['limited_trait']
	limited_description = data['limited_description']
	limited_subjects = data['limited_subjects']
	limited_extra = data['limited_extra']
	limited_language_type = data['limited_language_type']
	limited_degree = data['limited_degree']
	limited_sense = data['limited_sense']
	limited_subsense = data['limited_subsense']
	limited_descriptor = data['limited_descriptor']
	limited_range = data['limited_range']
	side_effect_type = data['side_effect_type']
	side_level = data['side_level']
	side_other = data['side_other']
	reflect_check = data['reflect_check']
	reflect_trait_type = data['reflect_trait_type']
	reflect_trait = data['reflect_trait']
	reflect_descriptor = data['reflect_descriptor']
	subtle_opponent_trait_type = data['subtle_opponent_trait_type']
	subtle_opponent_trait = data['subtle_opponent_trait']
	subtle_dc = data['subtle_dc']
	subtle_null_trait_type = data['subtle_null_trait_type']
	subtle_null_trait = data['subtle_null_trait']
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
	ranks = data['ranks']
	cost = data['cost']

	errors = id_check(PowerCost, cost)
	errors = id_check(PowerRanks, ranks)

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Defense, objects_alone, 'defense', errors)
	errors = id_check(Defense, objects_character, 'defense', errors)
	errors = id_check(Levels, limited_level, 'level', errors)
	errors = id_check(Extra, limited_extra, 'extra', errors)
	errors = id_check(Sense, limited_sense, 'sense', errors)
	errors = id_check(Range, limited_range, 'range', errors)
	errors = id_check(Levels, side_level, 'level', errors)
	errors = id_check(Check, reflect_check, 'check', errors)
	
	errors = int_check(effortless_degree, 'Effortless Degree', errors)
	errors = int_check(area_mod, 'Area Modifier', errors)
	errors = int_check(area_range, 'Area Range', errors)
	errors = int_check(limited_mod, 'Limited Modifier', errors)
	errors = int_check(limited_subjects, 'limited by Number of Subjects', errors)
	errors = int_check(limited_degree, 'limited by Degree', errors)
	errors = int_check(subtle_dc, 'Subtle DC', errors)
	errors = int_check(ranks_ranks, 'Number of Ranks', errors)
	errors = int_check(ranks_mod, 'Ranks Modifier', errors)
	errors = int_check(points_reroll_cost, 'Reroll Cost', errors)
	errors = int_check(points_rerolls, 'Number of Rerolls', errors)


	errors = check_fields(affects_objects, 'Affects Objects', [], errors)
	
	errors = check_fields(area, 'Area', [objects_alone, objects_character], errors)
	errors = check_field(area, 'Area', 'Affect Object Alone', objects_alone, errors)
	errors = check_field(area, 'Area', 'Affect Object with Character', objects_character, errors)
	
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

	errors = variable_fields('degree', 'Limited by Degree of Success', limited_type, [limited_degree], errors)
	errors = variable_field('degree', limited_type, 'Degree of Success', limited_degree, errors)

	errors = variable_fields('sense', 'Limited by Sense', limited_type, [limited_sense], errors)
	errors = variable_field('sense', limited_type, 'Sense', limited_sense, errors)

	errors = variable_fields('range', 'Limited by Range', limited_type, [limited_range], errors)
	errors = variable_field('range', limited_type, 'Range', limited_range, errors)

	errors = variable_fields('source', 'Requires Descriptor', limited_type, [limited_source], errors)
	errors = variable_field('source', limited_type, 'Required Descriptor', limited_source, errors)

	errors = variable_fields('other', 'Limited by Other', limited_type, [limited_description], errors)
	errors = variable_field('other', limited_type, 'Other Factor', limited_description, errors)

	errors = variable_fields('level', 'Limited by Level', limited_type, [limited_level], errors)
	errors = variable_field('level', limited_type, 'Level', limited_level, errors)


	errors = check_of(others, 'Affects Others', [others_carry, others_touch], errors)

	errors = check_fields(reflect, 'Reflect', [reflect_check, reflect_trait_type, reflect_trait, reflect_descriptor], errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Check Type', reflect_check, errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Trait Type', reflect_trait_type, errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Trait', reflect_trait, errors)
	errors = check_field(reflect, 'Reflect', 'Reflect Descriptor', reflect_descriptor, errors)

	errors = check_fields(subtle, 'Subtle', [subtle_opponent_trait_type, subtle_opponent_trait, subtle_dc], errors)
	errors = check_field(subtle, 'Subtle', 'Subtle DC', subtle_dc, errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Opponent Trait Type', subtle_opponent_trait_type, errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Opponent Trait', subtle_opponent_trait, errors)

	errors = check_fields(points, 'Spend Points', [points_type], errors)
	errors = check_field(points, 'Spend Points', 'Spend Points Type', points_type, errors)
	errors = variable_fields('reroll', 'Re-roll', points_type, [points_reroll_target, points_reroll_cost, points_rerolls], errors)
	errors = variable_field('reroll', points_type, 'Number of Rerolls', points_rerolls, errors)
	errors = variable_field('reroll', points_type, 'Re-roll Cost', points_reroll_cost, errors)
	errors = variable_field('reroll', points_type, 'Re-roll Target', points_reroll_target, errors)
	
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
	
	errors = check_fields(effortless, 'Effortless', [effortless_degree], errors)
	errors = check_field(effortless, 'Effortless', 'Degree of Failure', effortless_degree, errors)



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

	errors = id_check(PowerCirc, circ)
	errors = id_check(PowerDamage, damage)
	errors = id_check(PowerDC, dc)
	errors = id_check(PowerDegree, degree)

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
	ranks = data['ranks']
	cost = data['cost']
	power_cost = data['power_cost']
	circ = data['circ']

	errors = id_check(PowerCost, cost)
	errors = id_check(PowerRanks, ranks)
	errors = id_check(PowerCheck, skill)
	errors = id_check(PowerTimeType, time_type)
	errors = id_check(PowerTime, time_value)
	errors = id_check(PowerCircType, circ)
	
	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Skill, skill, 'skill', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	errors = id_check(Skill, time_skill, 'skill', errors)
	errors = id_check(Unit, distance_unit, 'unit', errors)

	errors = int_check(sense_cost, 'Sense Cost', errors)
	errors = int_check(subsense_cost, 'Subsense Cost', errors)
	errors = int_check(resist_circ, 'Resistance Circumstance Modifier', errors)
	errors = int_check(time_value, 'Time', errors)
	errors = int_check(time_factor, 'Time Factor', errors)
	errors = int_check(distance_dc, 'Distance DC', errors)
	errors = int_check(distance_mod, 'Distance Modifier', errors)
	errors = int_check(distance_value, 'Distance', errors)
	errors = int_check(distance_factor, 'Distance Factor', errors)
	
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
	errors = check_field(dark, 'Counters Darkness', 'Darkness Type', lighting, errors)
	errors = check_of(time, 'Time Effect', 'a Time Effect or Time Effect by Group', [time_value, time_type], errors)
	errors = seperate([time_value, time_type], 'the Time Effect', errors)
	errors = check_field(dimensional, 'Dimensional', 'Dimensional Type', dimensional_type, errors)

	return (errors)


def power_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
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
	opposed = data ['opposed']
	condition = data ['condition']
	condition_target = data ['condition_target']
	conditions_target = data ['conditions_target']



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


	errors = id_check(PowerDegreeType, degree, 'Degree', errors)
	errors = id_check(PowerCircType, circ, 'Circumstance', errors)
	errors = id_check(PowerDCType, dc, 'DC', errors)
	errors = id_check(PowerTimeType, time, 'Time Effect', errors)
	errors = id_check(PowerMoveType, move, 'Movement Effect', errors)
	errors = id_check(PowerOpposed, opposed, 'Opponent Check', errors)
	errors = id_check(PowerRangedType, ranged, 'Ranged', errors)

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

	errors = variable_fields('change', 'Trigger', trigger, [condition1, condition2, conditions_target], errors)
	errors = variable_field('change', trigger, 'Starting Condition', condition1, errors)
	errors = variable_field('change', trigger, 'Ending Condition', condition2, errors)
	errors = variable_field('change', trigger, 'Condition Target', conditions_target, errors)
	errors = variable_fields('condition', 'Trigger', trigger, [condition, condition_target], errors)
	errors = variable_field('condition', trigger, 'Condition', condition, errors)
	errors = variable_field('condition', trigger, 'Condition Target', condition_target, errors)
	errors = variable_fields('conflict', 'Trigger', trigger, [conflict], errors)
	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)

	errors = variable_field_linked('2', check_type, opposed, 'Opposed Check', 'Opponent Check', errors)
	errors = variable_field_linked('7', check_type, opposed, 'Comparison Check', 'Opponent Check', errors)

	errors = select_of('1', 'uses a skill check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = select_of('6', 'uses a resistance check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = seperate([dc, dc_value], 'DC or DC by Group', errors)

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


	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

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

	errors = id_check(Environment, environment, 'Environment', errors)
	errors = id_check(Nature, nature, 'Nature', errors)

	errors = id_check(PowerTime, lasts, 'Circumsrance Duration', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)	
	errors = required(mod, 'Circumstance Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = required(circ_target, 'Target', errors)

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


	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)


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


	errors = linked_field(condition1, linked, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)
	errors = linked_field(condition2, linked, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_field(consequence, linked, 'Consequence', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_group_check(PowerDC, 'other', target, 'other', 'target', power_id, 'power_id', 'a degree of success or failure for another character', 'DC', 'the target field to Other Character', errors)

	return (errors)

def power_move_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	speed = data['speed']
	speed_rank = data['speed_rank']
	speed_rank_mod = data['speed_rank_mod']
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
	objects_check = data['objects_check']
	objects_direction = data['objects_direction']
	objects_damage = data['object_damage']
	object_damage = data['object_damage']
	permeate_type = data['permeate_type']
	permeate_speed = data['permeate_speed']
	permeate_cover = data['permeate_cover']
	equip_type = data['equip_type']
	equipment = data['equipment']
	concealment_sense = data['concealment_sense']
	conceal_opposed = data['conceal_opposed']
	extended_actions = data['extended_actions']
	mass_value = data['mass_value']


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

	errors = id_multiple(Condition, flight_conditions, 'Condition', errors)
	
	errors = id_check(EquipType, flight_equip_type, 'Equipment Type', errors)
	errors = id_check(Equipment, flight_equipment, 'Equipment', errors)
	errors = id_check(Ground, ground_type, 'Ground Type', errors)
	errors = id_check(PowerDes, dimension_descriptor, 'Dimension Descriptor', errors)
	errors = id_check(Condition, condition, 'Condition', errors)
	errors = id_check(EquipType, equip_type, 'Equipment Type', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)
	errors = id_check(Sense, concealment_sense, 'Sense', errors)

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = required(direction, 'Direction', errors)

	errors = of([speed, distance], 'You must set the effect speed or distance', errors)

	errors = variable_fields('rank', 'Speed Rank', speed, [speed_rank], errors)
	errors = variable_field('rank', speed, 'Rank', speed_rank, errors)

	errors = variable_fields('rank_mod', 'Speed Rank Modifier', speed, [speed_rank_mod], errors)
	
	errors = variable_fields('mod', 'Speed Modifier', speed, [speed_trait, speed_math1, speed_value1], errors)
	errors = variable_field('mod', speed, 'Trait', speed_trait, errors)
	errors = variable_field('mod', speed, 'First Math', speed_math1, errors)
	errors = variable_field('mod', speed, 'First Modifier', speed_value1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [speed_value2, speed_math2], errors)

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

	errors = check_fields(objects, 'Move Objects', [objects_check, objects_direction], errors)
	errors = check_field(objects, 'Move Objects', 'Move Objects Check', objects_check, errors)
	errors = check_field(objects, 'Move Objects', 'Move Objects Direction', objects_direction, errors)
	errors = check_fields(objects_damage, 'Move Objects Damage', [object_damage], errors)
	errors = check_field(objects_damage, 'Move Objects Damage', 'Damage', object_damage, errors)

	errors = check_fields(permeate, 'Permeate', [permeate_type, permeate_speed], errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Type', permeate_type, errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Speed Rank Modifier', permeate_speed, errors)

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



	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(mod, 'Player Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)
	errors = id_check(Check, player_check, 'Player Check', errors)
	errors = id_check(Check, opponent_check, 'Opponent Check', errors)

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

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(attached, 'Attsched', errors)
	errors = required(frequency, 'Frequency', errors)
	errors = required(opponent_trait_type, 'Opponent Check Trait Typr', errors)
	errors = required(opponent_trait, 'Opponent Check Trait', errors)
	errors = required(opponent_check, 'Opponennt Check', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(description, 'Description', errors)

	errors = check_fields(recurring, 'Recurring', [recurring_value], errors)
	errors = check_field(recurring, 'Recurring', 'Recurring Value', recurring_value, errors)

	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC', errors)
	
	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC value', errors)
	errors = select_check('6', player_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', player_check, dc_check, 'Skill Check', 'a DC value', errors)

	errors = check_of(circ_check, 'Circumstance', 'a circums6ance modifier or circumstance group', [circ_value, circ], errors)
	errors = check_of(dc_check, 'DC', ' a dc value or dc group', [dc_player, dc_type, dc], errors)
	errors = check_of(degree_check, 'Degree', 'a degree value or degree group', [degree_value, degree], errors)
	errors = check_of(time_check, 'Time', 'a time effect or time effect group', [time, time_type], errors)
	errors = check_of(recurring, 'Recurring', 'recurring time or time effect group', [recurring_value, recurring_type], errors)
	errors = seperate([recurring_value, recurring_type], 'recurring', errors)

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

	errors = int_check(turns, 'Turns', errors)
	errors = id_check(PowerDegree, degree, 'Degree', errors)
	errors = id_check(PowerCirc, circ, 'Circumstance', errors)
	errors = id_check(PowerDC, dc, 'DC', errors)
	errors = id_check(PowerDegreeType, degree_type, 'Degree Group', errors)
	errors = id_check(PowerCircType, circ_type, 'Circumstance Group', errors)
	errors = id_check(PowerDCType, dc_type, 'DC Group', errors)
	

	errors = required(extra_id, 'Extra or Base Power', errors)
	errors = required(type, 'Time Type', errors)
	errors = required(value_type, 'Type', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('value', 'Time Value', value_type, [value, units], errors)
	errors = variable_field('value', value_type, 'Value', value, errors)
	errors = variable_field('value', value_type, 'Units', units, errors)

	errors = variable_fields('math', 'Time Math', value_type, [trait_type, trait, math, math_value], errors)
	errors = variable_field('math', value_type, 'Trait Type', trait_type, errors)
	errors = variable_field('math', value_type, 'Trait', trait, errors)
	errors = variable_field('math', value_type, 'Math', math, errors)
	errors = variable_field('math', value_type, 'Value', math_value, errors)

	errors = variable_fields('rank', 'Time Measurement', value_type, [rank_math], errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank1, rank1_value], ['first rank', 'first value'], errors)
	errors = variable_field('rank', value_type, 'Math', rank_math, errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank2, rank2_value], ['second rank', 'second value'], errors)

	errors = variable_fields('turns', 'Turns', value_type, [turns], errors)

	errors = variable_fields('time', 'Time Rank', value_type, [time], errors)

	errors = variable_fields('mod', 'Time Rank Modifier', value_type, [mod], errors)

	errors = variable_fields('recover', 'Recovery Time', type, [recovery_target], errors)
	errors = variable_field('recover', type, 'Recovery Target', recovery_target, errors)

	errors = seperate([dc, dc_type], 'DC', errors)
	errors = seperate([circ, circ_type], 'Circumstance', errors)
	errors = seperate([degree, degree_type], 'Degree', errors)

	return (errors)


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

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors =  int_check(ranks, 'Ranks', errors)
	
	errors = required(ranks, 'Ranks', errors)

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

	errors = power_check(power_id, errors)
	errors = id_check(Power, power_id, 'Power', errors)

	errors = int_check(cost, 'Cost', errors)
	errors = int_check(ranks, 'Ranks', errors)

	errors = id_check(inherit, 'Power', errors)

	errors = required(name, 'Name', errors)
	errors = not_required(alternate, cost, 'Cost', errors)
	errors = not_required(alternate, ranks, 'Ranks', errors)
	errors = required(des, 'Description', errors)

	return (errors)
