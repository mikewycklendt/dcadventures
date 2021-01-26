
@app.route('/weaponcat/create')
def weaponcat_create():

	entries = ['Melee', 'Ranged', 'Grenades and Explosives', 'Accessory']

	for i in entries:

		entry = WeaponCat(name=i)
		db.session.add(entry)
		db.session.commit()

	results = WeaponCat.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('weqpon category added')


@app.route('/weapontype/create')
def weapontype_create():

	entries = ['Simple', 'Aechaic', 'Exotic']

	for i in entries:

		entry = WeaponType(name=i, type_id=1)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Projectile', 'Energy', 'Heavy', 'Thrown']

	for i in entries:

		entry = WeaponType(name=i, type_id=2)
		db.session.add(entry)
		db.session.commit()
		
		
	entries = ['Grenades', 'Explosives']

	for i in entries:

		entry = WeaponType(name=i, type_id=3)
		db.session.add(entry)
		db.session.commit()


	entries = ['Accessories', 'Other']

	for i in entries:

		entry = WeaponType(name=i, type_id=4)
		db.session.add(entry)
		db.session.commit()

	results = WeaponType.query.all()

	for result in results:
		print (result.id)
		print (result.type_id)
		print (result.name)

	return ('weqpon category added')

