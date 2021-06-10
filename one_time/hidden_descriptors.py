
@app.route('/table/db')
def table_db_columns_create():

	name = 'Any Chosen Rare'

	entry = PowerDes(rare=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Uncommon'

	entry = PowerDes(uncommon=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Common'

	entry = PowerDes(common=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Very Commonn'

	entry = PowerDes(very=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Damage Descriptor'

	entry = PowerDes(any_damage=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Origin'

	entry = PowerDes(any_origin=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Source'

	entry = PowerDes(any_source=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Medium Type'

	entry = PowerDes(any_medium_type=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Medium Subtype'

	entry = PowerDes(any_medium_subtype=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Medium'

	entry = PowerDes(any_medium=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Material'

	entry = PowerDes(any_material=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Energy'

	entry = PowerDes(any_energy=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Any Chosen Descriptor'

	entry = PowerDes(any_descriptor=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Base Power Setting'

	entry = PowerDes(power=True, name=name)
	db.session.add(entry)
	db.session.commit()

	name = 'All Descriptors'

	entry = PowerDes(all=True, name=name, hidden=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerDes).filter_by(hidden=True).all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('hidden descriptors added')
