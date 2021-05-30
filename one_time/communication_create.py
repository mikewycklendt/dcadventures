from db.rule_models import Ability, Defense, Element, Action, EnvCondition, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType, Communication

@app.route('/communication/create')
def communication_create():

	tablename =  'Communication Medium'

	name = 'All Communication Mediums'

	entry = Communication(all=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Communication(current=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Communication(any=True, name=name)
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Communication(var=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Communication(none=True, name=name)
	db.session.add(entry)
	db.session.commit()
	
	visual = ['Lazer Link', 'Fiber-Optic Link']

	auditory = ['Ultrasonic Beam', 'Infrasonic Beam']

	olfactory = ['Pheramones', 'Chemical Markers']

	tactitle = ['Vibratory Carrier-Wave']

	radio = ['AM Radio', 'FM Radio', 'Short-Wave Radio', 'Micro-Waves']

	mental = ['Telepathic Transmission', 'Psychic Link', 'Mystical Sending']

	special = ['Neutrinos', 'Gravitrons', 'Magical Sendings']

	for sense in visual:
		sense_id = 6
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in auditory:
		sense_id = 7
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in olfactory:
		sense_id = 8
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in tactitle:
		sense_id = 9
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in radio:
		sense_id = 10
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in mental:
		sense_id = 11
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	for sense in special:
		sense_id = 12
		entry = Communication(name=sense, sense_id=sense_id, show=True)
		db.session.add(entry)
		db.session.commit()

	results = Communication.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Communication added')