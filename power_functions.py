def alt_check_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	check_type = data['check_type']
	mod = data['mod']
	circumstance = data['circumstance']
	when = data['when']
	trait_type = data['trait_type']
	trait = data['trait']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def change_action_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	action = data['action']
	mod = data['mod']
	objects = data['objects']
	circumstance = data['circumstance']

	errors['success'] = error
	errors['error_msgs'] = error_msgs


def character_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	value = data['value']
	increase = data['increase']
	limited = data['limited']
	reduced = data['reduced']
	limbs = data['limbs']
	carry = data['carry']
	sustained = data['sustained']
	permanent = data['permanent']
	points = data['points']
	appear = data['appear']
	insubstantial = data['insubstantial']
	weaken = data['weaken']
	weaken_type = data['weaken_type']
	weaken_trait_type = data['weaken_trait_type']
	weaken_trait = data['weaken_trait']
	weaken_broad = data['weaken_broad']
	weaken_descriptor = data['weaken_descriptor']
	weaken_simultaneous = data['weaken_simultaneous']
	limited_by = data['limited_by']
	limited_other = data['limited_other']
	limited_emotion = data['limited_emotion']
	limited_emotion_other = data['limited_emotion_other']
	reduced_trait_type = data['reduced_trait_type']
	reduced_trait = data['reduced_trait']
	reduced_value = data['reduced_value']
	reduced_full = data['reduced_full']
	limbs_continuous = data['limbs_continuous']
	limbs_sustained = data['limbs_sustained']
	limbs_distracting = data['limbs_distracting']
	limbs_projection = data['limbs_projection']
	carry_capacity = data['carry_capacity']
	points_value = data['points_value']
	points_trait_type = data['points_trait_type']
	points_trait = data['points_trait']
	points_descriptor = data['points_descriptor']
	appear_target = data['appear_target']
	appear_description = data['appear_description']
	insub_type = data['insub_type']
	insub_description = data['insub_description']
	cost = data['cost']
	ranks = data'ranks']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def circ_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	mod = data['mod']
	rounds = data['rounds']
	description = data['description']
	circ_type = data['circ_type']
	circ_range = data['circ_range']
	check_who = data['check_who']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	null_type = data['null_type']
	null_condition = data['null_condition']
	null_descriptor = data['null_descriptor']
	null_trait_type = data['null_trait_type']
	null_trait = data['null_trait']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def create_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	solidity = data['solidity']
	visibility = data['visibility']
	complexity = data['complexity']
	volume = data['volume']
	toughness = data['toughness']
	mass = data['mass']
	damageable = data['damageable']
	maintained = data['maintained']
	repairable = data['repairable']
	moveable = data['moveable']
	stationary = data['stationary']
	trap = data['trap']
	ranged = data['ranged']
	weapon = data['weapon']
	support = data['support']
	real = data['real']
	cover = data['cover']
	conceal = data['conceal']
	incoming = data['incoming']
	outgoing = data['outgoing']
	transform = data['transform']
	transform_type = data['transform_type']
	transform_start_mass = data['transform_start_mass']
	transfom_mass = data['transfom_mass']
	transform_start_descriptor = data['transform_start_descriptor']
	transform_end_descriptor = data['transform_end_descriptor']
	move_player = data['move_player']
	move_player_trait = data['move_player_trait']
	move_opponent_check = data['move_opponent_check']
	move_opponent_ability = data['move_opponent_ability']
	move_opponent_rank = data['move_opponent_rank']
	trap_type = data['trap_type']
	trap_dc = data['trap_dc']
	trap_trait_type = data['trap_trait_type']
	trap_trait = data['trap_trait']
	trap_resist_check = data['trap_resist_check']
	trap_resist_trait = data['trap_resist_trait']
	trap_resist_dc = data['trap_resist_dc']
	trap_escape = data['trap_escape']
	ranged_type = data['ranged_type']
	ranged_dc = data['ranged_dc']
	ranged_trait_type = data['ranged_trait_type']
	ranged_trait = data['ranged_trait']
	ranged_damage_type = data['ranged_damage_type']
	ranged_damage_value = data['ranged_damage_value']
	weapon_trait_type = data['weapon_trait_type']
	weapon_trait = data['weapon_trait']
	weapon_mod = data['weapon_mod']
	weapon_damage_type = data['weapon_damage_type']
	weapon_damage = data['weapon_damage']
	support_strength = data['support_strength']
	support_strengthen = data['support_strengthen']
	support_action = data['support_action']
	support_action_rounds = data['support_action_rounds']
	support_effort = data['support_effort']
	support_effort_rounds = data['support_effort_rounds']
	cost = data['cost']
	ranks = ['ranks']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def damage_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	strength = data['strength']
	damage_type = data['damage_type']
	descriptor = data['descriptor']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def dc_table_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	dc = data['dc']
	description = data['description']
	value = data['value']
	math_value = data['math_value']
	math = data['math']
	math_trait_type = data['math_trait_type']
	math_trait = data['math_trait']
	descriptor_check = data['descriptor_check']
	condition = data['condition']
	keyword_check = data['keyword_check']
	check_type = data['check_type']
	descriptor = data['descriptor']
	descriptor_possess = data['descriptor_possess']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_mod = data['check_mod']
	levels = data['levels']
	level = data['level']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def defense_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	defense = data['defense']
	use = data['use']
	mod = data['mod']
	roll = data['roll']
	outcome = data['outcome']
	dodge = data['dodge']
	fortitude = data['fortitude']
	parry = data['parry']
	toughness = data['toughness']
	will = data['will']
	resist_area = data['resist_area']
	resist_perception = data['resist_perception']
	reflect = data['reflect']
	immunity = data['immunity']
	reflect_action = data['reflect_action']
	reflect_check = data['reflect_check']
	reflect_dc = data['reflect_dc']
	reflect_opposed_trait_type = data['reflect_opposed_trait_type']
	reflect_opposed_trait = data['reflect_opposed_trait']
	reflect_resist_trait_type = data['reflect_resist_trait_type']
	reflect_resist_trait = data['reflect_resist_trait']
	immunity_type = data['immunity_type']
	immunity_trait_type = data['immunity_trait_type']
	immunity_trait = data['immunity_trait']
	immunity_descriptor = data['immunity_descriptor']
	immunity_damage = data['immunity_damage']
	immunity_rule = data['immunity_rule']
	cover_check = data['cover_check']
	cover_type = data['cover_type']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def degree_mod_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	value = data['value']
	deg_type = data['deg_type']
	circ_value = data['circ_value']
	circ_turns = data['circ_turns']
	circ_trait_type = data['circ_trait_type']
	circ_trait = data['circ_trait']
	measure_type = data['measure_type']
	measure_val1 = data['measure_val1']
	measure_math = data['measure_math']
	measure_trait_type = data['measure_trait_type']
	measure_trait = data['measure_trait']
	measure_value = data['measure_value']
	measure_rank = data['measure_rank']
	deg_condition_type = data['deg_condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']
	level = data['level']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def degree_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	degree_type = data['degree_type']
	degree = data['degree']
	keyword = data['keyword']
	desscription = data['desscription']
	extra_effort = data['extra_effort']
	cumulative = data['cumulative']
	target = data['target']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def environment_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	radius = data['radius']
	distance = data['distance']
	rank = data['rank']
	condition_check = data['condition_check']
	impede = data['impede']
	conceal = data['conceal']
	visibility = data['visibility']
	selective = data['selective']
	immunity = data['immunity']
	immunity_type = data['immunity_type']
	temp_type = data['temp_type']
	immunity_extremity = data['immunity_extremity']
	immunity_environment = data['immunity_environment']
	no_penalty = data['no_penalty']
	no_circumstance = data['no_circumstance']
	immunity_other = data['immunity_other']
	condition_temp_type = data['condition_temp_type']
	temp_extremity = data['temp_extremity']
	move_nature = data['move_nature']
	move_speed = data['move_speed']
	move_cost_circ = data['move_cost_circ']
	move_other = data['move_other']
	conceal_type = data['conceal_type']
	visibility_trait_type = data['visibility_trait_type']
	visibility_trait = data['visibility_trait']
	visibility_mod = data['visibility_mod']
	cost = data['cost']
	ranks = data['ranks']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def levels_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	level_effect = request.get_json()['level_effect']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def minion_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	points = request.get_json()['points']
	condition = request.get_json()['condition']
	player_condition = request.get_json()['player_condition']
	link = request.get_json()['link']
	variable_type = request.get_json()['variable_type']
	multiple = request.get_json()['multiple']
	attitude = request.get_json()['attitude']
	resitable = request.get_json()['resitable']
	heroic = request.get_json()['heroic']
	sacrifice = request.get_json()['sacrifice']
	sacrifice_cost = request.get_json()['sacrifice_cost']
	attitude_type = request.get_json()['attitude_type']
	attitude_trait_type = request.get_json()['attitude_trait_type']
	attitude_trait = request.get_json()['attitude_trait']
	resitable_check = request.get_json()['resitable_check']
	resitable_dc = request.get_json()['resitable_dc']
	multiple_value = request.get_json()['multiple_value']
	horde = request.get_json()['horde']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def mod_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	affects_objects = data['affects_objects']
	area = data['area']
	persistent = data['persistent']
	incurable = data['incurable']
	selective = data['selective']
	limited = data['limited']
	innate = data['innate']
	others = data['others']
	sustained = data['sustained']
	reflect = data['reflect']
	redirect = data['redirect']
	half = data['half']
	affects_corp = data['affects_corp']
	continuous = data['continuous']
	vulnerable = data['vulnerable']
	precise = data['precise']
	progressive = data['progressive']
	subtle = data['subtle']
	permanent = data['permanent']
	points = data['points']
	ranks = data['ranks']
	action = data['action']
	side_effect = data['side_effect']
	concentration = data['concentration']
	simultaneous = data['simultaneous']
	effortless = data['effortless']
	noticeable = data['noticeable']
	unreliable = data['unreliable']
	objects_alone = data['objects_alone']
	objects_character = data['objects_character']
	effortless_degree = data['effortless_degree']
	effortless_retries = data['effortless_retries']
	simultaneous_descriptor = data['simultaneous_descriptor']
	area_mod = data['area_mod']
	area_range = data['area_range']
	area_per_rank = data['area_per_rank']
	area_descriptor = data['area_descriptor']
	limited_type = data['limited_type']
	limited_mod = data['limited_mod']
	limited_level = data['limited_level']
	limited_source = data['limited_source']
	limited_task_type = data['limited_task_type']
	limited_task = data['limited_task']
	limited_trait_type = data['limited_trait_type']
	limited_trait = data['limited_trait']
	limited_description = data['limited_description']
	limited_subjects = data['limited_subjects']
	limited_extra = data['limited_extra']
	limited_language_type = data['limited_language_type']
	limited_degree = data['limited_degree']
	limited_sense = data['limited_sense']
	limited_subsense = data['limited_subsense']
	limited_descriptor = data['limited_descriptor']
	limited_range = data['limited_range']
	side_effect_type = data['side_effect_type']
	side_level = data['side_level']
	side_other = data['side_other']
	reflect_check = data['reflect_check']
	reflect_trait_type = data['reflect_trait_type']
	reflect_trait = data['reflect_trait']
	reflect_descriptor = data['reflect_descriptor']
	subtle_opponent_trait_type = data['subtle_opponent_trait_type']
	subtle_opponent_trait = data['subtle_opponent_trait']
	subtle_dc = data['subtle_dc']
	subtle_null_trait_type = data['subtle_null_trait_type']
	subtle_null_trait = data['subtle_null_trait']
	others_carry = data['others_carry']
	others_touch = data['others_touch']
	others_touch_continuous = data['others_touch_continuous']
	ranks_trait_type = data['ranks_trait_type']
	ranks_trait = data['ranks_trait']
	ranks_ranks = data['ranks_ranks']
	ranks_mod = data['ranks_mod']
	points_type = data['points_type']
	points_reroll_target = data['points_reroll_target']
	points_reroll_cost = data['points_reroll_cost']
	points_rerolls = data['points_rerolls']
	points_reroll_result = data['points_reroll_result']
	ranks_cost = data['ranks_cost']
	cost = data['cost']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def move_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	rank = data['rank']
	math = data['math']
	mod = data['mod']
	per_rank = data['per_rank']
	flight = data['flight']
	aquatic = data['aquatic']
	ground = data['ground']
	condition = data['condition']
	direction = data['direction']
	distance_type = data['distance_type']
	distance_value = data['distance_value']
	distance_math_value = data['distance_math_value']
	distance_math = data['distance_math']
	distance_math_value2 = data['distance_math_value2']
	distance_mod = data['distance_mod']
	dc = data['dc']
	others = data['others']
	continuous = data['continuous']
	subtle = data['subtle']
	concentration = data['concentration']
	obstacles = data['obstacles']
	objects = data['objects']
	permeate = data['permeate']
	special = data['special']
	prone = data['prone']
	check_type = data['check_type']
	obstacles_check = data['obstacles_check']
	concealment = data['concealment']
	extended = data['extended']
	mass = data['mass']
	mass_value = data['mass_value']
	extended_actions = data['extended_actions']
	acquatic_type = data['acquatic_type']
	concealment_sense = data['concealment_sense']
	concealment_trait_type = data['concealment_trait_type']
	concealment_trait = data['concealment_trait']
	permeate_type = data['permeate_type']
	permeate_speed = data['permeate_speed']
	permeate_cover = data['permeate_cover']
	special_type = data['special_type']
	teleport_type = data['teleport_type']
	teleport_change = data['teleport_change']
	teleport_portal = data['teleport_portal']
	teleport_obstacles = data['teleport_obstacles']
	dimension_type = data['dimension_type']
	dimension_mass_rank = data['dimension_mass_rank']
	dimension_descriptor = data['dimension_descriptor']
	special_space = data['special_space']
	special_time = data['special_time']
	special_time_carry = data['special_time_carry']
	ground_type = data['ground_type']
	ground_permanence = data['ground_permanence']
	ground_time = data['ground_time']
	ground_units = data['ground_units']
	ground_ranged = data['ground_ranged']
	subtle_trait_type = data['subtle_trait_type']
	subtle_trait = data['subtle_trait']
	subtle_mod = data['subtle_mod']
	flight_resist = data['flight_resist']
	flight_equip = data['flight_equip']
	flight_conditions = data['flight_conditions']
	objects_check = data['objects_check']
	objects_attack = data['objects_attack']
	objects_skill_type = data['objects_skill_type']
	objects_skill = data['objects_skill']
	objects_direction = data['objects_direction']
	objects_damage = data['objects_damage']
	damage_type = data['damage_type']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_free = data['check_free']
	ranks = data['ranks']
	cost = data['cost']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def opposed_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	opponent_trait_type = data['opponent_trait_type']
	opponent_trait = data['opponent_trait']
	opponent_mod = data['opponent_mod']
	player_check = data['player_check']
	opponent_check = data['opponent_check']

	errors['success'] = error
	errors['error_msgs'] = error_msgs


