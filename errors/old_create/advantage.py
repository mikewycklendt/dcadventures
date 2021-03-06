
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(action, 'Action', errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Check, check_type, 'Check Type', errors)
	errors = db_check(ConflictAction, conflict, 'Conflict Action', errors)
	errors = db_check(Ranged, conflict_range, 'Range', errors)

	check_trigger = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]


	errors = required(check_type, 'Check Type', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(when, 'When', errors)
	errors = required(action_type, 'Action Type', errors)
	errors = required(action, 'Action', errors)

	errors = variable_fields('condition', 'Triggered by Condition', trigger, [condition1, condition2], errors)
	errors = variable_field('condition', trigger, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', trigger, 'Ending Condition', condition2, errors)
	
	errors = variable_fields('conflict', 'Triggered by Conflict Action', trigger, [conflict], errors)
	errors = variable_field('conflict', trigger, 'Conflict Action', conflict, errors)

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
	null_override_trait_type = data['null_override_trait_type']
	null_override_trait = data['null_override_trait']
	
	errors = create_check('Advantage', advantage_id, Advantage, errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Range, circ_range, 'Range', errors)
	errors = db_check(ConflictAction, conflict, 'Conflict Action', errors)
	
	errors = required(target, 'Target', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Lasts', errors)
	errors = required(circumstance, 'Circumstance', errors)
	
	errors = variable_fields('range', 'Triggered by Range', circ_type, [circ_range], errors)
	errors = variable_field('range', circ_type, 'Range', circ_range, errors)
	errors = variable_fields('check', 'Triggered by Check Type', circ_type, [check_who, check_trait_type, check_trait], errors)
	errors = variable_field('check', circ_type, 'Whose Check', check_who, errors)
	errors = variable_field('check', circ_type, 'Trait Type', check_trait_type, errors)
	errors = variable_field('check', circ_type, 'Trait', check_trait, errors)
	errors = variable_fields('conflict', 'Triggered by Conflict Action', circ_type, [conflict], errors)
	errors = variable_field('conflict', circ_type, 'Conflict Action', conflict, errors)

	errors = variable_fields('trait', 'Nullified by Trait', null_type, [null_trait_type, null_trait], errors)
	errors = variable_field('trait', null_type, 'Trait Type', null_trait_type, errors)
	errors = variable_field('trait', null_type, 'Trait', null_trait, errors)
	errors = variable_fields('condition', 'Nullified by Condition', null_type, [null_condition], errors)
	errors = variable_field('condition', null_type, 'Condition', null_condition, errors)
	errors = variable_fields('override', 'Override Trait Circumstance', null_type, [null_override_trait_type, null_override_trait], errors)
	errors = variable_field('override', null_type, 'Trait Type', null_override_trait_type, errors)
	errors = variable_field('override', null_type, 'Trait', null_override_trait, errors)

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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value_value, 'DC', errors)
	errors = int_check(math_value, 'Math Value', errors)
	errors = int_check(check_mod, 'Check Modifier', errors)
	
	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Math, math_math, 'Math', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)

	errors = required(dc, 'DC Type', errors)
	errors = required(description, 'Description', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('value', 'DC Value', dc, [value_value], errors)
	errors = variable_field('value', dc, 'DC Value', value_value, errors)
	errors = variable_fields('math', 'DC Math', dc, [math_value, math_math, math_trait_type, math_trait], errors)
	errors = variable_field('math', dc, 'DC Math Value', math_value, errors)
	errors = variable_field('math', dc, 'DC Math', math_math, errors)
	errors = variable_field('math', dc, 'DC Math Trait Type', math_trait_type, errors)
	errors = variable_field('math', dc, 'DC Math Trait', math_trait, errors)

	errors = check_fields(condition, 'Condition', [condition1, condition2], errors)
	errors = check_field(condition, 'Condition', 'Starting Condition', condition1, errors)
	errors = check_field(condition, 'Condition', 'Ending Condition', condition2, errors)

	errors = check_field(keyword_check, 'Keyword', 'Keyword', keyword, errors)

	errors = check_fields(check_type, 'Check Type', [check_trait_type, check_trait, check_mod], errors)
	errors = check_field(check_type, 'Check Type', 'Trait Type', check_trait_type, errors)
	errors = check_field(check_type, 'Check Type', 'Trait', check_trait, errors)
	errors = check_field(check_type, 'Check Type', 'Check Modifier', check_mod, errors)

	errors = check_field(levels, 'Level', 'Level', level, errors)


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
	deg_type = data['deg_mod_type']
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value, 'Circumstance Modifier', errors)
	errors = int_check(consequence_action, 'Consequence Action', errors)
	errors = int_check(knowledge_count, 'Knowledge Amount', errors)
	errors = int_check(circ_value, 'Circumstance Value', errors)
	errors = int_check(circ_turns, 'Turns', errors)
	errors = int_check(measure_val1, 'Neasurement Rank', errors)
	errors = int_check(measure_value, 'Measurement Value', errors)
	errors = int_check(condition_damage_value, 'Condition Damage Value', errors)
	errors = int_check(condition_damage, 'Condition Direction', errors)
	errors = int_check(nullify, 'Nullify DC', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Consequence, consequence, 'Consequence', errors)
	errors = db_check(LevelType, level_type, 'Level Type', errors)
	errors = db_check(Levels, level, 'Level', errors)
	errors = db_check(Math, measure_math, 'Math', errors)
	errors = db_check(Rank, measure_rank, 'Measurement Rank', errors)

	errors = required(value, 'Degree', errors)
	errors = required(deg_type, 'Result Type', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('measure', 'Measurement', deg_type, [measure_type], errors)
	errors = variable_fields('math', 'Measurement Math', measure_type, [measure_val1, measure_math, measure_trait_type, measure_trait], errors)
	errors = variable_field('math', measure_type, 'Measurement Math Value', measure_val1, errors)
	errors = variable_field('math', measure_type, 'Measurement Math', measure_math, errors)
	errors = variable_field('math', measure_type, 'Measurement Trait Type', measure_trait_type, errors)
	errors = variable_field('math', measure_type, 'Measurement Trait', measure_trait, errors)

	errors = variable_fields('value', 'Measurement Value', measure_type, [measure_value, measure_rank], errors)
	errors = variable_field('value', measure_type, 'Measurement Value', measure_value, errors)
	errors = variable_field('value', measure_type, 'Measurement Rank Type', measure_rank, errors)
	
	errors = variable_fields('condition', 'Condition', deg_type, [condition_type], errors)
	errors = variable_fields('condition', 'Condition Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', condition_type, 'Ending Condition', condition2, errors)
	errors = variable_fields('damage', 'Damage Condition',condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Value', condition_damage_value, errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Change', condition_damage, errors)
	errors = variable_fields('circ', 'Circumstance', deg_type, [circ_value, circ_turns, circ_trait_type, circ_trait], errors)
	errors = variable_field('circ', deg_type, 'Circumstance Value', circ_value, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Turns', circ_turns, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait Type', circ_trait_type, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait',  circ_trait, errors)

	errors = variable_fields('level', 'Level', deg_type, [level_type, level], errors)
	
	errors = variable_fields('knowledge' , 'Knowledge', deg_type, [knowledge], errors)
	errors = variable_fields('bonus', 'Learn Bonus', knowledge, [knowledge_count, knowledge_specificity], errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Count', knowledge_count, errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Specificity', knowledge_specificity, errors)

	errors = variable_fields('consequence', 'Consequence', deg_type, [consequence], errors)
	errors = variable_field('consequence', deg_type, 'Consequence', consequence, errors)


	errors = variable_fields('level', 'Level', deg_type, [level], errors)

	errors = required(keyword, 'Keyword', errors)


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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Check, player_check, 'Player Check', errors)
	errors = db_check(Check, opponent_check, 'Opponent Check', errors)

	errors =  required(trait_type, 'Trait Type', errors)
	errors =  required(trait, 'Trait', errors)
	errors =  required(mod, 'Modifier', errors)
	errors =  required(opponent_trait_type, 'Opponent Trqait Type', errors)
	errors =  required(opponent_trait, 'Opponent Trait', errors)
	errors =  required(opponent_mod, 'Opponent Modifier', errors)
	errors =  required(player_check, 'Player Check', errors)
	errors =  required(opponent_check, 'Opponent Check', errors)

	return(errors)



def adv_time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	advantage_id = data['advantage_id']
	benefit = data['benefit']
	columns = data['columns']
	created = data['created']
	font = data['font']
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

	errors = create_check('Advantage', advantage_id, Advantage, errors)
	
	errors = int_check(value, 'Time Value', errors)
	errors = int_check(time_value, 'Time Math Value', errors)
	errors = int_check(dc, 'DC', errors)
	errors = int_check(recovery_penalty, 'Recovery Penalty', errors)	
	errors = int_check(recovery_time, 'Recovery Time', errors)

	errors = db_check(Advantage, advantage_id, 'Advantage', errors)
	errors = db_check(Benefit, benefit, 'Benefit', errors)
	errors = db_check(Unit, units, 'Units', errors)
	errors = db_check(Math, math, 'Math', errors)
	errors = db_check(Check, check_type, 'Check Type', errors)

	errors = required(time_type, 'Time Type', errors)
	errors = required(value_type, 'Time Value Type', errors)

	errors = variable_fields('value', 'Time Value', value_type, [value, units], errors)
	errors = variable_field('value', value_type,'Time Value', value, errors)
	errors = variable_field('value', value_type,'Time Units' , units, errors)
	errors = variable_fields('math', 'Time Math', value_type, [time_value, math, trait_type, trait], errors)
	errors = variable_field('math', value_type, 'Time Valuea', time_value, errors)
	errors = variable_field('math', value_type, 'Time Math', math, errors)
	errors = variable_field('math', value_type, 'Trait Type', trait_type, errors)
	errors = variable_field('math', value_type, 'Trait', trait, errors)

	errors = check_fields(recovery, 'Recovery', [recovery_penalty, recovery_time], errors)
	errors = check_field(recovery, 'Recovery', 'Recovery Penalty', recovery_penalty, errors)
	errors = check_field(recovery, 'Recovery', 'Recovery Time', recovery_time, errors)


	return(errors)




