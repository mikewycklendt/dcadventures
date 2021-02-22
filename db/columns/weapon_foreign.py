
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




class Weapon(db.Model):

	cat_id = db_integer(WeaponCat, cat_id)
	type_id = db_integer(WeaponType, type_id)
	material = db_integer(Material, material)
	length_units = db_integer(Unit, length_units)
	resistance = db_integer(Defense, resistance)
	power = db_integer(Power, power)
	advantage = db_integer(Advantage, advantage)
	conceal = db_integer(Conceal, conceal)
	sense = db_integer(Sense, sense)


class WeapDescriptor(db.Model):

	weapon_id = integer(weapon_id)
	descriptor = db_integer(Descriptor, descriptor)


class WeapBenefit(db.Model):

	weapon_id = integer(weapon_id)
	benefit = db_integer(Benefit, benefit)



class WeapCondition(db.Model):

	weapon_id = integer(weapon_id)
	condition = db_integer(Condition, condition)
	condition_null = db_integer(Condition, condition_null)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)


































class Weapon(db.Model):

	cost = integer(cost)
	critical = integer(critical)
	damage = integer(damage)
	toughness = integer(toughness)
	length = integer(length)
	resist_dc = integer(resist_dc)
	power_rank = integer(power_rank)
	hands = integer(hands)
	reach = integer(reach)
	ranged_attack_bonus = integer(ranged_attack_bonus)
	protect = integer(protect)
	ranged_burst = integer(ranged_burst)
	ranged_area_damage = integer(ranged_area_damage)
	attack_bonus = integer(attack_bonus)
	perception_dc = integer(perception_dc)
	grenade_burst = integer(grenade_burst)
	grenade_area_damage = integer(grenade_area_damage)
	double_mod = integer(double_mod)


class WeapDescriptor(db.Model):


class WeapBenefit(db.Model):



class WeapCondition(db.Model):

	damage_value = integer(damage_value)
	damage = integer(damage)















class WeapDescriptor(db.Model):

	weapon_id = integer(weapon_id)
	descriptor = get_name(Descriptor, descriptor)


class WeapBenefit(db.Model):

	weapon_id = integer(weapon_id)
	benefit = get_name(Benefit, benefit)



class WeapCondition(db.Model):

	weapon_id = integer(weapon_id)
	condition = get_name(Condition, condition)
	condition_null = get_name(Condition, condition_null)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

