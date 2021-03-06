

def adv_alt_check_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	check_trigger = entry.check_trigger
	check_type = entry.check_type
	mod = entry.mod
	circumstance = entry.circumstance
	trigger = entry.trigger
	when = entry.when
	trait_type = entry.trait_type
	trait = entry.trait
	conflict = entry.conflict
	conflict_range = entry.conflict_range
	conflict_weapon = entry.conflict_weapon
	condition1 = entry.condition1
	condition2 = entry.condition2
	action_type = entry.action_type
	action = entry.action
	free = entry.free

	trait = trait_select(trait, trait_type)

	mod = integer_convert(mod)
	action = action_convert(action_type, action)

	benefit = integer(benefit)
	check_type = get_name(Check, check_type)
	conflict = get_name(ConflictAction, conflict)
	conflict_range = get_name(Ranged, conflict_range)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)
	
	check_trigger_select = [{'type': '', 'name': 'Triggered'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'conflict', 'name': 'Conflict'}]

	check_type_select = [{'type': '', 'name': 'When'}, {'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_type_select)

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Check Type', 15, [check_type], cells)
	cells = cell('Modifier', 13, [mod], cells)

	vcells = vcell('condition', 20, [condition1, 'to', condition2]) 
	vcells = vcell('conflict', 20, [conflict, conflict_range], vcells)
	cells = vcell_add('Trigger', trigger, vcells, cells)

	conflict_weapon = variable_value('conflict', trigger, conflict_weapon)

	cells = check_cell('Weapon', 8, conflict_weapon, cells)
	cells = cell('Trait', 16, [trait], cells)
	cells = cell('Action', 17, [action], cells)
	cells = cell('When', 13, [when], cells)
	cells = check_cell('Free Check', 12, free, cells)
	cells = cell('Circumstance', 28, [circumstance], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_circ_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	mod = entry.mod
	rounds = entry.rounds
	circumstance = entry.circumstance
	circ_type = entry.circ_type
	circ_range = entry.circ_range
	conflict = entry.conflict
	check_who = entry.check_who
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	null_type = entry.null_type
	null_condition = entry.null_condition
	null_trait_type = entry.null_trait_type
	null_trait = entry.null_trait
	null_override_trait_type = entry.null_override_trait_type
	null_override_trait = entry.null_override_trait

	check_trait = trait_select(check_trait, check_trait_type)
	null_trait = trait_select(null_trait, null_trait_type)
	null_override_trait = trait_select(null_override_trait, null_override_trait_type)

	mod = integer_convert(mod)
	rounds = integer_convert(rounds)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	circ_type_select = [{'type': '', 'name': 'Triggered By'}, {'type': 'use', 'name': 'Use of this Advantage'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}, {'type': 'conflict', 'name': 'Conflict Action'}]


	who_check_select = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player'}, {'type': 'opponent', 'name': 'Opponent'}]
	check_who = selects(check_who, who_check_select)

	circ_null_select = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'condition', 'name': 'From Condition'}, {'type': 'override', 'name': 'Override Trait Circumstance'}]

	benefit = name(Benefit, benefit)
	circ_range = get_name(Ranged, circ_range)
	conflict = get_name(ConflictAction, conflict)
	null_condition = get_name(Condition, null_condition)

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Target', 13, [target], cells)
	cells = cell('Modifier', 10, [mod], cells)
	cells = cell('Lasts', 8, [rounds], cells)

	circrange = string('Range', [circ_range])
	vcells = vcell('range', 20, [circ_range, circrange])
	vcells = vcell('check', 25, [check_who, check_trait], vcells)
	vcells = vcell('use', 20, ['Use of this Advantage'], vcells)
	vcells = vcell('conflict', 16, [conflict], vcells)
	cells = vcell_add('Trigger', circ_type, vcells, cells)

	vcells = vcell('trait', 17, [null_trait])
	vcells = vcell('override', 19, ['Override', null_override_trait], vcells)
	vcells = vcell('condition', 17, [null_condition], vcells)	
	cells = vcell_add('Nullified', null_type, vcells, cells)

	cells = cell('Circumstance', 25, [circumstance], cells)


	body = send(cells, body)
	
	cells.clear()

	return (body)



def adv_dc_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	dc = entry.dc
	description = entry.description
	value_value = entry.value_value
	math_value = entry.math_value
	math_math = entry.math_math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
	condition = entry.condition
	keyword_check = entry.keyword_check
	check_type = entry.check_type
	levels = entry.levels
	level_type = entry.level_type
	level = entry.level
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_mod = entry.check_mod

	math_trait = trait_select(math_trait, math_trait_type)
	check_trait = trait_select(check_trait, check_trait_type)

	dc = integer_convert(dc)
	value_value = integer_convert(value_value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

	benefit = name(Benefit, benefit)
	math_math = math_convert(Math, math_math)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Target', 18, [target], cells)
	vcells = vcell('value', 10, [value_value])
	vcells = vcell('math', 20, [math_value, math_math, math_trait], vcells)
	cells = vcell_add('DC', dc, vcells, cells)

	cells = check_cell('Condition', 13, condition, cells, True)
	new_mod = mod_create('Condition', 12)
	word = string('to', [condition1, condition2])
	new_mod = mod_cell('Conditions', 14, [condition1, word, condition2], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Keyword', 15, keyword_check, cells, True)
	new_mod = mod_create('Keyword', 10)
	new_mod = mod_cell('Key:', 7, [keyword], new_mod)
	body = mod_add(keyword_check, new_mod, body)

	cells = check_cell('Check', 12, check_type, cells, True)
	new_mod = mod_create('Check Type', 15)
	new_mod = mod_cell('Trait:', 7, [check_trait], new_mod)
	new_mod = mod_cell('Modifier:', 12, [check_mod], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Level', 12, levels, cells, True)
	new_mod = mod_create('Level', 8)
	new_mod = mod_cell('Level:', 7, [level], new_mod)
	body = mod_add(levels, new_mod, body)

	cells = cell('Description', 40, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def adv_deg_mod_post(entry, body, cells):

	advantage_id = entry.advantage_id
	target = entry.target
	benefit = entry.benefit
	value = entry.value
	deg_type = entry.deg_mod_type
	consequence_action_type = entry.consequence_action_type
	consequence_action = entry.consequence_action
	consequence_trait_type = entry.consequence_trait_type
	consequence_trait = entry.consequence_trait
	consequence = entry.consequence
	knowledge = entry.knowledge
	knowledge_count = entry.knowledge_count
	knowledge_specificity = entry.knowledge_specificity
	level_type = entry.level_type
	level = entry.level
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
	condition_type = entry.condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	nullify = entry.nullify
	cumulative = entry.cumulative
	linked = entry.linked

	consequence_trait = trait_select(consequence_trait, consequence_trait_type)
	circ_trait = trait_select(circ_trait, circ_trait_type)
	measure_trait = trait_select(measure_trait, measure_trait_type)

	value = integer_convert(value)
	consequence_action = action_convert(consequence_action_type, consequence_action)
	knowledge_count = integer_convert(knowledge_count)
	circ_value = integer_convert(circ_value)
	circ_turns = integer_convert(circ_turns)
	measure_val1 = integer_convert(measure_val1)
	measure_value = integer_convert(measure_value)
	condition_damage_value = integer_convert(condition_damage_value)
	condition_damage = integer_convert(condition_damage)
	nullify = integer_convert(nullify)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}, {'type': 'team', 'name': 'Teammate'}, {'type': 'allies', 'name': 'All Allies'}, {'type': 'opp', 'name': 'Opponent'}]
	target = selects(target, targets_select)

	specificity_select = [{'type': '', 'name': 'Specifity'}, {'type': 'relative', 'name': 'Relative'}, {'type': 'exact', 'name': 'Exact'}]
	knowledge_specificity = selects(knowledge_specificity, specificity_select)

	updown_select = [{'type': '1', 'name': 'Up'}, {'type': '-1', 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown_select)

	condition_select = [{'type': 'current', 'name': 'Current'}, {'type': 'any', 'name': 'Any'}, {'type': 'linked_first', 'name': 'Linked Starting'}, {'type': 'linked_second', 'name': 'Linked Ending'}]
	condition1 = selects(condition1, condition_select)
	condition2 = selects(condition2, condition_select)

	benefit = name(Benefit, benefit)
	consequence = get_name(Consequence, consequence)
	level_type = get_name(LevelType, level_type)
	level = get_name(Levels, level)
	measure_math = math_convert(Math, measure_math)
	measure_rank = get_name(Rank, measure_rank)
	condition1 = get_name(Condition, condition1)
	condition2 = get_name(Condition, condition2)


	cells = cell('Benefit', 15, [benefit])
	cells = cell('Target', 14, [target], cells)
	cells = cell('Degree',10, [value], cells)
	cells = cell('Keyword', 14, [keyword], cells)
	cells = cell('Nullify DC', 14, [value], cells)
	cells = check_cell('Cumulative', 15, cumulative, cells)
	cells = check_cell('Linked', 9, linked, cells)
	word = string('for', [circ_trait, circ_value, circ_turns])
	word2 = string('Turns', [circ_trait, circ_value, circ_turns])
	vcells = vcell('circ', 30, [circ_trait, circ_value, word, circ_turns, word2]) 
	vcells = vcell('uncontrolled', 16, ['Uncontrolled'], vcells)
	vcells = vcell('level', 16, [level], vcells)
	vcells = vcell('measure', 22, [measure_value, measure_rank], vcells, 'value', measure_type)
	vcells = vcell('measure', 26, [measure_val1, measure_math, measure_trait], vcells, 'math', measure_type)
	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 32, [condition1, word, condition2], vcells, 'condition', condition_type)
	word = string('Conditions', [condition_damage_value, condition_damage])
	vcells = vcell('condition', 20, [condition_damage_value, word, condition_damage], vcells, 'damage', condition_type)
	vcells = vcell('knowledge', 28, [knowledge_count, knowledge_specificity, 'Bonuses'], vcells, 'bonus', knowledge)
	vcells = vcell('knowledge', 25, ['Gain Knowledge but GM may lie'], vcells, 'lie', knowledge)
	word = string('for', consequence_trait)
	vcells = vcell('consequence', 33, [consequence, word, consequence_trait, consequence_action], vcells)
	
	vcell_add('Effect', deg_type, vcells, cells)
	





	body = send(cells, body)
	
	cells.clear()

	return (body)


def adv_opposed_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check
	multiple = entry.multiple

	trait = trait_select(trait, trait_type)
	opponent_trait = trait_select(opponent_trait, opponent_trait_type)

	multiple_opposed = [{'type': '', 'name': 'If Multiple'}, {'type': 'high', 'name': 'Higher Rank'}, {'type': 'low', 'name': 'Lower Rank'}, {'type': 'player', 'name': 'Player Choice'}, {'type': 'opponent', 'name': 'Opponent Choice'}]
	multiple = selects(multiple, multiple_opposed)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)

	benefit = name(Benefit, benefit)
	player_check = get_name(Check, player_check)
	opponent_check = get_name(Check, opponent_check)

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Player Trait', 18, [trait], cells)
	cells = cell('Player Check', 15, [player_check], cells)
	cells = cell('Modifier', 9, [mod], cells)
	cells = cell('Opponent Trait', 18, [opponent_trait], cells)
	cells = cell('Opponent Check', 15, [opponent_check], cells)
	cells = cell('Modifier', 9, [opponent_mod], cells)
	cells = cell('Multiple', 12, [multiple], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)



def adv_time_post(entry, body, cells):

	advantage_id = entry.advantage_id
	benefit = entry.benefit
	time_type = entry.time_type
	value_type = entry.value_type
	value = entry.value
	units = entry.units
	time_value = entry.time_value
	math = entry.math
	trait_type = entry.trait_type
	trait = entry.trait
	dc = entry.dc
	check_type = entry.check_type
	recovery = entry.recovery
	recovery_penalty = entry.recovery_penalty
	recovery_time = entry.recovery_time
	recovery_incurable = entry.recovery_incurable

	trait = trait_select(trait, trait_type)

	value = integer_convert(value)
	time_value = integer_convert(time_value)
	dc = integer_convert(dc)
	recovery_penalty = integer_convert(recovery_penalty)
	recovery_time = integer_convert(recovery_time)

	benefit = name(Benefit, benefit)
	units = name(Unit, units)
	math = math_convert(Math, math)
	check_type = name(Check, check_type)

	time_effect = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]
	time_type = selects(time_type, time_effect)

	cells = cell('Benefit', 15, [benefit])
	cells = cell('Type', 22, [time_type], cells)
	vcells = vcell('value', 14, [value, units])
	word = string('= Time Rank', [time_value, math, trait])
	vcells = vcell('math', 26, [time_value, math, trait, word], vcells)
	vcell_add('Time', value_type, vcells, cells)
	cells = cell('DC', 7, [dc], cells)
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