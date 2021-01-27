
@app.route('/conceal/create')
def conceal_create():

	entries = []

	entries.append({'name': 'Awesome',
					'size': ,
					'strength': 20,
					'toughness': 15,
					'defense': -10})

	entries.append({'name': 'Colossal',
					'size': ,
					'strength': ,
					'toughness': ,
					'defense': })

	entries.append({'name': '',
					'size': ,
					'strength': ,
					'toughness': ,
					'defense': })

	entries.append({'name': '',
					'size': ,
					'strength': ,
					'toughness': ,
					'defense': })

	entries.append({'name': '',
					'size': ,
					'strength': ,
					'toughness': ,
					'defense': })

	entries.append({'name': '',
					'size': ,
					'strength': ,
					'toughness': ,
					'defense': })

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
		print ('strength: ' + str(result.strength))
		print ('toughness: ' + str(result.toughness))
		print ('defense: ' + str(result.defense))

	return ('concealment added')