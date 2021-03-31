
@app.route('/temp/create')
def temp_create():

	entries = ['Cold', 'Heat', 'High Pressure', 'Radiation', 'Vaccuum']

	for i in entries:

		entry = EnvCondition(name=i)
		db.session.add(entry)
		db.session.commit()
	
	
	tablename =  'Emvironment Condition'

	name = 'All Environment Conditions'

	entry = EnvCondition(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = EnvCondition(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = EnvCondition(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = EnvCondition(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = EnvCondition(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()


	results = EnvCondition.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('environment conditions added')