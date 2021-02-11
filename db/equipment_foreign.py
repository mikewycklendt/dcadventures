
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

	type_id = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	expertise = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	
	
class Feature(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipFeature(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	
	

class EquipEffect(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipBelt(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipCheck(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	
	
class EquipDamage(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	
	
class EquipDescriptor(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	descriptor = db.Column(db.Integer, db.ForeignKey('descriptors.id'))


class EquipLimit(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	range_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_capacity_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	area_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	light = db.Column(db.Integer, db.ForeignKey('light.id'))

	
class EquipMod(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
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
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	light = db.Column(db.Integer, db.ForeignKey('light.id'))

	
class EquipOpposed(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))





















class Equipment(db.Model):

	type_id = db.Column(db.Integer, db.ForeignKey('equipment_type.id'))
	expertise = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	
	
class Feature(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipFeature(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	
	

class EquipEffect(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipBelt(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))
	equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	
	
class EquipCheck(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	
	
class EquipDamage(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	
	
class EquipDescriptor(db.Model):
	
	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	descriptor = db.Column(db.Integer, db.ForeignKey('descriptors.id'))


class EquipLimit(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	range_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_capacity_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	area_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	light = db.Column(db.Integer, db.ForeignKey('light.id'))

	
class EquipMod(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
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
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	light = db.Column(db.Integer, db.ForeignKey('light.id'))

	
class EquipOpposed(db.Model):

	equip_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
	effect = db.Column(db.Integer, db.ForeignKey('equipment_effect.id'))
	feature = db.Column(db.Integer, db.ForeignKey('features.id'))
	skill_type = db.Column(db.Integer, db.ForeignKey('skills.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))

