@app.route('/units/create')
def units_create():

	units = []

	units.append({
		'name': 'pounds',
		'type_id': 1
	})

	units.append({
		'name': 'tons',
		'type_id': 1
	})

	units.append({
		'name': 'kilotons',
		'type_id': 1
	})

	units.append({
		'name': 'seconds',
		'type_id': 2
	})

	units.append({
		'name': 'minutes',
		'type_id': 2
	})

	units.append({
		'name': 'hours',
		'type_id': 2
	})

	units.append({
		'name': 'days',
		'type_id': 2
	})

	units.append({
		'name': 'weeks',
		'type_id': 2
	})

	units.append({
		'name': 'months',
		'type_id': 2
	})

	units.append({
		'name': 'years',
		'type_id': 2
	})

	units.append({
		'name': 'inches',
		'type_id': 3
	})

	units.append({
		'name': 'feet',
		'type_id': 3
	})

	units.append({
		'name': 'miles',
		'type_id': 3
	})

	units.append({
		'name': 'million miles',
		'type_id': 3
	})

	units.append({
		'name': 'cubic feet',
		'type_id': 4
	})

	units.append({
		'name': 'million cubic feet',
		'type_id': 4
	})

	units.append({
		'name': 'Time Rank',
		'type_id': 2
	})

	for unit in units:
		name = unit['name']
		type_id = unit['type_id']

		entry = Unit(name=name, type_id=type_id)
		db.session.add(entry)
		db.session.commit()

	return ('units created')
