
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
from db.linked_models import PowerCircType, PowerCheckType, PowerOpposedType, PowerDCType, PowerDegreeType, PowerMoveType, PowerRangedType, PowerTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects, preset_convert, db_multiple, id_multiple, get_multiple
from functions.create import name_exist, db_insert, capitalize
from functions.linked import link_add, delete_link, level_add, delete_level, linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import send_multiple, one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string, circ_cell, arrow_cell

from create_functions.power_create import power_check, rule_check, rule_select, cost_check, extra_cost, extra_check, extra_convert, field_cost, multiple_cost, variable_cost, sense_cost, power_rules, valid_extra, ranks_error, ranks_function, get_ranks, get_cost

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy


db = SQLAlchemy()


def change_action_post(entry, body, cells):
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	action = entry.action
	mod = entry.mod
	objects = entry.objects
	circumstance = entry.circumstance

	extra = extra_name(extra_id)
	action = name(Action, action)

	mod = integer_convert(mod)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Action', 17, [action], cells)
	cells = cell('Modifier', 12, [mod], cells)
	cells = check_cell('No Check', 9, objects, cells)
	cells = cell('Circumstance', 40, [circumstance], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def character_post(entry, body, cells):
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	value = entry.value
	increase = entry.increase
	limited = entry.limited
	reduced = entry.reduced
	limbs = entry.limbs
	carry = entry.carry
	sustained = entry.sustained
	permanent = entry.permanent
	points = entry.points
	appear = entry.appear
	insubstantial = entry.insubstantial
	weaken = entry.weaken
	weaken_type = entry.weaken_type
	weaken_trait_type = entry.weaken_trait_type
	weaken_trait = entry.weaken_trait
	weaken_broad = entry.weaken_broad
	weaken_descriptor = entry.weaken_descriptor
	weaken_simultaneous = entry.weaken_simultaneous
	limited_by = entry.limited_by
	limited_other = entry.limited_other
	limited_emotion = entry.limited_emotion
	limited_emotion_other = entry.limited_emotion_other
	reduced_trait_type = entry.reduced_trait_type
	reduced_trait = entry.reduced_trait
	reduced_value = entry.reduced_value
	reduced_full = entry.reduced_full
	limbs_continuous = entry.limbs_continuous
	limbs_sustained = entry.limbs_sustained
	limbs_distracting = entry.limbs_distracting
	limbs_projection = entry.limbs_projection
	carry_capacity = entry.carry_capacity
	points_value = entry.points_value
	points_trait_type = entry.points_trait_type
	points_trait = entry.points_trait
	points_descriptor = entry.points_descriptor
	appear_target = entry.appear_target
	appear_description = entry.appear_description
	insub_type = entry.insub_type
	insub_description = entry.insub_description
	cost = entry.cost
	ranks = entry.ranks

	cost = get_cost(cost, ranks, extra_id)

	trait = trait_select(trait, trait_type)
	weaken_trait = trait_select(weaken_trait, weaken_trait_type)
	reduced_trait = trait_select(reduced_trait, reduced_trait_type)
	points_trait = trait_select(points_trait, points_trait_type)

	extra = extra_name(extra_id)
	weaken_descriptor = descriptor_name(weaken_descriptor)
	points_descriptor = descriptor_name(points_descriptor)
	limited_emotion = name(Emotion, limited_emotion)

	limited_select = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]
	limited_by = selects(limited_by, limited_select)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	appear_target =  selects(appear_target, targets_select)

	insub_select = [{'type': '', 'name': 'Insubstantial Type'}, {'type': 'fluid', 'name': 'Fluid'}, {'type': 'gas', 'name': 'Gaseous'}, {'type': 'energy', 'name': 'Energy'}, {'type': 'incorp', 'name': 'Incorporeal'}]
	insub_type = selects(insub_type, insub_select)
	
	traits_select = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_power', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}]
	weaken_broad = selects(weaken_broad, traits_select)

	value = integer_convert(value)
	increase = integer_convert(increase)
	reduced_value = integer_convert(reduced_value)
	carry_capacity = integer_convert(carry_capacity)
	points_value = integer_convert(points_value)



	
	cells = cell('Extra', 15, [extra])
	cells = cell('Trait', 14, [trait], cells)
	wid = 8
	perrank = string('Per', increase)
	rank = string('Rank', increase)
	wid = width(wid, 8, increase)
	cells = cell('Increase', wid, [value, perrank, increase, rank], cells)

	cells = check_cell('Limited', 8, limited, cells, True)
	new_mod = mod_create('Limited', 12)
	new_mod = mod_cell('Limited While:', 15, [limited_by], new_mod)
	new_mod = mod_cell('Emotion:', 12, [limited_emotion], new_mod)
	body = mod_add(limited, new_mod, body)

	cells = check_cell('Reduced', 9, reduced, cells, True)
	new_mod = mod_create('Reduced Trait', 16)
	new_mod = mod_cell('Trait:', 8, [reduced_trait], new_mod)
	new_mod = mod_cell('Reduced By:', 12, [reduced_value], new_mod)
	new_mod = mod_cell('Normal Strength:', 16, [reduced_full], new_mod)
	body = mod_add(reduced, new_mod, body)

	cells = check_cell('Limbs', 8, limbs, cells, True)
	new_mod = mod_create('Extra Limbs', 14)
	new_mod = mod_cell('Continuous:', 11, [limbs_continuous], new_mod)
	new_mod = mod_cell('Sustained:', 10, [limbs_sustained], new_mod)
	new_mod = mod_cell('Distracting:', 12, [limbs_distracting], new_mod)
	new_mod = mod_cell('Projection:', 12, [limbs_projection], new_mod)
	body = mod_add(limbs, new_mod, body)

	cells = check_cell('Carry', 7, carry, cells, True)
	new_mod = mod_create('Extra Carry Capacity:', 25)
	sizerank = string('- Size Rank', [carry_capacity])
	new_mod = mod_cell('Maximum Size Rank', 22, [carry_capacity, sizerank], new_mod)
	body = mod_add(carry, new_mod, body)

	cells = check_cell('Sustained', 11, sustained, cells)
	cells = check_cell('Permanent', 10, permanent, cells)

	cells = check_cell('Points', 8, points, cells, True)
	new_mod = mod_create('Hero Points', 14)
	new_mod = mod_cell('Affected Trait', 18, [points_trait], new_mod)
	new_mod = mod_cell('Points:', 9, [points_value], new_mod)
	new_mod = mod_cell('Descriptor:', 12, [points_descriptor], new_mod)
	body = mod_add(points, new_mod, body)

	cells = check_cell('Appearance', 14, appear, cells, True)
	new_mod = mod_create('Alters Appearance', 20)
	new_mod = mod_cell('Target:', 7, [appear_target], new_mod)
	new_mod = mod_cell('Description:', 11, [appear_description], new_mod)
	body = mod_add(appear, new_mod, body)

	cells = check_cell('Insubstantial', 14, insubstantial, cells, True)
	new_mod = mod_create('Insubstantial', 16)
	new_mod = mod_cell('Type:', 6, [insub_type], new_mod)
	new_mod = mod_cell('Description:', 11, [insub_description], new_mod)
	body = mod_add(insubstantial, new_mod, body)

	cells = check_cell('Weaken', 8, weaken, cells, True)
	weaken_select = [{'type': 'trait', 'name': 'Specific', 'w': 12}, {'type': 'type', 'name': 'Broad Trait', 'w': 16}, {'type': 'descriptor', 'name': 'Broad Descriptor', 'w': 20}]
	new_mod = mod_create('Weaken', 10, weaken_type, weaken_select)
	value = 'trait'
	new_mod = mod_cell('Trait:', 8, [weaken_trait], new_mod, value)	
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	value = 'type'
	new_mod = mod_cell('Trait Type:', 12, [weaken_broad], new_mod, value)
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Descriptor:', 8, [weaken_descriptor], new_mod, value)
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	body = mod_add(weaken, new_mod, body)

	cells = cell('Cost/Rank', 10, [cost], cells)
	cells = cell('Ranks', 8, [ranks], cells)

	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	body = send(cells, body)

	cells.clear()

	return (body)

