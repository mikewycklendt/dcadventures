
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def integer(value):

	if value == 'perm':
		value = 123123
	elif value == 'rank':
		value = 121121
	elif value == 'any':
		value = 567567
	elif value == 'always':
		value = 222222
	elif value == 'round':
		value = 333333
	elif value == 'extra':
		value = 111111
	elif value == 'null':
		value = 444444
	elif value == 'normal':
		value = 555555
	elif value == 'instant':
		value = 666666
	elif value == 'distance':
		value = 777777
	elif value == 'vert':
		value = 888888
	elif value == 'free':
		value = 999999
	elif value == 'result':
		value = 432432
	elif value == 'all':
		value = 778778
	elif value == 'trait':
		value = 112112
	elif value == 'imperv':
		value = 334334
	elif value == 'check':
		value = 556556
	elif value == 'turn':
		value = 990990
	elif value == 'degree':
		value = 211211
	elif value == 'scene':
		value = 322322
	elif value == 'auto':
		value = 433433
	elif value == 'advantage':
		value = 544544
	elif value == 'bonus':
		value = 655655
	elif value == 'immune':
		value = 766766
	elif value == 'penalty':
		value = 877877
	elif value == 'double':
		value = 988988
	elif value == 'flat':
		value = 998998
	elif value == 'x':
		value = 12341234
	elif value == 'skill':
		value = 23452345
	elif value == 'parent':
		value = 34563456
	elif value == 'speed':
		value = 45674567
	elif value == 'unlimited':
		value = 56785678
	elif value == 'gm':
		value = 67896789
	elif value == 'fail':
		value = 987987
	elif value == 'success':
		value = 876876
	elif value == 'routine':
		value = 765765
	elif value == '':
		value = None
	elif value == 'none':
		value = None
	else:
		try:
			value = int(value)
		except:
			print('not an int')
			print(value)

	return (value)

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

