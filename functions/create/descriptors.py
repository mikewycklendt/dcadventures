
def descriptor_name(name):
	
	db = SQLAlchemy()

	try:
		query = db.session.query(PowerDes).filter_by(id=name).one()
		name = query.name
	except:
		print('invalid id')
	
	return (name)