def create_post(entry, body, cells):
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	solidity = entry.solidity
	visibility = entry.visibility
	complexity = entry.complexity
	volume = entry.volume
	toughness = entry.toughness
	mass = entry.mass
	damageable = entry.damageable
	maintained = entry.maintained
	repairable = entry.repairable
	moveable = entry.moveable
	stationary = entry.stationary
	trap = entry.trap
	ranged = entry.ranged
	weapon = entry.weapon
	support = entry.support
	real = entry.real
	cover = entry.cover
	conceal = entry.conceal
	incoming = entry.incoming
	outgoing = entry.outgoing
	transform = entry.transform
	transform_type = entry.transform_type
	transform_start_mass = entry.transform_start_mass
	transfom_mass = entry.transfom_mass
	transform_start_descriptor = entry.transform_start_descriptor
	transform_end_descriptor = entry.transform_end_descriptor
	move_player = entry.move_player
	move_check = entry.move_check
	move_opponent_check = entry.move_opponent_check
	move_opposed = entry.move_opposed
	trap_check = entry.trap_check
	trap_opposed = entry.trap_opposed
	trap_resist = entry.trap_resist
	trap_escape = entry.trap_escape
	weapon_damage = entry.weapon_damage
	support_strength = entry.support_strength
	support_strengthen = entry.support_strengthen
	support_action = entry.support_action
	support_action_rounds = entry.support_action_rounds
	support_effort = entry.support_effort
	support_effort_rounds = entry.support_effort_rounds
	cost = entry.cost
	ranks = entry.ranks
	ranged_damage = entry.ranged_damage
	ranged_check = entry.ranged_check

	cost = get_cost(cost, ranks, extra_id)

	move_check = get_keyword(PowerCheck, move_check)
	move_opposed = get_keyword(PowerOpposed, move_opposed)
	trap_check = get_keyword(PowerCheck, trap_check)
	trap_opposed = get_keyword(PowerOpposed, trap_opposed)
	trap_resist = get_keyword(PowerCheck, trap_resist)
	ranged_damage = get_keyword(PowerDamage, ranged_damage)
	ranged_check = get_keyword(PowerCheck, ranged_check)
	weapon_damage = get_keyword(PowerDamage, weapon_damage)
	
	trap_trait = trait_select(trap_trait, trap_trait_type)
	trap_resist_trait = trait_select(trap_resist_trait, trap_resist_check)

	extra = extra_name(extra_id)
	complexity = name(Complex, complexity)
	transform_start_descriptor = descriptor_name(transform_start_descriptor)
	transform_end_descriptor = descriptor_name(transform_end_descriptor)

	solidity_select = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]
	solidity = selects(solidity, solidity_select)

	visibility_select = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]
	visibility = selects(visibility, visibility_select)

	transform_select = [{'type': '', 'name': 'Transform Type'}, {'type': 'one', 'name': 'One Substance to One Substance'}, {'type': 'result', 'name': 'Group to Single Result'}, {'type': 'broad', 'name': 'Broad Group to Broad Group'}, {'type': 'any', 'name': 'Any Material into Anything Else'}]
	transform_type = selects(transform_type, transform_select)

	moveable_select = [{'type': '', 'name': 'Moveable With'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]
	move_player = selects(move_player, moveable_select)

	against_select = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]
	trap_type = selects(trap_type, against_select)

	object_damage_select = [{'type': '', 'name': 'Damage Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'effect', 'name': 'Effect Rank'}, {'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}, {'type': 'ability', 'name': 'Player Ability'}]
	ranged_damage_type = selects(ranged_damage_type, object_damage_select)

	weapon_damage_type = selects(weapon_damage_type, object_damage_select)

	volume = integer_convert(volume)
	toughness = integer_convert(toughness)
	mass = integer_convert(mass)
	transform_start_mass = integer_convert(transform_start_mass)
	transfom_mass = integer_convert(transfom_mass)
	move_opponent_rank = integer_convert(move_opponent_rank)
	trap_dc = integer_convert(trap_dc)
	trap_resist_dc = integer_convert(trap_resist_dc)

	support_strength = integer_convert(support_strength)
	support_action = integer_convert(support_action)
	support_action_rounds = integer_convert(support_action_rounds)
	support_effort = integer_convert(support_effort)
	support_effort_rounds = integer_convert(support_effort_rounds)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Solidity', 11, [solidity], cells)
	cells = cell('Visibility', 9, [visibility], cells)
	cells = cell('Complexity', 12, [complexity], cells)
	cells = cell('Volume', 8, [volume], cells)
	cells = cell('Toughness', 11, [toughness], cells)
	cells = cell('Mass', 9, [mass], cells)
	cells = check_cell('Damageable', 12, damageable, cells)
	cells = check_cell('Maintained', 12, maintained, cells)
	cells = check_cell('Repairable', 12, repairable, cells)
	
	cells = check_cell('Moveable', 10, moveable, cells, True)
	new_mod = mod_create('Moveable', 13)
	new_mod = mod_cell('Player Check:', 14, [move_check], new_mod)
	new_mod = mod_cell('Opponent Check:', 16, [move_opposed], new_mod)
	body = mod_add(moveable, new_mod, body)

	cells = check_cell('Stationary', 13, stationary, cells, True)
	new_mod = mod_create('Stationary', 14)
	new_mod = mod_cell('Player Check:', 14, [move_check], new_mod)
	new_mod = mod_cell('Opponent Check:', 16, [move_opposed], new_mod)
	body = mod_add(stationary, new_mod, body)

	cells = check_cell('Trap', 7, trap, cells, True)
	new_mod = mod_create('Trap', 6)
	new_mod = mod_cell('Check to Trap:', 15, [trap_check], new_mod)
	new_mod = mod_cell('Check to Hold:', 15, [trap_resist], new_mod)
	new_mod = mod_cell('Check to Escape:', 15, [trap_opposed], new_mod)
	body = mod_add(trap, new_mod, body)

	cells = check_cell('Ranged', 8, ranged, cells, True)
	new_mod = mod_create('Ranged', 9)
	new_mod = mod_cell('Check:', 8, [ranged_check], new_mod)
	new_mod = mod_cell('Damage:', 12, [ranged_damage], new_mod)
	body = mod_add(ranged, new_mod, body)

	cells = check_cell('Weapon', 9, weapon, cells, True)
	new_mod = mod_create('Weapon', 10)
	new_mod = mod_cell('Damage:', 8, [weapon_damage], new_mod)
	body = mod_add(weapon, new_mod, body)

	cells = check_cell('Support', 9, support, cells, True)
	new_mod = mod_create('Supports Weight', 19)
	new_mod = mod_cell('Strength Rank:', 14, [support_strength], new_mod)
	new_mod = mod_cell('Strength with Action:', 14, [support_action], new_mod)
	new_mod = mod_cell('Rounds:', 7, [support_action_rounds], new_mod)
	new_mod = mod_cell('With Extra Efffort:', 14, [support_effort], new_mod)
	new_mod = mod_cell('Extra Effort Rounds:', 14, [support_effort_rounds], new_mod)
	body = mod_add(support, new_mod, body)

	cells = check_cell('Appears Real', 15, real, cells)
	cells = check_cell('Cover', 8, cover, cells)
	cells = check_cell('Conceal', 8, conceal, cells)
	cells = check_cell('Blocks Incoming', 16, incoming, cells)
	cells = check_cell('Blocks Outgoing', 16, outgoing, cells)
	cells = check_cell('Transform', 10, transform, cells, True)
	new_mod = mod_create('Transform', 12)
	new_mod = mod_cell('Type', 5, [transform_type], new_mod)
	word = string('Per Rank', [transform_start_mass, transfom_mass])
	new_mod = mod_cell('Mass', 6, [transform_start_mass, transfom_mass, word], new_mod)
	new_mod = mod_cell('Start Descriptor', 17, [transform_start_descriptor], new_mod)
	new_mod = mod_cell('End Descriptor', 15, [transform_end_descriptor], new_mod)
	body = mod_add(transform, new_mod, body)

	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	body = send(cells, body)

	cells.clear()

	return (body)


def damage_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	strength = entry.strength
	damage_type = entry.damage_type
	descriptor = entry.descriptor
	keyword = entry.keyword
	value_type = entry.value_type
	math = entry.math

	trait = trait_select(trait, trait_type)

	extra = extra_name(extra_id)
	damage_type = get_multiple(Descriptor, damage_type)
	descriptor = get_multiple(PowerDes, descriptor)

	math = math_convert(math)

	mod = integer_convert(mod)
	damage_type = integer_convert(damage_type)

	damage_value = [{'type': '', 'name': 'Damage Dealt'}, {'type': 'rank', 'name': 'Rank Value'}, {'type': 'check', 'name': 'Checked Rank'}, {'type': 'value', 'name': 'Flat Value'}]
	value_type = selects(value_type, damage_value)

	cells = cell('Keyword', 15, [keyword])
	cells = cell('Extra', 15, [extra], cells)
	cells = cell('Damage', 25, [trait, math, mod], cells)
	cells = cell('Dealt By', 16, [value_type], cells)
	cells = check_cell('Strength Based', 16, strength, cells)
	cells = circ_cell('Damage Type', 'Damage Type', 13, damage_type, cells, body)
	cells = circ_cell('Descriptor', 'Descriptor', 12, descriptor, cells, body)

	body = send(cells, body)

	cells.clear()

	return (body)

