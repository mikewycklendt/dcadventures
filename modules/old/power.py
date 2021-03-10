
@powers.route('/power/alt_check/create', methods=['POST'])
def power_post_alt_check():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = alt_check_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	check_type = request.get_json()['check_type']
	mod = request.get_json()['mod']
	circumstance = request.get_json()['circumstance']
	when = request.get_json()['when']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	check_type = db_integer(Check, check_type)

	mod = integer(mod)
	trait = integer(trait)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']


	try:
		entry = PowerAltCheck(power_id = power_id,
								extra_id = extra_id,
								check_type = check_type,
								mod = mod,
								circumstance = circumstance,
								when = when,
								trait_type = trait_type,
								trait = trait)

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
		table_id = 'alt-check'
		spot = "alt-check-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = alt_check_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/alt_check/delete/<power_id>', methods=['DELETE'])
def delete_power_altcheck(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerAltCheck).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)


@powers.route('/power/circ/create', methods=['POST'])
def power_post_circ():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = circ_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	mod = request.get_json()['mod']
	rounds = request.get_json()['rounds']
	description = request.get_json()['description']
	circ_type = request.get_json()['circ_type']
	circ_range = request.get_json()['circ_range']
	check_who = request.get_json()['check_who']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	null_type = request.get_json()['null_type']
	null_condition = request.get_json()['null_condition']
	null_descriptor = request.get_json()['null_descriptor']
	null_trait_type = request.get_json()['null_trait_type']
	null_trait = request.get_json()['null_trait']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	circ_range = db_integer(Ranged, circ_range)
	null_condition = db_integer(Condition, null_condition)

	mod = integer(mod)
	rounds = integer(rounds)
	check_trait = integer(check_trait)
	null_descriptor = integer(null_descriptor)
	null_trait = integer(null_trait)

	try:
		entry = PowerCirc(power_id = power_id,
							extra_id = extra_id,
							target = target,
							mod = mod,
							rounds = rounds,
							description = description,
							circ_type = circ_type,
							circ_range = circ_range,
							check_who = check_who,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							null_type = null_type,
							null_condition = null_condition,
							null_descriptor = null_descriptor,
							null_trait_type = null_trait_type,
							null_trait = null_trait)

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
		spot = "circ-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = circ_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/circ/delete/<power_id>', methods=['DELETE'])
def delete_power_circ(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerCirc).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)



@powers.route('/power/dc_table/create', methods=['POST'])
def power_post_dc_table():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = dc_table_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	dc = request.get_json()['dc']
	description = request.get_json()['description']
	value = request.get_json()['value']
	math_value = request.get_json()['math_value']
	math = request.get_json()['math']
	math_trait_type = request.get_json()['math_trait_type']
	math_trait = request.get_json()['math_trait']
	descriptor_check = request.get_json()['descriptor_check']
	condition = request.get_json()['condition']
	keyword_check = request.get_json()['keyword_check']
	check_type = request.get_json()['check_type']
	descriptor = request.get_json()['descriptor']
	descriptor_possess = request.get_json()['descriptor_possess']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_mod = request.get_json()['check_mod']
	levels = request.get_json()['levels']
	level = request.get_json()['level']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	level = db_integer(Levels, level)

	value = integer(value)
	math_value = integer(math_value)
	math_trait = integer(math_trait)
	descriptor = integer(descriptor)
	check_trait = integer(check_trait)
	check_mod = integer(check_mod)

	if level is not None:
		try:
			level_dc = db.session.query(Levels).filter(Levels.id == level).one()
			level_dc.power_dc = True
			db.session.commit()
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()
		finally:
			db.session.close()
	try:
		entry = PowerDC(power_id = power_id,
						extra_id = extra_id,
						target = target,
						dc = dc,
						description = description,
						value = value,
						math_value = math_value,
						math = math,
						math_trait_type = math_trait_type,
						math_trait = math_trait,
						descriptor_check = descriptor_check,
						condition = condition,
						keyword_check = keyword_check,
						check_type = check_type,
						descriptor = descriptor,
						descriptor_possess = descriptor_possess,
						condition1 = condition1,
						condition2 = condition2,
						keyword = keyword,
						check_trait_type = check_trait_type,
						check_trait = check_trait,
						check_mod = check_mod,
						levels = levels,
						level = level)

		db.session.add(entry)
		db.session.commit()

		body = {}
		body['id'] = entry.id
		error = False
		error_msg = []
		body['success'] = True

		rows = columns
		body['rows'] = rows
		mods = []
		cells = []
		table_id = 'dc'
		spot = "dc-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = dc_table_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/dc/delete/<power_id>', methods=['DELETE'])
