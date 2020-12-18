from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSense, PowerTime 


def required(value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value == '':
		error = True
		message = name + ' field cannot be empty.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def extra_convert(extra_id):

	if extra_id == 0:
		extra_id = None
	else:
		integer(extra_id)

def one(name, value):

	data = {'name': name, 'value': value}

	return (data)

def field(name, value, data=['empty']):


	field = {'name': name, 'value': value}

	if data == ['empty']:
		new_data = []
		new_data.append(field)
		data = new_data
	else:
		data.append(field)

	return (data)

def data_add(name, fields, value='', data=[]):

	option = {'value': value,
				'choice': name,
				'values': fields}

	data.append(option)

	return (data)

def variable(field, data, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	for d in data:
		value = d['value']
		values = d['values']
		choice = d['choice']

		if field == value:
			for val in values:
				v = val['value']
				missing = val['name']
				if v == '':
					message = 'All required ' + choice + ' fields must be complete.'
					error = True
					error_msgs.append(message)
					break
			for val in values:
				v = val['value']
				missing = val['name']
				if v == '':
					message = missing + ' field cannot be empty.'
					error = True
					error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def select(fields, errors):
	error_msgs = errors['error_msgs']
	error = False

	for field in fields:
		name = field['name']
		values = field['values']

		for value in values:
			if value == '':
				error = True
				
		if error:
			message = 'All required ' + name + ' fields.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def together(name, values, errors):

	error_msgs = errors['error_msgs']
	error = False

	for value in values:
		if value == '':
			error = True
				
	if error:
		message = 'If thid power uses ' + name + ', all of those fields must be complete.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def check_fields(check, name, values, errors):

	error_msgs = errors['error_msgs']
	error = False

	if check:
		for value in values:
			if value == '':
				error = True
				
	if error:
		message = 'You must complete all required ' + name + ' fields.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)



def multiple(options, errors):
	error_msgs = errors['error_msgs']
	error = False

	for option in options:
		name = option['name']
		value = option['value']

		if value == '':
			error = True
			message = name + ' field cannot be empty.'
			error_msgs.appwnd(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def of_multiple(values, message, errors):
	error_msgs = errors['error_msgs']
	error = True

	for value in values:
		if value != '' or value == True:
			error = False

	if error:
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def id_check(Table, value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value_id != '':
		try:
			value_id = int(value_id)
		except:
			message = 'Not a valid ' + name
			error_msgs.append(message)	
			error = True
			errors['error'] = True
			errors['error_msgs'] = error_msgs

			return (errors)

		try:
			query = db.session.query(Table).filter_by(id=value_id).one()
		except:
			message = 'Could not find ' + name
			error = True
			error_msgs.append(message) 

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def integer(value):

	if value == 'perm':
		value = 123
	elif value == 'rank':
		value = 121
	elif value == 'any':
		value = 567
	elif value == 'always':
		value = 222
	elif value == 'round':
		value = 333
	elif value == 'extra':
		value = 111
	elif value == 'null':
		value = 444
	elif value == 'normal':
		value = 555
	elif value == 'instant':
		value = 666
	elif value == 'distance':
		value = 777
	elif value == 'vert':
		value = 888
	elif value == 'free':
		value = 999
	elif value == 'result':
		value = 432
	elif value == 'all':
		value = 778
	elif value == 'trait':
		value = 112
	elif value == 'imperv':
		value = 334
	elif value == 'check':
		value = 556
	elif value == 'turn':
		value = 990
	elif value == '':
		value = None
	else:
		try:
			value = int(value)
		except:
			print('not an int')

	return (value)

def int_check(value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	try:
		if value != '':
			value = int(value)
	except:
		error = True
		message = name + ' value must be a number.'
		error_msgs.append
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Check, check_type, 'Check', errors)
	

	return (errors)

def change_action_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	action = data['action']
	mod = data['mod']
	objects = data['objects']
	circumstance = data['circumstance']

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Action, action, 'Action', errors)
	


	return (errors)


def character_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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
	ranks = data['ranks']

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	


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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Range, circ_range, 'range', errors)

	return (errors)

def create_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Complex, complexity, 'complexity', errors)
	errors = id_check(Ability, move_opponent_ability, 'ability', errors)
	


	return (errors)

def damage_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = data['power_id']
	extra_id = data['extra_id']
	trait_type = data['trait_type']
	trait = data['trait']
	mod = data['mod']
	strength = data['strength']
	damage_type = data['damage_type']
	descriptor = data['descriptor']

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Descriptor, damage_type, 'descriptor', errors)
	


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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(PowerLevels, level, 'level', errors)
	


	return (errors)

