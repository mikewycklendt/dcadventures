@app.route('/skill/table')
def skill_table():

	tables = []

	tables.append(
					{'dc': 5,
					'skill_id': 16,
					'description': 'Easy (low-speed turn)'}
					)
	
	tables.append({'dc': 10,
					'skill_id': 16,
					'description': 'Average (sudden reverse, dodging obstacles)'}
					)

	tables.append({'dc': 15,
					'skill_id': 16,
					'description': 'Difficult (tight turns)'}
					)

	tables.append({'dc': 20,
					'skill_id': 16,
					'description': 'Challenging (bootlegger reverse, loop, barrel roll)'}
					)

	tables.append({'dc': 25,
					'skill_id': 16,
					'description': 'Formidable (high-speed maneuvers, jumping or flying around obstacles)'}
					)				
				

	for table in tables:
		dc = table['dc']
		skill_id = table['skill_id']
		descriptioon = table['description']

		entry = SkillTable(dc=dc, skill_id=skill_id, description=descriptioon)
		db.session.add(entry)
		db.session.commit()

	skill_tables = SkillTable.query.all()

	for skill_table in skill_tables:
		print (skill_table.id)
		print (skill_table.skill_id)

	return ('skill tables created')