def delete_power_dc(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerDC).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)



@powers.route('/power/degree_mod/create', methods=['POST'])
def power_post_degree_mod():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = degree_mod_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	target = request.get_json()['target']
	value = request.get_json()['value']
	deg_type = request.get_json()['deg_type']
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
	deg_condition_type = request.get_json()['deg_condition_type']
	condition_damage_value = request.get_json()['condition_damage_value']
	condition_damage = request.get_json()['condition_damage']
	condition1 = request.get_json()['condition1']
	condition2 = request.get_json()['condition2']
	keyword = request.get_json()['keyword']
	nullify = request.get_json()['nullify']
	cumulative = request.get_json()['cumulative']
	linked = request.get_json()['linked']
	level = request.get_json()['level']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']
	consequence_action_type = request.get_json()['consequence_action_type']
	consequence_action = request.get_json()['consequence_action']
	consequence_trait_type = request.get_json()['consequence_trait_type']
	consequence_trait = request.get_json()['consequence_trait']
	consequence = request.get_json()['consequence']
	knowledge = request.get_json()['knowledge']
	knowledge_count = request.get_json()['knowledge_count']
	knowledge_specificity = request.get_json()['knowledge_specificity']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	measure_math = db_integer(Math, measure_math)
	measure_rank = db_integer(Rank, measure_rank)
	condition1 = db_integer(Condition, condition1)
	condition2 = db_integer(Condition, condition2)
	level = db_integer(Levels, level)
	consequence = db_integer(Consequence, consequence)

	value = integer(value)
	circ_value = integer(circ_value)
	circ_turns = integer(circ_turns)
	circ_trait = integer(circ_trait)
	measure_val1 = integer(measure_val1)
	measure_trait = integer(measure_trait)
	measure_value = integer(measure_value)
	condition_damage_value = integer(condition_damage_value)
	condition_damage = integer(condition_damage)
	nullify = integer(nullify)
	consequence_action = integer(consequence_action)
	consequence_trait = integer(consequence_trait)
	knowledge_count = integer(knowledge_count)

	if level is not None:
		try:
			level_degree = db.session.query(Levels).filter(Levels.id == level).one()
			level_degree.power_degree = True
			db.session.commit()
		except:
			error = True
			body['success'] = False
			body['error'] = 'There was an error processing the request'
			db.session.rollback()
		finally:
			db.session.close()

	try:
		entry = PowerDegMod(power_id = power_id,
							extra_id = extra_id,
							target = target,
							value = value,
							deg_type = deg_type,
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
							deg_condition_type = deg_condition_type,
							condition_damage_value = condition_damage_value,
							condition_damage = condition_damage,
							condition1 = condition1,
							condition2 = condition2,
							keyword = keyword,
							nullify = nullify,
							cumulative = cumulative,
							linked = linked,
							level = level,
							consequence_action_type = consequence_action_type,
							consequence_action = consequence_action,
							consequence_trait_type = consequence_trait_type,
							consequence_trait = consequence_trait,
							consequence = consequence,
							knowledge = knowledge,
							knowledge_count = knowledge_count,
							knowledge_specificity = knowledge_specificity)

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
		spot = "deg-mod-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = degree_mod_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/degree_mod/delete/<power_id>', methods=['DELETE'])
