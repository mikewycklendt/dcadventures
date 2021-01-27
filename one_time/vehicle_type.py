
@app.route('/vehicletype/create')
def vehicletype_create():

	entries = ['Ground', 'Water', 'Air', 'Space', 'Special']

	for i in entries:

		entry = VehicleType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = VehicleType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('vehicle types added')