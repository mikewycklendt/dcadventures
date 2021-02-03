
@app.route('/advtype/create')
def advtype_create():

	entries = ['combat', 'Fortune', 'General', 'Skill']

	for i in entries:

		entry = AdvantageType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = AdvantageType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('concealment added')