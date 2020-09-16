@APP.route('/combined/create')
def combined_conditions_create():

	conditions = []

	conditions.append({
		'name': 'Normal',
		'conditions':  [],
		'description': 'The character is unharmed and unaffected by other conditions, acting normally.'
		''
	})

	conditions.append({
		'name': 'Standing',
		'conditions':  [],
		'description': 'The character is unharmed and unaffected by other conditions, acting normally.'
	})

	conditions.append({
		'name': 'Asleep',
		'conditions':  [5, 11, 13],
		'description': 'While asleep, a character is defenseless, stunned,and unaware. A hearing Perception check with three ormore degrees of success wakes the character and removesall these conditions, as does any sudden movement (suchas shaking the sleeping character) or any effect allowinga resistance check.'
	
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})

	conditions.append({
		'name': '',
		'conditions':  [],
		'description': ''
	})