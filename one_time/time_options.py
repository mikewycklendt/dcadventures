

@app.route('/time/options')
def time_db_columns_create():

	name = 'Permanent'

	entry = SkillTime(perm=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Round'
	
	entry = SkillTime(round=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Scene'

	entry = SkillTime(scene=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = 'Instant'

	entry = SkillTime(instant=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	name = '1 Turn'

	entry = SkillTime(turn=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Next Round'

	entry = SkillTime(next=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(SkillTime).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.keyword)

	return ('time fields added')
