@app.route('/benefit/create')
def benefit_create():

	benefit = ['Action', 'Bonus', 'Power', 'Power Stunt', 'Resistance', 'Retry', 'Speed', 'Strength']

	for i in benefit:

		entry = Benefit(name=i, effort=True)
		db.session.add(entry)
		db.session.commit()

	results = Benefit.query.all()

	for result in results:
		approve = db.session.query(Benefit).filter(Benefit.id == result.id)
		approve.approved = True
		db.session.commit()
		db.session.close()
		print (result.id)
		print (result.name)

	return ('benefit added')