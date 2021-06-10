
@app.route('/table/db')
def table_db_columns_create():


	name = 'Time Rank'

	entry = Unit(time=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Distance Rank'

	entry = Unit(distance=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Speed Rank'

	entry = Unit(speed=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()


	results = db.session.query(Unit).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Unit Ranks db added')
