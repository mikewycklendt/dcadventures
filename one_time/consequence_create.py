@app.route('/consequence/create')
def consequence_create():

	consequence = ['Heat', 'Cold', 'Starvation', 'Thirst', 'Suffocation', 'Fall', 'Poison', 'Disease', 'Radiation', 'Critical Hit', 'Critical Miss', 'Drowning']

	for i in consequence:

		entry = Consequence(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Consequence.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('consequences added')