def defense_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	defense = entry.defense
	use = entry.use
	mod = entry.mod
	roll = entry.roll
	outcome = entry.outcome
	dodge = entry.dodge
	fortitude = entry.fortitude
	parry = entry.parry
	toughness = entry.toughness
	will = entry.will
	resist_area = entry.resist_area
	resist_perception = entry.resist_perception
	reflect = entry.reflect
	immunity = entry.immunity
	reflect_action = entry.reflect_action
	reflect_check = entry.reflect_check
	reflect_dc = entry.reflect_dc
	reflect_opposed_trait_type = entry.reflect_opposed_trait_type
	reflect_opposed_trait = entry.reflect_opposed_trait
	reflect_resist_trait_type = entry.reflect_resist_trait_type
	reflect_resist_trait = entry.reflect_resist_trait
	immunity_type = entry.immunity_type
	immunity_trait_type = entry.immunity_trait_type
	immunity_trait = entry.immunity_trait
	immunity_descriptor = entry.immunity_descriptor
	immunity_damage = entry.immunity_damage
	immunity_rule = entry.immunity_rule
	cover_check = entry.cover_check
	cover_type = entry.cover_type
	
	reflect_opposed_trait = trait_select(reflect_opposed_trait, reflect_opposed_trait_type)
	reflect_resist_trait = trait_select(reflect_resist_trait, reflect_resist_trait_type)
	immunity_trait = trait_select(immunity_trait, immunity_trait_type)
	
	extra = extra_name(extra_id)
	immunity_descriptor = descriptor_name(immunity_descriptor)

	defense = get_name(Defense, defense)
	reflect_action = get_name(Action, reflect_action)
	reflect_check = get_name(Check, reflect_check)
	immunity_damage = get_name(Descriptor, immunity_damage)
	cover_type = get_name(Cover, cover_type)

	game_rule_select = [{'type': '', 'name': 'Game Rule'}, {'type': 'critical', 'name': 'Critical Hits'}, {'type': 'suffocate', 'name': 'Suffocation'}, {'type': 'starve', 'name': 'Starvation'}, {'type': 'thirst', 'name': 'Thirst'}, {'type': 'sleep', 'name': 'Need for Sleep'}, {'type': 'fall', 'name': 'Falling'}]
	immunity_rule = selects(immunity_rule, game_rule_select)

	mod = integer_convert(mod)
	roll = integer_convert(roll)
	reflect_dc = integer_convert(reflect_dc)

	use_type_select = [{'type': '', 'name': 'Use Type'}, {'type': 'add', 'name': 'Add to'}, {'type': 'replace', 'name': 'In Place of'}, {'type': 'gm', 'name': 'GM Choice'}]
	use = selects(use, use_type_select)

	cover_select = [{'type': '', 'name': 'Cover Type'}, {'type': 'partial', 'name': 'Partial Cover'}, {'type': 'total', 'name': 'Total Cover'}]
	cover_type = selects(cover_type, cover_select)

	outcome_select = [{'type': '', 'name': ''}, {'type': '<', 'name': 'Lower'}, {'type': '>', 'name': 'Higher'}]
	outcome = selects(outcome, outcome_select)

	cells.clear()

	cells = cell('Extra', 15, [extra])
	cells = cell('Defense', 12, [defense])
	cells = cell('Use', 10, [use], cells)
	cells = cell('Mod', 7, [mod], cells)
	word = string('or', [roll, outcome])
	print('\n\n\n')
	print(word)
	print(roll)
	print(outcome)
	cells = cell('Roll', 10, [roll, word, outcome], cells)
	cells = check_cell('Dodge', 7, dodge, cells)
	cells = check_cell('Fortitude', 10, fortitude, cells)
	cells = check_cell('Parry', 7, parry, cells)
	cells = check_cell('Toughness', 10, toughness, cells)
	cells = check_cell('Will', 5, will, cells)
	cells = check_cell('Resists Area', 12, resist_area, cells)
	cells = check_cell('Resists Perception', 19, resist_perception, cells)
	
	cells = check_cell('Reflect', 10, reflect, cells, True)
	select = [{'type': 1, 'name': 'Skill Check', 'w': 10}, {'type': 2, 'name': 'Opposed Check', 'w': 15}, {'type': 3, 'name': 'Routine Check', 'w': 15}, {'type': 4, 'name': 'Team Check', 'w': 15}, {'type': 5, 'name': 'Attack Check', 'w': 15}, {'type': 6, 'name': 'Resistance Check', 'w': 15}, {'type': 7, 'name': 'Comparison Check', 'w': 15}]
	new_mod = mod_create('Reflects Attacks', 17, reflect_check, select)

	value = 1
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('DC:', 7, [reflect_dc], new_mod, value)
	value = 2
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('Opposed By:', 15, [reflect_opposed_trait], new_mod, value)
	value = 3
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 4
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 5
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 6
	new_mod = mod_cell('Action Type', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('Resisted By', 15, [reflect_resist_trait], new_mod, value)
	body = mod_add(reflect, new_mod, body)
	value = 7
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	cells = check_cell('Immunity', 10, immunity, cells, True)
	select =[{'type': 'trait', 'name': 'Immune From Trait', 'w': 18}, {'type': 'damage', 'name': 'Immune From Damage Type', 'w': 25}, {'type': 'descriptor', 'name': 'Immune From Descriptor', 'w': 25}, {'type': 'rule', 'name': 'Immune From Game Rule', 'w': 25}]
	new_mod = mod_create('Immunity', 17, immunity_type, select)
	value = 'trait'
	new_mod = mod_cell('Trait:', 15, [immunity_trait], new_mod, value)
	value = 'damage'
	new_mod = mod_cell('Damage:', 10, [immunity_damage], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Descriptor:', 15, [immunity_descriptor], new_mod, value)
	value = 'rule'
	new_mod = mod_cell('Rule:', 10, [immunity_rule], new_mod, value)
	body = mod_add(immunity, new_mod, body)	

	cells = check_cell('Cover', 7, cover_check, cells, True)
	new_mod = mod_create('Provides Cover', 20)
	new_mod = mod_cell('Cover Type', 18, [cover_type], new_mod)
	body = mod_add(cover_check, new_mod, body)
		

	body = send(cells, body)

	cells.clear()

	return (body)

	


def environment_post(entry, body, cells):
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	radius = entry.radius
	distance = entry.distance
	rank = entry.rank
	condition_check = entry.condition_check
	impede = entry.impede
	conceal = entry.conceal
	visibility = entry.visibility
	selective = entry.selective
	immunity = entry.immunity
	immunity_type = entry.immunity_type
	temp_type = entry.temp_type
	immunity_extremity = entry.immunity_extremity
	immunity_environment = entry.immunity_environment
	no_penalty = entry.no_penalty
	no_circumstance = entry.no_circumstance
	immunity_other = entry.immunity_other
	condition_temp_type = entry.condition_temp_type
	temp_extremity = entry.temp_extremity
	move_nature = entry.move_nature
	move_speed = entry.move_speed
	move_cost_circ = entry.move_cost_circ
	move_other = entry.move_other
	conceal_type = entry.conceal_type
	visibility_trait_type = entry.visibility_trait_type
	visibility_trait = entry.visibility_trait
	visibility_mod = entry.visibility_mod
	cost = entry.cost
	ranks = entry.ranks

	cost = get_cost(cost, ranks, extra_id)

	visibility_trait = trait_select(visibility_trait, visibility_trait_type)

	extra = extra_name(extra_id)
	immunity_environment = get_name(Environment, immunity_environment)
	move_nature = get_name(Nature, move_nature)

	temp_type_select = [{'type': '', 'name': 'Type'}, {'type': 'all', 'name': 'All'}, {'type': 'cold', 'name': 'Cold'}, {'type': 'heat', 'name': 'Heat'}, {'type': 'pressure', 'name': 'High Pressure'}, {'type': 'radiation', 'name': 'Radiation'}, {'type': 'vaccum', 'name': 'Vaccuum'}]
	temp_type = selects(temp_type, temp_type_select)

	extremity_select = [{'type': '', 'name': 'Extremity'}, {'type': 'intense', 'name': 'Intense'}, {'type': 'extreme', 'name': 'Extreme'}]
	immunity_extremity = selects(immunity_extremity, extremity_select)

	condition_temp_type = selects(condition_temp_type, temp_type_select)

	temp_extremity = selects(temp_extremity, extremity_select)

	nature_select = [{'type': '', 'name': 'Nature'}, {'type': 'ice', 'name': 'Ice'}, {'type': 'rain', 'name': 'Rain'}, {'type': 'snow', 'name': 'Snow'}, {'type': 'wind', 'name': 'Wind'}, {'type': 'other', 'name': 'Other'}]
	move_nature = selects(move_nature, nature_select)

	conceal_type_select = [{'type': 'reduce', 'name': 'Reduce'}, {'type': 'eliminate', 'name': 'Eliminate'}]
	conceal_type = selects(conceal_type, conceal_type_select)

	radius = integer_convert(radius)
	distance = integer_convert(distance)
	rank = integer_convert(rank)
	move_speed = integer_convert(move_speed)
	visibility_mod = integer_convert(visibility_mod)


	
	cells = cell('Extra', 15, [extra])
	cells = cell('Start Radius', 16, [radius], cells)
	word = string('Per', [distance, rank])
	word2 = string('Rank', [distance, rank])
	cells = cell('Radius', 14, [distance, word, rank, word2], cells)
	cells = check_cell('Condition', 9, condition_check, cells, True)
	new_mod = mod_create('Temperature Condition', 25)
	new_mod = mod_cell('Temperature Type:', 20, [condition_temp_type], new_mod)
	new_mod = mod_cell('Extremity:', 10, [temp_extremity], new_mod)
	body = mod_add(condition_check, new_mod, body)

	cells = check_cell('Impede', 7, impede, cells, True)
	new_mod = mod_create('Impede Movement', 20)
	new_mod = mod_cell('Nature Type:', 12, [move_nature], new_mod)
	new_mod = mod_cell('Other:', 7, [move_other], new_mod)
	new_mod = mod_cell('Speed:', 7, [move_speed], new_mod)
	new_mod = mod_cell('Surface Modifier:', 18, [move_cost_circ], new_mod)
	body = mod_add(impede, new_mod, body)

	cells = check_cell('Counter Conceal', 17, conceal, cells, True)
	new_mod = mod_create('Counters Concealment', 23)
	new_mod = mod_cell('Type:', 7, [conceal_type], new_mod)
	body = mod_add(conceal, new_mod, body)

	cells = check_cell('Visibility', 13, visibility, cells, True)
	new_mod = mod_create('Lessen Visibility', 22)
	new_mod = mod_cell('Trait:', 7, [visibility_trait], new_mod)
	new_mod = mod_cell('Modifier:', 11, [visibility_mod], new_mod)
	body = mod_add(visibility, new_mod, body)

	cells = check_cell('Selective', 10, selective, cells)
	cells = check_cell('Immunity', 11, immunity, cells, True)
	environment_immunity_select = [{'type': 'environment', 'name': 'Environment', 'w': 13}, {'type': 'condition', 'name': 'Condition', 'w': 12}]
	new_mod = mod_create('Immunity', 12, immunity_type, environment_immunity_select)
	value = 'environment'
	new_mod = mod_cell('Type', 6, [immunity_environment], new_mod, value)
	new_mod = mod_cell('No Penalty', 13, [no_penalty], new_mod, value)
	new_mod = mod_cell('No Circumstance', 16, [no_circumstance], new_mod, value)
	value = 'condition'
	new_mod = mod_cell('Type', 6, [temp_type], new_mod, value)
	new_mod = mod_cell('Extremity', 10, [immunity_extremity], new_mod, value)
	body = mod_add(immunity, new_mod, body)

	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	body = send(cells, body)

	cells.clear()

	return (body)


def levels_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	level_type = entry.level_type
	level = entry.name
	level_effect = entry.level_effect

	extra = extra_name(extra_id)

	cells = cell('Extra', 15, [extra])
	cells = cell('Level', 17, [level], cells)
	cells = cell('Effect', 58, [level_effect], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def minion_post(entry, body, cells):
		
	power_id = entry.power_id
	extra_id = entry.extra_id
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
	attitude_attitude = entry.attitude_attitude
	attitude_type = entry.attitude_type
	attitude_trait_type = entry.attitude_trait_type
	attitude_trait = entry.attitude_trait
	resitable_check = entry.resitable_check
	resitable_dc = entry.resitable_dc
	multiple_value = entry.multiple_value
	horde = entry.horde

	attitude_trait = trait_select(attitude_trait, attitude_trait_type)

	extra = extra_name(extra_id)
	condition = get_name(Condition, condition)
	player_condition = get_name(Condition, player_condition)
	attitude_type = get_name(LevelType, attitude_type)
	attitude_attitude = get_name(Levels, attitude_attitude)
	resitable_check = get_name(Defense, resitable_check)

	minion_type_select = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]
	variable_type = selects(variable_type, minion_type_select)

	points = integer_convert(points)
	sacrifice_cost = integer_convert(sacrifice_cost)
	resitable_dc = integer_convert(resitable_dc)
	multiple_value = integer_convert(multiple_value)

	cells = cell('Extra', 15, [extra])
	cells = cell('Points', 8, [points], cells)
	cells = cell('Minion Condition', 16, [condition], cells)
	cells = cell('Player Condition', 16, [player_condition], cells)
	cells = cell('Type', 10, [variable_type], cells)
	cells = check_cell('Link', 7, link, cells)
	cells = check_cell('Multiple', 9, multiple, cells, True)
	new_mod = mod_create('Multiple Minions', 20)
	new_mod  = mod_cell('Count', 7, [multiple_value], new_mod)
	new_mod  = mod_cell('Horde', 7, [horde], new_mod)
	body = mod_add(multiple, new_mod, body)
	
	cells = check_cell('Attitide', 9, attitude, cells, True)
	new_mod = mod_create('Attitude', 11)
	new_mod  = mod_cell('Level', 7, [attitude_attitude], new_mod)
	new_mod  = mod_cell('Trait to Control', 18, [attitude_trait], new_mod)
	body = mod_add(attitude, new_mod, body)
	
	cells = check_cell('Resistable', 9, resitable, cells, True)
	new_mod = mod_create('Resistable', 11)
	new_mod  = mod_cell('Defense', 9, [resitable_check], new_mod)
	new_mod  = mod_cell('DC', 4, [resitable_dc, '+ Effect Rank'], new_mod)
	body = mod_add(resitable, new_mod, body)
	
	cells = check_cell('Heroic', 7, heroic, cells)
	cells = check_cell('Sacrifice', 9, sacrifice, cells, True)
	new_mod = mod_create('Sacrifice', 11)
	new_mod  = mod_cell('Cost', 6, [sacrifice_cost], new_mod)
	body = mod_add(sacrifice, new_mod, body)
	body = send(cells, body)

	cells.clear()

	return (body)

def mod_post(entry, body, cells):
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	affects_objects = entry.affects_objects
	area = entry.area
	persistent = entry.persistent
	incurable = entry.incurable
	selective = entry.selective
	limited = entry.limited
	innate = entry.innate
	others = entry.others
	sustained = entry.sustained
	reflect = entry.reflect
	redirect = entry.redirect
	half = entry.half
	affects_corp = entry.affects_corp
	continuous = entry.continuous
	vulnerable = entry.vulnerable
	precise = entry.precise
	progressive = entry.progressive
	subtle = entry.subtle
	permanent = entry.permanent
	points = entry.points
	ranks_check = entry.ranks_check
	action = entry.action
	side_effect = entry.side_effect
	concentration = entry.concentration
	simultaneous = entry.simultaneous
	effortless = entry.effortless
	noticeable = entry.noticeable
	unreliable = entry.unreliable
	radius = entry.radius
	accurate = entry.accurate
	acute = entry.acute
	objects_alone = entry.objects_alone
	objects_character = entry.objects_character
	effortless_degree = entry.effortless_degree
	effortless_retries = entry.effortless_retries
	simultaneous_descriptor = entry.simultaneous_descriptor
	area_damage = entry.area_damage
	area_ranged = entry.area_ranged
	area_descriptor = entry.area_descriptor
	limited_type = entry.limited_type
	limited_mod = entry.limited_mod
	limited_level = entry.limited_level
	limited_source = entry.limited_source
	limited_task_type = entry.limited_task_type
	limited_task = entry.limited_task
	limited_trait_type = entry.limited_trait_type
	limited_trait = entry.limited_trait
	limited_description = entry.limited_description
	limited_subjects = entry.limited_subjects
	limited_extra = entry.limited_extra
	limited_language_type = entry.limited_language_type
	limited_degree = entry.limited_degree
	limited_sense = entry.limited_sense
	limited_subsense = entry.limited_subsense
	limited_descriptor = entry.limited_descriptor
	limited_range = entry.limited_range
	limited_ground = entry.limited_ground
	side_effect_type = entry.side_effect_type
	side_level = entry.side_level
	side_other = entry.side_other
	reflect_check = entry.reflect_check
	reflect_descriptor = entry.reflect_descriptor
	subtle_opposed = entry.subtle_opposed
	subtle_null_trait_type = entry.subtle_null_trait_type
	subtle_null_trait = entry.subtle_opponent_trait
	others_carry = entry.others_carry
	others_touch = entry.others_touch
	others_touch_continuous = entry.others_touch_continuous
	ranks_trait_type = entry.ranks_trait_type
	ranks_trait = entry.ranks_trait
	ranks_ranks = entry.ranks_ranks
	ranks_mod = entry.ranks_mod
	points_type = entry.points_type
	points_reroll_target = entry.points_reroll_target
	points_reroll_cost = entry.points_reroll_cost
	points_rerolls = entry.points_rerolls
	points_reroll_result = entry.points_reroll_result
	ranks = entry.ranks
	cost = entry.cost	
	extra = entry.extra
	extra_count = entry.extra_count
	extra_degree = entry.extra_degree
	extra_dc = entry.extra_dc
	extra_circ = entry.extra_circ


	cost = get_cost(cost, ranks, extra_id)

	area_damage = get_keyword(PowerDamage, area_damage)
	area_ranged = get_name(PowerRangedType, area_ranged)
	reflect_check = get_keyword(PowerCheck, reflect_check)
	subtle_opposed = get_keyword(PowerOpposed, subtle_opposed)
	extra_degree = get_name(PowerDegreeType, extra_degree)
	extra_dc = get_name(PowerDCType, extra_dc)
	extra_circ = get_name(PowerCircType, extra_circ)

	limited_trait = trait_select(limited_trait, limited_trait_type)
	subtle_null_trait = trait_select(subtle_null_trait, subtle_null_trait_type)
	ranks_trait = trait_select(ranks_trait, ranks_trait_type)
	
	extra = extra_name(extra_id)
	objects_alone = get_name(Defense, objects_alone)
	objects_character = get_name(Defense, objects_character)
	limited_level = get_name(Levels, limited_level)
	limited_extra = get_name(Extra, limited_extra)
	limited_sense = get_name(Sense, limited_sense)
	limited_range = get_name(Range, limited_range)
	side_level = get_name(Levels, side_level)
	limited_ground = get_name(Ground, limited_ground)

	reflect_descriptor = descriptor_name(reflect_descriptor)
	limited_descriptor = descriptor_name(limited_descriptor)
	limited_source = descriptor_name(limited_source)
	simultaneous_descriptor = descriptor_name(simultaneous_descriptor)
	area_descriptor = descriptor_name(area_descriptor)
	
	limited_type_select = [{'type': '', 'name': 'Limited Against'}, {'type': 'task_type', 'name': 'Task Type'}, {'type': 'task', 'name': 'All tasks but One'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'subjects', 'name': 'Subjects'}, {'type': 'language', 'name': 'Different Language'}, {'type': 'extra', 'name': 'Extra Effect'}, {'type': 'degree', 'name': 'Degree of Success'}, {'type': 'sense', 'name': 'Sense'},  {'type': 'range', 'name': 'Range'}, {'type': 'source', 'name': 'Requires Descriptor'}, {'type': 'other', 'name': 'Other'}, {'type': 'level', 'name': 'Level'}]

	task_type_select = [{'type': '', 'name': 'Does Not Work On'}, {'type': 'physical', 'name': 'Physical Tasks'}, {'type': 'mental', 'name': 'Mental Tasks'}]
	limited_task_type = selects(limited_task_type, task_type_select)

	null_type_select = [{'type': '', 'name': 'Effect'}, {'type': 'null', 'name': 'Nullifies Effect'}, {'type': 'mod', 'name': 'Modifier to Check'}]
	limited_language_type = selects(limited_language_type, null_type_select)

	spend_select = [{'type': '', 'name': 'Effect'}, {'type': 'reroll', 'name': 'Re-roll'}]
	points_type = selects(points_type, spend_select)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	points_reroll_target = selects(points_reroll_target, targets_select)

	result_select = [{'type': '', 'name': 'Result'}, {'type': 'high', 'name': 'Higher'}, {'type': 'low', 'name': 'Lower'}]
	points_reroll_result = selects(points_reroll_result, result_select)

	effortless_degree = integer_convert(effortless_degree)
	limited_mod = integer_convert(limited_mod)
	limited_subjects = integer_convert(limited_subjects)
	limited_degree = integer_convert(limited_degree)
	ranks_ranks = integer_convert(ranks_ranks)
	ranks_mod = integer_convert(ranks_mod)
	points_reroll_cost = integer_convert(points_reroll_cost)
	points_rerolls = integer_convert(points_rerolls)
	points_reroll_result = integer_convert(points_reroll_result)
	extra_count = integer_convert(extra_count)
	
	cells = cell('Extra', 15, [extra])
	cells = check_cell('Affects Objects', 16, affects_objects, cells, True)
	new_mod = mod_create('Affects Objects', 20)
	new_mod = mod_cell('Objects Alone', 17, [objects_alone], new_mod)
	new_mod = mod_cell('With Character', 15, [objects_character], new_mod)
	body = mod_add(affects_objects, new_mod, body)

	cells = check_cell('Area', 7, area, cells, True)
	new_mod = mod_create('Area', 6)
	new_mod = mod_cell('Damage', 9, [area_damage], new_mod)
	new_mod = mod_cell('Range', 7, [area_ranged], new_mod)
	new_mod = mod_cell('Descriptor', 7, [area_descriptor], new_mod)
	body = mod_add(area, new_mod, body)

	cells = check_cell('Persistant', 10, persistent, cells)
	cells = check_cell('Incurable', 8, incurable, cells)
	cells = check_cell('Selective', 9, selective, cells)

	cells = check_cell('Limited', 8, limited, cells, True)
	limited_type_select = [{'type': 'task_type', 'name': 'Limited by Task Type', 'w': 23}, {'type': 'task', 'name': 'Limited by All tasks but One', 'w': 34}, {'type': 'trait', 'name': 'Limited by Trait', 'w': 19}, {'type': 'descriptor', 'name': 'Limited by Descriptor', 'w': 23}, {'type': 'subjects', 'name': 'Limited by Subjects', 'w': 22}, {'type': 'language', 'name': 'Limited by Language', 'w': 24}, {'type': 'extra', 'name': 'Limited to Extra', 'w': 20}, {'type': 'degree', 'name': 'Limited by Degree of Success', 'w': 33}, {'type': 'sense', 'name': 'Limited by Sense', 'w': 19},  {'type': 'range', 'name': 'Limited by Range', 'w': 19}, {'type': 'source', 'name': 'Limited by Requireed Descriptor', 'w': 35}, {'type': 'other', 'name': 'Limited by Other Factor', 'w': 27}, {'type': 'level', 'name': 'Limited by Level', 'w': 19}]
	new_mod = mod_create('Limited', 9, limited_type, limited_type_select)
	value = 'task_type'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell("Doesn't Work On:", 16, [limited_task_type], new_mod, value)
	value = 'task'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Task:', 6, [limited_task], new_mod, value)
	value = 'trait'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Trait:', 7, [limited_trait], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Descriptor:', 12, [limited_descriptor], new_mod, value)
	value = 'subjects'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Number of Affected Characters:', 28, [limited_subjects], new_mod, value)
	value = 'language'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Effect:', 8, [limited_language_type], new_mod, value)
	value = 'extra'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Extra Effect:', 15, [limited_extra], new_mod, value)
	value = 'degree'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Degree:', 8, [limited_degree], new_mod, value)
	value = 'sense'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Sense:', 7, [limited_sense], new_mod, value)
	new_mod = mod_cell('Subsense:', 10, [limited_subsense], new_mod, value)
	value = 'range'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Range:', 7, [limited_range], new_mod, value)
	value = 'source'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Required Descriptor:', 20, [limited_source], new_mod, value)
	value = 'other'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Other Factor:', 16, [limited_description], new_mod, value)
	value = 'level'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Level:', 7, [limited_level], new_mod, value)
	value = 'ground'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Ground Type:', 15, [limited_ground], new_mod, value)
	body = mod_add(limited, new_mod, body)

	cells = check_cell('Innate', 8, innate, cells)

	cells = check_cell('Affects Others', 15, others, cells, True)
	new_mod = mod_create('Affects Others', 17)
	new_mod = mod_cell('Requires Carrying:', 18, [others_carry], new_mod)
	new_mod = mod_cell('Requires Touch:', 18, [others_touch], new_mod)
	new_mod = mod_cell('Continous Touch:', 18, [others_touch_continuous], new_mod)
	body = mod_add(others, new_mod, body)

	cells = check_cell('Sustained', 9, sustained, cells)

	cells = check_cell('Reflect', 8, reflect, cells, True)
	new_mod = mod_create('Reflect', 8)
	new_mod = mod_cell('Check:', 7, [reflect_check], new_mod)
	new_mod = mod_cell('Descriptor:', 12, [reflect_descriptor], new_mod)
	body = mod_add(others, new_mod, body)
	
	body = mod_add(reflect, new_mod, body)

	cells = check_cell('Redirect', 8, redirect, cells)
	cells = check_cell('Half', 7, half, cells)
	cells = check_cell('Affects Corporeal', 17, affects_corp, cells)
	cells = check_cell('Continuous', 10, continuous, cells)
	cells = check_cell('Vulnerable', 11, vulnerable, cells)
	cells = check_cell('Precise', 8, precise, cells)
	cells = check_cell('Progressive', 11, progressive, cells)

	cells = check_cell('Subtle', 7, subtle, cells, True)
	new_mod = mod_create('Subtle', 8)
	new_mod = mod_cell('Opponent Check:', 17, [subtle_opposed], new_mod)
	new_mod = mod_cell('Nullfied Trait:', 17, [subtle_null_trait], new_mod)
	body = mod_add(subtle, new_mod, body)

	cells = check_cell('Permanent', 10, permanent, cells)

	cells = check_cell('Points', 8, points, cells, True)
	new_mod = mod_create('Points Rerolls', 17)
	new_mod = mod_cell('Target:', 8, [points_reroll_target], new_mod)
	new_mod = mod_cell('Cost:', 6, [points_reroll_cost], new_mod)
	new_mod = mod_cell('Rerolls:', 10, [points_reroll_result], new_mod)

	body = mod_add(points, new_mod, body)

	cells = check_cell('Ranks', 7, ranks_check, cells, True)
	new_mod = mod_create('Gain Trait', 12)
	new_mod = mod_cell('Trait:', 7, [ranks_trait], new_mod)
	new_mod = mod_cell('Ranks:', 6, [ranks_ranks], new_mod)
	new_mod = mod_cell('Modifier:', 9, [ranks_mod], new_mod)	
	body = mod_add(ranks_check, new_mod, body)

	cells = check_cell('Action', 7, action, cells)
	
	cells = check_cell('Side Effect', 12, side_effect, cells, True)
	side_effects_select = [{'type': 'complication', 'name': 'Complication', 'w': 14}, {'type': 'level', 'name': 'Level', 'w': 8}, {'type': 'other', 'name': 'Other', 'w': 8}]
	new_mod = mod_create('Side Effect', 13, side_effect_type, side_effects_select)
	value = 'complication'
	value = 'level'	
	new_mod = mod_cell('Level:', 8, [side_level], new_mod, value)
	value = 'other'
	new_mod = mod_cell('Other Side Effect:', 22, [side_other], new_mod, value)
	body = mod_add(side_effect, new_mod, body)
	
	cells = check_cell('Concentration', 13, concentration, cells)
	
	cells = check_cell('Simultaneous', 13, simultaneous, cells, True)
	new_mod = mod_create('Simultaneous', 14)
	new_mod = mod_cell('Descriptor:',13 , [simultaneous_descriptor], new_mod)
	body = mod_add(simultaneous, new_mod, body)
	
	cells = check_cell('Effortless', 11, effortless, cells, True)
	new_mod = mod_create('Effortless', 12)
	new_mod = mod_cell('Degree:', 8, [effortless_degree], new_mod)
	new_mod = mod_cell('Unlimited Retries:', 20, [effortless_retries], new_mod)	
	body = mod_add(effortless, new_mod, body)
	
	cells = check_cell('Extra', 7, extra, cells, True)
	new_mod = mod_create('Extra Effect', 16)
	new_mod = mod_cell('Degree:', 8, [extra_degree], new_mod)
	new_mod = mod_cell('Circumstance', 17, [extra_circ], new_mod)
	new_mod = mod_cell('DC', 5, [extra_dc], new_mod)	
	body = mod_add(extra, new_mod, body)
	
	cells = check_cell('Noticeable', 11, noticeable, cells)
	cells = check_cell('Unreliable', 11, unreliable, cells)
	cells = check_cell('Radius', 7, ranks, cells)
	cells = check_cell('Accurate', 9, accurate, cells)
	cells = check_cell('Acute', 7, acute, cells)

	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	body = send(cells, body)

	cells.clear()

	return (body)


def ranged_post(entry, body, cells):
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	range_type = entry.range_type
	flat_value = entry.flat_value
	flat_units = entry.flat_units
	flat_rank = entry.flat_rank
	flat_rank_value = entry.flat_rank_value
	flat_rank_units = entry.flat_rank_units
	flat_rank_rank = entry.flat_rank_rank
	flat_rank_distance = entry.flat_rank_distance
	flat_rank_distance_rank = entry.flat_rank_distance_rank
	units_rank_start_value = entry.units_rank_start_value
	units_rank_value = entry.units_rank_value
	units_rank_units = entry.units_rank_units
	units_rank_rank = entry.units_rank_rank
	rank_distance_start = entry.rank_distance_start
	rank_distance = entry.rank_distance
	rank_effect_rank = entry.rank_effect_rank
	effect_mod_math = entry.effect_mod_math
	effect_mod = entry.effect_mod
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_math = entry.check_math
	check_mod = entry.check_mod
	trait_trait_type = entry.trait_trait_type
	trait_trait = entry.trait_trait
	trait_math = entry.trait_math
	trait_mod = entry.trait_mod
	distance_mod_rank = entry.distance_mod_rank
	distance_mod_math = entry.distance_mod_math
	distance_mod_trait_type = entry.distance_mod_trait_type
	distance_mod_trait = entry.distance_mod_trait
	dc = entry.dc
	circ = entry.circ
	degree = entry.degree
	damage = entry.damage
	keyword = entry.keyword
	title = entry.title
	rank = entry.rank
	
	title_name = get_name(PowerMoveType, title)
	body['title'] = title_name

	check_trait = trait_select(check_trait, check_trait_type)
	trait_trait = trait_select(trait_trait, trait_trait_type)
	distance_mod_trait = trait_select(distance_mod_trait, distance_mod_trait_type)

	dc = get_keyword(PowerDC, dc)
	circ = get_keyword(PowerCirc, circ)
	degree = get_keyword(PowerDegree, degree)
	damage = get_keyword(PowerDamage, damage)

	extra = extra_name(extra_id)
	flat_units = name(Unit, flat_units)
	flat_rank_units = name(Unit, flat_rank_units)
	units_rank_units = name(Unit, units_rank_units)
	effect_mod_math = math_convert(Math, effect_mod_math)
	check_math = math_convert(Math, check_math)
	trait_math = math_convert(Math, trait_math)
	distance_mod_math = math_convert(Math, distance_mod_math)

	flat_value = integer_convert(flat_value)
	flat_rank = integer_convert(flat_rank)
	flat_rank_value = integer_convert(flat_rank_value)
	flat_rank_rank = integer_convert(flat_rank_rank)
	flat_rank_distance = integer_convert(flat_rank_distance)
	flat_rank_distance_rank = integer_convert(flat_rank_distance_rank)
	units_rank_start_value = integer_convert(units_rank_start_value)
	units_rank_value = integer_convert(units_rank_value)
	units_rank_units = integer_convert(units_rank_units)
	units_rank_rank = integer_convert(units_rank_rank)
	rank_distance_start = integer_convert(rank_distance_start)
	rank_distance = integer_convert(rank_distance)
	rank_effect_rank = integer_convert(rank_effect_rank)
	effect_mod = integer_convert(effect_mod)
	check_mod = integer_convert(check_mod)
	trait_mod = integer_convert(trait_mod)
	distance_mod_rank = integer_convert(distance_mod_rank)



	cells = cell('Keyword', 15, [keyword])
	cells = cell('Extra', 15, [extra], cells)

	vcells = vcell('flat_units', 30, [flat_value, flat_units])

	distance_rank = string('Rank Distance', [flat_rank])
	vcells = vcell('distance_rank', 30, [flat_rank, distance_rank], vcells)

	rank = string('Rank:', [flat_rank_rank, flat_rank_value, flat_rank_units])
	equals = string('=', [flat_rank_rank, flat_rank_value, flat_rank_units])
	vcells = vcell('flat_rank_units', 30, [rank, flat_rank_rank, equals, flat_rank_value, flat_rank_units], vcells)
	
	rank = string('Rank:', [flat_rank_distance, flat_rank_distance_rank])
	equals = string('=', [flat_rank_distance, flat_rank_distance_rank])
	distance_rank = string('Rank Distance', [flat_rank_distance, flat_rank_distance_rank])
	vcells = vcell('flat_rank_distance', 35, [rank, flat_rank_distance_rank, equals, flat_rank_distance, distance_rank], vcells)
	
	start = string('Starts at', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	then = string('then', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	per = string('Per', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	rank = string('Rank', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	vcells = vcell('units_rank', 75, [start, units_rank_start_value, units_rank_units, then, units_rank_value, units_rank_units, per, units_rank_rank, rank], vcells)
	
	start = string('Starts at', [rank_distance_start, rank_distance, rank_effect_rank])
	rankdistance = string('Rank Distance', [rank_distance_start, rank_distance, rank_effect_rank])
	then = string('then', [rank_distance_start, rank_distance, rank_effect_rank])
	per = string('Per', [rank_distance_start, rank_distance, rank_effect_rank])
	rank = string('Rank', [rank_distance_start, rank_distance, rank_effect_rank])
	vcells = vcell('rank_rank', 50, [start, rank_distance_start, rankdistance, then, rank_distance, rankdistance, per, rank_effect_rank, rank], vcells)
	
	effect_rank = string('Effect Rank', [effect_mod_math, effect_mod])
	distance_rank = string('= Distance Rank', [effect_rank, effect_mod_math, effect_mod])
	vcells = vcell('effect_mod', 50, [effect_rank, effect_mod_math, effect_mod, distance_rank], vcells) 
	
	distance_rank = string('= Distance Rank', [trait_trait, trait_math, trait_mod])
	vcells = vcell('trait_mod', 45, [trait_trait, trait_math, trait_mod, distance_rank], vcells)
	
	distance_rank = string('= Distance Rank', [distance_mod_rank, distance_mod_math, distance_mod_trait])
	vcells = vcell('distance_mod', 50, [distance_mod_rank, distance_mod_math, distance_mod_trait, distance_rank], vcells)
	
	distance_rank = string('= Distance Rank', [check_trait, check_math, check_mod, distance_rank])
	vcells = vcell('check', 50, [check_trait, check_math, check_mod, distance_rank], vcells)
	cells = vcell_add('Range', range_type, vcells, cells)

	cells = check_cell('Per Rank', 9, rank, cells)

	cells = cell('Circumstance', 15, [circ], cells)
	cells = cell('Damage', 15, [damage], cells)
	cells = cell('DC', 15, [dc], cells)
	cells = cell('Degree', 15, [degree], cells)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)

def resist_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	mod = entry.mod	
	rounds = entry.rounds
	circumstance = entry.circumstance
	resist_check_type = entry.resist_check_type
	trait_type = entry.trait_type
	trait = entry.trait
	descriptor = entry.descriptor
	requires_check = entry.requires_check
	check_type = entry.check_type
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait

	trait = trait_select(trait, trait_type)
	check_trait = trait_select(check_trait, check_trait_type)

	extra = extra_name(extra_id)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)


	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 16, [target], cells)
	cells = cell('Mod', 7, [mod], cells)
	cells = cell('Rounds', 8, [rounds], cells)

	vcells = vcell('descriptor', 18, [descriptor])
	vcells = vcell('trait', 16, [trait], vcells) 
	vcells = vcell('harmed', 18, ['Subject Harmed'], vcells)

	cells = vcell_add('Applies to', resist_check_type, vcells, cells)

	cells = check_cell('Check', 8, requires_check, cells, True)
	new_mod = mod_create('Requires Check', 17)
	new_mod = mod_cell('Check Type:', 12, [check_type], new_mod)
	new_mod = mod_cell('TraitL', 7, [check_trait], new_mod)
	body = mod_add(requires_check, new_mod, body)

	cells = cell('Circumstance', 35, [circumstance], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def resisted_by_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id	
	trait_type = entry.trait_type
	dc = entry.dc
	mod = entry.mod
	description = entry.description
	trait = entry.trait
	effect = entry.effect
	level = entry.level
	degree = entry.degree
	descriptor = entry.descriptor
	weaken_max = entry.weaken_max
	weaken_restored = entry.weaken_restored
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage =  entry.damage
	strength = entry.strength
	nullify_descriptor = entry.nullify_descriptor
	nullify_alternate = entry.nullify_alternate
	extra_effort = entry.extra_effort

	trait = trait_select(trait, trait_type)
	descriptor = descriptor_name(descriptor)
	nullify_descriptor = descriptor_name(nullify_descriptor)

	extra = extra_name(extra_id)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	nullify_alternate = get_name(Defense, nullify_alternate)

	dc = integer_convert(dc)
	mod = integer_convert(mod)
	degree = integer_convert(degree)
	weaken_max = integer_convert(weaken_max)
	weaken_restored = integer_convert(weaken_restored)
	damage =  integer_convert(damage)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Trait', 15, [trait], cells)
	cells = cell('DC', 7, [dc], cells)
	cells = cell('Mod', 7, [mod], cells)
	cells = cell('Degree', 9, [degree], cells)
	cells = cell('Descriptor', 22, [descriptor], cells)

	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 25, [condition1, word, condition2])
	vcells = vcell('damage', 18, [damage], vcells)
	wid = width(18, 10, nullify_alternate)
	vcells = vcell('nullify', wid, [nullify_descriptor, nullify_alternate], vcells)
	wid = width(10, 15, weaken_restored)
	word =  string('Max:', [weaken_max])
	word2 = string('Restored', [weaken_max, weaken_restored])
	vcells = vcell('trait', wid, [word, weaken_max, word2, weaken_restored], vcells) 
	vcells = vcell('level', 18, [level], vcells)
	cells = vcell_add('Effect', effect, vcells, cells)
	cells = check_cell('Extra Effort', 14, extra_effort, cells)
	cells = cell('Circumstaance', 30, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)
	
def reverse_effect_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	degree = entry.degree
	when = entry.when
	check_check = entry.check_check
	time_check = entry.time_check
	trait_type = entry.trait_type
	trait = entry.trait
	value_type = entry.value_type
	value_dc = entry.value_dc
	math_dc = entry.math_dc
	math = entry.math
	time_value = entry.time_value
	time_unit = entry.time_unit

	trait = trait_select(trait, trait_type)
	
	extra = extra_name(extra_id)
	math = math_convert(Math, math)
	time_unit = name(Unit, time_unit)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	whens_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]
	when = selects(when, whens_select)

	degree = integer_convert(degree)
	value_dc = integer_convert(value_dc)
	math_dc = integer_convert(math_dc)
	time_value = integer_convert(time_value)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 16, [target], cells)
	cells = cell('Degree', 8, [degree], cells)
	cells = cell('When', 10, [when], cells)

	cells = check_cell('Reverse by Check', 25, check_check, cells, True)
	select =  [{'type': 'value', 'name': 'DC', 'w': 10}, {'type': 'math', 'name': 'DC', 'w': 10}]
	new_mod = mod_create('Reverse by Check', 23, value_type, select)
	value = 'value'
	new_mod = mod_cell('Value:', 13, [value_dc], new_mod, value)
	new_mod = mod_cell('Trait:', 10, [trait], new_mod, value)
	value = 'math'
	word = string('Rank', [math_dc, math])
	new_mod = mod_cell('Math:', 10, [math_dc, math, word], new_mod, value)
	new_mod = mod_cell('Trait:', 10, [trait], new_mod, value)
	body = mod_add(check_check, new_mod, body)

	cells = check_cell('Reverse by Time', 25, time_check, cells, True)
	new_mod = mod_create('Reverse by Time', 23)
	new_mod = mod_cell('Time:', 10, [time_value, time_unit], new_mod)
	body = mod_add(time_check, new_mod, body)

	body = send(cells, body)

	cells.clear()

	return (body)


