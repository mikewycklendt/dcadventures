@app.route('/complexity/create')
def complex_create():

	complexity = []

	complexity.append({
		'name': 'Simple',
		'dc': 15,
		'time': 10
	})
	
	complexity.append({
		'name': 'Moderate',
		'dc': 20,
		'time': 12
	})

	complexity.append({
		'name': 'Complex',
		'dc': 25,
		'time': 14
	})

	complexity.append({
		'name': 'Advanced',
		'dc': 30,
		'time': 16
	})


	for complexi in complexity:
		name = complexi['name']
		dc = complexi['dc']
		time = complexi['time']

		entry = Complex(name=name, dc=dc, time=time)
		db.session.add(entry)
		db.session.commit()

	return ('complexity created')
