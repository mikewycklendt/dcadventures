
@app.route('/weapon/style')
def weapon_style_create():

	tablename =  'Weapon Style'

	name = 'All Weapon Styles'

	entry = WeaponStyle(all=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = WeaponStyle(current=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = WeaponStyle(any=True, name=name)
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = WeaponStyle(var=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = WeaponStyle(none=True, name=name)
	db.session.add(entry)
	db.session.commit()

	entries = ['Improvised']

	for i in entries:

		entry = WeaponStyle(name=i, improvise=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Swords', 'Knives', 'Axes', 'Spears', 'Whips', 'Clubs', 'Maces', 'Unarmed', 'Lances', 'Hammers', 'Batons']

	for i in entries:

		entry = WeaponStyle(name=i, type_id=1, show=True, base=True)
		db.session.add(entry)
		db.session.commit()

	entries = ['Guns', 'Fire', 'Throwing', 'Rockets']

	for i in entries:

		entry = WeaponStyle(name=i, type_id=2, show=True, base=True)
		db.session.add(entry)
		db.session.commit()

	results = WeaponStyle.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('concealment added')