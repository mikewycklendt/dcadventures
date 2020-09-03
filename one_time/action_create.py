@app.route('/action/create')
def action_create():

	actions = []

	actions.append({
		'name': 'Standard Action',
		'cost': True,
		'turn': True,
		'description': 'A standard action generally involves acting upon something, whether it’s an attack or using a power to affect something. You’re limited to one standard action each round.'	
		})

	actions.append({
		'name': 'Move Action',
		'cost': True,
		'turn': True,
		'description': 'A move action, like the name implies, usually involves moving. You can take your move action before or afteryour standard action, so you can attack then move, or move then attack. You cannot, however, normally split-up your move action before and after your standard action. Move actions also include things like drawing weapons, standing up, and picking up or manipulating objects.'	
		})

	actions.append({
		'name': 'Free Action',
		'cost': False,
		'turn': True,
		'description': 'A free action is something so comparatively minor it doesn’t take significant time, so you can perform as many free actions in a round as the GM considers reasonable. Free actions include things like talking (heroes and villains always find time to say a lot in the middle of a fight), dropping something, ending the use of a power, activating or maintaining some other powers, and so forth.'	
		})

	actions.append({
		'name': 'Reaction',
		'cost': False,
		'turn': False,
		'description': 'A reaction is something you do in response to something else. A reaction doesn’t take any significant time, like a free action. The difference is you react in response to something else happening during the round, perhaps not even on your turn. Reactions don’t count against your normal allotment of actions and you can react as often as the circumstances dictate, but only when they dictate.'	
		})

	actions.append({
		'name': 'Multiple Actions',
		'cost': True,
		'turn': True,
		'description': 'This kind of action takes more than one standard action and may take up multiple turns.'	
		})

	for action in actions:
		name = action['name']
		cost = action['cost']
		turn = action['turn']
		description= action['description']

		entry = Action(name=name, cost=cost, turn=turn, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Action.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.cost)
		print (result.turn)
		print (result.description)

	return ('Actions Added') 
