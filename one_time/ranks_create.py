@app.route('/ranks/create')
def ranks_create():

	ranks = []

	ranks.append({
		'name': 'This Skill'
	})

	ranks.append({
		'name': 'Parent Skill'
	})

	ranks.append({
		'name': 'Parent Ability'
	})

	ranks.append({
		'name': 'Distance Rank'
	})

	ranks.append({
		'name': 'Speed Rank'
	})

	ranks.append({
		'name': 'Time Rank'
	})

	ranks.append({
		'name': 'Throwing Rank'
	})

	ranks.append({
		'name': 'This Advantage'
	})

	ranks.append({
		'name': 'This Power'
	})

	ranks.append({
		'name': 'This Extra'
	})

	ranks.append({
		'name': 'This Weapon'
	})

	ranks.append({
		'name': 'This Equipment'
	})
	
	ranks.append({
		'name': 'This Vehicle'
	})

	ranks.append({
		'name': 'This Vehicle'
	})

	for rank in ranks:
		name= rank['name']

		entry = Rank(name=name)
		db.session.add(entry)
		db.session.commit()

	names = ['Defense', 'Opponent Skill', 'Opponent Power', 'Opponent Ability', 'Opponent Advantage', 'Opponent Equipment', 'Opponent Weapon', 'Opponent Defense', 'Opponent Device', 'Opponent Construct', 'Opponent Speed', 'Opponent Throwing']

	for name in names:

		entry = Rank(name=name)
		db.sexssion.add(entry)
		db.session.commit()

	units = Rank.query.all()

	for unit in units:
		if 0 < unit.id < 4:
			unit.rank_type = 'char'
		if 3 < unit.id < 8:
			unit.rank_type = 'measure'
		if 7 < unit.id < 16:
			unit.rank_type = 'char'
		if unit.id > 15:
			unit.rank_type = 'opp'

		db.session.commit()
		db.session.close()

	unit_add = []

	unit_add.append({
		'name': 'mass rank',
		'rank_type': 'measure'
	})
	unit_add.append({
		'name': 'volume rank',
		'rank_type': 'measure'
	})

	for rank in unit_add:
		name = rank['name']
		rank_type = rank['rank_type']

		entry = Rank(name=name, rank_type=rank_type)
		db.session.add(entry)
		db.session.commit()
		
	results = Rank.query.all()

	for result in results:
		print (result.name)
		print (result.rank_type)

	return ('ranks added')
