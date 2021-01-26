
def weap_condition_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	Created = data['created']
	font = data['font']
	condition_type = data['condition_type']
	condition = data['condition']
	condition_null = data['condition_null']
	condition1 = data['condition1']
	condition2 = data['condition2']
	damage_value = data['damage_value']
	damage = data['damage']

	errors = create_check('Weapon', weapon_id, Weapon, errors)
	
	errors = int_check(damage_value, 'Condition Damage', errors)
	errors = int_check(damage, 'Damage Direction', errors)

	errors = db_check(Weapon, weapon_id, 'Weapon', errors)

	errors = required(condition_type, 'Condition Type', errors)

	errors = variable_fields('active', 'Active Condition', condition_type, [condition], errors)
	errors = variable_field('active', condition_type, 'Condition', condition, errors)
	errors = variable_fields('change', 'CondItion Change', condition_type, [condition1, condition2], errors)
	errors = variable_field('change', condition_type, 'Starting CondItion', condition1, errors)
	errors = variable_field('change', condition_type, 'Ending CondItion', condition2, errors)
	errors = variable_fields('damage', 'Condition Damage', condition_type, [damage_value, damage], errors)
	errors = variable_field('damage', condition_type, 'Damage Degrees', damage_value, errors)
	errors = variable_field('damage', condition_type, 'Condition Damage Direction ', damage, errors)
	errors = variable_fields('null', 'Nullify Condition', condition_type, [condition_null], errors)
	errors = variable_field('null', condition_type, 'Nullified Condition', condition_null, errors)


	return(errors)

def weap_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	descriptor = data['descriptor']

	errors = id_check(Weapon, weapon_id, 'Weapon', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)

	return (errors)

def weap_benefit_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	weapon_id = data['weapon_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	benefit = data['benefit']

	errors = id_check(Weapon, weapon_id, 'Weapon', errors)
	errors = id_check(Benefit, descriptor, 'Benefit', errors)

	errors = required(benefit, 'Benefit', errors)

	return (errors)
