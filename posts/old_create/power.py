
	
def alt_check_post(entry, body, cells):
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	check_type = entry.check_type
	mod = entry.mod
	circumstance = entry.circumstance
	when = entry.when
	trait_type = entry.trait_type
	trait = entry.trait
	
	trait = trait_select(trait, trait_type)

	extra = extra_name(extra_id)
	check_type = name(Check, check_type)

	check_types = [{'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_types)

	mod = integer_convert(mod)

	cells = cell('Extra', 15, [extra])
	cells = cell('Check', 14, [check_type], cells)
	cells = cell('Mod', 8, [mod], cells)
	cells = cell('Trait', 17, [trait], cells)
	cells = cell('When', 12, [when], cells)
	cells = cell('Circumstabce', 35, [circumstance], cells)
	
	body = send(cells, body)
	
	cells.clear()

	return (body)




def circ_post(entry, body, cells):
		
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
	
	check_trait = trait_select(check_trait, check_trait_type)
	null_trait = trait_select(null_trait, null_trait_type)

	extra = extra_name(extra_id)
	circ_range = get_name(Ranged, circ_range)
	null_condition = get_name(Condition, null_condition)
	null_descriptor = descriptor_name(null_descriptor)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)


	who_check_select = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]
	check_who = selects(check_who, who_check_select)

	
	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	circ_range = integer_convert(circ_range)


	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 12, [target], cells)
	cells = cell('Modifier', 9, [mod], cells)
	cells = cell('Lasts', 8, [rounds], cells)

	circrange = string('Range', [circ_range])
	vcells = vcell('range', 20, [circ_range, circrange])
	vcells = vcell('check', 25, [check_who, check_trait], vcells)
	cells = vcell_add('Trigger', circ_type, vcells, cells)

	vcells = vcell('trait', 17, [null_trait])
	vcells = vcell('descriptor', 19, [null_descriptor], vcells)
	vcells = vcell('condition', 17, [null_condition], vcells)	
	cells = vcell_add('Nullified', null_type, vcells, cells)

	cells = cell('Circumstance', 35, [description], cells)

	body = send(cells, body)


	cells.clear()

	return (body)



