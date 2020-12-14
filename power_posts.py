from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSense, PowerTime 


def name(Table, name):
	try:
		query = db.session,query(Table).filter_by(id=name).one()
		name = query.name
	except:
		print('invalid id')
	
	return (name)

def extra_name(name):
	if name is None:
		name = 'Base Power'
	else:
		try:
			query = db.session,query(Extra).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)

def descriptor_name(name):

	if name = 1111111:
		name = 'Any Chosen Rare' 
	elif name = 2222222:
		name = 'Any Chosen Uncommon'
	elif name = 3333333:
		name = 'Any Chosen Common' 
	elif name = 4444444:
		name = 'Any Chosen Very Common' 
	elif name = 5555555:
		name = 'Any Chosen Damage'
	elif name = 6666666:
		name = 'Any Chosen Origin'
	elif name = 7777777:
		name = 'Any Chosen Source'
	elif name = 8888888:
		name = 'Any Chosen Medium Type'
	elif name = 9999999:
		name = 'Any Chosen Medium Subtype'
	elif name = 11111111:
		name = 'Any Chosen Medium'
	elif name = 22222222:
		name = 'Any Chosen Descriptor'
	else:
		try:
			query = db.session,query(PowerDes).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)


def alt_check_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	check_type = entry.check_type
	mod = entry.mod
	circumstance = entry.circumstance
	when = entry.when
	trait_type = entry.trait_type
	trait = entry.trait




def change_action_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	action = entry.action
	mod = entry.mod
	objects = entry.objects
	circumstance = entry.circumstance

def character_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	value = entry.value
	increase = entry.increase
	limited = entry.limited
	reduced = entry.reduced
	limbs = entry.limbs
	carry = entry.carry
	sustained = entry.sustained
	permanent = entry.permanent
	points = entry.points
	appear = entry.appear
	insubstantial = entry.insubstantial
	weaken = entry.weaken
	weaken_type = entry.weaken_type
	weaken_trait_type = entry.weaken_trait_type
	weaken_trait = entry.weaken_trait
	weaken_broad = entry.weaken_broad
	weaken_descriptor = entry.weaken_descriptor
	weaken_simultaneous = entry.weaken_simultaneous
	limited_by = entry.limited_by
	limited_other = entry.limited_other
	limited_emotion = entry.limited_emotion
	limited_emotion_other = entry.limited_emotion_other
	reduced_trait_type = entry.reduced_trait_type
	reduced_trait = entry.reduced_trait
	reduced_value = entry.reduced_value
	reduced_full = entry.reduced_full
	limbs_continuous = entry.limbs_continuous
	limbs_sustained = entry.limbs_sustained
	limbs_distracting = entry.limbs_distracting
	limbs_projection = entry.limbs_projection
	carry_capacity = entry.carry_capacity
	points_value = entry.points_value
	points_trait_type = entry.points_trait_type
	points_trait = entry.points_trait
	points_descriptor = entry.points_descriptor
	appear_target = entry.appear_target
	appear_description = entry.appear_description
	insub_type = entry.insub_type
	insub_description = entry.insub_description
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)

def circ_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	mod = entry.mod
	rounds = entry.rounds
	description = entry.description
	circ_type = entry.circ_type
	circ_range = entry.circ_range
	check_who = entry.check_who
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	null_type = entry.null_type
	null_condition = entry.null_condition
	null_descriptor = entry.null_descriptor
	null_trait_type = entry.null_trait_type
	null_trait = entry.null_trait

	extra = extra_name(extra_id)
	circ_range = name(Range, circ_range)
	null_descriptor = descriptor_name(null_descriptor)


