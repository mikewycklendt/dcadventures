@app.route('/sources/create')
def sources_create():

	sources = ['Biological', 'Cosmic', 'Divine', 'Extradimensional', 'Magical', 'Moral', 'Psionic', 'Technological', 'Other']

	for i in sources:

		entry = Source(name=i, damage=True)
		db.session.add(entry)
		db.session.commit()

	results = Source.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('sources added')