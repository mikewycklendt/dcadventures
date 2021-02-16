
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillMove, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait, get_name, get_circ, int_word, one_of, trait_select, string_value, string_value_else

def skill_ability_post(entry, body, cells):

	ability = entry.ability
	circumstance = entry.circumstance

	ability = get_name(Ability, ability)

	cells = cell('Ability', 15, [ability])
	cells = cell('Circumstance', 75, [circumstance])

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
	
	trait = trait_select(trait, trait_type)

	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	mod = integer_convert(mod)
	action = action_convert(action_type, action)
	

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_type_select)

	cells = cell('Check', 15, [check_type])
	cells = cell('Modifier', 8, [mod], cells)
	cells = cell('When', 8, [when], cells)
	cells = cell('Check Trait', 14, [trait], cells)
	cells = cell('Action', 14, [action], cells)
	
	vcells = vcell('condition', 25, [condition1, 'to', condition2])
	w = width(10, 8, conflict_range)
	vcells = vcell('conflict', w, [conflict, conflict_range], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	cells = check_cell('Free', 7, free, cells)
	cells = check_cell('Weapon', 8, conflict_weapon, cells)

	cells = cell('Circumstance', 30, [circumstance], cells)

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
	measure_math_rank = entry.measure_math_rank
	keyword = entry.keyword
	cumulative = entry.cumulative
	optional = entry.optional
	lasts = entry.lasts
	turns = entry.turns
	unit_time = entry.unit_time
	time_units = entry.time_units
	time_rank = entry.time_rank
	circumstance = entry.circumstance

	measure_trait = trait_select(measure_trait, measure_trait_type)

	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_math_rank = get_name(Rank, measure_math_rank)
	time_units = get_name(Unit, time_units)

	mod = integer_convert(mod)
	speed = integer_convert(speed)
	temp = integer_convert(temp)
	time = integer_convert(time)
	conditions = integer_convert(conditions)	
	measure_rank_value = integer_convert(measure_rank_value)
	unit_value = integer_convert(unit_value)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	turns = integer_convert(turns)
	unit_time = integer_convert(unit_time)
	time_rank = integer_convert(time_rank)


	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	circ_target = selects(circ_target, targets_select)

	circ_targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar Biology'}]
	target = selects(target, circ_targets_select)

	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	conditions_effect = selects(conditions_effect, updown)


	cells = cell('Target', 16, [circ_target])
	cells = cell('Modifier', 8, [mod], cells)
	cells = cell('Keyword', 18, [keyword], cells)

	vcells = vcell('turns', 10, [turns])
	vcells = vcell('time', 14, [unit_time, time_units], vcells)
	vcells = vcell('rank', 6, [time_rank], vcells)
	cells = vcell_add('Lasts', lasts, vcells, cells)

	vcells = vcell('condition', 25, [condition1, 'to', condition2], 'e', condition_type, 'condition')
	vcells = vcell('condition', 17, [conditions, 'Conditions', conditions_effect], vcells, condition_type, 'damage')
	
	time = add_plus(time)
	vcells = vcell('time', 14, [time, 'Time Rank'], vcells)
	
	temp = int_word(temp, 'Turns')
	vcells = vcell('temp', 25, ['Effect Lasts for', temp], vcells)

	measure_rank_value = add_plus(measure_rank_value)
	vcells = vcell('measure', 18, [measure_rank_value, measure_rank], vcells, measure_effect, 'rank')

	vcells = vcell('measure', 16, [unit_value, unit], vcells, measure_effect, 'unit')

	vcells = vcell('measure', 35, [measure_trait, measure_trait_math, measure_mod, measure_math_rank], vcells, measure_effect, 'skill')
	
	vcells = vcell('level', 16, [level], vcells)
	
	speed = add_plus(speed)
	vcells = vcell('speed', 20, ['Speed Rank', speed], vcells)
	
	vcells = vcell('target', 30, ['If Target is', target], vcells)
	
	cells = vcell_add('Effect', effect, vcells, cells)

	cells = cell('Circumstance', 30, [circumstance], cells)

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
	measure_math_rank = entry.measure_math_rank
	measure_trait_type_unit = entry.measure_trait_type_unit
	measure_trait_unit = entry.measure_trait_unit
	measure_trait_math_unit = entry.measure_trait_math_unit
	measure_mod_unit = entry.measure_mod_unit
	measure_math_unit = entry.measure_math_unit
	level_type = entry.level_type
	level = entry.level
	condition1 = entry.condition1
	condition2 = entry.condition2
	condition_turns = entry.condition_turns
	keyword = entry.keyword
	complexity = entry.complexity
	action_no_damage = entry.action_no_damage
	condition_no_damage = entry.condition_no_damage

	math_trait = trait_select(math_trait, math_trait_type)	
	inflict_trait = trait_select(inflict_trait, inflict_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)
	measure_trait_unit = trait_select(measure_trait_unit, measure_trait_type_unit)


	value = integer_convert(value)
	mod = integer_convert(mod)
	math_value = integer_convert(math_value)
	inflict_flat = integer_convert(inflict_flat)
	inflict_mod = integer_convert(inflict_mod)
	inflict_bonus = integer_convert(inflict_bonus)
	damage_mod = integer_convert(damage_mod)
	measure_rank_value = integer_convert(measure_rank_value)
	unit_value = integer_convert(unit_value)
	measure_mod = integer_convert(measure_mod)
	measure_mod_unit = integer_convert(measure_mod_unit)
	condition_turns = integer_convert(condition_turns)

	math = math_convert(math)
	action = get_name(Action, action)
	inflict_math = math_convert(inflict_math)
	damage_consequence = get_name(Consequence, damage_consequence)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert(measure_trait_math)
	measure_math_rank = get_name(Rank, measure_math_rank)
	measure_math_unit = get_name(Unit, measure_math_unit)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	complexity = get_name(Complex, complexity)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)
	
	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	action_when = selects(action_when, check_type_select)

	conditions_select = [{'type': 'current', 'name': 'Current Condition'}, {'type': 'any', 'name': 'Any Condition'}]
	condition1 = selects(condition1, conditions_select)
	condition2 = selects(condition2, conditions_select)

	cells = cell('Target', 15, [target])
	
	vcells = vcell('value', 6, [value])
	vcells = vcell('math', 16, [math_value, math, math_trait], vcells)
	mod = add_plus(mod)
	vcells = vcell('mod', 7, [mod], vcells)
	vcells = vcell('choice', 14, ['Chosen by Player'], vcells)
	cells = vcell_add('DC', dc, vcells, cells)

	cells = check_cell('Condition', 9, condition, cells, True)
	new_mod = mod_create('Condition', 12)
	word = string('for', condition_turns)
	word2 = string('Turns', condition_turns)
	new_mod = mod_cell('Effect', 7, ['From', condition1, 'to', condition2, word, condition_turns, word2], new_mod)
	new_mod = mod_cell('Only if No Damage', 20, [condition_no_damage], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Keyword', 8, keyword_check, cells, True)
	new_mod = mod_create('Keyword', 9)
	new_mod = mod_cell('Keyword', 9, [keyword], new_mod)
	body = mod_add(keyword_check, new_mod, body)

	cells = check_cell('Level', 7, levels, cells, True)
	new_mod = mod_create('Level', 7)
	new_mod = mod_cell('Level Type', 14, [level_type], new_mod)
	new_mod = mod_cell('Leve;', 6, [level], new_mod)		
	body = mod_add(levels, new_mod, body)

	cells = check_cell('Damage', 8, damage, cells, True)	
	select = [{'type': 'inflict', 'name': 'Inflict Damage', 'w': 16}, {'type': 'reduce', 'name': 'Reduce Damage', 'w': 14}]
	new_mod = mod_create('Damage', 8, damage_type, select)
	value = 'inflict'
	new_mod = mod_cell('Value', 7, [inflict_flat], new_mod, value)
	new_mod = mod_cell('Math', 6, [inflict_trait, inflict_math, inflict_mod], new_mod, value)
	new_mod = mod_cell('Bonus', 7, [inflict_bonus], new_mod, value)
	value = 'reduce'
	new_mod = mod_cell('Modifier', 9, [damage_mod], new_mod, value)
	new_mod = mod_cell('Consequence', 13, [damage_consequence], new_mod, value)
	body = mod_add(damage, new_mod, body)

	cells = check_cell('Complexity', 11, complex, cells, True)
	new_mod = mod_create('Complexity', 11)
	new_mod = mod_cell('Complexity Type', 17, [complexity], new_mod)	
	body = mod_add(complex, new_mod, body)

	cells = check_cell('Measurement', 12, measure, cells, True)
	select = [{'type': 'rank', 'name': 'Measurement Rank', 'w': 17}, {'type': 'unit', 'name': 'Measurement Value', 'w': 17}, {'type': 'skill', 'name': 'Skill Modifier Measurement', 'w': 27}]
	new_mod = mod_create('Measurement', 12, measure_effect, select)
	value = 'rank'
	new_mod = mod_cell('Value', 7, [measure_rank_value], new_mod, value)
	new_mod = mod_cell('Rank', 5, [measure_rank], new_mod, value)
	value = 'unit'
	new_mod = mod_cell('Value', 6, [unit_value], new_mod, value)
	new_mod = mod_cell('Units', 6, [unit], new_mod, value)
	value = 'skill_rank'
	new_mod = mod_cell('Math', 5, [measure_trait, measure_trait_math, measure_mod, measure_math_rank], new_mod, value)
	value = 'skill_unit'
	new_mod = mod_cell('Math', 5, [measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], new_mod, value)
	
	body = mod_add(measure, new_mod, body)

	cells = check_cell('Action Change', 15, change_action, cells, True)
	new_mod = mod_create('Action Change', 15)
	new_mod = mod_cell('Action Changed To', 20, [action], new_mod)
	new_mod = mod_cell('When', 5, [action_when], new_mod)
	new_mod = mod_cell('Only if No Damage', 20, [action_no_damage], new_mod)
	body = mod_add(change_action, new_mod, body)

	cells = check_cell('Cover', 7, cover, cells)
	cells = check_cell('Concealmet', 10, conceal, cells)

	cells = cell('Description', 35, [description], cells)

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
	measure_math_rank = entry.measure_math_rank
	measure_trait_type_unit = entry.measure_trait_type_unit
	measure_trait_unit = entry.measure_trait_unit
	measure_trait_math_unit = entry.measure_trait_math_unit
	measure_mod_unit = entry.measure_mod_unit
	measure_math_unit = entry.measure_math_unit
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

	inflict_trait = trait_select(inflict_trait, inflict_trait_type)
	consequence_trait = trait_select(consequence_trait, consequence_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)
	measure_trait_unit = trait_select(measure_trait_unit, measure_trait_type_unit)

	action = get_name(Action, action)
	damage_consequence = get_name(Consequence, damage_consequence)
	consequence = get_name(Consequence, consequence)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_math_rank = get_name(Rank, measure_math_rank)
	measure_math_unit = get_name(Unit, measure_math_unit)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

	value = integer_convert(value)
	time = integer_convert(time)
	object = integer_convert(object)
	inflict_flat = integer_convert(inflict_flat)
	inflict_math = math_convert(inflict_math)
	inflict_mod = integer_convert(inflict_mod)
	inflict_bonus = integer_convert(inflict_bonus)
	damage_mod = integer_convert(damage_mod)
	consequence_action = action_convert(consequence_action_type, consequence_action)
	knowledge_count = integer_convert(knowledge_count)
	circumstance = get_circ(SkillCirc, circumstance)
	measure_rank_value = integer_convert(measure_rank_value)
	unit_value = integer_convert(unit_value)
	measure_trait_math = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	measure_trait_math_unit = math_convert(measure_trait_math_unit)
	measure_mod_unit = integer_convert(measure_mod_unit)
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

	cells = cell('Target', 15, [target])
	cells = cell('Degree', 8, [value], cells)
	cells = cell('Keyword', 15, [keyword], cells)

	vcells = vcell('action', 40, ['Action Changed to', action])

	vcells = vcell('measure', 20, [measure_rank_value, measure_rank], vcells, measure_effect, 'rank')
	vcells = vcell('measure', 20, [unit_value, unit], vcells, measure_effect, 'unit')	
	vcells = vcell('measure', 35, [measure_trait, measure_trait_math, measure_mod, measure_math_rank], vcells, measure_effect, 'skill_rank')
	vcells = vcell('measure', 35, [measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], vcells, measure_effect, 'skill_unit')

	word = string('for', condition_turns)
	word2 = string('Turns', condition_turns)
	vcells = vcell('condition', 40, ['From', condition1, 'to', condition2, word, condition_turns, word2], vcells, condition_type, 'condition')
	vcells = vcell('condition', 25, [condition_damage_value, 'Conditions', condition_damage], vcells, condition_type, 'damage')

	vcells = vcell('circ', 40, [circumstance, 'on', circ_target], vcells)
	time = add_plus(time)
	vcells = vcell('time', 25, [time, 'Time Rank'], vcells)
	
	vcells = vcell('damage', 20, [inflict_flat, 'Rank Damage'], vcells, damage_type, 'inflict', inflict_type, 'flat')
	inflict_bonus = add_plus(inflict_bonus)
	vcells = vcell('damage', 20, [inflict_bonus, 'Rank Damage'], vcells, damage_type, 'inflict', inflict_type, 'bonus')
	vcells = vcell('damage', 5, [inflict_trait, 'Rank', inflict_math, inflict_mod, '= Rank Damage'], vcells, damage_type, 'inflict', inflict_type, 'math')
	word = string('if', damage_consequence)
	w = width(10, 16, damage_consequence)
	vcells = vcell('damage', w, [damage_mod, word, damage_consequence], vcells, damage_type, 'reduce')
	vcells = vcell('damage', 25, [object, 'More', object_effect], vcells, damage_type, 'object')

	level_value = one_of(level_type, [level])
	level_value = one_of(level_type, [level_direction])
	vcells = vcell('level', 20, [level_value], vcells)

	vcells = vcell('knowledge', 35, ['Learn', knowledge_count, knowledge_specificity, 'Bonud'], vcells, knowledge, 'bonus')
	vcells = vcell('knowledge', 12, ['GM May Lie'], vcells, knowledge, 'lie')

	w = width(17, 13, consequence_action)
	w = width(w, 13, consequence_trait)
	word = string('with', [consequence_trait])
	vcells = vcell('consequence', w, [consequence_action, word, consequence_trait, 'results in', consequence], vcells)

	cells = vcell_add('Effect', type, vcells, cells)
	
	cells = cell('Nullify DC', 13, [nullify], cells)
	cella = check_cell('Cumulative', 12, cumulative, cells)
	cella = check_cell('Linked', 7, linked, cells)

	body = send(cells, body)

	cells.clear()

	return (body)
		
def skill_move_post(entry, body, cells):

	speed = entry.speed
	speed_rank = entry.speed_rank
	speed_trait_type = entry.speed_trait_type
	speed_trait = entry.speed_trait
	speed_math1 = entry.speed_math1
	speed_value1 = entry.speed_value1
	speed_math2 = entry.speed_math2
	speed_value2 = entry.speed_value2
	speed_description = entry.speed_description
	distance = entry.distance
	distance_rank = entry.distance_rank
	distance_value = entry.distance_value
	distance_units = entry.distance_units
	distance_rank_trait_type = entry.distance_rank_trait_type
	distance_rank_trait = entry.distance_rank_trait
	distance_rank_math1 = entry.distance_rank_math1
	distance_rank_value1 = entry.distance_rank_value1
	distance_rank_math2 = entry.distance_rank_math2
	distance_rank_value2 = entry.distance_rank_value2
	distance_unit_trait_type = entry.distance_unit_trait_type
	distance_unit_trait = entry.distance_unit_trait
	distance_unit_math1 = entry.distance_unit_math1
	distance_unit_value1 = entry.distance_unit_value1
	distance_unit_math2 = entry.distance_unit_math2
	distance_unit_value2 = entry.distance_unit_value2
	distance_math_units = entry.distance_math_units
	distance_description = entry.distance_description
	direction = entry.direction
	check_type = entry.check_type
	turns = entry.turns

	speed_trait = trait_select(speed_trait, speed_trait_type)
	distance_rank_trait = trait_select(distance_rank_trait, distance_rank_trait_type)
	distance_unit_trait = trait_select(distance_unit_trait, distance_unit_trait_type)

	bonus_type = string_value_else('Bonus', 'Check', 3, check_type)

	speed_rank = integer_convert(speed_rank)
	speed_trait = integer_convert(speed_trait)
	speed_value1 = integer_convert(speed_value1)
	speed_value2 = integer_convert(speed_value2)
	distance_rank = integer_convert(distance_rank)
	distance_value = integer_convert(distance_value)
	distance_rank_trait = integer_convert(distance_unit_trait)
	distance_rank_value1 = integer_convert(distance_rank_value1)
	distance_rank_value2 = integer_convert(distance_rank_value2)
	distance_unit_trait = integer_convert(distance_unit_trait)
	distance_unit_value1 = integer_convert(distance_unit_value1)
	distance_unit_value2 = integer_convert(distance_unit_value2)
	turns = integer_convert(turns)

	speed_math1 = math_convert(speed_math1)
	speed_math2 = math_convert(speed_math2)
	distance_units = get_name(Unit, distance_units)
	distance_rank_math1 = math_convert(distance_rank_math1)
	distance_rank_math2 = math_convert(distance_rank_math2)
	distance_unit_math1 = math_convert(distance_unit_math1)
	distance_unit_math2 = math_convert(distance_unit_math2)
	distance_math_units = get_name(Unit, distance_math_units)
	check_type = get_name(Check, check_type)

	direction_select = [{'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]
	direction = selects(direction, direction_select)

	cells = cell('Check', 16, [check_type])
	cells = cell('Direction', 12, [direction], cells)
	cells = cell('Turns', 12, [turns], cells)

	vcells = vcell('rank', 20, ['Speed Rank', speed_rank])
	vcells = vcell('mod', 25, [speed_trait, bonus_type, speed_math1, speed_value1, speed_math2, speed_value2], vcells)
	cells = vcell_add('Speed', speed, vcells, cells)
	cells = cell('Description', 20, [speed_description], cells)
	
	vcells = vcell('rank', 20, [distance_rank, 'Rank Distance'])
	vcells = vcell('unit', 20, [distance_value, distance_units], vcells)
	vcells = vcell('unit_math', 25, [distance_unit_trait, bonus_type, distance_unit_math1, distance_unit_value1, distance_unit_math2,  distance_unit_value2, distance_math_units], vcells)
	vcells = vcell('rank_math', 25, [distance_rank_trait, bonus_type, distance_rank_math1, distance_rank_value1, distance_rank_math2, distance_rank_value2], vcells)
	cells = vcell_add('Distance', distance, vcells, cells)
	cells = cell('Description', 20, [distance_description], cells)

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

	trait = trait_select(trait, trait_type)
	opponent_trait = trait_select(opponent_trait, opponent_trait_type)

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

	cells = cell('When', 13, [attached])
	cells = cell('Frequency', 13, [frequency], cells)
	cells = cell('Player Check', 15, [trait], cells)
	cells = cell('Modifier', 9, [mod], cells)
	cells = cell('Check', 14, [player_check], cells)
	cells = cell('Opponent Check', 15, [opponent_trait], cells)
	cells = cell('Modifier', 9, [opponent_mod], cells)
	cells = cell('Check', 14, [opponent_check], cells)
	cells = check_cell('Secret', 8, secret, cells)

	cells = check_cell('Recurring', 10, recurring, cells, True)
	new_mod = mod_create('Recurring Check', 17)
	new_mod = mod_cell('Every', 7, [recurring_value, recurring_units], new_mod)
	mod_add(recurring, new_mod, body)

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

	trait = trait_select(trait, trait_type)

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

	cells = cell('Time Type', 24, [type])

	vcells = vcell('value', 17, [value, units])
	vcells = vcell('math', 30, [trait, math, math_value, '= Time Rank'], vcells)
	vcells = vcell('rank', 45, [rank1, rank1_value, rank_math, rank2, rank2_value], vcells)
	vcells = vcell('gm', 13, ['Set by GM'], vcells)
	vcell_add('Time', value_type, vcells, cells)

	cells = check_cell('Recovey', 12, recovery, cells, True)
	new_mod = mod_create('Recovery Time', 18)
	new_mod = mod_cell('Effect', 7, [recovery_penalty, 'Toughness Penalty Nullified Every', recovery_time, 'Time Rank'], new_mod)
	mod_add(recovery, new_mod, body)

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

	bonus_trait = trait_select(bonus_trait, bonus_trait_type)
	penalty_trait = trait_select(penalty_trait, penalty_trait_type)









	bonus = integer_convert(bonus)
	penalty = integer_convert(penalty)
	multiple_count = integer_convert(multiple_count)
	lasts = integer_convert(lasts)

	modifier_type = [{'type': '', 'name': 'Type'}, {'type': 'up', 'name': 'Up to'}, {'type': 'value', 'name': 'Exact'}, {'type': 'rank', 'name': 'Per Rank'},  {'type': '-1', 'name': 'Rank - 1'}]
	bonus_type = selects(bonus_type, modifier_type)
	penalty_type = selects(penalty_type, modifier_type)

	multiple_select = [{'type': '', 'name': 'If Multiple'}, {'type': 'together', 'name': 'All Work Together'}, {'type': 'round', 'name': 'Choose for Round'}, {'type': 'turn', 'name': 'Choose for Turn'}, {'type': 'pick', 'name': 'Pick 1'}, {'type': 'rank', 'name': '1 Per Rank'}]
	multiple = selects(multiple, multiple_select)

	environment = get_name(Environment, environment)
	sense = get_name(Sense, sense)
	mod_range = get_name(Ranged, mod_range)
	subsense = get_name(SubSense, subsense)
	cover = get_name(Cover, cover)
	conceal = get_name(Conceal, conceal)
	maneuver = get_name(Maneuver, maneuver)
	weapon_melee = get_name(WeaponType, weapon_melee)
	weapon_ranged = get_name(WeaponType,  weapon_ranged)
	condition = get_name(Condition, condition)
	power = get_name(Power, power)
	consequence = get_name(Consequence, consequence)
	creature = get_name(Creature, creature)
	emotion = get_name(Emotion, emotion)
	conflict = get_name(ConflictAction, conflict)
	profession = get_name(Job, profession)
	bonus_conflict = get_name(ConflictAction, bonus_conflict)
	penalty_conflict = get_name(ConflictAction, penalty_conflict)
	skill = get_name(Skill, skill)
	light = get_name(Light, light)
	bonus_check = get_name(Check, bonus_check)
	bonus_check_range = get_name(Ranged, bonus_check_range)
	penalty_check = get_name(Check, penalty_check)
	penalty_check_range = get_name(Ranged, penalty_check_range)

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

	skill_id = entry.skill_id
	level_type = entry.level_type
	level = entry.name
	level_effect = entry.level_effect


	cells = cell('Level', 17, [level], cells)
	cells = cell('Effect', 58, [level_effect], cells)

	body = send(cells, body)

	cells.clear()

	return (body)
