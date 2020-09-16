@app.route('/ranks/create')
def ranks_create():

	ranks = []

	ranks.append({
		'name': 'This Skill',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'Parent Skill',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'Parent Ability',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'Distance Rank',
		'rank_type': 
	})

	ranks.append({
		'name': 'Speed Rank',
		'rank_type': 
	})

	ranks.append({
		'name': 'Time Rank',
		'rank_type': 
	})

	ranks.append({
		'name': 'Throwing Rank',
		'rank_type': 
	})

	ranks.append({
		'name': 'This Advantage',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'This Power',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'This Extra',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'This Weapon',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'This Equipment',
		'rank_type': 'char'
	})
	
	ranks.append({
		'name': 'This Vehicle',
		'rank_type': 'char'
	})

	ranks.append({
		'name': 'Defense',
		'rank_type': 'char'
	})

	for rank in ranks:
		name= rank['name']
		rank_type = rank['rank_type']

		entry = Rank(name=name)
		db.session.add(entry)
		db.session.commit()

	names = ['Opponent Skill', 'Opponent Power', 'Opponent Ability', 'Opponent Advantage', 'Opponent Equipment', 'Opponent Weapon', 'Opponent Defense', 'Opponent Device', 'Opponent Construct', 'Opponent Speed', 'Opponent Throwing']

	for name in names:
		rank_type = 'opp'

		entry = Rank(name=name, rank_type=rank_type)
		db.sexssion.add(entry)
		db.session.commit()

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
