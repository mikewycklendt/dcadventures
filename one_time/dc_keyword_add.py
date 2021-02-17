from db.skill_models import SkillDC


@app.route('/dc/keyword')
def dc_keyword_add():

	id = 2
	keyword = 'A Yard'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
		
	id = 4
	keyword = 'Wide Ledge'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	
	id = 7
	keyword = 'Narrow Ledge'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 8
	keyword = 'Balance Beam'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 9 
	keyword = 'Tightrope'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 10
	keyword = 'Not Vulnerable'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 11
	keyword = 'Normal Speed'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 12
	keyword = 'Stand'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 13
	keyword = 'Ease Fall'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 14
	keyword = 'Ladder'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 15
	keyword = 'Knotted Rope'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 16
	keyword = 'Rope'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 17
	keyword = 'Rock Face'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 18
	keyword = 'Brick Wall'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 19
	keyword = 'Faster'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 20
	keyword = 'Rescue'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 21
	keyword = 'Choppy Water'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 23
	keyword = 'Full Speed'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)
	
	id = 24
	keyword = 'Turbulant Water'

	entry = db.session.query(SkillDC).filter(SkillDC.id == id).one()
	entry.keyword = keyword
	db.session.commit()
	db.session.close()

	result = db.session.query(SkillDC).filter_by(id = id).one()

	print(str(result.id) + ' ' +  result.keyword)

	return ('keywords added')
