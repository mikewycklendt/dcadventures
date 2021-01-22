
@app.route('/equiptype/create')
def equiptype_create():

	entries = ['Camera', 'Cell Phone', 'Commlink', 'Computer', 'Audio Recorder', 'Video Camera']

	for i in entries:

		entry = Equipment(name=i, type_id=1, cost=1)
		db.session.add(entry)
		db.session.commit()

	entries = ['Handcuffs', 'Lock Release Gun', 'Resistable']

	for i in entries:

		entry = Equipment(name=i, type_id=2, cost=2)
		db.session.add(entry)
		db.session.commit()


	results = EquipType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('equipment type added')