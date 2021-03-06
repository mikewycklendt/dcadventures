	
@advantage.route('/advantage/alt_check/create', methods=['POST'])
def advantage_post_alt_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_alt_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	check_type = request.get_json()['check_type']
	check_trigger = request.get_json()['check_trigger']
	mod = request.get_json()['mod']
	circumstance = request.get_json()['circumstance']
	trigger = request.get_json()['trigger']
	when = request.get_json()['when']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	conflict = request.get_json()['conflict']
	conflict_range = request.get_json()['conflict_range']
	conflict_weapon = request.get_json()['conflict_weapon']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	action_type = request.get_json()['action_type']
	action = request.get_json()['action']
	free = request.get_json()['free']

	try:

		check_type = db_integer(Check, check_type)
		conflict = db_integer(ConflictAction, conflict)
		conflict_range = db_integer(Ranged, conflict_range)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		mod = integer(mod)
		trait = integer(trait)
		action = integer(action)	

		entry = AdvAltCheck(advantage_id = advantage_id,
								benefit = benefit,
								check_trigger = check_trigger,
								check_type = check_type,
								mod = mod,
								circumstance = circumstance,
								trigger = trigger,
								when = when,
								trait_type = trait_type,
								trait = trait,
								conflict = conflict,
								conflict_range = conflict_range,
								conflict_weapon = conflict_weapon,
								condition1 = condition1,
								condition2 = condition2,
								action_type = action_type,
								action = action,
								free = free)

		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'check'	
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []	
		body['font'] = font
		body['circ'] = []
			
		body = adv_alt_check_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/alt_check/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_alt_check(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvAltCheck).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)


	
@advantage.route('/advantage/circ/create', methods=['POST'])
def advantage_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_circ_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	mod = request.get_json()['mod']
	rounds = request.get_json()['rounds']
	circumstance = request.get_json()['circumstance']
	circ_type = request.get_json()['circ_type']
	circ_range = request.get_json()['circ_range']
	conflict = request.get_json()['conflict']
	check_who = request.get_json()['check_who']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	null_type = request.get_json()['null_type']
	null_condition = request.get_json()['null_condition']
	null_trait_type = request.get_json()['null_trait_type']
	null_trait = request.get_json()['null_trait']
	null_override_trait_type = request.get_json()['null_override_trait_type']
	null_override_trait = request.get_json()['null_override_trait']


	try:
		circ_range = db_integer(Ranged, circ_range)
		conflict = db_integer(ConflictAction, conflict)
		null_condition = db_integer(Condition, null_condition)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
		mod = integer(mod)
		rounds = integer(rounds)
		check_trait = integer(check_trait)
		null_trait = integer(null_trait)
		null_override_trait = integer(null_override_trait)
		
		entry = AdvCirc(advantage_id = advantage_id,
							target = target,
							benefit = benefit,
							mod = mod,
							rounds = rounds,
							circumstance = circumstance,
							circ_type = circ_type,
							circ_range = circ_range,
							conflict = conflict,
							check_who = check_who,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							null_type = null_type,
							null_condition = null_condition,
							null_trait_type = null_trait_type,
							null_trait = null_trait,
							null_override_trait_type = null_override_trait_type,
							null_override_trait = null_override_trait)

		db.session.add(entry)
		db.session.commit()

		body = {}	
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []	
		cells = []
		table_id = 'circ'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot	
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = adv_circ_post(entry, body, cells)
		
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/circ/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_circ(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvCirc).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)


	
@advantage.route('/advantage/dc/create', methods=['POST'])
def advantage_post_dc():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_dc_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	dc = request.get_json()['dc']
	description = request.get_json()['description']
	value_value = request.get_json()['value_value']
	math_value = request.get_json()['math_value']
	math_math = request.get_json()['math_math']
	math_trait_type = request.get_json()['math_trait_type']
	math_trait = request.get_json()['math_trait']
	condition = request.get_json()['condition']
	keyword_check = request.get_json()['keyword_check']
	check_type = request.get_json()['check_type']
	levels = request.get_json()['levels']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_mod = request.get_json()['check_mod']

	try:
		math_math = db_integer(Math, math_math)
		level_type = db_integer(LevelType, level_type)
		level = db_integer(Levels, level)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
	
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value_value = integer(value_value)
		math_value = integer(math_value)
		math_trait = integer(math_trait)
		check_trait = integer(check_trait)
		check_mod = integer(check_mod)

		entry = AdvDC(advantage_id = advantage_id,
							target = target,
							benefit = benefit,
							dc = dc,
							description = description,
							value_value = value_value,
							math_value = math_value,
							math_math = math_math,
							math_trait_type = math_trait_type,
							math_trait = math_trait,
							condition = condition,
							keyword_check = keyword_check,
							check_type = check_type,
							levels = levels,
							level_type = level_type,
							level = level,
							condition1 = condition1,
							condition2 = condition2,
							keyword = keyword,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							check_mod = check_mod)
							
		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'dc'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []
				
		body = adv_dc_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/dc/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_dc(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvDC).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

	
