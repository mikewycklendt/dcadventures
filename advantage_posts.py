from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, name_variable, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add. vcell, check_cell, cell, mod_create, mod_cell, mod_add

def adv_benefit_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	name = entry.name
	description = entry.description
	effort = entry.effort

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_alt_check_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
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


	mod = integer_convert(mod)
	action = action_convert(action_type, action)

	benefit = name(Benefit, benefit)
	check_type = name(Check, check_type)
	conflict = name(ConflictAction, conflict)
	conflict_range = name(Ranged, conflict_range)

	check_trigger_select = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]
	trigger = selects(check_trigger, check_trigger_select)

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_type_select)





	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_circ_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	target = entry.target
	benefit = entry.benefit
	mod = entry.mod
	rounds = entry.rounds
	ranks = entry.ranks
	circumstance = entry.circumstance
	circ_type = entry.circ_type
	circ_range = entry.circ_range
	conflict = entry.conflict
	check_who = entry.check_who
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	null_type = entry.null_type
	null_condition = entry.null_condition
	null_trait_type = entry.null_trait_type
	null_trait = entry.null_trait

	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	ranks = integer_convert(ranks)

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


	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_combined_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	ranks = entry.ranks
	advantage = entry.advantage

	ranks = integer_convert(ranks)



	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_condition_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	Created = entry.created
	font = entry.font
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

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_dc_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	target = entry.target
	benefit = entry.benefit
	dc = entry.dc
	description = entry.description
	value_value = entry.value_value
	math_value = entry.math_value
	math_math = entry.math_math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
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
	check_mod = entry.check_mod

	
	dc = integer_convert(dc)
	value_value = integer_convert(value_value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

	benefit = name(Benefit, benefit)
	math_math = name(Math, math_math)
	level_type = name(LevelType, level_type)
	level = name(Levels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)



	body = send(cells, body)

	cells.clear()

	return (body)
`

def adv_deg_mod_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	Created = entry.created
	font = entry.font
	target = entry.target
	benefit = entry.benefit
	value = entry.value
	deg_mod_type = entry.deg_mod_type
	consequence_action_type = entry.consequence_action_type
	consequence_action = entry.consequence_action
	consequence_trait_type = entry.consequence_trait_type
	consequence_trait = entry.consequence_trait
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
	measure_type = entry.measure_type
	measure_val1 = entry.measure_val1
	measure_math = entry.measure_math
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
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
	measure_math = name(Math, measure_math)
	measure_rank = name(Rank, measure_rank)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_effort_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns= entry.columns
	created = entry.created
	font = entry.font
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

	benefit = name(Benefit, benefit)
	benefit_choice = name(Benefit, benefit_choice)


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
	resitable_check = entry.resitable_check
	resitable_dc = entry.resitable_dc
	multiple_value = entry.multiple_value
	horde = entry.horde
	columns = entry.columns
	created = entry.created
	font = entry.font

	points = integer_convert(points)
	sacrifice_cost = integer_convert(sacrifice_cost)
	resitable_dc = integer_convert(resitable_dc)
	multiple_value = integer_convert(multiple_value)

	
	attitude_type = name(, )
	attitude_attitude = name(, )
	resitable_check = name(, )


	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_modifiers_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	Benefit = entry.benefit
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
	bonus_check = entry.bonus_check
	bonus_check_range = entry.bonus_check_range
	bonus_conflict = entry.bonus_conflict
	penalty_trait_type = entry.penalty_trait_type
	penalty_trait = entry.penalty_trait
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

	environment = name(, , '')
	sense = name(, , '')
	mod_range = name(, , '')
	subsense = name(, , '')
	cover = name(, , '')
	conceal = name(, , '')
	maneuver = name(, , '')
	weapon_melee = name(, , '')
	weapon_ranged = name(, , '')
	consequence = name(, , '')
	creature = name(, , '')
	emotion = name(, , '')
	conflict = name(, , '')
	profession = name(, , '')
	bonus_check = name(, , '')
	bonus_check_range = name(, , '')
	bonus_conflict = name(, , '')
	penalty_check = name(, , '')
	penalty_check_range = name(, , '')
	penalty_conflict = name(, , '')

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_opposed_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check
	multiple = entry.multiple


	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)

	benefit = name(, )
	player_check = name(, )
	opponent_check = name(, )

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_points_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
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

	benefit = name(, )
	benefit_choice = name(, )



	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_resist_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	which = entry.which

	mod = integer_convert(mod)

	benefit = name(, )


	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_rounds_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	benefit = entry.benefit
	rounds = entry.rounds
	cost = entry.cost
	check = entry.check
	trait_type = entry.trait_type
	trait = entry.trait
	end = entry.end

	rounds = integer_convert(rounds)

	benefit = name(, )
	cost = name(, )
	check = name(, )

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_skill_post(entry, body, cells):


	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	replaced_trait_type = entry.replaced_trait_type
	replaced_trait = entry.replaced_trait
	multiple = entry.multiple

	benefit = name(, )

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_time_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	benefit = entry.benefit
	time_type = entry.time_type
	value_type = entry.value_type
	value = entry.value
	units = entry.units
	time_value = entry.time_value
	math = entry.math
	trait_type = entry.trait_type
	trait = entry.trait
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

	benefit = name(, )
	units = name(, )
	math = name(, )
	check_type = name(, )

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_variable_post(entry, body, cells):

	advantage_id = entry.advantage_id
	columns = entry.columns
	created = entry.created
	font = entry.font
	trait_type = entry.trait_type
	trait = entry.trait



	body = send(cells, body)
	
	cells.clear()

	return (body)
``
