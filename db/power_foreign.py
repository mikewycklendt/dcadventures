
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

	cost = integer()
	limit = integer()
	dc_value = integer()
	dc_mod = integer()
	opponent_dc = integer()
	routine_trait = integer()
	partner_trait = integer()
	partner_dc = integer()
	conflict_bonus = integer()


class Extra(db.Model):

	cost = integer()
	ranks = integer()


class PowerAltCheck(db.Model):

	mod = integer()
	trait = integer()


class PowerAction(db.Model):

	mod = integer()


class PowerChar(db.Model):

	trait = integer()
	value = integer()
	increase = integer()
	weaken_trait = integer()
	weaken_descriptor = integer()
	reduced_trait = integer()
	reduced_value = integer()
	carry_capacity = integer()
	points_value = integer()
	points_trait = integer()
	points_descriptor = integer()
	cost = integer()
	ranks = integer()


class PowerCirc(db.Model):

	mod = integer()
	rounds = integer()
	check_trait = integer()
	null_descriptor = integer()
	null_trait = integer()


class PowerCreate(db.Model):

	volume = integer()
	toughness = integer()
	mass = integer()
	transform_start_mass = integer()
	transfom_mass = integer()
	transform_start_descriptor = integer()
	transform_end_descriptor = integer()
	move_player_trait = integer()
	move_opponent_rank = integer()
	trap_dc = integer()
	trap_trait = integer()
	trap_resist_trait = integer()
	trap_resist_dc = integer()
	ranged_dc = integer()
	ranged_trait = integer()
	ranged_damage_value = integer()
	weapon_trait = integer()
	weapon_mod = integer()
	weapon_damage = integer()
	support_strength = integer()
	support_action = integer()
	support_action_rounds = integer()
	support_effort = integer()
	support_effort_rounds = integer()
	cost = integer()
	ranks = integer()


class PowerDamage(db.Model):

	trait = integer()
	mod = integer()
	descriptor = integer()


class PowerDC(db.Model):

	value = integer()
	math_value = integer()
	math_trait = integer()
	descriptor = integer()
	check_trait = integer()
	check_mod = integer()


class PowerDefense(db.Model):

	mod = integer()
	roll = integer()
	reflect_dc = integer()
	reflect_opposed_trait = integer()
	reflect_resist_trait = integer()
	immunity_trait = integer()
	immunity_descriptor = integer()


class PowerDegMod(db.Model):

	value = integer()
	circ_value = integer()
	circ_turns = integer()
	circ_trait = integer()
	measure_val1 = integer()
	measure_trait = integer()
	measure_value = integer()
	condition_damage_value = integer()
	condition_damage = integer()
	nullify = integer()
	consequence_action = integer()
	consequence_trait = integer()
	knowledge_count = integer()


class PowerDegree(db.Model):

	degree = integer()


class PowerEnv(db.Model):

	radius = integer()
	distance = integer()
	rank = integer()
	move_speed = integer()
	visibility_trait = integer()
	visibility_mod = integer()
	cost = integer()
	ranks = integer()


class PowerMinion(db.Model):

	points = integer()
	sacrifice_cost = integer()
	attitude_trait = integer()
	resitable_dc = integer()
	multiple_value = integer()


class PowerMod(db.Model):

	effortless_degree = integer()
	effortless_retries = integer()
	simultaneous_descriptor = integer()
	area_mod = integer()
	area_range = integer()
	area_descriptor = integer()
	limited_mod = integer()
	limited_source = integer()
	limited_trait = integer()
	limited_subjects = integer()
	limited_degree = integer()
	limited_descriptor = integer()
	reflect_dc = integer()
	reflect_trait = integer()
	reflect_descriptor = integer()
	subtle_opponent_trait = integer()
	subtle_dc = integer()
	subtle_null_trait = integer()
	ranks_trait = integer()
	ranks_ranks = integer()
	ranks_mod = integer()
	points_reroll_cost = integer()
	points_rerolls = integer()
	ranks_cost = integer()
	cost = integer()


class PowerMove(db.Model):

	rank = integer()
	mod = integer()
	distance_value = integer()
	distance_math_value = integer()
	distance_math_value2 = integer()
	distance_mod = integer()
	dc = integer()
	mass_value = integer()
	extended_actions = integer()
	concealment_trait = integer()
	permeate_speed = integer()
	dimension_mass_rank = integer()
	dimension_descriptor = integer()
	special_time_carry = integer()
	ground_time = integer()
	subtle_trait = integer()
	subtle_mod = integer()
	objects_skill = integer()
	check_trait = integer()
	ranks = integer()
	cost = integer()


class PowerOpposed(db.Model):

	trait = integer()
	mod = integer()
	opponent_trait = integer()
	opponent_mod = integer()


class PowerRanged(db.Model):

	flat_value = integer()
	flat_rank = integer()
	flat_rank_value = integer()
	flat_rank_rank = integer()
	flat_rank_distance = integer()
	flat_rank_distance_rank = integer()
	units_rank_start_value = integer()
	units_rank_value = integer()
	units_rank_rank = integer()
	rank_distance_start = integer()
	rank_distance = integer()
	rank_effect_rank = integer()
	effect_mod = integer()
	check_trait = integer()
	check_mod = integer()
	trait_trait = integer()
	trait_mod = integer()
	distance_mod_rank = integer()
	distance_mod_trait = integer()
	dc_value = integer()
	dc_trait = integer()


class PowerResist(db.Model):

	mod = integer()
	rounds = integer()
	trait = integer()
	descriptor = integer()
	check_trait = integer()


class PowerResistBy(db.Model):

	trait = integer()
	dc = integer()
	mod = integer()
	degree = integer()
	descriptor = integer()
	weaken_max = integer()
	weaken_restored = integer()
	damage = integer()
	nullify_descriptor = integer()



class PowerSenseEffect(db.Model):

	sense_cost = integer()
	subsense_cost = integer()
	height_trait = integer()
	resist_trait = integer()
	resist_circ = integer()
	time_value = integer()
	time_factor = integer()
	distance_dc = integer()
	distance_mod = integer()
	distance_value = integer()
	distance_factor = integer()
	ranks = integer()
	cost = integer()


class PowerReverse(db.Model):

	degree = integer()
	trait = integer()
	value_dc = integer()
	math_dc = integer()
	time_value = integer()



class PowerTime(db.Model):

	value = integer()
	time_value = integer()
	trait = integer()
	dc = integer()
	descriptor = integer()
	recovery_penalty = integer()
	recovery_time = integer()












































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
	math = get_name(Math, math)
	condition = get_name(Condition, condition)
	distance_math = get_name(Math, distance_math)
	concealment_sense = get_name(Sense, concealment_sense)
	ground_type = get_name(Ground, ground_type)
	ground_units = get_name(Unit, ground_units)
	objects_check = get_name(Check, objects_check)
	objects_attack = get_name(ConflictAction, objects_attack)
	damage_type = get_name(Ability, damage_type)


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