def delete_power_degree_mod(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerDegMod).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/degree/create', methods=['POST'])
def power_post_degree():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = degree_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	degree_type = request.get_json()['degree_type']
	degree = request.get_json()['degree']
	keyword = request.get_json()['keyword']
	desscription = request.get_json()['desscription']
	extra_effort = request.get_json()['extra_effort']
	cumulative = request.get_json()['cumulative']
	target = request.get_json()['target']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = extra_convert(extra_id)
	degree = integer(degree)

	try:
		entry = PowerDegree(power_id = power_id,
							extra_id = extra_id,
							degree_type = degree_type,
							degree = degree,
							keyword = keyword,
							desscription = desscription,
							extra_effort = extra_effort,
							cumulative = cumulative,
							target = target)

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
		table_id = 'degree'
		spot = "degree-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = degree_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/degree/delete/<power_id>', methods=['DELETE'])
def delete_power_degree(power_id):
	try:
		db.session.query(PowerDegree).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify({'success': True, 'id': power_id})



@powers.route('/power/move/create', methods=['POST'])
def power_post_move():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = move_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	rank = request.get_json()['rank']
	math = request.get_json()['math']
	mod = request.get_json()['mod']
	per_rank = request.get_json()['per_rank']
	flight = request.get_json()['flight']
	aquatic = request.get_json()['aquatic']
	ground = request.get_json()['ground']
	condition = request.get_json()['condition']
	direction = request.get_json()['direction']
	distance_type = request.get_json()['distance_type']
	distance_value = request.get_json()['distance_value']
	distance_math_value = request.get_json()['distance_math_value']
	distance_math = request.get_json()['distance_math']
	distance_math_value2 = request.get_json()['distance_math_value2']
	distance_mod = request.get_json()['distance_mod']
	dc = request.get_json()['dc']
	others = request.get_json()['others']
	continuous = request.get_json()['continuous']
	subtle = request.get_json()['subtle']
	concentration = request.get_json()['concentration']
	obstacles = request.get_json()['obstacles']
	objects = request.get_json()['objects']
	permeate = request.get_json()['permeate']
	special = request.get_json()['special']
	prone = request.get_json()['prone']
	check_type = request.get_json()['check_type']
	materials = request.get_json()['materials']
	concealment = request.get_json()['concealment']
	extended = request.get_json()['extended']
	mass = request.get_json()['mass']
	mass_value = request.get_json()['mass_value']
	extended_actions = request.get_json()['extended_actions']
	acquatic_type = request.get_json()['acquatic_type']
	concealment_sense = request.get_json()['concealment_sense']
	concealment_trait_type = request.get_json()['concealment_trait_type']
	concealment_trait = request.get_json()['concealment_trait']
	permeate_type = request.get_json()['permeate_type']
	permeate_speed = request.get_json()['permeate_speed']
	permeate_cover = request.get_json()['permeate_cover']
	special_type = request.get_json()['special_type']
	teleport_type = request.get_json()['teleport_type']
	teleport_change = request.get_json()['teleport_change']
	teleport_portal = request.get_json()['teleport_portal']
	teleport_obstacles = request.get_json()['teleport_obstacles']
	dimension_type = request.get_json()['dimension_type']
	dimension_mass_rank = request.get_json()['dimension_mass_rank']
	dimension_descriptor = request.get_json()['dimension_descriptor']
	special_space = request.get_json()['special_space']
	special_time = request.get_json()['special_time']
	special_time_carry = request.get_json()['special_time_carry']
	ground_type = request.get_json()['ground_type']
	ground_permanence = request.get_json()['ground_permanence']
	ground_time = request.get_json()['ground_time']
	ground_units = request.get_json()['ground_units']
	ground_ranged = request.get_json()['ground_ranged']
	subtle_trait_type = request.get_json()['subtle_trait_type']
	subtle_trait = request.get_json()['subtle_trait']
	subtle_mod = request.get_json()['subtle_mod']
	flight_resist = request.get_json()['flight_resist']
	flight_equip = request.get_json()['flight_equip']
	flight_conditions = request.get_json()['flight_conditions']
	objects_check = request.get_json()['objects_check']
	objects_attack = request.get_json()['objects_attack']
	objects_skill_type = request.get_json()['objects_skill_type']
	objects_skill = request.get_json()['objects_skill']
	objects_direction = request.get_json()['objects_direction']
	objects_damage = request.get_json()['objects_damage']
	damage_type = request.get_json()['damage_type']
	check_trait_type = request.get_json()['check_trait_type']
	check_trait = request.get_json()['check_trait']
	check_free = request.get_json()['check_free']
	ranks = request.get_json()['ranks']
	cost = request.get_json()['cost']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	math = db_integer(Math, math)
	condition = db_integer(Condition, condition)
	distance_math = db_integer(Math, distance_math)
	concealment_sense = db_integer(Sense, concealment_sense)
	ground_type = db_integer(Ground, ground_type)
	ground_units = db_integer(Unit, ground_units)
	objects_check = db_integer(Check, objects_check)
	objects_attack = db_integer(ConflictAction, objects_attack)
	damage_type = db_integer(Ability, damage_type)

	rank = integer(rank)
	mod = integer(mod)
	distance_value = integer(distance_value)
	distance_math_value = integer(distance_math_value)
	distance_math_value2 = integer(distance_math_value2)
	distance_mod = integer(distance_mod)
	dc = integer(dc)
	mass_value = integer(mass_value)
	extended_actions = integer(extended_actions)
	concealment_trait = integer(concealment_trait)
	permeate_speed = integer(permeate_speed)
	dimension_mass_rank = integer(dimension_mass_rank)
	dimension_descriptor = integer(dimension_descriptor)
	special_time_carry = integer(special_time_carry)
	ground_time = integer(ground_time)
	subtle_trait = integer(subtle_trait)
	subtle_mod = integer(subtle_mod)
	objects_skill = integer(objects_skill)
	check_trait = integer(check_trait)
	ranks = integer(ranks)
	cost = integer(cost)

	try:
		entry = PowerMove(power_id = power_id,
							extra_id = extra_id,
							rank = rank,
							math = math,
							mod = mod,
							per_rank = per_rank,
							flight = flight,
							aquatic = aquatic,
							ground = ground,
							condition = condition,
							direction = direction,
							distance_type = distance_type,
							distance_value = distance_value,
							distance_math_value = distance_math_value,
							distance_math = distance_math,
							distance_math_value2 = distance_math_value2,
							distance_mod = distance_mod,
							dc = dc,
							others = others,
							continuous = continuous,
							subtle = subtle,
							concentration = concentration,
							obstacles = obstacles,
							objects = objects,
							permeate = permeate,
							special = special,
							prone = prone,
							check_type = check_type,
							materials = materials,
							concealment = concealment,
							extended = extended,
							mass = mass,
							mass_value = mass_value,
							extended_actions = extended_actions,
							acquatic_type = acquatic_type,
							concealment_sense = concealment_sense,
							concealment_trait_type = concealment_trait_type,
							concealment_trait = concealment_trait,
							permeate_type = permeate_type,
							permeate_speed = permeate_speed,
							permeate_cover = permeate_cover,
							special_type = special_type,
							teleport_type = teleport_type,
							teleport_change = teleport_change,
							teleport_portal = teleport_portal,
							teleport_obstacles = teleport_obstacles,
							dimension_type = dimension_type,
							dimension_mass_rank = dimension_mass_rank,
							dimension_descriptor = dimension_descriptor,
							special_space = special_space,
							special_time = special_time,
							special_time_carry = special_time_carry,
							ground_type = ground_type,
							ground_permanence = ground_permanence,
							ground_time = ground_time,
							ground_units = ground_units,
							ground_ranged = ground_ranged,
							subtle_trait_type = subtle_trait_type,
							subtle_trait = subtle_trait,
							subtle_mod = subtle_mod,
							flight_resist = flight_resist,
							flight_equip = flight_equip,
							flight_conditions = flight_conditions,
							objects_check = objects_check,
							objects_attack = objects_attack,
							objects_skill_type = objects_skill_type,
							objects_skill = objects_skill,
							objects_direction = objects_direction,
							objects_damage = objects_damage,
							damage_type = damage_type,
							check_trait_type = check_trait_type,
							check_trait = check_trait,
							check_free = check_free,
							ranks = ranks,
							cost = cost)

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
		table_id = 'move'
		spot = "move-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = move_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()
	finally:
		db.session.close()

	return jsonify(body)


