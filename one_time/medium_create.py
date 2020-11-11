@app.route('/mediumtype/create')
def mediumtype_create():

	medium = ['Material', 'Energy']

	for i in medium:

		entry = Medium(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

@app.route('/materialtype/create')
def materialtype_create():

	medium = ['Gas', 'Liquid', 'Earth', 'Biological']

	for i in medium:

		entry = Medium(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')


@app.route('/energytype/create')
def energytype_create():

	medium = ['Electromagnetic', 'Gravity', 'Kinetic', 'Divine', 'Magical', 'Psionic', 'Cosmic']

	for i in medium:

		entry = Medium(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

@app.route('/medium/create')
def medium_create():

	medium_gas = ['Air']
	
	medium_liquid = ['Water']
	
	medium_earth = ['Soil', 'Rock', 'Sand']
	
	medium_biological = ['Acid', 'Blood']

	for i in medium_gas:

		entry = Medium(name=i, medium_type=1, material_type=1)
		db.session.add(entry)
		db.session.commit()

	for i in medium_liquid:

		entry = Medium(name=i, medium_type=1, material_type=2)
		db.session.add(entry)
		db.session.commit()

	for i in medium_earth:

		entry = Medium(name=i, medium_type=1, material_type=3)
		db.session.add(entry)
		db.session.commit()

	for i in medium_biological:

		entry = Medium(name=i, medium_type=1, material_type=4)
		db.session.add(entry)
		db.session.commit()

	medium_electromagnetic = ['Electricity', 'Light', 'Radio', 'Radiation']

	for i in medium_electromagnetic:

		entry = Medium(name=i, medium_type=1, energy_type=1)
		db.session.add(entry)
		db.session.commit()

	

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

