@app.route('/damage/create')
def damage_create():

	values = ['Bullets', 'Cold', , 'Falling', 'fire']


	for i in values:
		damage_type = 1
		entry = Damage(name=i, damage_type=damage_type)
		db.session.add(entry)
		db.session.commit()

	values = ['Electricity', 'Magic', 'Radiation', 'Sonic']

	for i in values:
		damage_type = 2
		entry = Damage(name=i, damage_type=damage_type)
		db.session.add(entry)
		db.session.commit()

	results = Damage.query.all()

	for result in results:
		print (result.id)
		print (result.damage_type)
		print (result.name)

	return ('damage added')

@app.route('/damagetype/create')
def damage_type_create():

	values = ['Physical', 'Energy']

	for i in values:

		entry = Damage(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Damage.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('damage added')
