
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


