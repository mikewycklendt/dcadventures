

@app.route('/powers/all')
def powers_all_create():


	for name in names:

		entry = Power(show=True, name=name, base=True )
		db.session.add(entry)
		db.session.commit()

	results = Power.query.all()

	for r in results:
		print(str(r.id) + ' ' + r.name)


Affliction
Alternate Form
Burrowing
Blast
Communication
C