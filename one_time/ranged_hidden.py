
@app.route('/table/db')
def table_db_columns_create():

	name = 'Perception Range'

	entry = PowerRanged(perception=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerRanged).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return (name + ' db added')