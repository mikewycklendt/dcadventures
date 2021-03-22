
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

from functions.create import capitalize

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import literal_column
from copy import deepcopy

db = SQLAlchemy()

def user_item(table, name, value, new, field, body, name_check=True, class_check=False, sub=False, sub_column=False):

	new_items = body['new_items']
	error_msgs = body['error_msgs']

	new = capitalize(new)

	if value == 'other':
		try:
			if name_check:
				name_check = db.session.query(table).filter_by(name=new, show=True).first()
				if name_check is not None:
					body['success'] = False
					message = 'There is already a ' + name + ' with that name'
					error_msgs.append(message)
					body['error_msgs'] = error_msgs
					return (body)

			entry = table(name=new)
			db.session.add(entry)
			if sub != False:
				setattr(table, sub_column, sub)
				
			db.session.commit()
			value = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = class_check
			item['field'] = field
			new_items.append(item)
			db.session.close()
		except:
			body['success'] = False
			message = 'Could not create that ' + name + '.'
			error_msgs.append(message)

	body['output'] = value
	body['new_items'] = new_items
	body['error_msgs'] = error_msgs

	return (body)