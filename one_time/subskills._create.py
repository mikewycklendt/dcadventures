
@app.route('/close/create')
def subskill_close_create():

	ability = 5
	skill = 3
	check_type = 5
	action = 1
	attack = integer('skill')

	styles = db.session.query(WeaponStyle).filter_by(type_id=1).all()

	for i in styles:

		if i.id == 14:
			description = 'Attack Bonus equal to this rank for all unarmed attacks.'
		else:
			description = 'Attack Bonus equal to this rank for attacks with ' + i.name
 
		entry = SkillBonus(name=i, show=True, base=True, subskill=True, description=description, weapon_style=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')

@app.route('/close/create')
def subskill_ranged_create():

	entries = ['Unarmed']
	ability = 4
	skill = 11
	check_type = 5
	action = 1
	attack = integer('skill')

	styles = db.session.query(WeaponStyle).filter_by(type_id=2).all()

	for i in styles:
	
		description = 'Attack Bonus equal to this rank for attacks with ' + i.name + ' Weapons.'
 
		entry = SkillBonus(name=i, show=True, base=True, subskill=True, description=description, weapon_style=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')


@app.route('/close/create')
def subskill_ranged_create():

	ability = 4
	skill = 11
	check_type = 3
	action = 1
	attack = integer('skill')

	styles = db.session.query(Job).all()

	for i in styles:
	
		description = 'Can perform most ' + i.name + ' related tasks as routine checks.'
 
		entry = SkillBonus(name=i, show=True, base=True, subskill=True, description=description, weapon_style=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')