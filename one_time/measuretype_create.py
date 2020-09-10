@app.route('/measuretype/create')
def measure_type_create():

	types = []

	types.append({
		'name': 'mass'
	})

	types.append({
		'name': 'time'
	})

	types.append({
		'name': 'distance'
	})

	types.append({
		'name': 'volume'
	})

	for measure in types:
		name = measure['name']

		entry = MeasureType(name=name)
		db.session.add(entry)
		db.session.commit()

	return 'measurement type created'
