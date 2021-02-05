
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
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait, get_name, get_circ




def skill_ability_post(entry, body, cells):

	ability = entry.ability
	circumstance = entry.circumstance

	ability = get_name(Ability, ability)



	body = send(cells, body)

	cells.clear()

	return (body)
	
def skill_check_post(entry, body, cells):

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
	
	
	check_type = get_name(Check, check_type)
	mod = integer_convert(mod)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	action = action_convert(action_type, action)
	

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_type_select)



	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]


	body = send(cells, body)

	cells.clear()

	return (body)
	
def skill_circ_post(entry, body, cells):

	circ_target = entry.circ_target
	mod = entry.mod
	effect = entry.effect
	speed = entry.speed
	temp = entry.temp
	target = entry.target
	level_type = entry.level_type
	level = entry.level
	time = entry.time
	condition_type = entry.condition_type
	condition1 = entry.condition1
	condition2 = entry.condition2
	conditions = entry.conditions
	conditions_effect = entry.conditions_effect
	measure_effect = entry.measure_effect
	measure_rank_value = entry.measure_rank_value
	measure_rank = entry.measure_rank
	unit_value = entry.unit_value
	unit_type = entry.unit_type
	unit = entry.unit
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_trait_math = entry.measure_trait_math
	measure_mod = entry.measure_mod
	keyword = entry.keyword
	cumulative = entry.cumulative
	optional = entry.optional
	lasts = entry.lasts
	turns = entry.turns
	unit_time = entry.unit_time
	time_units = entry.time_units
	time_rank = entry.time_rank
	circumstance = entry.circumstance

	mod = integer_convert(mod)
	speed = integer_convert(speed)
	temp = integer_convert(temp)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	time = integer_convert(time)
	conditions = integer_convert(conditions)	
	measure_rank_value = integer_convert(measure_rank_value)
	measure_rank = get_name(Rank, measure_rank)
	unit_value = integer_convert(unit_value)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert()
	measure_mod = integer_convert(measure_mod)
	turns = integer_convert(turns)
	unit_time = integer_convert(unit_time)
	time_units = get_name(Unit, time_units)
	time_rank = integer_convert(time_rank)


	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	circ_target = selects(circ_target, targets_select)

	circ_targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]
	target = selects(target, circ_targets_select)

	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	conditions_effect = selects(conditions_effect, updown)


	circ_effect_select = [{'type': '', 'name': 'Condition'}, {'type': 'condition', 'name': 'Condition Effect'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'temp', 'name': 'Effect Temporary'}, {'type': 'measure', 'name': 'If Measurement'}, {'type': 'level', 'name': 'If Level'}, {'type': 'speed', 'name': 'If Speed'}, {'type': 'target', 'name': 'If Target'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]

	lasts = [{'type': '', 'name': 'Lasts'}, {'type': 'turns', 'name': 'Turns'}, {'type': 'time', 'name': 'Time'}, {'type': 'rank', 'name': 'Time Rank'}]

	body = send(cells, body)

	cells.clear()

	return (body)
	
def skill_dc_post(entry, body, cells):

	target = entry.target
	dc = entry.dc
	description = entry.description
	value = entry.value
	mod = entry.mod
	math_value = entry.math_value
	math = entry.math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
	condition = entry.condition
	keyword_check = entry.keyword_check
	levels = entry.levels
	damage = entry.damage
	cover = entry.cover
	complex = entry.complex
	measure = entry.measure
	change_action = entry.change_action
	conceal = entry.conceal
	action = entry.action
	action_when = entry.action_when
	damage_type = entry.damage_type
	inflict_type = entry.inflict_type
	inflict_flat = entry.inflict_flat
	inflict_trait_type = entry.inflict_trait_type
	inflict_trait = entry.inflict_trait
	inflict_math = entry.inflict_math
	inflict_mod = entry.inflict_mod
	inflict_bonus = entry.inflict_bonus
	damage_mod = entry.damage_mod
	damage_consequence = entry.damage_consequence
	measure_effect = entry.measure_effect
	measure_rank_value = entry.measure_rank_value
	measure_rank = entry.measure_rank
	unit_value = entry.unit_value
	unit_type = entry.unit_type
	unit = entry.unit
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_trait_math = entry.measure_trait_math
	measure_mod = entry.measure_mod
	level_type = entry.level_type
	level = entry.level
	condition1 = entry.condition1
	condition2 = entry.condition2
	condition_turns = entry.condition_turns
	keyword = entry.keyword
	complexity = entry.complexity

	value = integer_convert(value)
	mod = integer_convert(mod)
	math_value = integer_convert(math_value)
	math = math_convert(math)
	action = get_name(Action, action)
	inflict_flat = integer_convert(inflict_flat)
	inflict_math = math_convert(inflict_math)
	inflict_mod = integer_convert(inflict_mod)
	inflict_bonus = integer_convert(inflict_bonus)
	damage_mod = integer_convert(damage_mod)
	damage_consequence = get_name(Consequence, damage_consequence)
	measure_rank_value = integer_convert(measure_rank_value)
	measure_rank = get_name(Rank, measure_rank)
	unit_value = integer_convert(unit_value)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition_turns = integer_convert(condition_turns)
	complexity = get_name(Complex, complexity)


	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)
	
	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	action_when = selects(action_when, check_type_select)

	conditions_select = [{'type': 'current', 'name': 'Current Condition'}, {'type': 'any', 'name': 'Any Condition'}]
	condition1 = selects(condition1, conditions_select)
	condition2 = selects(condition2, conditions_select)

	
	
	
	dc_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'mod', 'name': 'DC Modifier'}, {'type': 'choice', 'name': 'Chosen by Player'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]



	body = send(cells, body)

	cells.clear()

	return (body)

