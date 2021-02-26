
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


def level_add_skill(level, level_type, skill_id, body):
	
	skill_id = integer(skill_id)

	level_check = db.session.query(LevelType).filter(LevelType.name == level_type).first()
	if level_check is None:

		level_add = LevelType(bonus_id=skill_id,
									name=level_type)

		db.session.add(level_add)
		db.session.commit()

		type_id = level_add.id

		body['level_type'] = level_add.name
		body['created'] = False
		add_title = True
		db.session.close()
		
	else:
		level_skill = level_check.bonus_id
		print(skill_id)
		print(level_skill)
		if skill_id != level_skill:
			body['success'] = False
			body['error_msgs'] = ['There is already a level type with that name.']
			return jsonify(body)

		type_id = level_check.id
		body['created'] = True
		add_title = False

	body['title_id'] = type_id


	return (body)

	
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
