from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
from models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait



def equip_belt_post(entry, body, cells):

	equip_id = entry.equip_id
	feature = entry.feature
	weapon = entry.weapon
	equipment = entry.equipment
	cost = entry.cost
	belt_item_type = entry.belt_item_type

	feature = name(Feature, feature)
	weapon = name(Weapon, weapon)
	equipment = name(Equipment, equipment)
	
	cost = str(cost)


	vcells = vcell('equip', 30, [equipment])
	vcells = vcell('weapon', 30, [weapon], vcells)
	vcells = vcell('feature', 30, [feature], vcells)
	cells = vcell_add('Item', belt_item_type, vcells, cells) 
	cells = cell('Cost', 10, [cost], cells)
	body = send(cells, body)
	
	cells.clear()

	print('\n\n')
	print(cost)
	print('\n')

	return (body)

def equip_check_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	when = entry.when
	skill_type = entry.skill_type
	skill = entry.skill
	check_type = entry.check_type
	action = entry.action
	action_time = entry.action_time

	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)
	check_type = name(Check, check_type)
	action = name(Action, action)
	
	when_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]
	when = selects(when, when_select)

	cells = cell('Effect', 15, [effect])
	cells = cell('Feature', 15, [feature], cells)
	cells = cell('When', 14, [when], cells)
	cells = cell('Skill', 15, [skill_type], cells)
	cells = cell('Enhanced Skill', 20, [skill], cells)
	cells = cell('Check', 14, [check_type], cells)
	cells = cell('Action', 15, [action], cells)
	cells = check_cell('Action Time', 12, action_time, cells)
	

	body = send(cells, body)
	
	cells.clear()

	return (body)
	
def equip_damaged_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	damage = entry.damage
	skill_type = entry.skill_type
	skill = entry.skill
	toughness = entry.toughness
	penalty = entry.penalty


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)

	damage = name(Descriptor, damage)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)

	toughness = integer_convert(toughness)

	damaged_select = [{'type': '', 'name': 'Damaged Effect'}, {'type': 'feature', 'name': 'Loses a Feature'}, {'type': 'circ', 'name': '-1 Circumstance'}]
	penalty = selects(penalty, damaged_select)

	cells = cell('Effect', 15, [effect])
	cells = cell('Feature', 15, [feature], cells)
	cells = cell('Damage', 25, [damage], cells)
	cells = cell('Skill', 18, [skill_type], cells)
	cells = cell('Enhanced Skill', 20, [skill], cells)
	cells = cell('Toughness', 12, [toughness], cells)
	cells = cell('Penalty', 17, [penalty], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_descriptor_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	descriptor = entry.descriptor


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	descriptor = name(Descriptor, descriptor)
	
	cells = cell('Effect', 15, [effect])
	cells = cell('Feature', 15, [feature], cells)
	cells = cell('Descriptor', 25, [descriptor], cells)


	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_effect_post(entry, body, cells):

	equip_id = entry.equip_id
	name = entry.name
	description = entry.description

	cells = cell('Name', 20, [name])
	cells = cell('Description', 80, [description], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_feature_post(entry, body, cells):

	equip_id = entry.equip_id
	feature_name = entry.name
	description = entry.description
	feature = entry.feature

	feature = name(Feature, feature)

	if feature_name == '':
		cells = cell('Feature', 20, [feature])
	else:
		cells = cell('Feature', 20, [feature_name], cells)
	cells = cell('Description', 60, [description], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_limits_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	time = entry.time
	time_units = entry.time_units
	range = entry.range
	range_units = entry.range_units
	extend = entry.extend
	extendable = entry.extendable
	time_capacity = entry.time_capacity
	time_capacity_units = entry.time_capacity_units
	capacity = entry.capacity
	item = entry.item
	ammo = entry.ammo
	fuel = entry.fuel
	area_long = entry.area_long
	area_wide = entry.area_wide
	area_units = entry.area_units
	recharge = entry.recharge
	refill = entry.refill
	uses = entry.uses
	light = entry.light
	internet = entry.internet
	needs_interneT = entry.needs_internet


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	time_units = name(Unit, time_units)
	range_units = name(Unit, range_units)
	time_capacity_units = name(Unit, time_capacity_units)
	area_units = name(Unit, area_units)
	light = name(Light, light)
	
	
	time = integer_convert(time)
	range = integer_convert(range)
	time_capacity = integer_convert(time_capacity)
	capacity = integer_convert(capacity)
	area_long = integer_convert(area_long)
	area_wide = integer_convert(area_wide)
	uses = integer_convert(uses)

	cells = cell('Effect', 15, [effect])
	cells = cell('Feature', 15, [feature], cells)

	
	cells = cell('Duration', 16, [time, time_units], cells)
	cells = cell('Range', 16, [range, range_units], cells)
	cells = cell('Time Capacity', 18, [time_capacity, time_capacity_units], cells)
	cells = cell('Capacity', 18, [capacity, item], cells)
	word = string('x', [area_long, area_wide])
	cells = cell('Area', 18, [area_long, word, area_wide, area_units], cells)
	cells = cell('Uses', 6, [uses], cells)
	cells = cell('Lighting', 14, [light], cells)
	cells = check_cell('Extendable', 13, extendable, cells)
	cells = check_cell('Extends', 8, extend, cells)
	cells = check_cell('Ammo', 7, ammo, cells)
	cells = check_cell('Fuel', 6, fuel, cells)
	cells = check_cell('Recharges', 10, recharge, cells)
	cells = check_cell('Refills', 9, refill, cells)
	cells = check_cell('Internet', 9, internet, cells)
	cells = check_cell('Needs Internet', 14, needs_interneT, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def equip_modifiers_post(entry, body, cells):

	equip_id = entry.equip_id
	feature = entry.feature
	effect = entry.effect
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
	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)

	bonus_active_defense = variable_value('trait', bonus_effect, bonus_active_defense)
	bonus_conflict_defend = variable_value('conflict', bonus_effect, bonus_conflict_defend)
	penalty_active_defense = variable_value('trait', penalty_effect, penalty_active_defense)
	penalty_conflict_defend = variable_value('conflict', penalty_effect, penalty_conflict_defend)

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	cells = cell('Feature', 11, [feature])
	cells = cell('Effect', 11, [effect], cells)
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



def equip_opposed_post(entry, body, cells):

	equip_id = entry.equip_id
	effect = entry.effect
	feature = entry.feature
	dc = entry.dc
	skill_type = entry.skill_type
	skill = entry.skill
	check = entry.check
	when = entry.when
	condition1 = entry.condition1
	condition2 = entry.condition2


	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)
	skill_type = name(Skill, skill_type)
	skill = name(SkillBonus, skill)
	check = name(Check, check)
	
	dc = integer_convert(dc)

	when_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Use'}, {'type': 'after', 'name': 'After Use'}]
	when = selects(when, when_select)
	
	cells = cell('Effect', 15, [effect])
	cells = cell('Feature', 15, [feature], cells)
	cells = cell('DC', 6, [dc], cells)
	cells = cell('Skill', 16, [skill_type], cells)
	cells = cell('Enhanced Skill', 20, [skill], cells)
	cells = cell('Check', 14, [check], cells)
	cells = cell('Required Condition', 18, [condition1], cells)
	cells = cell('Result Condition', 18, [condition2], cells)
	cells = cell('When', 11, [when], cells)
	
	body = send(cells, body)
	
	cells.clear()

	return (body)