def create_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	solidity = entry.solidity
	visibility = entry.visibility
	complexity = entry.complexity
	volume = entry.volume
	toughness = entry.toughness
	mass = entry.mass
	damageable = entry.damageable
	maintained = entry.maintained
	repairable = entry.repairable
	moveable = entry.moveable
	stationary = entry.stationary
	trap = entry.trap
	ranged = entry.ranged
	weapon = entry.weapon
	support = entry.support
	real = entry.real
	cover = entry.cover
	conceal = entry.conceal
	incoming = entry.incoming
	outgoing = entry.outgoing
	transform = entry.transform
	transform_type = entry.transform_type
	transform_start_mass = entry.transform_start_mass
	transfom_mass = entry.transfom_mass
	transform_start_descriptor = entry.transform_start_descriptor
	transform_end_descriptor = entry.transform_end_descriptor
	move_player = entry.move_player
	move_player_trait = entry.move_player_trait
	move_opponent_check = entry.move_opponent_check
	move_opponent_ability = entry.move_opponent_ability
	move_opponent_rank = entry.move_opponent_rank
	trap_type = entry.trap_type
	trap_dc = entry.trap_dc
	trap_trait_type = entry.trap_trait_type
	trap_trait = entry.trap_trait
	trap_resist_check = entry.trap_resist_check
	trap_resist_trait = entry.trap_resist_check
	trap_resist_dc = entry.trap_resist_dc
	trap_escape = entry.trap_escape
	ranged_type = entry.ranged_type
	ranged_dc = entry.ranged_dc
	ranged_trait_type = entry.ranged_trait_type
	ranged_trait = entry.ranged_trait
	ranged_damage_type = entry.ranged_damage_type
	ranged_damage_value = entry.ranged_damage_value
	weapon_trait_type = entry.weapon_trait_type
	weapon_trait = entry.weapon_trait
	weapon_mod = entry.weapon_mod
	weapon_damage_type = entry.weapon_damage_type
	weapon_damage = entry.weapon_damage
	support_strength = entry.support_strength
	support_strengthen = entry.support_strengthen
	support_action = entry.support_action
	support_action_rounds = entry.support_action_rounds
	support_effort = entry.support_effort
	support_effort_rounds = entry.support_effort_rounds
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)
	complexity = name(Complex, complexity)
	transform_start_descriptor = descriptor_name(transform_start_descriptor)
	transform_end_descriptor = descriptor_name(transform_end_descriptor)
	move_opponent_ability = name(Ability, move_opponent_ability)

def damage_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	strength = entry.strength
	damage_type = entry.damage_type
	descriptor = entry.descriptor

	extra = extra_name(extra_id)
	damage_type = name(Descriptor, damage_type)
	descriptor = descriptor_name(descriptor)

def dc_table_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	dc = entry.dc
	description = entry.description
	value = entry.value
	math_value = entry.math_value
	math = entry.math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
	descriptor_check = entry.descriptor_check
	condition = entry.condition
	keyword_check = entry.keyword_check
	check_type = entry.check_type
	descriptor = entry.descriptor
	descriptor_possess = entry.descriptor_possess
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_mod = entry.check_mod
	levels = entry.level

	extra = extra_name(extra_id)
	math = name(Math, math)
	descriptor = descriptor_name(descriptor)
	level = name(PowerLevels, level)

def defense_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	defense = entry.defense
	use = entry.use
	mod = entry.mod
	roll = entry.roll
	outcome = entry.outcome
	dodge = entry.dodge
	fortitude = entry.fortitude
	parry = entry.parry
	toughness = entry.toughness
	will = entry.will
	resist_area = entry.resist_area
	resist_perception = entry.resist_perception
	reflect = entry.reflect
	immunity = entry.immunity
	reflect_action = entry.reflect_action
	reflect_check = entry.reflect_check
	reflect_dc = entry.reflect_dc
	reflect_opposed_trait_type = entry.reflect_opposed_trait_type
	reflect_opposed_trait = entry.reflect_opposed_trait
	reflect_resist_trait_type = entry.reflect_resist_trait_type
	reflect_resist_trait = entry.reflect_resist_trait
	immunity_type = entry.immunity_type
	immunity_trait_type = entry.immunity_trait_type
	immunity_trait = entry.immunity_trait
	immunity_descriptor = entry.immunity_descriptor
	immunity_damage = entry.immunity_damage
	immunity_rule = entry.immunity_rule
	cover_check = entry.cover_check
	cover_type = entry.cover_type

	extra = extra_name(extra_id)
	reflect_action = name(Action, reflect_action)
	reflect_check = name(Check, reflect_check)
	immunity_descriptor = descriptor_name(immunity_descriptor)
	immunity_damage = name(Descriptor, immunity_damage)

