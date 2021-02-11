
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

	adv_type = db.Column(db.Integer, db.ForeignKey('advantage_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	expertise = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	conflict_immune = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	action1 = db.Column(db.Integer, db.ForeignKey('actions.id'))
	action2 = db.Column(db.Integer, db.ForeignKey('actions.id'))
	
	
	
class AdvAltCheck(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvCirc(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	circ_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
		
class AdvCombined(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))

	
	
class AdvCondition(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_null = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvDC(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	math_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvDegree(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvEffort(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvMinion(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	attitude_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	attitude_attitude = db.Column(db.Integer, db.ForeignKey('levels.id'))
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))
	
	
class AdvMod(db.Model):
	
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	mod_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	cover = db.Column(db.Integer, db.ForeignKey('cover.id'))
	conceal = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	maneuver = db.Column(db.Integer, db.ForeignKey('maneuvers.id'))
	weapon_melee = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon_ranged = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	creature = db.Column(db.Integer, db.ForeignKey('creature.id'))
	emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	profession = db.Column(db.Integer, db.ForeignKey('jobs.id'))
	bonus_conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	penalty_conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	
	
class AdvOpposed(db.Model):
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))


class AdvPoints(db.Model):
	advantage_id = integer(advantage_id)
	benefit = integer
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvResist(db.Model):
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvRounds(db.Model):
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	cost = db.Column(db.Integer, db.ForeignKey('actions.id'))
	check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	
		}

class AdvSkill(db.Model):
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvTime(db.Model):
	
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	
	
class AdvVariable(db.Model):
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	
	
	