
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


def integer(value):

	if value == 'perm':
		value = 123123
	elif value == 'rank':
		value = 121121
	elif value == 'any':
		value = 567567
	elif value == 'always':
		value = 222222
	elif value == 'round':
		value = 333333
	elif value == 'extra':
		value = 111111
	elif value == 'null':
		value = 444444
	elif value == 'normal':
		value = 555555
	elif value == 'instant':
		value = 666666
	elif value == 'distance':
		value = 777777
	elif value == 'vert':
		value = 888888
	elif value == 'free':
		value = 999999
	elif value == 'result':
		value = 432432
	elif value == 'all':
		value = 778778
	elif value == 'trait':
		value = 112112
	elif value == 'imperv':
		value = 334334
	elif value == 'check':
		value = 556556
	elif value == 'turn':
		value = 990990
	elif value == 'degree':
		value = 211211
	elif value == 'scene':
		value = 322322
	elif value == 'auto':
		value = 433433
	elif value == 'advantage':
		value = 544544
	elif value == 'bonus':
		value = 655655
	elif value == 'immune':
		value = 766766
	elif value == 'penalty':
		value = 877877
	elif value == 'double':
		value = 988988
	elif value == 'flat':
		value = 998998
	elif value == 'x':
		value = 12341234
	elif value == 'skill':
		value = 23452345
	elif value == 'parent':
		value = 34563456
	elif value == 'speed':
		value = 45674567
	elif value == 'unlimited':
		value = 56785678
	elif value == 'gm':
		value = 67896789
	elif value == 'fail':
		value = 987987
	elif value == 'success':
		value = 876876
	elif value == 'routine':
		value = 765765
	elif value == 'penval':
		value = 654654
	elif value == 'oppbonus':
		value = 543543
	elif value == 'retry':
		value = 432432
	elif value == 'prop':
		value = 321321
	elif value == 'volume':
		value = 210210
	elif value == 'halfrank':
		value = 223223
	elif value == 'halfpenalty':
		value = 445445
	elif value == '':
		value = None
	elif value == 'none':
		value = None
	else:
		try:
			value = int(value)
		except:
			print('not an int')
			print(value)

	return (value)
	
def var_convert(value):

	if value == 'x':
		value = None
	else:
		value = int(value)

	return (value)

def cost_convert(value):
	if value == '0':
		value = None
	else:
		value = int(value)

	return (value)
	
def var_string(value):

	if value is None:
		value = 'Variable'
	else:
		value = str(value)

	return (value)

def integer_convert(value):

	if value == 123123:
		value = "Permanent"
		print(value)
	elif value == 121121:
		value = "Power Rank"
		print(value)
	elif value == 567567:
		value = "Any"
		print(value)
	elif value == 222222:
		value = "Always"
		print(value)
	elif value == 333333:
		value = "One Round"
		print(value)
	elif value == 111111:
		value = "Extra Rank"
		print(value)
	elif value == 444444:
		value = "Nullified"
		print(value)
	elif value == 555555:
		value = "Normal"
		print(value)
	elif value == 666666:
		value = "Instant"
		print(value)
	elif value == 777777:
		value = "Distance rank"
		print(value)
	elif value == 888888:
		value = "Vertical Height"
		print(value)
	elif value == 999999:
		value = "No Check"
		print(value)
	elif value == 432432:
		value = "Result"
		print(value)
	elif value == 778778:
		value = "All"
		print(value)
	elif value == 112112:
		value = "Trait"
		print(value)
	elif value == 334334:
		value = "Impervious"
		print(value)
	elif value == 556556:
		value = "Check"
		print(value)
	elif value == 990990:
		value = "Turn"
		print(value)
	elif value == 211211:
		value = 'One Per Degree'
	elif value == 322322:
		value = 'Scene'
	elif value == 433433:
		value = 'Automatic'
	elif value == 544544:
		value = 'Advantage Rank'
	elif value == 655655:
		value = 'Same as Bonus'
	elif value == 766766:
		value = 'Immune'
	elif value == 877877:
		value = 'No Penalties'
	elif value == 988988:
		value = 'Doubles Per Rank'
	elif value == 998998:
		value = 'Flat Value'
	elif value == 23452345:
		value = 'This Rank'
	elif value == 34563456:
		value = 'Parent Skill'
	elif value == 45674567:
		value = 'Speed Rank'
	elif value == 56785678:
		value = 'Unlimited'
	elif value == 67896789:
		value = 'GM Decides'
	elif value == 987987:
		value = 'Failure'
	elif value == 876876:
		value = 'Success'
	elif value == 765765:
		value = 'Routine'
	elif value == 654654:
		value = 'Penalty Value'
	elif value == 543543:
		value = 'No Opponent Bonus'
	elif value == 432432:
		value = 'Retry Chhck'
	elif value == 321321:
		value = 'Proportional'
	elif value == 210210:
		value = 'Volume Rank'
	elif value == 223223:
		value = '1/2 Power Rank'
	elif value == 445445:
		value = '- 1/2 Power Rank'
	elif value is None:
		value = ''
	else:
		value = str(value)

	return (value)


