@app.route('/deleteitems')
def delete_items():

	todelete = list(range(9, 369))

	print (todelete)
	
	for itemid in todelete:
		item = db.session.query(Ability).filter_by(id=itemid).one()
		db.session.delete(item)
		db.session.commit()
		db.session.close()
	
	table = Ability.query.all()

	for row in table:
		print(row.id)
		print(row.name)

	return ('deleted')