def ranged_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	range_type = data['range_type']
	flat_value = data['flat_value']
	flat_units = data['flat_units']
	flat_rank = data['flat_rank']
	flat_rank_value = data['flat_rank_value']
	flat_rank_units = data['flat_rank_units']
	flat_rank_rank = data['flat_rank_rank']
	flat_rank_distance = data['flat_rank_distance']
	flat_rank_distance_rank = data['flat_rank_distance_rank']
	units_rank_start_value = data['units_rank_start_value']
	units_rank_value = data['units_rank_value']
	units_rank_units = data['units_rank_units']
	units_rank_rank = data['units_rank_rank']
	rank_distance_start = data['rank_distance_start']
	rank_distance = data['rank_distance']
	rank_effect_rank = data['rank_effect_rank']
	effect_mod_math = data['effect_mod_math']
	effect_mod = data['effect_mod']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_math = data['check_math']
	check_mod = data['check_mod']
	trait_trait_type = data['trait_trait_type']
	trait_trait = data['trait_trait']
	trait_math = data['trait_math']
	trait_mod = data['trait_mod']
	distance_mod_rank = data['distance_mod_rank']
	distance_mod_math = data['distance_mod_math']
	distance_mod_trait_type = data['distance_mod_trait_type']
	distance_mod_trait = data['distance_mod_trait']
	dc = data['dc']
	dc_value = data['dc_value']
	dc_trait_type = data['dc_trait_type']
	dc_trait = data['dc_trait']

	errors['success'] = error
	errors['error_msgs'] = error_msgs


