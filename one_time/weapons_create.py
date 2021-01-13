
@app.route('/conceal/create')
def conceal_create():

	entries = ['No Concealment', 'Partial Concealment', 'Total Concealment']

	for i in entries:

		entry = Conceal(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Conceal.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('concealment added')