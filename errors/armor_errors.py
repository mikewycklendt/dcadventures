
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from create_functions.armor_create import arm_entry_check

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def arm_save_errors(data):

	errors = {'error': False, 'error_msgs': []}
	armor_id = data['armor_id']
	description = data['description']
	type_id = data['type_id']
	cost = data['cost']
	material = data['material']
	toughness = data['toughness']
	active = data['active']
	subtle = data['subtle']
	perception = data['perception']
	impervious = data['impervious']
	defense = data['defense']
	descriptor = data['descriptor']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(ArmorType, type_id, 'Armor Type', errors)
	errors = int_check(cost, 'Cost', errors)
	errors = id_check(Material, material, 'Material', errors)
	errors = int_check(toughness, 'Toughness Bonus', errors)
	errors = int_check(active, 'Active Defense Bonus', errors)
	errors = int_check(perception, 'Perception DC', errors)

	errors = required(type_id, 'Armor Type', errors)
	errors = required(cost, 'Cost', errors)
	errors = of([toughness, active, defense], 'You must set a toughness bonus, active defense bonus or at least one defense bonus', errors)

	arm_entry_check('Armor Descriptors', ArmDescriptor, descriptor, armor_id, errors)
	arm_entry_check('Defense Bonus', ArmDefense, defense, armor_id, errors)

	return (errors)

def arm_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	armor_id = data['armor_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	descriptor = data['descriptor']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)

	return (errors)
	
def arm_defense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	armor_id = data['armor_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	defense = data['defense']
	bonus = data['bonus']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(Defense, defense, 'Defense', errors)

	errors = required(defense, 'Defense', errors)
	errors = required(bonus, 'Bonus', errors)

	return (errors)
