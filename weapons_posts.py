
def weap_condition_post(entry, body, cells):

	weapon_id = entry.weapon_id
	condition_type = entry.condition_type
	condition = entry.condition
	condition_null = entry.condition_null
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage_value = entry.damage_value
	damage = entry.damage

	damage_value = integer_convert(damage_value)

	updown_select = [{'type': 1, 'name': 'Up'}, {'type': -1, 'name': 'Down'}]
	damage = selects(damage, updown_select)

	vcells = vcell('active', 40, [condition, 'Active'])
	vcells = vcell('change', 60, [condition1, 'to', condition2], vcells)
	vcells = vcell('damage', 40, [damage_value, 'Condition', damage], vcells)
	vcells = vcell('null', 40, [condition_null, 'Nullified'], vcells)
	cells = vcell_add('Condition Effect', condition_type, vcells, cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)


def weap_descriptor_post(entry, body, cells):

	weapon_id = entry.weapon_id
	descriptor = entry.descriptor

	descriptor = name(Descriptor, descriptor)
	
	cells = cell('Descriptor', 25, [descriptor], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)

def weap_benefit_post(entry, body, cells):

	weapon_id = entry.weapon_id
	benefit = entry.benefit

	benefit = name(benefit, descriptor)
	
	cells = cell('Benefit', 25, [benefit], cells)

	body = send(cells, body)
	
	cells.clear()

	return (body)
