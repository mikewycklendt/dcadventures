
@app.route('/weapons/create')
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

		entry = Weapon(name=i, cat_id=2, type_id=4, cost=4, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Blaster Pistol', 'Blaster Rifle', 'Taser']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=5, cost=5, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Flamethrower', 'Grenade Launcher', 'Rocket Launcher']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=6, cost=6, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Bolos', 'Boomerang', 'Javelin', 'Shuriken']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id=7, cost=7, description=description)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Fragmentation Grenade', 'Smoke Grenade', 'Flash Bang Grenade', 'Sleep Gas Grenade', 'Tear Gas Grrenade', 'Dynamite', 'Plastic Explosives']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=4, type_id=8, cost=8, description=description)
		db.session.add(entry)
		db.session.commit()

	entries = ['Laser Sight', 'Stun Ammo', 'Suppressor', 'Targeting Scope']

	for i in entries:
		description = ''
		description = 'This is the description for ' + i + '.  '
		description = description + description + description + description + description + description

		entry = Weapon(name=i, cat_id=2, type_id= 9, cost=9, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Weapon.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('weapons added')