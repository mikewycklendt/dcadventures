
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillMove, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import SkillCircType, SkillDCType, SkillDegreeType, SkillMoveType, SkillTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, value_limit, select_check, check_of, multiple_effect_check, multiple_link_check, required_setting, linked_group_check, required_link_field, linked_field, required_rule
from functions.create_posts import send_multiple, one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string, circ_cell

from create_functions.skill_create import skill_entry_check, skill_required_entry, skill_required_entry_multiple

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()


def skill_ability_post(entry, body, cells):

	ability = entry.ability
	circumstance = entry.circumstance
	variable = entry.variable

	ability = get_name(Ability, ability)
	variable = get_keyword(SkillCheck, variable)

	cells = cell('Ability', 15, [ability])
	cells = cell('Checl', 18, variable)
	cells = cell('Circumstance', 75, [circumstance])

	body = send(cells, body)

	cells.clear()

	return (body)
	
def skill_check_post(entry, body, cells):

	id = entry.id
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
	degree = entry.degree
	circ = entry.circ
	dc = entry.dc
	dc_value = entry.dc_value
	time = entry.time
	move = entry.move
	keyword = entry.keyword
	attack = entry.attack
	opposed = entry.opposed
	condition = entry.condition
	condition_target = entry.condition_target
	conditions_target = entry.conditions_target

	body['title'] = keyword
	body['add_title'] = True
	body['created'] = False


	trait = trait_select(trait, trait_type)

	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	mod = integer_convert(mod)
	action = action_convert(action_type, action)
	condition = get_name(Condition, condition)

	degree = get_name(SkillDegreeType, degree)
	circ = get_name(SkillCircType, circ)
	dc = get_name(SkillDCType, dc)
	time = get_name(SkillTimeType, time)
	move = get_name(SkillMoveType, move)
	dc_value = get_keyword(SkillDC, dc_value)
	opposed = get_keyword(SkillOpposed, opposed)

	attack = integer_convert(attack)

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}]
	when = selects(when, check_type_select)

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	condition_target = selects(condition_target, targets)
	conditions_target = selects(conditions_target, targets)

	cells = cell('Keyword', 14, [keyword])
	cells = cell('Check', 11, [check_type], cells)
	cells = cell('Modifier', 8, [mod], cells)
	cells = cell('When', 12, [when], cells)
	cells = cell('Check Trait', 16, [trait], cells)
	cells = cell('Action', 11, [action], cells)
	
	vcells = vcell('change', 25, [conditions_target, 'from', condition1, 'to', condition2])
	vcells = vcell('condition', 20, [condition_target, condition], vcells)
	w = width(10, 8, conflict_range)
	vcells = vcell('conflict', w, [conflict, conflict_range], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	attack = add_plus(attack)
	cells = cell('Attack', 9, [attack], cells)
	cells = cell('Opposed', 14, [opposed], cells)
	cells = cell('Circumstance', 14, [circ], cells)
	cells = cell('DC', 14, [dc, dc_value], cells)
	cells = cell('Degree', 14, [degree], cells)
	cells = cell('Movement', 14, [move], cells)
	cells = cell('Time', 14, [time], cells)

	cells = check_cell('Free', 7, free, cells)
	cells = check_cell('Weapon', 8, conflict_weapon, cells)

	cells = circ_cell('Circ', 'Circumstance', 6, circumstance, cells, body)

	body = send_multiple(id, cells, body)

	cells.clear()

	return (body)
	
def skill_circ_post(entry, body, cells):

	circ_target = entry.circ_target
	mod = entry.mod
	effect = entry.effect
	speed = entry.speed
	target = entry.target
	level_type = entry.level_type
	level = entry.level
	condition_type = entry.condition_type
	condition1 = entry.condition1
	condition2 = entry.condition2
	conditions = entry.conditions
	conditions_effect = entry.conditions_effect
	measure_effect = entry.measure_effect
	measure_type = entry.measure_type
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
	surface = entry.surface
	circumstance = entry.circumstance
	lasts = entry.lasts
	title = entry.title
	tools = entry.tools
	materials = entry.materials
	max = entry.max
	trait_type = entry.trait_type
	trait = entry.trait
	trait_target = entry.trait_target
	environment = entry.environment
	nature = entry.nature
	check_type =  entry.check_type



	title_name = get_name(SkillCircType, title)
	body['title'] = title_name

	measure_trait = trait_select(measure_trait, measure_trait_type)
	trait = trait_select(trait, trait_type)

	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_math_rank = get_name(Rank, measure_math_rank)
	measure_type = math_convert(measure_type)
	environment = get_name(Environment, environment)
	nature = get_name(Nature, nature)
	check_type = get_name(Check, check_type)

	speed = integer_convert(speed)
	conditions = integer_convert(conditions)	
	measure_rank_value = integer_convert(measure_rank_value)
	unit_value = integer_convert(unit_value)
	measure_trait_math = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	max = integer_convert(max)

	lasts = get_keyword(SkillTime, lasts)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	circ_target = selects(circ_target, targets_select)

	circ_targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'biology', 'name': 'Unfamiliar'}]
	target = selects(target, circ_targets_select)

	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	conditions_effect = selects(conditions_effect, updown)

	tools_select = [{'type': '', 'name': 'Tools'}, {'type': 'with', 'name': 'With Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'none', 'name': 'No Tools'}]
	tools = selects(tools, tools_select)

	materials_select = [{'type': '', 'name': 'Materials'}, {'type': 'with', 'name': 'With Materials'}, {'type': 'improper', 'name': 'Improper Materials'}, {'type': 'none', 'name': 'No Materials'}]
	materials = selects(materials, materials_select)
	
	offers  = [{'type': '', 'name': 'Effect'}, {'type': 'required', 'name': 'Requires'}, {'type': 'provides', 'name': 'Provides'}]

	required_tools = [{'type': '', 'name': 'Tools'}, {'type': 'correct', 'name': 'Correct Tools'}, {'type': 'improper', 'name': 'Improper Tools'}, {'type': 'gm', 'name': 'GM Decides'}]



	cells = cell('Keyword', 13, [keyword])
	cells = cell('Target', 12, [circ_target], cells)
	cells = cell('Modifier', 8, [mod], cells)
	cells = cell('Lasts', 15, [lasts], cells)

	vcells = vcell('condition', 25, [condition1, 'to', condition2], 'e', condition_type, 'condition')
	vcells = vcell('condition', 17, [conditions, 'Conditions', conditions_effect], vcells, condition_type, 'damage')
	
	measure_rank_value = add_plus(measure_rank_value)
	vcells = vcell('measure', 18, [measure_type, measure_rank_value, measure_rank], vcells, measure_effect, 'rank')

	vcells = vcell('measure', 16, [measure_type, unit_value, unit], vcells, measure_effect, 'unit')

	vcells = vcell('measure', 35, [measure_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], vcells, measure_effect, 'skill')
	
	vcells = vcell('level', 16, [level], vcells)
	
	speed = add_plus(speed)
	vcells = vcell('speed', 20, ['Speed Rank', speed], vcells)
	
	vcells = vcell('target', 30, ['If Target is', target], vcells)
	
	vcells = vcell('tools', 25, [tools], vcells)
	
	vcells = vcell('materials', 25, [materials], vcells)
	
	word = string('on', [check_type])
	word2 = string('Check', [check_type])
	vcells = vcell('trait', 35, ['Affects', trait, word, check_type, word2], vcells)
	
	vcells = vcell('env', 25, ['If', environment], vcells)
	
	vcells = vcell('nature', 25, ['If', nature], vcells)
	
	cells = vcell_add('Effect', effect, vcells, cells)

	cells = check_cell('Surface', 8, surface, cells)
	cells = check_cell('Optional', 9, optional, cells)
	cells = check_cell('Cumulative', 10, cumulative, cells)
	cells = cell('Maximum', 9, [max], cells)

	cells = circ_cell('Circ', 'Circumstance', 6, circumstance, cells, body)

	body = send_multiple(title, cells, body)

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
	surface = entry.surface
	levels = entry.levels
	damage = entry.damage
	cover = entry.cover
	complex = entry.complex
	measure = entry.measure
	conceal = entry.conceal
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
	measure_type = entry.measure_type
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
	tools_check = entry.tools_check
	cover_effect = entry.cover_effect
	cover_type = entry.cover_type
	conceal_effect = entry.conceal_effect
	conceal_type = entry.conceal_type
	tools = entry.tools
	variable_check = entry.variable_check
	variable = entry.variable
	time = entry.time
	title = entry.title
	effect_target = entry.effect_target
	equipment_use = entry.equipment_use
	equipment_type = entry.equipment_type
	equipment = entry.equipment
	equip = entry.equip

	title_name = get_name(SkillDCType, title)
	body['title'] = title_name

	cover_type = get_name(Cover, cover_type)
	conceal_type = get_name(Conceal, conceal_type)
	variable = get_keyword(SkillCheck, variable)
	time = get_keyword(SkillTime, time)
	measure_type = math_convert(measure_type)

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
	inflict_math = math_convert(inflict_math)
	damage_consequence = get_name(Consequence, damage_consequence)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = math_convert(measure_trait_math)
	measure_math_rank = get_name(Rank, measure_math_rank)
	measure_math_unit = get_name(Unit, measure_math_unit)
	measure_trait_math_unit = get_name(Math, measure_trait_math_unit)
	equipment_type = get_name(EquipType, equipment_type)
	equipment = get_name(Equipment, equipment)

	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	complexity = get_name(Complex, complexity)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)
	effect_target = selects(effect_target, targets_select)

	equipment_use_select = [{'type': '', 'name': 'Use Type'}, {'type': 'use', 'name': 'With Use of'}, {'type': 'resist', 'name': 'Resist'}]
	equipment_use = selects(equipment_use, equipment_use_select)


	cells = cell('Keyword', 14, [keyword])
	cells = cell('Target', 10, [target], cells)
	cells = cell('Effect Target', 16, [effect_target], cells)
	cells = cell('Duration', 14, [time], cells)

	vcells = vcell('value', 6, [value])
	vcells = vcell('math', 22, [math_value, math, math_trait], vcells)
	mod = add_plus(mod)
	vcells = vcell('mod', 7, [mod], vcells)
	vcells = vcell('choice', 14, ['Chosen by Player'], vcells)
	cells = vcell_add('DC', dc, vcells, cells)

	cells = check_cell('Condition', 9, condition, cells, True)
	new_mod = mod_create('Condition', 12)
	new_mod = mod_cell('Effect', 7, ['From', condition1, 'to', condition2], new_mod)
	new_mod = mod_cell('Only if No Damage', 20, [condition_no_damage], new_mod)
	body = mod_add(condition, new_mod, body)

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
	new_mod = mod_cell('Value', 7, [measure_type, measure_rank_value], new_mod, value)
	new_mod = mod_cell('Rank', 5, [measure_rank], new_mod, value)
	value = 'unit'
	new_mod = mod_cell('Value', 6, [measure_type, unit_value], new_mod, value)
	new_mod = mod_cell('Units', 6, [unit], new_mod, value)
	value = 'skill_rank'
	new_mod = mod_cell('Math', 5, [measure_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], new_mod, value)
	value = 'skill_unit'
	new_mod = mod_cell('Math', 5, [measure_type, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], new_mod, value)
	
	body = mod_add(measure, new_mod, body)

	cells = check_cell('Cover', 7, cover, cells, True)
	new_mod = mod_create('Cover', 10)
	new_mod = mod_cell('Effect', 8, [cover_effect], new_mod)
	new_mod = mod_cell('Type', 5, [cover_type], new_mod)
	body = mod_add(cover, new_mod, body)

	cells = check_cell('Concealment', 13, conceal, cells, True)
	new_mod = mod_create('Concealment', 15)
	new_mod = mod_cell('Effect', 8, [conceal_effect], new_mod)
	new_mod = mod_cell('Type', 5, [conceal_type], new_mod)
	body = mod_add(conceal, new_mod, body)

	cells = check_cell('Check', 10, variable_check, cells, True)
	new_mod = mod_create('Change Check', 18)
	new_mod = mod_cell('Check', 7, [variable], new_mod)
	body = mod_add(variable_check, new_mod, body)
	
	cells = check_cell('Equipment', 12, equip, cells, True)
	new_mod = mod_create('Equipment', 15)
	new_mod = mod_cell('Use Type', 9, [equipment_use], new_mod)
	new_mod = mod_cell('Type', 5, [equipment_type], new_mod)
	new_mod = mod_cell('Item', 9, [equipment], new_mod)
	body = mod_add(equip, new_mod, body)
	
	cells = check_cell('Surface', 8, surface, cells)

	cells = circ_cell('Description', 'Description', 13, description, cells, body)

	body = send_multiple(title, cells, body)

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
	level_time = entry.level_time
	circumstance = entry.circumstance
	circ_target = entry.circ_target
	measure_effect = entry.measure_effect
	measure_type = entry.measure_type
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
	check_type = entry.check_type
	opposed = entry.opposed
	variable = entry.variable
	resist_dc = entry.resist_dc
	resist_trait_type = entry.resist_trait_type
	resist_trait = entry.resist_trait
	skill_dc = entry.skill_dc
	skill_trait_type = entry.skill_trait_type
	skill_trait = entry.skill_trait
	routine_trait_type = entry.routine_trait_type
	routine_trait = entry.routine_trait
	routine_mod = entry.routine_mod
	attack = entry.attack
	attack_turns = entry.attack_turns
	compare = entry.compare
	title = entry.title
	effect_target = entry.effect_target
	value_type = entry.value_type
	description = entry.description

	title_name = get_name(SkillDegreeType, title)
	body['title'] = title_name

	inflict_trait = trait_select(inflict_trait, inflict_trait_type)
	consequence_trait = trait_select(consequence_trait, consequence_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)
	measure_trait_unit = trait_select(measure_trait_unit, measure_trait_type_unit)
	resist_trait =  trait_select(resist_trait, resist_trait_type)
	skill_trait = trait_select(skill_trait, skill_trait_type)
	routine_trait = trait_select(routine_trait, routine_trait_type)

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

	opposed = get_keyword(SkillOpposed, opposed)
	resist_dc = get_keyword(SkillDC, resist_dc)
	skill_dc = get_keyword(SkillDC, skill_dc)
	compare = get_keyword(SkillOpposed, compare)
	variable = get_keyword(SkillCheck, variable)
	attack_turns  = get_keyword(SkillTime, get_keyword)
	condition_turns = get_keyword(SkillTime, condition_turns)
	level_time = get_keyword(SkillTime, level_time)
	linked = get_keyword(SkillDegree, linked)
	measure_type = math_convert(measure_type)
	value_type = math_convert(value_type)

	variable_id = db_integer(Check, 'x')

	resist_trait = integer_convert(resist_trait)
	skill_trait = integer_convert(skill_trait)
	routine_trait = integer_convert(routine_trait)
	routine_mod = integer_convert(routine_mod)
	attack = integer_convert(attack)
	attack_turns = integer_convert(attack_turns)

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
	level_direction = integer_convert(level_direction)

	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'One Level Up'}, {'type': -1, 'name': 'One Level Down'}]
	level_direction = selects(level_direction, updown) 
	
	updown = [{'type': '', 'name': 'Direction'}, {'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown)
	
	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)
	circ_target = selects(circ_target, targets_select)
	effect_target = selects(effect_target, targets_select)

	repair_select = [{'type': '', 'name': 'Effect'}, {'type': 'stable', 'name': 'Stable'}, {'type': 'broke', 'name': 'Broken'}]
	object_effect = selects(object_effect, repair_select)

	specificity_select = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	knowledge_specificity = selects(knowledge_specificity, specificity_select)

	conditions_select = [{'type': 'current', 'name': 'Current Condition'}, {'type': 'any', 'name': 'Any Condition'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, conditions_select)
	condition2 = selects(condition2, conditions_select)

	cells = cell('Keyword', 15, [keyword])
	cells = cell('Target', 15, [target], cells)
	cells = cell('Effect Target', 16, [effect_target], cells)
	cells = cell('Degree', 12, [value_type, value], cells)

	vcells = vcell('action', 40, ['Action Changed to', action])

	vcells = vcell('measure', 20, [measure_type, measure_rank_value, measure_rank], vcells, measure_effect, 'rank')
	vcells = vcell('measure', 20, [measure_type, unit_value, unit], vcells, measure_effect, 'unit')	
	vcells = vcell('measure', 35, [measure_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], vcells, measure_effect, 'skill_rank')
	vcells = vcell('measure', 35, [measure_type, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], vcells, measure_effect, 'skill_unit')

	word = string('for', condition_turns)
	word2 = string('Turns', condition_turns)
	vcells = vcell('condition', 40, ['From', condition1, 'to', condition2], vcells, condition_type, 'condition')
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
	level_value = one_of(level_type, ['One Level', level_direction, level_type], level_value)
	vcells = vcell('level', 40, [level_value], vcells)

	vcells = vcell('knowledge', 35, ['Learn', knowledge_count, knowledge_specificity, 'Bonud'], vcells, knowledge, 'bonus')
	vcells = vcell('knowledge', 12, ['GM May Lie'], vcells, knowledge, 'lie')

	w = width(17, 13, consequence_action)
	w = width(w, 13, consequence_trait)
	word = string('with', [consequence_trait])
	vcells = vcell('consequence', w, [consequence_action, word, consequence_trait, 'results in', consequence], vcells)

	attack = add_plus(attack)
	vcells = vcell('check', 35, [skill_trait, 'Skill Check using', skill_dc, 'DC'], vcells, 1, check_type)
	vcells = vcell('check', 35, [opposed, 'Opposed Check'], vcells, 2, check_type)
	vcells = vcell('check', 35, [attack, 'using', attack_turns, 'Time'], vcells, 5, check_type)
	word = string('with', [routine_mod])
	word2 = string('Modifier', [routine_mod])
	w = width(20, 15, routine_mod)
	vcells = vcell('check', 35, [routine_trait, 'Routine Check', word, routine_mod, word2], vcells, 3, check_type)
	vcells = vcell('check', 35, [resist_trait, 'Resistance Check using', resist_dc, 'DC'], vcells, 6, check_type)
	vcells = vcell('check', 35, [compare, 'Comparison Check'], vcells, 7, check_type)
	vcells = vcell('check', 35, [variable, 'Variable Check'], vcells, variable_id, check_type)

	vcells = vcell('object', 25, ['Object Destroyed'], vcells)
	
	vcells = vcell('dc', 25, ['Attach DC to Object'], vcells)

	cells = vcell_add('Effect', type, vcells, cells)
	
	cells = cell('Nullify DC', 13, [nullify], cells)
	cells = check_cell('Cumulative', 12, cumulative, cells)
	cells = cell('Linked', 15, [linked], cells)

	cells = circ_cell('Desc', 'Description', 6, description, cells, body)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)
		
def skill_move_post(entry, body, cells):

	speed = entry.speed
	speed_rank = entry.speed_rank
	speed_rank_mod = entry.speed_rank_mod
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
	degree = entry.degree
	circ = entry.circ
	dc = entry.dc
	time = entry.time
	keyword = entry.keyword
	title = entry.title

	title_name = get_name(SkillMoveType, title)
	body['title'] = title_name

	degree = get_keyword(SkillDegree, degree)
	circ = get_keyword(SkillCirc, circ)
	dc = get_keyword(SkillDC, dc)
	time = get_keyword(SkillTime, time)

	speed_trait = trait_select(speed_trait, speed_trait_type)
	distance_rank_trait = trait_select(distance_rank_trait, distance_rank_trait_type)
	distance_unit_trait = trait_select(distance_unit_trait, distance_unit_trait_type)

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
	speed_rank_mod = integer_convert(speed_rank_mod)

	speed_math1 = math_convert(speed_math1)
	speed_math2 = math_convert(speed_math2)
	distance_units = get_name(Unit, distance_units)
	distance_rank_math1 = math_convert(distance_rank_math1)
	distance_rank_math2 = math_convert(distance_rank_math2)
	distance_unit_math1 = math_convert(distance_unit_math1)
	distance_unit_math2 = math_convert(distance_unit_math2)
	distance_math_units = get_name(Unit, distance_math_units)

	direction_select = [{'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]
	direction = selects(direction, direction_select)


	cells = cell('Keyword', 18, [keyword])
	cells = cell('Direction', 12, [direction], cells)

	vcells = vcell('rank', 20, ['Speed Rank', speed_rank])
	speed_rank_mod = add_plus(speed_rank_mod)
	vcells = vcell('rank_mod', 20, [speed_rank_mod, 'Speed Rank'])
	vcells = vcell('mod', 25, [speed_trait, speed_math1, speed_value1, speed_math2, speed_value2], vcells)
	cells = vcell_add('Speed', speed, vcells, cells)
	cells = circ_cell('Description', 'Description', 13, speed_description, cells, body)
	
	vcells = vcell('rank', 20, [distance_rank, 'Rank Distance'])
	vcells = vcell('unit', 20, [distance_value, distance_units], vcells)
	vcells = vcell('unit_math', 25, [distance_unit_trait, distance_unit_math1, distance_unit_value1, distance_unit_math2,  distance_unit_value2, distance_math_units], vcells)
	vcells = vcell('rank_math', 25, [distance_rank_trait, distance_rank_math1, distance_rank_value1, distance_rank_math2, distance_rank_value2], vcells)
	cells = vcell_add('Distance', distance, vcells, cells)
	cells = circ_cell('Description', 'Description', 13, distance_description, cells, body)

	cells = cell('Time', 18, [time], cells)
	cells = cell('Degree', 18, [degree], cells)
	cells = cell('DC', 18, [dc], cells)
	cells = cell('Circumstance', 18, [circ], cells)

	body = send_multiple(title, cells, body)

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
	player_secret = entry.player_secret
	opponent_check = entry.opponent_check
	secret = entry.secret
	recurring = entry.recurring
	multiple = entry.multiple
	recurring_value = entry.recurring_value
	keyword = entry.keyword
	degree = entry.degree
	circ = entry.circ
	dc = entry.dc
	time = entry.time
	degree_check = entry.degree_check
	circ_check = entry.circ_check
	dc_check = entry.dc_check
	time_check = entry.time_check
	degree_value = entry.degree_value
	dc_type = entry.dc_type
	dc_player = entry.dc_player
	circ_value = entry.circ_value
	time_type = entry.time_type
	description = entry.description
	recurring_type = entry.recurring_type

	trait = trait_select(trait, trait_type)
	opponent_trait = trait_select(opponent_trait, opponent_trait_type)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)
	
	recurring_value = get_keyword(SkillTime, recurring_value)
	degree = get_name(SkillDegreeType, degree)
	circ = get_name(SkillCircType, circ)
	dc = get_keyword(SkillDC, dc)
	time = get_keyword(SkillTime, time)
	degree_value = get_keyword(SkillDegree, degree_value)
	dc_type = get_name(SkillDCType, dc_type)
	dc_player = get_keyword(SkillDC, dc_player)
	circ_value = get_keyword(SkillCirc, circ_value)
	time_type = get_name(SkillTimeType, time_type)
	recurring_type = get_name(SkillTimeType, recurring_type)

	frequency_select = [{'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}, {'type': 'player', 'name': 'Player Choice'}]
	frequency = selects(frequency, frequency_select)

	attached_select = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}, {'type': 'with', 'name': 'With Skill Check'}, {'type': 'before_attack', 'name': 'Before Attack Check'}, {'type': 'after_attack', 'name': 'After Attack Check'}, {'type': 'opp_success', 'name': 'Opponent Success'}, {'type': 'success', 'name': 'Player Success'}, {'type': 'opp_fail', 'name': 'Opponent Failure'}, {'type': 'fail', 'name': 'Player Failure'}]
	attached = selects(attached, attached_select)

	cells = cell('Keyword', 15, [keyword])
	cells = cell('When', 13, [attached], cells)
	cells = cell('Frequency', 13, [frequency], cells)
	cells = cell('Player', 12, [trait], cells)
	cells = cell('Mod', 6, [mod], cells)
	cells = cell('Check', 10, [player_check], cells)
	cella = check_cell('Secret', 8, player_secret, cells)

	cells = cell('Opponent', 12, [opponent_trait], cells)
	cells = cell('Mod', 6, [opponent_mod], cells)
	cells = cell('Check', 10, [opponent_check], cells)
	
	cells = check_cell('Secret', 8, secret, cells)

	cells = check_cell('Circ', 6, circ_check, cells, True)
	new_mod = mod_create('Circumstance Modifier', 24)
	new_mod = mod_cell('Group', 7, [circ], new_mod)
	new_mod = mod_cell('Value', 7, [circ_value], new_mod) 
	mod_add(circ_check, new_mod, body)
	
	cells = check_cell('DC', 5, dc_check, cells, True)
	new_mod = mod_create('DC', 5)
	new_mod = mod_cell('Group', 7, [dc_type], new_mod)
	new_mod = mod_cell('Player DC', 13, [dc_player], new_mod)
	new_mod = mod_cell('Opponent DC', 15, [dc], new_mod)
	mod_add(dc_check, new_mod, body)
	
	cells = check_cell('Degree', 10, degree_check, cells, True)
	new_mod = mod_create('Degree', 7)
	new_mod = mod_cell('Value', 8, [degree_value], new_mod)
	new_mod = mod_cell('Group', 7, [degree], new_mod)
	mod_add(degree_check, new_mod, body)
	
	cells = check_cell('Time', 6, time_check, cells, True)
	new_mod = mod_create('Time Effect', 13)
	new_mod = mod_cell('Value', 7, [time], new_mod)
	new_mod = mod_cell('Group', 7, [time_type], new_mod)
	mod_add(time_check, new_mod, body)	


	cells = check_cell('Recurring', 10, recurring, cells, True)
	new_mod = mod_create('Recurring Check', 17)
	new_mod = mod_cell('Every', 15, [recurring_value], new_mod)
	word = string('Time Group', [recurring_type])
	new_mod = mod_cell('Using', 10, [recurring_type, word], new_mod)
	mod_add(recurring, new_mod, body)

	cells = circ_cell('Desc', 'Description', 6, description, cells, body)

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
	recovery_penalty = entry.recovery_penalty
	recovery_incurable = entry.recovery_incurable
	degree = entry.degree
	circ = entry.circ
	dc = entry.dc
	turns = entry.turns
	keyword = entry.keyword
	title = entry.title
	circ_type = entry.circ_type
	degree_type = entry.degree_type
	dc_type = entry.dc_type
	time = entry.time
	mod = entry.mod
	recovery_target = entry.recovery_target


	title_name = get_name(SkillTimeType, title)
	body['title'] = title_name

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
	turns = integer_convert(turns)
	time = integer_convert(time)
	mod = integer_convert(mod)

	degree = get_keyword(SkillDegree, degree)
	circ = get_keyword(SkillCirc, circ)
	dc = get_keyword(SkillDC, dc)
	degree_type = get_name(SkillDegreeType, degree_type)
	circ_type = get_name(SkillCircType, circ_type)
	dc_type = get_name(SkillDCType, dc_type)

	
	time_effect_select = [{'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'effect', 'name': 'Time Effect Happens'}, {'type': 'limit', 'name': 'Time Limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}, {'type': 'recover', 'name': 'Recovery Time'}]
	type = selects(type, time_effect_select)

	
	recovery_select = [{'type': '', 'name': 'Target'}, {'type': 'player', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'either', 'name': 'Any'}]
	recovery_target = selects(recovery_target, recovery_select)

	cells = cell('Keyword', 17, [keyword])
	cells = cell('Time Type', 20, [type], cells)

	vcells = vcell('value', 17, [value, units])
	vcells = vcell('math', 30, [trait, math, math_value, '= Time Rank'], vcells)
	vcells = vcell('rank',35, [rank1, rank1_value, rank_math, rank2, rank2_value], vcells)
	vcells = vcell('gm', 13, ['Set by GM'], vcells)
	vcells = vcell('player', 16, ['Set by Player'], vcells)
	word = int_word('Turns', turns)
	vcells = vcell('turns', 18, [turns, word], vcells)	
	vcells = vcell('instant', 14, ['Instant'], vcells)
	vcells = vcell('perm', 14, ['Permanent'], vcells)
	vcells = vcell('round', 14, ['One Round'], vcells)
	vcells = vcell('next', 14, ['Next Round'], vcells)
	vcells = vcell('maintain', 25, ['While Maintsining Action'], vcells)
	vcells = vcell('scene', 14, ['Scene'], vcells)
	vcells = vcell('turn', 14, ['One Turn'], vcells)
	vcells = vcell('time', 17, ['Time Rank', time], vcells)
	mod = add_plus(mod)
	vcells = vcell('mod', 18, [mod, 'Time Rank'], vcells)
	vcell_add('Time', value_type, vcells, cells)

	cells = cell('Degree', 18, [degree, degree_type], cells)
	cells = cell('DC', 18, [dc, dc_type], cells)
	cells = cell('Circumstance', 18, [circ, circ_type], cells)

	recovery_penalty = add_plus(recovery_penalty)
	word = string('on', [recovery_penalty])
	cells = cell('Recovery', 14, [recovery_penalty, word, recovery_target], cells)
	cells = check_cell('Incurable', 9, recovery_incurable, cells)

	body = send_multiple(title, cells, body)

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
	skill = entry.skill
	light = entry.light


	lasts = get_keyword(SkillTime, lasts)


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

	cells = cell('Duration', 20, [lasts], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)



def skill_levels_post(entry, body, cells):

	skill_id = entry.skill_id
	level_type = entry.level_type
	type_id = entry.type_id
	level = entry.name
	level_effect = entry.level_effect

	title = get_name(LevelType, type_id)
	body['title'] = title


	cells = cell('Level', 20, [level], cells)
	cells = cell('Effect', 75, [level_effect], cells)

	body = send_multiple(type_id, cells, body)

	cells.clear()

	return (body)