def skill_degree_post(entry, body, cells):

	target = entry.target
	value = entry.value
	type = entry.type
	action = entry.action
	time = entry.time
	recovery = entry.recovery
	damage_type = entry.damage_type
	object = entry.object
	object_effect = entry.object_effect
	inflict_type = entry.inflict_type
	inflict_flat = entry.inflict_flat
	inflict_trait_type = entry.inflict_trait_type
	inflict_trait = entry.inflict_trait
	inflict_math = entry.inflict_math
	inflict_mod = entry.inflict_mod
	inflict_bonus = entry.inflict_bonus
	damage_mod = entry.damage_mod
	damage_consequence = entry.damage_consequence
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
	level_direction = entry.level_direction
	circumstance = entry.circumstance
	circ_target = entry.circ_target
	measure_effect = entry.measure_effect
	measure_rank_value = entry.measure_rank_value
	measure_rank = entry.measure_rank
	unit_value = entry.unit_value
	unit_type = entry.unit_type
	unit = entry.unit
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_trait_math = entry.measure_trait_math
	measure_mod = entry.measure_mod
	condition_type = entry.condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	condition_turns = entry.condition_turns
	keyword = entry.keyword
	nullify = entry.nullify
	cumulative = entry.cumulative
	linked = entry.linked

	value = integer_convert(value)
	action = get_name(Action, action)
	time = integer_convert(time)
	object = integer_convert(object)
	inflict_flat = integer_convert(inflict_flat)
	inflict_math = math_convert(inflict_math)
	inflict_mod = integer_convert(inflict_mod)
	inflict_bonus = integer_convert(inflict_bonus)
	damage_mod = integer_convert(damage_mod)
	damage_consequence = get_name(Consequence, damage_consequence)
	consequence_action = action_convert(consequence_action_type, consequence_action)
	consequence = get_name(Consequence, consequence)
	knowledge_count = integer_convert(knowledge_count)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	circumstance = get_circ(SkillCirc, circumstance)
	measure_rank_value = integer_convert(measure_rank_value)
	measure_rank = get_name(Rank, measure_rank)
	unit_value = integer_convert(unit_value)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	condition_damage_value = integer_convert(condition_damage_value)
	condition_turns = integer_convert(condition_turns)
	nullify = integer_convert(nullify)

	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'One Level Up'}, {'type': -1, 'name': 'One Level Down'}]
	level_direction = selects(level_direction, updown) 
	
	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown)
	
	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)
	circ_target = selects(circ_target, targets_select)

	repair_select = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]
	object_effect = selects(object_effect, repair_select)

	specificity_select = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	knowledge_specificity = selects(knowledge_specificity, specificity_select)

	conditions_select = [{'type': 'current', 'name': 'Current Condition'}, {'type': 'any', 'name': 'Any Condition'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, conditions_select)
	condition2 = selects(condition2, conditions_select)


	deg_mod_type = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'action', 'name': 'Action Change'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'time', 'name': 'Time Modifier'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'level', 'name': 'Level'}, {'type': 'knowledge', 'name': 'Gain Knowledge'}, {'type': 'consequence', 'name': 'Consequence'}]

	damage_type = [{'type': '', 'name': 'Damage Type'}, {'type': 'inflict', 'name': 'Inflict'}, {'type': 'reduce', 'name': 'Reduce'}, {'type': 'object', 'name': 'Object'}]

	inflict = [{'type': '', 'name': 'Inflict Type'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'bonus', 'name': 'Flat Bonus'}, {'type': 'math', 'name': 'Math'}]

	knowledge = [{'type': '', 'name': 'GM Knowledge'}, {'type': 'bonus', 'name': 'Learn Bonus'}, {'type': 'lie', 'name': 'GM May Lie'}]

	measure_effect = [{'type': '', 'name': 'Measurement Type'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'unit', 'name': 'Unit Value'}, {'type': 'skill', 'name': 'Skill Modifier'}]

	condition_type = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]


	body = send(cells, body)

	cells.clear()

	return (body)
	
