@app.route('/check/create')
def check_create():

	checks = []

	checks.append({
		'name': 'Team Check',
		'critical': False,
		'dc': True,
		'opposed': True,
		'automatic': False,
		'routine': False,
		'graded': True,
		'fail': None
	})

	checks.append({
		'name': 'Attack Check',
		'critical': True,
		'dc': False,
		'opposed': True,
		'automatic': False,
		'routine': False,
		'graded': False,
		'fail': 1
	})

	checks.append({
		'name': 'Resistance Check',
		'critical': False,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'fail': None
	})

	for check in checks:
		name = check['name']
		critical = check['critical']
		dc = check['dc']
		opposed = check['opposed']
		automatic = check['automatic']
		routine = check['routine']
		graded = check['graded']
		fail = check['fail']

		entry = Check(name=name, critical=critical, dc=dc, opposed=opposed, automatic=automatic, routine=routine, graded=graded, fail=fail)
		db.session.add(entry)
		db.session.commit()

	results = Check.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Checks Added')




