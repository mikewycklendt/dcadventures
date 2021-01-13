@app.route('/cover/create')
def cover_create():

	entries = ['No Cover', 'Partial Cover', 'Total Cover']

	for i in entries:

		entry = Maneuver(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Maneuver.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('MANEUVERS added')