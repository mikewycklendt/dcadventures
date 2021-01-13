@app.route('/maneuver/create')
def maneuver_create():

	entries = ['Accurate Attack', 'All-Out Attack', 'Defensive Attack', 'Finishing Attack', 'Power Attack', 'Slam Attack', 'Surprise Attack', 'Team Attack']

	for i in entries:

		entry = Maneuver(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Maneuver.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('MANEUVERS added')