@advantage.route('/advantage/degree_mod/create', methods=['POST'])
def advantage_post_deg_mod():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_deg_mod_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	target = request.get_json()['target']
	benefit = request.get_json()['benefit']
	value = request.get_json()['value']
	deg_mod_type = request.get_json()['deg_mod_type']
	consequence_action_type = request.get_json()['consequence_action_type']
	consequence_action = request.get_json()['consequence_action']
	consequence_trait_type = request.get_json()['consequence_trait_type']
	consequence_trait = request.get_json()['consequence_trait']
	consequence = request.get_json()['consequence']
	knowledge = request.get_json()['knowledge']
	knowledge_count = request.get_json()['knowledge_count']
	knowledge_specificity = request.get_json()['knowledge_specificity']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	circ_value = request.get_json()['circ_value']
	circ_turns = request.get_json()['circ_turns']
	circ_trait_type = request.get_json()['circ_trait_type']
	circ_trait = request.get_json()['circ_trait']
	measure_type = request.get_json()['measure_type']
	measure_val1 = request.get_json()['measure_val1']
	measure_math = request.get_json()['measure_math']
	measure_trait_type = request.get_json()['measure_trait_type']
	measure_trait = request.get_json()['measure_trait']
	measure_value = request.get_json()['measure_value']
	measure_rank = request.get_json()['measure_rank']
	condition_type = request.get_json()['condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	nullify = request.get_json()['nullify']
	cumulative = request.get_json()['cumulative']
	linked = request.get_json()['linked']

	try:
		consequence = db_integer(Consequence, consequence)
		level_type = db_integer(LevelType, level_type)
		level = db_integer(Levels, level)
		measure_math = db_integer(Math, measure_math)
		measure_rank = db_integer(Rank, measure_rank)
		condition1 = db_integer(Condition, condition1)
		condition2 = db_integer(Condition, condition2)
		
		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value = integer(value)
		consequence_action = integer(consequence_action)
		consequence_trait = integer(consequence_trait)
		knowledge_count = integer(knowledge_count)
		circ_value = integer(circ_value)
		circ_turns = integer(circ_turns)
		circ_trait = integer(circ_trait)
		measure_val1 = integer(measure_val1)
		measure_trait = integer(measure_trait)
		measure_value = integer(measure_value)
		condition_damage_value = integer(condition_damage_value)
		condition_damage = integer(condition_damage)
		nullify = integer(nullify)
		
		entry = AdvDegree(advantage_id = advantage_id,
								target = target,
								benefit = benefit,
								value = value,
								deg_mod_type = deg_mod_type,
								consequence_action_type = consequence_action_type,
								consequence_action = consequence_action,
								consequence_trait_type = consequence_trait_type,
								consequence_trait = consequence_trait,
								consequence = consequence,
								knowledge = knowledge,
								knowledge_count = knowledge_count,
								knowledge_specificity = knowledge_specificity,
								level_type = level_type,
								level = level,
								circ_value = circ_value,
								circ_turns = circ_turns,
								circ_trait_type = circ_trait_type,
								circ_trait = circ_trait,
								measure_type = measure_type,
								measure_val1 = measure_val1,
								measure_math = measure_math,
								measure_trait_type = measure_trait_type,
								measure_trait = measure_trait,
								measure_value = measure_value,
								measure_rank = measure_rank,
								condition_type = condition_type,
								condition_damage_value = condition_damage_value,
								condition_damage = condition_damage,
								condition1 = condition1,
								condition2 = condition2,
								keyword = keyword,
								nullify = nullify,
								cumulative = cumulative,
								linked = linked)

		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'deg-mod'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []
				
		body = adv_deg_mod_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()

	return jsonify(body)


@advantage.route('/advantage/degree_mod/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_deg_mod(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvDegree).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)


@advantage.route('/advantage/opposed/create', methods=['POST'])
def advantage_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	opponent_trait_type = request.get_json()['opponent_trait_type']
	opponent_trait = request.get_json()['opponent_trait']
	opponent_mod = request.get_json()['opponent_mod']
	player_check = request.get_json()['player_check']
	opponent_check = request.get_json()['opponent_check']
	multiple = request.get_json()['multiple']

	try:
		player_check = db_integer(Check, player_check)
		opponent_check = db_integer(Check, opponent_check)

		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		trait = integer(trait)
		mod = integer(mod)
		opponent_trait = integer(opponent_trait)
		opponent_mod = integer(opponent_mod)

		entry = AdvOpposed(advantage_id = advantage_id,
								benefit = benefit,
								trait_type = trait_type,
								trait = trait,
								mod = mod,
								opponent_trait_type = opponent_trait_type,
								opponent_trait = opponent_trait,
								opponent_mod = opponent_mod,
								player_check = player_check,
								opponent_check = opponent_check,
								multiple = multiple)

		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []	
		cells = []
		table_id = 'opposed'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot	
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []
				
		body = adv_opposed_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/opposed/delete/<advantage_id>', methods=['DELETE'])
def delete_post_opposed(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvOpposed).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)

@advantage.route('/advantage/time/create', methods=['POST'])
def advantage_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = adv_time_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)

	advantage_id = request.get_json()['advantage_id']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	benefit = request.get_json()['benefit']
	time_type = request.get_json()['time_type']
	value_type = request.get_json()['value_type']
	value = request.get_json()['value']
	units = request.get_json()['units']
	time_value = request.get_json()['time_value']
	math = request.get_json()['math']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	dc = request.get_json()['dc']
	check_type = request.get_json()['check_type']
	recovery = request.get_json()['recovery']
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_time = request.get_json()['recovery_time']
	recovery_incurable = request.get_json()['recovery_incurable']

	try:
		units = db_integer(Unit, units)
		math = db_integer(Math, math)
		check_type = db_integer(Check, check_type)

		advantage_id = integer(advantage_id)
		benefit = integer(benefit)
	
		value = integer(value)
		time_value = integer(time_value)
		trait = integer(trait)
		dc = integer(dc)
		recovery_penalty = integer(recovery_penalty)
		recovery_time = integer(recovery_time)

		entry = AdvTime(advantage_id = advantage_id,
							benefit = benefit,
							time_type = time_type,
							value_type = value_type,
							value = value,
							units = units,
							time_value = time_value,
							math = math,
							trait_type = trait_type,
							trait = trait,
							dc = dc,
							check_type = check_type,
							recovery = recovery,
							recovery_penalty = recovery_penalty,
							recovery_time = recovery_time,
							recovery_incurable = recovery_incurable)

		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		mods = []
		cells = []
		table_id = 'time'
		spot = table_id + '-spot'

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows	
		body['mods'] = []
		body['font'] = font
		body['circ'] = []
				
		body = adv_time_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['success'] = False
		body['error_msgs'] = error_msgs 
		db.session.rollback()
	
	finally:
		db.session.close()
	return jsonify(body)


@advantage.route('/advantage/time/delete/<advantage_id>', methods=['DELETE'])
def delete_advantage_time(advantage_id):
	body = {}
	body['success'] = True
	body['id'] = advantage_id
	try:
		db.session.query(AdvTime).filter_by(id=advantage_id).delete()
		db.session.commit()
	except:
		body['success'] = False
		message = 'Could not delete this rule.'
		error_msgs = []
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(advantage_id) + ' DELETED\n\n')
		return jsonify(body)
