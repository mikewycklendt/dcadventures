
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
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillMove, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 
from db.linked_models import SkillCircType, SkillDCType, SkillDegreeType, SkillMoveType, SkillTimeType

from functions.converts import integer, integer_convert, int_check, name, get_name, get_id, get_circ, get_keyword, get_description, action_convert, math_convert, extra_name, db_integer, id_check, trait_select, db_check, selects
from functions.create import name_exist, db_insert, capitalize
from functions.linked import linked_options, level_reference, linked_move, linked_time, level_bonus_circ, level_bonus_dc, level_bonus_degree, level_power_circ, level_power_dc, level_power_degree, level_adv_circ, level_adv_dc, level_adv_degree, required_link
from functions.user_functions import user_item

from functions.create_errors import required, required_keyword, required_if_any, no_zero, required_multiple, variable, select, variable_fields, if_fields, if_field, if_or, seperate, variable_field, variable_field_linked, select_variable, together, dependent, valid_time_type, invalid_time, check_together_var, together_names, check_fields, check_field, multiple, check_of_multiple, of_multiple, check_of, of, either, select_of, create_check, required_entry_multiple, required_variable, value_limit, select_check, check_of, multiple_effect_check, multiple_link_check, required_setting, linked_group_check, required_link_field, linked_field, required_rule
from functions.create_posts import one, field, int_word, select_multiple, string, string_value, string_value_else, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, one_of, check_cell, if_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, int_word, check_string

from create_functions.skill_create import skill_entry_check, skill_required_entry, skill_required_entry_multiple

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def skill_save_errors(data):

	errors = {'error': False, 'error_msgs': []}


	skill_id = data['skill_id']
	description = data['description']
	ability = data['ability']
	skill = data['skill']
	check_type = data['check_type']
	action = data['action']
	type = data['type']
	dc_type = data['dc_type']
	dc_value = data['dc_value']
	dc_mod = data['dc_mod']
	target = data['target']
	targets = data['targets']
	speed_type = data['speed_type']
	speed_turns = data['speed_turns']
	speed_direction = data['speed_direction']
	speed_mod = data['speed_mod']
	speed_value = data['speed_value']
	condition = data['condition']
	advantage = data['advantage']
	concealment_type = data['concealment_type']
	concealment = data['concealment']
	for_weapon = data['for_weapon']
	weapon_cat = data['weapon_cat']
	weapon_type = data['weapon_type']
	weapon = data['weapon']
	untrained = data['untrained']
	tools = data['tools']
	required_tools = data['required_tools']
	subskill = data['subskill']
	check_dc = data['check_dc']
	secret = data['secret']
	secret_frequency = data['secret_frequency']
	ability_check = data['ability_check']
	check_check = data['check_check']
	circumstance = data['circumstance']
	dc = data['dc']
	degree = data['degree']
	levels = data['levels']
	modifiers = data['modifiers']
	move = data['move']
	opposed = data['opposed']
	time = data['time']
	opposed_multiple = data['opposed_multiple']
	modifiers_multiple = data['modifiers_multiple']
	modifiers_multiple_count = data['modifiers_multiple_count']
	time_multiple = data['time_multiple']
	opposed_attached = data['opposed_attached']
	partner = data['partner']
	partner_type = data['partner_type']
	partner_trait_type = data['partner_trait_type']
	partner_trait = data['partner_trait']
	partner_tools = data['partner_tools']
	partner_materials = data['partner_materials']
	partner_equip_type = data['partner_equip_type']
	partner_equip = data['partner_equip']
	partner_feature = data['partner_feature']
	opponent_turn = data['opponent_turn']
	opponent_turn_check = data['opponent_turn_check']
	opponent_turn_when = data['opponent_turn_when']
	secret_trait_type = data['secret_trait_type']
	secret_trait = data['secret_trait']



	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = required(description, 'Description', errors)
	errors = required(ability, 'Parent Ability', errors)
	errors = required(skill, 'Parent Skill', errors)
	errors = required(check_type, 'Check Type', errors)
	errors = required(action, 'Action Type', errors)
	
	errors = variable_fields('value', 'Speed Value', speed_type, [speed_value, speed_turns, speed_direction], errors)
	errors = variable_field('value', speed_type, 'Movement Speed', speed_value, errors)
	errors = variable_field('value', speed_type, 'Speed Turns', speed_turns, errors)
	errors = variable_field('value', speed_type, 'Speed Direction', speed_direction, errors)

	errors = variable_fields('mod', 'Speed Modifier', speed_type, [speed_mod, speed_turns, speed_direction], errors)
	errors = variable_fields('mod', speed_type, 'Speed Modifier', speed_mod, errors)
	errors = variable_fields('mod', speed_type, 'Speed Turns', speed_turns, errors)
	errors = variable_fields('mod', speed_type, 'Speed Direction', speed_direction, errors)

	errors = check_fields(secret, 'GM Secret Check', [secret_frequency, secret_trait_type, secret_trait], errors)
	errors = check_field(secret, 'GM Secret Check', 'Secret Check Frequency', secret_frequency, errors)
	errors = check_field(secret, 'GM Secret Check', 'Secret Trait Type', secret_trait_type, errors)
	errors = check_field(secret, 'GM Secret Check', 'Secret Trait', secret_trait, errors)

	errors = check_fields(tools, 'Tools', [required_tools], errors)
	errors = check_field(tools, 'Tools', 'Tool Type', required_tools, errors)

	errors = check_fields(opponent_turn, 'Opponent Turn', [opponent_turn_check, opponent_turn_when], errors)
	errors = check_field(opponent_turn, 'Opponent Turn', 'When during opponents turn', opponent_turn_when, errors)
	errors = check_field(opponent_turn, 'Opponent Turn', 'Opponent Check', opponent_turn_check, errors)

	errors = together_names('Concealment', ['Concealment Type', 'Concealment'], [concealment_type, concealment], errors)
	
	errors = skill_required_entry('table', dc_type, 'Check Table', 'Check Table', SkillDC, skill_id, errors)
	errors = skill_required_entry('2', check_type, 'Opposed Check', 'Opponent Check', SkillOpposed, skill_id, errors)
	errors = required_entry_multiple('x', ability, 'skill', 'Variable Ability', 'Variable Ability', SkillAbility, 'skill_id', skill_id, errors)
	errors = required_entry_multiple('x', action, 'skill', 'Variable Action', 'Variable Check', SkillCheck, 'skill_id', skill_id, errors)
	errors = required_entry_multiple('x', check_type, 'skill', 'Variable Check', 'Variable Check', SkillCheck, 'skill_id', skill_id, errors)
	errors = required_variable('x', SkillAbility, ability, 'Ability', 'Variable Ability', 'skill', 'Variable', 'skill_id', skill_id, errors)
	errors = required_variable('table', SkillDC, dc_type, 'Difficulty Class', 'Check Table', 'skill', 'Table', 'skill_id', skill_id, errors)

	errors = skill_entry_check('Bonus/Penalty Modifier', SkillMod, modifiers, skill_id, errors)
	errors = skill_entry_check('Check Table', SkillDC, dc, skill_id, errors)
	errors = skill_entry_check('Degree of Success/Failure Modifier Table', SkillDegree, degree, skill_id, errors)
	errors = skill_entry_check('Circumstance Modifier', SkillCirc, circumstance, skill_id, errors)
	errors = skill_entry_check('Opponent Check',SkillOpposed, opposed, skill_id, errors)
	errors = skill_entry_check('Time Effect', SkillTime, time, skill_id, errors)
	errors = skill_entry_check('Variable Check', SkillCheck, check_check, skill_id, errors)
	errors = skill_entry_check('Variable Ability', SkillAbility, ability_check, skill_id, errors)
	errors = skill_entry_check('Movement', SkillMove, move, skill_id, errors)

	errors = required_rule('1', check_type, False, skill_id, 'skill_id', dc_type, 'skill', 'Skill Check', 'DC', 'Difficulty Class Field or Check Table form', errors)
	errors = required_rule('6', check_type, False, skill_id, 'skill_id', dc_type, 'skill', 'Resistence Check', 'DC', 'Difficulty Class Field or Check Table form', errors)
	
	time_effect_select = [{'type': 'prepare', 'name': 'Time to Prepare'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time Limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}, {'type': 'recover', 'name': 'Recovery Time'}]

	errors = multiple_link_check(SkillCirc, skill_id, 'skill_id', 'skill', 'circ', 'Circumstance', 'Time Effect', time_multiple, 'if multiple', errors)
	errors = multiple_link_check(SkillCirc, skill_id, 'skill_id', 'skill', 'degree', 'Degree', 'Time Effect', time_multiple, 'if multiple', errors)
	errors = multiple_link_check(SkillCirc, skill_id, 'skill_id', 'skill', 'dc', 'DC', 'Time Effect', time_multiple, 'if multiple', errors)

	attached_select = [{'type': 'before', 'name': 'Before Skill Check'}, {'type': 'after', 'name': 'After Skill Check'}]

	errors = required_setting('before', opposed_attached, [dc_type], attached_select, 'skill', skill_id, False, 'skill_id', 'Opponent Check Attached', 'DC for the skill check', 'DC field in the skill settings or the DC Table', errors)
	errors = required_setting('after', opposed_attached, [dc_type], attached_select, 'skill', skill_id, False, 'skill_id', 'Opponent Check Attached', 'DC for the skill check', 'DC field in the skill settings or the DC Table', errors)
	
	errors = required_link_field(SkillDC, 'skill_id', skill_id, partner_trait, 'DC for another character', 'skill', 'partner check trait', errors, 'target', 'other')

	return (errors)

