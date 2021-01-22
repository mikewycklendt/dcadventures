
@app.route('/equipment/create')
def equipment_create():

	entries = ['Camera', 'Cell Phone', 'Commlink', 'Computer', 'Audio Recorder', 'Video Camera']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i '.  '
		description = description + description + description + description + description + description

		entry = Equipment(name=i, type_id=2, cost=2, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Handcuffs', 'Lock Release Gun', 'Restraints']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i '.  '
		description = description + description + description + description + description + description

		entry = Equipment(name=i, type_id=3, cost=3 description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Binoculars', 'Concealable Microphone', 'Mini-Tracer', 'Night-Vision Goggles', 'Parabolic Microphone']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i '.  '
		description = description + description + description + description + description + description

		entry = Equipment(name=i, type_id=4, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Camo Clothing', 'Flashh Goggles', 'Fire Extinguisher', 'Gas Mask', 'GPS', 'Multi-Tool', 'Rebreather', 'SCUBA Gear']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i '.  '
		description = description + description + description + description + description + description

		entry = Equipment(name=i, type_id=5, cost=5, description=description)
		db.session.add(entry)
		db.session.commit()


	results = Equipment.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('equipment added')