@powers.route('/power/move/delete/<power_id>', methods=['DELETE'])
def delete_power_move(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerMove).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)

@powers.route('/power/opposed/create', methods=['POST'])
def power_post_opposed():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = opposed_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	mod = request.get_json()['mod']
	opponent_trait_type = request.get_json()['opponent_trait_type']
	opponent_trait = request.get_json()['opponent_trait']
	opponent_mod = request.get_json()['opponent_mod']
	player_check = request.get_json()['player_check']
	opponent_check = request.get_json()['opponent_check']
	columns = request.get_json()['columns']
	created = request.get_json()['created']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	player_check = db_integer(Check, player_check)
	opponent_check = db_integer(Check, opponent_check)

	trait = integer(trait)
	mod = integer(mod)
	opponent_trait = integer(opponent_trait)
	opponent_mod = integer(opponent_mod)

	try:
		entry = PowerOpposed(power_id = power_id,
								extra_id = extra_id,
								trait_type = trait_type,
								trait = trait,
								mod = mod,
								opponent_trait_type = opponent_trait_type,
								opponent_trait = opponent_trait,
								opponent_mod = opponent_mod,
								player_check = player_check,
								opponent_check = opponent_check)

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
		spot = "opposed-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = opposed_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()	
	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/opposed/delete/<power_id>', methods=['DELETE'])