def degree_mod_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	value = entry.value
	deg_type = entry.deg_type
	circ_value = entry.circ_value
	circ_turns = entry.circ_turns
	circ_trait_type = entry.circ_trait_type
	circ_trait = entry.circ_trait
	measure_type = entry.measure_type
	measure_val1 = entry.measure_val1
	measure_math = entry.measure_math
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_value = entry.measure_value
	measure_rank = entry.measure_rank
	deg_condition_type = entry.deg_condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	nullify = entry.nullify
	cumulative = entry.cumulative
	linked = entry.linked
	level = entry.level

	extra = extra_name(extra_id)
	measure_math = name(Math, measure_math)
	measure_rank = name(Rank, measure_rank)
	level = name(PowerLevels, level)

def degree_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	degree_type = entry.degree_type
	degree = entry.degree
	keyword = entry.keyword
	desscription = entry.desscription
	extra_effort = entry.extra_effort
	cumulative = entry.cumulative
	target = entry.target

	extra = extra_name(extra_id)


def environment_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	radius = entry.radius
	distance = entry.distance
	rank = entry.rank
	condition_check = entry.condition_check
	impede = entry.impede
	conceal = entry.conceal
	visibility = entry.visibility
	selective = entry.selective
	immunity = entry.immunity
	immunity_type = entry.immunity_type
	temp_type = entry.temp_type
	immunity_extremity = entry.immunity_extremity
	immunity_environment = entry.immunity_environment
	no_penalty = entry.no_penalty
	no_circumstance = entry.no_circumstance
	immunity_other = entry.immunity_other
	condition_temp_type = entry.condition_temp_type
	temp_extremity = entry.temp_extremity
	move_nature = entry.move_nature
	move_speed = entry.move_speed
	move_cost_circ = entry.move_cost_circ
	move_other = entry.move_other
	conceal_type = entry.conceal_type
	visibility_trait_type = entry.visibility_trait_type
	visibility_trait = entry.visibility_trait
	visibility_mod = entry.visibility_mod
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)


def levels_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	level_type = entry.level_type
	level = entry.level
	level_effect = entry.level_effect


	extra = extra_name(extra_id)

def minion_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	points = entry.points
	condition = entry.condition
	player_condition = entry.player_condition
	link = entry.link
	variable_type = entry.variable_type
	multiple = entry.multiple
	attitude = entry.attitude
	resitable = entry.resitable
	heroic = entry.heroic
	sacrifice = entry.sacrifice
	sacrifice_cost = entry.sacrifice_cost
	attitude_type = entry.attitude_type
	attitude_trait_type = entry.attitude_trait_type
	attitude_trait = entry.attitude_trait
	resitable_check = entry.resitable_check
	resitable_dc = entry.resitable_dc
	multiple_value = entry.multiple_value
	horde = entry.horde

	extra = extra_name(extra_id)	
	attitude_type = name(PowerLevels, attitude_type)
	resitable_check = name(Defense, resitable_check)

