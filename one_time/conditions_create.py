@app.route('/condition/create')
def create_conditions():

	conditions = []

	conditions.append({
		'name': 'Compelled',
		'description': 'A compelled character is directed by an outside force, but struggling against it; the character is limited to a single standard action each turn, chosen by another, controlling, character. As usual, this standard action can be traded for a move or even free action. Controlled supersedes compelled',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': False
		})

	conditions.append({
		'name': 'Controlled',
		'description': 'A controlled character has no free will; the character’s actions each turn are dictated by another, controlling, character.',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': False
		})

	conditions.append({
		'name': 'Dazed',
		'description': 'A dazed character is limited to a single standard action per round, although the character may use that action to perform a move or free action, as usual. Stunned supersedes dazed.',
		'phase': 1,
		'supercede': 'Stunned',
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': True 
		})

	conditions.append({
		'name': 'Debilitated',
		'description': 'The character has one or more abilities lowered below –5. (See Debilitated Abilities in the Abilities chapter.)',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': True
		})

	conditions.append({
		'name': 'Defenseless',
		'description': 'A defenseless character has active defense bonuses of 0. Attackers can make attacks on defenseless opponents as routine checks (see Routine Checks). If the attacker chooses to forgo the routine check and make a normal attack check, any hit is treated as a critical hit (see Critical Hit). Defenseless characters are often prone, providing opponents with an additional bonus to attack checks (see Prone, later in this section).',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple':True
		})

	conditions.append({
		'name': 'Disabled',
		'phase': 4,
		'supercede': 'Debilitated',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'A disabled character is at a –5 circumstance penalty on checks. If the penalty applies to specific checks, they are added to the name of the condition, such as Attack Disabled, Fighting Disabled, Perception Disabled, and so forth. Debilitated, if it applies to the same trait(s), supersedes disabled.',
		})

	conditions.append({
		'name': 'Fatigued',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': 1,
		'time_unit': 'hour',
		'effects': 'Hindered',
		'description': 'Fatigued characters are hindered. Characters recover from a fatigued condition after an hour of rest.'
		})

	conditions.append({
		'name': 'Hindered',
		'phase': 1,
		'supercede': 'Immobile',
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'A hindered character moves at half normal speed (–1 speed rank). Immobile supersedes hindered.'
		})

	conditions.append({
		'name': 'Immobile',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Immobile characters have no movement speed and cannot move from the spot they occupy, although they are still capable of taking actions unless prohibited by another condition.'
		})

	conditions.append({
		'name': 'Impaired',
		'phase': 4,
		'supercede': 'Disabled',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'An impaired character is at a –2 circumstance penalty on checks. If the impairment applies to specific checks, they are added to the name of the condition, such as Fighting Impaired, Perception Impaired, and so forth. If it applies to the same trait(s), disabled supersedes impaired'
		})

	conditions.append({
		'name': 'Stunned',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Stunned characters cannot take any actions.'
		})


	conditions.append({
		'name': 'Transformed',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Transformed characters have some or all of their traits altered by an outside agency. This may range from a change in the character’s appearance to a complete change in trait ranks, even the removal of some traits and the addition of others! The primary limit on the transformed condition is the character’s power point total cannot increase, although it can effectively decrease for the duration of the transformation, such as when a powerful super hero is turned into an otherwise powerless mouse or frog (obviously based on considerably fewer power points).'
		})

	conditions.append({
		'name': 'Unaware',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'The character is completely unaware of his surroundings, unable to make interaction or Perception checks or perform any action based on them. If the condition applies to a specific sense or senses, they are added to the name of the condition, such as visually unaware, tactilely unaware (or numb), and so forth. Subjects have full concealment from all of a character’s unaware senses.'
		})

	conditions.append({
		'name': 'Vulnerable',
		'phase': 1,
		'supercede': 'Defenseless',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Vulnerable characters are limited in their ability to defend themselves, halving their active defenses (round up the final value). Defenseless supersedes vulnerable.'
		})

	conditions.append({
		'name': 'Weakened',
		'phase': 1,
		'supercede': 'Debilitated',
		'specific': True,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'The character has temporarily lost power points in a trait. See the Weaken effect in the Powers chapter for more. Debilitated supersedes weakened.'
		})

	for condition in conditions:
		name = condition['name']
		phase = condition['phase']
		supercede = condition['supercede']
		specific = condition['specific']
		multiple = condition['multiple']
		time = condition['time']
		unit = condition['time_unit']
		effects = condition['effects']
		description = condition['description']

		entry = Condition(name=name, phase=phase, supercede=supercede, specific=specific, multiple=multiple, time=time, unit=unit, effects=effects, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Condition.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.description)

	return ('conditions added')

