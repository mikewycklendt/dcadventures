
def alt_check_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	check_type = data['check_type']
	mod = data['mod']
	circumstance = data['circumstance']
	when = data['when']
	trait_type = data['trait_type']
	trait = data['trait']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Check, check_type, 'Check', errors)
	
	errors = int_check(mod, 'Modifier', errors)

	errors = required(mod, 'Modifier', errors)
	errors = required(check_type, 'Check Type', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(when, 'When', errors)
	errors = required(trait_type, 'Trait Type', errors)
	errors = required(trait, 'Trait', errors)


	return (errors)



def circ_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Range, circ_range, 'range', errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)

	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Rounds', errors)
	errors = required(target, 'Targwt', errors)
	errors = required(description, 'Circumstance', errors)

	errors = variable_fields('range', 'Triggered by Range', circ_type, [circ_range], errors)
	errors = variable_field('range', circ_type, 'Range Distance', circ_range, errors) 
	errors = variable_fields('check', 'Triggered by Check Type', circ_type, [check_who, check_trait_type, check_trait], errors)
	errors = variable_field('check', circ_type, 'Whose Check',  check_who, errors)
	errors = variable_field('check', circ_type, 'Trait Type',  check_trait_type, errors)
	errors = variable_field('check', circ_type, 'Trait',  check_trait, errors)

	errors = variable_fields('trait', 'Nullified From Trait', null_type, [null_trait_type, null_trait], errors)
	errors = variable_field('trait', null_type, 'Trait Type', null_trait_type, errors)
	errors = variable_field('trait', null_type, 'Trait', null_trait, errors)
	errors = variable_fields('descriptor', 'Nullified From Descriptor', null_type, [null_descriptor], errors)
	errors = variable_field('descriptor', null_type, 'Descriptor', null_descriptor, errors)
	errors = variable_fields('condition', 'Nullified From Condition', null_type, [null_condition], errors)
	errors = variable_field('condition', null_type, 'Condition', null_condition, errors)

	return (errors)



