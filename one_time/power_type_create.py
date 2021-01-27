
@app.route('/powertype/create')
def powertype_create():

	entries = ['Attack', 'Movement', 'Sensory', 'Control', 'Defense', 'General']

	for i in entries:

		entry = PowerType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = PowerType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('power types added')