
@app.route('/table/db')
def table_db_columns_create():

	tablename =  'Subsense'

	name = 'All SubSenses'

	entry = SubSense(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = SubSense(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = SubSense(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = SubSense(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = SubSense(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Active Power'

	entry = SubSense(active=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(SubSense).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (tablename + ' db added')

