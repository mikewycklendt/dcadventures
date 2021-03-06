@app.route('/mediumtype/create')
def mediumtype_create():

	medium = ['Material', 'Energy']

	for i in medium:
		
		entry = MediumType(name=i, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = MediumType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

@app.route('/mediumtype/create')
def mediumtype_create():

	name = 'Physical Damage'

	entry = Descriptor(name=name, medium_type=1, damage=True)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Energy Damage'

	entry = Descriptor(name=name, medium_type=2, damage=True)
	db.session.add(entry)
	db.session.commit()

	results = Descriptor.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')



@app.route('/mediumsubtype/create')
def mediumsubtypetype_create():

	materials = ['Gas', 'Liquid', 'Earth', 'Biological']

	for i in materials:

		entry = MediumSubType(name=i, medium_type=1, damage=True)
		db.session.add(entry)
		db.session.commit()

	energies = ['Electromagnetic', 'Gravity', 'Kinetic', 'Divine', 'Magical', 'Psionic', 'Cosmic']

	for i in energies:

		entry = MediumSubType(name=i, medium_type=2, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = MediumSubType.query.all()

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

		entry = Medium(name=i, medium_type=1, medium_subtype=1, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_liquid:

		entry = Medium(name=i, medium_type=1, medium_subtype=2, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_earth:

		entry = Medium(name=i, medium_type=1, medium_subtype=3, damage=True)
		db.session.add(entry)
		db.session.commit()

	for i in medium_biological:

		entry = Medium(name=i, medium_type=1, medium_subtype=4, damage=True)
		db.session.add(entry)
		db.session.commit()

	medium_electromagnetic = ['Electricity', 'Light', 'Radio', 'Radiation']

	for i in medium_electromagnetic:

		entry = Medium(name=i, medium_type=2, medium_subtype=5, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = Medium.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('medium added')

