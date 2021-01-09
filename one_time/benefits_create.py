@app.route('/benefit/create')
def benefit_create():

	benefit = ['Action', 'Bonus', 'Power', 'Power Stunt', 'Resistance', 'Retry', 'Speed', 'Strength']

	for i in benefit:

		entry = Benefit(name=i, effort=True)
		db.session.add(entry)
		db.session.commit()

	results = Benefit.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('origins added')