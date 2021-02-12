
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


class Advantage(db.Model):

	adv_type = integer(adv_type)
	action = db_integer(Action, action)
	check_type = db_integer(Check, check_type)
	expertise = db_integer(SkillBonus, expertise)
	conflict = db_integer(ConflictAction, conflict)
	consequence = db_integer(Consequence, consequence)
	conflict_immune = db_integer(ConflictAction, conflict_immune)
	action1 = db_integer(Action, action1)
	action2 = db_integer(Action, action2)
	
	
	
class AdvAltCheck(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	check_type = db_integer(Check, check_type)
	conflict = db_integer(ConflictAction, conflict)
	conflict_range = db_integer(Ranged, conflict_range)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	
	
class AdvCirc(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	circ_range = db_integer(Ranged, circ_range)
	conflict = db_integer(ConflictAction, conflict)
	null_condition = db_integer(Condition, null_condition)
	
		
		
	
	
class AdvCondition(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition = db_integer(Condition, condition)
	condition_null = db_integer(Condition, condition_null)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	
	
class AdvDC(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	math_math = db_integer(Math, math_math)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	
	
class AdvDegree(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	consequence = db_integer(Consequence, consequence)
	level_type = db_integer(LevelType, level_type)
	level = db_integer(Levels, level)
	measure_math = db_integer(Math, measure_math)
	measure_rank = db_integer(Rank, measure_rank)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	
	
class AdvEffort(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	benefit_choice = db_integer(Benefit, benefit_choice)
	
	
class AdvMinion(db.Model):
	
	advantage_id = integer(advantage_id)
	condition = db_integer(Condition, condition)
	player_condition = db_integer(Condition, player_condition)
	attitude_type = db_integer(LevelType, attitude_type)
	attitude_attitude = db_integer(Levels, attitude_attitude)
	resitable_check = db_integer(Defense, resitable_check)
	
	
class AdvMod(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)

	sense = db_integer(Sense, sense)
	mod_range = db_integer(Ranged, mod_range)
	subsense = db_integer(SubSense, subsense)
	cover = db_integer(Cover, cover)
	conceal = db_integer(Conceal, conceal)
	maneuver = db_integer(Maneuver, maneuver)
	weapon_melee = db_integer(WeaponType, weapon_melee)
	weapon_ranged = db_integer(WeaponType, weapon_ranged)
	condition = db_integer(Condition, condition)
	power = db_integer(Power, power)
	consequence = db_integer(Consequence, consequence)
	creature = db_integer(Creature, creature)
	emotion = db_integer(Emotion, emotion)
	conflict = db_integer(ConflictAction, conflict)
	profession = db_integer(Job, profession)
	bonus_conflict = db_integer(ConflictAction, bonus_conflict)
	penalty_conflict = db_integer(ConflictAction, penalty_conflict)
	bonus_check = db_integer(Check, bonus_check)
	bonus_check_range = db_integer(Ranged, bonus_check_range)
	penalty_check = db_integer(Check, penalty_check)
	penalty_check_range = db_integer(Ranged, penalty_check_range)
	
	
class AdvOpposed(db.Model):

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)


class AdvPoints(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	benefit_choice = db_integer(Benefit, benefit_choice)
	
	
class AdvResist(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	
class AdvRounds(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	cost = db_integer(Action, cost)
	check = db_integer(Check, check)
	


class AdvTime(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)
	check_type = db_integer(Check, check_type)




























class Advantage(db.Model):


	ranked_ranks = integer(ranked_ranks)
	ranked_max = integer(ranked_max)
	trait = integer(trait)
	replaced_trait = integer(replaced_trait)
	skill = integer(skill)
	dc_value = integer(dc_value)
	dc_mod = integer(dc_mod)
	invent_trait = integer(invent_trait)
	gm_trait = integer(gm_trait)
	languages = integer(languages)
	language_rank = integer(language_rank)
	mods_count = integer(mods_count)



class AdvAltCheck(db.Model):

	mod = integer(mod)
	trait = integer(trait)
	action = integer(action)

class AdvCirc(db.Model):

	mod = integer(mod)
	rounds = integer(rounds)
	check_trait = integer(check_trait)
	null_trait = integer(null_trait)
	null_override_trait = integer(null_override_trait)

	
class AdvCombined(db.Model):

	ranks = integer(ranks)


class AdvCondition(db.Model):

	damage_value = integer(damage_value)
	damage = integer(damage)


class AdvDC(db.Model):

	value_value = integer(value_value)
	math_value = integer(math_value)
	math_trait = integer(math_trait)
	check_trait = integer(check_trait)
	check_mod = integer(check_mod)



class AdvDegree(db.Model):

	value = integer(value)
	consequence_action = integer(consequence_action)
	consequence_trait = integer(consequence_trait)
	knowledge_count = integer(knowledge_count)
	circ_value = integer(circ_value)
	circ_turns = integer(circ_turns)
	circ_trait = integer(circ_trait)
	measure_val1 = integer(measure_val1)
	measure_trait = integer(measure_trait)
	measure_value = integer(measure_value)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	nullify = integer(nullify)
	
	
class AdvEffort(db.Model):
	
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	benefit_turns = integer(benefit_turns)
	benefit_count = integer(benefit_count)

	
class AdvMinion(db.Model):
	
	points = integer(points)
	sacrifice_cost = integer(sacrifice_cost)
	attitude_trait = integer(attitude_trait)
	resitable_dc = integer(resitable_dc)
	multiple_value = integer(multiple_value)
	
	
class AdvMod(db.Model):

	bonus = integer(bonus)
	penalty = integer(penalty)
	bonus_trait = integer(bonus_trait)
	bonus_check = integer(bonus_check)
	bonus_check_range = integer(bonus_check_range)
	penalty_trait = integer(penalty_trait)
	penalty_check = integer(penalty_check)
	penalty_check_range = integer(penalty_check_range)
	multiple_count = integer(multiple_count)
	lasts = integer(lasts)


class AdvOpposed(db.Model):
	
	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)


class AdvPoints(db.Model):

	condition_cost = integer(condition_cost)
	equipment_points = integer(equipment_points)
	initiative_cost = integer(initiative_cost)
	twenty = integer(twenty)
	check_bonus = integer(check_bonus)
	check_cost = integer(check_cost)
	check_turns = integer(check_turns)
	benefit_count = integer(benefit_count)
	benefit_cost = integer(benefit_cost)
	benefit_turns = integer(benefit_turns)
	ranks_gained = integer(ranks_gained)
	ranks_max = integer(ranks_max)
	ranks_lasts = integer(ranks_lasts)
	ranks_trait = integer(ranks_trait)


class AdvResist(db.Model):

	trait = integer(trait)
	mod = integer(mod)


class AdvRounds(db.Model):

	rounds = integer(rounds)
	trait = integer(trait)


class AdvSkill(db.Model):

	trait = integer(trait)
	replaced_trait = integer(replaced_trait)


class AdvTime(db.Model):

	value = integer(value)
	time_value = integer(time_value)
	trait = integer(trait)
	dc = integer(dc)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)
	
	
class AdvVariable(db.Model):
	trait = integer(trait)
	









	









class Advantage(db.Model):

	adv_type = integer(adv_type)
	action = get_name(Action, action)
	check_type = get_name(Check, check_type)
	expertise = get_name(SkillBonus, expertise)
	conflict = get_name(ConflictAction, conflict)
	consequence = get_name(Consequence, consequence)
	conflict_immune = get_name(ConflictAction, conflict_immune)
	action1 = get_name(Action, action1)
	action2 = get_name(Action, action2)
	
	
	
class AdvAltCheck(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	
	
class AdvCirc(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	circ_range = get_name(Ranged, circ_range)
	conflict = get_name(ConflictAction, conflict)
	null_condition = get_name(Condition, null_condition)
	
	
class AdvCondition(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition = get_name(Condition, condition)
	condition_null = get_name(Condition, condition_null)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	
	
class AdvDC(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	math_math = get_name(Math, math_math)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	
	
class AdvDegree(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	consequence = get_name(Consequence, consequence)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	measure_math = get_name(Math, measure_math)
	measure_rank = get_name(Rank, measure_rank)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	
	
class AdvEffort(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	benefit_choice = get_name(Benefit, benefit_choice)
	
	
class AdvMinion(db.Model):
	
	advantage_id = integer(advantage_id)
	condition = get_name(Condition, condition)
	player_condition = get_name(Condition, player_condition)
	attitude_type = get_name(LevelType, attitude_type)
	attitude_attitude = get_name(Levels, attitude_attitude)
	resitable_check = get_name(Defense, resitable_check)
	
	
class AdvMod(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)

	sense = get_name(Sense, sense)
	mod_range = get_name(Ranged, mod_range)
	subsense = get_name(SubSense, subsense)
	cover = get_name(Cover, cover)
	conceal = get_name(Conceal, conceal)
	maneuver = get_name(Maneuver, maneuver)
	weapon_melee = get_name(WeaponType, weapon_melee)
	weapon_ranged = get_name(WeaponType, weapon_ranged)
	condition = get_name(Condition, condition)
	power = get_name(Power, power)
	consequence = get_name(Consequence, consequence)
	creature = get_name(Creature, creature)
	emotion = get_name(Emotion, emotion)
	conflict = get_name(ConflictAction, conflict)
	profession = get_name(Job, profession)
	bonus_conflict = get_name(ConflictAction, bonus_conflict)
	penalty_conflict = get_name(ConflictAction, penalty_conflict)
	bonus_check = get_name(Check, bonus_check)
	bonus_check_range = get_name(Ranged, bonus_check_range)
	penalty_check = get_name(Check, penalty_check)
	penalty_check_range = get_name(Ranged, penalty_check_range)
	
	
class AdvOpposed(db.Model):

	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)


class AdvPoints(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	benefit_choice = get_name(Benefit, benefit_choice)
	
	
class AdvResist(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	
class AdvRounds(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	cost = get_name(Action, cost)
	check = get_name(Check, check)
	


class AdvTime(db.Model):
	
	advantage_id = integer(advantage_id)
	benefit = integer(benefit)
	units = get_name(Unit, units)
	math = get_name(Math, math)
	check_type = get_name(Check, check_type)
	
	
	
	