def mod_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	affects_objects = entry.affects_objects
	area = entry.area
	persistent = entry.persistent
	incurable = entry.incurable
	selective = entry.selective
	limited = entry.limited
	innate = entry.innate
	others = entry.others
	sustained = entry.sustained
	reflect = entry.reflect
	redirect = entry.redirect
	half = entry.half
	affects_corp = entry.affects_corp
	continuous = entry.continuous
	vulnerable = entry.vulnerable
	precise = entry.precise
	progressive = entry.progressive
	subtle = entry.subtle
	permanent = entry.permanent
	points = entry.points
	ranks = entry.ranks
	action = entry.action
	side_effect = entry.side_effect
	concentration = entry.concentration
	simultaneous = entry.simultaneous
	effortless = entry.effortless
	noticeable = entry.noticeable
	unreliable = entry.unreliable
	objects_alone = entry.objects_alone
	objects_character = entry.objects_character
	effortless_degree = entry.effortless_degree
	effortless_retries = entry.effortless_retries
	simultaneous_descriptor = entry.simultaneous_descriptor
	area_mod = entry.area_mod
	area_range = entry.area_range
	area_per_rank = entry.area_per_rank
	area_descriptor = entry.area_descriptor
	limited_type = entry.limited_type
	limited_mod = entry.limited_mod
	limited_level = entry.limited_level
	limited_source = entry.limited_source
	limited_task_type = entry.limited_task_type
	limited_task = entry.limited_task
	limited_trait_type = entry.limited_trait_type
	limited_trait = entry.limited_trait
	limited_description = entry.limited_description
	limited_subjects = entry.limited_subjects
	limited_extra = entry.limited_extra
	limited_language_type = entry.limited_language_type
	limited_degree = entry.limited_degree
	limited_sense = entry.limited_sense
	limited_subsense = entry.limited_subsense
	limited_descriptor = entry.limited_descriptor
	limited_range = entry.limited_range
	side_effect_type = entry.side_effect_type
	side_level = entry.side_level
	side_other = entry.side_other
	reflect_check = entry.reflect
	reflect_trait_type = entry.reflect_trait_type
	reflect_trait = entry.reflect_trait
	reflect_descriptor = entry.reflect_descriptor
	subtle_opponent_trait_type = entry.subtle_opponent_trait_type
	subtle_opponent_trait = entry.subtle_opponent_trait
	subtle_dc = entry.subtle_dc
	subtle_null_trait_type = entry.subtle_null_trait_type
	subtle_null_trait = entry.subtle_opponent_trait
	others_carry = entry.others_carry
	others_touch = entry.others_touch
	others_touch_continuous = entry.others_touch_continuous
	ranks_trait_type = entry.ranks_trait_type
	ranks_trait = entry.ranks_trait
	ranks_ranks = entry.ranks_ranks
	ranks_mod = entry.ranks_mod
	points_type = entry.points_type
	points_reroll_target = entry.points_reroll_target
	points_reroll_cost = entry.points_reroll_cost
	points_rerolls = entry.points_rerolls
	points_reroll_result = entry.points_reroll_result
	ranks_cost = entry.ranks_cost
	cost = entry.cost

	extra = extra_name(extra_id)
	objects_alone = name(Defense, objects_alone)
	objects_character = name(Defense, objects_character)
	simultaneous_descriptor = descriptor_name(simultaneous_descriptor)
	area_descriptor = descriptor_name(area_descriptor)
	limited_level = name(PowerLevels, limited_level)
	limited_source = descriptor_name(limited_source)
	limited_extra = name(Extra, limited_extra)
	limited_sense = name(Sense, limited_sense)
	limited_descriptor = descriptor_name(limited_descriptor)
	limited_range = name(Range, limited_range)
	side_level = name(PowerLevels, side_level)
	reflect_check = name(Check, reflect_check)
	reflect_descriptor = descriptor_name(reflect_descriptor)
	