def defense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	
	errors = id_check(Action, reflect_action, 'Action', errors)
	errors = id_check(Check, reflect_check, 'Check', errors)
	errors = id_check(Descriptor, immunity_damage, 'Descriptor', errors)

	errors = together('a die roll', [roll, outcome], errors)
	errors = check_fields(reflect, 'Reflects Attacks', [reflect_action, reflect_check], errors)

	fields = field('Trait Type', reflect_opposed_trait_type)
	fields = field('Trait', reflect_opposed_trait, fields)
	data = data_add('Opposed Check', fields, 2)
	fields = field('DC', reflect_dc)
	data = data_add('Skill Check', fields, 1, data)
	fields = field('Trait Type', reflect_resist_trait)
	fields = field('Trait', reflect_resist_trait_type, fields)
	data = data_add('Resistance Check', fields, 6, data)

	errors = variable(reflect_check, data, errors)

	errors = check_fields(immunity, 'immunity', [immunity_type], errors)

	fields = []
	data =  []
	fields = field('Trait Type', immunity_trait_type)
	fields = field('Trait', immunity_trait, fields)
	data = data_add('Trait Immunity', fields, 'trait')

	for f in fields:
		print(f)
		print('/n/n/n')

	fields = field('Damage Type', immunity_damage)
	data = data_add('Damage Immunity', fields, 'damage', data)
	fields = field('Descriptor', immunity_descriptor)
	data = data_add('Descriptor Immunity', fields, 'descriptor', data)
	fields = field('Rule', immunity_rule)
	data = data_add('Game Rule Immunity', fields, 'rule', data)

	errors = variable(immunity_type, data, errors)

	errors = check_fields(cover_check, 'cover', [cover_type], errors)

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Math, measure_math, 'math', errors)
	errors = id_check(Rank, measure_rank, 'rank', errors)
	errors = id_check(PowerLevels, level, 'level', errors)

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	

	return (errors)

def environment_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	


	return (errors)

def levels_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	power_id = request.get_json()['power_id']
	extra_id = request.get_json()['extra_id']
	level_type = request.get_json()['level_type']
	level = request.get_json()['level']
	level_effect = request.get_json()['level_effect']

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	

	return (errors)

def minion_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(PowerLevels, attitude_type, 'level', errors)
	errors = id_check(Defense, resitable_check, 'defense', errors)
	


	return (errors)

def mod_post_errors(data):

	errors = {'error': False, 'error_msgs': []}
	
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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Defense, objects_alone, 'defense', errors)
	errors = id_check(Defense, objects_character, 'defense', errors)
	errors = id_check(PowerLevels, limited_level, 'level', errors)
	errors = id_check(Extra, limited_extra, 'extra', errors)
	errors = id_check(Sense, limited_sense, 'sense', errors)
	errors = id_check(Range, limited_range, 'range', errors)
	errors = id_check(PowerLevels, side_level, 'level', errors)
	errors = id_check(Check, reflect_check, 'check', errors)
	
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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Math, distance_math, 'math', errors)
	errors = id_check(Sense, concealment_sense, 'sense', errors)
	errors = id_check(Ground, ground_type, 'ground', errors)
	errors = id_check(Unit, ground_units, 'unit', errors)
	errors = id_check(Check, objects_check, 'check', errors)
	errors = id_check(ConflictAction, objects_attack, 'action', errors)

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Check, player_check, 'check', errors)
	errors = id_check(Check, opponent_check, 'check', errors)

	return (errors)


def ranged_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Unit, flat_units, 'unit', errors)
	errors = id_check(Unit, flat_rank_units, 'unit', errors)
	errors = id_check(Unit, units_rank_units, 'unit', errors)
	errors = id_check(Math, effect_mod_math, 'math', errors)
	errors = id_check(Math, check_math, 'math', errors)
	errors = id_check(Math, trait_math, 'math', errors)
	errors = id_check(Math, distance_mod_math, 'math', errors)


	return (errors)


def resist_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Check, check_type, 'check', errors)
	
	return (errors)

def resisted_by_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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
	damage = data['damage']
	strength = data['strength']
	nullify_descriptor = data['nullify_descriptor']
	nullify_alternate = data['nullify_alternate']
	extra_effort = data['extra_effort']

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(PowerLevels, level, 'level', errors)
	errors = id_check(Defense, nullify_alternate, 'defense', errors)
		


	return (errors)


def reverse_effect_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	


	return (errors)


def sense_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Skill, skill, 'skill', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	errors = id_check(Skill, time_skill, 'skill', errors)
	errors = id_check(Unit, distance_unit, 'unit', errors)

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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = id_check(Extra, extra_id, 'Extra', errors)
	errors = id_check(Unit, units, 'unit', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Check, check_type, 'check', errors)
	


	return (errors)

