@app.route('/range/create')
def range_create():

	ranges = []

	ranges.append({'name': 'Short',
					'distance': 25
					})
					
	ranges.append({'name': 'Medium',
					'distance': 50
					})

	ranges.append({'name': 'Long',
					'distance': 100
					})


	for r in ranges:
		name = r['name']
		distance = r['distance']

		entry = Range(name=name, distance=distance)
		db.session.add(entry)
		db.session.commit()

	results = Range.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('ranges added')