def move_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	rank = entry.rank
	math = entry.math	
	mod = entry.mod
	per_rank = entry.per_rank
	flight = entry.flight
	aquatic = entry.aquatic
	ground = entry.ground
	condition = entry.condition
	direction = entry.direction
	distance_type = entry.distance_type
	distance_value = entry.distance_value
	distance_math_value = entry.distance_math_value
	distance_math = entry.distance_math
	distance_math_value2 = entry.distance_math_value2
	distance_mod = entry.distance_mod
	dc = entry.dc
	others = entry.others
	continuous = entry.continuous
	subtle = entry.subtle
	concentration = entry.concentration
	obstacles = entry.obstacles
	objects = entry.objects
	permeate = entry.permeate
	special = entry.special
	prone = entry.prone
	check_type = entry.check_type
	obstacles_check = entry.obstacles_check
	concealment = entry.concealment
	extended = entry.extended
	mass = entry.mass
	mass_value = entry.mass_value
	extended_actions = entry.extended_actions
	acquatic_type = entry.acquatic_type
	concealment_sense = entry.concealment_sense
	concealment_trait_type = entry.concealment_trait_type
	concealment_trait = entry.concealment_trait
	permeate_type = entry.permeate_type
	permeate_speed = entry.permeate_speed
	permeate_cover = entry.permeate_cover
	special_type = entry.special_type
	teleport_type = entry.teleport_type
	teleport_change = entry.teleport_change
	teleport_portal = entry.teleport_portal
	teleport_obstacles = entry.teleport_obstacles
	dimension_type = entry.dimension_type
	dimension_mass_rank = entry.dimension_mass_rank
	dimension_descriptor = entry.dimension_descriptor
	special_space = entry.special_space
	special_time = entry.special_time
	special_time_carry = entry.special_time_carry
	ground_type = entry.ground_type
	ground_permanence = entry.ground_permanence
	ground_time = entry.ground_time
	ground_units = entry.ground_units
	ground_ranged = entry.ground_ranged
	subtle_trait_type = entry.subtle_trait_type
	subtle_trait = entry.subtle_trait
	subtle_mod = entry.subtle_mod
	flight_resist = entry.flight_resist
	flight_equip = entry.flight_equip
	flight_conditions = entry.flight_conditions
	objects_check = entry.objects_check
	objects_attack = entry.objects_attack
	objects_skill_type = entry.objects_skill_type
	objects_skill = entry.objects_skill
	objects_direction = entry.objects_direction
	objects_damage = entry.objects_damage
	damage_type = entry.damage_type
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_free = entry.check_free
	ranks = entry.ranks
	cost = entry.cost

	extra = extra_name(extra_id)
	math = name(Math, math)
	distance_math = name(Math, distance_math)
	concealment_sense = name(Sense, concealment_sense)
	dimension_descriptor = descriptor_name(dimension_descriptor)
	ground_type = name(Ground, ground_type)
	ground_units = name(Unit, ground_units)
	objects_check = name(Check, objects_check)
	objects_attack = name(ConflictAction, objects_attack)

def opposed_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check

	extra = extra_name(extra_id)
	player_check = name(Check, player_check)
	opponent_check = name(Check, opponent_check)

def ranged_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	range_type = entry.range_type
	flat_value = entry.flat_value
	flat_units = entry.flat_units
	flat_rank = entry.flat_rank
	flat_rank_value = entry.flat_rank_value
	flat_rank_units = entry.flat_rank_units
	flat_rank_rank = entry.flat_rank_rank
	flat_rank_distance = entry.flat_rank_distance
	flat_rank_distance_rank = entry.flat_rank_distance_rank
	units_rank_start_value = entry.units_rank_start_value
	units_rank_value = entry.units_rank_value
	units_rank_units = entry.units_rank_units
	units_rank_rank = entry.units_rank_rank
	rank_distance_start = entry.rank_distance_start
	rank_distance = entry.rank_distance
	rank_effect_rank = entry.rank_effect_rank
	effect_mod_math = entry.effect_mod_math
	effect_mod = entry.effect_mod
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_math = entry.check_math
	check_mod = entry.check_mod
	trait_trait_type = entry.trait_trait_type
	trait_trait = entry.trait_trait
	trait_math = entry.trait_math
	trait_mod = entry.trait_mod
	distance_mod_rank = entry.distance_mod_rank
	distance_mod_math = entry.distance_mod_math
	distance_mod_trait_type = entry.distance_mod_trait_type
	distance_mod_trait = entry.distance_mod_trait
	dc = entry.dc
	dc_value = entry.dc_value
	dc_trait_type = entry.dc_trait_type
	dc_trait = entry.dc_trait

	extra = extra_name(extra_id)
	flat_units = name(Unit, flat_units)
	flat_rank_units = name(Unit, flat_rank_units)
	units_rank_units = name(Unit, units_rank_units)
	effect_mod_math = name(Math, effect_mod_math)
	check_math = name(Math, check_math)
	trait_math = name(Math, trait_math)
	distance_mod_math = name(Math, distance_mod_math)

