
@app.route('/cover/create')
def cover_create():

	entries = ['No Cover', 'Partial Cover', 'Total Cover']

	for i in entries:

		entry = Cover(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Cover.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('cover added')