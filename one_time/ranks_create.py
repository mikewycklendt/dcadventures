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
		
	return ('ranks added')