def resist_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	mod = entry.mod	
	rounds = entry.rounds
	circumstance = entry.circumstance
	resist_check_type = entry.resist_check_type
	trait_type = entry.trait_type
	trait = entry.trait
	descriptor = entry.descriptor
	requires_check = entry.requires_check
	check_type = entry.check_type
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait

	extra = extra_name(extra_id)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)

def resisted_by_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id	
	trait_type = entry.trait_type
	dc = entry.dc
	mod = entry.mod
	description = entry.description
	trait = entry.trait
	effect = entry.effect
	level = entry.level
	degree = entry.degree
	descriptor = entry.descriptor
	weaken_max = entry.weaken_max
	weaken_restored = entry.weaken_restored
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage =  entry.damage
	strength = entry.strength
	nullify_descriptor = entry.nullify_descriptor
	nullify_alternate = entry.nullify_alternate
	extra_effort = entry.extra_effort

	extra = extra_name(extra_id)
	level = name(PowerLevels, level)
	descriptor = descriptor_name(descriptor)
	nullify_descriptor = descriptor_name(nullify_descriptor)
	nullify_alternate = name(Defense, nullify_alternate)


def reverse_effect_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	degree = entry.degree
	when = entry.when
	check_check = entry.check_check
	time_check = entry.time_check
	trait_type = entry.trait_type
	trait = entry.trait
	value_type = entry.value_type
	value_dc = entry.value_dc
	math_dc = entry.math_dc
	math = entry.math
	time_value = entry.time_value
	time_unit = entry.time_unit


	extra = extra_name(extra_id)
	math = name(Math, math)
	time_unit = name(Unit, time_unit)


def sense_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	sense = entry.sense
	subsense = entry.subsense
	sense_cost = entry.sense_cost
	subsense_cost = entry.subsense_cost
	skill = entry.skill
	skill_required = entry.skill_required
	sense_type = entry.sense_type
	height_trait_type = entry.height_trait_type
	height_trait = entry.height_trait
	height_power_required = entry.height_power_required
	height_ensense = entry.height_ensense
	resist_trait_type = entry.resist_trait_type
	resist_trait = entry.resist_trait
	resist_immune = entry.resist_immune
	resist_permanent = entry.resist_permanent
	resist_circ = entry.resist_circ
	objects = entry.objects
	exclusive = entry.exclusive
	gm = entry.gm
	dark = entry.dark
	lighting = entry.lighting
	time = entry.time
	dimensional = entry.dimensional
	radius = entry.radius
	accurate = entry.accurate
	acute = entry.acute
	time_set = entry.time_set
	time_value = entry.time_value
	time_unit = entry.time_unit
	time_skill = entry.time_skill	
	time_bonus = entry.time_bonus
	time_factor = entry.time_factor
	distance = entry.distance
	distance_dc = entry.distance_dc
	distance_mod = entry.distance_mod
	distance_value = entry.distance_value
	distance_unit = entry.distance_unit
	distance_factor = entry.distance_factor
	dimensional_type = entry.dimensional_type
	ranks = entry.ranks
	cost = entry.cost


	extra = extra_name(extra_id)
	skill = name(Skill, skill)
	time_unit = name(Unit, time_unit)
	time_skill = name(Skill, time_skill)
	distance_unit = name(Unit, distance_unit)




def time_post(entry):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	power_id = entry.power_id
	extra_id = entry.extra_id
	time_type = entry.time_type
	value_type = entry.value_type
	value = entry.value
	units = entry.units
	time_value = entry.time_value
	math = entry.math
	trait_type = entry.trait_type
	trait = entry.trait
	dc = entry.dc
	descriptor = entry.descriptor
	check_type = entry.check_type
	recovery = entry.recovery
	recovery_penalty = entry.recovery_penalty
	recovery_time = entry.recovery_time
	recovery_incurable = entry.recovery_incurable

	extra = extra_name(extra_id)
	units = name(Unit, units)
	math = name(Math, math)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)