
@app.route('/weapon/create')
def weapon_create():

	entries = ['Brass Knuckles', 'Club', 'Knife', 'Pepper Spray', 'Stun Gun']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=1, cost=2, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Battleaxe', 'Sword', 'Spear', 'Warhammer']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=2, cost=3, description=description)
		db.session.add(entry)
		db.session.commit()
	
	entries = ['Chain', 'Chainsaw', 'Nunchaku', 'Whip']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=1, type_id=3, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Holdout Pistol', 'Light Pistol', 'Heavy Pistol', 'Machine Pistol', 'Submachine Gun', 'Shotgun', 'Assault Rifle', 'Sniper Rifle', 'Bow', 'Crossbow']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=1, cost=2, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Blaster Pistol', 'Blaster Rifle', 'Taser']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=2, cost=3, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Flamethrower', 'Grenade Launcher', 'Rocket Launcher']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=3, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()




	results = Weapon.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('equipment added')