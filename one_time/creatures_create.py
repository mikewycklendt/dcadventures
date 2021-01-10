@app.route('/creatures/create')
def creatures_create():

	entries = ['Alien', 'Animal', 'Construct', 'mETAHUMAN', 'Undead']

	for i in entries:

		entry = Creature(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Creature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('creatures added')