
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
	
def link_add(table, title_table, column, id, title, keyword, body):
	error_msgs = []
	success = body['success']
	body['add_title'] = False	

	id = int(id)
	attribute = getattr(title_table, column)
	print (attribute)
	the_filter = attribute == id
	entry = db.session.query(title_table).filter(the_filter, title_table.name == title).first()
	if entry is not None:
		title_id = entry.id
		body['add_title'] = False
	else:
		try:
			entry = title_table(name=title)
			db.session.add(entry)
			setattr(entry, column, id)
			db.session.commit()
			title_id = entry.id
			body['add_title'] = True
			body['created'] = False
			db.session.close()
		except:
			success = False
			error_msgs.append('There was an error adding that title.')
			db.session.rollback()
		finally:
			db.session.close()

	entry = db.session.query(table).filter(table.title == title_id, table.keyword == keyword).first()
	if entry is not None:
		success = False
		error_msgs.append('You have already created a rule with that keyword for this title.')

	body['success'] = success
	body['error_msgs'] = error_msgs
	body['title_id'] = title_id

	return (body)

def level_add(id, column, level, level_type, body):
	error_msgs = []
	success = body['success']
	body['add_title'] = False	

	id = int(id)

	level_check = db.session.query(LevelType).filter(LevelType.name == level_type).first()
	if level_check is None:
		try:
			level_add = LevelType(name=level_type, show=True)
			db.session.add(level_add)
			setattr(level_add, column, id)
			db.session.commit()
			add_title = True
			created = False
			title_id = level_add.id
		except:
			success = False
			error_msgs.append('There was an error adding that level type.')
			db.session.rollback()
		finally:
			db.session.close()
	else:
		trait_id = getattr(level_check, column)
		if id != trait_id:
			success = False
			error_msgs.append('There is already a level type with that name.')
		created = True
		title_id = level_check.id
		created = True
		add_title = False
 
	try:
		entry = db.session.query(Levels).filter(Levels.type_id == title_id, Levels.name == level).first()
		if entry is not None:
			success = False
			error_msgs.append('You have already created a rule with that keyword for this title.')
	except:
		success = False
		error_msgs.append('There was an error processing that level')

	body['success'] = success
	body['created'] = created
	body['error_msgs'] = error_msgs
	body['title_id'] = title_id
	body['add_title'] = add_title
	body['title'] = level_type

	return (body)


def delete_link(table, link_table, id):
	body = {}
	body['success'] = True
	body['hide_table'] = False
	error_msgs = []

	try:
		get_trait = db.session.query(table).filter_by(id=id).first()
		title_id = get_trait.title
		body['title_id'] = title_id
		body['id'] = id
		db.session.query(table).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
		db.session.close()
		
		empty = db.session.query(table).filter_by(title=title_id).first()
		if empty is None:
			db.session.query(link_table).filter_by(id=title_id).delete()
			body['hide_table'] = True
			db.session.commit()
	except:
		body['success'] = False
		message = 'There was an error deleting this rule.  You may have applied it to another rule.  Delete that rule then try again.'
		error_msgs.append(message)
		db.session.rollback()
	finally:
		db.session.close()
		body['error_msgs'] = error_msgs

	return (body)

def delete_level(id):
	body = {}
	body['success'] = True
	body['hide_table'] = False
	error_msgs = []

	try:
		get_level = db.session.query(Levels).filter_by(id=id).first()
		title_id = get_level.type_id
		body['title_id'] = title_id
		body['id'] = id
		db.session.query(Levels).filter_by(id=id).delete()
		db.session.commit()
		print('\n\n' + str(id) + ' DELETED\n\n')
		db.session.close()

		empty = db.session.query(Levels).filter_by(type_id=title_id).first()
		if empty is None:
			db.session.query(LevelType).filter_by(id=title_id).delete()
			body['hide_table'] = True
			db.session.commit()
	except:
		body['success'] = False
		message = 'There was an error deleting that level.  You may have applied it to another rule.  Delete that rule then try again.'
		error_msgs.append(message)
		db.session.rollback()
	finally:
		db.session.close()
		body['error_msgs'] = error_msgs

	return (body)

def required_link(table, field, name, table_name, trait, column, id, errors):
		
	error_msgs = errors['error_msgs']
	error = False
		
	try:
		id = int(id)
		attribute = getattr(table, column)
		the_filter = attribute == id
		entry = db.session.query(table).filter(the_filter).first()
		if entry is not None:
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

def linked_ref(table, value, name, column, body):
	
	error_msgs = body['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(table).filter(table.id == value).one()
			setattr(tsble, column, True)
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	body['error_msgs'] = error_msgs
	if error:
		body['success'] = False

	return (errors)

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


def linked_options(table, trait, column, option):
	options = []

		
	entries = db.session.query(table).all()
	for e in entries:
		name = getattr(e, option)
		if name is None:
			name = ''
		id = getattr(e, column)
		try:
			entry_name = db.session.query(trait).filter(trait.id == id).one()
			options.append({'id': e.id, 'name': str(e.id) + ' ' +  entry_name.name + ' ' + name})
		except:
			print('hidden')
			db.session.close()

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

