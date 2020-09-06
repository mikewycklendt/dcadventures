@app.route('/modifier/table')
def modifiers_table_create():
	modifiers = []

	modifiers.append({
		'description': 'major penalty',
		'value': -5,
		'modifier_id': 24
		})

	modifiers.append({
		'description': 'penalty',
		'value': -2,
		'modifier_id': 24
		})

	modifiers.append({
		'description': 'bonus',
		'value': 2,
		'modifier_id': 24
		})

	modifiers.append({
		'description': 'major bonus',
		'value': 5,
		'modifier_id': 24
		})
	for modifier in modifiers:
		value = modifier['value']
		modifier_id = modifier['modifier_id']
		description = modifier['description']

		entry = ModifierTable(description=description, value=value, modifier_id=modifier_id)
		db.session.add(entry)
		db.session.commit()

	added = Modifier.query.all()

	for add in added:
		modifier_id = add.id
		description = add.description

		print(modifier_id)
		print(description)


	return ('modifier table added')