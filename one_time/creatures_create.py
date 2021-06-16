@app.route('/creatures/create')
def creatures_create():

	entries = ['Alien', 'Animal', 'Construct', 'Metahuman', 'Undead', 'Elves', 'Sea']

	for i in entries:

		entry = Creature(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Creature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('creatures added')

@app.route('/creatures/create')
def creatures_create():

	entries = ['Elves', 'Sea']

	for i in entries:

		entry = Creature(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Creature.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('creatures added')

@app.route('/narrow/create')
def narrow_create():

	entries = ['Dog', 'Falcon', 'Cat']

	for i in entries:

		entry = Narrow(name=i, creature=9, show=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Dolphin', 'Whale', 'Shark']

	for i in entries:

		entry = Narrow(name=i, creature=19, show=True)
		db.session.add(entry)
		db.session.commit()


	entries = ['Same Size and Gender']

	for i in entries:

		entry = Narrow(name=i, creature=21, similar=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Same Mass']

	for i in entries:

		entry = Narrow(name=i, same=True)
		db.session.add(entry)
		db.session.commit()
	

	results = Narrow.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('creatures added')