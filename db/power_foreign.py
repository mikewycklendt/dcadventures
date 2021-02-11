
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

	power_type = db.Column(db.Integer, db.ForeignKey('power_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	power_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
	
class Extra(db.Model):
	
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	inherit = db.Column(db.Integer, db.ForeignKey('powers.id'))


class PowerAltCheck(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerAction(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))


class PowerChar(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))


class PowerCirc(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	circ_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class PowerCreate(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))
	move_opponent_ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class PowerDamage(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	damage_type = db.Column(db.Integer, db.ForeignKey('descriptors.id'))


class PowerDC(db.Model):
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))


class PowerDefense(db.Model):
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
	reflect_action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	immunity_damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))


class PowerDegMod(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))


class PowerDegree(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))


class PowerEnv(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	immunity_environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	move_nature = db.Column(db.Integer, db.ForeignKey('nature.id'))


class PowerMinion(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	attitude_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	attitude_attitude = db.Column(db.Integer, db.ForeignKey('levels.id'))
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))


class PowerMod(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	objects_alone = db.Column(db.Integer, db.ForeignKey('defense.id'))
	objects_character = db.Column(db.Integer, db.ForeignKey('defense.id'))
	limited_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	limited_extra = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	limited_range = db.Column(db.Integer, db.ForeignKey('range.id'))
	side_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerMove(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	distance_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	concealment_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	ground_type = db.Column(db.Integer, db.ForeignKey('ground.id'))
	ground_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	objects_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	objects_attack = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	damage_type = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class PowerOpposed(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerRanged(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	flat_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	units_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	effect_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))


class PowerResist(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerResistBy(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	nullify_alternate = db.Column(db.Integer, db.ForeignKey('defense.id'))


class PowerSenseEffect(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))
	lighting = db.Column(db.Integer, db.ForeignKey('light.id'))
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	time_bonus = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	distance_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class PowerReverse(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))



class PowerTime(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))









class Power(db.Model):

	power_type = db.Column(db.Integer, db.ForeignKey('power_type.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	power_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
	
class Extra(db.Model):
	
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	inherit = db.Column(db.Integer, db.ForeignKey('powers.id'))


class PowerAltCheck(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerAction(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	action = db.Column(db.Integer, db.ForeignKey('actions.id'))


class PowerChar(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))


class PowerCirc(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	circ_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class PowerCreate(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	complexity = db.Column(db.Integer, db.ForeignKey('complexity.id'))
	move_opponent_ability = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class PowerDamage(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	damage_type = db.Column(db.Integer, db.ForeignKey('descriptors.id'))


class PowerDC(db.Model):
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))


class PowerDefense(db.Model):
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	defense = db.Column(db.Integer, db.ForeignKey('defense.id'))
	reflect_action = db.Column(db.Integer, db.ForeignKey('actions.id'))
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	immunity_damage = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))


class PowerDegMod(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))


class PowerDegree(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))


class PowerEnv(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	immunity_environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	move_nature = db.Column(db.Integer, db.ForeignKey('nature.id'))


class PowerMinion(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	attitude_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	attitude_attitude = db.Column(db.Integer, db.ForeignKey('levels.id'))
	resitable_check = db.Column(db.Integer, db.ForeignKey('defense.id'))


class PowerMod(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	objects_alone = db.Column(db.Integer, db.ForeignKey('defense.id'))
	objects_character = db.Column(db.Integer, db.ForeignKey('defense.id'))
	limited_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	limited_extra = db.Column(db.Integer, db.ForeignKey('extras.id'))
	limited_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	limited_range = db.Column(db.Integer, db.ForeignKey('range.id'))
	side_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	reflect_check = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerMove(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	distance_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	concealment_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	ground_type = db.Column(db.Integer, db.ForeignKey('ground.id'))
	ground_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	objects_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	objects_attack = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	damage_type = db.Column(db.Integer, db.ForeignKey('abilities.id'))


class PowerOpposed(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerRanged(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	flat_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	flat_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	units_rank_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	effect_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_mod_math = db.Column(db.Integer, db.ForeignKey('math.id'))


class PowerResist(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))


class PowerResistBy(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	nullify_alternate = db.Column(db.Integer, db.ForeignKey('defense.id'))


class PowerSenseEffect(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))
	lighting = db.Column(db.Integer, db.ForeignKey('light.id'))
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	time_bonus = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))
	distance_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))


class PowerReverse(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))



class PowerTime(db.Model):

	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))


