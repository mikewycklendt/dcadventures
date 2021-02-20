
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

