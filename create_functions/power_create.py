
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
from db.linked_models import *

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def ranks_error(id, ranks, base_cost, base_ranks, base_flat, extra_id, power):
	error_msgs = errors['error_msgs']
	error = False

	name = 'base power'

	if extra_id == '':
		error = True
		message = 'You must select an extra or set this variable rank to base power.'
		error_msgs.append(message)
	elif extra_id == '0':
		base_cost = base_cost
		base_ranks = base_ranks
		base_flat = base_flat
	else:
		try:
			extra_id = int(extra_id)
			extra = db.session.query(Extra).filter_by(id=extra_id).one()
			base_cost = extra.cost
			base_ranks = extra.ranks
			base_flat = extra.flat
			name = extra.name
		except:
			error = True
			message = 'There was a problem with that extra.'
			error_msgs.append(message)
	
	
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error
		return (errors)

	if id == '0':
		if base_cost == '':
			error = True
			message = 'You hsve not set the cost for this power yet.  Set the cost before you create a variable rank.'
			error_msgs.append(message)
		elif base_cost == 'x':
			error = True
			message = 'You set the base cost for this power to variable so you must create a variable cost and select it in the box to the left or set the base cost and base ranks values in the main create power form.'
			error_msgs.append(message)
		elif base_ranks == '':
			error = True
			message = 'You hsve not set the ranks for points value for this power yet.  Set the amount of ranks you get for the cost before you create a variable rank.'
			error_msgs.append(message)
		elif base_flat == True:
			error = True
			message = 'You have this power set at a flat cost.  Uncheck the flat cost checkbox in the main create power form to set a variable rank.'
		else:
			try:
				power = int(power)
				ranks = int(ranks)
				power_ranks = db.session.query(PowerRanks).filter(PowerRanks.power_id == power, PowerRanks.extra == None).first()
				if power_ranks is not None:
					power_ranks = db.session.query(PowerRanks).filter(PowerRanks.power_id == power, PowerRanks.extra == None).all()
					for p in power_ranks:
						if power_ranks.ranks == ranks:
							error = True
							message = 'Tou have already created a variable rank with that value for the base power.'
							error_msgs.append(message)
						else: 
							base_ranks = int(base_ranks)
							base_cost = int(base_cost)
							value = ranks / base_ranks
							value = value * base_cost
							value = round(value)
			except:
				error = True
				message = 'There was an error processing that rank.'
				error_msgs.append(message)
	elif id == '':
		error = True
		message = 'You must select a cost before you can set a variable rank.'
		error_msgs.append(message)
	elif id == 'ex':
		if base_flat == True:
			error = True
			message = 'You set the cost for ' + name + ' to flat so you cannot set a variable rank for this extra.'
			error_msgs.append(message)
		else:
			try:
				ranks = int(ranks)
				extra_id = int(extra_id)
				power_ranks = db.session.query(PowerRanks).filter(PowerRanks.extra == extra_id).first()
				if power_ranks is not None:
					power_ranks = db.session.query(PowerRanks).filter(PowerRanks.power_id == power, PowerRanks.extra == None).all()
					for p in power_ranks:
						if power_ranks.ranks == ranks:
							error = True
							message = 'Tou have already created a variable rank with that value for that extra.'
							error_msgs.append(message)
						else:
							value = ranks / base_ranks
							value = value * base_cost
							value = round(value)
			except:
				print ('not an int')
	else:
		try:
			id = int(id)
			get_cost = db.session.query(PowerCost).filter_by(id=id).first()
			if get_cost is None:
				error = True
				message = 'You set the base cost for this power to variable but you have not created a variable cost with the variable cost form.  Set the cost there and select it in the box to the left to create a variable rank.'
				error_msgs.append(message)
			get_cost = db.session.query(PowerCost).filter_by(id=id).one()
			ranks = int(ranks)
			value = ranks / get_cost.rank
			value = value * get_cost.cost
			value = round(value)
		except:
			error = True
			message = 'There was an error processing thst cost.'
			error_msgs.append(message)		

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def ranks_function(id, ranks, base_cost, base_ranks, extra_id):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id is not None:
		extra = db.session.query(Extra).filter_by(id=extra_id).one()
		base_cost = extra.cost
		base_ranks = extra.ranks

	if id is None:
		try:
			base_ranks = int(base_ranks)
			base_cost = int(base_cost)
			value = ranks / base_ranks
			value = value * cost
		except:
			print('not an int')
	else:
		get_cost = db.session.query(PowerCost).filter_by(id=id).one()
		value = ranks / get_cost.rank
		value = value * get_cost.cost
		value = round(value)

	return (value)