def skill_opposed_post(entry, body, cells):

	attached = entry.attached
	frequency = entry.frequency
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check
	secret = entry.secret
	recurring = entry.recurring
	multiple = entry.multiple
	recurring_value = entry.recurring_value
	recurring_units = entry.recurring_units

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)
	recurring_value = integer_convert(recurring_value)
	recurring_units = get_name(Unit, recurring_units)

	frequency_select = [{'type': '', 'name': 'Frequency'}, {'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}]
	frequency = selects(frequency, frequency_select)

	attached_select = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}]
	attached = selects(attached, attached_select)


	body = send(cells, body)

	cells.clear()

	return (body)

def skill_time_post(entry, body, cells):

	type = entry.type
	value_type = entry.value_type
	rank1 = entry.rank1
	rank1_value = entry.rank1_value
	rank_math = entry.rank_math
	rank2 = entry.rank2
	rank2_value = entry.rank2_value
	value = entry.value
	units = entry.units
	trait_type = entry.trait_type
	trait = entry.trait
	math = entry.math
	math_value = entry.math_value
	recovery = entry.recovery
	recovery_penalty = entry.recovery_penalty
	recovery_time = entry.recovery_time
	recovery_incurable = entry.recovery_incurable

	
	rank1 = get_name(Rank, rank1)
	rank1_value = integer_convert(rank1_value)
	rank_math = math_convert(rank_math)
	rank2 = get_name(Rank, rank2)
	rank2_value = integer_convert(rank2_value)
	value = integer_convert(value)
	units = get_name(Unit, units)
	math = math_convert(math)
	math_value = integer_convert(math_value)
	recovery_penalty = integer_convert(recovery_penalty)
	recovery_time = integer_convert(recovery_time)

	time_effect_select = [{'type': '', 'name': 'Time Type'}, {'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]
	type = selects(type, time_effect_select)



	time_value = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}, {'type': 'rank', 'name': 'Measurement'}, {'type': 'gm', 'name': 'Set by GM'}]



	body = send(cells, body)

	cells.clear()

	return (body)

def skill_modifiers_post(entry, body, cells):

	skill_id = entry.skill_id
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
	bonus_trait = variable_trait(bonus_trait, bonus_trait_type)
	bonus_check = entry.bonus_check
	bonus_check_range = entry.bonus_check_range
	bonus_conflict = entry.bonus_conflict
	penalty_trait_type = entry.penalty_trait_type
	penalty_trait = entry.penalty_trait
	penalty_trait = variable_trait(penalty_trait, penalty_trait_type)
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
	skill = entry.skill
	light = entry.light

	bonus = integer_convert(bonus)
	penalty = integer_convert(penalty)
	multiple_count = integer_convert(multiple_count)
	lasts = integer_convert(lasts)

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	bonus_type = selects(bonus_type, modifier_type)
	penalty_type = selects(penalty_type, modifier_type)

	multiple_select = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]
	multiple = selects(multiple, multiple_select)

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
	skill = name(Skill, skill)
	light = name(Light, light)

	bonus_active_defense = variable_value('trait', bonus_effect, bonus_active_defense)
	bonus_conflict_defend = variable_value('conflict', bonus_effect, bonus_conflict_defend)
	penalty_active_defense = variable_value('trait', penalty_effect, penalty_active_defense)
	penalty_conflict_defend = variable_value('conflict', penalty_effect, penalty_conflict_defend)

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	cells = cell('Bonus', 8, [bonus], cells)
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
	
	cells = cell('Penalty', 8, [penalty], cells)
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
	vcells = vcell('skill', 20, [skill], vcells)
	vcells = vcell('light', 20, [light], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)



def skill_levels_post(entry, body, cells):

	skill_id = entry.sjukk_id
	level_type = entry.level_type
	level = entry.name
	level_effect = entry.level_effect


	cells = cell('Level', 17, [level], cells)
	cells = cell('Effect', 58, [level_effect], cells)

	body = send(cells, body)

	cells.clear()

	return (body)
