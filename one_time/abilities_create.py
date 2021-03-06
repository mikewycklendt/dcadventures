@app.route('/abilities/create')
def abilities_create():
	abilities = []
		
	abilities.append({'name': "Strength",
		'description': ['Damage dealt by your unarmed and strength-based attacks.',
						'How far you can jump.',
						'The amount of weight you can lift, carry, and throw.',
						'Athletics skill checks.'],
		'summary': 'Strength measures sheer muscle power and the ability to apply it. Your Strength rank applies to:'})

	abilities.append({'name': "Stamina",
		'description': ['Toughness defense, for resisting damage.',
						'Fortitude defense, for resisting effects targeting your character’s health.',
						'Stamina checks to resist or recover from things af-fecting your character’s health when a specific de-fense doesn’t apply.'],
		'summary': 'Stamina is health, endurance, and overall physical resil-ience. Stamina is important because it affects a charac-ter’s ability to resist most forms of damage. Your Stamina modifier applies to:'})

	abilities.append({'name': "Agility",
		'description': ['Dodge defense, for avoiding ranged attacks and oth-er hazards.',
						'Initiative bonus, for acting first in combat.',
						'Acrobatics and Stealth skill checks.',
						'Agility checks for feats of coordination, gross move-ment, and quickness when a specific skill doesn’t apply.'],
		'summary': 'Agility is balance, grace, speed, and overall physical coor-dination. Your Agility rank applies to:'})

	abilities.append({'name': "Dexterity",
		'description': ['Attack checks for ranged attacks.',
						'Sleight of Hand and Vehicles skill checks.',
						'Dexterity checks for feats of fine control and preci-sion when a specific skill doesn’t apply.'],
		'summary': 'Dexterity is a measure of hand-eye coordination, precision, and manual dexterity. Your Dexterity rank applies to:'})
					
	abilities.append({'name': "Fighting",
		'description': ['Attack checks for close attacks.',
						'Parry defense, for avoiding close attacks'],
		'summary': 'Fighting measures your character’s ability in close com-bat, from hitting a target to ducking and weaving around any counter-attacks. Your Fighting rank applies to:'})

	abilities.append({'name': "Intellect",
		'description': ['Expertise, Investigation, Technology, and Treatment skill checks.',
						'Intellect checks to solve problems using sheer brain-power when a specific skill doesn’t apply.'],
		'summary': 'Intellect covers reasoning ability and learning. A character with a high Intellect rank tends to be knowledgeable and well educated. Your Intellect modifier applies to:'})

	abilities.append({'name': "Awareness",
		'description': ['Will defense, for resisting attacks on your mind.',
						'Insight and Perception skill checks.',
						'Awareness checks to resolve matters of intuition when a specific skill doesn’t apply.'],
		'summary': 'While Intellect covers reasoning, Awareness describes common sense and intuition, what some might call “wis-dom.” A character with a high Intellect and a low Aware-ness may be an “absent-minded professor” type, smart but not always aware of what’s going on. On the other hand, a not so bright (low Intellect) character may have a great deal of common sense (high Awareness). Your Awareness modifier applies to:'})

	abilities.append({'name': "Presence",
		'description': ['Deception, Intimidation, and Persuasion skill checks.',
						'Presence checks to influence others through force of personality when a specific skill doesn’t apply.'],
		'summary': 'Presence is force of personality, persuasiveness, leader-ship ability and (to a lesser degree) attractiveness. Pres-ence is useful for heroes who intend to be leaders as well as those who strike fear into the hearts of criminals with their presence. Your Presence modifier applies to:'})
	
	for ability in abilities:
		print (ability['name'])
		name = ability['name']
		print (ability['summary'])
		summary = ability['summary']
		description = ability['description']
		newEntry = Ability(name=name, description=description, summary=summary)
		db.session.add(newEntry)
		db.session.commit()
		for describe in description:
			print (describe)



@app.route('/abilities/create')
def abilities_create():


	id = 2
	icon = 'athletics-icon'
	skill = db.session.query(Skill).filter(Skill.id == id).one()
	skill.icon = icon
	db.session.commit()
	db.session.close()

	id = 1
	icon = 'strength-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 2
	icon = 'stamina-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 3
	icon = 'agility-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 4
	icon = 'dexterity-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 5
	icon = 'fighting-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 6
	icon = 'intellect-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 7
	icon = 'awareness-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	id = 8
	icon = 'presence-icon'
	ability = db.session.query(Ability).filter(Ability.id == id).one()
	ability.icon = icon
	db.session.commit()
	db.session.close()

	results = Ability.query.all()

	for result in results:
		print(result.name)
		print(result.icon)

	return ('abilities icons')



@app.route('/ability/db')
def ability_extras_create():

	tablename = 'Ability'

	name = 'All Abilities'

	entry = Ability(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Ability(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Ability(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Ability(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Ability(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Power Rank' 

	entry = Ability(power=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Skill Rank'

	entry = Ability(skill=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Extra Rank'

	entry = Ability(extra=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(Ability).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')