def int_check(value, name, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value == 'perm':
		return (errors)
	elif value == 'rank':
		return (errors)
	elif value == 'any':
		return (errors)
	elif value == 'always':
		return (errors)
	elif value == 'round':
		return (errors)
	elif value == 'extra':
		return (errors)
	elif value == 'null':
		return (errors)
	elif value == 'normal':
		return (errors)
	elif value == 'instant':
		return (errors)
	elif value == 'distance':
		return (errors)
	elif value == 'vert':
		return (errors)
	elif value == 'free':
		return (errors)
	elif value == 'result':
		return (errors)
	elif value == 'all':
		return (errors)
	elif value == 'trait':
		return (errors)
	elif value == 'imperv':
		return (errors)
	elif value == 'check':
		return (errors)
	elif value == 'turn':
		return (errors)
	elif value == 'degree':
		return (errors)
	elif value == 'scene':
		return (errors)
	elif value == 'auto':
		return (errors)
	elif value == 'advantage':
		return (errors)
	elif value == 'bonus':
		return (errors)
	elif value == 'immune':
		return (errors)
	elif value == 'penalty':
		return (errors)
	elif value == 'double':
		return (errors)
	elif value == 'flat':
		return (errors)
	elif value == 'x':
		return (errors)
	elif value == 'skill':
		return (errors)
	elif value == 'parent':
		return (errors)
	elif value == 'speed':
		return (errors)
	elif value == 'unlimited':
		return (errors)
	elif value == 'gm':
		return (errors)
	elif value == 'fail':
		return (errors)
	elif value == 'success':
		return (errors)
	elif value == 'routine':
		return (errors)
	elif value == '':
		return (errors)
	elif value == 'none':
		return (errors)
	elif value == 'penval':
		return (errors)
	elif value == 'oppbonus':
		return (errors)
	elif value == 'retry':
		return (errors)
	elif value == 'prop':
		return (errors)
	elif value == 'volume':
		return (errors)
	elif value == 'halfrank':
		return (errors)
	elif value == 'halfpenalty':
		return (errors)
	else:
		try:
			value = int(value)
		except:
			error = True
			message = name + ' value is not valid.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)



def name(Table, value, name=''):
	
	if value == 0:
		value = 'All'
		return (value)

	if value == 1234:
		value = name
		return (value)

	if value is not None:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.name
		except:
			print('no entry')
	else:
		value = ''

	
	return (value)

def get_name(Table, value):
	
	if value is None:
		value = ''
		return (value)
	else:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.name
		except:
			print('no entry')
			value = ''
		finally:
			db.session.close()

	return (value)

def get_multiple(Table, multiple):

	names = ''

	for m in multiple:
		name = get_name(Table, m)
		if names == '':
			names += name
		else:
			names += ', ' + name

	return (names)

def get_id(Table, value):
	
	if value is None:
		print (value)
		value = ''
		return (value)
	else:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.name
		except:
			print('no entry')
			value = ''
		finally:
			db.session.close()

	return (value)

def get_circ(Table, value, name=''):
	
	if value == 0:
		value = 'All'
		return (value)

	if value == 1234:
		value = name
		return (value)

	if value is not None:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.keyword
		except:
			print('no entry')
		finally:
			db.session.close()
	else:
		value = ''

	
	return (value)

def get_keyword(Table, value):
	
	if value is not None:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.keyword
		except:
			print('no entry')
		finally:
			db.session.close()
	else:
		value = ''

	
	return (value)


def get_description(Table, value, name=''):
	
	if value is not None:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			description = name_query.description
		except:
			print('no entry')
		finally:
			db.session.close()
	else:
		value = ''

	return (description)

def action_convert(value, action_value):

	if value == 'auto':
		a = 'Automatic'
	elif value == 'base':
		action = db.session.query(Action).filter_by(id=action_value).one()
		a = action.name
		db.session.close()
	elif value == 'conflict':
		action = db.session.query(ConflictAction).filter_by(id=action_value).one()
		a = action.name
		db.session.close()
	else:
		a = ''
	
	

	return (a)

def math_convert(name):
	
	db = SQLAlchemy()

	if name is None:
		name =  ''
		return (name)
	elif name == 1:
		name = '<i class="fas fa-plus"></i>'
	elif name == 2:
		name = '<i class="fas fa-minus"></i>'
	elif name == 4:
		name = '<i class="fas fa-divide"></i>'
	elif name == 3:
		name = '<i class="fas fa-times"></i>'
	elif name == '>=':
		name = '<i class="fas fa-greater-than-equal"></i>'
	elif name == '<=':
		name = '<i class="fas fa-less-than-equal"></i>'
	elif name == '>':
		name = '<i class="fas fa-greater-than"></i>'
	elif name == '<':
		name = '<i class="fas fa-less-than"></i>'
	elif name == '=':
		name = '<i class="fas fa-equals"></i>'
	
	return (name)

def extra_name(name):
	
	db = SQLAlchemy()

	if name is None:
		name = 'Base Power'
	else:
		try:
			query = db.session.query(Extra).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
		finally:
			db.session.close()
	
	return (name)

def selects(value, options):

	if value != '':
		for option in options:
			if value == option['type']:
				value = option['name']

	return (value)

def db_multiple(table, multiple):

	for i in range(0, len(multiple), 1):
		db = multiple[i]
		db = db_integer(table, db)
		multiple[i] = db

	return (multiple)

def db_integer(table, value):
	
	if value == 'all':
		try:
			query = db.session.query(table).filter_by(all=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'current':
		try:
			query = db.session.query(table).filter_by(current=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'any':
		try:
			query = db.session.query(table).filter_by(any=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'x':
		try:
			query = db.session.query(table).filter_by(var=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'none':
		try:
			query = db.session.query(table).filter_by(none=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'power':
		try:
			query = db.session.query(table).filter_by(power=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'skill':
		try:
			query = db.session.query(table).filter_by(skill=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'extra':
		try:
			query = db.session.query(table).filter_by(extra=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'free':
		try:
			query = db.session.query(table).filter_by(free=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'linked':
		try:
			query = db.session.query(table).filter_by(linked=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'linked_first':
		try:
			query = db.session.query(table).filter_by(linked_first=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'linked_second':
		try:
			query = db.session.query(table).filter_by(linked_second=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'linked_damage':
		try:
			query = db.session.query(table).filter_by(linked_damage=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'stable':
		try:
			query = db.session.query(table).filter_by(stable=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'perm':
		try:
			query = db.session.query(table).filter_by(perm=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'round':
		try:	
			query = db.session.query(table).filter_by(round=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'scene':
		try:
			query = db.session.query(table).filter_by(scene=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'instant':
		try:	
			query = db.session.query(table).filter_by(instant=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'turn':
		try:	
			query = db.session.query(table).filter_by(turn=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'next':
		try:	
			query = db.session.query(table).filter_by(next=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'outdoors':
		try:	
			query = db.session.query(table).filter_by(outdoors=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'active':
		try:	
			query = db.session.query(table).filter_by(active=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'gm':
		try:	
			query = db.session.query(table).filter_by(gm=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'player':
		try:	
			query = db.session.query(table).filter_by(player=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'maintain':
		try:	
			query = db.session.query(table).filter_by(maintain=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'remove':
		try:	
			query = db.session.query(table).filter_by(remove=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'improvise':
		try:	
			query = db.session.query(table).filter_by(improvise=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'xsense':
		try:	
			query = db.session.query(table).filter_by(var_sense=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'percep':
		try:	
			query = db.session.query(table).filter_by(perception=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'machine':
		try:	
			query = db.session.query(table).filter_by(machine=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'human':
		try:	
			query = db.session.query(table).filter_by(human=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'normal':
		try:	
			query = db.session.query(table).filter_by(normal=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == 'dead':
		try:	
			query = db.session.query(table).filter_by(dead=True).first()
			value = query.id
		except:
			print(value)
			return (value)
		finally:
			db.session.close()
	elif value == '':
		value = None
		return (value)
	elif value == '0':
		value = None
		return(value)
	elif value == 'ex':
		value = None
		return (value)
	else:
		try:
			value = int(value)
		except:
			print('not an int')
			print(value)

	return (value)

def id_multiple(table, multiple, name, errors):

	for m in multiple:
		errors = id_check(table, m, name, errors)

	return (errors)

def id_check(table, value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	

	if value_id == '':
		return (errors)
	if value_id == 'base':
		return (errors)
	elif value_id == 'all':
		query = db.session.query(table).filter_by(all=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'current':
		query = db.session.query(table).filter_by(current=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'any':
		query = db.session.query(table).filter_by(any=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'x':
		query = db.session.query(table).filter_by(var=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'none':
		query = db.session.query(table).filter_by(none=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'power':
		query = db.session.query(table).filter_by(power=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'skill':
		query = db.session.query(table).filter_by(skill=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'extra':
		query = db.session.query(table).filter_by(extra=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'free':
		query = db.session.query(table).filter_by(free=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'linked':
		query = db.session.query(table).filter_by(linked=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'linked_first':
		query = db.session.query(table).filter_by(linked_first=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'linked_second':
		query = db.session.query(table).filter_by(linked_second=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'linked_damage':
		query = db.session.query(table).filter_by(linked_damage=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'remove':
		query = db.session.query(table).filter_by(remove=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'stable':
		query = db.session.query(table).filter_by(stable=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'perm':
		query = db.session.query(table).filter_by(perm=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'round':
		query = db.session.query(table).filter_by(round=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'scene':
		query = db.session.query(table).filter_by(scene=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'instant':
		query = db.session.query(table).filter_by(instant=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'turn':
		query = db.session.query(table).filter_by(turn=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'next':
		query = db.session.query(table).filter_by(next=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'outdoors':
		query = db.session.query(table).filter_by(outdoors=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'active':
		query = db.session.query(table).filter_by(active=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'gm':
		query = db.session.query(table).filter_by(gm=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'player':
		query = db.session.query(table).filter_by(player=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'maintain':
		query = db.session.query(table).filter_by(maintain=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'improvise':
		query = db.session.query(table).filter_by(improvise=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'xsense':
		query = db.session.query(table).filter_by(var_sense=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'percep':
		query = db.session.query(table).filter_by(perception=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'machine':
		query = db.session.query(table).filter_by(machine=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'human':
		query = db.session.query(table).filter_by(human=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'normal':
		query = db.session.query(table).filter_by(normal=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id == 'dead':
		query = db.session.query(table).filter_by(dead=True).first()
		if query is None:
			message = 'Not a valid option for ' + name
			error = True
			error_msgs.append(message)
		db.session.close()
	elif value_id ==  'ex':
		return (errors)
	else:
		try:
			value_id = int(value_id)
			query = db.session.query(table).filter_by(id=value_id).first()
			if query is None:
				message = 'Could not find ' + name
				error = True
				error_msgs.append(message) 
		except:
			print('not an int')
			print(value_id)
			message = 'Not a valid ' + name
			error_msgs.append(message)	
			error = True
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def preset_convert(value, field):

	if value == field:
		preset = True
	else:
		preset = None

	return (preset)


def trait_select(value, trait):

	if trait == 'ability':
		try:
			query = db.session.query(Ability).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'defense':
		try:
			query = db.session.query(Defense).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'resist':
		try:
			query = db.session.query(Defense).filter_by(id=value).one()
			value = 'Powers Resisted by ' + query.name
		except:
			value = 'Not Found'
	elif trait == 'skill':
		try:
			query = db.session.query(Skill).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'bonus':
		try:
			query = db.session.query(SkillBonus).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'power':
		try:
			query = db.session.query(Power).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'effect':
		try:
			query = db.session.query(Power).filter_by(id=value).one()
			value = 'Trait Affected by ' + query.name
		except:
			value = 'Not Found'
	elif trait == 'advantage':
		try:
			query = db.session.query(Advantage).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'extra':
		try:
			query = db.session.query(Extra).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'equip':
		try:
			query = db.session.query(Equipment).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'interact':
		value =  'Any Interarction'
	elif trait == 'manipulate':
		value =  'Any Manipulation'
	elif trait == 'this_power':
		value =  'This Power'
	elif trait == 'this_advantage':
		value =  'This Advantage'
	elif trait == 'sense':
		value =  'Sense'
	elif trait == 'size':	
		value =  'Size Rank'
	elif trait == 'speed':	
		value =  'Speed Rank'
	elif trait == 'intim':
		value =  'Intimidation Rank'
	elif trait == 'any':
		value =  'Any Trait'
	elif trait == 'x':
		value =  'Variable'
	elif trait == 'auto':
		value =  'Automatic'
	elif trait == '':
		 value = ''
	elif trait == 'immoveable':
		value =  'Immoveable'
	elif trait == 'this_bonus':
		value =  'This Skill'
	elif trait == 'active':
		value =  'Active Opponent Rank'
	elif trait == 'choice':
		value =  'Players Chosen DC'
	elif trait == 'mass':
		value = "Object Mass"
	elif trait == 'volume':
		value = "Object Volume"
	elif trait == 'tough':
		value = "Object Toughness"
	elif trait == 'attack':
		value = "Attack Bonus"
	elif trait == 'vert':
		value = "Vertical Distance"
	elif trait == 'points':
		value = "Hero Point Total"
	elif trait == 'alteration':
		value = "Alteration Effects"
	elif trait == 'emotion':
		value = "Emotion Effects"
	
	return (value)


def db_check(Table, value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	

	if value_id != '' and value_id != '0' and value_id != 'x' and value_id != 'other':
		try:
			value_id = int(value_id)
		except:
			message = 'Not a valid ' + name
			error_msgs.append(message)	
			error = True
			errors['error'] = True
			errors['error_msgs'] = error_msgs

			return (errors)

		try:
			query = db.session.query(Table).filter_by(id=value_id).one()
		except:	
			message = 'Could not find ' + name
			error = True
			error_msgs.append(message) 

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def rarity_convert(rare, damage=False):
	
	if rare < 3:
		rarity = 'very'
	if rare == 3 :	
		rarity = 'common'
	if 3 < rare < 7:
		rarity = 'uncommon'
	if rare > 7:
		rarity= 'rare'

	if damage == True:
		rarity = None

	return (rarity)