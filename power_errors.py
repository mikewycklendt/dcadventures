from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSense, PowerTime 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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

def power(value):
	error_msgs = errors['error_msgs']
	error = False

	if value == '' or value is None:
		error = True
		message = 'You must create a power name first.'
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

def field(name, value, fields=['empty']):


	field = {'name': name, 'value': value}

	if fields == ['empty']:
		new_data = []
		new_data.append(field)
		fields = new_data
	else:
		fields.append(field)

	return (fields)

def variable(name, value, field, fields, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	
	if value == field:
		for val in fields:
			v = val['value']
			if v == '':
				message = 'All required ' + name + ' fields must be complete.'
				error = True
				error_msgs.append(message)
				break
		for val in fields:
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
		name = field['type']
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


def variable_fields(value, name, field, fields, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		for f in fields:
			if f == '':
				error = True
				
		if error:
			message = 'You must enter all required ' + name + ' fields.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def variable_field(value, field, name, f, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f == '':
			error = True
				
	if error:
		message = name + ' field is required.'
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def select_variable(value, field, select, name, f, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f == '':
			error = True
				
	if error:
		message = 'If this effect uses ' + select + ' the ' name + ' field is required.'
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def together(name, values, errors):

	error_msgs = errors['error_msgs']
	error = False

	check = False

	for value in values:
		if value != '':
			check = True

	if check:
		for value in values:
			if value == '':
				error = True
				
	if error:
		message = 'If thid power requires ' + name + ', all of those fields must be complete.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def check_together_var(check, checkname, message, values, errors):

	error_msgs = errors['error_msgs']
	error = True

	if check:
		for value in values:
			for v in value: 
				if v != '' and v is not None and v != False:
					error = False
				else:
					error = True
			if error == False:
				break

	if error:
		message += ' or uncheck the ' + checkname +  ' box.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def together_names(name, names, values, errors):

	error_msgs = errors['error_msgs']
	error = False

	check = False

	for value in values:
		if value != '':
			check = True

	if check:
		for value in values:
			if value == '':
				error = True

	all_names = names[0]
	last_name = len(names) - 1

	if len(names) > 2:
		for i in range(1, len(names) - 1, 1):
			all_names += ', ' + names[i]

	all_names += names[last_name]

	if error:
		message = 'If thid power requires ' + name + ' the ' + names ' fields must be complete.'
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
		message = 'You must complete all required ' + name + ' fields or uncheck the ' + name + ' checkbox.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def check_field(check, checkname, name, value, errors):

	error_msgs = errors['error_msgs']
	error = False

	if check:
		if value == '' or value is None:
				error = True
				
	if error:
		message = name + ' field is required or uncheck the ' + checkname + ' checkbox.'
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

def check_of_multiple(check, name, values, message, errors):
	error_msgs = errors['error_msgs']
	error = True
	complete = False

	if check:
		for value in values:
			for v in value:
				if v != '' or value == True:
					complete = True
				else:
					complete = False
			if complete:
				error = False
	else:
		error = False

	if error:
		message = message + ' or uncheck the ' + name + ' checkbox.' 
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def of_multiple(values, message, errors):
	error_msgs = errors['error_msgs']
	error = True
	complete = False

	for value in values:
		for v in value:
			if v != '' or value == True:
				complete = True
			else:
				complete = False
		if complete:
			error = False

	if error:
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def check_of(check, name, values, errors):
	error_msgs = errors['error_msgs']
	error = True
	sub_error = False

	if check:
		for value in values:
			if value != '' or value == True:
				error = False
	else:
		error = False

	if error:
		message = 'You must select one of the required ' + name + ' options or uncheck the ' + name + ' checkbox.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def of(values, message, errors):
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

def select_of(value, selected_name, field_name, field, values, names, errors):
	error_msgs = errors['error_msgs']
	error = True

	if value == field:
		for value in values:
			if value != '' or value == True:
				error = False

	last = len(names) - 1
	for_message = names[0]
	if len(names) > 2:
		for i in range(1, len(names) - 1, 1):
			for_message += ', ' + names[i]
		for_message += ' or ' + names[last]

	message = 'If this effect ' + selected_name + ', you must complete one of the ' + for_message + ' fields or make a different selection in the ' + field_name + ' field.'

	if error:
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def id_check(Table, value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	db = SQLAlchemy()

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

def extra_check(value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	db = SQLAlchemy()

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

		if value_id == 0:
			return (errors)

		try:
			query = db.session.query(Extra).filter_by(id=value_id).one()
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
		if value != '' and value != 'perm' and value != 'rank' and value != 'any' and value != 'always' and value != 'round' and value != 'extra' and value != 'null' and value != 'normal' and value != 'instant' and value != 'distance' and value != 'vert' and value != 'free' and value != 'result' and value != 'all' and value != 'trait' and value != 'imperv' and value != 'check' and value != 'turn' and value is not None:
			value = int(value)
	except:
		error = True
		message = name + ' value is not valid.'
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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)

	errors = int_check(value, 'Increased By', errors)
	errors = int_check(increase, 'Per Rank', errors)
	errors = int_check(reduced_value, 'Reduced', errors)
	errors = int_check(carry_capacity, 'Carry Capacity', errors)
	errors = int_check(points_value, 'Points', errors)
	errors = int_check(cost, 'Cost', errors)
	errors = int_check(ranks, 'Ranks', errors)

	errors = together('an Increased Trait', [trait_type, value, increase], errors)
	errors = check_field(limited, 'Limited', 'Limited By', limited_by, errors)
	errors = variable_fields('emotion', 'Emotional State', limited_by, [emotion], errors)
	errors = variable_fields('other', 'Other Condition', limited_by, [other], errors)

	errors = check_fields(reduced, 'Reduced Trait', [reduced_trait_type, reduced_value], errors)
	errors = check_field(reduced, 'Reduced Trait', 'Reduced Trait Type', reduced_trait_type, errors)
	errors = check_field(reduced, 'Reduced Trait', 'Reduced By Value', reduced_value, errors)
	errors = variable_fields('ability', 'Reduced Ability', reduced_trait_type, [reduced_trait], errors)
	errors = variable_field('ability', reduced_trait_type, 'Ability', reduced_trait, errors)
	errors = variable_fields('defense', 'Reduced Defense', reduced_trait_type, [reduced_trait], errors)
	errors = variable_fields('defense', reduced_trait_type, 'Defense', reduced_trait, errors)

	errors = check_of(limbs, 'Extra Limbs', [limbs_continuous, limbs_sustained, limbs_distracting, limbs_projection], errors)
	errors = check_field(carry, 'Extra Carry', 'Carry Capacity', carry_capacity, errors)
	errors = check_fields(points, 'Hero Points', [points_value, points_trait_type, points_trait])
	errors = check_field(points, 'Hero Points', 'Points Value', points_value, errors)
	errors = check_field(points, 'Hero Points', 'Trait Type', points_trait_type, errors)
	errors = check_field(points, 'Hero Points', 'Trait', points_trait, errors)

	errors = check_fields(appear, 'Alters Appearance', [appear_target, appear_description], errors)
	errors = check_field(appear, 'Alters Appearance', 'Target', appear_target, errors)
	errors = check_field(appear, 'Alters Appearance', 'Description', appear_description, errors)

	errors = check_fields(insubstantial, 'Insubstantial', [insub_type, insub_description], errors)
	errors = check_field(insubstantial, 'Insubstantial', 'Insubstantial Type', insub_type, errors)
	errors = check_field(insubstantial, 'Insubstantial', 'Insubstantial Description', insub_description, errors)

	errors = check_fields(weaken, 'Weaken', [weaken_type], errors)
	errors = check_field(weaken, 'Weaken', 'Weaken Type', weaken_type, errors)
	errors = variable_fields()

	errors = variable_fields('trait', 'Specific', weaken_type, [weaken_trait_type, weaken_trait], errors)
	errors = variable_field('trait', weaken_type, 'Trait Type', weaken_trait_type, errors)
	errors = variable_field('trait', weaken_type, 'Trait', weaken_trait, errors) 
	errors = variable_fields('type', weaken_type, 'Broad Trait', [weaken_broad], errors)
	errors = variable_field('type', weaken_type, 'Broad Trait Type', weaken_broad, errors)
	errors = variable_fields('descriptor', 'Broad Descriptor', weaken_type, [weaken_descriptor], errors)
	errors = variable_field('descriptor', weaken_type, 'Descriptor', weaken_descriptor, errors)












	


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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Range, circ_range, 'range', errors)

	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)

	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Rounds', errors)
	errors = required(target, 'Targwt', errors)
	errors = required(description, 'Circumstance', errors)

	errors = variable_fields()

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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Complex, complexity, 'complexity', errors)
	errors = id_check(Ability, move_opponent_ability, 'ability', errors)

	errors = int_check(volume, 'Volume', errors)
	errors = int_check(toughness, 'Toughness', errors)
	errors = int_check(mass, 'Mass', errors)
	errors = int_check(transform_start_mass, 'Transform Starting Mass', errors)
	errors = int_check(transfom_mass, 'Transform Ending Mass', errors)
	errors = int_check(move_opponent_rank, 'Rank for Opponent to Move', errors)
	errors = int_check(trap_dc, 'Trap DC', errors)
	errors = int_check(trap_resist_dc, 'Trap Resistance DC', errors)
	errors = int_check(ranged_dc, 'Ranged DC', errors)
	errors = int_check(ranged_damage_value, 'Ranged Damage Value', errors)
	errors = int_check(weapon_mod, 'Weapon Modifier', errors)
	errors = int_check(weapon_damage, 'Weapon Damage', errors)
	errors = int_check(support_strength, 'Support Strength Rank', errors)
	errors = int_check(support_action, 'Strengthen With Action Modifier', errors)
	errors = int_check(support_action_rounds, 'Strengthen with Action Number of Rounds', errors)
	errors = int_check(support_effort, 'Strengthen with Extra Effort Bonus', errors)
	errors = int_check(support_effort_rounds, 'Strengthen with Extra Effort Number of Rounds', errors)
	errors = int_check(cost, 'Cost', errors)
	errors = int_check(ranks, 'Ranks', errors)

	errors = together_names('Creating an object', ['Solidity', 'Visibility', 'Complexity', 'Volume Rank', 'Toughness', 'Mass Rank'], [solidity, visibility, complexity, volume, toughness, mass], errors)
	errors = check_fields(moveable, 'Moveable', [move_player], errors)
	errors = check_field(moveable, 'Moveable', 'Moveable With', move_player, errors)
	errors = select_variable('ability', move_player, 'an Ability', 'Trait',  errors)
	errors = select_variable('skill', move_player, 'a Skill', 'Trait',  errors)
	errors = select_variable('bonus', move_player, 'an Enhanced Skill', 'Trait',  errors)
	errors = select_variable('defense', move_player, 'a Defense', 'Trait',  errors)
	errors = select_variable('power', move_player, 'a Power', 'Trait',  errors)
	errors = check_fields(move_opponent_check, 'Opponent Can Move the Object', [move_opponent_ability, move_opponent_rank, errors], errors)
	errors = check_field(move_opponent_check, 'Opponent Can Move the Object', 'Ability', move_opponent_ability, errors)
	errors = check_field(move_opponent_check, 'Opponent Can Move the Object', 'Rank', move_opponent_rank, errors)
	errors = check_fields(stationary, 'Stationary', [move_player], errors)
	errors = check_field(stationary, 'Stationary', 'Moveable With', move_player, errors)
	
	errors = check_fields(trap, 'Trap', [trap_type, trap_resist_check, trap_resist_trait, trap_resist_dc], errors)
	errors = check_field(trap, 'Trap', 'Trap Check Type', trap_type, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance Trait Type', trap_type trap_resist_check, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance Trait', trap_resist_trait, errors)
	errors = check_field(trap, 'Trap', 'Trap Resistance DC' trap_resist_dc], errors)
	errors = variable_fields('dc', 'Trap DC', trap_type, [trap_dc], errors)
	errors = variable_fields('trait', 'Trap Check Against Trait', trap_type, [trap_trait_type, trap_trait], errors)
	errors = variable_field('trait', trap_type, 'Trap Check Against Trait Type', trap_trait_type, errors)
	errors = variable_field('trait', trap_type, 'Trap Check Against Trait', trap_trait, errors)

	errors = check_fields(ranged, 'Ranged Attack', [ranged_type, ranged_damage_type], errors)
	errors = check_field(ranged, 'Ranged Attack', 'Ranged Check Type', ranged_type, errors)
	errors = check_field(ranged, 'Ranged Attack', 'Ranged Damage Type', ranged_damage_type, errors)
	errors = variable_fields('dc', 'Ranged DC', ranged_type, [ranged_dc], errors)
	errors = variable_fields('target', 'Ranged Target Trait', ranged_type, [ranged_trait_type, ranged_trait], errors)
	errors = variable_fields('player', 'Ranged Player Trait', ranged_type, [ranged_trait_type, ranged_trait], errors)
	errors = variable_field('target', ranged_type, 'Ranged Target Trait Type', ranged_trait_type, errors)
	errors = variable_field('target', ranged_type, 'Ranged Target Trait', ranged_trait, errors)
	errors = variable_field('player', ranged_type, 'Ranged Player Trait Type', ranged_trait_type, errors)
	errors = variable_field('player', ranged_type, 'Ranged Player Trait', ranged_trait, errors)
	errors = variable_fields('value', 'Ranged Damage Value', ranged_damage_type, [ranged_damage_value], errors)

	errors = check_fields(weapon, 'Weapon', [weapon_trait_type, weapon_trait, weapon_mod, weapon_damage_type], errors)
	errors = check_field(weapon, 'Weapon', 'Weapon Trait Type', weapon_trait_type, errors)
	errors = check_field(weapon, 'Weapon', 'Wespon Trait', weapon_trait, errors)
	errors = check_fields(weapon, 'Weapon', 'Weapon Modifier', weapon_mod, errors)
	errors = check_fields(weapon, 'Weapon', 'Weapon Damage Type', weapon_damage_type, errors)
	errors = variable_fields('value', 'Weapon Damage Value', weapon_damage_type, [weapon_damage], errors)

	errors = check_fields(support, 'Supports Weight', [support_strength], errors)
	errors = check_field(support, 'Supports Weight', 'Supports Weight Strength Rank', support_strength, errors)
	errors = check_together_var(support_strengthen, 'Suupports Weight and Can Strengthen', 'Complete the action fields or extra effort fields (or all)', [[support_action, support_action_rounds], [support_effort, support_effort_rounds]], errors)

	errors = check_fields(transform, 'Transform', [transform_type, transform_start_mass, transfom_mass], errors)
	errors = check_field(transform, 'Transform', 'Transform Type', errors)
	errors = check_field(transform, 'Transform', 'Transform Starting Mass', transform_start_mass, errors)
	errors = check_field(transform, 'Transform', 'Transform Ending Mass', transfom_mass, errors)

	errors = together('a Transform Descriptor', [transform_start_descriptor, transform_end_descriptor], errors)

	
	
	


	


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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)

	print('\n\n\n\n\n')
	print(reflect_action)
	
	errors = id_check(Action, reflect_action, 'Action', errors)

	print(reflect_check)
	errors = id_check(Check, reflect_check, 'Check', errors)
	errors = id_check(Descriptor, immunity_damage, 'Descriptor', errors)

	errors = together('a die roll', [roll, outcome], errors)
	errors = check_fields(reflect, 'Reflects Attacks', [reflect_action, reflect_check], errors)
	errors = check_field(reflect, 'Reflects Attacks', 'Reflect Action Type', reflect_action, errors)
	errors = check_field(reflect, 'Reflects Attacks', 'Reflect Check Type', reflect_check, errors)

	value = reflect_check
	fields = field('Trait Type', reflect_opposed_trait_type)
	fields = field('Trait', reflect_opposed_trait, fields)
	errors = variable('Opposed Check', '2', value, fields, errors)
	fields = field('DC', reflect_dc)
	errors = variable('Skill Check', '1', value, fields, errors)
	fields = field('Trait Type', reflect_resist_trait)
	fields = field('Trait', reflect_resist_trait_type, fields)
	errors = variable('Resistance Check', '6', value, fields, errors)

	errors = check_fields(immunity, 'immunity', [immunity_type], errors)

	value = immunity_type
	fields = field('Trait Type', immunity_trait_type)
	fields = field('Trait', immunity_trait, fields)
	errors = variable('Trait Immunity', 'trait', value, fields, errors)
	fields = field('Damage Type', immunity_damage)
	errors = variable('Damage Immunity', 'damage', value, fields, errors)
	fields = field('Descriptor', immunity_descriptor)
	errors = variable('Descriptor Immunity', 'descriptor', value, fields, errors)
	fields = field('Rule', immunity_rule)
	errors = variable('Game Rule Immunity', 'rule', value, fields, errors)

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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
	

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
	errors = extra_check(extra_id, 'Extra', errors)
	


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
	errors = extra_check(extra_id, 'Extra', errors)

	errors = required(level_type, 'Level Type', errors)
	errors = required(level, 'Level', errors)
	errors = required(level_effect, 'Level Effect', errors)
	

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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Math, distance_math, 'math', errors)
	errors = id_check(Sense, concealment_sense, 'sense', errors)
	errors = id_check(Ground, ground_type, 'ground', errors)
	errors = id_check(Unit, ground_units, 'unit', errors)
	errors = id_check(Check, objects_check, 'check', errors)
	errors = id_check(ConflictAction, objects_attack, 'action', errors)

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
	check_field = check_field(aquatic, 'Aquatic Type','Aquatic', acquatic_type, errors)

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
	errors - variable_fields('1', 'Move Objects Skill Check', objects_check, [objects_skill_type, objects_skill], errors)
	errors = variable_field('1', objects_check, 'Move Objects Skill Tyoe', objects_skill_type, errors)
	errors = variable_field('1', objects_check, 'Move Objects Skill', objects_skill, errors)
	errors - variable_fields('5', 'Move Objects Attack Check', objects_check, [objects_attack], errors)
	errors = variable_field('5', objects_check, 'Move Objects Attack Check Type', objects_attack, errors)
	errors = check_fields(objects_damage, 'Move Objects Damage Inflict', [damage_type], errors)
	errors = check_field(objects_damage, 'Move Objects Damage Inflict', 'Damage Dealt By', damage_type, errors)

	errors = check_fields(permeate, 'Permeate', [permeate_type, permeate_speed], errors)
	errors = check_field(permeate, 'Permeate', 'Permeate Type', permeate_type, errors)
	errors = check_fields(permeate, 'Permeate', 'Permeate Speed Rank Modifier', permeate_speed, errors)

	errors = check_fields(special, 'Special Travel', [special_type], errors)
	errors = variable_fields('dimension', 'Dimension Travel', special_type, [dimension_type, dimension_mass_rank], errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Type', dimension_type, errors)
	errors = variable_field('dimension', special_type, 'Dimension Travel Carry Mass', dimension_mass_rank, errors)
	errors - variable_fields('descriptor', 'Dimension Descriptor', dimension_type, [dimension_descriptor], errors)
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

	errors = id_check(Power, power_id, 'Power', errors)
	errors = required(extra_id, 'Extra', errors)
	errors = extra_check(extra_id, 'Extra', errors)
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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Unit, flat_units, 'unit', errors)
	errors = id_check(Unit, flat_rank_units, 'unit', errors)
	errors = id_check(Unit, units_rank_units, 'unit', errors)
	errors = id_check(Math, effect_mod_math, 'math', errors)
	errors = id_check(Math, check_math, 'math', errors)
	errors = id_check(Math, trait_math, 'math', errors)
	errors = id_check(Math, distance_mod_math, 'math', errors)

	flat_value = integer(flat_value)
	flat_rank = integer(flat_rank)
	flat_rank_value = integer(flat_rank_value)
	flat_rank_units = integer(flat_rank_units)
	flat_rank_rank = integer(flat_rank_rank)
	flat_rank_distance = integer(flat_rank_distance)
	flat_rank_distance_rank = integer(flat_rank_distance_rank)
	integer(units_rank_start_value)
	integer(units_rank_value)
	integer(units_rank_rank)
	integer(rank_distance_start)
	integer(rank_distance)
	integer(rank_effect_rank)
	integer(effect_mod)
	integer(check_mod)
	integer(trait_mod)
	integer(distance_mod_rank)
	integer(dc_value)
	

	errors = int_check(flat_value, 'Flat Value', errors)
	errors = int_check(flat_rank, 'Rank', errors)
	errors = int_check(flat_rank_value, 'Value', errors)
	errors = int_check(flat_rank_rank, 'Rank', errors)
	errors = int_check(flat_rank_distance, 'Distance', errors)
	errors = int_check(flat_rank_distance_rank, 'Rank', errors)
	errors = int_check(units_rank_start_value, 'Start Value', errors)
	errors = int_check(units_rank_value, 'Value', errors)
	errors = int_check(units_rank_rank, 'Rank', errors)
	errors = int_check(rank_distance_start, 'Start Distance', errors)
	errors = int_check(rank_distance, 'Distance', errors)
	errors = int_check(rank_effect_rank, 'Rank', errors)
	errors = int_check(effect_mod, 'Mod Value', errors)
	errors = int_check(check_mod, 'Mod Value', errors)
	errors = int_check(trait_mod, 'Mod Value', errors)
	errors = int_check(distance_mod_rank, 'Rank', errors)
	errors = int_check(dc_value, 'DC Value', errors)

	errors = check_fields(dc, 'DC', [dc_value, dc_trait_type, dc_trait], errors)
	errors - check_field(dc, 'DC', 'DC', dc_value, errors)
	errors - check_field(dc, 'Trait Type', 'DC', dc_trait_type, errors)
	errors - check_field(dc, 'Trait', 'DC', dc_trait, errors)
	
	errors = variable(range_type, 'flat_units', 'Flat Units', [{'value': flat_value, 'name': 'Distanve'}, {'value': flat_units, 'name': 'Unita'}], errors)
	errors = variable(range_type, 'distance_rank', 'Flat Distance Rank', [{'value': flat_rank, 'name': 'Distance Rank'}], errors)
	errors = variable(range_type, 'flat_rank_units', 'Flat Units By Rank', [{'value': flat_rank_value, 'name': 'Distance'}, {'value': flat_rank_units, 'name': 'Units'}, {'value': flat_rank_rank, 'name': 'Rank'}], errors)
	errors = variable(range_type, 'flat_rank_distance', 'Flat Distance Rank By Rank', [{'value': flat_rank_distance, 'name': 'Distance Rank'}, {'value': flat_rank_distance_rank, 'name': 'Effect Rank'}], errors)
	errors = variable(range_type, 'units_rank', 'Units Per Rank', [{'value': units_rank_start_value, 'name': 'Starting Distance'}, {'value': units_rank_value, 'name': 'Distance'}, {'value': units_rank_units, 'name': 'Units'}, {'value': units_rank_rank, 'name': 'Effect Rank'}], errors)
	errors = variable(range_type, 'rank_rank', 'Distance Rank Per Rank', [{'value': rank_distance_start, 'name': 'Starting Distance'}, {'value': rank_distance, 'name': 'Distance Rank'}, {'value': rank_effect_rank, 'name': 'Effect Rank'}], errors)
	errors = variable(range_type, 'effect_mod', 'Effect Rank Modifier', [{'value': effect_mod_math, 'name': 'Math'}, {'value': effect_mod, 'name': 'Modifier'}], errors)
	errors = variable(range_type, 'trait_mod', 'Trait Rank Modifier', [{'value': check_trait_type, 'name': 'Trait Type'}, {'value': check_trait, 'name': 'Trait'}, {'value': check_math, 'name': 'Math'}, {'value': check_mod, 'name': 'Modifier'}], errors)
	errors = variable(range_type, 'distance_mod', 'Distance Rank Modifier', [{'value': trait_trait_type, 'name': 'Trait Type'}, {'value': trait_trait, 'name': 'Trait'}, {'value': trait_math, 'name': 'Math'}, {'value': trait_mod, 'name': 'Modifier'}], errors)
	errors = variable(range_type, 'check', 'Check Result', [{'value': distance_mod_rank, 'name': 'Distance'}, {'value': distance_mod_math, 'name': 'Math'}, {'value': distance_mod_trait_type, 'name': 'Trait Type'}, {'value': distance_mod_trait, 'name': 'Trait'}], errors)




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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Check, check_type, 'check', errors)
	
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(rounds, 'Rounds', errors)
	
	errors = required(mod, 'Modifier', errors)
	errors = required(rounds, 'Rounds', errors)
	errors = required(circumstance, 'Circumstance', errors)
	errors = required(target, 'Target', errors)

	errors = variable_fields('descriptor', 'Descriptor', resist_check_type, [descriptor], errors)
	errors = variable_fields('trait', 'Check Type', resist_check_type, [check_trait_type, check_trait], errors)
	errors = variable_field('trait', resist_check_type, 'Trait Type', check_trait_type, errors)
	errors = variable_field('trait', resist_check_type, 'Trait', check_trait, errors)
	errors = check_fields(requires_check, 'Requires Check', [check_type, check_trait_type, check_trait], errors)
	errors = check_field(requires_check, 'Requires Check', 'Check Type', check_type, errors)
	errors = check_fields(requires_check, 'Requires Check', 'Check Trait Type', check_trait_type, errors)
	errors = check_fields(requires_check, 'Requires Check', 'Check Trait', check_trait, errors)


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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(PowerLevels, level, 'level', errors)
	errors = id_check(Defense, nullify_alternate, 'defense', errors)

	errors = int_check(dc, 'DC', errors)
	errors = int_check(mod, 'Modifier', errors)
	errors = int_check(degree, 'Degree', errors)
	errors = int_check(weaken_max, 'Weaken Maximum', errors)
	errors = int_check(weaken_restored, 'Weaken Restored', errors)
	errors = int_check(damage, 'Damage', errors)

	errors = required(dc, 'DC', errors)
	errors = required(mod, 'Modifier', errors)
	errors = required(description, 'Circumstance', errors)
	errors = required(trait_type, 'Resisted by Trait Type', errors)
	errors = required(trait, 'Resisted by Trait', errors)
	errors = required(degree, 'Degree', errors)

	errors = variable_fields('condition', 'Condition', effect, [condition1, condition2], errors)
	errors = variable_field('condition', effect, 'Starting Condition', condition1, errors)
	errors = variable_field('condition', effect, 'Ending Condition', condition2, errors) 
	errors = variable_fields('damage', 'Damage', effect, [damage], errors) 
	errors = variable_field('damage', effect, 'Damage Type', damage, errors)
	errors = select_of('nullify', 'Nullifies an Opponent Effect', 'Effect Type', effect, [nullify_descriptor, nullify_alternate], ['Nullified by Descriptor', 'Alternate Resistance'], errors)
	errors = variable_fields('trait', 'Weakened Trait', effect, [weaken_max, weaken_restored], errors)
	errors = variable_field('trait', effect, 'Maximum Lost Points', weaken_max, errors)
	errors = variable_field('trait', effect, 'Restored Points Rate', weaken_restored, errors)
	errors = variable_fields('level', 'Level', effect, [level], errors)

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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	
	errors = int_check(degree, 'Degree', errors)
	errors = int_check(value_dc, 'DC', errors)
	errors = int_check(math_dc, 'DC', errors)
	errors = int_check(time_value, 'Time', errors)

	errors = required(degree, 'Degree', errors)
	errors = required(when, 'When', errors)
	errors = required(target, 'Target', errors)

	errors = of([check_check, time_check], 'You must choose if this effect is reversed by a check or time or both', errors)
	errors = check_fields(check_check, 'Reversed by Check', [trait_type, trait, value_type], errors)
	errors = check_field(check_check, 'Reversed by Check', 'Trait Type', trait_type, errors)
	errors = check_field(check_check, 'Reversed by Check', 'Trait', trait, errors)
	errors = check_field(check_check, 'Reversed by Check', 'DC Type', value_type, errors)
	errors = variable_fields('value', 'DC Value', value_type, [value_dc], errors)
	errors = variable_fields('math', 'DC Math', value_type, [math_dc, math], errors)
	errors = variable_fields('math', value_type, 'DC', math_dc, errors)
	errors = variable_fields('math', value_type, ' Math', math, errors)
	errors = check_fields(time_check, 'Reversed by Time', [time_value, time_unit], errors)
	errors = check_fields(time_check, 'Reversed by Time', 'Time', time_value, errors)
	errors = check_fields(time_check, 'Reversed by Time', 'Time Units', time_unit, errors)

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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Skill, skill, 'skill', errors)
	errors = id_check(Unit, time_unit, 'unit', errors)
	errors = id_check(Skill, time_skill, 'skill', errors)
	errors = id_check(Unit, distance_unit, 'unit', errors)

	errors = int_check(sense_cost, 'Sense Cost', errors)
	errors = int_check(subsense_cost, 'Subsense Cost', errors)
	errors = int_check(resist_circ, 'Resistance Circumstance Modifier', errors)
	errors = int_check(time_value, 'Time', errors)
	errors = int_check(time_factor, 'Time Factor', errors)
	errors = int_check(distance_dc, 'Distance DC', errors)
	errors = int_check(distance_mod, 'Distance Modifier', errors)
	errors = int_check(distance_value, 'Distance', errors)
	errors = int_check(distance_factor, 'Distance Factor', errors)
	errors = int_check(ranks, 'Ranks', errors)
	errors = int_check(cost, 'Cost', errors)

	errors = required(sense, 'Sense', errors)
	errors = required(sense_type, 'Sense Effect Type')
	errors = required(target, 'Target', errors)

	errors = variable_fields('height', 'Heightened Sense', sense_type, [height_trait_type, height_trait], errors)
	errors = variable_field('height', sense_type, 'Heightened Sense Trait Type', height_trait_type, errors)
	errors = variable_field('height', sense_type, 'Heightened Sense Trait', height_trait, errors)
	errors = check_field(height_power_required, 'Needs Sense Power', 'Enhanced Sense', height_ensense, errors)
	errors = variable_fields('resist', 'Resistant Sense', sense_type, [resist_trait_type, resist_trait], errors)
	errors = variable_field('resist', sense_type, 'Resistant Trait Type', resist_trait_type, errors)
	errors = variable_field('resist', sense_type, 'Resistant Trait', resist_trait, errors)
	errors = check_field(resist_immune, 'Immunity', 'Immunity Type', resist_permanent, errors)
	errors = check_field(dark, 'Counters Darkness', 'Darkness Type', lighting, errors)
	errors = check_field(time, 'Time Effect', 'Time Set By', time_set, errors)
	errors = variable_fields('value', 'Time Set by Value', time_set, [time_value, time_unit], errors)
	errors = variable_field('value', time_set, 'Value', time_value, errors)
	errors = variable_field('value', time_set, 'Units', time_unit, errors)
	errors = variable_fields('skill', 'Time Set by Skill', time_set, [time_skill], errors)
	errors = variable_field('skill', time_set, 'Skill', time_skill, errors)
	errors = variable_fields('bonus', 'Time Set by Enhanced Skill', time_set, [time_bonus], errors)
	errors = variable_field('bonus', time_set, 'Enhanced Skill', time_bonus, errors)
	errors = check_field(dimensional, 'Dimensional', 'Dimensional Type', dimensional_type, errors)




	

	



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
	errors = extra_check(extra_id, 'Extra', errors)
	errors = id_check(Unit, units, 'unit', errors)
	errors = id_check(Math, math, 'math', errors)
	errors = id_check(Check, check_type, 'check', errors)
	


	return (errors)

