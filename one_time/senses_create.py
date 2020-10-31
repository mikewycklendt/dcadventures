@app.route('/senses/create')
def senses_create():

	senses = ['Visual', 'Auditory', 'Olfactory', 'Tactile', 'Radio', 'Mental', 'Special']

	for sense in senses:

		entry = Sense(name=sense)
		db.session.add(entry)
		db.session.commit()

	results = Sense.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('senses added')

@app.route('/subsenses/create')
def subsenses_create():

	visual = ['Normal Sight', 'Darkvision', 'Infravision', 'Low-Light Vision', 'Microscopic Vision', 'Ultravision', 'X-Ray Vision']

	auditory = ['Normal Hearing', 'Sonar (accurate ultrasonic)', 'Ultrasonic Hearing']

	olfactory = ['Normal Smell', 'Normal Taste', 'Scent']

	tactitle = ['Normal Touch', 'Tremorsense']

	radio = ['Radar (accurate radio)', 'Radio']

	mental = ['Mental Awareness', 'Mind Reading', 'Precognition', 'Postcognition']

	for sense in visual:
		sense_id = 6
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	for sense in auditory:
		sense_id = 7
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	for sense in olfactory:
		sense_id = 8
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	for sense in tactitle:
		sense_id = 9
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	for sense in radio:
		sense_id = 10
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	for sense in mental:
		sense_id = 11
		entry = SubSense(name=sense, sense_id=sense_id)
		db.session.add(entry)
		db.session.commit()

	results = SubSense.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('senses added')