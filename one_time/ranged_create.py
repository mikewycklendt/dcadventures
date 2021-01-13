
@app.route('/ranged/create')
def ranged_create():

	entries = ['Personal', 'Close', 'Ranged', 'Perception']

	for i in entries:

		entry = Ranged(name=i, show=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Ranked'} 

	for i in entries:

		entry = Ranged(name=i, show=False)
		db.session.add(entry)
		db.session.commit()

	results = Ranged.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('ranged added')