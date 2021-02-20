
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



def power_check(value, errors):
	error_msgs = errors['error_msgs']
	error = False

	if value == '' or value is None:
		error = True
		message = 'You must create a power name first.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def rule_check(check, name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule = db.session.query(table).filter_by(power_id = power).first()

	if check:
		if rule is None:
			error = True
			message = 'You must create a ' + name + ' rule or uncheck the ' + name + ' checkbox.'
			error_msgs.append(message)
	else:
		if rule is not None:
			error = True
			message = 'Delete the ' + name + ' rules you created or check the ' + name + ' checkbox.'
			error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def rule_select(value, field, name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	if field == value:
		rule = db.session.query(table).filter_by(power_id = power).first()

		if rule is None:
			message = 'If this rule has a ' + name + ' effect, you must add ' + name + ' rules for it.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def cost_check(check, name, field, table, power, errors, values='e'):
	error_msgs = errors['error_msgs']
	error = False

	rule_check = db.session.query(table).filter_by(power_id=power).first()

	if rule_check is not None:
		if field != 'x':
			cost_check = db.session.query(table).filter_by(power_id=power, extra_id=None).all()
			for c in cost_check:
				if c.cost is not None:
					error = True
					message = 'You set a rule for a ' + name + ' that has a cost of its own but you set a cost for the base power.  If you want to set a different cost for this rule you must set the base power cost to variable.'
					error_msgs.append(message)
		else:
			cost_check = db.session.query(table).filter_by(power_id=power, extra_id=None).all()
			for c in cost_check:
				if c.cost is None:
					error = True
					message = 'You set a variable cost for this power, so you must delete and recreate the ' + name + ' rule and specify the cost or set a cost for the base power.'
					error_msgs.append(message)
				
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def extra_cost(name, table, power, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule_check = db.session.query(table).filter_by(power_id=power).first()

	if rule_check is not None:
		cost_check = db.session.query(table).filter_by(power_id=power).all() 
		for c in cost_check:
			extra_id = c.extra_id
			if extra_id is not None:
				extra_check = db.session.query(Extra).filter_by(id=extra_id).first()	
				if extra_check is not None:
					if extra_check.cost is not None:
						if c.cost is not None:
							error = True
							message = 'You set a rule for a ' + name + ' effect that was assigned to the ' + extra_check.name + ' extra that has its own cost.  If you want to set an alternate cost for this rule it cannot be assigned to this extra or you can delete the extra and recreate it, this time setting a variable cost for the extra and delete and recreate the rule and setting it to the recreated extra with its variable cost.'
							error_msgs.append(message)
					else:
						if c.cost is None:
							error = True
							message = 'You set a variable cost for the ' + extra_check.name + ' extra and created a ' + name + ' rule was assigned to i, so you must delete and recreate the ' + name + ' rule for that extra and specify the cost.'
							error_msgs.append(message)
				
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def extra_check(value_id, name, errors):
	error_msgs = errors['error_msgs']
	error = False
	
	db = SQLAlchemy()

	if value_id != '':
		try:
			value_id = int(value_id)
		except:
			message = 'Not a valid ' + name
			error_msgs.append(message)	
			error = True
			errors['error'] = True
			errors['error_msgs'] = error_msgs

			return (errors)

		if value_id == 0:
			return (errors)

		try:
			query = db.session.query(Extra).filter_by(id=value_id).one()
		except:
			message = 'Could not find ' + name
			error = True
			error_msgs.append(message) 

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def extra_convert(extra_id):

	if extra_id == '0':
		extra_id = None
	else:
		integer(extra_id)

	return (extra_id)



def field_cost(name, field, value, effect_cost, rule_cost, power_cost, extra_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id != '' and extra_id != '0':
		extra_id = integer(extra_id)
		if extra_id is not None:
			extra = db.session.query(Extra).filter_by(id = extra_id).first()
			if extra is not None:
				cost = extra.cost
				power_name = extra.name + ' Extra'
	else:
		cost = power_cost
		power_name = 'Base Power'

	if field == value:
		if effect_cost == '':
			error = True
			message = 'You selected a varible value for the ' + name + ' field so you must set a cost for it.'
			error_msgs.append(message)
			
	if effect_cost != '':
		if cost is not None:
			error = True
			message = 'You have selected a variable value for the ' + name + ' field so the cost for thw ' + power_name + ' must be set as variable.'
			error_msgs.append(message)
		if rule_cost != '':
			error = True
			message = 'Since you set a cost for the ' + name + ' field, you cannot set an overall cost for this rule.'
			error_msgs.append(message)
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def multiple_cost(names, effects_cost, rule_cost, power_cost, extra_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id != '' and extra_id != '0':
		extra_id = integer(extra_id)
		if extra_id is not None:
			extra = db.session.query(Extra).filter_by(id = extra_id).first()
			if extra is not None:
				cost = extra.cost
				power_name = extra.name + ' Extra'
	else:
		cost = power_cost
		power_name = 'Base Power'

	multiple = 0
	for	e in effects_cost:
		if e != '':
			multiple += 1
			
	if multiple > 1:
		if rule_cost != '':
			error = True
			message = 'You set multiple possible costs for the ' + names + ' fields so so you cannot set a overall cost for this rule.'
			error_msgs.append(message)
		if cost is not None:
			error = True
			message = 'Since you set multiple costs for ' + names + ' fields you must set a variable cost for the ' + power_name + '.'
			error_msgs.append(message)
			
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def variable_cost(values, names, rule_cost, power_cost, extra_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id != '' and extra_id != '0':
		extra_id = integer(extra_id)
		if extra_id is not None:
			extra = db.session.query(Extra).filter_by(id = extra_id).first()
			if extra is not None:
				cost = extra.cost
				power_name = extra.name + ' Extra'
	else:
		cost = power_cost
		power_name = 'Base Power'

	if cost is None:
		error = True
		for v in values:
			if v != '':
				error = False
		if rule_cost != '':
			error = False

	names_string = ''
	for n in names:
		if names_string == '':
			names_string = n
		else:
			names_string += ' or ' + n

	if error:
		message = 'You set a variable cost for the ' + power_name + ' so you must set a cost for it or set a cost for this rule or set a cost for one of the ' + names_string + ' fields.'
		error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def sense_cost(power, field, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule_check = db.session.query(PowerSenseEffect).filter_by(power_id=power).first()

	if rule_check is None:
		return (errors)

	rules = db.session.query(PowerSenseEffect).filter_by(power_id=power, extra_id=None).all()
	if field != 'x':
		for r in rules:
			if r.cost is not None:
				error = True
				message = 'You created a Sense rule with its own cost.  You must delete that rule or set this powers cost to vsrisble.'
				error_msgs.append(message)
			if r.sense_cost is not None:
				error = True
				message = 'You created a Sense rule that defined a cost for a sense.  You must delete that rule or set this powers cost to vsrisble.'
				error_msgs.append(message)
			if r.subsense_cost is not None:
				error = True
				message = 'You created a Sense rule that defined a cost for a subsense.  You must delete that rule or set this powers cost to vsrisble.'
				error_msgs.append(message)
	else:
		for r in rules:
			error = True
			if r.cost is not None:
				error = False
			if r.sense_cost is not None:
				error = False
			if r.subsense_cost is not None:
				error = False
			if error:
				message = 'You set a variable cost for this power but created a Sense rule that did not set a cost.  Set a cost for this power or delete the rule and recreate it, this time setting a cost for the rule or for a sense and/or subsense.'
				error_msgs.append(message)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def power_rules(power, errors):
	error_msgs = errors['error_msgs']
	error = True

	rule = db.session.query(PowerAltCheck).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerAction).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerChar).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerCirc).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerCreate).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerDamage).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerDefense).filter_by(power_id = power).first()
	if rule is not None:
		error = False
	
	rule = db.session.query(PowerDegMod).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerEnv).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(Levels).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerMinion).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerMod).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerMove).filter_by(power_id = power).first()
	if rule is not None:
		error = False
	
	rule = db.session.query(PowerOpposed).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerRanged).filter_by(power_id = power).first()
	if rule is not None:
		error = False
	
	rule = db.session.query(PowerResist).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerResistBy).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerReverse).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerSenseEffect).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	rule = db.session.query(PowerTime).filter_by(power_id = power).first()
	if rule is not None:
		error = False

	if error:
		message = 'You must create at least one rule before you can save this power.'
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