def resist_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	mod = data['mod']
	rounds = data['rounds']
	circumstance = data['circumstance']
	resist_check_type = data['resist_check_type']
	trait_type = data['trait_type']
	trait = data['trait']
	descriptor = data['descriptor']
	requires_check = data['requires_check']
	check_type = data['check_type']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def resisted_by_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	dc = data['dc']
	mod = data['mod']
	description = data['description']
	trait = data['trait']
	effect = data['effect']
	level = data['level']
	degree = data['degree']
	descriptor = data['descriptor']
	weaken_max = data['weaken_max']
	weaken_restored = data['weaken_restored']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage = data'damage']
	strength = data['strength']
	nullify_descriptor = data['nullify_descriptor']
	nullify_alternate = data['nullify_alternate']
	extra_effort = data['extra_effort']

	errors['success'] = error
	errors['error_msgs'] = error_msgs


def reverse_effect_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	degree = data['degree']
	when = data['when']
	check_check = data['check_check']
	time_check = data['time_check']
	trait_type = data['trait_type']
	trait = data['trait']
	value_type = data['value_type']
	value_dc = data['value_dc']
	math_dc = data['math_dc']
	math = data['math']
	time_value = data['time_value']
	time_unit = data['time_unit']

	errors['success'] = error
	errors['error_msgs'] = error_msgs


