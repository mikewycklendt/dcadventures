
@app.route('/element/create')
def element_create():

	entries = ['Earth', 'Wind', 'Water', 'Fire']

	for i in entries:

		entry = Element(name=i)
		db.session.add(entry)
		db.session.commit()

	tablename =  'Element'

	name = 'All Elements'

	entry = Element(all=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Current ' + tablename

	entry = Element(current=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Any ' + tablename

	entry = Element(any=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Variable ' + tablename

	entry = Element(var=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'No ' + tablename

	entry = Element(none=True, name=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	

	results = Element.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Elements added')