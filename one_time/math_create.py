@app.route('/math/create')
def math_create():

	maths = []

	maths.append({
		'name': 'add'
	})

	maths.append({
		'name': 'subtract'
	})

	maths.append({
		'name': 'multiply'
	})

	maths.append({
		'name': 'divide'
	})

	for math in maths:
		name = math['name']

		entry = Math(name=name)
		db.session.add(entry)
		db.session.commit()

	symbols = []

	symbols.append({
		'id': 1,
		'name': 'add',
		'symbol': '+'
	})

	symbols.append({
		'id': 2,
		'name': 'subtract',
		'symbol': '-'
	})

	symbols.append({
		'id': 3,
		'name': 'multiply',
		'symbol': 'x'
	})

	symbols.append({
		'id': 4,
		'name': 'divide',
		'symbol': '/'
	})

	for sym in symbols:
		math_id = sym['id']
		symbol = sym['symbol']

		math = db.session.query(Math).filter_by(id=math_id)
		math.symbol = symbol
		db.session.commit()
		db.session.close()

	maths = Math.query.all()

	for math in maths:
		print (math.name)
		print (math.symbol)


	return ('maths added')
