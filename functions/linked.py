
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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import literal_column
from copy import deepcopy

db = SQLAlchemy()

def linked_time(table, value, name, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(table).filter(table.id == value).one()
			edit.time_table = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def linked_move(table, value, name, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(table).filter(table.id == value).one()
			edit.move_table = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def linked_options(table, trait, column):
	options = []

		
	entries = db.session.query(table).filter_by(hide=None).all()
	for e in entries:
		if e.keyword is None:
			keyword = ''
		else:
			keyword = e.keyword
		id = getattr(e, column)
		entry_name = db.session.query(trait).filter(trait.id == id).one()
		options.append({'id': e.id, 'name': str(e.id) +  entry_name.name + ' ' + keyword})

	return (options)

def level_reference(column, value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	add = True

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			setattr(edit, column, add)
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that Level.'
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_citc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_bonus_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value is not None:
		try:
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_circ = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def level_bonus_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_bonus_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_citc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

	
def required_link(table, field, name, table_name, trait, column, id, errors):
		
	error_msgs = errors['error_msgs']
	error = False
		
	try:
		id = int(id)
		attribute = getattr(table, column)
		the_filter = attribute == id
		query = db.session.query(table).filter(the_filter).first()
		if query is not None:
			if field == '' or field == False:
				error = True
				message = 'You have created a ' + table_name + ' for this ' + trait + ' so you must assign one of those entries to this ' + name + ' before you can create this rule.'
				error_msgs.append(message)
	except:
		error = True
		message = 'There was an error proceessing this request.'
		error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