def sense_post(entry, body, cells):	

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	sense = entry.sense
	subsense = entry.subsense
	skill = entry.skill
	sense_type = entry.sense_type
	height_trait_type = entry.height_trait_type
	height_trait = entry.height_trait
	height_power_required = entry.height_power_required
	height_ensense = entry.height_ensense
	resist_trait_type = entry.resist_trait_type
	resist_trait = entry.resist_trait
	resist_immune = entry.resist_immune
	resist_permanent = entry.resist_permanent
	resist_circ = entry.resist_circ
	objects = entry.objects
	exclusive = entry.exclusive
	gm = entry.gm
	dark = entry.dark
	lighting = entry.lighting
	time = entry.time
	dimensional = entry.dimensional
	radius = entry.radius
	accurate = entry.accurate
	acute = entry.acute
	distance = entry.distance
	distance_dc = entry.distance_dc
	distance_mod = entry.distance_mod
	distance_value = entry.distance_value
	distance_unit = entry.distance_unit
	distance_factor = entry.distance_factor
	dimensional_type = entry.dimensional_type
	ranks = entry.ranks
	cost = entry.cost
	time_value = entry.time_value
	time_type = entry.time_type
	circ = entry.circ

	cost = get_cost(cost, ranks, extra_id)
	
	skill =  get_keyword(PowerCheck, skill)
	time_value = get_keyword(PowerTime, time_value)
	time_type = get_name(PowerTimeType, time_type)
	circ = get_keyword(PowerCirc, circ)

	height_trait = trait_select(height_trait, height_trait_type)
	resist_trait = trait_select(resist_trait, resist_trait_type)

	extra = extra_name(extra_id)
	sense = get_name(Sense, sense)
	subsense = get_name(SubSense, subsense)
	height_ensense = get_name(Power, height_ensense)
	lighting = get_name(Light, lighting)
	time_unit = get_name(Unit, time_unit)
	time_skill = get_name(Skill, time_skill)
	time_bonus = get_name(SkillBonus, time_bonus)
	distance_unit = get_name(Unit, distance_unit)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	all_some_select = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]
	resist_permanent = selects(resist_permanent, all_some_select)

	darkness_select = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]
	lighting = selects(lighting, darkness_select)

	
	sense_distance_select = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'unit', 'name': 'By Rank (Units)'}, {'type': 'rank', 'name': 'By Rank'}]
	distance = selects(distance, sense_distance_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimensional_type = selects(dimensional_type, dimensions_select)

	resist_circ = integer_convert(resist_circ)
	distance_dc = integer_convert(distance_dc)
	distance_mod = integer_convert(distance_mod)
	distance_value = integer_convert(distance_value)
	distance_factor = integer_convert(distance_factor)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Sense', 9, [sense], cells)
	cells = cell('Subsense', 14, [subsense], cells)
	cells = cell('Check', 16, [skill], cells)

	wid = 17
	affects = string('Affects', [height_trait])
	word = string('Requires', [height_ensense])
	wid = width(wid, 18, height_ensense)
	vcells = vcell('height', wid, [affects, height_trait, word, height_ensense])
	wid = 14
	affects =  string('Affects', [resist_trait])
	word = check_convert('Immune', resist_immune)
	wid = width(wid, 10, resist_immune)
	perm = string(resist_permanent, word)
	wid = width(wid, 12, resist_permanent)
	vcells = vcell('resist', wid, [affects, resist_trait, word, perm], vcells)
	vcell_add('Effect', sense_type, vcells, cells)

	cells = circ_cell('Circ', 'Circumstance', 6, circ, cells, body)

	cells = check_cell('Penetrates', 12, objects, cells)
	cells = check_cell('Exclusive', 10, exclusive, cells)
	cells = check_cell('GM', 6, gm, cells)

	cells = check_cell('Counters Dark', 16, dark, cells, True)
	new_mod = mod_create('Counters Darkness', 22)
	new_mod = mod_cell('See In:', 8, lighting, new_mod)
	body = mod_add(dark, new_mod, body)

	cells = check_cell('Time Effect', 14, time, cells, True)
	new_mod = mod_create('Time Effect', 15)
	new_mod = mod_cell('Keyword', 10, [time_value, time_type])
	body = mod_add(time, new_mod, body)

	cells = check_cell('Dimensional', 14, dimensional, cells, True)
	new_mod = mod_create('Dimensional', 15)
	new_mod = mod_cell('Type', 6, [dimensional_type], new_mod)
	body = mod_add(dimensional, new_mod, body)

	cells = check_cell('Radius', 8, radius, cells)
	cells = check_cell('Accurate', 10, accurate, cells)
	cells = check_cell('Acute', 7, acute, cells)
	
	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	
	body = send(cells, body)

	cells.clear()

	return (body)


def power_check_post(entry, body, cells):

	extra = entry.extra_id
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
	ranged = entry.ranged
	variable = entry.variable
	opponent = entry.opponent
	opponent_type = entry.opponent_type
	varible_type = entry.variable_type
	title = entry.title

	title_name = get_name(PowerCheckType, title)

	body['title'] = title_name
	body['add_title'] = True

	extra = extra_name(extra_id)

	trait = trait_select(trait, trait_type)

	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	mod = integer_convert(mod)
	action = action_convert(action_type, action)
	condition = get_name(Condition, condition)

	degree = get_name(PowerDegreeType, degree)
	circ = get_name(PowerCircType, circ)
	dc = get_name(PowerDCType, dc)
	time = get_name(PowerTimeType, time)
	move = get_name(PowerMoveType, move)
	dc_value = get_keyword(PowerDC, dc_value)
	opposed = get_keyword(PowerOpposed, opposed)
	ranged = get_name(PowerRangedType, ranged)
	opponent = get_keyword(PowerOpposed, opponent)
	variable = get_keyword(PowerCheck, variable)
	
	attack = integer_convert(attack)

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'gm', 'name': 'GM Choice'}]
	when = selects(when, check_type_select)

	targets = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	condition_target = selects(condition_target, targets)
	conditions_target = selects(conditions_target, targets)

	cells = cell('Keyword', 14, [keyword])
	cells = cell('Extra', 13, [extra], cells)
	cells = cell('Check', 11, [check_type], cells)
	cells = cell('Modifier', 8, [mod], cells)
	cells = cell('When', 12, [when], cells)
	cells = cell('Check Trait', 16, [trait], cells)
	cells = cell('Action', 11, [action], cells)
	
	vcells = vcell('change', 25, [conditions_target, 'from', condition1, 'to', condition2])
	vcells = vcell('condition', 20, [condition_target, condition], vcells)
	w = width(10, 8, conflict_range)
	vcells = vcell('conflict', w, [conflict, conflict_range], vcells)
	vcells = vcell('variable', 18, [variable, varible_type], vcells)
	vcells = vcell('opposed', 18, [opponent, opponent_type], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	attack = add_plus(attack)
	cells = cell('Attack', 9, [attack], cells)

	cells = circ_cell('Opposed', 'Opposed', 8, opposed, cells, body)
	cells = circ_cell('Circ Mod', 'Circumstance', 8, circ, cells, body)
	content = arrow_cell([dc])
	content = arrow_cell([dc_value], content)
	cells = circ_cell('DC', 'DC', 5, content, cells, body)
	cells = circ_cell('Degree', 'Degree', 7, degree, cells, body)
	cells = circ_cell('Move', 'Move', 6, move, cells, body)
	cells = circ_cell('Time', 'Time', 6, time, cells, body)
	cells = circ_cell('Ranged', 'Ranged', 7, ranged, cells, body)

	cells = check_cell('Free', 7, free, cells)
	cells = check_cell('Weapon', 8, conflict_weapon, cells)

	cells = circ_cell('Circ', 'Circumstance', 6, circumstance, cells, body)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)
	
