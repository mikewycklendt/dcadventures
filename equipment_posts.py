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

	feature = name(Feature, feature)
	weapon = name(Weapon, weapon)
	equipment = name(Equipment, equipment)
	
	cost = integer_convert(cost)

	'equip' 
	'weapon' 
	'feature'


	body = send(cells, body)
	
	cells.clear()

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
	damaged = selects(damaged, damaged_select)

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
	name = entry.name
	description = entry.description

	cells = cell('Name', 20, [name])
	cells = cell('Description', 80, [description], cells)

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
	skill = name(Skill, skill)
	light = name(Light, light)
	effect = name(EquipEffect, effect)
	feature = name(Feature, feature)

	bonus_active_defense = variable_value('trait', bonus_effect, bonus_active_defense)
	bonus_conflict_defend = variable_value('conflict', bonus_effect, bonus_conflict_defend)
	penalty_active_defense = variable_value('trait', penalty_effect, penalty_active_defense)
	penalty_conflict_defend = variable_value('conflict', penalty_effect, penalty_conflict_defend)

	modifier_trigger = [{'type': '', 'name': 'Trigger'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'cover', 'name': 'Cover'}, {'type': 'conceal', 'name': 'Concealment'}, {'type': 'sense', 'name': 'Sense'}, {'type': 'subsense', 'name': 'Subsense'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'profession', 'name': 'Characters Profession'}, {'type': 'creature', 'name': 'Creature'}, {'type': 'power', 'name': 'Power'}, {'type': 'emotion', 'name': 'Emotion'}, {'type': 'consequence', 'name': 'Consequence'}, {'type': 'range', 'name': 'Range'}, {'type': 'critical', 'name': 'Critical Attempt'}, {'type': 'conflict', 'name': 'Conflict Action'}, {'type': 'maneuver', 'name': 'Maneuver'}, {'type': 'tools', 'name': 'Tool Requirement'}, {'type': 'ranged', 'name': 'Ranged Weapon'}, {'type': 'melee', 'name': 'Melee Weapon'}]

	cells = cell('Feature', 15, [feature])
	cells = cell('Effect', 15, [effect], cells)
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
	
	
	body = send(cells, body)
	
	cells.clear()

	return (body)