def delete_power_opposed(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerOpposed).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)


@powers.route('/power/time/create', methods=['POST'])
def power_post_time():

	body = {}
	body['success'] = True
	errors = {'error': False, 'error_msgs': []}
	data = request.get_json()

	errors = time_post_errors(data)

	error = errors['error']
	if error:
		body['success'] = False
		body['error_msgs'] = errors['error_msgs']
		return jsonify(body)


	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	time_type = request.get_json()['time_type']
	value_type = request.get_json()['value_type']
	value = request.get_json()['value']
	units = request.get_json()['units']
	time_value = request.get_json()['time_value']
	math = request.get_json()['math']
	trait_type = request.get_json()['trait_type']
	trait = request.get_json()['trait']
	dc = request.get_json()['dc']
	descriptor = request.get_json()['descriptor']
	check_type = request.get_json()['check_type']
	recovery = request.get_json()['recovery']
	recovery_penalty = request.get_json()['recovery_penalty']
	recovery_time = request.get_json()['recovery_time']
	recovery_incurable = request.get_json()['recovery_incurable']
	created = request.get_json()['created']
	columns = request.get_json()['columns']
	font = request.get_json()['font']

	power_id = integer(power_id)
	extra_id = db_integer(Extra, extra_id)
	units = db_integer(Unit, units)
	math = db_integer(Math, math)
	check_type = db_integer(Check, check_type)

	value = integer(value)
	time_value = integer(time_value)
	trait = integer(trait)
	dc = integer(dc)
	descriptor = integer(descriptor)
	recovery_penalty = integer(recovery_penalty)
	recovery_time = integer(recovery_time)

	try:
		entry = PowerTime(power_id = power_id,
							extra_id = extra_id,
							time_type = time_type,
							value_type = value_type,
							value = value,
							units = units,
							time_value = time_value,
							math = math,
							trait_type = trait_type,
							trait = trait,
							dc = dc,
							descriptor = descriptor,
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
		spot = "time-spot"

		body['table_id'] = table_id
		body['spot'] = spot
		body['created'] = created
		body['title'] = ''
		body['rows'] = rows
		body['mods'] = []
		body['font'] = font
		body['circ'] = []

		body = time_post(entry, body, cells)
	except:
		error = True
		error_msgs = []
		body['success'] = False
		message = 'There was an error processing the request'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
		db.session.rollback()

	finally:
		db.session.close()
	return jsonify(body)


@powers.route('/power/time/delete/<power_id>', methods=['DELETE'])
def delete_power_time(power_id):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		db.session.query(PowerTime).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return jsonify(body)