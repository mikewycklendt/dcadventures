
@app.route('/subskill/create')
def subskill_create():

	entries = ['Unarmed']
	ability = 5
	skill = 3
	check_type = 5
	action = 1
	attack = integer('skill')


	for i in entries:

		entry = SkillBonus(name=i, show=True, base=True, subskill=True, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')