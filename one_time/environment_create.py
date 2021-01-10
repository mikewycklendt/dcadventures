@app.route('/env/create')
def env_create():

	environment = ['Underwater', 'Zero Gravity', 'Mountains', 'Jungle', 'Desert', 'Volcano', 'Space', 'Woodlands', 'Arctic']


	for i in environment:

		entry = Environment(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Environment.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('environments added')