def power_circ_post(entry, body, cells):

	extra = entry.extra_id
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
	check_type = entry.check_type
	descriptor_effect = entry.descriptor_effect
	descriptor_target = entry.descriptor_target
	descriptor = entry.descriptor


	title_name = get_name(PowerCircType, title)
	body['title'] = title_name

	extra = extra_name(extra_id)

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
	descriptor = get_name(PowerDes, descriptor)

	speed = integer_convert(speed)
	conditions = integer_convert(conditions)	
	measure_rank_value = eger_convert(unit_value)
	measure_trait_integer_convert(measure_rank_value)
	unit_value = intmath = math_convert(measure_trait_math)
	measure_mod = integer_convert(measure_mod)
	max = integer_convert(max)

	lasts = get_keyword(PowerTime, lasts)

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

	effect_target_select = [{'type': '', 'name': 'Effect Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'object', 'name': 'Object'}]
	descriptor_target  = selects(descriptor_target, effect_target_select)
	
	descriptor_effect_select = [{'type': '', 'name': 'Effect'}, {'type': 'apply', 'name': 'Applies'}, {'type': 'remove', 'name': 'Removes'}, {'type': 'if', 'name': 'If'}]
	descriptor_effect = selects(descriptor_effect, descriptor_effect_select)


	cells = cell('Keyword', 13, [keyword])
	cells = cell('Extra', 13, [extra], cells)
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

	vcells = vcell('descriptor', 30, [descriptor_effect, descriptor, 'on', descriptor_target], vcells)
	
	cells = vcell_add('Effect', effect, vcells, cells)

	cells = check_cell('Surface', 8, surface, cells)
	cells = check_cell('Optional', 9, optional, cells)
	cells = check_cell('Cumulative', 10, cumulative, cells)
	cells = cell('Maximum', 9, [max], cells)

	cells = circ_cell('Circ', 'Circumstance', 6, circumstance, cells, body)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)
	
def power_dc_post(entry, body, cells):

	extra = entry.extra_id
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
	descriptor_effect = entry.descriptor_effect
	descriptor_target = entry.descriptor_target
	descriptor = entry.descriptor
	descrip = entry.descrip

	title_name = get_name(PowerDCType, title)
	body['title'] = title_name

	extra = extra_name(extra_id)

	cover_type = get_name(Cover, cover_type)
	conceal_type = get_name(Conceal, conceal_type)
	variable = get_keyword(PowerCheck, variable)
	time = get_keyword(PowerTime, time)
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
	descriptor = get_name(PowerDes, descriptor)

	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	complexity = get_name(Complex, complexity)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)


	effect_target_select = [{'type': '', 'name': 'Effect Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'object', 'name': 'Object'}]
	descriptor_target  = selects(descriptor_target, effect_target_select)
	
	descriptor_effect_select = [{'type': '', 'name': 'Effect'}, {'type': 'apply', 'name': 'Applies'}, {'type': 'remove', 'name': 'Removes'}, {'type': 'if', 'name': 'If'}]
	descriptor_effect = selects(descriptor_effect, descriptor_effect_select)
	
	effect_target = selects(effect_target, effect_target_select)

	equipment_use_select = [{'type': '', 'name': 'Use Type'}, {'type': 'use', 'name': 'With Use of'}, {'type': 'resist', 'name': 'Resist'}]
	equipment_use = selects(equipment_use, equipment_use_select)


	cells = cell('Keyword', 14, [keyword])
	cells = cell('Extra', 13, [extra], cells)
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

	cells = check_cell('Descriptor', 12, descrip, cells, True)
	new_mod = mod_create('Descriptor', 15)
	new_mod = mod_cell('Effect', 7, [descriptor_effect], new_mod)
	new_mod = mod_cell('Target', 7, [descriptor_target], new_mod)
	new_mod = mod_cell('Descriptor', 9, [descriptor], new_mod)
	body = mod_add(descrip, new_mod, body)

	
	
	cells = check_cell('Surface', 8, surface, cells)

	cells = circ_cell('Description', 'Description', 13, description, cells, body)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)

def power_degree_post(entry, body, cells):

	extra = entry.extra_id
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
	descriptor_effect = entry.descriptor_effect
	descriptor_target = entry.descriptor_target
	descriptor = entry.descriptor

	title_name = get_name(PowerDegreeType, title)
	body['title'] = title_name

	inflict_trait = trait_select(inflict_trait, inflict_trait_type)
	consequence_trait = trait_select(consequence_trait, consequence_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)
	measure_trait_unit = trait_select(measure_trait_unit, measure_trait_type_unit)
	resist_trait =  trait_select(resist_trait, resist_trait_type)
	skill_trait = trait_select(skill_trait, skill_trait_type)
	routine_trait = trait_select(routine_trait, routine_trait_type)

	extra = extra_name(extra_id)

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
	descriptor = get_name(PowerDes, descriptor)

	measure_type = math_convert(measure_type)
	value_type = math_convert(value_type)

	opposed = get_keyword(PowerOpposed, opposed)
	resist_dc = get_keyword(PowerDC, resist_dc)
	skill_dc = get_keyword(PowerDC, skill_dc)
	compare = get_keyword(PowerOpposed, compare)
	variable = get_keyword(PowerCheck, variable)
	attack_turns  = get_keyword(PowerTime, get_keyword)
	condition_turns = get_keyword(PowerTime, condition_turns)
	level_time = get_keyword(PowerTime, level_time)
	linked = get_keyword(PowerDegree, linked)
	circumstance = get_circ(PowerCirc, circumstance)

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

	effect_target_select = [{'type': '', 'name': 'Effect Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}, {'type': 'object', 'name': 'Object'}]
	descriptor_target  = selects(descriptor_target, effect_target_select)
	
	descriptor_effect_select = [{'type': '', 'name': 'Effect'}, {'type': 'apply', 'name': 'Applies'}, {'type': 'remove', 'name': 'Removes'}, {'type': 'if', 'name': 'If'}]
	descriptor_effect = selects(descriptor_effect, descriptor_effect_select)

	cells = cell('Keyword', 15, [keyword])
	cells = cell('Extra', 13, [extra], cells)
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
	
	vcells = vcell('descriptor', 30, [descriptor_effect, descriptor, 'on', descriptor_target], vcells)

	cells = vcell_add('Effect', type, vcells, cells)
	
	cells = cell('Nullify DC', 13, [nullify], cells)
	cells = check_cell('Cumulative', 12, cumulative, cells)
	cells = cell('Linked', 15, [linked], cells)

	cells = circ_cell('Desc', 'Description', 6, description, cells, body)

	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)
		
def power_move_post(entry, body, cells):

	extra = entry.extra_id
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
	degree_type = entry.degree_type
	circ_type = entry.circ_type
	dc_type = entry.dc_type
	time_type = entry.time_type
	keyword = entry.keyword
	title = entry.title
	
	speed_per = entry.speed_per
	distance_per = entry.distance_per
	flight = entry.flight
	aquatic = entry.aquatic
	ground = entry.ground
	special = entry.special
	condition_check = entry.condition_check
	obstacles = entry.obstacles
	objects = entry.objects
	permeate = entry.permeate
	prone = entry.prone
	equip = entry.equip
	concealment = entry.concealment
	extended = entry.extended
	mass = entry.mass
	flight_resist = entry.flight_resist
	flight_resist_check = entry.flight_resist_check
	flight_equip = entry.flight_equip
	flight_equip_type = entry.flight_equip_type
	flight_equipment = entry.flight_equipment
	flight_conditions = entry.flight_conditions
	acquatic_type = entry.acquatic_type
	ground_type = entry.ground_type
	ground_perm = entry.ground_perm
	ground_time = entry.ground_time
	ground_ranged = entry.ground_ranged
	ground_range = entry.ground_range
	special_type = entry.special_type
	teleport_type = entry.teleport_type
	teleport_change = entry.teleport_change
	teleport_portal = entry.teleport_portal
	teleport_obstacles = entry.teleport_obstacles
	dimension_type = entry.dimension_type
	dimension_mass_rank = entry.dimension_mass_rank
	dimension_descriptor = entry.dimension_descriptor
	special_space = entry.special_space
	special_time = entry.special_time
	special_time_carry = entry.special_time_carry
	condition = entry.condition
	objects_check = entry.objects_check
	objects_direction = entry.objects_direction
	objects_damage = entry.object_damage
	object_damage = entry.object_damage
	permeate_type = entry.permeate_type
	permeate_speed = entry.permeate_speed
	permeate_cover = entry.permeate_cover
	equip_type = entry.equip_type
	equipment = entry.equipment
	concealment_sense = entry.concealment_sense
	conceal_opposed = entry.conceal_opposed
	extended_actions = entry.extended_actions
	mass_value = entry.mass_value
	cost = entry.cost
	ranks = entry.ranks


	title_name = get_name(PowerMoveType, title)
	body['title'] = title_name

	degree = get_keyword(PowerDegree, degree)
	circ = get_keyword(PowerCirc, circ)
	dc = get_keyword(PowerDC, dc)
	time = get_keyword(PowerTime, time)
	degree_type = get_keyword(PowerDegreeType, degree_type)
	circ_type = get_keyword(PowerCircType, circ_type)
	dc_type = get_keyword(PowerDCType, dc_type)
	time_type = get_keyword(PowerTimeType, time_type)

	
	degree_value = arrow_cell([degree])
	circ_value = arrow_cell([circ])
	dc_value = arrow_cell([dc])
	time_value = arrow_cell([time])

	degree_value = arrow_cell([degree_type], degree_value)
	circ_value = arrow_cell([circ_type], circ_value)
	dc_value = arrow_cell([dc_type], dc_value)
	time_value = arrow_cell([time_type], time_value)


	flight_resist_check = get_keyword(PowerCheck, flight_resist_check)
	ground_time = get_keyword(PowerTime, ground_time)
	ground_range = get_name(PowerRangedType, ground_range)
	objects_check = get_keyword(PowerCheck, objects_check)
	object_damage = get_keyword(PowerDamage, objects_damage)
	conceal_opposed = get_keyword(PowerOpposed, conceal_opposed)

	cost = get_cost(cost, ranks, extra)


	speed_trait = trait_select(speed_trait, speed_trait_type)
	distance_rank_trait = trait_select(distance_rank_trait, distance_rank_trait_type)
	distance_unit_trait = trait_select(distance_unit_trait, distance_unit_trait_type)

	extra = extra_name(extra)

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

	dimension_mass_rank = integer_convert(dimension_mass_rank)
	special_time_carry = integer_convert(special_time_carry)
	permeate_speed = integer_convert(permeate_speed)
	extended_actions = integer_convert(extended_actions)
	mass_value = integer_convert(mass_value)

	speed_math1 = math_convert(speed_math1)
	speed_math2 = math_convert(speed_math2)
	distance_units = get_name(Unit, distance_units)
	distance_rank_math1 = math_convert(distance_rank_math1)
	distance_rank_math2 = math_convert(distance_rank_math2)
	distance_unit_math1 = math_convert(distance_unit_math1)
	distance_unit_math2 = math_convert(distance_unit_math2)
	distance_math_units = get_name(Unit, distance_math_units)

	flight_equip_type = get_name(EquipType, flight_equip_type)
	flight_equipment = get_name(Equipment, flight_equipment)
	ground_type = get_name(Ground, ground_type)
	dimension_descriptor = get_name(PowerDes, dimension_descriptor)
	condition = get_name(Condition, condition)
	equip_type = get_name(EquipType, equip_type)
	equipment = get_name(Equipment, equipment)
	concealment_sense = get_name(Sense, concealment_sense)

	flight_conditions = get_multiple(Condition, flight_conditions)

	direction_select = [{'type': 'vert', 'name': 'Vertical'}, {'type': 'hor', 'name': 'Horizontal'}, {'type': 'both', 'name': 'both'}, {'type': 'swim', 'name': 'Swim'}, {'type': 'jump', 'name': 'Jump'} ]
	direction = selects(direction, direction_select)

	aquatic_select = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}]
	acquatic_type = selects(acquatic_type, aquatic_select)

	openings_select = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]
	permeate_type = selects(permeate_type, openings_select)

	travel_select = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]

	teleport_change_select = [{'type': '', 'name': 'Can Change'}, {'type': 'direction', 'name': 'Direction'}, {'type': 'velocity', 'name': 'Velocity'}]
	teleport_change = selects(teleport_change, teleport_change_select)

	teleport_select = [{'type': '', 'name': 'Type'}, {'type': 'know', 'name': 'Know Destination'}, {'type': 'any', 'name': 'Any Destination'}]
	teleport_type = selects(teleport_type, teleport_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimension_type = selects(dimension_type, dimensions_select)

	space_select = [{'type': '', 'name': 'Space Travel Type'}, {'type': 'solar', 'name': 'Planets in Solar System'}, {'type': 'star', 'name': 'Other Star Systems'}, {'type': 'galaxy', 'name': 'Other Galaxies'}]
	special_space = selects(special_space, space_select)

	time_travel_select = [{'type': '', 'name': 'Time Travel Type'}, {'type': 'Fixed', 'name': 'Fixed Point in Time'}, {'type': 'past', 'name': 'Any Point in Past'}, {'type': 'future', 'name': 'Any Point in Future'}, {'type': 'timeline', 'name': 'Alternate Timeline'}, {'type': 'any', 'name': 'Any Point in time'}  ]
	special_time = selects(special_time, time_travel_select)

	permanence_select = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	ground_permanence = selects(ground_permanence, permanence_select)

	move_objects_select = [{'type': '', 'name': 'Direction'}, {'type': 'all', 'name': 'All Directions'}, {'type': 'vertical', 'name': 'Up and Down'}, {'type': 'horizontal', 'name': 'Towards and Away'}, {'type': 'attract', 'name': 'Attraction'}, {'type': 'repel', 'name': 'Repulsion'}]
	objects_direction = selects(objects_direction, move_objects_select)


	cells = cell('Keyword', 18, [keyword])
	cells = cell('Extra', 13, [extra], cells)
	cells = cell('Direction', 12, [direction], cells)

	vcells = vcell('rank', 20, ['Speed Rank', speed_rank])
	speed_rank_mod = add_plus(speed_rank_mod)
	vcells = vcell('rank_mod', 20, [speed_rank_mod, 'Speed Rank'])
	vcells = vcell('mod', 25, [speed_trait, speed_math1, speed_value1, speed_math2, speed_value2], vcells)
	cells = vcell_add('Speed', speed, vcells, cells)
	cells = circ_cell('Desc', 'Description', 5, speed_description, cells, body)
	
	vcells = vcell('rank', 20, [distance_rank, 'Rank Distance'])
	vcells = vcell('unit', 20, [distance_value, distance_units], vcells)
	vcells = vcell('unit_math', 25, [distance_unit_trait, distance_unit_math1, distance_unit_value1, distance_unit_math2,  distance_unit_value2, distance_math_units], vcells)
	vcells = vcell('rank_math', 25, [distance_rank_trait, distance_rank_math1, distance_rank_value1, distance_rank_math2, distance_rank_value2], vcells)
	cells = vcell_add('Distance', distance, vcells, cells)
	cells = circ_cell('Desc', 'Description', 5, distance_description, cells, body)

	cells = check_cell('Flight', 8, flight, cells, True)
	new_mod = mod_create('Flight', 10)
	new_mod = mod_cell('Conditions:', 10, [flight_conditions], new_mod)
	new_mod = mod_cell('Resistance Check:', 15, [flight_resist_check], new_mod)
	new_mod = mod_cell('Requires Equipment:', 20, [flight_equipment], new_mod)
	body = mod_add(flight, new_mod, body)

	cells = check_cell('Aquatic', 9, aquatic, cells, True)
	new_mod = mod_create('Aquatic', 10)
	new_mod = mod_cell('Type:', 7, [acquatic_type], new_mod)
	body = mod_add(aquatic, new_mod, body)

	cells = check_cell('Ground', 8, ground, cells, True)
	new_mod = mod_create('Through Ground', 17)
	new_mod = mod_cell('Type:', 7, [ground_type], new_mod)
	new_mod = mod_cell('Permanance:', 10, [ground_perm], new_mod)
	new_mod = mod_cell('Lasts:', 5, [ground_time], new_mod)
	new_mod = mod_cell('Ranged', 7, [ground_range], new_mod)
	body = mod_add(ground, new_mod, body)

	cells = check_cell('Special', 10, special, cells, True)
	travel_select = [{'type': 'dimension', 'name': 'Dimension Travel', 'w': 20}, {'type': 'space', 'name': 'Space Travel', 'w': 18}, {'type': 'time', 'name': 'Time Travel', 'w': 15}, {'type': 'teleport', 'name': 'Teleport', 'w': 10}]
	new_mod = mod_create('Special Travel', 19, special_type, travel_select)
	value = 'dimension'
	new_mod = mod_cell('Type:', 8, [dimension_type], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [dimension_mass_rank], new_mod, value)
	new_mod = mod_cell('Descriptor:', 13, [dimension_descriptor], new_mod, value)
	value = 'space'
	new_mod = mod_cell('Type:', 8, [special_space], new_mod, value)
	value = 'time'
	new_mod = mod_cell('Type:', 8, [special_time], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [special_time_carry], new_mod, value)
	value = 'teleport'
	new_mod = mod_cell('Type:', 8, [teleport_type], new_mod, value)
	new_mod = mod_cell('Can Change:', 12, [teleport_change], new_mod, value)
	new_mod = mod_cell('Portal:', 9, [teleport_portal], new_mod, value)
	new_mod = mod_cell('Turnabout:', 9, [teleport_obstacles], new_mod, value)
	body = mod_add(special, new_mod, body)

	cells = check_cell('Condition', 10, condition_check, cells, True)
	new_mod = mod_create('Movement Condition', 20)
	new_mod = mod_cell('Condition', 12, [condition], new_mod)
	body = mod_add(condition_check, new_mod, body)

	cells = check_cell('Prone', 7, prone, cells)

	cells = check_cell('Objects', 9, objects, cells, True)
	new_mod = mod_create('Move Objects', 15)
	new_mod = mod_cell('Check', 7, [objects_check], new_mod)
	new_mod = mod_cell('Direction', 10, [objects_direction], new_mod)
	new_mod = mod_cell('Damage', 8, [object_damage], new_mod)
	body = mod_add(objects, new_mod, body)

	cells = check_cell('Permeate', 10, permeate, cells, True)
	new_mod = mod_create('Permeate', 12)
	new_mod = mod_cell('Type:', 8, [permeate_type], new_mod)
	new_mod = mod_cell('Speed Modifier:', 18, [permeate_speed], new_mod)
	new_mod = mod_cell('Provides Cover:', 18, [permeate_cover], new_mod)
	body = mod_add(permeate, new_mod, body)

	cells = check_cell('Equipment', 11, equip, cells, True)
	new_mod = mod_create('Equipment', 15)
	new_mod = mod_cell('Type:', 6, [equip_type], new_mod)
	new_mod = mod_cell('Required:', 12, [equipment], new_mod)
	body = mod_add(equip, new_mod, body)

	cells = check_cell('Conceal', 9, concealment, cells, True)
	new_mod = mod_create('Concealment', 15)
	new_mod = mod_cell('Concealed From:', 18, [concealment_sense], new_mod)
	new_mod = mod_cell('Opponent Check:', 15, [conceal_opposed], new_mod)
	body = mod_add(concealment, new_mod, body)

	cells = check_cell('Extended', 11, extended, cells, True)
	new_mod = mod_create('Extended', 10)
	word = string('Actions', [extended_actions])
	new_mod = mod_cell('For:', 5, [extended_actions, word], new_mod)
	body = mod_add(extended, new_mod, body)

	cells = check_cell('Carry', 7, mass, cells, True)
	new_mod = mod_create('Increased Carry Mass', 30)
	new_mod = mod_cell('Mass Rank:', 13, [mass_value], new_mod)
	body = mod_add(mass, new_mod, body)

	cells = circ_cell('Time', 6, time_value, cells, body)
	cells = circ_cell('Degree', 7, degree_value, cells, body)
	cells = circ_cell('DC', 5, dc_value, cells, body)
	cells = circ_cell('Circ', 6, circ_value, cells, body)

	cells = circ_cell('Cost', 'Cost', 5, cost, cells, body)
	
	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)

