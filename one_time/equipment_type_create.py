
@app.route('/equiptype/create')
def equiptype_create():

	entries = ['General Equipment', 'Electronics', 'Criminal Gear', 'Surveillance Gear', 'Survival Gear', 'Utility Belt']

	for i in entries:

		entry = EquipType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = EquipType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('equipment type added')