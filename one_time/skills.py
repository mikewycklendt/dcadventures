

@app.route('/skills/all')
def skills_all_create():

	names = ['Balancing',
			'Maneuvering',
			'Standing',
			'Tumbling',
			'Climbing',
			'Jumping',
			'Running',
			'Swimming',
			'Bluffing',
			'Disguise',
			'Feinting',
			'Innuendo',
			'Tricking',
			'Detect Illusion',
			'Detect Influence',
			'Evaluate',
			'Innuendo',
			'Resist Influence',
			'Coercing',
			'Demoralizing',
			'Intimidating Minions',
			'Search',
			'Gather Evidence',
			'Analyze Evidence',
			'Gather Information',
			'Surveillance',
			'Hearing',
			'Seeing',
			'Other Senses',
			'Concealing',
			'Contorting',
			'Escaping',
			'Legerdemain',
			'Stealing',
			'Hiding',
			'Tailing',
			'Operating',
			'Building',
			'Repairing',
			'Jury-Rigging',
			'Demolitions',
			'Inventing',
			'Security',
			'Diagnosis',
			'Provide Care',
			'Revive',
			'Stabalize',
			'Treat Disease',
			'Treat Poison']

	for name in names:

		entry = SkillBonus(show=True, name=name, base=True )
		db.session.add(entry)
		db.session.commit()

	results = SkillBonus.query.all()

	for r in results:
		print(str(r.id) + ' ' + r.name)

	return ('skills added')