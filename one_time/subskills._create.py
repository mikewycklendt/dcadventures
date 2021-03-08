
@app.route('/close/create')
def subskill_close_create():

	ability = 5
	skill = 3
	check_type = 5
	action = 1
	attack = integer('skill')

	styles = db.session.query(WeaponStyle).filter(WeaponStyle.type_id == 1, WeaponStyle.show == True).all()

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

	styles = db.session.query(WeaponStyle).filter(WeaponStyle.type_id == 1, WeaponStyle.show == True).all()

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


@app.route('/expertise/create')
def subskill_expertise_create():

	ability = db_integer(Ability, 'gm')
	skill = 11
	check_type = 3
	action = 1

	styles = db.session.query(Job).filter(Job.show == True).all()

	for i in styles:
	
		description = 'Can answer all ' + i.name + ' related questions and perform ' + i.name + ' routine tasks as routine checks.'
 
		entry = SkillBonus(name=i, show=True, base=True, subskill=True, description=description, profession=i.id, ability=ability, skill=skill, check_type=check_type, action=action, attack=attack)
		db.session.add(entry)
		db.session.commit()

	results = db.session.query(SkillBonus).filter_by(subskill=True)

	for result in results:
		print (result.id)
		print (result.name)

	return ('subskill added')
