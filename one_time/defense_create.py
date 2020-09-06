@app.route('/defense/create')
def defense_create():

	defenses = []

	defenses.append({'name': 'Dodge',
						'ability_id': 3,
						'description': 'Dodge defense is based on Agility rank. It includes reaction time, quickness, nimbleness, and overall coordination, used to avoid ranged attacks or other hazards where reflexes and speed are important.'
						, 'modifier_id': 4})
	defenses.append({'name': 'Fortitude',
						'ability_id': 2,
						'description': 'Fortitude defense is based on Stamina and measures health and resistance to threats like poison or disease. It incorporates constitution, ruggedness, metabolism, and immunity.'
						, 'modifier_id': 4)}
	defenses.append({'name': 'Parry',
						'ability_id': 5,
						'description': 'Parry defense is based on Fighting. It is the ability to counter, duck, or otherwise evade a foe’s attempts to strike you in close combat through superior fighting ability.'
						, 'modifier_id': 4
	defenses.append({'name': 'Toughness',
						'ability_id': 2,
						'description': 'Toughness defense is based on Stamina and is resistance to direct damage or harm, and overall durability.'
						, 'modifier_id': 4 })
	defenses.append({'name': 'Will',
						'ability_id': 7,
						'description': 'Will defense is based on Awareness rank. It measures mental stability, level-headedness, determination, selfconfidence, self-awareness, and willpower, and is used to resist mental or spiritual attacks.'
						, 'modifier_id': 4 })
	for defense in defenses:
		name = defense['name']
		ability_id = defense['ability_id']
		description = defense['description']
		modifier_id = 4

		entry = Defense(name=name, ability_id=ability_id, description=description, modifier_id=modifier_id)
		db.session.add(entry)
		db.session.commit()

	additions = Defense.query.all()
	for addition in additions:
		defense_id = addition.id
		name = addition.name
		ability_id = addition.ability_id
		description = addition.description
		modifier = addition.modifier_id

		print (defense_id)
		print (name)
		print (ability_id)
		print (description)
		print (modifier)

	return ('defense')
