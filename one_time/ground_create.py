@app.route('/ground/create')
def ground_create():

	ground = ['Sand', 'Soil', 'Hard Clay', 'Packed Earth', 'Solid Rock', 'Impervious']

	for i in ground:

		entry = Ground(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Ground.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('grounds added')