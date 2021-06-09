
from db.linked_models import PowerOpposedType
from create_functions.power_create import trait_cost
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

def not_required(check, value, name, errors, option='e', field=False):
	error_msgs = errors['error_msgs']
	error = False

	if check:
		return (errors)

	if option == field:
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


def variable_fields_of(value, name, field, fields, errors):
	error_msgs = errors['error_msgs']
	error = True

	if field != value:
		return (errors)
	else:
		for f in fields:
			if f != '':
				error = False
				
		if error:
			message = 'You select one of the ' + name + ' fields.'
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

	
def variable_field(value, field, name, f, errors, mod=False):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f == '':
			error = True
				
	if error:
		message = name + ' field is required.'
		if mod:
			message += ' If no options are in the dropdown you have not created a rule that is compatible with this modifier.'
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
	
def variable_field_required(value, field, name, firstname, value_name, second_name, f, v, errors, mod=False):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f != v:
			error = True
				
	if error:
		message = 'If you want to choose ' + firstname + ' for the ' + name + ' field, you must also choose ' + value_name + ' for the ' + second_name + ' field.'  
		if mod:
			message += ' If no options are in the dropdown you have not created a rule that is compatible with this modifier.'
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def extra_option(field, name, f, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != 'extra':
		return (errors)
	else:
		if f == '0':
			error = True
				
	if error:
		message = 'You set this rule for the base power effect so you cannot set the ' + name + ' field to Extra Rank.'
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def incompatible(value, field, dependent, val, f, fieldname, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field != value:
		return (errors)
	else:
		if f == val:
			error = True
				
	if error:
		message = 'If this rule uses ' + dependent + ' the ' + fieldname + ' cannot be set to ' + na,e
		error_msgs.append(message)


	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def valid_options(check, name, values, names, field, fieldname, errors):
	error_msgs = errors['error_msgs']
	error = True
	
	if check == False:
		return (errors)

	for v in values:
		if field == v:
			error = False

	if error:
		message = 'If this rule ' + name + ' you can only select ' + names + ' from the ' + fieldname + ' field.'
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)
	
def variable_field_of(value, field, names, fields, errors):
	error_msgs = errors['error_msgs']
	error = True

	if field != value:
		return (errors)
	else:
		for f in fields:
			if f != '' and f != False:
				error = False
				
	if error:
		message = 'You must select one of the ' + names + ' fields.'
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
	
def dependent_of(name, names, value, values, errors):

	error_msgs = errors['error_msgs']
	error = True

	check = False

	if value == '':
		return (errors)

	for value in values:
		if value != '' and value != False:
			error = False
				
	if error:
		message = 'If this rule ' + name + ' you must ' + names + '.'
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

def check_field(check, checkname, name, value, errors, mod=False):

	error_msgs = errors['error_msgs']
	error = False

	if check:
		if value == '' or value is None:
				error = True
				
	if error:
		message = name + ' field is required or uncheck the ' + checkname + ' checkbox.'
		if mod:
			message += ' If no options are in the dropdown you have not created a rule that is compatible with this modifier yet.'
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
				if v != '' and v != False:
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
			if v != '' and v != False:
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
			if v != '':
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

def select_of_check(value, selected_name, names, field_name, field, values, errors):
	error_msgs = errors['error_msgs']
	error = True

	if value != field:
		return (errors)

	if value == field:
		for v in values:
			if v == True:
				error = False

	message = 'If this effect ' + selected_name + ', you must select one of the ' + names + ' fields or make a different selection in the ' + field_name + ' field.'

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

def variable_required_rules(value, field, rulename, required, table_name, table, column, id, errors, second_column=False, second_value=False, any=False):
		
	error_msgs = errors['error_msgs']
	error = False

	if value != field:
		return (errors)
		
	try:
		id = int(id)
		attribute = getattr(table, column)
		the_filter = attribute == id
		if second_column == False:
			check = db.session.query(table).filter(the_filter).first()
		else:
			if any != False:
				second_attribute = getattr(table, second_column)
				second_filter = second_attribute != second_value
			else:
				second_attribute = getattr(table, second_column)
				second_filter = second_attribute == second_value
			check = db.session.query(table).filter(the_filter, second_filter).first()
		if check is None:
			error = True
			message = 'If this rule involves ' + rulename + ' you must fill out the ' + required + ' on the ' + table_name + " form first."
			error_msgs.append(message)
	except:
		error = True
		message = 'There was an error proceessing this request.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def cross_check(rulename, first_tablename, directions, second_tablename, table, column, value, second_table, trait_column, id, errors, second_column=False, second_value=False, any=False, second_any=False):
	error_msgs = errors['error_msgs']
	error = False

	try:
		id = int(id)
		attribute = getattr(table, trait_column)
		the_filter = attribute == id
		first_attribute = getattr(table, column)
		if any != False:
			first_filter = first_attribute != value
		else:
			first_filter = first_attribute == value
		check = db.session.query(table).filter(the_filter, first_filter).first()
		
		if check is None:
			return (errors)

		if second_column == False:
			check = db.session.query(second_table).filter(the_filter).first()
		else:
			second_attribute = getattr(second_table, second_column)
			if second_any != False:
				second_filter = second_attribute != value
			else:
				second_filter = second_attribute == value
			check = db.session.query(second_table).filter(the_filter, second_filter).first()
			
		if check is None:
			error = True
			message = 'You created a ' + rulename + ' rule on the ' + first_tablename + " form so you must " + directions + ' on the ' + second_tablename + ' form.'
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


def linked_field(value, field, table, name, rule, required, errors):

	error_msgs = errors['error_msgs']
	error = False

	if  value != 'linked' and value != 'linked_first' and value != 'linked_second':
		return (errors)

	if field == '':
		error = True

		message = 'If this ' + rule + ' involves a linked ' + name + ' you must set the ' + required + '.'
		error_msgs.append(message)

	if field != '':
		try:
			field = int(field)
		except:
			error = True
			message = 'Invalid Linked Degree.'
			error_msgs.append(message)

	try:
		check = db.session.query(table).filter_by(id=field).one()
	except:
		error = True
		message = 'Could not find the linked degree.'
		error_msgs.append(message)

	if value == 'linked':
		if check.type != 'consequence':
			error = True
			message = 'You set this rule to have a linked ' + name + ' but the ' + rule + ' you linked this rule to does not set a ' + name + '.  Link this rule to the ' + rule + ' that sets the ' + name + ' this rule links to.'
			error_msgs.append(message)
		else:
			consequence = db.session.query(Consequence).filter_by(id=check.consequence).one()
			if consequence.linked == True:
				error = True
				message = 'The ' + name + ' you set in the ' + rule + ' this rule links to is set to linked.  A Linked ' + name + ' cannot be linked to a ' + rule + ' where the ' + name + ' is set to linked.  Tou must set the ' + name + ' in the ' + rule +  ' a linked ' + name + ' is linked to.'
				error_msgs.append(message)
	elif value == 'linked_first' or value == 'linked_second':
		if check.type != 'condition':
			error = True
			message = 'You set this rule to have a linked ' + name + ' but the ' + rule + ' you linked this rule to does not set a ' + name + '.  Link this rule to the ' + rule + ' that sets the ' + name + ' this rule links to.'
			error_msgs.append(message)
		if check.condition_type == 'condition':
			if value == 'linked_first':
				condition = db.session.query(Condition).filter_by(check.condition1).first()
				if condition.linked_first == True or condition.linked_second == True:
					error = True	
					message = 'The ' + name + ' you set in the ' + rule + ' this rule links to is set to linked.  A Linked ' + name + ' cannot be linked to a ' + rule + ' where the ' + name + ' is set to linked.  Tou must set the ' + name + ' in the ' + rule +  ' a linked ' + name + ' is linked to.'
					error_msgs.append(message)
			elif value == 'linked_second':
				condition = db.session.query(Condition).filter_by(check.condition2).first()
				if condition.linked_first == True or condition.linked_second == True:
					error = True	
					message = 'The ' + name + ' you set in the ' + rule + ' this rule links to is set to linked.  A Linked ' + name + ' cannot be linked to a ' + rule + ' where the ' + name + ' is set to linked.  Tou must set the ' + name + ' in the ' + rule +  ' a linked ' + name + ' is linked to.'
					error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def primary_check(name, trait, check_values, value_name, table, type_table, other_table, other_name, title, primary, power_action, power_check, power_id, body, variable=False, opposed=False, opposed_type=False):

	error_msgs = body['error_msgs']
	error = False

	if primary != True:
		return (body)

	stop = True

	for c in check_values:
		if c == power_check:
			stop = False

	if stop:
		error = True
		message = 'If this ' + name + ' is a primary check for this ' + trait + ', you must set this ' + trait + "'s Check to " + vslue_name '. In the base power settings. You have currently set a different primary check for this ' + trait '.'
		error_msgs.append(message)

	if variable:
		if power_action != 'x':
			error = True
			message = 'If this is the primary check for this ' + trait + ' you must set the action field in the base power settings to variable.'
			error_msgs.append(message)
			
	check = db.session.query(type_table).filter_by(id=title).one()
	if check.primary != True:
		error = True
		message = 'You set this ' + name  + ' to be a primary check for this ' + trait + ' but the title group you have assigned it to is not a primary check group. Keep all Primary Checks in the same group.'
		error_msgs.append(message)

	check = db.session.query(type_table).filter_by(power_id=power_id, primary=True).first()
	if check.id != title:
		error = True
		message = 'You have already created a group for this ' + trait + "'s primary check.  If this is a primary check for this " + trait + ', put this check in the group containing the existing primary checks.'
		error_msgs.append(message)

	check = db.session.query(other_table).filter_by(power_id=power_id, primary=True).first()
	if check is not None:
		if opposed == False and opposed_type == False:
			error = True
			message = 'You have already set the primary check for this ' + trait + ' with the ' + other_name + ' form.  You can either attach this check to it or you can delete the primary check you created with the ' + other_name + ' form and create the primary check here.'
		else:
			if opposed is not None:
				check = db.session.query(PowerOpposed).filter_by(id=opposed).one()
				if check.primary != False:
					error = True
					message = 'You have already set the primary check for this ' + trait + ' with the ' + other_name + ' form.  You can still make this check the primary check by making this check an opposed check or comparison check and selecting either the primary opponent check or primary opponent check group.  If rhis check is not an opposed check or comparison check but you still want it to be the primary check you must delete the primary check group you created on the opponent check form first or you can keep the opponent check as the primary check and attach this check to it.'
					error_msgs.append(nessage)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (body)