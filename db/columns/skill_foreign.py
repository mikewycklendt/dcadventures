
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




class SkillBonus(db.Model):


	ability = db_integer(Ability, ability)
	skill = db_integer(Skill, skill)
	check_type = db_integer(Check, check_type)
	action = db_integer(Action, action)
	type = db_integer(SkillType, type)
	condition = db_integer(Condition, condition)
	advantage = db_integer(Advantage, advantage)
	concealment = db_integer(Conceal, concealment)
	weapon_cat = db_integer(WeaponCat, weapon_cat)
	weapon_type = db_integer(WeaponType, weapon_type)
	weapon = db_integer(Weapon, weapon)



class SkillAbility(db.Model):


	skill_id = integer(skill_id)
	ability = db_integer(Ability, ability)


class SkillCheck(db.Model):

	skill_id = integer(skill_id)
	check_type = db_integer(Check, check_type)
	conflict = db_integer(ConflictAction, conflict)
	conflict_range = db_integer(Ranged, conflict_range)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)

class SkillCirc(db.Model):

	skill_id = integer(skill_id)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	time_units = db_integer(Unit, time_units)

class SkillDC(db.Model):

	skill_id = integer(skill_id)
	math = db_integer(Math, math)
	action = db_integer(Action, action)
	inflict_math = db_integer(Math, inflict_math)
	damage_consequence = db_integer(Consequence, damage_consequence)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Math, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	complexity = db_integer(Complex, complexity)


class SkillDegree(db.Model):

	skill_id = integer(skill_id)
	action = db_integer(Action, action)
	inflict_math = db_integer(Math, inflict_math)
	damage_consequence = db_integer(Consequence, damage_consequence)
	consequence = db_integer(Consequence, consequence)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	circumstance = integer(circumstance)
	measure_rank = db_integer(Rank, measure_rank)
	unit_type = db_integer(MeasureType, unit_type)
	unit = db_integer(Unit, unit)
	measure_trait_math = db_integer(Msth, measure_trait_math)
	measure_math_rank = db_integer(Rank, measure_math_rank)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)

class SkillMod(db.Model):

	skill_id = integer(skill_id)
	environment = db_integer(Environment, environment)
	sense = db_integer(Sense, sense)
	mod_range = db_integer(Ranged, mod_range)
	subsense = db_integer(SubSense, subsense)
	cover = db_integer(Cover, cover)
	conceal = db_integer(Conceal, conceal)
	maneuver = db_integer(Maneuver, maneuver)
	weapon_melee = db_integer(WeaponType, weapon_melee)
	weapon_ranged = db_integer(WeaponType,  weapon_ranged)
	condition = db_integer(Condition, condition)
	power = db_integer(Power, power)
	consequence = db_integer(Consequence, consequence)
	creature = db_integer(Creature, creature)
	emotion = db_integer(Emotion, emotion)
	conflict = db_integer(ConflictAction, conflict)
	profession = db_integer(Job, profession)
	bonus_conflict = db_integer(ConflictAction, bonus_conflict)
	penalty_conflict = db_integer(ConflictAction, penalty_conflict)
	skill = db_integer(Skill, skill)
	light = db_integer(Light, light)
	bonus_check = db_integer(Check, bonus_check)
	bonus_check_range = db_integer(Ranged, bonus_check_range)
	penalty_check = db_integer(Check, penalty_check)
	penalty_check_range = db_integer(Ranged, penalty_check_range)


class SkillOpposed(db.Model):

	skill_id = integer(skill_id)
	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)
	recurring_units = db_integer(Unit, recurring_units)


class SkillTime(db.Model):

	skill_id = integer(skill_id)
	rank1 = db_integer(Rank, rank1)
	rank_math = db_integer(Math, rank_math)
	rank2 = db_integer(Rank, rank2)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)





































class SkillBonus(db.Model):

	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	targets = integer(targets)
	speed_turns = integer(speed_turns)
	speed_mod = integer(speed_mod)
	speed_value = integer(speed_value)
	modifiers_multiple_count = integer(modifiers_multiple_count)




class SkillAbility(db.Model):


