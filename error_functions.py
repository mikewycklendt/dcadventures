from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

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

def power_check(value, errors):
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

def rule_check(check, name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule = db.session.query(table).filter_by(power_id = power).first()

	if check:
		if rule is None:
			error = True
			message = 'You must create a ' + name + ' rule or uncheck the ' + name + ' checkbox.'
			error_msgs.append(message)
	else:
		if rule is not None:
			error = True
			message = 'Delete the ' + name + ' rules you created or check the ' + name + ' checkbox.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def rule_select(value, field, name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field == value:
		rule = db.session.query(table).filter_by(power_id = power).first()

		if rule is None:
			message = 'If this rule has a ' + name + ' effect, you must add ' + name + ' rules for it.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def cost_check(check, name, field, table, power, errors, values='e'):
	error_msgs = errors['error_msgs']
	error = False

	rule_check = db.session.query(table).filter_by(power_id=power).first()

	if rule_check is not None:
		if field != 'x':
			cost_check = db.session.query(table).filter_by(power_id=power, extra_id=None).all()
			for c in cost_check:
				if c.cost is not None:
					error = True
					message = 'You set a rule for a ' + name + ' that has a cost of its own but you set a cost for the base power.  If you want to set a different cost for this rule you must set the base power cost to variable.'
					error_msgs.append(message)
		else:
			cost_check = db.session.query(table).filter_by(power_id=power, extra_id=None).all()
			for c in cost_check:
				if c.cost is None:
					error = True
					message = 'You set a variable cost for this power, so you must delete and recreate the ' + name + ' rule and specify the cost or set a cost for the base power.'
					error_msgs.append(message)
				
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def extra_cost(name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule_check = db.session.query(table).filter_by(power_id=power).first()

	if rule_check is not None:
		cost_check = db.session.query(table).filter_by(power_id=power).all() 
		for c in cost_check:
			extra_id = c.extra_id
			if extra_id is not None:
				extra_check = db.session.query(Extra).filter_by(id=extra_id).first()	
				if extra_check is not None:
					if extra_check.cost is not None:
						if c.cost is not None:
							error = True
							message = 'You set a rule for a ' + name + ' effect that was assigned to the ' + extra_check.name + ' extra that has its own cost.  If you want to set an alternate cost for this rule it cannot be assigned to this extra or you can delete the extra and recreate it, this time setting a variable cost for the extra and delete and recreate the rule and setting it to the recreated extra with its variable cost.'
							error_msgs.append(message)
					else:
						if c.cost is None:
							error = True
							message = 'You set a variable cost for the ' + extra_check.name + ' extra and created a ' + name + ' rule was assigned to i, so you must delete and recreate the ' + name + ' rule for that extra and specify the cost.'
							error_msgs.append(message)
				
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

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

def if_fields(name, field, fields, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field == '':
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

def if_field(main, field, select, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field == '':
		return (errors)
	
	if select == '':
		error = True
		message = 'If this rule involves a ' + main + ', the ' + name + ' field is required.'
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
		message = 'If this effect uses ' + select + ' the ' + name + ' field is required.'
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
	error = False
	
	if check:
		error = True
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
		message = 'If thid power requires ' + name + ' the'
		for n in names:
			message += ' ' + n
		message += ' fields must be complete.'
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

	if value != field:
		return (errors)

	if value == field:
		for v in values:
			if v != '' or v == True:
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

def db_check(Table, value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	db = SQLAlchemy()

	if value_id != '' and value_id != '0' and value_id != 'x' and value_id != 'other':
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
	elif value == 'degree':
		value = 211
	elif value == 'scene':
		value = 322
	elif value == 'auto':
		value = 433
	elif value == 'advantage':
		value = 544
	elif value == 'bonus':
		value = 655
	elif value == 'immune':
		value = 766
	elif value == 'penalty':
		value = 877
	elif value == 'double':
		value = 988
	elif value == 'flat':
		value = 998
	elif value == 'x':
		value = 1234
	elif value == '':
		value = None
	else:
		try:
			value = int(value)
		except:
			print('not an int')
			print(value)

	return (value)

def extra_convert(extra_id):

	if extra_id == '0':
		extra_id = None
	else:
		integer(extra_id)

	return (extra_id)

def int_check(value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	try:
		if value != 'perm' and value != 'rank' and value != 'any' and value != 'always' and value != 'round' and value != 'extra' and value != 'null' and value != 'normal' and value != 'instant' and value != 'distance' and value != 'vert' and value != 'free' and value != 'result' and value != 'all' and value != 'trait' and value != 'imperv' and value != 'check' and value != 'turn' and value != 'degree' and value != 'scene' and value != 'auto' and value != 'advantage' and value != 'bonus' and value != 'immune' and value != 'penalty' and value != 'double' and value != 'flat' and value != 'x' and value != '':
			value = int(value)
	except:
		error = True
		message = name + ' value is not valid.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

	

def db_integer(value):

	if value == '0' or value == 'x':
		value = None

	return (value)

