@app.route('/phases/create')
def phases_create():

	phases = []

	phases.append({
		'name': 'before anything'
	})

	phases.append({
		'name': 'before  actions'
	})

	phases.append({
		'name': 'after action'
	})

	phases.append({
		'name': 'before check'
	})

	phases.append({
		'name': 'after check'
	})

	for phase in phases:
		name = phase['name']

		entry = Phase(name=name)
		db.session.add(entry)
		db.session.commit()

	results = Phase.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('phases added')
