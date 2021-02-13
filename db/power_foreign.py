
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipFeature, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 


from error_functions import integer, required, power_check, one, field, rule_check, rule_select, cost_check, extra_cost, variable, select, variable_fields, variable_field, select_variable, together, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, select_of, id_check, extra_check, extra_convert, int_check, db_integer
from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, trait
from posts.equipment_posts import equip_belt_post, equip_check_post, equip_damaged_post, equip_descriptor_post, equip_effect_post, equip_feature_post, equip_limits_post, equip_modifiers_post, equip_opposed_post
from errors.equipment_errors import equip_belt_post_errors, equip_check_post_errors, equip_damaged_post_errors, equip_descriptor_post_errors, equip_effect_post_errors, equip_feature_post_errors, equip_limits_post_errors, equip_modifiers_post_errors, equip_opposed_post_errors, equip_save_errors, feature_save_errors



class Power(db.Model):

	power_type = integer(power_type)
	action = db_integer(Action, action)
	power_range = db_integer(Ranged, power_range)
	duration = integer(duration)
	check_type = db_integer(Check, check_type)
	skill = db_integer(Skill, skill)
	conflict = db_integer(ConflictAction, conflict)
	condition = db_integer(Condition, condition)
	
	
	
class Extra(db.Model):
	
	power_id = integer(power_id)
	inherit = integer(inherit)


