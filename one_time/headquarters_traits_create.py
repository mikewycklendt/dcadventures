
@app.route('/headquarters_traits/create')
def headquarters_traits_create():

	name = 'Combat Simulator'
	description = 
	items = []

	for i in entries:

		entry = HeadFeature(name=i)
		db.session.add(entry)
		db.session.commit()

		items = []

	results = HeadFeature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('concealment added')