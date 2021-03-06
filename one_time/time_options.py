

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
	
	name = 'Set by GM'

	entry = SkillTime(gm=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Set by Player'

	entry = SkillTime(player=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Maintaining Action'

	entry = SkillTime(maintain=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Until Next Check'

	entry = SkillTime(check=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()
	
	name = 'Never Again'

	entry = PowerTime(never=True, keyword=name, hide=True )
	db.session.add(entry)
	db.session.commit()

	results = db.session.query(PowerTime).filter_by(hide=True).all()

	for result in results:
		print (result.id)
		print (result.keyword)

	return ('time fields added')