def cost_error(cost, id, extra_id, base_cost, base_flat):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id == '0':
		if base_cost != 'x':
			error = True
			message = 'You must set the base cost of this power to variable if you want to create a variable cost for the base power.'
			error_msgs.append(message)
		if base_flat:
			error = True
			message = 'You checked the flat cost check box.  Uncheck that box if you want to create a variable cost.'
			error_msgs.append(message)			
		id = int(id)
		extra = db.session.query(PowerCost).filter(PowerCost.extra == None, PowerCost.power_id == id).first()
		if extra is not None:
			extra = db.session.query(PowerCost).filter(PowerCost.extra == None, PowerCost.power_id == id).all()
			for e in extra:
				try:
					cost = int(cost)
					if e.cost == cost:
						error = True
						message = 'You have already set ' + str(e.rank) + ' ranks to cost ' + str(cost) + ' points for the base power.'
						error_msgs.append(message) 
				except:
					print('not an int')
		try:
			cost = int(cost)
			if cost < 1:
				error = True
				message = 'Base power costs must be positive.'
				error_msgs.append(message)
		except:
			print ('not sn int')
	else:
		try:
			extra_id = int(extra_id)
			extra = db.session.query(PowerCost).filter(PowerCost.extra == extra_id).first()
			if extra is not None:
				extra = db.session.query(PowerCost).filter(PowerCost.extra == extra_id).all()
				for e in extra:
					cost = int(cost)
					if e.cost == cost:
						error = True
						message = 'You have already set ' + str(e.rank) + ' ranks to cost ' + str(cost) + ' points for the base power.'
						error_msgs.append(message) 
		except:
			print('not an int')

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def get_ranks(Table, value):
	
	if value is None:
		value = ''
		return (value)
	else:
		try:
			name_query = db.session.query(Table).filter_by(id=value).one()
			value = name_query.ranks
		except:
			print('no entry')
			value = ''
		finally:
			db.session.close()

	return (value)

def get_cost(value, ranks_id, extra):

	if ranks_id is None:
		ranks = None
	else:
		get_rank = db.session.query(PowerRanks).filter_by(id=ranks_id).one()
		ranks = get_rank.ranks
	
	if value is None:
		if ranks is None:
			value = ''
		else:
			if extra is None:
				value = str(ranks) + ' Ranks at Base Power Cost rate'
			else:
				try:
					extra = db.session.query(Extra).filter_by(id=extra).one()
					value = ranks / extra.ranks
					value = value * extra.cost
					value = round(value)
					value = str(ranks) + ' Ranks for ' + str(value) + ' points'
				except:
					print('no entry')
					value = ''
				finally:
					db.session.close()
	else:
		try:
			cost = db.session.query(PowerCost).filter_by(id=value).one()
			flat = cost.flat
			if flat == False:
				every = 'every '
			else:
				every = ''
			if ranks is None:
				value = str(cost.cost) + ' polnts for ' + every + str(cost.rank) + 'Ranks'
			else:
				value = ranks / cost.rank
				value = value * cost.cost
				value = round(value)
				value = str(ranks) + ' Ranks for ' + str(value) + ' Points'
		except:
			print('no entry')
			value = ''
		finally:
			db.session.close()

	return (value)

def cost_check_table(table, id, check):

	check = db.session.query(table).filter_by(cost=id).first()
	if check is not None:
		check = False
		
	return(check)

