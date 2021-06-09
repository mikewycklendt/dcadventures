
@app.route('/table/db')
def table_db_columns_create():

	name = 'Primary Check'

	entry = PowerCheckType(primary=True, name=name)
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerCheckType).filter_by(power_id=None).all()

	for result in results:
		print (result.id)
		print (result.name)

	entry = PowerOpposedType(primary=True, name=name)
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerOpposedType).filter_by(power_id=None).all()

	for result in results:
		print (result.id)
		print (result.name)

	entry = PowerOpposed(primary=True, keyword=name)
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerOpposed).filter_by(power_id=None).all()

	for result in results:
		print (result.id)
		print (result.keyword)
		
	entry = PowerCheck(primary=True, keyword=name)
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerCheck).filter_by(power_id=None).all()

	for result in results:
		print (result.id)
		print (result.keyword)


	return (name + ' db added')

