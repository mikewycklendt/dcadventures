
@app.route('/armortype/create')
def armor_type_create():

	entries = ['Archaic', 'Modern', 'Shield']

	for i in entries:

		entry = ArmorType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Cover.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('armor type added')