def required_keyword(value, form, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value == '':
		error = True
		message = 'If you wsnt to create ' + form + ', tou must set the ' + name  + ' settings first.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def required_if_any(value, name, field, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		if field == '':
			error = True
			message = name + ' is required.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def no_zero(value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value == '0' or value == 0:
		error = True
		message = 'You did not set a ' + name + ' value.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def required_multiple(field, values, value_field, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	check = False

	for value in values:
		if value == value_field:
			check = True

	if check == False:
		return (errors)

	if field == '':
		error = True
		message = name + ' field is required.'
		error_msgs.append(message)

	if error:
		errors['error_msgs'] = error_msgs
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
		message = 'If this effect involves a ' + main + ', the ' + name + ' field is required.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def if_or(main, field, selects, names, errors):
	error_msgs = errors['error_msgs']
	error = True

	if field == '':
		return (errors)
	
	for select in selects:
		if select != '' :
			error = False

	message = 'If this effect involves a ' + main + ', the ' + names + ' field is required.'		
	if error:
		errors['error'] = error
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
	
	return (errors)

def seperate(selects, names, errors):
	error_msgs = errors['error_msgs']
	error = False

	i = 0
	
	for select in selects:
		if select != '' :
			i += 1

	if i > 1:			
		error = True
		message = 'You can only choose one of ' + names + ' fields at once.'		
	if error:
		errors['error'] = error
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
	
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
	
def variable_field_linked(value, field, f, name, form, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f == '':
			error = True
				
	if error:
		message = 'If this rule uses a ' name + ' you must set the ' + form ' settings first.'
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
		message = 'If thid effect requires ' + name + ', all of those fields must be complete.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def dependent(name, value, values, errors):

	error_msgs = errors['error_msgs']
	error = False

	check = False

	if value == '':
		return (errors)

	for value in values:
		if value == '':
			error = True
				
	if error:
		message = 'All  required ' + name + ' fields must be complete.'
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

	all_names = ''

	if error:
		message = 'If this effect requires ' + name + ' the '
		for n in names:
			if all_names == '':
				all_names = n
				end_message = n + ' field is required'
			else:
				all_names += ' and ' + n
				end_message += all_names + ' fields must be complete.'
		if len(values) > 2:
			message += end_message
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
		if value != '' and value != False:
			error = False

	if error:
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def either(values, message, errors):
	error_msgs = errors['error_msgs']
	error = False
	together = False

	for value in values:
		if together == True and value != '':
			error = True
		if value != '':
			together = True

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

	if value_id == '':
		return (errors)
	if value_id == 'base':
		return (errors)
	elif value_id == 'all':
		query = db.session.query(table).filter_by(all=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'current':
		query = db.session.query(table).filter_by(current=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'any':
		query = db.session.query(table).filter_by(any=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'x':
		query = db.session.query(table).filter_by(var=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'none':
		query = db.session.query(table).filter_by(none=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'power':
		query = db.session.query(table).filter_by(power=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'skill':
		query = db.session.query(table).filter_by(skill=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'extra':
		query = db.session.query(table).filter_by(extra=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'free':
		query = db.session.query(table).filter_by(free=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'linked_first':
		query = db.session.query(table).filter_by(linked_first=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	elif value_id == 'linked_second':
		query = db.session.query(table).filter_by(linked_second=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
	else:
		try:
			value_id = int(value_id)
			query = db.session.query(Table).filter_by(id=value_id).first()
			if query is None:
				message = 'Could not find ' + name
				error = True
				error_msgs.append(message) 
		except:
			print('not an int')
			print(value_id)
			message = 'Not a valid ' + name
			error_msgs.append(message)	
			error = True

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
		if value != 'perm' and value != 'rank' and value != 'any' and value != 'always' and value != 'round' and value != 'extra' and value != 'null' and value != 'normal' and value != 'instant' and value != 'distance' and value != 'vert' and value != 'free' and value != 'result' and value != 'all' and value != 'trait' and value != 'imperv' and value != 'check' and value != 'turn' and value != 'degree' and value != 'scene' and value != 'auto' and value != 'advantage' and value != 'bonus' and value != 'immune' and value != 'penalty' and value != 'double' and value != 'flat' and value != 'x' and value != '' and value != 'none' and value != 'current' and value != 'all' and value != 'any' and value != 'x' and value != 'power' and value !=  'skill' and value != 'extra' and value != 'free' and value != 'linked_first' and value != 'linked_second' and value != 'skill' and value != 'parent' and value != 'speed' and value != 'unlimited' and value != 'gm' and value != 'fail' and value != 'success' and value != 'routine':
			value = int(value)
	except:
		error = True
		message = name + ' value is not valid.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

	

def db_integer(table, value):
	
	if value == 'all':
		try:
			query = db.session.query(table).filter_by(all=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'current':
		try:
			query = db.session.query(table).filter_by(current=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'any':
		try:
			query = db.session.query(table).filter_by(any=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'x':
		try:
			query = db.session.query(table).filter_by(var=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'none':
		try:
			query = db.session.query(table).filter_by(none=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'power':
		try:
			query = db.session.query(table).filter_by(power=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'skill':
		try:
			query = db.session.query(table).filter_by(skill=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'extra':
		try:
			query = db.session.query(table).filter_by(extra=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'free':
		try:
			query = db.session.query(table).filter_by(free=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'linked_first':
		try:
			query = db.session.query(table).filter_by(linked_first=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == 'linked_second':
		try:
			query = db.session.query(table).filter_by(linked_second=True).first()
			value = query.id
		except:
			print(value)
			return (value)
	elif value == '':
		value = None
	else:
		try:
			value = int(value)
		except:
			print('not an int')
			print(value)

	return (value)

def create_check(name, item_id, table, errors):

	error_msgs = errors['error_msgs']
	error = False

	if item_id != '':
		return (errors)
	else:
		error = True
		message = 'You must create a ' + name + ' name first.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def equip_create_check(item_id, feature_id, errors):

	error_msgs = errors['error_msgs']
	error = False

	if item_id != '' or feature_id != '':
		return (errors)
	else:
		error = True
		message = 'You must set an advantage name or create and select a feature first.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def db_insert(table_name, table, field, entry, errors):

	error_msgs = errors['error_msgs']
	error = False

	if field != 'other':
		return (errors)

	if entry == '':
		error = True
		message = 'You must set a name for the new ' + table_name + ' or make a different selection.'
		error_msgs.append(message)
	else:
		check = db.session.query(table).filter(table.name == entry).first()

		if check is not None:
			error = True
			message = 'There is already a ' + table_name + ' with that name.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def adv_entry_check(name, table, check, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	entry = db.session.query(table).filter_by(advantage_id=id).first()

	if check == True:
		if entry is None:
			error = True
			message = 'You checked the ' + name + ' box.  Either create a ' + name + ' rule or uncheck the box.'
			error_msgs.append(message)
	else:
		if entry is not None:
			error = True
			message = 'You created a ' + name + ' rule but the box for that rule is not checked.  Check that box or delete that rule.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def unsaved(fields, equip_id, errors):

	error_msgs = errors['error_msgs']
	error = False

	if equip_id != '':
		error = True
		message = 'You have started creating equipment.  Finish setting the values for the equipment and click the save equipment button.  Any features you have created will still be saved.'

	for f in fields:
		name = f['name']
		field = f['val']
		if field != '' and field != False:
			error = True
			message = 'The ' + name + ', ' 
			
	if error:		
		message += 'fields are just for equioment.  If you need that setting, create a new equipment item and assign save the equipment.  Otherwise reset those settings to continue.  The features will be saved on their own and be assigned to the new equipment.'
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def equip_entry_check(name, table, check, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	try:
		if id != '':
			id = int(id)
		else:
			return(errors)
	except:
		print('invalid id')

	entry = db.session.query(table).filter_by(equip_id=id).first()

	if check == True:
		if entry is None:
			error = True
			message = 'You checked the ' + name + ' box.  Either create a ' + name + ' rule or uncheck the box.'
			error_msgs.append(message)
	else:
		if entry is not None:
			error = True
			message = 'You created a ' + name + ' rule but the box for that rule is not checked.  Check that box or delete that rule.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def skill_entry_check(name, table, check, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	try:
		if id != '':
			id = int(id)
		else:
			return(errors)
	except:
		print('invalid id')

	entry = db.session.query(table).filter_by(skill_id=id).first()

	if check == True:
		if entry is None:
			error = True
			message = 'You checked the ' + name + ' box.  Either create a ' + name + ' rule or uncheck the box.'
			error_msgs.append(message)
	else:
		if entry is not None:
			error = True
			message = 'You created a ' + name + ' rule but the box for that rule is not checked.  Check that box or delete that rule.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def arm_entry_check(name, table, check, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	try:
		if id != '':
			id = int(id)
		else:
			return(errors)
	except:
		print('invalid id')

	entry = db.session.query(table).filter_by(armor_id=id).first()

	if check == True:
		if entry is None:
			error = True
			message = 'You checked the ' + name + ' box.  Either create a ' + name + ' rule or uncheck the box.'
			error_msgs.append(message)
	else:
		if entry is not None:
			error = True
			message = 'You created a ' + name + ' rule but the box for that rule is not checked.  Check that box or delete that rule.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def weap_entry_check(name, table, check, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	try:
		if id != '':
			id = int(id)
		else:
			return(errors)
	except:
		print('invalid id')


	entry = db.session.query(table).filter_by(weapon_id=id).first()

	if check == True:
		if entry is None:
			error = True
			message = 'You checked the ' + name + ' box.  Either create a ' + name + ' rule or uncheck the box.'
			error_msgs.append(message)
	else:
		if entry is not None:
			error = True
			message = 'You created a ' + name + ' rule but the box for that rule is not checked.  Check that box or delete that rule.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def adv_check_multiple(name, table, field, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	entry = db.session.query(table).filter_by(advantage_id=id).first()

	if entry is not None:
		count = db.session.query(table).filter_by(advantage_id=id).count()
		if count > 1:
			if field == '':
				error = True
				message = 'You created a ' + name + ' rule that has more than one entry but you did not make a selection for the multiple values.  Go bavk and make that selection before you can proceed.'
				error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def adv_check_multiple_fields(name, table, fields, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	entry = db.session.query(table).filter_by(advantage_id=id).first()

	if entry is not None:
		count = db.session.query(table).filter_by(advantage_id=id).count()
		if count > 1:
			for field in fields:
				if field == '':
					error = True
					message = 'You created a ' + name + ' rule that has more than one entry but you did not make a selection for one of the multiple value fields.  Go bavk and make that selection before you can proceed.'
									

	if error:
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def equip_check_multiple_fields(name, table, fields, id, errors):

	error_msgs = errors['error_msgs']
	error = False

	entry = db.session.query(table).filter_by(equip_id=id).first()

	if entry is not None:
		count = db.session.query(table).filter_by(equip_id=id).count()
		if count > 1:
			for field in fields:
				if field == '':
					error = True
					message = 'You created a ' + name + ' rule that has more than one entry but you did not make a selection for one of the multiple value fields.  Go bavk and make that selection before you can proceed.'
									

	if error:
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def adv_select_entry(value, option, fieldname, rule, field, table, advantage_id, errors, multiple=False):

	error_msgs = errors['error_msgs']
	error = False

	if value != field:
		return (errors)
	
	entry = db.session.query(table).filter_by(advantage_id=advantage_id).first()

	if entry is None:
		error = True
		message = 'You chose the ' + option + ' option for the ' + fieldname + ' field so you must create a ' + rule + ' rule or make a different selection for the ' + fieldname + ' field.'
		error_msgs.append(message)
	else:
		if multiple:
			count = db.session.query(table).filter_by(advantage_id=advantage_id).count()
			if count < 2:
				error = True
				message = 'Since you chose the ' + option + ' for the ' + fieldname + ' field, you must create at least two entries for the ' + rule + ' rule or make a different selection for the ' + fieldname + ' field.'
				error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def name_exist(name, table, value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	name_check = db.session.query(table).filter(table.name == value).first()

	if name_check is not None:
		error = True
		messqge = 'There is already a ' + name + ' with that name.'
		error_msgs.append(messqge)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def feature_check(equip_id, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	equip_id = int(equip_id)

	features = db.session.query(Feature).filter_by(equip_id=equip_id).first()

	if features is None:
		return (errors)

	features = db.session.query(Feature).filter_by(equip_id=equip_id).all()

	for f in features:
		if f.name != '':
			if f.toughness is None:
				error = True
				message = 'You created the feature ' + f.name + ' without setting the toughness  Check the damaged box, select the feature from the dropdown and set the toughness.'
				error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def head_feature_duplicate(value, id, table, errors):

	error_msgs = errors['error_msgs']
	error = False

	if value == '':
		return (errors)

	try:
		id = int(id)
		value = int(value)
		check = db.session.query(table).filter_by(head_id=id).all()
		for c in check:
			if c.feature == value:
				error = True
	except:
		print('new feature')
	
	if error:
		message = 'You have already added that feature.'
		error_msgs.append(message)	
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def skill_required_entry(value, field, name, table_name, table, id, errors):
		
	error_msgs = errors['error_msgs']
	error = False

	if id == '':
		return (errors)
		
	if value == field:
		try:
			id = int(id)
			query = db.session.query(table).filter_by(skill_id=id).first()
			if query is None:
				message = 'If this skill involves a ' + name + ' you must create at least one entry on the ' + table_name + ' form.'
				error_msgs.append(message)
		except:
			message = 'There was an error proceessing this request.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def skill_required_entry_multiple(value, field, name, table_name, table, id, errors):
		
	error_msgs = errors['error_msgs']
	error = False

	if id == '':
		return (errors)
		
	if value == field:
		try:
			id = int(id)
			query = db.session.query(table).filter_by(skill_id=id).count()
			if query < 2:
				message = 'If this skill involves a ' + name + ' you must create at least two entries on the ' + table_name + ' form.'
				error_msgs.append(message)
		except:
			message = 'There was an error proceessing this request.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
