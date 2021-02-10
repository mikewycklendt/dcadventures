
@app.route('/power/duration')
def powerduration_create():

	entries = ['Instant', 'Concentration', 'Sustained', 'Continuous', 'Permanent']


	for i in entries:

		entry = PowerDuration(name=i)
		db.session.add(entry)
		db.session.commit()

	results = PowerDuration.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('power duration added')