def valid_extra(power, errors):
	error_msgs = errors['error_msgs']
	error = False

	rule = db.session.query(PowerAltCheck).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerAltCheck).filter_by(power_id = power).all()
		name = 'Alternate Check'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerAction).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerAction).filter_by(power_id = power).all()	
		name = 'Action Change'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)
				
	rule = db.session.query(PowerChar).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerChar).filter_by(power_id = power).all()
		name = 'Changes Character Trait'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerCirc).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerCirc).filter_by(power_id = power).all()
		name = 'Circumstance Modifier'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerCreate).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerCreate).filter_by(power_id = power).all()
		name = 'Create'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerDamage).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerDamage).filter_by(power_id = power).all()
		name = 'Damage'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerDefense).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerDefense).filter_by(power_id = power).all()
		name = 'Defensive Effect'
		'Defense'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerDegMod).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerDegMod).filter_by(power_id = power).all()
		name = 'Degree of Success/Failure Modifier'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerEnv).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerEnv).filter_by(power_id = power).all()
		name = 'Environment Effect'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(Levels).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(Levels).filter_by(power_id = power).all()
		name = 'Level'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerMinion).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerMinion).filter_by(power_id = power).all()
		name = 'Minion'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerMod).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerMod).filter_by(power_id = power).all()
		name = 'Modifier'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	rule = db.session.query(PowerMove).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerMove).filter_by(power_id = power).all()
		name = 'Movement'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	
	rule = db.session.query(PowerOpposed).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerOpposed).filter_by(power_id = power).all()
		name = 'Opposed Check'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerRanged).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerRanged).filter_by(power_id = power).all()
		name = 'Ranged'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)

	
	rule = db.session.query(PowerResist).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerResist).filter_by(power_id = power).all()
		name = 'Resistance Modifier'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerResistBy).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerResistBy).filter_by(power_id = power).all()		
		name = 'Resisted By'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerReverse).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerReverse).filter_by(power_id = power).all()
		name = 'Reverse Effect'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerSenseEffect).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerSenseEffect).filter_by(power_id = power).all()
		name = 'Sense Effect'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	rule = db.session.query(PowerTime).filter_by(power_id = power).first()
	if rule is not None:
		rule = db.session.query(PowerTime).filter_by(power_id = power).all()
		name = 'Time Effect'
		for r in rule:
			extra_id = r.extra_id
			if extra_id is not None:
				extra = db.session.query(Extra).filter_by(id = extra_id).first()
				if extra is None:
					error = True
					message = 'You created a ' + name + ' rule that is assigned to an extra you must have created and deleted. You must delete that ' + name + ' rule.'
					error_msgs.append(message)


	if error:
		message = 'You must create at least one rule before you can save this power.'
		error_msgs.append(message)
		errors['error_msgs'] = error_msgs
		errors['error'] = error

	return (errors)

