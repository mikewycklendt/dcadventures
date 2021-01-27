
@app.route('/vehiclesize/create')
def vehiclesize_create():

	entries = []

	entries.append({'name': 'Awesome',
					'size': 3,
					'strength': 20,
					'toughness': 15,
					'defense': -10})

	entries.append({'name': 'Colossal',
					'size': 2,
					'strength': 16,
					'toughness': 13,
					'defense': -8})

	entries.append({'name': 'Gargantuan',
					'size': 1,
					'strength': 12,
					'toughness': 11,
					'defense': -6})

	entries.append({'name': 'Huge',
					'size': 0,
					'strength': 8,
					'toughness': 9,
					'defense': -4})

	entries.append({'name': 'Large',
					'size': -1,
					'strength': 4,
					'toughness': 7,
					'defense': -2})

	entries.append({'name': 'Medium',
					'size': -2,
					'strength': 0,
					'toughness': 5,
					'defense': 0})

	for i in entries:
		name = i['name']
		strength = i['strength']
		toughness = i['toughness']
		defense = i['defense']
		size = i['size']

		entry = VehicleSize(name = name,
						strength = strength,
						toughness = toughness,
						defense = defense,
						size = size)

		db.session.add(entry)
		db.session.commit()

	results = VehicleSize.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print ('size: ' + str(result.size))
		print ('strength: ' + str(result.strength))
		print ('toughness: ' + str(result.toughness))
		print ('defense: ' + str(result.defense))

	return ('vehicle sizes added')