def cost_exist(power_id, cost, errors):
	error_msgs = errors['error_msgs']
	error = False

	costs = db.session.query(PowerCost).filter_by(power_id=power_id).first()
	powercosts = db.session.query(PowerCost).filter(PowerCost.power_id == power_id, PowerCost.extra == None).first()
	if costs is None:
		if cost == 'x':
			error = True
			message = 'You set this power to have a variable cost but you never set a variable cost with the variable cost form.  Create a variable cost or set a base power cost.'
			error_msgs.append(message)
		else:
			return (errors)
	else:
		if powercosts is not None and cost != 'x':
			error = True
			message = 'You created a variable cost for this power so you must set the base power cost to variable.'
			error_msgs.append(message)
		for c in costs:
			check = True
			id = c.id
			check = cost_check_table(PowerSenseEffect, id, check)
			check = cost_check_table(PowerMod, id, check)
			check = cost_check_table(PowerMove, id, check)
			check = cost_check_table(PowerCreate, id, check)
			check = cost_check_table(PowerChar, id, check)
			check = cost_check_table(PowerEnv, id, check)
			if check:
				error = True
				message = 'You never assigned the ' + c.keyword + ' cost to a rule.  Assign it to a rule or delete it.'
				error_msgs.append(message)			

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def extra_cost_exist(power_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	extras = db.session.query(Extra).filter_by(power_id=power_id).first()

	if extras is None:
		return (errors)

	extras = db.session.query(Extra).filter_by(power_id=power_id).all()

	for e in extras:
		id = e.id
		if e.cost is None:
			check = db.session.query(PowerCost).filter_by(extra=id).first()
			if check is None:
				error = True
				message = 'You set the extra ' + e.name + ' to have a variable cost but did not set a variable cost for it.  Create the cost for ' + e.name + ' with the variable cost form and assign it to at least one rule before you can save this power.'
				error_msgs.append(message)			

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


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

def degree_check(title, value, multiple, power_id, extra_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	if extra_id == '0':
		extra_id = None
	else:
		extra_id = int(extra_id)

	power_id = int(power_id)

	try:
		get_title = db.session.query(PowerDegreeType).filter_by(power_id=power_id, name=title).first()
		if get_title is None:
			return (errors)
		else:
			title = get_title.id

		check = db.session.query(PowerDegree).filter_by(title=title, value=value, extra_id=extra_id).first()
		if check is not None:
			if multiple == '':
				error = True
				message = 'Tou have set more than one effect for the degree in this degree group so you must select an option from the the if multiple field or create a new group with a new title.'
				error_msgs.append(message)
	except:
		error = True
		message = 'There was an error processing that degree.'
		error_msgs.append(message)
		

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def multiple_error(check, name, table, power_id, errors, title_table=False, column=False):
	error_msgs = errors['error_msgs']
	error = False
	multiple = False

	check = db.session.query(table).filter_by(power_id=power_id).first()
	if check is None:
		error = True
		message = 'You cannot have extra effects for ' + name + ' because you have not created a rule for ' + name + ' yet.  In order for this extra to give an extra ' + name + ' effect you must create more than one rule and set the if multiple field to Chosen with Power.'
		error_msgs.append(message)
	if check is not None:
		if title_table != False:
			check = db.session.query(table).filter_by(power_id=power_id).all()
			for c in check:
				title_id = c.title
				if column != False:
					value = getattr(c, column)
					attribute = getattr(table, column)
					the_filter = attribute == value
					checked = db.session.query(table).filter(table.title == title_id, the_filter, table.extra_id == None).count()
				else:
					checked = db.session.query(table).filter_by(title=title_id, extra_id=None).count()			
				if checked > 1:
					check_title = db.session.query(link_table).filter_by(id=title_id).one()
					if check_title.multiple == 'x':
						multiple = True
		else:
			check = db.session.query(table).filter_by(power_id=power_id, extra_id=None, multiple='x').count()
			if check > 1:
				multiple = True

		if multiple == False:
			error = True
			message = 'You cannot have extra effects for ' + name + ' because you have not created more than one ' + name + ' rule yet and set those rules if multiple fields to chosen with power.  In order for this extra to give an extra ' + name + ' effect you must create more than one rule and set the if multiple field to Chosen with Power.'
			error_msgs.append(message)
			
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def degree_multiple(value, title, power_id, body):
	multiple = False

	try:
		check = db.session.query(PowerDegree).filter_by(title=title, value=value, extra_id=None).count()
		if check > 1:
			check_title = db.session.query(PowerDegreeType).filter_by(id=title).one()
			if check_title.multiple == 'x':
				multiple = True

		body['multiple'] = multiple
	except:
		body['success'] = False
		body['error_msgs'] = ['There Was an error processing this degree']

	return (body)

def one_multiple(table, power_id, body):
	multiple = False

	try:
		check = db.session.query(table).filter_by(power_id=power_id, extra_id=None, multiple='x').count()
		if check > 1:
			multiple = True

		body['multiple'] = multiple
	except:
		body['success'] = False
		body['error_msgs'] = ['There Was an error processing this degree']

	return (body)

def title_multiple(table, title_table, title, power_id, body):
	multiple = False

	try:
		check = db.session.query(table).filter_by(title=title, extra_id=None).count()
		if check > 1:
			check_title = db.session.query(title_table).filter_by(id=title).one()
			if check_title.multiple == 'x':
				multiple = True

		body['multiple'] = multiple
	except:
		body['success'] = False
		body['error_msgs'] = ['There Was an error processing this degree']

	return (body)

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

def power_sense_condition(power_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	check = db.session.query(PowerDegree).filter_by(power_id=power_id, type='sense').first()

	if check is None:
		return (errors)
	else:
		for c in check:
			sense = db.session.query(PowerSenseEffect).filter_by(power_id=power_id, condition_degree=c.id).first()
			if sense is None:
				error = True
				messege = 'You created a degree of success/failure rule with the keyword ' + c.keyword + ' but never set the sense condition in the sense effect form.  Assign that degree of success/failure rule to a sense rule or delete that success/failure rule'
				error_msgs.append(messege)

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def power_reflect_immune(power_id, reflect_immune, errors):
	error_msgs = errors['error_msgs']
	error = False

	if reflect_immune == False: 
		return (errors)

	check = db.session.query(PowerDefense).filter_by(power_id=power_id, immunity=True).first()

	if check is None:
		error = True
		messege = "You chose to limit the reflect effect to attacks to which you are immune but you haven't set an immunity rule yet.  Create an immunity rule for this power or uncheck the Only for Immune Attacks checkbox to create this reflect rule."
		error_msgs.append(messege)

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

def trait_cost(cost, power_id, errors):
	error_msgs = errors['error_msgs']
	error = False

	if cost == 'trait':
		check = db.session.query(PowerChar).filter_by(power_id=power_id, extra_id=None).first()
		if check is None:
			error = True	
			message = 'You selected Trait Cost for this power but that is only a valid option for powers that change character traits.  Select a different cost for this power.'
			error_msgs.append(message)

	check_cost = db.session.query(PowerCost).filter_by(power_id=power_id).first()
	if check is not None:
		for c in check_cost:
			cost = c.id
			if c.cost == 112112:
				check = db.session.query(PowerChar).filter_by(cost=cost).first()
				if check is None:
					error = True	
					message = 'You selected Trait Cost for the variable cost '  + c.keyword + ' but that is only a valid option for powers that change character traits.  You must assign that cost to a changes character traits rule.'
					error_msgs.append(message)
	
	check_extra = db.session.query(Extra).filter_by(power_id=power_id).first()
	if check is not None:
		for c in check_extra:
			extra = c.id
			if c.cost == 112112:
				check = db.session.query(PowerChar).filter_by(power_id=power_id).first()
				if check is None:
					error = True	
					message = 'You selected Trait Cost for the extra '  + c.name + ' but that is only a valid option for powers that change character traits and this power does not have a changes character trait rule assigned to it.  Create that rule or recreate the extra with a different cost.'
					error_msgs.append(message)
		
	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def delete_power(table, power_id, multiple=False):
	body = {}
	body['success'] = True
	body['id'] = power_id
	try:
		if multiple:
			check = db.session.query(table).filter_by(power_id=power_id, extra_id=None, multiple='x').count()
			if check > 1:
				multiple = True
			else:
				multiple = False
			body['multiple'] = multiple

		db.session.query(PowerAction).filter_by(id=power_id).delete()
		db.session.commit()
	except:
		db.session.rollback()
		body['success'] = False
		error_msgs = []
		message = 'Could not delete this entry.'
		error_msgs.append(message)
		body['error_msgs'] = error_msgs
	finally:
		db.session.close()
		print('\n\n' + str(power_id) + ' DELETED\n\n')
		return (body)

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

