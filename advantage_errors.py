
def adv_alt_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	check_type = data['check_type']
	mod = data['mod']
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

	return(errors)

def adv_benefit_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	name = data['name']
	description = data['description']
	effort = data['effort']


	return(errors)

def adv_circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}


	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	mod = data['mod']
	rounds = data['rounds']
	ranks = data['ranks']
	circumstance = data['circumstance']
	circ_type = data['circ_type']
	circ_range = data['circ_range']
	conflict = data['conflict']
	check_who = data['check_who']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	null_type = data['null_type']
	null_condition = data['null_condition']
	null_trait_type = data['null_trait_type']
	null_trait = data['null_trait']


	return(errors)

def adv_combined_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	ranks = data['ranks']
	advantage = data['advantage']


	return(errors)


def adv_condition_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	benefit = data['benefit']
	condition_type = data['condition_type']
	condition = data['condition']
	condition_null = data['condition_null']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage_value = data['damage_value']
	damage = data['damage']



	return(errors)

def adv_dc_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	dc = data['dc']
	description = data['description']
	value_value = data['value_value']
	math_value = data['math_value']
	math_math = data['math_math']
	math_trait_type = data['math_trait_type']
	math_trait = data['math_trait']
	condition = data['condition']
	keyword_check = data['keyword_check']
	check_type = data['check_type']
	levels = data['levels']
	level_type = data['level_type']
	level = data['level']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	check_trait_type = data['check_trait_type']
	check_trait = data['check_trait']
	check_mod = data['check_mod']


	return(errors)

def adv_deg_mod_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	target = data['target']
	benefit = data['benefit']
	value = data['value']
	deg_mod_type = data['deg_mod_type']
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
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	keyword = data['keyword']
	nullify = data['nullify']
	cumulative = data['cumulative']
	linked = data['linked']


	return(errors)

def adv_effort_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	effect = data['effect']
	condition_type = data['condition_type']
	condition_damage_value = data['condition_damage_value']
	condition_damage = data['condition_damage']
	condition1 = data['condition1']
	condition2 = data['condition2']
	benefit_choice = data['benefit_choice']
	benefit_turns = data['benefit_turns']
	benefit_count = data['benefit_count']
	benefit_effort = data['benefit_effort']


	return(errors)

def adv_minion_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	points = data['points']
	condition = data['condition']
	player_condition = data['player_condition']
	link = data['link']
	variable_type = data['variable_type']
	multiple = data['multiple']
	attitude = data['attitude']
	resitable = data['resitable']
	heroic = data['heroic']
	sacrifice = data['sacrifice']
	sacrifice_cost = data['sacrifice_cost']
	attitude_type = data['attitude_type']
	attitude_attitude = data['attitude_attitude']
	attitude_trait_type = data['attitude_trait_type']
	attitude_trait = data['attitude_trait']
	resitable_check = data['resitable_check']
	resitable_dc = data['resitable_dc']
	multiple_value = data['multiple_value']
	horde = data['horde']
	columns = data['columns']
	created = data['created']
	font = data['font']


	return(errors)

def adv_modifiers_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	Benefit = data['benefit']
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


	return(errors)

def adv_opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	opponent_trait_type = data['opponent_trait_type']
	opponent_trait = data['opponent_trait']
	opponent_mod = data['opponent_mod']
	player_check = data['player_check']
	opponent_check = data['opponent_check']
	multiple = data['multiple']


	return(errors)

def adv_points_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	spend = data['spend']
	condition_cost = data['condition_cost']
	condition1 = data['conditioon1']
	condition2 = data['condition2']
	equipment_points = data['equipment_points']
	equipment_vehicles = data['equipment_vehicles']
	equipment_headquarters = data['equipment_headquarters']
	initiative_cost = data['initiative_cost']
	twenty = data['twenty']
	check_bonus = data['check_bonus']
	check_cost = data['check_cost']
	check_turns = data['check_turns']
	check_target = data['check_target']
	check_all = data['check_all']
	benefit_choice = data['benefit_choice']
	benefit_count = data['benefit_count']
	benefit_cost = data['benefit_cost']
	benefit_turns = data['benefit_turns']
	ranks_gained = data['ranks_gained']
	ranks_max = data['ranks_max']
	ranks_lasts = data['ranks_lasts']
	ranks_trait_type = data['ranks_trait_type']
	ranks_trait = data['ranks_trait']


	return(errors)

def adv_resist_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	which = data['which']


	return(errors)

def adv_rounds_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	rounds = data['rounds']
	cost = data['cost']
	check = data['check']
	trait_type = data['trait_type']
	trait = data['trait']
	end = data['end']


	return(errors)

def adv_skill_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	trait_type = data['trait_type']
	trait = data['trait']
	replaced_trait_type = data['replaced_trait_type']
	replaced_trait = data['replaced_trait']
	multiple = data['multiple']


	return(errors)

def adv_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']
	time_type = data['time_type']
	value_type = data['value_type']
	value = data['value']
	units = data['units']
	time_value = data['time_value']
	math = data['math']
	trait_type = data['trait_type']
	trait = data['trait']
	dc = data['dc']
	check_type = data['check_type']
	recovery = data['recovery']
	recovery_penalty = data['recovery_penalty']
	recovery_time = data['recovery_time']
	recovery_incurable = data['recovery_incurable']


	return(errors)

def adv_variable_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	trait_type = data['trait_type']
	trait = data['trait']


	return(errors)