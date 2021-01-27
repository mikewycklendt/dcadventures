
def arm_descriptor_post_errors(data):

	errors = {'error': False, 'error_msgs': []}

	armor_id = data['armor_id']
	columns = data['columns']
	created = data['created']
	font = data['font']
	descriptor = data['descriptor']

	errors = create_check('Armor', armor_id, Armor, errors)

	errors = id_check(Armor, armor_id, 'Armor', errors)
	errors = id_check(Descriptor, descriptor, 'Descriptor', errors)

	errors = required(descriptor, 'Descriptor', errors)

	return (errors)