def dc_table_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Levels, level, 'level', errors)
	
	errors = int_check(value, 'DC Value', errors)
	errors = int_check(math_value, 'Math DC Value', errors)
	errors = int_check(check_mod, 'Check Modifier', errors)

	errors = required(dc, 'DC Type', errors)
	errors = required(description, 'Description', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('value', 'DC Value', dc, [value], errors)
	errors = variable_field('value', dc, 'DC Value', value, errors)
	errors = variable_fields('math', 'DC Math', dc, [math_value, math, math_trait_type, math_trait], errors)
	errors = variable_field('math', dc, 'DC Math Value', math_value, errors)
	errors = variable_field('math', dc, 'DC Math', math, errors)
	errors = variable_field('math', dc, 'DC Math Trait Type', math_trait_type, errors)
	errors = variable_field('math', dc, 'DC Math Trait', math_trait, errors)

	errors = check_fields(descriptor_check, 'Descriptor', [descriptor, descriptor_possess], errors)
	errors = check_field(descriptor_check, 'Descriptor', 'Descriptor', descriptor, errors)
	errors = check_field(descriptor_check, 'Descriptor', 'Descriptor Possession', descriptor_possess, errors)

	errors = check_fields(condition, 'Condition', [condition1, condition2], errors)
	errors = check_field(condition, 'Condition', 'Starting Condition', condition1, errors)
	errors = check_field(condition, 'Condition', 'Ending Condition', condition2, errors)

	errors = check_field(keyword_check, 'Keyword', 'Keyword', keyword, errors)

	errors = check_fields(check_type, 'Check Type', [check_trait_type, check_trait, check_mod], errors)
	errors = check_field(check_type, 'Check Type', 'Trait Type', check_trait_type, errors)
	errors = check_field(check_type, 'Check Type', 'Trait', check_trait, errors)
	errors = check_field(check_type, 'Check Type', 'Check Modifier', check_mod, errors)

	errors = check_field(levels, 'Level', 'Level', level, errors)

	return (errors)




def degree_mod_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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
	consequence_action_type = data['consequence_action_type']
	consequence_action = data['consequence_action']
	consequence_trait_type = data['consequence_trait_type']
	consequence_trait = data['consequence_trait']
	consequence = data['consequence']
	knowledge = data['knowledge']
	knowledge_count = data['knowledge_count']
	knowledge_specificity = data['knowledge_specificity']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, measure_math, 'math', errors)
	errors = id_check(Rank, measure_rank, 'rank', errors)
	errors = id_check(Levels, level, 'level', errors)


	errors = int_check(value, 'Degree', errors)
	errors = int_check(circ_value, 'Circumstance Modifier', errors)
	errors = int_check(circ_turns, 'Circxumstance Turns', errors)
	errors = int_check(measure_val1, 'Measurement Math Value', errors)
	errors = int_check(measure_value, 'Measurement Value', errors)
	errors = int_check(condition_damage_value, 'Condition Damage Value', errors) 
	errors = int_check(condition_damage, 'Condition Damage', errors)
	errors = int_check(nullify, 'Nullify Value', errors)

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
	
	errors = variable_fields('condition', 'Condition', deg_type, [deg_condition_type], errors)
	errors = variable_fields('condition', 'Condition Change', deg_condition_type, [condition1, condition2], errors)
	errors = variable_field('condition', deg_condition_type, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', deg_condition_type, 'Ending Condition', condition2, errors)
	errors = variable_fields('damage', 'Damage Condition', deg_condition_type, [condition_damage_value, condition_damage], errors)
	errors = variable_field('damage', deg_condition_type, 'Condition Damage Value', condition_damage_value, errors)
	errors = variable_field('damage', deg_condition_type, 'Condition Damage Change', condition_damage, errors)
	errors = variable_fields('circ', 'Circumstance', deg_type, [circ_value, circ_turns, circ_trait_type, circ_trait], errors)
	errors = variable_field('circ', deg_type, 'Circumstance Value', circ_value, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Turns', circ_turns, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait Type', circ_trait_type, errors)
	errors = variable_field('circ', deg_type, 'Circumstance Trait',  circ_trait, errors)

	errors = variable_fields('level', 'Level', deg_type, [level], errors)
	
	errors = variable_fields('knowledge' , 'Knowledge', deg_type, [knowledge], errors)
	errors = variable_fields('bonus', 'Learn Bonus', knowledge, [knowledge_count, knowledge_specificity], errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Count', knowledge_count, errors)
	errors = variable_field('bonus', knowledge, 'Knowledge Specificity', knowledge_specificity, errors)

	errors = variable_fields('consequence', 'Consequence', deg_type, [consequence], errors)
	errors = variable_field('consequence', deg_type, 'Consequence', consequence, errors)

	errors = required(keyword, 'Keyword', errors)



	return (errors)

def degree_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	degree_type = data['degree_type']
	degree = data['degree']
	keyword = data['keyword']
	desscription = data['desscription']
	extra_effort = data['extra_effort']
	cumulative = data['cumulative']
	target = data['target']

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(degree, 'Degree', errors)

	errors = required(degree_type, 'Degree Type', errors)
	errors = required(degree, 'Degree', errors)
	errors = required(keyword, 'Keywprd', errors)
	errors = required(desscription, 'Description', errors)
	errors = required(target, 'Target', errors)

	return (errors)



def move_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Math, distance_math, 'math', errors)
	errors = id_check(Sense, concealment_sense, 'sense', errors)
	errors = id_check(Ground, ground_type, 'ground', errors)
	errors = id_check(Unit, ground_units, 'unit', errors)
	errors = id_check(Check, objects_check, 'check', errors)
	errors = id_check(ConflictAction, objects_attack, 'action', errors)
	print(mod)
	errors = int_check(rank, 'Speed Rank', errors)
	errors = int_check(mod, 'Speed Rank Modifier', errors)
	errors = int_check(distance_value, 'Distance Value', errors)
	errors = int_check(distance_math_value, 'First Distance Math Value', errors)
	errors = int_check(distance_math_value2, 'Second Distance Math Value', errors)
	errors = int_check(distance_mod, 'Distance Modifier', errors)
	errors = int_check(dc, 'DC Value', errors)
	errors = int_check(mass_value, 'Mass Value', errors)
	errors = int_check(extended_actions, 'Move Actions', errors)
	errors = int_check(permeate_speed, 'Permeate Speed', errors)
	errors = int_check(dimension_mass_rank, 'Dimensional Carry Mass Rank', errors)
	errors = int_check(special_time_carry, 'Time Travel Carry Mass Rank', errors)
	errors = int_check(ground_time, 'Through Ground Time Value', errors)
	errors = int_check(subtle_mod, 'Subtle Modifier', errors)
	errors = int_check(ranks, 'Ranks', errors)
	errors = int_check(cost, 'Cost', errors)

	errors = required(rank, 'Speed Rank' , errors)
	errors = required(math, 'Speed Rank Math', errors)
	errors = required(mod, 'Speed Rank Modifier', errors)
	errors = check_fields(aquatic, 'Aquatic', [acquatic_type], errors)
	errors = check_field(aquatic, 'Aquatic Type','Aquatic', acquatic_type, errors)

	errors = check_fields(flight, 'Flight', [flight_conditions], errors)
	errors = check_field(flight, 'Flight Conditions', 'Flight', flight_conditions, errors)
	
	errors = check_fields(ground, 'Through Ground', [ground_type, ground_permanence], errors)
	errors = check_field(ground, 'Through Ground', 'Through Ground Type', ground_type, errors)
	errors = check_field(ground, 'Through Ground', 'Ground Permanance', ground_permanence, errors)

	errors = variable_fields('temp', 'Temporary Ground Permanace', ground_permanence, [ground_time, ground_units], errors)
	errors = variable_field('temp', ground_permanence, 'Time', ground_time, errors)
	errors = variable_field('temp', ground_permanence, 'Units', ground_units, errors)

	errors = required(direction, 'Direction', errors)

	errors = required(distance_type, 'Distance', errors)
	errors = variable_field('value', distance_type, 'Distance Rank', distance_value, errors)
	errors = variable_fields('math', 'Distance Math', distance_type, [distance_math_value, distance_math, distance_math_value2], errors)
	print
	errors = variable_field('math', distance_type, 'First Distance Math Value', distance_math_value, errors)
	errors = variable_field('math', distance_type, 'Distance Math', distance_math, errors)
	errors = variable_field('math', distance_type, 'Second Distance Math Value', distance_math_value2, errors)
	errors = variable_fields('mod', 'Distance Modifier', distance_type, [distance_mod], errors)
	errors = variable_field('mod', distance_type, 'Distance Modifier', distance_mod, errors)

	errors = check_fields(subtle, 'Subtle', [subtle_trait_type, subtle_trait, subtle_mod], errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Trait Type', subtle_trait_type, errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Trait', subtle_trait, errors)
	errors = check_field(subtle, 'Subtle', 'Subtle Modifier', subtle_mod, errors)

	errors = check_fields(objects, 'Move Objects', [objects_check, objects_direction], errors)
	errors = variable_fields('1', 'Move Objects Skill Check', objects_check, [objects_skill_type, objects_skill], errors)
	errors = variable_field('1', objects_check, 'Move Objects Skill Tyoe', objects_skill_type, errors)
	errors = variable_field('1', objects_check, 'Move Objects Skill', objects_skill, errors)
	errors = variable_fields('5', 'Move Objects Attack Check', objects_check, [objects_attack], errors)
	errors = variable_field('5', objects_check, 'Move Objects Attack Check Type', objects_attack, errors)
	errors = check_fields(objects_damage, 'Move Objects Damage Inflict', [damage_type], errors)
	errors = check_field(objects_damage, 'Move Objects Damage Inflict', 'Damage Dealt By', damage_type, errors)

	errors = check_fields(permeate, 'Permeate', [permeate_type, permeate_speed], errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Type', permeate_type, errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Speed Rank Modifier', permeate_speed, errors)

	errors = check_fields(special, 'Special Travel', [special_type], errors)
	errors = variable_fields('dimension', 'Dimension Travel', special_type, [dimension_type, dimension_mass_rank], errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Type', dimension_type, errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Carry Mass', dimension_mass_rank, errors)
	errors = variable_fields('descriptor', 'Dimension Descriptor', dimension_type, [dimension_descriptor], errors)
	errors = variable_fields('space', 'Space Travel', special_type, [special_space], errors)
	errors = variable_field('space', special_type, 'Space Travel Type', special_space, errors) 
	errors = variable_fields('time', 'Time Travel', special_type, [special_time, special_time_carry], errors)
	errors = variable_field('time', special_type, 'Time Travel Type', special_time, errors)
	errors = variable_field('time', special_type, 'Time Travel Carry Mass', special_time_carry, errors)
	errors = variable_fields('teleport', 'Teleport', special_type, [teleport_type], errors)
	errors = variable_field('teleport',  special_type, 'Teleport Type', teleport_type, errors)

	errors = check_of_multiple(check_type, 'Check Type', [[check_trait_type, check_trait], [check_free]], 'You mest eitherr set a trait type and trait or specify that this is a free check', errors)

	errors = check_fields(concealment, 'Concealment', [concealment_sense, concealment_trait, concealment_trait_type], errors)
	errors = check_field(concealment, 'Concealment', 'Concealed from Sense', concealment_sense, errors)
	errors = check_field(concealment, 'Concealment', 'Concealment Detection Trait Type', concealment_trait_type, errors)
	errors = check_field(concealment, 'Concealment', 'Concealment Detection Trait', concealment_trait, errors)

	errors = check_fields(extended, 'Extended', [extended_actions], errors)
	errors = check_field(extended, 'Extended', 'Extended Actions', extended_actions, errors)

	errors = check_fields(mass, 'Increased Mass', [mass_value], errors)
	errors = check_field(mass, 'Increased Mass', 'Increased Mass Amount', mass_value, errors)

	return (errors)

def opposed_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Check, player_check, 'check', errors)
	errors = id_check(Check, opponent_check, 'check', errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(opponent_mod, 'Opponent Modifier', errors)

	errors = required(trait_type, 'Trait Type', errors)
	errors = required(trait, 'Trait', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(opponent_trait_type, 'Opponent Trait Type', errors)
	errors = required(opponent_trait, 'Opponent Trait', errors)
	errors = required(opponent_mod, 'Opponent Modifier', errors)
	errors = required(player_check, 'Check Type', errors)
	errors = required(opponent_check, 'Opponent Check Type', errors)

	return (errors)


def time_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = power_check(power_id, errors)

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Unit, units, 'unit', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Check, check_type, 'check', errors)
	
	errors = int_check(value, 'Time Value', errors)
	errors = int_check(time_value, 'Math Time Value', errors)
	errors = int_check(dc, 'DC', errors)
	errors = int_check(recovery_penalty, 'Recovery Penalty', errors)
	errors = int_check(recovery_time, 'Recovery Time', errors)

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

	return (errors)

