@app.route('/skill/table')
def skill_table():

	tables = []

	tables.append(
					{'dc': 5,
					'skill_id': 16,
					'description': 'Easy (low-speed turn)',
					'check_id': 1,
					'circumstance': False,
					'degree': False,
					'measurement':  None,
					'complexity': None,
					'modifier': False
					})
	
	tables.append({'dc': 10,
					'skill_id': 16,
					'description': 'Average (sudden reverse, dodging obstacles)',
					'check_id': 1,
					'circumstance': False,
					'degree': False,
					'measurement':  None,
					'complexity': None,
					'modifier': False
					})

	tables.append({'dc': 15,
					'skill_id': 16,
					'description': 'Difficult (tight turns)',
					'check_id': 1,
					'circumstance': False,
					'degree': False,
					'measurement':  None,
					'distance': None,
					'complexity': None,
					'modifier': False
					})

	tables.append({'dc': 20,
					'skill_id': 16,
					'description': 'Challenging (bootlegger reverse, loop, barrel roll)',
					'check_id': 1,
					'circumstance': False,
					'degree': False,
					'measurement':  None,
					'complexity': None,
					'modifier': False
					})

	tables.append({'dc': 25,
					'skill_id': 16,
					'description': 'Formidable (high-speed maneuvers, jumping or flying around obstacles)',
					'check_id': 1,
					'circumstance': False,
					'degree': False,
					'measurement':  None,
					'complexity': None,
					'modifier': False
					})			


	for table in tables:
		dc = table['dc']
		skill_id = table['skill_id']
		check_id = ['check_id']
		circumstance = ['circumstance']
		degree = ['degree']
		measurement	= ['measurement']
		complexity = ['complexity']
		modifier = ['modifier']		
		descriptioon = table['description']
		
		
		entry = SkillTable(dc=dc, skill_id=skill_id, description=descriptioon, modifier=modifier, complexity=complexity, measurement=measurement, degree=degree, circumstance=circumstance, check_id=check_id)
		db.session.add(entry)
		db.session.commit()

	skill_tables = SkillTable.query.all()

	for skill_table in skill_tables:
		print (skill_table.id)
		print (skill_table.skill_id)

	return ('skill tables created')