def sense_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	target = data['target']
	sense = data['sense']
	subsense = data['subsense']
	sense_cost = data['sense_cost']
	subsense_cost = data['subsense_cost']
	skill = data['skill']
	skill_required = data['skill_required']
	sense_type = data['sense_type']
	height_trait_type = data['height_trait_type']
	height_trait = data['height_trait']
	height_power_required = data['height_power_required']
	height_ensense = data['height_ensense']
	resist_trait_type = data['resist_trait_type']
	resist_trait = data['resist_trait']
	resist_immune = data['resist_immune']
	resist_permanent = data['resist_permanent']
	resist_circ = data['resist_circ']
	objects = data['objects']
	exclusive = data['exclusive']
	gm = data['gm']
	dark = data['dark']
	lighting = data['lighting']
	time = data['time']
	dimensional = data['dimensional']
	radius = data['radius']
	accurate = data['accurate']
	acute = data['acute']
	time_set = data['time_set']
	time_value = data['time_value']
	time_unit = data['time_unit']
	time_skill = data['time_skill']
	time_bonus = data['time_bonus']
	time_factor = data['time_factor']
	distance = data['distance']
	distance_dc = data['distance_dc']
	distance_mod = data['distance_mod']
	distance_value = data['distance_value']
	distance_unit = data['distance_unit']
	distance_factor = data['distance_factor']
	dimensional_type = data['dimensional_type']
	ranks = data['ranks']
	cost = data['cost']

	errors['success'] = error
	errors['error_msgs'] = error_msgs

def time_post_errors(data):

	errors = {}
	error = False
	error_msgs = []

	power_id = data['power_id']
	extra_id = data['extra_id']
	time_type = data['time_type']
	value_type = data['value_type']
	value = data['value']
	units = data['units']
	time_value = data['time_value']
	math = data['math']
	trait_type = data['trait_type']
	trait = data['trait']
	dc = data['dc']
	descriptor = data['descriptor']
	check_type = data['check_type']
	recovery = data['recovery']
	recovery_penalty = data['recovery_penalty']
	recovery_time = data['recovery_time']
	recovery_incurable = data['recovery_incurable']

	errors['success'] = error
	errors['error_msgs'] = error_msgs




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