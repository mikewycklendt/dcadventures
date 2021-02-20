
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


def capitalize(name):
	
	name_split = name.split(' ')
	name = name_split[0].capitalize()
	i = 1
	while i < len(name_split):
		name += ' ' 
		name += name_split[i].capitalize()
		i += 1

	return (name)

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

