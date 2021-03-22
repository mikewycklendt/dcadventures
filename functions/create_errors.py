
from models import *
from db.rule_models import *
from db.measure_models import *
from db.user_rules import *

from db.advanrtage_modeks import *
from db.armor_models import *
from db.descriptor_models import*
from db.equipment_models import *
from db.headquarters_models import *
from db.power_models import *
from db.skill_models import *
from db.vehicle_models import *
from db.weapon_models import *

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

def not_required(check, value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if check:
		return (errors)

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


def if_fields(name, field, fields, errors, exception=False):
	error_msgs = errors['error_msgs']
	error = False

	if exception == field:
		return (errors)

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

def if_field(main, field, select, name, errors, exception=False):
	error_msgs = errors['error_msgs']
	error = False

	if exception == field:
		return (errors)

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

def seperate_checks(checks, names, errors):
	error_msgs = errors['error_msgs']
	error = False

	i = 0
	
	for c in checks:
		if c == True:
			i += 1

	if i > 1:			
		error = True
		message = 'You can can only apply ' + names + ' to one rule'		
	if error:
		errors['error'] = error
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
	
	return (errors)

	


	if error:
		errors['error'] = error
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
	
	return (errors)


def value_limit(limit, selects, names, errors):
	error_msgs = errors['error_msgs']
	error = False

	i = 0
	
	for select in selects:
		if select != '' :
			i += 1

	if i > limit:			
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
		message = 'If this rule uses a ' + name + ' you must set the ' + form + ' settings first.'
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


def valid_time_type(table, id, values, message):

	error_msgs = errors['error_msgs']
	error = True

	try:
		time = db.session.query(table).filter_by(id=id).one()
	except:
		print ('invalid time')

	for value in values:
		if value == time.type:
			error = False
	
	if error:
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def invalid_time(table, id, value, name, rule):

	error_msgs = errors['error_msgs']
	error = False

	try:
		time = db.session.query(table).filter_by(id=id).one()
	except:
		print ('invalid time')

	if value == time.value_type:
		error = True
	
	if error:
		message = name + ' is	not a valid option for ' + rule
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
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

def check_of(check, checkname, names, values, errors):

	error_msgs = errors['error_msgs']
	error = True

	if check == False:
		return (errors)

	for value in values:
		if value != '':
			error = False
				
	if error:
		message = 'You must select ' + names + ' or uncheck the ' + checkname + ' checkbox.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def select_check(value, field, check, name, require, errors):

	error_msgs = errors['error_msgs']
	error = False

	if value != field:
		return (errors)

	if check == False:
		error = True

	if error:
		message = 'If rhis rule involves a ' + name + ' you must set ' + require + '.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def checked_invalid_option(check, value, field, checkname, fieldname, name, errors):

	error_msgs = errors['error_msgs']
	error = False

	if check == False:
		return (errors)

	if value == field:
		error = True
		message = 'If rhis rule ' + checkname + ' you cannot set the ' + fieldname + ' field to ' + name + '.'
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

def required_entry_multiple(value, field, trait, name, table_name, table, column,  id, errors):
		
	error_msgs = errors['error_msgs']
	error = False

	if id == '':
		return (errors)
		
	if value == field:
		try:
			id = int(id)
			attribute = getattr(table, column)
			the_filter = attribute == id
			query = db.session.query(table).filter(the_filter).count()
			if query < 2:
				error = True
				message = 'If this ' + trait + ' involves a ' + name + ' you must create at least two entries on the ' + table_name + ' form.'
				error_msgs.append(message)
		except:
			error = True
			message = 'There was an error proceessing this request.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def required_rule(value, field, table, id, column, required, trait, rule, name, names, errors, multiple=False):
		
	error_msgs = errors['error_msgs']
	error = True
	add = ''

	if value != field:
		return (errors)
	
	if required != False:
		if required != '':
			error = False

	if table != False:
		id = int(id)
		attribute = getattr(table, column)
		check = db.session.query(table).filter(attribute == id).count()
		if multiple:
			if check > 1:
				error = False
			else:	
				add = ' and create at least 2 entries'
		else:
			if check > 0:
				error = False 

	if error:
		message = 'If this ' + trait + ' uses a ' + rule + ' you must set the ' + name + ' with the ' + names + add +'.'
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

	
def required_variable(value, table, field, name, table_name, trait, selection, column, id, errors):
		
	error_msgs = errors['error_msgs']
	error = False
		
	try:
		id = int(id)
		attribute = getattr(table, column)
		the_filter = attribute == id
		query = db.session.query(table).filter(the_filter).first()
		if query is not None:
			if field != value:
				error = True
				message = 'You have created a ' + table_name + ' for this ' + trait + ' so you must set the ' + name + ' field to ' + selection +  '.'
				error_msgs.append(message)
	except:
		error = True
		message = 'There was an error proceessing this request.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def required_link_field(table, column, id, field, table_name, trait, fieldname, errors, second_column=False, second_value=False):
		
	error_msgs = errors['error_msgs']
	error = False
		
	try:
		id = int(id)
		attribute = getattr(table, column)
		the_filter = attribute == id
		if second_column == False:
			check = db.session.query(table).filter(the_filter).first()
		else:
			second_attribute = getattr(table, second_column)
			second_filter = second_attribute == second_value
			check = db.session.query(table).filter(the_filter, second_filter).first()
		if check is None:
			return (errors)

		if field == '':
			error = True
			message = 'You have created a ' + table_name + ' for this ' + trait + ' so you must set the ' + fieldname + " before you can save this " + trait +'.'
			error_msgs.append(message)
	except:
		error = True
		message = 'There was an error proceessing this request.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def multiple_effect_check(table, column, value, id, select, errors):
		
	error_msgs = errors['error_msgs']
	error = False

	attribute = getattr(table, column)
	the_filter = attribute == id
	time = db.session.query(table).filter(the_filter).count()

	if time < 2:
		return (errors)

	time = db.session.query(table).filter(the_filter).all()

	for s in select:
		count = 0
		value = s.type
		for t in time:
			if t.type == value:
				count += 1
		if count > 1:
			if value == '':
				error = True
				message = 'You set more than 1 time for the ' + s.name + ' time effect but did not make a selection on the if multiple field.  Tou need ro set that value before you can save this skill.'
				error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors) 

