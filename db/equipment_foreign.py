
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




class Equipment(db.Model):

	type_id = integer(type_id)
	expertise = db_integer(SkillBonus, expertise)
	
	
class Feature(db.Model):
	
	equip_id = integer(equip_id)
	
	
class EquipFeature(db.Model):
	
	equip_id = integer(equip_id)
	feature = integer(feature)
	

class EquipEffect(db.Model):
	
	equip_id = integer(equip_id)
	
	
class EquipBelt(db.Model):
	
	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	weapon = db_integer(Weapon, weapon)
	equipment = db_integer(Equipment, equipment)
	
	
class EquipCheck(db.Model):
	
	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

	skill_type = db_integer(Skill, skill_type)
	skill = db_integer(SkillBonus, skill)
	check_type = db_integer(Check, check_type)
	action = db_integer(Action, action)
	
	
class EquipDamage(db.Model):
	
	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

	damage = db_integer(Descriptor, damage)
	skill_type = db_integer(Skill, skill_type)
	skill = db_integer(SkillBonus, skill)
	
	
class EquipDescriptor(db.Model):
	
	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

	descriptor = db_integer(Descriptor, descriptor)


class EquipLimit(db.Model):

	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

	time_units = db_integer(Unit, time_units)
	range_units = db_integer(Unit, range_units)
	time_capacity_units = db_integer(Unit, time_capacity_units)
	area_units = db_integer(Unit, area_units)
	light = db_integer(Light, light)

	
class EquipMod(db.Model):


	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

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

	
class EquipOpposed(db.Model):


	equip_id = integer(equip_id)
	feature = db_integer(Feature, feature)
	effect = db_integer(EquipEffect, effect)

	skill_type = db_integer(Skill, skill_type)
	skill = db_integer(SkillBonus, skill)
	check = db_integer(Check, check)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)




































class Equipment(db.Model):

	cost = integer(cost)
	toughness = integer(toughness)
	speed_mod = integer(speed_mod)
	mod_multiple_count = integer(mod_multiple_count)


class Feature(db.Model):

	toughness = integer(toughness)


	
class EquipBelt(db.Model):

	cost = integer(cost)

	
class EquipCheck(db.Model):


class EquipDamage(db.Model):

	toughness = integer(toughness)

	
class EquipDescriptor(db.Model):

	
class EquipLimit(db.Model):

	time = integer(time)
	range = integer(range)
	time_capacity = integer(time_capacity)
	capacity = integer(capacity)
	area_long = integer(area_long)
	area_wide = integer(area_wide)
	uses = integer(uses)

	
class EquipMod(db.Model):

	bonus = integer(bonus)
	penalty = integer(penalty)
	bonus_trait = integer(bonus_trait)
	penalty_trait = integer(penalty_trait)
	multiple_count = integer(multiple_count)
	lasts = integer(lasts)


class EquipOpposed(db.Model):

	dc = integer(dc)























class Equipment(db.Model):

	type_id = integer(type_id)
	expertise = get_name(SkillBonus, expertise)
	
	
	

class EquipEffect(db.Model):
	
	
	
	
class EquipBelt(db.Model):
	
	
	feature = get_name(Feature, feature)
	weapon = get_name(Weapon, weapon)
	equipment = get_name(Equipment, equipment)
	
	
class EquipCheck(db.Model):
	
	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

	skill_type = get_name(Skill, skill_type)
	skill = get_name(SkillBonus, skill)
	check_type = get_name(Check, check_type)
	action = get_name(Action, action)
	
	
class EquipDamage(db.Model):
	
	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

	damage = get_name(Descriptor, damage)
	skill_type = get_name(Skill, skill_type)
	skill = get_name(SkillBonus, skill)
	
	
class EquipDescriptor(db.Model):
	
	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

	descriptor = get_name(Descriptor, descriptor)


class EquipLimit(db.Model):

	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

	time_units = get_name(Unit, time_units)
	range_units = get_name(Unit, range_units)
	time_capacity_units = get_name(Unit, time_capacity_units)
	area_units = get_name(Unit, area_units)
	light = get_name(Light, light)

	
class EquipMod(db.Model):


	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

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

	
class EquipOpposed(db.Model):


	
	feature = get_name(Feature, feature)
	effect = get_name(EquipEffect, effect)

	skill_type = get_name(Skill, skill_type)
	skill = get_name(SkillBonus, skill)
	check = get_name(Check, check)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)









