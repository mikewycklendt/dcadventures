
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

	dc_value = db.Column(db.Integer)
	dc_mod = db.Column(db.Integer)
	targets = db.Column(db.Integer)
	speed_turns = db.Column(db.Integer)
	speed_mod = db.Column(db.Integer)
	speed_value = db.Column(db.Integer)
	modifiers_multiple_count = db.Column(db.Integer)




class SkillAbility(db.Model):


class SkillCheck(db.Model):

	mod = db.Column(db.Integer)
	trait = db.Column(db.Integer)
	action = db.Column(db.Integer)


class SkillCirc(db.Model):

	mod = db.Column(db.Integer)
	speed = db.Column(db.Integer)
	temp = db.Column(db.Integer)
	time = db.Column(db.Integer)
	conditions = db.Column(db.Integer)
	conditions_effect = db.Column(db.Integer)
	measure_rank_value = db.Column(db.Integer)
	unit_value = db.Column(db.Integer)
	measure_trait = db.Column(db.Integer)
	measure_mod = db.Column(db.Integer)
	turns = db.Column(db.Integer)
	unit_time = db.Column(db.Integer)
	time_rank = db.Column(db.Integer)


class SkillDC(db.Model):

	value = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math_trait = db.Column(db.Integer)
	inflict_flat = db.Column(db.Integer)
	inflict_trait = db.Column(db.Integer)
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	measure_rank_value = db.Column(db.Integer)
	unit_value = db.Column(db.Integer)
	measure_trait = db.Column(db.Integer)
	measure_mod = db.Column(db.Integer)
	condition_turns = db.Column(db.Integer)


class SkillDegree(db.Model):

	value = db.Column(db.Integer)
	time = db.Column(db.Integer)
	object = db.Column(db.Integer)
	inflict_flat = db.Column(db.Integer)
	inflict_trait = db.Column(db.Integer)
	inflict_mod = db.Column(db.Integer)
	inflict_bonus = db.Column(db.Integer)
	damage_mod = db.Column(db.Integer)
	consequence_action = db.Column(db.Integer)
	consequence_trait = db.Column(db.Integer)
	knowledge_count = db.Column(db.Integer)
	level_direction = db.Column(db.Integer)
	measure_rank_value = db.Column(db.Integer)
	unit_value = db.Column(db.Integer)
	measure_trait = db.Column(db.Integer)
	measure_mod = db.Column(db.Integer)
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition_turns = db.Column(db.Integer)
	nullify = db.Column(db.Integer)


class SkillMod(db.Model):

	bonus = db.Column(db.Integer)
	penalty = db.Column(db.Integer)
	bonus_trait = db.Column(db.Integer)
	bonus_check = db.Column(db.Integer)
	bonus_check_range = db.Column(db.Integer)
	penalty_trait = db.Column(db.Integer)
	penalty_check = db.Column(db.Integer)
	penalty_check_range = db.Column(db.Integer)
	multiple_count = db.Column(db.Integer)
	lasts = db.Column(db.Integer)


class SkillOpposed(db.Model):

	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	opponent_trait = db.Column(db.Integer)
	opponent_mod = db.Column(db.Integer)
	recurring_value = db.Column(db.Integer)


class SkillTime(db.Model):

	rank1_value = db.Column(db.Integer)
	rank2_value = db.Column(db.Integer)
	value = db.Column(db.Integer)
	trait = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)



































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