class SkillCheck(db.Model):

	mod = integer(mod)
	trait = integer(trait)
	action = integer(action)


class SkillCirc(db.Model):

	mod = integer(mod)
	speed = integer(speed)
	temp = integer(temp)
	time = integer(time)
	conditions = integer(conditions)
	conditions_effect = integer(conditions_effect)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	turns = integer(turns)
	unit_time = integer(unit_time)
	time_rank = integer(time_rank)


class SkillDC(db.Model):

	value = integer(value)
	mod = integer(mod)
	math_value = integer(math_value)
	math_trait = integer(math_trait)
	inflict_flat = integer(inflict_flat)
	inflict_trait = integer(inflict_trait)
	inflict_mod = integer(inflict_mod)
	inflict_bonus = integer(inflict_bonus)
	damage_mod = integer(damage_mod)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	condition_turns = integer(condition_turns)


class SkillDegree(db.Model):

	value = integer(value)
	time = integer(time)
	object = integer(object)
	inflict_flat = integer(inflict_flat)
	inflict_trait = integer(inflict_trait)
	inflict_mod = integer(inflict_mod)
	inflict_bonus = integer(inflict_bonus)
	damage_mod = integer(damage_mod)
	consequence_action = integer(consequence_action)
	consequence_trait = integer(consequence_trait)
	knowledge_count = integer(knowledge_count)
	level_direction = integer(level_direction)
	measure_rank_value = integer(measure_rank_value)
	unit_value = integer(unit_value)
	measure_trait = integer(measure_trait)
	measure_mod = integer(measure_mod)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	condition_turns = integer(condition_turns)
	nullify = integer(nullify)


class SkillMod(db.Model):

	bonus = integer(bonus)
	penalty = integer(penalty)
	bonus_trait = integer(bonus_trait)
	penalty_trait = integer(penalty_trait)
	multiple_count = integer(multiple_count)
	lasts = integer(lasts)


class SkillOpposed(db.Model):

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)
	recurring_value = integer(recurring_value)


class SkillTime(db.Model):

	rank1_value = integer(rank1_value)
	rank2_value = integer(rank2_value)
	value = integer(value)
	trait = integer(trait)
	math_value = integer(math_value)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)



































class SkillAbility(db.Model):


	skill_id = integer(skill_id)
	ability = get_name(Ability, ability)


class SkillCheck(db.Model):

	skill_id = integer(skill_id)
	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

class SkillCirc(db.Model):

	skill_id = integer(skill_id)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = get_name(Math, measure_trait_math)
	measure_math_rank = get_name(Rank, measure_math_rank)
	time_units = get_name(Unit, time_units)

class SkillDC(db.Model):

	skill_id = integer(skill_id)
	math = get_name(Math, math)
	action = get_name(Action, action)
	inflict_math = get_name(Math, inflict_math)
	damage_consequence = get_name(Consequence, damage_consequence)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = get_name(Math, measure_trait_math)
	measure_math_rank = get_name(Rank, measure_math_rank)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	complexity = get_name(Complex, complexity)


class SkillDegree(db.Model):

	skill_id = integer(skill_id)
	action = get_name(Action, action)
	inflict_math = get_name(Math, inflict_math)
	damage_consequence = get_name(Consequence, damage_consequence)
	consequence = get_name(Consequence, consequence)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	circumstance = get_name(circumstance)
	measure_rank = get_name(Rank, measure_rank)
	unit_type = get_name(MeasureType, unit_type)
	unit = get_name(Unit, unit)
	measure_trait_math = get_name(Msth, measure_trait_math)
	measure_math_rank = get_name(Rank, measure_math_rank)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

class SkillMod(db.Model):

	skill_id = integer(skill_id)
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


class SkillOpposed(db.Model):

	skill_id = integer(skill_id)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)
	recurring_units = get_name(Unit, recurring_units)


class SkillTime(db.Model):

	skill_id = integer(skill_id)
	rank1 = get_name(Rank, rank1)
	rank_math = get_name(Math, rank_math)
	rank2 = get_name(Rank, rank2)
	units = get_name(Unit, units)
	math = get_name(Math, math)






