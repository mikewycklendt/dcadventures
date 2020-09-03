@app.route('/modifierid')
def modifierid():

	modifierid = 1

	abilities = Ability.query.all()

	for ability in abilities:
		ability.modifier_id = 1
		db.session.commit()
		db.session.close()

	table = Ability.query.all()

	for row in table:
		print(row.id)
		print(row.name)
		print(row.modifier_id)

	return ('updated modifieer')