def dc_table_post(entry, body, cells):
		
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
	level = entry.level
	levels = entry.levels

	math_trait = trait_select(math_trait, math_trait_type)
	check_trait = trait_select(check_trait, check_trait_type)

	extra = extra_name(extra_id)
	math = math_convert(Math, math)
	descriptor = descriptor_name(descriptor)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	level = get_name(Levels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	
	possess_select = [{'type': '', 'name': 'Possession'}, {'type': 'possess', 'name': 'While Possessing'}, {'type': 'oppose', 'name': 'While Opposing'}]
	descriptor_possess = selects(descriptor_possess, possess_select)

	value = integer_convert(value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 14, [target], cells)
	vcells = vcell('value', 7, [value])
	vcells = vcell('math', 15, [math_value, math, math_trait], vcells)
	cells = vcell_add('DC', dc, vcells, cells)

	cells = check_cell('Descriptor', 14, descriptor_check, cells, True)
	new_mod = mod_create('Descriptor DC', 16)
	new_mod = mod_cell('Descriptor', 12, [descriptor], new_mod)
	new_mod = mod_cell('Possession', 12, [descriptor_possess], new_mod)	
	body = mod_add(descriptor_check, new_mod, body)

	cells = check_cell('Condition', 13, condition, cells, True)
	new_mod = mod_create('Condition', 12)
	word = string('to', [condition1, condition2])
	new_mod = mod_cell('Conditions', 14, [condition1, word, condition2], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Keyword', 10, keyword_check, cells, True)
	new_mod = mod_create('Keyword', 10)
	new_mod = mod_cell('Key:', 7, [keyword], new_mod)
	body = mod_add(keyword_check, new_mod, body)

	cells = check_cell('Check', 7, check_type, cells, True)
	new_mod = mod_create('Check Type', 15)
	new_mod = mod_cell('Trait:', 7, [check_trait], new_mod)
	new_mod = mod_cell('Modifier:', 12, [check_mod], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Level', 7, levels, cells, True)
	new_mod = mod_create('Level', 8)
	new_mod = mod_cell('Level:', 7, [level], new_mod)
	body = mod_add(levels, new_mod, body)

	cells = cell('Description', 40, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)



def degree_mod_post(entry, body, cells):

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
	consequence_action_type = entry.consequence_action_type
	consequence_action = entry.consequence_action
	consequence_trait_type = entry.consequence_trait_type
	consequence_trait = entry.consequence_trait
	consequence = entry.consequence
	knowledge = entry.knowledge
	knowledge_count = entry.knowledge_count
	knowledge_specificity = entry.knowledge_specificity

	circ_trait = trait_select(circ_trait, circ_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)
	consequence_trait = trait_select(consequence_trait, consequence_trait_type)

	measure_rank = get_name(Rank, measure_rank)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	level = get_name(Levels, level)
	consequence = get_name(Consequence, consequence)
	extra = extra_name(extra_id)
	measure_math = math_convert(Math, measure_math)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	deg_mod_type_select = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'uncontrolled', 'name': 'Effect Uncontrolled'}, {'type': 'level', 'name': 'Level'}]

	value_type_select = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]

	condition_type_select = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]

	updown_select = [{'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown_select)

	specificity_select = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	knowledge_specificity = selects(knowledge_specificity, specificity_select)

	condition_select = [{'type': 'current', 'name': 'Current'}, {'type': 'any', 'name': 'Any'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, condition_select)
	condition2 = selects(condition2, condition_select)

	value = integer_convert(value)
	circ_value = integer_convert(circ_value)
	circ_turns = integer_convert(circ_turns)
	measure_val1 = integer_convert(measure_val1)
	measure_value = integer_convert(measure_value)
	measure_rank = integer_convert(measure_rank)
	condition_damage_value = integer_convert(condition_damage_value)
	condition_damage = integer_convert(condition_damage)
	nullify = integer_convert(nullify)

	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 14, [target], cells)
	cells = cell('Degree', 7, [value], cells)
	cells = cell('Keyword', 14, [keyword], cells)
	cells = cell('Nullify DC', 10, [value], cells)
	cells = check_cell('Cumulative', 12, cumulative, cells)
	cells = check_cell('Linked', 7, linked, cells)
	word = string('for', [circ_trait, circ_value, circ_turns])
	word2 = string('Turns', [circ_trait, circ_value, circ_turns])
	vcells = vcell('circ', 24, [circ_trait, circ_value, word, circ_turns, word2]) 
	vcells = vcell('uncontrolled', 12, ['Uncontrolled'], vcells)
	vcells = vcell('level', 10, [level], vcells)
	vcells = vcell('measure', 17, [measure_value, measure_rank], vcells, 'value', measure_type)
	vcells = vcell('measure', 18, [measure_val1, measure_math, measure_trait], vcells, 'math', measure_type)
	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 25, [condition1, word, condition2], vcells, 'condition', deg_condition_type)
	word = string('Conditions', [condition_damage_value, condition_damage])
	vcells = vcell('condition', 17, [condition_damage_value, word, condition_damage], vcells, 'damage', deg_condition_type)
	vcells = vcell('knowledge', 28, [knowledge_count, knowledge_specificity, 'Bonuses'], vcells, 'bonus', knowledge)
	vcells = vcell('knowledge', 25, ['Gain Knowledge but GM may lie'], vcells, 'lie', knowledge)
	vcells = vcell('consequence', 33, [consequence, 'for', consequence_trait, consequence_action], vcells)
	
	vcell_add('Effect', deg_type, vcells, cells)
	
	body = send(cells, body)

	cells.clear()

	return (body)



def degree_post(entry, body, cells):

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

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	degree = integer_convert(degree)

	
	cells = cell('Extra', 15, [extra])



	body = send(cells, body)

	cells.clear()

	return (body)


	
def move_post(entry, body, cells):

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
	materials = entry.materials
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

	concealment_trait = trait_select(concealment_trait, concealment_trait_type)
	subtle_trait = trait_select(subtle_trait, subtle_trait_type)
	objects_skill = trait_select(objects_skill, objects_skill_type)
	check_trait = trait_select(check_trait, check_trait_type)

	condition = get_name(Condition, condition)
	concealment_sense = get_name(Sense, concealment_sense)
	ground_type = get_name(Ground, ground_type)
	ground_units = get_name(Unit, ground_units)
	objects_check = get_name(Check, objects_check)
	objects_attack = get_name(ConflictAction, objects_attack)
	damage_type = get_name(Ability, damage_type)
	extra = extra_name(extra_id)
	math = math_convert(Math, math)
	distance_math = math_convert(Math, distance_math)

	dimension_descriptor = descriptor_name(dimension_descriptor)

	directions_select = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]
	direction = selects(direction, directions_select)

	aquatic_select = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}]
	acquatic_type = selects(acquatic_type, aquatic_select)

	openings_select = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]
	permeate_type = selects(permeate_type, openings_select)

	travel_select = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]

	teleport_change_select = [{'type': '', 'name': 'Can Change'}, {'type': 'direction', 'name': 'Direction'}, {'type': 'velocity', 'name': 'Velocity'}]
	teleport_change = selects(teleport_change, teleport_change_select)

	teleport_select = [{'type': '', 'name': 'Type'}, {'type': 'know', 'name': 'Know Destination'}, {'type': 'any', 'name': 'Any Destination'}]
	teleport_type = selects(teleport_type, teleport_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimension_type = selects(dimension_type, dimensions_select)

	space_select = [{'type': '', 'name': 'Space Travel Type'}, {'type': 'solar', 'name': 'Planets in Solar System'}, {'type': 'star', 'name': 'Other Star Systems'}, {'type': 'galaxy', 'name': 'Other Galaxies'}]
	special_space = selects(special_space, space_select)

	time_travel_select = [{'type': '', 'name': 'Time Travel Type'}, {'type': 'Fixed', 'name': 'Fixed Point in Time'}, {'type': 'past', 'name': 'Any Point in Past'}, {'type': 'future', 'name': 'Any Point in Future'}, {'type': 'timeline', 'name': 'Alternate Timeline'}, {'type': 'any', 'name': 'Any Point in time'}  ]
	special_time = selects(special_time, time_travel_select)

	permanence_select = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	ground_permanence = selects(ground_permanence, permanence_select)

	flight_conditions = select_multiple(flight_conditions)

	move_objects_select = [{'type': '', 'name': 'Direction'}, {'type': 'all', 'name': 'All Directions'}, {'type': 'vertical', 'name': 'Up and Down'}, {'type': 'horizontal', 'name': 'Towards and Away'}, {'type': 'attract', 'name': 'Attraction'}, {'type': 'repel', 'name': 'Repulsion'}]
	objects_direction = selects(objects_direction, move_objects_select)

	rank = integer_convert(rank)
	mod = integer_convert(mod)
	distance_value = integer_convert(distance_value)
	distance_math_value = integer_convert(distance_math_value)
	distance_math_value2 = integer_convert(distance_math_value2)
	distance_mod = integer_convert(distance_mod)
	dc = integer_convert(dc)
	mass_value = integer_convert(mass_value)
	extended_actions = integer_convert(extended_actions)
	permeate_speed = integer_convert(permeate_speed)
	dimension_mass_rank = integer_convert(dimension_mass_rank)
	special_time_carry = integer_convert(special_time_carry)
	ground_time = integer_convert(ground_time)
	subtle_mod = integer_convert(subtle_mod)
	ranks = integer_convert(ranks)
	cost = integer_convert(cost)
	
	
	cells = cell('Extra', 15, [extra])
	per = check_convert('Per Rank', per_rank)
	cells = cell('Speed', 18, [rank, math, mod, per], cells)
	cells = cell('Condition', 12, [condition], cells)
	cells = cell('Direction', 13, [direction], cells)
	
	vcells = vcell('unlimited', 12, ['Unlimited'])
	vcells = vcell('value', 12, [distance_value], vcells)
	vcells = vcell('math', 20, [distance_math_value, distance_math, distance_math_value2], vcells)
	vcells = vcell('mod', 20, ['Effect Rank', '-', distance_mod], vcells)
	cells = vcell_add('Distance', distance_type, vcells, cells)

	cells = cell('DC', 7, dc, cells)

	print('\n\n\n\n')
	print(ground_time)
	print('\n\n\n')
	

	cells = check_cell('Flight', 10, flight, cells, True)
	new_mod = mod_create('Flight', 10)
	new_mod = mod_cell('Conditions:', 10, [flight_conditions], new_mod)
	new_mod = mod_cell('Perception Check:', 15, [flight_resist], new_mod)
	new_mod = mod_cell('Requires Equipment:', 20, [flight_equip], new_mod)
	body = mod_add(flight, new_mod, body)

	cells = check_cell('Aquatic', 10, aquatic, cells, True)
	new_mod = mod_create('Aquatic', 10)
	new_mod = mod_cell('Type:', 7, [acquatic_type], new_mod)
	body = mod_add(aquatic, new_mod, body)

	cells = check_cell('Ground', 10, ground, cells, True)
	new_mod = mod_create('Through Ground', 17)
	new_mod = mod_cell('Type:', 7, [ground_type], new_mod)
	new_mod = mod_cell('Permanance:', 10, [ground_permanence], new_mod)
	new_mod = mod_cell('Lasts:', 5, [ground_time, ground_units], new_mod)
	new_mod = mod_cell('Ranged', 7, [ground_ranged], new_mod)
	body = mod_add(ground, new_mod, body)

	cells = check_cell('Affects Others', 18, others, cells)
	cells = check_cell('Continuous', 13, continuous, cells)
	
	cells = check_cell('Subtle', 8, subtle, cells, True)
	new_mod = mod_create('Subtle', 10)
	new_mod = mod_cell('Bonus Against:', 15, [subtle_trait], new_mod)
	new_mod = mod_cell('Bonus:', 8, [subtle_mod], new_mod)
	body = mod_add(subtle, new_mod, body)

	cells = check_cell('Concentration', 15, concentration, cells)
	cells = check_cell('Through Obstacles', 20, obstacles, cells)

	cells = check_cell('Move Objects', 18, objects, cells, True)
	select = [{'type': 1, 'name': 'Skill Check', 'w': 10}, {'type': 2, 'name': 'Opposed Check', 'w': 15}, {'type': 3, 'name': 'Routine Check', 'w': 15}, {'type': 4, 'name': 'Team Check', 'w': 15}, {'type': 5, 'name': 'Attack Check', 'w': 15}, {'type': 6, 'name': 'Resistance Check', 'w': 15}, {'type': 7, 'name': 'Comparison Check', 'w': 15}]
	new_mod = mod_create('Move Objects', 17, objects_check, select)
	value = 1
	new_mod = mod_cell('Skill:', 7, [objects_skill], new_mod, value)
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 2
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 3
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 4
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 5
	new_mod = mod_cell('Check Type:', 12, [objects_attack], new_mod, value)
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 6
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 7
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	body = mod_add(objects, new_mod, body)

	cells = check_cell('Permeate', 10, permeate, cells, True)
	new_mod = mod_create('Permeate', 12)
	new_mod = mod_cell('Type:', 8, [permeate_type], new_mod)
	new_mod = mod_cell('Speed Modifier:', 18, [permeate_speed], new_mod)
	new_mod = mod_cell('Provides Cover:', 18, [permeate_cover], new_mod)
	body = mod_add(permeate, new_mod, body)

	cells = check_cell('Special', 12, special, cells, True)
	travel_select = [{'type': 'dimension', 'name': 'Dimension Travel', 'w': 20}, {'type': 'space', 'name': 'Space Travel', 'w': 18}, {'type': 'time', 'name': 'Time Travel', 'w': 15}, {'type': 'teleport', 'name': 'Teleport', 'w': 10}]
	new_mod = mod_create('Special Travel', 19, special_type, travel_select)
	value = 'dimension'
	new_mod = mod_cell('Type:', 8, [dimension_type], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [dimension_mass_rank], new_mod, value)
	new_mod = mod_cell('Descriptor:', 13, [dimension_descriptor], new_mod, value)
	value = 'space'
	new_mod = mod_cell('Type:', 8, [special_space], new_mod, value)
	value = 'time'
	new_mod = mod_cell('Type:', 8, [special_time], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [special_time_carry], new_mod, value)
	value = 'teleport'
	new_mod = mod_cell('Type:', 8, [teleport_type], new_mod, value)
	new_mod = mod_cell('Can Change:', 12, [teleport_change], new_mod, value)
	new_mod = mod_cell('Portal:', 9, [teleport_portal], new_mod, value)
	new_mod = mod_cell('Turnabout:', 9, [teleport_obstacles], new_mod, value)
	body = mod_add(special, new_mod, body)

	cells = check_cell('While Prone', 18, prone, cells)

	cells = check_cell('Check', 8, check_type, cells, True)
	new_mod = mod_create('Check Type', 18)
	new_mod = mod_cell('Trait:', 10, [check_trait], new_mod)
	new_mod = mod_cell('Free Check:', 12, [check_free], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Material', 12, materials, cells)

	cells = check_cell('Concealment', 14, concealment, cells, True)
	new_mod = mod_create('Concealment', 15)
	new_mod = mod_cell('Concealed From:', 18, [concealment_sense], new_mod)
	new_mod = mod_cell('Detected By:', 15, [concealment_trait], new_mod)
	body = mod_add(concealment, new_mod, body)

	cells = check_cell('Extended', 11, extended, cells, True)
	new_mod = mod_create('Extended', 10)
	word = string('Actions', [extended_actions])
	new_mod = mod_cell('For:', 5, [extended_actions, word], new_mod)
	body = mod_add(extended, new_mod, body)

	cells = check_cell('Carry Mass', 14, mass, cells, True)
	new_mod = mod_create('Increased Carry Mass', 30)
	new_mod = mod_cell('Mass Rank:', 13, [mass_value], new_mod)
	body = mod_add(mass, new_mod, body)
	
	cells = cell('Cost/Rank', 9, [cost], cells)
	cells = cell('Ranks', 7, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)



def opposed_post(entry, body, cells):	

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

	trait = trait_select(trait, trait_type)
	opponent_trait = trait_select(opponent_trait, opponent_trait_type)
	
	extra = extra_name(extra_id)
	player_check = name(Check, player_check)
	opponent_check = name(Check, opponent_check)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)

	cells = cell('Extra', 15, [extra])

	cells = cell('Player Trait', 18, [trait], cells)
	cells = cell('Mod', 6, [mod], cells)
	cells = cell('Player Check', 18, [player_check], cells)
	cells = cell('Opponent Trait', 18, [opponent_trait], cells)
	cells = cell('Mod', 6, [opponent_mod], cells)
	cells = cell('Opponent Check', 18, [opponent_check], cells)
	
	body = send(cells, body)

	cells.clear()

	return (body)


def time_post(entry, body, cells):
		
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

	trait = trait_select(trait, trait_type)

	extra = extra_name(extra_id)
	units = name(Unit, units)
	math = math_convert(Math, math)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)

	time_effect_select = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]
	time_type = selects(time_type, time_effect_select)

	value = integer_convert(value)
	time_value = integer_convert(time_value)
	trait = integer_convert(trait)
	dc = integer_convert(dc)
	recovery_penalty = integer_convert(recovery_penalty)
	recovery_time = integer_convert(recovery_time)

		
	cells = cell('Extra', 15, [extra])
	cells = cell('Type', 22, [time_type], cells)
	vcells = vcell('value', 14, [value, units])
	word = string('= Time Rank', [time_value, math, trait])
	vcells = vcell('math', 26, [time_value, math, trait, word], vcells)
	vcell_add('Time', value_type, vcells, cells)
	cells = cell('DC', 7, [dc], cells)
	cells = cell('Descriptor', 20, [descriptor], cells)
	cells = cell('Check', 18, [check_type], cells)

	cells = check_cell('Recovery', 10, recovery, cells, True)
	new_mod = mod_create('Recovery Time', 18)
	word = string('Every', [recovery_penalty, recovery_time])
	word2 = string('Time Rank', [recovery_penalty, recovery_time])
	new_mod = mod_cell('Toughness Penalty Nullified', 27, [recovery_penalty, word, recovery_time, word2], new_mod)
	new_mod = mod_cell('Includes Incurable', 16, [recovery_incurable], new_mod)
	body = mod_add(recovery, new_mod, body)

	body = send(cells, body)

	cells.clear()

	return (body)