def multiple_link_check(table, id, column, trait, value, name, rule, field, fieldname, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != field:
		return (errors)

	attribute = getattr(table, column)
	the_filter = attribute == id
	check = db.session.query(table).filter(the_filter).first()

	if check is not None:
		return (errors)
	else:
		error = True
		message = 'Tou selected ' + name + ' for the ' + fieldname + ' field for a ' + rule + ' rule but have not set any ' + name + ' rules for this ' + trait + '.  Either create the appropriate rule or make a different selection on thst if multiple field.' 
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors) 
	

def required_setting(value, field, fields, select, trait, id, table, column, name, required, requirement, errors):
	error_msgs = errors['error_msgs']
	error = True

	if field != value:
		return (errors)

	for f in fields:
		if f != '':
			return (errors)

	if table:
		attribute = getattr(table, column)
		the_filter = attribute == id
		check = db.session.query(table).filter(the_filter).first()
		if check is not None:
			return (errors)
	
	for s in select:
		if value == s.type:
			option = s.name
		else:
			option = ''
				
		if error:
			message = 'You selected ' + option + ' for the ' + name + ' field but have not set a ' + required + ' for this '  + trait + '.  Set a ' + required + ' with the ' + requirement + ' before you can save this ' + trait + '.' 
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def linked_group_check(table, value, field, required, column, id, group_column, name, groupname, requirement, errors, group=False):

	error_msgs = errors['error_msgs']
	error = False

	if value != field:
		return (errors)

	if id == '':
		return (errors)

	id = int(id)
	attribute = getattr(table, column)
	second = getattr(table, group_column)
	the_filter = attribute == required
	second_filter = second == id
	check = db.session.query(table).filter(second_filter, the_filter).first()

	if check is None:
		error = True

	if error:
		if group:
			message = 'You set this rule to have ' + name + ' but the ' + groupname + ' group you chose does not contain a ' + requirement + '.'
			error_msgs.append(message)
		else:
			message = 'Before youi can create this rule that uses ' + name + ' you must create a ' + groupname + ' and set ' + requirement + ' first.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def linked_field(value, field, name, rule, required, errors):

	error_msgs = errors['error_msgs']
	error = False

	if  value != 'linked' and value != 'linked_first' and value != 'linked_second':
		return (errors)

	if field == '':
		error = True

		message = 'If this ' + rule + ' involves a linked ' + name + ' you must set the ' + required + '.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)