
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


