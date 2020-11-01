@app.route('/materials/create')
def materials_create():

	materials = []

	materials.append({
		'name': 'Paper',
		'toughness': 0
	})
	
	materials.append({
		'name': 'Soil',
		'toughness': 0
	})

	
	materials.append({
		'name': 'Glass',
		'toughness': 1
	})

	materials.append({
		'name': 'Ice',
		'toughness': 1
	})
	
	materials.append({
		'name': 'Rope',
		'toughness': 1
	})
	
	materials.append({
		'name': 'Wood',
		'toughness': 3
	})

	materials.append({
		'name': 'Stone',
		'toughness': 5
	})
	
	materials.append({
		'name': 'Iron',
		'toughness': 7
	})
	
	materials.append({
		'name': 'Reinforced Concrete',
		'toughness': 8
	})
	
	materials.append({
		'name': 'Steel',
		'toughness': 9
	})
	
	materials.append({
		'name': 'Titanium',
		'toughness': 15
	})
	
	materials.append({
		'name': 'Promedtheum',
		'toughness': 20
	})

	for material in materials:
		name = material['name']
		toughness = material['toughness']

		entry = Material(name=name, toughness=toughness)
		db.session.add(entry)
		db.session.commit()

	return ('materials created')
