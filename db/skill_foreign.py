
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


	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	type = db.Column(db.Integer, db.ForeignKey('skill_type.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	concealment = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	weapon_cat = db.Column(db.Integer, db.ForeignKey('weapon_category.id'))
	weapon_type = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))



class SkillAbility(db.Model):


	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class SkillCheck(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class SkillCirc(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class SkillDC(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))


class SkillDegree(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	circumstance = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class SkillMod(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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


class SkillOpposed(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class SkillTime(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	rank1 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	rank_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	rank2 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))






class SkillBonus(db.Model):


	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	type = db.Column(db.Integer, db.ForeignKey('skill_type.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	concealment = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	weapon_cat = db.Column(db.Integer, db.ForeignKey('weapon_category.id'))
	weapon_type = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon = db.Column(db.Integer, db.ForeignKey('weapons.id'))



class SkillAbility(db.Model):


	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class SkillCheck(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class SkillCirc(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	time_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class SkillDC(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))


class SkillDegree(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	inflict_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	damage_consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	circumstance = db.Column(db.Integer, db.ForeignKey('skill_circ.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	unit_type = db.Column(db.Integer, db.ForeignKey('measurement_type.id'))
	unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	measure_trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_math_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class SkillMod(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
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


class SkillOpposed(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recurring_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class SkillTime(db.Model):

	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	rank1 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	rank_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	rank2 = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))

