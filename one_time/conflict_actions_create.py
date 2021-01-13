@app.route('/conflict/create')
def conflict_action_create():

	actions = ['Aid', 'Aim', 'Attack', 'Charge', 'Defend', 'Disarm', 'Grab', 'Ready', 'Recover', 'Smash', 'Trip']

	for i in actions:

		entry = ConflictAction(name=i, action_id=1)
		db.session.add(entry)
		db.session.commit()

	actions = ['Command', 'Crawl', 'Escape', 'Stand', 'Draw Weapon']

	for i in actions:

		entry = ConflictAction(name=i, action_id=2)
		db.session.add(entry)
		db.session.commit()

	actions = ['Drop Prone', 'Drop an Item']

	for i in actions:

		entry = ConflictAction(name=i, action_id=3)
		db.session.add(entry)
		db.session.commit()

	actions = ['Delay']

	for i in actions:

		entry = ConflictAction(name=i)
		db.session.add(entry)
		db.session.commit()

	results = ConflictAction.query.all()

	for result in results:
		print (result.id)
		print(result.action_id)
		print (result.name)

	return ('actions added')