def power_opposed_post(entry, body, cells):

	extra = entry.extra_id
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
	variable = entry.variable
	title = entry.title
	opponent = entry.opponent
	opposed = entry.opposed
	variable_type = entry.variable_type

	title_name = get_name(PowerOpposedType, title)
	body['title'] = title_name

	trait = trait_select(trait, trait_type)
	opponent_trait = trait_select(opponent_trait, opponent_trait_type)

	extra = extra_name(extra_id)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)
	

	recurring_value = get_keyword(PowerTime, recurring_value)
	degree = get_name(PowerDegreeType, degree)
	circ = get_name(PowerCircType, circ)
	dc = get_keyword(PowerDC, dc)
	time = get_keyword(PowerTime, time)
	degree_value = get_keyword(PowerDegree, degree_value)
	dc_type = get_name(PowerDCType, dc_type)
	dc_player = get_keyword(PowerDC, dc_player)
	circ_value = get_keyword(PowerCirc, circ_value)
	time_type = get_name(PowerTimeType, time_type)
	recurring_type = get_name(PowerTimeType, recurring_type)
	variable = get_keyword(PowerCheck, variable)
	opponent = get_name(PowerOpposedType, opponent)
	opposed = get_keyword(PowerOpposed, opposed)
	variable_type = get_name(PowerCheckType, variable_type)

	frequency_select = [{'type': 'always', 'name': 'Always'}, {'type': 'gm', 'name': 'GM Discretion'}, {'type': 'player', 'name': 'Player Choice'}]
	frequency = selects(frequency, frequency_select)

	opposed_check = one_of(opposed, [opposed, 'Opponent Check'])
	opposed_check = one_of(opponent, [opponent, 'Opponent Check'], opposed_check)
	variable_check = one_of(variable, [variable, 'Variable Check'])
	variable_check = one_of(variable_type, [variable_type, 'Variable Check'], variable_check)

	attached = [{'type': '', 'name': 'Attached'}, {'type': 'alone', 'name': 'Only Check'}, {'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}, {'type': 'with', 'name': 'With Skill Check'}, {'type': 'before_attack', 'name': 'Before Attack Check'}, {'type': 'after_attack', 'name': 'After Attack Check'}, {'type': 'opp_success', 'name': 'After Opponent Success'}, {'type': 'success', 'name': 'After Player Success'}, {'type': 'opp_fail', 'name': 'After Opponent Failure'}, {'type': 'fail', 'name': 'After Player Failure'}, {'type': 'before_var', 'name': 'Before Variable Check ' + variable_check}, {'type': 'after_var', 'name': 'After Variable Check ' + variable_check}, {'type': 'opponent', 'name': 'After Opponent Check ' + opposed_check}]
	attached = selects(attached, attached_select)

	happens = frequency + ' ' + attached

	cells = cell('Keyword', 15, [keyword])
	cells = cell('Extra', 13, [extra], cells)
	cells = cell('Player', 12, [trait], cells)
	cells = cell('Mod', 6, [mod], cells)
	cells = cell('Check', 10, [player_check], cells)
	cella = check_cell('Secret', 8, player_secret, cells)

	cells = cell('Opponent', 12, [opponent_trait], cells)
	cells = cell('Mod', 6, [opponent_mod], cells)
	cells = cell('Check', 10, [opponent_check], cells)
	
	cells = check_cell('Secret', 8, secret, cells)

	cells = circ_cell('When', 'Check Happens', 6, happens, cells, body)

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
	
	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)

def power_time_post(entry, body, cells):

	extra = entry.extra_id
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
	measure_type = entry.measure_type
	rank = entry.rank


	title_name = get_name(PowerTimeType, title)
	body['title'] = title_name

	trait = trait_select(trait, trait_type)
	measure_type = math_convert(measure_type)

	extra = extra_name(extra_id)

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

	degree = get_keyword(PowerDegree, degree)
	circ = get_keyword(PowerCirc, circ)
	dc = get_keyword(PowerDC, dc)
	degree_type = get_name(PowerDegreeType, degree_type)
	circ_type = get_name(PowerCircType, circ_type)
	dc_type = get_name(PowerDCType, dc_type)

	
	time_effect_select = [{'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'effect', 'name': 'Time Effect Happens'}, {'type': 'limit', 'name': 'Time Limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}, {'type': 'recover', 'name': 'Recovery Time'}]
	type = selects(type, time_effect_select)

	
	recovery_select = [{'type': '', 'name': 'Target'}, {'type': 'player', 'name': 'Player'}, {'type': 'other', 'name': 'Character'}, {'type': 'either', 'name': 'Any'}]
	recovery_target = selects(recovery_target, recovery_select)

	cells = cell('Keyword', 17, [keyword])
	cells = cell('Extra', 13, [extra], cells)

	cells = cell('Time Type', 20, [type], cells)

	vcells = vcell('value', 17, [measure_type, value, units])
	vcells = vcell('math', 30, [measure_type, trait, math, math_value, '= Time Rank'], vcells)
	vcells = vcell('rank',35, [measure_type, rank1, rank1_value, rank_math, rank2, rank2_value], vcells)
	vcells = vcell('gm', 13, ['Set by GM'], vcells)
	vcells = vcell('player', 16, ['Set by Player'], vcells)
	word = int_word('Turns', turns)
	vcells = vcell('turns', 18, [measure_type, turns, word], vcells)	
	vcells = vcell('instant', 14, ['Instant'], vcells)
	vcells = vcell('perm', 14, ['Permanent'], vcells)
	vcells = vcell('round', 14, ['One Round'], vcells)
	vcells = vcell('next', 14, ['Next Round'], vcells)
	vcells = vcell('maintain', 25, ['While Maintsining Action'], vcells)
	vcells = vcell('scene', 14, ['Scene'], vcells)
	vcells = vcell('turn', 14, ['One Turn'], vcells)
	vcells = vcell('time', 17, [measure_type, 'Time Rank', time], vcells)
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

	cells  = check_cell('Per Rank', 9, rank, cells)
	body = send_multiple(title, cells, body)

	cells.clear()

	return (body)

def power_cost_post(entry, body, cells):
	
	keyword = entry.keyword
	cost = entry.cost
	rank = entry.rank
	flat = entry.flat
	extra = entry.extra

	cost = integer_convert(cost)
	rank = integer_convert(rank)

	extra = extra_name(extra_id)

	cells = cell('Keyword', 25, [keyword])
	cells = cell('Extra', 25, [extra], cells)
	cells = cell('Cost', 10, [cost], cells)
	cells = cell('Per Rank', 12, [rank], cells)
	cells = check_cell('Flat', 6, flat, cells)

	body = send(cells, body)


def power_ranks_post(entry, body, cells, base_cost, base_ranks):
	
	ranks = entry.ranks
	extra = entry.extra
	cost = entry.cost

	ranks = integer_convert(ranks)

	extra = extra_name(extra_id)

	calculated = ranks_function(cost, ranks, base_cost, base_ranks, extra)

	cells = cell('Extra', 25, [extra], cells)
	cells = cell('Ranks', 12, [ranks], cells)
	cells = cell('Cost', 12, [calculated], cells)

	body = send(cells, body)


def power_extra_post(entry, body, cells):

	name = entry.name
	cost = entry.cost
	ranks = entry.ranks
	des = entry.des
	inherit = entry.inherit
	alternate = entry.alternate
	flat = entry.flat


	cost = integer_convert(cost)
	ranks = integer_convert(ranks)
	inherit = get_name(inherit)

	cells = cell('Name', 23, [name])
	cells = cell('Cost', 12, [cost], cells)
	cells = cell('Ranks', 12, [ranks], cells)
	cells = check_cell('Flat Cost', 12, flat, cells)
	cells = circ_cell('Description', 'Description', 12, des, cells, body)
	cells = check_cell('Alternate Effect', 17, alternate, cells)

	body = send(cells, body)
