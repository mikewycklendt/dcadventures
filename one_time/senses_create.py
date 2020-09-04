@app.route('/senses/create')
def senses_create():

	senses = ['Sight', 'Hearing', 'Smell', 'Taste', 'Touch']

	for sense in senses:

		entry = Sense(name=sense)
		db.session.add(entry)
		db.session.commit()

	results = Sense.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('senses added')