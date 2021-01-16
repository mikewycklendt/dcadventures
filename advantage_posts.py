from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait

def adv_benefit_post(entry, body, cells):

	advantage_id = entry.advantage_id
	name = entry.name
	description = entry.description
	effort = entry.effort

	cells = cell('Name', 25, [name])
	cells = cell('Description', 55, [description], cells)
	cells = check_cell('Extra Effort', 15, effort, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_alt_check_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	check_trigger = entry.check_trigger
	check_type = entry.check_type
	mod = entry.mod
	circumstance = entry.circumstance
	trigger = entry.trigger
	when = entry.when
	trait_type = entry.trait_type
	trait = entry.trait
	conflict = entry.conflict
	conflict_range = entry.conflict_range
	conflict_weapon = entry.conflict_weapon
	condition1 = entry.condition1
	condition2 = entry.condition2
	action_type = entry.action_type
	action = entry.action
	free = entry.free

	trait = variable_trait(trait)


	mod = integer_convert(mod)
	action = action_convert(action_type, action)

	benefit = name(Benefit, benefit)
	check_type = name(Check, check_type)
	conflict = name(ConflictAction, conflict)
	conflict_range = name(Ranged, conflict_range)

	check_trigger_select = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_type_select)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Check Type', 15, [check_type], cells)
	cells = cell('Modifier', 10, [mod], cells)

	vcells = vcell('condition', 30, [condition1, 'to', condition2]) 
	vcells = vcell('conflict', 30, ['Action: ', conflict, 'Range: ', conflict_range], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	conflict_weapon = variable_value('conflict', trigger, conflict_weapon)

	cells = check_cell('Weapon', 8, conflict_weapon, cells)
	cells = cell('Trait', 20, [trait], cells)
	cells = cell('Action', 17, [action], cells)
	cells = cell('When', 10, [when], cells)
	cells = check_cell('Free Check', 12, [free], cells)
	cells = cell('Circumstance', 35, [circumstance], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_circ_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	mod = entry.mod
	rounds = entry.rounds
	circumstance = entry.circumstance
	circ_type = entry.circ_type
	circ_range = entry.circ_range
	conflict = entry.conflict
	check_who = entry.check_who
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_trait = variable_trait(check_trait)
	null_type = entry.null_type
	null_condition = entry.null_condition
	null_trait_type = entry.null_trait_type
	null_trait = entry.null_trait
	null_trait = variable_trait(null_trait)
	null_override_trait_type = entry.null_override_trait_type
	null_override_trait = entry.null_override_trait
	null_override_trait = variable_trait(null_override_trait)

	mod = integer_convert(mod)
	rounds = integer_convert(rounds)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	circ_type_select = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]
	circ_type = selects(circ_type, circ_type_select)

	who_check_select = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]
	who = selects(who, who_check_select)

	circ_null_select = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'condition', 'name': 'From Condition'}, {'type': 'override', 'name': 'Override Trait Circumstance'}]
	null_type = selects(null_type, circ_null_select)

	benefit = name(Benefit, benefit)
	circ_range = name(Range, circ_range)
	conflict = name(ConflictAction, conflict)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Target', 18, [target], cells)
	cells = cell('Modifier', 10, [mod], cells)
	cells = cell('Lasts', 8, [rounds], cells)

	circrange = string('Range', [circ_range])
	vcells = vcell('range', 20, [circ_range, circrange])
	vcells = vcell('check', 25, [check_who, check_trait], vcells)
	cells = vcell_add('Trigger', circ_type, vcells, cells)

	vcells = vcell('trait', 17, [null_trait])
	vcells = vcell('override', 19, [null_override_trait], vcells)
	vcells = vcell('condition', 17, [null_condition], vcells)	
	cells = vcell_add('Nullified', null_type, vcells, cells)

	cells = cell('Circumstance', 35, [description], cells)


	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_combined_post(entry, body, cells):

	advantage_id = entry.advantage_id
	ranks = entry.ranks
	advantage = entry.advantage

	ranks = integer_convert(ranks)

	cells = cell('Advantage', 35, [advantage])
	cells = cell('Ranks', 10, [ranks], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_condition_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	condition_type = entry.condition_type
	condition = entry.condition
	condition_null = entry.condition_null
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage_value = entry.damage_value
	damage = entry.damage

	updown_select = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]
	damage = selects(damage, updown_select)

	damage_value = integer_convert(damage_value)

	benefit = name(Benefit, benefit)

	cells = cell('Benefit', 20, [benefit])

	vcells = vcell('active', 40, [condition, 'Active'])
	vcells = vcell('change', 60, [condition1, 'to', condition2], vcells)
	vcells = vcell('damage', 40, [damage_value, 'Condition', damage], vcells)
	vcells = vcell('null', 40, [condition_null, 'Nullified'], vcells)
	cells = vcell_add('Condition Effect', condition_type, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_dc_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	dc = entry.dc
	description = entry.description
	value_value = entry.value_value
	math_value = entry.math_value
	math_math = entry.math_math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
	math_trait = variable_trait(math_trait)
	condition = entry.condition
	keyword_check = entry.keyword_check
	check_type = entry.check_type
	levels = entry.levels
	level_type = entry.level_type
	level = entry.level
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_trait = variable_trait(check_trait)
	check_mod = entry.check_mod

	
	dc = integer_convert(dc)
	value_value = integer_convert(value_value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

	benefit = name(Benefit, benefit)
	math_math = math_convert(Math, math_math)
	level_type = name(LevelType, level_type)
	level = name(Levels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Target', 18, [target], cells)
	vcells = vcell('value', 10, [value_value])
	vcells = vcell('math', 20, [math_value, math_math, math_trait], vcells)
	cells = vcell_add('DC', dc, vcells, cells)

	cells = check_cell('Condition', 13, condition, cells, True)
	new_mod = mod_create('Condition', 12)
	word = string('to', [condition1, condition2])
	new_mod = mod_cell('Conditions', 14, [condition1, word, condition2], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Keyword', 15, keyword_check, cells, True)
	new_mod = mod_create('Keyword', 10)
	new_mod = mod_cell('Key:', 7, [keyword], new_mod)
	body = mod_add(keyword_check, new_mod, body)

	cells = check_cell('Check', 12, check_type, cells, True)
	new_mod = mod_create('Check Type', 15)
	new_mod = mod_cell('Trait:', 7, [check_trait], new_mod)
	new_mod = mod_cell('Modifier:', 12, [check_mod], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Level', 12, levels, cells, True)
	new_mod = mod_create('Level', 8)
	new_mod = mod_cell('Level:', 7, [level], new_mod)
	body = mod_add(levels, new_mod, body)

	cells = cell('Description', 40, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def adv_deg_mod_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	value = entry.value
	deg_mod_type = entry.deg_mod_type
	consequence_action_type = entry.consequence_action_type
	consequence_action = entry.consequence_action
	consequence_trait_type = entry.consequence_trait_type
	consequence_trait = entry.consequence_trait
	consequence_trait = variable_trait(consequence_trait)
	consequence = entry.consequence
	knowledge = entry.knowledge
	knowledge_count = entry.knowledge_count
	knowledge_specificity = entry.knowledge_specificity
	level_type = entry.level_type
	level = entry.level
	circ_value = entry.circ_value
	circ_turns = entry.circ_turns
	circ_trait_type = entry.circ_trait_type
	circ_trait = entry.circ_trait
	circ_trait = variable_trait(circ_trait)
	measure_type = entry.measure_type
	measure_val1 = entry.measure_val1
	measure_math = entry.measure_math
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_trait = variable_trait(measure_trait)
	measure_value = entry.measure_value
	measure_rank = entry.measure_rank
	condition_type = entry.condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	nullify = entry.nullify
	cumulative = entry.cumulative
	linked = entry.linked

	value = integer_convert(value)
	consequence_action = action_convert(consequence_action_type, consequence_action)
	knowledge_count = integer_convert(knowledge_count)
	circ_value = integer_convert(circ_value)
	circ_turns = integer_convert(circ_turns)
	measure_val1 = integer_convert(measure_val1)
	measure_value = integer_convert(measure_value)
	condition_damage_value = integer_convert(condition_damage_value)
	condition_damage = integer_convert(condition_damage)
	nullify = integer_convert(nullify)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	knowledge_select = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]
	knowledge = selects(knowledge, knowledge_select)

	specificity_select = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	knowledge_specificity = selects(knowledge_specificity, specificity_select)

	updown_select = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown_select)

	condition_select = [{'type': 'current', 'name': 'Current'}, {'type': 'any', 'name': 'Any'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, condition_select)
	condition2 = selects(condition2, condition_select)

	benefit = name(Benefit, benefit)
	consequence = name(Consequence, consequence)
	level_type = name(LevelType, level_type)
	level = name(Levels, level)
	measure_math = math_convert(Math, measure_math)
	measure_rank = name(Rank, measure_rank)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Target', 18, [target], cells)
	cells = cell('Degree',10, [value], cells)
	cells = cell('Keyword', 18, [keyword], cells)
	cells = cell('Nullify DC', 14, [value], cells)
	cells = check_cell('Cumulative', 15, cumulative, cells)
	cells = check_cell('Linked', 9, linked, cells)
	word = string('for', [circ_trait, circ_value, circ_turns])
	word2 = string('Turns', [circ_trait, circ_value, circ_turns])
	vcells = vcell('circ', 30, [circ_trait, circ_value, word, circ_turns, word2]) 
	vcells = vcell('uncontrolled', 16, ['Uncontrolled'], vcells)
	vcells = vcell('level', 16, [level], vcells)
	vcells = vcell('measure', 22, [measure_value, measure_rank], vcells, 'value', measure_type)
	vcells = vcell('measure', 26, [measure_val1, measure_math, measure_trait], vcells, 'math', measure_type)
	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 32, [condition1, word, condition2], vcells, 'condition', deg_condition_type)
	word = string('Conditions', [condition_damage_value, condition_damage])
	vcells = vcell('condition', 20, [condition_damage_value, word, condition_damage], vcells, 'damage', deg_condition_type)
	vcells = vcell('knowledge', 28, [knowledge_count, knowledge_specificity, 'Bonuses'], vcells, 'bonus', knowledge)
	vcells = vcell('knowledge', 25, ['Gain Knowledge but GM may lie'], vcells, 'lie', knowledge)
	vcells = vcell('consequence', 33, [consequence, 'for', consequence_trait, consequence_action], vcells)
	
	vcell_add('Effect', deg_type, vcells, cells)
	





	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_effort_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	effect = entry.effect
	condition_type = entry.condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	benefit_choice = entry.benefit_choice
	benefit_turns = entry.benefit_turns
	benefit_count = entry.benefit_count
	benefit_effort = entry.benefit_effort

	condition_damage_value = integer_convert(condition_damage_value)
	condition_damage = integer_convert(condition_damage)
	benefit_turns = integer_convert(benefit_turns)
	benefit_count = integer_convert(benefit_count)
	
	condition_select = [{'type': 'current', 'name': 'Current'}, {'type': 'any', 'name': 'Any'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, condition_select)
	condition2 = selects(condition2, condition_select)	
	updown_select = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown_select)

	benefit = name(Benefit, benefit)
	benefit_choice = name(Benefit, benefit_choice, 'Variable Benefit')

	cells = cell('Benefit', 20, [benefit])
	vcells = vcell('condition', 35, [condition1, 'tO', condition2])
	vcells = vcell('damage', 23, [condition_damage_value, 'Conditions', condition_damage], vcells)
	cells = vcell_add('Condition Effect', condition_type, vcells, cells)
	cells = cell('Benefits', 8, [benefit_count], cells)
	cells = cell('Benefit Gained', 23, [benefit_choice], cells)
	cells = cell('Turns', 7, [benefit_turns], cells)
	cells = check_cell('Only Extra Effort', 15, benefit_effort, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)



def adv_minion_post(entry, body, cells):

	advantage_id = entry.advantage_id
	points = entry.points
	condition = entry.condition
	player_condition = entry.player_condition
	link = entry.link
	variable_type = entry.variable_type
	multiple = entry.multiple
	attitude = entry.attitude
	resitable = entry.resitable
	heroic = entry.heroic
	sacrifice = entry.sacrifice
	sacrifice_cost = entry.sacrifice_cost
	attitude_type = entry.attitude_type
	attitude_attitude = entry.attitude_attitude
	attitude_trait_type = entry.attitude_trait_type
	attitude_trait = entry.attitude_trait
	attitude_trait = variable_trait(attitude_trait)
	resitable_check = entry.resitable_check
	resitable_dc = entry.resitable_dc
	multiple_value = entry.multiple_value
	horde = entry.horde

	points = integer_convert(points)
	sacrifice_cost = integer_convert(sacrifice_cost)
	resitable_dc = integer_convert(resitable_dc)
	multiple_value = integer_convert(multiple_value)

	minion_type_select = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]
	variable_type = selects(variable_type, minion_type_select)
	
	attitude_type = name(LevelType, attitude_type)
	attitude_attitude = name(Levels, attitude_attitude)
	resitable_check = name(Defense, resitable_check)

	cells = cell('Points', 19, [points])
	cells = cell('Minion Condition', 20, [condition], cells)
	cells = cell('Player Condition', 20, [player_condition], cells)
	cells = cell('Type', 15, [variable_type], cells)
	cells = check_cell('Link', 7, link, cells)
	cells = check_cell('Multiple', 12, multiple, cells, True)
	new_mod = mod_create('Multiple Minions', 20)
	new_mod  = mod_cell('Count', 7, [multiple_value], new_mod)
	new_mod  = mod_cell('Horde', 7, [horde], new_mod)
	body = mod_add(multiple, new_mod, body)
	
	cells = check_cell('Attitide', 12, attitude, cells, True)
	new_mod = mod_create('Attitude', 11)
	new_mod  = mod_cell('Level', 7, [attitude_attitude], new_mod)
	new_mod  = mod_cell('Trait to Control', 18, [attitude_trait], new_mod)
	body = mod_add(attitude, new_mod, body)
	
	cells = check_cell('Resistable', 12, resitable, cells, True)
	new_mod = mod_create('Resistable', 11)
	new_mod  = mod_cell('Defense', 9, [resitable_check], new_mod)
	new_mod  = mod_cell('DC', 4, [resitable_dc], new_mod)
	body = mod_add(resitable, new_mod, body)
	
	cells = check_cell('Heroic', 19, heroic, cells)
	cells = check_cell('Sacrifice', 13, sacrifice, cells, True)
	new_mod = mod_create('Sacrifice', 11)
	new_mod  = mod_cell('Cost', 6, [sacrifice_cost], new_mod)
	body = mod_add(sacrifice, new_mod, body)
	body = send(cells, body)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_modifiers_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	bonus = entry.bonus
	bonus_type = entry.bonus_type
	penalty = entry.penalty
	penalty_type = entry.penalty_type
	trigger = entry.trigger
	bonus_effect = entry.bonus_effect
	penalty_effect = entry.penalty_effect
	environment = entry.environment
	environment_other = entry.environment_other
	sense = entry.sense
	mod_range = entry.mod_range
	subsense = entry.subsense
	cover = entry.cover
	conceal = entry.conceal
	maneuver = entry.maneuver
	weapon_melee = entry.weapon_melee
	weapon_ranged = entry.weapon_ranged
	tools = entry.tools
	condition = entry.condition
	power = entry.power
	consequence = entry.consequence
	creature = entry.creature
	creature_other = entry.creature_other
	emotion = entry.emotion
	emotion_other = entry.emotion_other
	conflict = entry.conflict
	profession = entry.profession
	profession_other = entry.profession_other
	bonus_trait_type = entry.bonus_trait_type
	bonus_trait = entry.bonus_trait
	bonus_trait = variable_trait(bonus_trait)
	bonus_check = entry.bonus_check
	bonus_check_range = entry.bonus_check_range
	bonus_conflict = entry.bonus_conflict
	penalty_trait_type = entry.penalty_trait_type
	penalty_trait = entry.penalty_trait
	penalty_trait = variable_trait(penalty_trait)
	penalty_check = entry.penalty_check
	penalty_check_range = entry.penalty_check_range
	penalty_conflict = entry.penalty_conflict
	bonus_active_defense = entry.bonus_active_defense
	bonus_conflict_defend = entry.bonus_conflict_defend
	penalty_active_defense = entry.penalty_active_defense
	penalty_conflict_defend = entry.penalty_conflict_defend
	multiple = entry.multiple
	multiple_count = entry.multiple_count
	lasts = entry.lasts

	bonus = integer_convert(bonus)
	penalty = integer_convert(penalty)
	multiple_count = integer_convert(multiple_count)
	lasts = integer_convert(lasts)

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	bonus_type = selects(bonus_type, modifier_type)
	penalty_type = selects(penalty_type, modifier_type)

	multiple_select = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]
	multiple = selects(multiple, multiple_select)

	benefit = name(Benefit, benefit)
	environment = name(Environment, environment, 'Variable Environment')
	sense = name(Sense, sense, 'Variable ')
	mod_range = name(Ranged, mod_range, 'Variable ')
	subsense = name(SubSense, subsense, 'Variable Subssense')
	cover = name(Cover, cover, 'Variable Cover')
	conceal = name(Conceal, conceal, 'Variable Concealment')
	maneuver = name(Maneuver, maneuver, 'Variable Maneuver')
	weapon_melee = name(WeaponType, weapon_melee, 'Variable Melee Weapon')
	weapon_ranged = name(WeaponType, weapon_ranged, 'Variable Ranged Weapon')
	consequence = name(Consequence, consequence, 'Variable Consequence')
	creature = name(Creature, creature, 'Variable Creature')
	emotion = name(Emotion, emotion, 'Variable Emotion')
	conflict = name(ConflictAction, conflict, 'Variable Conflict Action')
	profession = name(Job, profession, 'Variable Profession')
	bonus_check = name(Check, bonus_check,)
	bonus_check_range = name(Ranged, bonus_check_range)
	bonus_conflict = name(ConflictAction, bonus_conflict, 'Variable Conflict Action')
	penalty_check = name(Check, penalty_check)
	penalty_check_range = name(Ranged, penalty_check_range)
	penalty_conflict = name(ConflictAction, penalty_conflict, 'Variable Conflict Action')

	bonus_active_defense = variable_value('trait', bonus_effect, bonus_active_defense)
	bonus_conflict_defend = variable_value('conflict', bonus_effect, bonus_conflict_defend)
	penalty_active_defense = variable_value('trait', penalty_effect, penalty_active_defense)
	penalty_conflict_defend = variable_value('conflict', penalty_effect, penalty_conflict_defend)

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Bonus', 12, [bonus], cells)
	cells = cell('Type', 8, [bonus_type], cells)
	vcells = vcell('effect', 15, ['Effect Modifier'])
	vcells = vcell('attack', 12, ['Attack Bonus'], vcells)
	vcells = vcell('damage', 13, ['Damage Bonus'], vcells)
	vcells = vcell('defense', 16, ['Active Defenses'], vcells)
	vcells = vcell('trait', 18, [bonus_trait], vcells)
	word = string(', Range:', [bonus_check_range])
	vcells = vcell('check', 29, [bonus_check, word, bonus_check_range], vcells)
	vcells = vcell('conflict', 16, [bonus_conflict], vcells)
	cells = vcell_add('Bonus Effect', bonus_effect, vcells, cells)

	cells = check_cell('Active', 8, bonus_active_defense, cells)
	cells = check_cell('Only Active', 11, bonus_conflict_defend, cells)
	
	cells = cell('Penalty', 12, [penalty], cells)
	cells = cell('Type', 8, [penalty_type], cells)
	
	vcells = vcell('effect', 15, ['Effect Modifier'])
	vcells = vcell('attack', 12, ['Attack Bonus'], vcells)
	vcells = vcell('damage', 13, ['Damage Bonus'], vcells)
	vcells = vcell('defense', 16, ['Active Defenses'], vcells)
	vcells = vcell('trait', 18, [penalty_trait], vcells)
	word = string(', Range:', [penalty_check_range])
	vcells = vcell('check', 29, [penalty_check, word, penalty_check_range], vcells)
	vcells = vcell('conflict', 16, [penalty_conflict], vcells)
	
	cells = vcell_add('Affects', penalty_effect, vcells, cells)

	cells = check_cell('Active', 8, penalty_active_defense, cells)
	cells = check_cell('Only Active', 11, penalty_conflict_defend, cells)
	
	vcells = vcell('environment', 20, [environment])
	vcells = vcell('cover', 20, [cover], vcells)
	vcells = vcell('conceal', 20, [conceal], vcells)
	vcells = vcell('sense', 20, [sense], vcells)
	vcells = vcell('subsense', 20, [subsense], vcells)
	vcells = vcell('condition', 20, [condition], vcells)
	vcells = vcell('profession', 20, [profession], vcells)
	vcells = vcell('creature', 20, [creature], vcells)
	vcells = vcell('power', 20, [power], vcells)
	vcells = vcell('emotion', 20, [emotion], vcells)
	vcells = vcell('consequence', 20, [consequence], vcells)
	vcells = vcell('range', 20, [mod_range], vcells)
	vcells = vcell('critical', 20, ['Critical Attempt'], vcells)
	vcells = vcell('conflict', 20, [conflict], vcells)
	vcells = vcell('maneuver', 20, [maneuver], vcells)
	vcells = vcell('tools', 20, [tools], vcells)
	vcells = vcell('ranged', 20, [weapon_ranged], vcells)
	vcells = vcell('melee', 20, [weapon_melee], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_opposed_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_trait = variable_trait(opponent_trait)
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check
	multiple = entry.multiple

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]
	multiple = selects(multiple, multiple_opposed)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)

	benefit = name(Benefit, benefit)
	player_check = name(Check, player_check)
	opponent_check = name(Check, opponent_check)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Player Trait', 18, [trait], cells)
	cells = cell('Player Check', 15, [player_check], cells)
	cells = cell('Modifier', 9, [mod], cells)
	cells = cell('Opponent Trait', 18, [opponent_trait], cells)
	cells = cell('Opponent Check', 15, [opponent_check], cells)
	cells = cell('Modifier', 9, [opponent_mod], cells)
	cells = cell('Multiple', 12, [multiple], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_points_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	spend = entry.spend
	condition_cost = entry.condition_cost
	condition1 = entry.conditioon1
	condition2 = entry.condition2
	equipment_points = entry.equipment_points
	equipment_vehicles = entry.equipment_vehicles
	equipment_headquarters = entry.equipment_headquarters
	initiative_cost = entry.initiative_cost
	twenty = entry.twenty
	check_bonus = entry.check_bonus
	check_cost = entry.check_cost
	check_turns = entry.check_turns
	check_target = entry.check_target
	check_all = entry.check_all
	benefit_choice = entry.benefit_choice
	benefit_count = entry.benefit_count
	benefit_cost = entry.benefit_cost
	benefit_turns = entry.benefit_turns
	ranks_gained = entry.ranks_gained
	ranks_max = entry.ranks_max
	ranks_lasts = entry.ranks_lasts
	ranks_trait_type = entry.ranks_trait_type
	ranks_trait = entry.ranks_trait
	ranks_trait = variable_trait(ranks_trait)

	


	condition_cost = integer_convert(condition_cost)
	equipment_points = integer_convert(equipment_points)
	initiative_cost = integer_convert(initiative_cost)
	twenty = integer_convert(twenty)
	check_bonus = integer_convert(check_bonus)
	check_cost = integer_convert(check_cost)
	check_turns = integer_convert(check_turns)
	benefit_count = integer_convert(benefit_count)
	benefit_cost = integer_convert(benefit_cost)
	benefit_turns = integer_convert(benefit_turns)
	ranks_gained = integer_convert(ranks_gained)
	ranks_max = integer_convert(ranks_max)
	ranks_lasts = integer_convert(ranks_lasts)

	check_bonus = add_plus(check_bonus)

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	check_target = selects(check_target, targets)

	benefit = name(Benefit, benefit)
	benefit_choice = name(Benefit, benefit_choice, 'Variable Benefit')

	cells = cell('Benefit', 20, [benefit])
	word = string('Max Existing:', ranks_max)
	vcells = vcell('ranks', 65, ['Gain', ranks_gained, 'of', ranks_trait, 'for', ranks_lasts, word, ranks_max])
	vcells = vcell('benefit', 55, ['Gain', benefit_choice, 'for', benefit_turns, 'for', benefit_cost, 'Points'], vcells)
	vcells = vcell('check', 65, [check_bonus, 'on', check_target, 'for', check_turns, 'for', check_cost], vcells)
	vcells = vcell('equip', 55, [equipment_points, 'of Equipment Per Rank'], vcells)
	vcells = vcell('condition', 65, [condition1, 'to', condition2, 'for', condition_cost, 'Points'], vcells)
	vcells = vcell('initiative', 35 ['Gain Initiative for', initiative_cost, 'Points'], vcells)
	vcells = vcell('20', 30 ['Automatic 20', 'for', twenty, 'Points'], vcells)
	cells = vcell_add('Effect', spend, vcells, cells)

	check_all = variable_value('check', spend, check_all)
	cells = check_cell('All Checks', 12, check_all, cells)
	equipment_vehicles = variable_value('equip', spend, equipment_vehicles)
	cells = check_cell('Vehicles', 12, equipment_vehicles, cells)
	equipment_headquarters = variable_value('equip', spend, equipment_headquarters)
	cells = check_cell('Headquarters', 15, equipment_headquarters, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_resist_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	mod = entry.mod
	which = entry.which

	mod = integer_convert(mod)

	benefit = name(Benefit, benefit)

	which_select = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Value'}, {'type': 'low', 'name': 'Lower Value'}]
	which = selects(which, which_select)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Resisted By', 30, [trait], cells)
	cells = cell('Modifier', 12, [mod], cells)
	cells = cell('If Kultiple', 20, [which], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_rounds_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	rounds = entry.rounds
	cost = entry.cost
	check = entry.check
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	end = entry.end

	rounds = integer_convert(rounds)

	benefit = name(Benefit, benefit)
	cost = name(Action, cost)
	check = name(Check, check)

	rounds_end = [{'type': '', 'name': 'Ends'}, {'type': 'action', 'name': 'Stop Taking Action'}, {'type': 'resist', 'name': 'Successful Resistance'}, {'type': 'danger', 'name': 'Danger'}]
	end = select(end, rounds_end)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Turns', 12, [rounds], cells)
	cells = cell('Action', 22, [cost], cells)
	cells = cell('Check', 22, [check], cells)
	cells = cell('Trait', 22, [trait], cells)
	cells = cell('Ends', 22, [end], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_skill_post(entry, body, cells):


	advantage_id = entry.advantage_id
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	replaced_trait_type = entry.replaced_trait_type
	replaced_trait = entry.replaced_trait
	replaced_trait = variable_trait(replaced_trait)
	multiple = entry.multiple

	benefit = name(Benefit, benefit)\

	multiple_select = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]
	multiple = selects(multiple, multiple_select)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Replace', 25, [replaced_trait], cells)
	cells = cell('Replace With', 25, [trait], cells)
	cells = cell('If Multiple', 20, [multiple], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_time_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	time_type = entry.time_type
	value_type = entry.value_type
	value = entry.value
	units = entry.units
	time_value = entry.time_value
	math = entry.math
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	dc = entry.dc
	check_type = entry.check_type
	recovery = entry.recovery
	recovery_penalty = entry.recovery_penalty
	recovery_time = entry.recovery_time
	recovery_incurable = entry.recovery_incurable


	value = integer_convert(value)
	time_value = integer_convert(time_value)
	dc = integer_convert(dc)
	recovery_penalty = integer_convert(recovery_penalty)
	recovery_time = integer_convert(recovery_time)

	benefit = name(Benefit, benefit)
	units = name(Unit, units)
	math = math_convert(Math, math)
	check_type = name(Check, check_type)

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]
	time_type = selects(time_type, time_effect)

	cells = cell('Benefit', 20, [benefit])
	cells = cell('Type', 22, [time_type], cells)
	vcells = vcell('value', 14, [value, units])
	word = string('= Time Rank', [time_value, math, trait])
	vcells = vcell('math', 26, [time_value, math, trait, word], vcells)
	vcell_add('Time', value_type, vcells, cells)
	cells = cell('DC', 7, [dc], cells)
	cells = cell('Check', 18, [check_type], cells)

	cells = check_cell('Recovery', 10, recovery, cells, True)
	new_mod = mod_create('Recovery Time', 18)
	word = string('Every', [recovery_penalty, recovery_time])
	word2 = string('Time Rank', [recovery_penalty, recovery_time])
	new_mod = mod_cell('Toughness Penalty Nullified', 27, [recovery_penalty, word, recovery_time, word2], new_mod)
	new_mod = mod_cell('Includes Incurable', 16, [recovery_incurable], new_mod)
	body = mod_add(recovery, new_mod, body)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def adv_variable_post(entry, body, cells):

	advantage_id = entry.advantage_id
	trait_type = entry.trait_type
	trait = entry.trait
	trait = variable_trait(trait)
	active = entry.active
	effort = entry.effort

	cells = cell('Trait', 40, [trait])
	cells = check_cell('Only Active', 13, active, cells)
	cells = check_cell('Only Extra Effort', 22, effort, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