class PowerAltCheck(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	check_type = db_integer(Check, check_type)


class PowerAction(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	action = db_integer(Action, action)


class PowerChar(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	limited_emotion = db_integer(Emotion, limited_emotion)


class PowerCirc(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	circ_range = db_integer(Ranged, circ_range)
	null_condition = db_integer(Condition, null_condition)


class PowerCreate(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	complexity = db_integer(Complex, complexity)
	move_opponent_ability = db_integer(Ability, move_opponent_ability)


class PowerDamage(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	damage_type = db_integer(Descriptor, damage_type)


class PowerDC(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	level = db_integer(Levels, level)


class PowerDefense(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	defense = db_integer(Defense, defense)
	reflect_action = db_integer(Action, reflect_action)
	reflect_check = db_integer(Check, reflect_check)
	immunity_damage = db_integer(Descriptor, immunity_damage)
	cover_type = db_integer(Cover, cover_type)


class PowerDegMod(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	measure_math = db_integer(Math, measure_math)
	measure_rank = db_integer(Rank, measure_rank)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	level = db_integer(Levels, level)
	consequence = db_integer(Consequence, consequence)




class PowerEnv(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	immunity_environment = db_integer(Environment, immunity_environment)
	move_nature = db_integer(Nature, move_nature)


class PowerMinion(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	condition = db_integer(Condition, condition)
	player_condition = db_integer(Condition, player_condition)
	attitude_type = db_integer(LevelType, attitude_type)
	attitude_attitude = db_integer(Levels, attitude_attitude)
	resitable_check = db_integer(Defense, resitable_check)


class PowerMod(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	objects_alone = db_integer(Defense, objects_alone)
	objects_character = db_integer(Defense, objects_character)
	limited_level = db_integer(Levels, limited_level)
	limited_extra = db_integer(Extra, limited_extra)
	limited_sense = db_integer(Sense, limited_sense)
	limited_range = db_integer(Range, limited_range)
	side_level = db_integer(Levels, side_level)
	reflect_check = db_integer(Check, reflect_check)


class PowerMove(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	condition = db_integer(Condition, condition)
	distance_math = db_integer(Math, distance_math)
	concealment_sense = db_integer(Sense, concealment_sense)
	ground_type = db_integer(Ground, ground_type)
	ground_units = db_integer(Unit, ground_units)
	objects_check = db_integer(Check, objects_check)
	objects_attack = db_integer(ConflictAction, objects_attack)
	damage_type = db_integer(Ability, damage_type)


class PowerOpposed(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)


class PowerRanged(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	flat_units = db_integer(Unit, flat_units)
	flat_rank_units = db_integer(Unit, flat_rank_units)
	units_rank_units = db_integer(Unit, units_rank_units)
	effect_mod_math = db_integer(Math, effect_mod_math)
	check_math = db_integer(Math, check_math)
	trait_math = db_integer(Math, trait_math)
	distance_mod_math = db_integer(Math, distance_mod_math)


class PowerResist(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	check_type = db_integer(Check, check_type)


class PowerResistBy(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	nullify_alternate = db_integer(Defense, nullify_alternate)


class PowerSenseEffect(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	sense = db_integer(Sense, sense)
	subsense = db_integer(SubSense, subsense)
	skill = db_integer(Skill, skill)
	height_ensense = db_integer(Power, height_ensense)
	lighting = db_integer(Light, lighting)
	time_unit = db_integer(Unit, time_unit)
	time_skill = db_integer(Skill, time_skill)
	time_bonus = db_integer(SkillBonus, time_bonus)
	distance_unit = db_integer(Unit, distance_unit)


class PowerReverse(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	time_unit = db_integer(Unit, time_unit)



class PowerTime(db.Model):

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)
	check_type = db_integer(Check, check_type)































class Power(db.Model):

	cost = integer(cost)
	limit = integer(limit)
	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	opponent_dc = integer(opponent_dc)
	routine_trait = integer(routine_trait)
	partner_trait = integer(partner_trait)
	partner_dc = integer(partner_dc)
	conflict_bonus = integer(conflict_bonus)


class Extra(db.Model):

	cost = integer(cost)
	ranks = integer(ranks)


class PowerAltCheck(db.Model):

	mod = integer(mod)
	trait = integer(trait)


class PowerAction(db.Model):

	mod = integer(mod)


class PowerChar(db.Model):

	trait = integer(trait)
	value = integer(value)
	increase = integer(increase)
	weaken_trait = integer(weaken_trait)
	weaken_descriptor = integer(weaken_descriptor)
	reduced_trait = integer(reduced_trait)
	reduced_value = integer(reduced_value)
	carry_capacity = integer(carry_capacity)
	points_value = integer(points_value)
	points_trait = integer(points_trait)
	points_descriptor = integer(points_descriptor)
	cost = integer(cost)
	ranks = integer(ranks)


class PowerCirc(db.Model):

	mod = integer(mod)
	rounds = integer(rounds)
	check_trait = integer(check_trait)
	null_descriptor = integer(null_descriptor)
	null_trait = integer(null_trait)


class PowerCreate(db.Model):

	volume = integer(volume)
	toughness = integer(toughness)
	mass = integer(mass)
	transform_start_mass = integer(transform_start_mass)
	transfom_mass = integer(transfom_mass)
	transform_start_descriptor = integer(transform_start_descriptor)
	transform_end_descriptor = integer(transform_end_descriptor)
	move_player_trait = integer(move_player_trait)
	move_opponent_rank = integer(move_opponent_rank)
	trap_dc = integer(trap_dc)
	trap_trait = integer(trap_trait)
	trap_resist_trait = integer(trap_resist_trait)
	trap_resist_dc = integer(trap_resist_dc)
	ranged_dc = integer(ranged_dc)
	ranged_trait = integer(ranged_trait)
	ranged_damage_value = integer(ranged_damage_value)
	weapon_trait = integer(weapon_trait)
	weapon_mod = integer(weapon_mod)
	weapon_damage = integer(weapon_damage)
	support_strength = integer(support_strength)
	support_action = integer(support_action)
	support_action_rounds = integer(support_action_rounds)
	support_effort = integer(support_effort)
	support_effort_rounds = integer(support_effort_rounds)
	cost = integer(cost)
	ranks = integer(ranks)


class PowerDamage(db.Model):

	trait = integer(trait)
	mod = integer(mod)
	descriptor = integer(descriptor)


class PowerDC(db.Model):

	value = integer(value)
	math_value = integer(math_value)
	math_trait = integer(math_trait)
	descriptor = integer(descriptor)
	check_trait = integer(check_trait)
	check_mod = integer(check_mod)


class PowerDefense(db.Model):

	mod = integer(mod)
	roll = integer(roll)
	reflect_dc = integer(reflect_dc)
	reflect_opposed_trait = integer(reflect_opposed_trait)
	reflect_resist_trait = integer(reflect_resist_trait)
	immunity_trait = integer(immunity_trait)
	immunity_descriptor = integer(immunity_descriptor)


class PowerDegMod(db.Model):

	value = integer(value)
	circ_value = integer(circ_value)
	circ_turns = integer(circ_turns)
	circ_trait = integer(circ_trait)
	measure_val1 = integer(measure_val1)
	measure_trait = integer(measure_trait)
	measure_value = integer(measure_value)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	nullify = integer(nullify)
	consequence_action = integer(consequence_action)
	consequence_trait = integer(consequence_trait)
	knowledge_count = integer(knowledge_count)


class PowerDegree(db.Model):

	degree = integer(degree)


class PowerEnv(db.Model):

	radius = integer(radius)
	distance = integer(distance)
	rank = integer(rank)
	move_speed = integer(move_speed)
	visibility_trait = integer(visibility_trait)
	visibility_mod = integer(visibility_mod)
	cost = integer(cost)
	ranks = integer(ranks)


class PowerMinion(db.Model):

	points = integer(points)
	sacrifice_cost = integer(sacrifice_cost)
	attitude_trait = integer(attitude_trait)
	resitable_dc = integer(resitable_dc)
	multiple_value = integer(multiple_value)


class PowerMod(db.Model):

	effortless_degree = integer(effortless_degree)
	effortless_retries = integer(effortless_retries)
	simultaneous_descriptor = integer(simultaneous_descriptor)
	area_mod = integer(area_mod)
	area_range = integer(area_range)
	area_descriptor = integer(area_descriptor)
	limited_mod = integer(limited_mod)
	limited_source = integer(limited_source)
	limited_trait = integer(limited_trait)
	limited_subjects = integer(limited_subjects)
	limited_degree = integer(limited_degree)
	limited_descriptor = integer(limited_descriptor)
	reflect_dc = integer(reflect_dc)
	reflect_trait = integer(reflect_trait)
	reflect_descriptor = integer(reflect_descriptor)
	subtle_opponent_trait = integer(subtle_opponent_trait)
	subtle_dc = integer(subtle_dc)
	subtle_null_trait = integer(subtle_null_trait)
	ranks_trait = integer(ranks_trait)
	ranks_ranks = integer(ranks_ranks)
	ranks_mod = integer(ranks_mod)
	points_reroll_cost = integer(points_reroll_cost)
	points_rerolls = integer(points_rerolls)
	ranks_cost = integer(ranks_cost)
	cost = integer(cost)


class PowerMove(db.Model):

	rank = integer(rank)
	mod = integer(mod)
	distance_value = integer(distance_value)
	distance_math_value = integer(distance_math_value)
	distance_math_value2 = integer(distance_math_value2)
	distance_mod = integer(distance_mod)
	dc = integer(dc)
	mass_value = integer(mass_value)
	extended_actions = integer(extended_actions)
	concealment_trait = integer(concealment_trait)
	permeate_speed = integer(permeate_speed)
	dimension_mass_rank = integer(dimension_mass_rank)
	dimension_descriptor = integer(dimension_descriptor)
	special_time_carry = integer(special_time_carry)
	ground_time = integer(ground_time)
	subtle_trait = integer(subtle_trait)
	subtle_mod = integer(subtle_mod)
	objects_skill = integer(objects_skill)
	check_trait = integer(check_trait)
	ranks = integer(ranks)
	cost = integer(cost)


class PowerOpposed(db.Model):

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)


class PowerRanged(db.Model):

	flat_value = integer(flat_value)
	flat_rank = integer(flat_rank)
	flat_rank_value = integer(flat_rank_value)
	flat_rank_rank = integer(flat_rank_rank)
	flat_rank_distance = integer(flat_rank_distance)
	flat_rank_distance_rank = integer(flat_rank_distance_rank)
	units_rank_start_value = integer(units_rank_start_value)
	units_rank_value = integer(units_rank_value)
	units_rank_rank = integer(units_rank_rank)
	rank_distance_start = integer(rank_distance_start)
	rank_distance = integer(rank_distance)
	rank_effect_rank = integer(rank_effect_rank)
	effect_mod = integer(effect_mod)
	check_trait = integer(check_trait)
	check_mod = integer(check_mod)
	trait_trait = integer(trait_trait)
	trait_mod = integer(trait_mod)
	distance_mod_rank = integer(distance_mod_rank)
	distance_mod_trait = integer(distance_mod_trait)
	dc_value = integer(dc_value)
	dc_trait = integer(dc_trait)


class PowerResist(db.Model):

	mod = integer(mod)
	rounds = integer(rounds)
	trait = integer(trait)
	descriptor = integer(descriptor)
	check_trait = integer(check_trait)


class PowerResistBy(db.Model):

	trait = integer(trait)
	dc = integer(dc)
	mod = integer(mod)
	degree = integer(degree)
	descriptor = integer(descriptor)
	weaken_max = integer(weaken_max)
	weaken_restored = integer(weaken_restored)
	damage = integer(damage)
	nullify_descriptor = integer(nullify_descriptor)



class PowerSenseEffect(db.Model):

	sense_cost = integer(sense_cost)
	subsense_cost = integer(subsense_cost)
	height_trait = integer(height_trait)
	resist_trait = integer(resist_trait)
	resist_circ = integer(resist_circ)
	time_value = integer(time_value)
	time_factor = integer(time_factor)
	distance_dc = integer(distance_dc)
	distance_mod = integer(distance_mod)
	distance_value = integer(distance_value)
	distance_factor = integer(distance_factor)
	ranks = integer(ranks)
	cost = integer(cost)


class PowerReverse(db.Model):

	degree = integer(degree)
	trait = integer(trait)
	value_dc = integer(value_dc)
	math_dc = integer(math_dc)
	time_value = integer(time_value)



class PowerTime(db.Model):

	value = integer(value)
	time_value = integer(time_value)
	trait = integer(trait)
	dc = integer(dc)
	descriptor = integer(descriptor)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)












































class Power(db.Model):

	power_type = integer(power_type)
	action = get_name(Action, action)
	power_range = get_name(Ranged, power_range)
	duration = get_name(duration)
	check_type = get_name(Check, check_type)
	skill = get_name(Skill, skill)
	conflict = get_name(ConflictAction, conflict)
	condition = get_name(Condition, condition)
	
	
	
class Extra(db.Model):
	
	power_id = integer(power_id)
	inherit = integer(inherit)


class PowerAltCheck(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	check_type = get_name(Check, check_type)


class PowerAction(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	action = get_name(Action, action)


class PowerChar(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	limited_emotion = get_name(Emotion, limited_emotion)


class PowerCirc(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	circ_range = get_name(Ranged, circ_range)
	null_condition = get_name(Condition, null_condition)


class PowerCreate(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	complexity = get_name(Complex, complexity)
	move_opponent_ability = get_name(Ability, move_opponent_ability)


class PowerDamage(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	damage_type = get_name(Descriptor, damage_type)


class PowerDC(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	math = get_name(Math, math)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	level = get_name(Levels, level)


class PowerDefense(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	defense = get_name(Defense, defense)
	reflect_action = get_name(Action, reflect_action)
	reflect_check = get_name(Check, reflect_check)
	immunity_damage = get_name(Descriptor, immunity_damage)
	cover_type = get_name(Cover, cover_type)


class PowerDegMod(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	measure_math = get_name(Math, measure_math)
	measure_rank = get_name(Rank, measure_rank)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	level = get_name(Levels, level)
	consequence = get_name(Consequence, consequence)




class PowerEnv(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	immunity_environment = get_name(Environment, immunity_environment)
	move_nature = get_name(Nature, move_nature)


class PowerMinion(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	condition = get_name(Condition, condition)
	player_condition = get_name(Condition, player_condition)
	attitude_type = get_name(LevelType, attitude_type)
	attitude_attitude = get_name(Levels, attitude_attitude)
	resitable_check = get_name(Defense, resitable_check)


class PowerMod(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	objects_alone = get_name(Defense, objects_alone)
	objects_character = get_name(Defense, objects_character)
	limited_level = get_name(Levels, limited_level)
	limited_extra = get_name(Extra, limited_extra)
	limited_sense = get_name(Sense, limited_sense)
	limited_range = get_name(Range, limited_range)
	side_level = get_name(Levels, side_level)
	reflect_check = get_name(Check, reflect_check)


class PowerMove(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	

class PowerOpposed(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)


class PowerRanged(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	flat_units = get_name(Unit, flat_units)
	flat_rank_units = get_name(Unit, flat_rank_units)
	units_rank_units = get_name(Unit, units_rank_units)
	effect_mod_math = get_name(Math, effect_mod_math)
	check_math = get_name(Math, check_math)
	trait_math = get_name(Math, trait_math)
	distance_mod_math = get_name(Math, distance_mod_math)


class PowerResist(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	check_type = get_name(Check, check_type)


class PowerResistBy(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	nullify_alternate = get_name(Defense, nullify_alternate)


class PowerSenseEffect(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	sense = get_name(Sense, sense)
	subsense = get_name(SubSense, subsense)
	skill = get_name(Skill, skill)
	height_ensense = get_name(Power, height_ensense)
	lighting = get_name(Light, lighting)
	time_unit = get_name(Unit, time_unit)
	time_skill = get_name(Skill, time_skill)
	time_bonus = get_name(SkillBonus, time_bonus)
	distance_unit = get_name(Unit, distance_unit)


class PowerReverse(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	math = get_name(Math, math)
	time_unit = get_name(Unit, time_unit)



class PowerTime(db.Model):

	power_id = integer(power_id)
	extra_id = get_name(Extra, extra_id)
	units = get_name(Unit, units)
	math = get_name(Math, math)
	check_type = get_name(Check, check_type)






