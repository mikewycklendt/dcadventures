
@app.route('/light/create')
def conceal_create():

	entries = ['Fully Lit', 'Dim', 'Near Dark', 'Total Dark']

	for i in entries:

		entry = Light(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Light.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('light added')