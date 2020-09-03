@app.route('/check/create')
def check_create():

	checks = []

	checks.append({
		'name': 'Check',
		'critical': True,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': True,
		'graded': True
	})

	checks.append({
		'name': 'Opposed Check',
		'critical': True,
		'dc': False,
		'opposed': True,
		'automatic': False,
		'routine': True,
		'graded': True
	})

	checks.append({
		'name': 'Routine Check',
		'critical': False,
		'dc': False,
		'opposed': False,
		'automatic': True,
		'routine': True,
		'graded': False
	})

	for check in checks:
		name = check['name']
		critical = check['critical']
		dc = check['dc']
		opposed = check['opposed']
		automatic = check['automatic']
		routine = check['routine']
		graded = check['graded']

		entry = Check(name=name, critical=critical, dc=dc, opposed=opposed, automatic=automatic, routine=routine, graded=graded)
		db.session.add(entry)
		db.session.commit()

	results = Check.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Checks Added')