def skill_ability_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	ability = data['ability']
	circumstance = data['circumstance']
	variable = data['variable']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = id_check(Ability, ability, 'Ability', errors)
	errors = id_check(SkillCheck, variable, 'Variable Check', variable)

	errors = required(ability, 'Ability', errors)
	errors = required(circumstance, 'Circumstance', errors)

	return (errors)

def skill_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	check_type = data['check_type']
	circumstance = data['circumstance']
	trigger = data['trigger']
	when = data['when']
	trait_type = data['trait_type']
	trait = data['trait']
	conflict = data['conflict']
	conflict_range = data['conflict_range']
	conflict_weapon = data['conflict_weapon']
	condition1 = data['condition1']
	condition2 = data['condition2']
	action_type = data['action_type']
	action = data['action']
	free = data['free']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	dc_value = data['dc_value']
	time = data['time']
	move = data['move']
	keyword = data['keyword']
	attack = data['attack']
	opposed = data ['opposed']
	condition = data ['condition']
	condition_target = data ['condition_target']
	conditions_target = data ['conditions_target']


	
	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)	
	errors = id_check(Check, check_type, 'Check', errors)
	errors = id_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = id_check(Ranged, conflict_range, 'Conflict Range', errors)
	errors = int_check(action, 'Action', errors)
	errors = id_check(Condition, condition1, 'Start Condition', errors)
	errors = id_check(Condition, condition2, 'End Condition', errors)
	errors = id_check(Condition, condition, 'Condition', errors)


	errors = id_check(SkillDegreeType, degree, 'Degree', errors)
	errors = id_check(SkillCircType, circ, 'Circumstance', errors)
	errors = id_check(SkillDCType, dc, 'DC', errors)
	errors = id_check(SkillTimeType, time, 'Time Effect', errors)
	errors = id_check(SkillMoveType, move, 'Movement Effect', errors)
	errors = id_check(SkillOpposed, opposed, 'Opponent Check', errors)

	errors = int_check(attack, 'Attack Check Modifier', errors)

	errors = required(check_type, 'Check Type', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(when, 'When', errors)
	errors = required(action_type, 'Action Type', errors)
	errors = required(action, 'Action', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(trait_type, 'Rank', errors)
	errors = required(trait, 'Trait', errors)	

	errors = variable_fields('change', 'Trigger', trigger, [condition1, condition2, conditions_target], errors)
	errors = variable_field('change', trigger, 'Starting Condition', condition1, errors)
	errors = variable_field('change', trigger, 'Ending Condition', condition2, errors)
	errors = variable_field('change', trigger, 'Condition Target', conditions_target, errors)
	errors = variable_fields('condition', 'Trigger', trigger, [condition, condition_target], errors)
	errors = variable_field('condition', trigger, 'Condition', condition, errors)
	errors = variable_field('condition', trigger, 'Condition Target', condition_target, errors)
	errors = variable_fields('conflict', 'Trigger', trigger, [conflict], errors)
	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)

	errors = variable_field_linked('2', check_type, opposed, 'Opposed Check', 'Opponent Check', errors)
	errors = variable_field_linked('7', check_type, opposed, 'Comparison Check', 'Opponent Check', errors)

	errors = select_of('1', 'uses a skill check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = select_of('6', 'uses a resistance check', 'Check Type', check_type, [dc, dc_value], ['DC', 'DC by group'], errors)
	errors = seperate([dc, dc_value], 'DC or DC by Group', errors)

	return (errors)

def skill_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	circ_target = data['circ_target']
	mod = data['mod']
	effect = data['effect']
	speed = data['speed']
	target = data['target']
	level_type = data['level_type']
	level = data['level']
	condition_type = data['condition_type']
	condition1 = data['condition1']
	condition2 = data['condition2']
	conditions = data['conditions']
	conditions_effect = data['conditions_effect']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	keyword = data['keyword']
	cumulative = data['cumulative']
	optional = data['optional']
	circumstance = data['circumstance']
	lasts = data['lasts']
	title = data['title']
	tools = data['tools']
	materials = data['materials']
	trait_type = data['trait_type']
	trait = data['trait']
	trait_target = data['trait_target']
	environment = data['environment']
	nature = data['nature']
	check_type = data['check_type']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(speed, 'Speed', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(conditions, 'Condition Degree', errors)
	errors = int_check(conditions_effect, 'Condition Effect', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Unit', errors)
	errors = id_check(Math, measure_trait_math, 'Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(trait, 'Trait', errors)
	errors = id_check(Check, check_type, 'Check Type', errors)

	errors = id_check(Environment, environment, 'Environment', errors)
	errors = id_check(Nature, nature, 'Nature', errors)

	errors = id_check(SkillTime, lasts, 'Circumsrance Duration', errors)
	
	errors = required(mod, 'Circumstance Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = required(circ_target, 'Target', errors)

	errors = variable_fields('condition', 'Circumstance Effect', effect, [condition_type], errors)
	errors = variable_field('condition', effect, 'Condition Type', condition_type, errors)
	errors = variable_fields('condition', 'Condition Type', condition_type, [], errors)

	errors = variable_fields('damage', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('damage', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('damage', condition_type, 'Ending Condition', condition2, errors)

	errors = variable_fields('damage', 'Condition Damage', condition_type, [conditions, conditions_effect], errors)
	errors = variable_field('damage', condition_type, 'Conditions', conditions, errors)
	errors = variable_field('damage', condition_type, 'Condition Effect', conditions_effect, errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors)

	errors = variable_fields('rank', 'Measurement Rank', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Measurement Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Units', unit, errors)

	errors = variable_fields('skill', 'Measurement Skill Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill', measure_effect, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('skill', measure_effect, 'Measurement Trait', measure_trait, errors)
	errors = variable_field('skill', measure_effect, 'Math', measure_trait_math, errors)
	errors = variable_field('skill', measure_effect, 'Measuremet Modifier', measure_mod, errors)
	errors = variable_field('skill', measure_effect, 'Rank', measure_math_rank, errors)
	
	errors = variable_fields('level', 'Circumstance Effect', effect, [level_type, level], errors)
	errors = variable_field('level', effect, 'Level Type', level_type, errors)
	errors = variable_field('level', effect, 'Level', level, errors)
	
	errors = variable_fields('speed', 'Circumstance Effect', effect, [speed], errors)
	errors = variable_field('speed', effect, 'Speed Rank', speed, errors)
	
	errors = variable_fields('target', 'Circumstance Effect', effect, [target], errors)
	errors = variable_field('target', effect, 'If Target', target, errors)
	
	errors = variable_fields('tools', 'Circumstance Effect', effect, [tools], errors)
	errors = variable_field('tools', effect, 'Tool Type', tools, errors)
	
	errors = select_of('trait', 'affects another check', 'circumstance effect', effect, [trait, check_type], ['Trait', 'Check Type'], errors)
	errors = variable_field('trait', effect, 'Check Target', trait_target, errors)

	errors = variable_fields('env', 'Environment', effect, [environment], errors)

	errors = variable_fields('nature', 'Nature', effect, [nature], errors)

	errors = variable_fields('materials', 'Circumstance Effect', effect, [materials], errors)
	errors = variable_field('materials', effect, 'Material Type', materials, errors)


	return (errors)

def skill_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	target = data['target']
	dc = data['dc']
	description = data['description']
	value = data['value']
	mod = data['mod']
	math_value = data['math_value']
	math = data['math']
	math_trait_type = data['math_trait_type']
	math_trait = data['math_trait']
	condition = data['condition']
	levels = data['levels']
	damage = data['damage']
	cover = data['cover']
	complex = data['complex']
	measure = data['measure']
	conceal = data['conceal']
	damage_type = data['damage_type']
	inflict_type = data['inflict_type']
	inflict_flat = data['inflict_flat']
	inflict_trait_type= data['inflict_trait_type']
	inflict_trait = data['inflict_trait']
	inflict_math = data['inflict_math']
	inflict_mod = data['inflict_mod']
	inflict_bonus = data['inflict_bonus']
	damage_mod = data['damage_mod']
	damage_consequence = data['damage_consequence']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	measure_trait_type_unit = data['measure_trait_type_unit']
	measure_trait_unit = data['measure_trait_unit']
	measure_trait_math_unit = data['measure_trait_math_unit']
	measure_mod_unit = data['measure_mod_unit']
	measure_math_unit = data['measure_math_unit']
	level_type = data['level_type']
	level = data['level']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	keyword = data['keyword']
	complexity = data['complexity']
	tools_check = data['tools_check']
	cover_effect = data['cover_effect']
	cover_type = data['cover_type']
	conceal_effect = data['conceal_effect']
	conceal_type = data['conceal_type']
	tools = data['tools']
	variable_check = data['variable_check']
	variable = data['variable']
	time = data['time']
	title = data['title']
	equipment_use = data['equipment_use']
	equipment_type = data['equipment_type']
	equipment = data['equipment']
	equip = data['equip']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(value, 'DC', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(math_value, 'Math Value', errors)
	errors = id_check(Math, math, 'Math', errors)
	errors = int_check(inflict_flat, 'Infllict Damage Value', errors)
	errors = id_check(Math, inflict_math, 'Math', errors)
	errors = int_check(inflict_mod, 'Inflict Damage Modifier', errors)
	errors = int_check(inflict_bonus, 'Inflict Damage Bonus', errors)
	errors = int_check(damage_mod, 'Damage Modifier', errors)
	errors = id_check(Consequence, damage_consequence, 'Consequence Damage Modifier', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Vslue', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Unit Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Unit', errors)
	errors = id_check(Math, measure_trait_math, 'MeaSurement Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = id_check(Rank, measure_math_rank, 'Measurement Rank', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = id_check(Complex, complexity, 'Complexity', errors)
	errors = id_check(EquipType, equipment_type, 'Equipment Type', errors)
	errors = id_check(Equipment, equipment, 'Equipment', errors)

	errors = id_check(Cover, cover_type, 'Cover', errors)
	errors = id_check(Conceal, conceal_type, 'Concealment', errors)
	
	errors = id_check(SkillCheck, variable, 'Variable Check', errors)
	errors = id_check(SkillTime, time, 'Duration of Effect', errors)

	errors = required(target, 'Target', errors)
	errors = required(dc, 'DC Type', errors)
	errors = required(description, 'Description', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('value', 'DC Value', dc, [value], errors) 
	errors = variable_field('value', dc, 'DC', value, errors) 

	errors = variable_fields('math', 'DC Math', dc, [math_value, math, math_trait_type, math_trait], errors)
	errors = variable_field('math', dc, 'DC Math Value', math_value, errors)
	errors = variable_field('math', dc, 'DC Math', math, errors)
	errors = variable_field('math', dc, 'DC Math Trait Type', math_trait_type, errors)
	errors = variable_field('math', dc, 'DC Math Trait', math_trait, errors)
	
	errors = variable_fields('mod', 'DC Modifier', dc, [mod], errors)
	errors = variable_field('mod', dc, 'Modifier', mod, errors)

	errors = check_fields(condition, 'Condition', [condition1, condition2], errors)
	errors = check_field(condition, 'Condition', 'Starting Condition', condition1, errors)
	errors = check_field(condition, 'Condition', 'Ending Condtion', condition2, errors)
	
	errors = check_fields(levels, 'Levels', [level_type, level], errors)
	errors = check_field(levels, 'Levels', ':evel Type', level_type, errors)
	errors = check_field(levels, 'Levels', 'Level', level, errors)

	errors = check_fields(damage, 'Damage', [damage_type], errors)
	errors = check_field(damage, 'Damage', 'Damage Type', damage_type, errors)

	errors = variable_fields('inflict', 'Inflict Damage', damage_type, [inflict_type], errors)
	errors = variable_field('inflict', damage_type, 'Inflict Damage Type', inflict_type, errors)

	errors = variable_fields('flat', 'Flat Damage Value', inflict_type, [inflict_flat], errors)
	errors = variable_field('flat', inflict_type, 'Damage', inflict_flat, errors)

	errors = variable_fields('bonus', 'Flat Damage Bonus', inflict_type, [inflict_bonus], errors)
	errors = variable_fields('bonus', inflict_type, 'Bonus', inflict_bonus, errors)
	
	errors = variable_fields('math', 'Math Damage', inflict_type, [inflict_trait_type, inflict_trait, inflict_math, inflict_mod], errors)
	errors = variable_field('math', inflict_type, 'Math Damage Trait Type', inflict_trait_type, errors)
	errors = variable_field('math', inflict_type, 'Math Damage Trait', inflict_trait, errors)
	errors = variable_field('math', inflict_type, 'Math', inflict_math, errors)
	errors = variable_field('math', inflict_type, 'Math Damage Modifier', inflict_mod, errors)

	errors = variable_fields('reduce', 'Reduce Damage', damage_type, [damage_mod], errors)
	errors = variable_field('reduce', damage_type, 'Damage Modifier', damage_mod, errors)
	
	errors = check_fields(complex, 'Complexity', [complexity], errors)
	errors = check_field(complex, 'Complexity', 'Complexity', complexity, errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors)

	errors = variable_fields('rank', 'Measurement Rank Value', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Rank Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Measurement Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit Value', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Measurement Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Measurement UnitS', unit, errors)

	errors = variable_fields('skill_rank', 'Measurement Skill Rank Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Trait', measure_trait, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Skill Modifier Math', measure_trait_math, errors)
	errors = variable_field('skill_rank', measure_effect, 'Skill Modifier', measure_mod, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Rank', measure_math_rank, errors)
	
	errors = variable_fields('skill_unit', 'Measurement Skill Unit Modifier', measure_effect, [measure_trait_type_unit, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait Type', measure_trait_type_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait', measure_trait_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Math', measure_trait_math_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Skill Modifier', measure_mod_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Measurement Rank', measure_math_unit, errors)

	errors = check_fields(conceal, 'Concealment', [conceal_effect, conceal_type], errors)
	errors = check_field(conceal, 'Concealment', 'Concealment Type', conceal_type, errors)
	errors = check_field(conceal, 'Concealment', 'Concealment Effect', conceal_effect, errors)
	
	errors = check_fields(cover, 'Cover', [cover_effect, cover_type], errors)
	errors = check_field(cover, 'Cover', 'Cover Type', cover_type, errors)
	errors = check_field(cover, 'Cover', 'Cover Effect', cover_effect, errors)

	errors = check_fields(equip, 'Equipment', [equipment_use, equipment_type, equipment], errors)
	errors = check_field(equip, 'Equipment', 'Equipment Use Type', equipment_use, errors)
	errors = check_field(equip, 'Equipment', 'Equipment Type', equipment_type, errors)
	errors = check_field(equip, 'Equipment', 'Equipment', equipment, errors)

	errors = check_fields(variable_check, 'Variable Check', [variable], errors)

	return (errors)

def skill_degree_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	target = data['target']
	value = data['value']
	type = data['type']
	action = data['action']
	time = data['time']
	recovery = data['recovery']
	damage_type = data['damage_type']
	object = data['object']
	object_effect = data['object_effect']
	inflict_type = data['inflict_type']
	inflict_flat = data['inflict_flat']
	inflict_trait_type = data['inflict_trait_type']
	inflict_trait = data['inflict_trait']
	inflict_math = data['inflict_math']
	inflict_mod = data['inflict_mod']
	inflict_bonus = data['inflict_bonus']
	damage_mod = data['damage_mod']
	damage_consequence = data['damage_consequence']
	consequence_action_type = data['consequence_action_type']
	consequence_action = data['consequence_action']
	consequence_trait_type = data['consequence_trait_type']
	consequence_trait = data['consequence_trait']
	consequence = data['consequence']
	knowledge = data['knowledge']
	knowledge_count = data['knowledge_count']
	knowledge_specificity = data['knowledge_specificity']
	level_type = data['level_type']
	level = data['level']
	level_direction = data['level_direction']
	level_time = data['level_time']
	circumstance = data['circumstance']
	circ_target = data['circ_target']
	measure_effect = data['measure_effect']
	measure_type = data['measure_type']
	measure_rank_value = data['measure_rank_value']
	measure_rank = data['measure_rank']
	unit_value = data['unit_value']
	unit_type = data['unit_type']
	unit = data['unit']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_trait_math = data['measure_trait_math']
	measure_mod = data['measure_mod']
	measure_math_rank = data['measure_math_rank']
	measure_trait_type_unit = data['measure_trait_type_unit']
	measure_trait_unit = data['measure_trait_unit']
	measure_trait_math_unit = data['measure_trait_math_unit']
	measure_mod_unit = data['measure_mod_unit']
	measure_math_unit = data['measure_math_unit']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	condition_turns = data['condition_turns']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']
	check_type = data['check_type']
	opposed = data['opposed']
	variable = data['variable']
	resist_dc = data['resist_dc']
	resist_trait_type = data['resist_trait_type']
	resist_trait = data['resist_trait']
	skill_dc = data['skill_dc']
	skill_trait_type = data['skill_trait_type']
	skill_trait = data['skill_trait']
	routine_trait_type = data['routine_trait_type']
	routine_trait = data['routine_trait']
	routine_mod = data['routine_mod']
	attack = data['attack']
	attack_turns = data['attack_turns']
	compare = data['compare']
	duration = data['duration']
	title = data['title']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)
	errors = int_check(value, 'Degree Value', errors)
	errors = id_check(Action, action, 'Action', errors)
	errors = int_check(time, 'Time Value', errors)
	errors = int_check(object, 'Object Damage', errors)
	errors = int_check(inflict_flat, 'Inflict Damage Value', errors)
	errors = id_check(Math, inflict_math, 'Inflict Damage Math', errors)
	errors = int_check(inflict_mod, 'Inflict Damage Modifier', errors)
	errors = int_check(inflict_bonus, 'Inflict Damage Bonus', errors)
	errors = int_check(damage_mod, 'Damage Modifier', errors)
	errors = id_check(Consequence, damage_consequence, 'Consequence', errors)
	errors = int_check(consequence_action, 'Consequence Action', errors)
	errors = id_check(Consequence, consequence, 'Consequence', errors)
	errors = int_check(knowledge_count, 'Knowledge Count', errors)
	errors = id_check(LevelType, level_type, 'Level Type', errors)
	errors = id_check(Levels, level, 'Level', errors)
	errors = int_check(level_direction, 'Level Change', errors)
	errors = id_check(SkillCirc, circumstance, 'Circumstance Modifier Keyword', errors)
	errors = int_check(measure_rank_value, 'Measurement Rank Value', errors)
	errors = id_check(Rank, measure_rank, 'Measurement Rank', errors)
	errors = int_check(unit_value, 'Unit Value', errors)
	errors = id_check(MeasureType, unit_type, 'Unit Type', errors)
	errors = id_check(Unit, unit, 'Units', errors)
	errors = id_check(Math, measure_trait_math, 'Measurement Math', errors)
	errors = int_check(measure_mod, 'Measurement Modifier', errors)
	errors = int_check(condition_damage_value, 'Condition Degrees', errors)
	errors = int_check(condition_damage, 'Condition Damage', errors)
	errors = int_check(nullify, 'Nullify DC', errors)

	errors = id_check(Check, check_type, 'Check Tyoe', errors)
	errors = id_check(SkillOpposed, opposed, 'Opposed Check', errors)
	errors = id_check(SkillDC, resist_dc, 'Resistance Check DC', errors)
	errors = id_check(SkillDC, skill_dc, 'Skilll Check DC', errors)
	errors = id_check(SkillOpposed, compare, 'Comparison Check', errors)
	errors = id_check(SkillCheck, variable, 'Variable Check', errors)
	errors = id_check(SkillTime, level_time, 'Level Duration', errors)
	errors = id_check(SkillTime, attack_turns, 'Attack Bonus Duration', errors)
	errors = id_check(SkillTime, condition_turns, 'Condition Duration', errors)
	errors = id_check(SkillDegree, linked, 'Linked Degree', errors)

	errors = int_check(resist_trait, 'Resistance Trait', errors)
	errors = int_check(skill_trait, 'Skill Check Trait', errors)
	errors = int_check(routine_trait, 'Routine Check Trait', errors)
	errors = int_check(routine_mod, 'Routine Check Modifier', errors)
	errors = int_check(attack, 'Attack Check Modifier', errors)
	
	errors = required(target, 'Target', errors)
	errors = required(value, 'Degree', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('measure', 'Measurement Effect', type, [measure_effect, measure_type], errors)
	errors = variable_field('measure', type, 'Measurement Effect', measure_effect, errors)
	errors = variable_field('measure', type, 'Measurement Type', measure_type, errors) 

	errors = variable_fields('rank', 'Measurement Rank Value', measure_effect, [measure_rank_value, measure_rank], errors)
	errors = variable_field('rank', measure_effect, 'Value', measure_rank_value, errors)
	errors = variable_field('rank', measure_effect, 'Rank', measure_rank, errors)

	errors = variable_fields('unit', 'Measurement Unit Value', measure_effect, [unit_value, unit_type, unit], errors)
	errors = variable_field('unit', measure_effect, 'Value', unit_value, errors)
	errors = variable_field('unit', measure_effect, 'Unit Type', unit_type, errors)
	errors = variable_field('unit', measure_effect, 'Units', unit, errors)

	errors = variable_fields('skill_rank', 'Measurement Skill Rank Modifier', measure_effect, [measure_trait_type, measure_trait, measure_trait_math, measure_mod, measure_math_rank], errors)
	errors = variable_field('skill_rank', measure_effect, 'Trait Type', measure_trait_type, errors)
	errors = variable_field('skill_rank', measure_effect, 'Trait', measure_trait, errors)
	errors = variable_field('skill_rank', measure_effect, 'Math', measure_trait_math, errors)
	errors = variable_field('skill_rank', measure_effect, 'Skill Modifier', measure_mod, errors)
	errors = variable_field('skill_rank', measure_effect, 'Measurement Rank', measure_math_rank, errors)

	errors = variable_fields('skill_unit', 'Measurement Skill Unit Modifier', measure_effect, [measure_trait_type_unit, measure_trait_unit, measure_trait_math_unit, measure_mod_unit, measure_math_unit], errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait Type', measure_trait_type_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Trait', measure_trait_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Math', measure_trait_math_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Skill Modifier', measure_mod_unit, errors)
	errors = variable_field('skill_unit', measure_effect, 'Measurement Rank', measure_math_unit, errors)

	errors = variable_fields('condition', 'Condition Effect', type, [condition_type], errors)
	errors = variable_field('condition', type, 'Condition Type', condition_type, errors)

	errors = variable_fields('condition', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', condition_type, 'Ending Condition Change', condition2, errors)

	errors = variable_fields('damage', 'Damage Condition', condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', condition_type, 'Damage Value', condition_damage_value, errors)
	errors = variable_field('damage', condition_type, 'Damage Direction', condition_damage, errors)

	errors = variable_fields('action', 'Action Change Effect', type, [action], errors)
	errors = variable_field('action', type, 'Changed Action', action, errors)
	
	errors = variable_fields('circ', 'Circumstance Effect', type, [circumstance, circ_target], errors)
	errors = variable_field('circ', type, 'Circumstance', circumstance, errors)
	errors = variable_field('circ', type, 'Circumstance Target', circ_target, errors)
	
	errors = variable_fields('time', 'Time Modifier Effect', type, [time], errors)
	errors = variable_field('time', type, 'Time Modifier', time, errors)
	
	errors = variable_fields('damage', 'Damage Effect', type, [damage_type], errors)
	errors = variable_field('damage', type, 'Damage Type', damage_type, errors)

	errors = variable_fields('inflict', 'Inflict Damage', damage_type, [inflict_type], errors)
	errors = variable_field('inflict', damage_type, 'Inflict Damage Type', inflict_type, errors)
	
	errors = variable_fields('flat', 'Flat Damage', inflict_type, [inflict_flat], errors)
	errors = variable_field('flat', inflict_type, 'Flat vALUE', inflict_flat, errors)

	errors = variable_fields('bonus', 'Flat Damage Bonus', inflict_type, [inflict_bonus], errors)
	errors = variable_field('bonus', inflict_type, 'Bonus', inflict_bonus, errors)

	errors = variable_fields('math', 'Math Damage', inflict_type, [inflict_trait_type, inflict_trait, inflict_math, inflict_mod], errors)
	errors = variable_field('math', inflict_type, 'Trait Type', inflict_trait_type, errors)
	errors = variable_field('math', inflict_type, 'Trait', inflict_trait, errors)
	errors = variable_field('math', inflict_type, 'Math', inflict_math, errors)
	errors = variable_field('math', inflict_type, 'Math Value', inflict_mod, errors)


	errors = variable_fields('reduce', 'Reduce Damage', damage_type, [damage_mod], errors)
	errors = variable_field('reduce', damage_type, 'Modifier', damage_mod, errors)

	errors = variable_fields('object', 'Damage Object', damage_type, [object, object_effect], errors)
	errors = variable_field('object', damage_type, 'Degrees', object, errors)
	errors = variable_field('object', damage_type, 'Object Condition', object_effect, errors)
	
	errors = variable_fields('level', 'Level Effect', type, [level_type], errors)
	errors = variable_field('level', type, 'Level Type', level_type, errors)
	errors = if_or('Level', level_type, [level, level_direction], 'Level or Level Change', errors)
	errors = seperate([level, level_direction], 'Level or Level Change', errors)
	
	errors = variable_fields('knowledge', 'Gain Knowledge Effect', type, [knowledge], errors)
	errors = variable_field('knowledge', type, 'Knowledge Type', knowledge, errors)

	errors = variable_fields('bonus', 'Learn Bonus', knowledge, [knowledge_count, knowledge_specificity], errors)
	errors = variable_field('bonus', knowledge, 'Amount', knowledge_count, errors)
	errors = variable_field('bonus', knowledge, 'Specificity', knowledge_specificity, errors)
	
	errors = variable_fields('consequence', 'Consequence Effect', type, [consequence_action_type, consequence_action, consequence], errors)
	errors = variable_field('consequence', type, 'Consequence Action Type', consequence_action_type, errors)
	errors = variable_field('consequence', type, 'Consequence Action', consequence_action, errors)
	errors = variable_field('consequence', type, 'Consequence', consequence, errors)

	errors = variable_fields('check', 'Check', type, [check_type], errors)
	errors = variable_field('check', type, 'Check Type', check_type, errors)

	errors = variable_fields('1', 'Skill Check', check_type, [skill_trait_type, skill_trait, skill_dc], errors)
	errors = variable_field('1', check_type, 'Trait Type', skill_trait_type, errors)
	errors = variable_field('1', check_type, 'Trait', skill_trait, errors)
	errors = variable_field('1', check_type, 'DC', skill_dc, errors)

	errors = variable_fields('2', 'Opposed Check', check_type, [opposed], errors)
	errors = variable_field('2', check_type, 'Opposed', opposed, errors)
	
	errors = variable_fields('5', 'Arrack Check', check_type, [attack, attack_turns], errors)
	errors = variable_field('5', check_type, 'Arrack Modifier', attack, errors)
	errors = variable_field('5', check_type, 'Turns', attack_turns, errors)

	errors = variable_fields('6', 'Resistance Check', check_type, [resist_dc, resist_trait_type, resist_trait], errors)
	errors = variable_field('6', check_type, 'DC', resist_dc, errors)
	errors = variable_field('6', check_type, 'Trait Type', resist_trait_type, errors)
	errors = variable_field('6', check_type, 'Trait', resist_trait, errors)

	errors = variable_fields('3', 'Routine Check', check_type, [routine_trait_type, routine_trait, routine_mod], errors)
	errors = variable_field('3', check_type, 'Trait Type', routine_trait_type, errors)
	errors = variable_field('3', check_type, 'Trait', routine_trait, errors)
	errors = variable_field('3', check_type, 'Modifier', routine_mod, errors)

	errors = variable_fields('7', 'Comparison Check', check_type, [compare], errors)

	errors = variable_fields('duration', 'Effect Duration', type, [duration], errors)

	errors = linked_field(condition1, linked, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)
	errors = linked_field(condition2, linked, 'Condition', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_field(consequence, linked, 'Consequence', 'Degree of Success/Failure rule', 'linked degree', errors)

	errors = linked_group_check(SkillDC, 'other', target, 'other', 'target', skill_id, 'skill_id', 'a degree of success or failure for another character', 'DC', 'the target field to Other Character', errors)

	return (errors)

def skill_move_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	speed = data['speed']
	speed_rank = data['speed_rank']
	speed_rank_mod = data['speed_rank_mod']
	speed_trait_type = data['speed_trait_type']
	speed_trait = data['speed_trait']
	speed_math1 = data['speed_math1']
	speed_value1 = data['speed_value1']
	speed_math2 = data['speed_math2']
	speed_value2 = data['speed_value2']
	distance = data['distance']
	distance_rank = data['distance_rank']
	distance_value = data['distance_value']
	distance_units = data['distance_units']
	distance_rank_trait_type = data['distance_rank_trait_type']
	distance_rank_trait = data['distance_rank_trait']
	distance_rank_math1 = data['distance_rank_math1']
	distance_rank_value1 = data['distance_rank_value1']
	distance_rank_math2 = data['distance_rank_math2']
	distance_rank_value2 = data['distance_rank_value2']
	distance_unit_trait_type = data['distance_unit_trait_type']
	distance_unit_trait = data['distance_unit_trait']
	distance_unit_math1 = data['distance_unit_math1']
	distance_unit_value1 = data['distance_unit_value1']
	distance_unit_math2 = data['distance_unit_math2']
	distance_unit_value2 = data['distance_unit_value2']
	distance_math_units = data['distance_math_units']
	direction = data['direction']
	distance_description = data['distance_description']
	speed_description = data['speed_description']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	time = data['time']
	keyword = data['keyword']
	title = data['title']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = id_check(SkillDegree, degree, 'Degree', errors)
	errors = id_check(SkillCirc, circ, 'Circumstance', errors)
	errors = id_check(SkillDC, dc, 'DC', errors)
	errors = id_check(SkillTime, time, 'Time', errors)

	errors = int_check(speed_rank, 'Speed Rank', errors)
	errors = int_check(speed_trait, 'Speed Trait', errors)
	errors = int_check(speed_value1, 'First Speed Value', errors)
	errors = int_check(speed_value2, 'Second Speed Value', errors)
	errors = int_check(distance_rank, 'Distance Rank', errors)
	errors = int_check(distance_value, 'Distance Value', errors)
	errors = int_check(distance_rank_trait, 'Trait', errors)
	errors = int_check(distance_rank_value1, 'Distance Furst Value', errors)
	errors = int_check(distance_rank_value2, 'Distance Second Value', errors)
	errors = int_check(distance_unit_trait, 'Distance Trait', errors)
	errors = int_check(distance_unit_value1, 'Distance Furst Value', errors)
	errors = int_check(distance_unit_value2, 'Distance Second Value', errors)
	errors  = int_check(speed_rank_mod, 'Speed Rank Modifier', errors)

	errors = id_check(Math, speed_math1, 'Speed Msth 1', errors)
	errors = id_check(Math, speed_math2, 'Speed Msth 2', errors)
	errors = id_check(Unit, distance_units, 'Distance Units', errors)
	errors = id_check(Math, distance_rank_math1, 'Distance Msth 1', errors)
	errors = id_check(Math, distance_rank_math2, 'Distance Msth 2', errors)
	errors = id_check(Math, distance_unit_math1, 'Distance Msth 1', errors)
	errors = id_check(Math, distance_unit_math2, 'Distance Msth 2', errors)
	errors = id_check(Unit, distance_math_units, 'Distance Units', errors)
	
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)
	errors = of([speed, distance], 'You must set the effect speed or distance', errors)

	errors = variable_fields('rank', 'Speed Rank', speed, [speed_rank], errors)
	errors = variable_field('rank', speed, 'Rank', speed_rank, errors)

	errors = variable_fields('rank_mod', 'Speed Rank Modifier', speed, [speed_rank_mod], errors)
	
	errors = variable_fields('mod', 'Speed Modifier', speed, [speed_trait, speed_math1, speed_value1], errors)
	errors = variable_field('mod', speed, 'Trait', speed_trait, errors)
	errors = variable_field('mod', speed, 'First Math', speed_math1, errors)
	errors = variable_field('mod', speed, 'First Modifier', speed_value1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [speed_value2, speed_math2], errors)

	errors = required_if_any(speed, 'Speed Description', speed_description, errors)

	errors = variable_fields('rank', 'Distance Rank', distance, [distance_rank], errors)
	errors = variable_field('rank', distance, 'Rank', distance_rank, errors)

	errors = variable_fields('unit', 'Distance Value', distance, [distance_value, distance_units], errors)
	errors = variable_field('unit', distance, 'Value', distance_value, errors)
	errors = variable_field('unit', distance, 'Units', distance_units, errors)

	errors = variable_fields('unit_math', 'Unit Modifier', distance, [distance_unit_trait, distance_unit_value1, distance_unit_math1, distance_math_units], errors)
	errors = variable_field('unit_math', distance, 'Trait', distance_unit_trait, errors)
	errors = variable_field('unit_math', distance, 'First Modifier', distance_unit_value1, errors)
	errors = variable_field('unit_math', distance, 'First Math', distance_unit_math1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [distance_unit_value2, distance_unit_math2], errors)
	errors = variable_field('unit_math', distance, 'Unit', distance_math_units, errors)

	errors = variable_fields('rank_math', 'Rank Modifier', distance, [distance_rank_trait, distance_rank_value1, distance_rank_math1], errors)
	errors = variable_field('rank_math', distance, 'Trait', distance_rank_trait, errors)
	errors = variable_field('rank_math', distance, 'First Modifier', distance_rank_value1, errors)
	errors = variable_field('rank_math', distance, 'First Math', distance_rank_math1, errors)
	errors = together_names('a second modifier', ['second modifier', 'second math'], [distance_rank_value2, distance_rank_math2], errors)

	errors = required_if_any(distance, 'Distance Description', distance_description, errors)

	errors = required(direction, 'Direction', errors)

	return (errors)

def skill_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	attached = data['attached']
	frequency = data['frequency']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	opponent_trait_type = data['opponent_trait_type']
	opponent_trait = data['opponent_trait']
	opponent_mod = data['opponent_mod']
	player_check = data['player_check']
	opponent_check = data['opponent_check']
	secret = data['secret']
	recurring = data['recurring']
	multiple = data['multiple']
	recurring_value = data['recurring_value']
	description = data['description']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	time = data['time']
	keyword = data['keyword']
	degree_check = data['degree_check']
	circ_check = data['circ_check']
	dc_check = data['dc_check']
	time_check = data['time_check']
	degree_value = data['degree_value']
	dc_type = data['dc_type']
	dc_player = data['dc_player']
	circ_value = data['circ_value']
	time_type = data['time_type']
	recurring_type = data['recurring_type']



	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = int_check(mod, 'Player Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)
	errors = id_check(Check, player_check, 'Player Check', errors)
	errors = id_check(Check, opponent_check, 'Opponent Check', errors)

	errors = id_check(SkillDegreeType, degree, 'Degree Group', errors)
	errors = id_check(SkillCircType, circ, 'Circumstance Group', errors)
	errors = id_check(SkillDC, dc, 'DC', errors)
	errors = id_check(SkillTime, time, 'DC', errors)
	errors = id_check(SkillTime, recurring_value, 'Recurring Time', errors)
	errors = id_check(SkillDegree, degree_value, 'Degree', errors)
	errors = id_check(SkillDCType, dc_type, 'DC Group', errors)
	errors = id_check(SkillDC, dc_player, 'Player DC', errors)
	errors = id_check(SkillCirc, circ_value, 'Degree', errors)
	errors = id_check(SkillTimeType, time_type, 'Time Group', errors)
	errors = id_check(SkillTimeType, recurring_type, 'Recurring Time Group', errors)

	errors = required(attached, 'Attsched', errors)
	errors = required(frequency, 'Frequency', errors)
	errors = required(opponent_trait_type, 'Opponent Check Trait Typr', errors)
	errors = required(opponent_trait, 'Opponent Check Trait', errors)
	errors = required(opponent_check, 'Opponennt Check', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(description, 'Description', errors)

	errors = check_fields(recurring, 'Recurring', [recurring_value], errors)
	errors = check_field(recurring, 'Recurring', 'Recurring Value', recurring_value, errors)

	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC', errors)
	
	errors = select_check('6', opponent_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', opponent_check, dc_check, 'Skill Check', 'a DC value', errors)
	errors = select_check('6', player_check, dc_check, 'Resistance Check', 'a DC value', errors)
	errors = select_check('1', player_check, dc_check, 'Skill Check', 'a DC value', errors)

	errors = check_of(circ_check, 'Circumstance', 'a circums6ance modifier or circumstance group', [circ_value, circ], errors)
	errors = check_of(dc_check, 'DC', ' a dc value or dc group', [dc_player, dc_type, dc], errors)
	errors = check_of(degree_check, 'Degree', 'a degree value or degree group', [degree_value, degree], errors)
	errors = check_of(time_check, 'Time', 'a time effect or time effect group', [time, time_type], errors)
	errors = check_of(recurring, 'Recurring', 'recurring time or time effect group', [recurring_value, recurring_type], errors)
	errors = seperate([recurring_value, recurring_type], 'recurring', errors)

	errors = linked_group_check(SkillDC, '1', opponent_check, 'opp', 'target', dc_type, 'title', 'an Opponent Skill Check', 'DC', 'Opponent DC', errors, True)
	errors = linked_group_check(SkillDC, '6', opponent_check, 'opp', 'target', dc_type, 'title', 'an Opponent Resistance Check Check', 'DC', 'Opponent DC', errors, True)

	return (errors)

def skill_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	type = data['type']
	value_type = data['value_type']
	rank1 = data['rank1']
	rank1_value = data['rank1_value']
	rank_math = data['rank_math']
	rank2 = data['rank2']
	rank2_value = data['rank2_value']
	value = data['value']
	units = data['units']
	trait_type = data['trait_type']
	trait = data['trait']
	math = data['math']
	math_value = data['math_value']
	recovery_penalty = data['recovery_penalty']
	recovery_incurable = data['recovery_incurable']
	turns = data['turns']
	degree = data['degree']
	circ = data['circ']
	dc = data['dc']
	keyword = data['keyword']
	title = data['title']
	circ_type = data['circ_type']
	degree_type = data['degree_type']
	dc_type = data['dc_type']
	time = data['time']
	mod = data['mod']
	recovery_target = data['recovery_target']


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)	
	errors = id_check(Rank, rank1, 'First Rank', errors)
	errors = int_check(rank1_value, 'First Rank Value', errors)
	errors = id_check(Math, rank_math, 'Rank Math', errors)
	errors = id_check(Rank, rank2, 'Second Rank', errors)
	errors = int_check(rank2_value, 'Second Rank Value', errors)
	errors = int_check(value, 'Time Value', errors)
	errors = id_check(Unit, units, 'Units', errors)
	errors = id_check(Math, math, 'Msth', errors)
	errors = int_check(math_value, 'Time Math Value', errors)
	errors = int_check(recovery_penalty, 'Recovery Penalty Modifier', errors)
	errors = int_check(time, 'Time Rank', errors)
	errors = int_check(mod, 'Time Rank Modifier', errors)

	errors = int_check(turns, 'Turns', errors)
	errors = id_check(SkillDegree, degree, 'Degree', errors)
	errors = id_check(SkillCirc, circ, 'Circumstance', errors)
	errors = id_check(SkillDC, dc, 'DC', errors)
	errors = id_check(SkillDegreeType, degree_type, 'Degree Group', errors)
	errors = id_check(SkillCircType, circ_type, 'Circumstance Group', errors)
	errors = id_check(SkillDCType, dc_type, 'DC Group', errors)
	

	errors = required(type, 'Time Type', errors)
	errors = required(value_type, 'Type', errors)
	errors = required(keyword, 'Keyword', errors)
	errors = required(title, 'Title', errors)

	errors = variable_fields('value', 'Time Value', value_type, [value, units], errors)
	errors = variable_field('value', value_type, 'Value', value, errors)
	errors = variable_field('value', value_type, 'Units', units, errors)

	errors = variable_fields('math', 'Time Math', value_type, [trait_type, trait, math, math_value], errors)
	errors = variable_field('math', value_type, 'Trait Type', trait_type, errors)
	errors = variable_field('math', value_type, 'Trait', trait, errors)
	errors = variable_field('math', value_type, 'Math', math, errors)
	errors = variable_field('math', value_type, 'Value', math_value, errors)

	errors = variable_fields('rank', 'Time Measurement', value_type, [rank_math], errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank1, rank1_value], ['first rank', 'first value'], errors)
	errors = variable_field('rank', value_type, 'Math', rank_math, errors)
	errors = select_of('rank', 'uses rank math', 'time value type', value_type, [rank2, rank2_value], ['second rank', 'second value'], errors)

	errors = variable_fields('turns', 'Turns', value_type, [turns], errors)

	errors = variable_fields('time', 'Time Rank', value_type, [time], errors)

	errors = variable_fields('mod', 'Time Rank Modifier', value_type, [mod], errors)

	errors = variable_fields('recover', 'Recovery Time', type, [recovery_target], errors)
	errors = variable_field('recover', type, 'Recovery Target', recovery_target, errors)

	errors = seperate([dc, dc_type], 'DC', errors)
	errors = seperate([circ, circ_type], 'Circumstance', errors)
	errors = seperate([degree, degree_type], 'Degree', errors)

	return (errors)

def skill_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	bonus = data['bonus']
	bonus_type = data['bonus_type']
	penalty = data['penalty']
	penalty_type = data['penalty_type']
	trigger = data['trigger']
	bonus_effect = data['bonus_effect']
	penalty_effect = data['penalty_effect']
	environment = data['environment']
	environment_other = data['environment_other']
	sense = data['sense']
	mod_range = data['mod_range']
	subsense = data['subsense']
	cover = data['cover']
	conceal = data['conceal']
	maneuver = data['maneuver']
	weapon_melee = data['weapon_melee']
	weapon_ranged = data['weapon_ranged']
	tools = data['tools']
	condition = data['condition']
	power = data['power']
	consequence = data['consequence']
	creature = data['creature']
	creature_other = data['creature_other']
	emotion = data['emotion']
	emotion_other = data['emotion_other']
	conflict = data['conflict']
	profession = data['profession']
	profession_other = data['profession_other']
	bonus_trait_type = data['bonus_trait_type']
	bonus_trait = data['bonus_trait']
	bonus_check = data['bonus_check']
	bonus_check_range = data['bonus_check_range']
	bonus_conflict = data['bonus_conflict']
	penalty_trait_type = data['penalty_trait_type']
	penalty_trait = data['penalty_trait']
	penalty_check = data['penalty_check']
	penalty_check_range = data['penalty_check_range']
	penalty_conflict = data['penalty_conflict']
	bonus_active_defense = data['bonus_active_defense']
	bonus_conflict_defend = data['bonus_conflict_defend']
	penalty_active_defense = data['penalty_active_defense']
	penalty_conflict_defend = data['penalty_conflict_defend']
	multiple = data['multiple']
	multiple_count = data['multiple_count']
	lasts = data['lasts']
	skill = data['skill']
	light = data['light']


	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = int_check(bonus, 'Bonus', errors)
	errors = int_check(penalty, 'Penalty', errors)
	errors = int_check(multiple_count, 'Multiple Count', errors)

	errors = db_insert('Environment', Environment, environment, environment_other, errors)
	errors = db_insert('Emotion', Emotion, emotion, emotion_other, errors)
	errors = db_insert('Creature', Creature, creature, creature_other, errors)
	errors = db_insert('Profession', Job, profession, profession_other, errors)

	errors = id_check(Skill, skill, 'Skill', errors)
	errors = id_check(Light, light, 'Light', errors)
	errors = id_check(Environment, environment, 'Environment', errors)
	errors = id_check(Sense, sense, 'Sense', errors)
	errors = id_check(Ranged, mod_range, 'Range', errors)
	errors = id_check(SubSense, subsense, 'Subsense', errors)
	errors = id_check(Cover, cover, 'Cover', errors)
	errors = id_check(Conceal, conceal, 'Concealment', errors)
	errors = id_check(Maneuver, maneuver, 'Maneuver', errors)
	errors = id_check(WeaponType, weapon_melee, 'Melee Weapon Type', errors)
	errors = id_check(WeaponType, weapon_ranged, 'Ranged Weapon Type', errors)
	errors = id_check(Consequence, consequence, 'Consequence', errors)
	errors = id_check(Creature, creature, 'Creature', errors)
	errors = id_check(Emotion, emotion, 'Emotion', errors)
	errors = id_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = id_check(Job, profession, 'Profession', errors)
	errors = id_check(Check, bonus_check, 'Bonus Check Type', errors)
	errors = id_check(Ranged, bonus_check_range, 'Bonus Check Range', errors)
	errors = id_check(ConflictAction, bonus_conflict, 'Bonus Conflict Action', errors)
	errors = id_check(Check, penalty_check, 'Penalty Check Type', errors)
	errors = id_check(Ranged, penalty_check_range, 'Penalty Check Range', errors)
	errors = id_check(ConflictAction, penalty_conflict, 'Penalty Conflict Action', errors)
	
	errors = id_check(SkillTime, lasts, 'Bonus/Penalty Duration', errors)

	errors = of([bonus, penalty], 'You must set a value for either a bonus or a penalty.', errors)

	errors = if_fields('Bonus', bonus, [bonus_type, bonus_effect], errors)
	errors = if_field('Bonus', bonus, bonus_type, 'Bonus Type', errors)
	errors = if_field('Bonus', bonus, bonus_effect, 'Bonus Effect', errors)
	errors = if_fields('Penalty', penalty, [penalty_type, penalty_effect], errors)
	errors = if_field('Penalty', penalty, penalty_type, 'Penalty Type', errors)
	errors = if_field('Penalty', penalty, penalty_effect, 'Penalty Effect', errors)

	errors = required(lasts, 'Time Bonud/Penalty Applies', errors)

	errors = variable_fields('trait', 'Bonus Trait', bonus_effect, [bonus_trait_type, bonus_trait], errors)
	errors = variable_fields('check', 'Bonus Check', bonus_effect, [bonus_check], errors)
	errors = variable_fields('conflict', 'Bonus Conflict Action', bonus_effect, [bonus_conflict], errors)

	errors = variable_fields('trait', 'Penalty Trait', penalty_effect, [penalty_trait_type, penalty_trait], errors)
	errors = variable_fields('check', 'Penalty Check', penalty_effect, [penalty_check], errors)
	errors = variable_fields('conflict', 'Penalty Conflict Action', penalty_effect, [penalty_conflict], errors)

	errors = variable_fields('environment', 'Environment', trigger, [environment], errors)
	errors = variable_fields('cover', 'Cover', trigger, [cover], errors)
	errors = variable_fields('conceal', 'Concealment', trigger, [conceal], errors)
	errors = variable_fields('sense', 'Sense', trigger, [sense], errors)
	errors = variable_fields('subsense', 'Subsense', trigger, [subsense], errors)
	errors = variable_fields('condition', 'Condition', trigger, [condition], errors)
	errors = variable_fields('profession', 'Characters Profession', trigger, [profession], errors)
	errors = variable_fields('creature', 'Creature', trigger, [creature], errors)
	errors = variable_fields('power', 'Power', trigger, [power], errors)
	errors = variable_fields('emotion', 'Emotion', trigger, [emotion], errors)
	errors = variable_fields('consequence', 'Consequence', trigger, [consequence], errors)
	errors = variable_fields('range', 'Range', trigger, [mod_range], errors)
	errors = variable_fields('conflict', 'Conflict Action', trigger, [conflict], errors)
	errors = variable_fields('maneuver', 'Maneuver', trigger, [maneuver], errors)
	errors = variable_fields('tools', 'Tool Requirement', trigger, [tools], errors)
	errors = variable_fields('ranged', 'Ranged Weapon', trigger, [weapon_ranged], errors)
	errors = variable_fields('melee', 'Melee Weapon', trigger, [weapon_melee], errors)
	errors = variable_fields('skill', 'Skill', trigger, [skill], errors)
	errors = variable_fields('light', 'Light', trigger, [light], errors)

	return (errors)

def skill_levels_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	skill_id = data['skill_id']
	level_type = data['level_type']
	level = data['level']
	level_effect = data['level_effect']

	errors = create_check('Enhanced Skill', skill_id, SkillBonus, errors)

	errors = id_check(SkillBonus, skill_id, 'Enhanced Skill', errors)

	errors = required(level_type, 'Level Type', errors)
	errors = required(level, 'Level', errors)
	errors = required(level_effect, 'Level Effect', errors)
	

	return (errors)
