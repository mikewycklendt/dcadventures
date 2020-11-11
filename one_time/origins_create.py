@app.route('/origins/create')
def origins_create():

	origins = ['Accidental', 'Bestowed', 'Invented', 'Metahuman', 'Training', 'Other']

	for i in origins:

		entry = Origin(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Origin.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('origins added')