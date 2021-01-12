@app.route('/check/create')
def check_create():

	checks = []

	checks.append({
		'name': 'Skill Check',
		'critical': True,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': True,
		'compare': False,
		'fail': None
	})

	checks.append({
		'name': 'Opposed Check',
		'critical': True,
		'dc': False,
		'opposed': True,
		'automatic': False,
		'routine': True,
		'graded': False,
		'roll': True,
		'compare': False,
		'fail': 1
	})

	checks.append({
		'name': 'Routine Check',
		'critical': False,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': False,
		'compare': False,
		'fail': None
	})

	checks.append({
		'name': 'Team Check',
		'critical': False,
		'dc': True,
		'opposed': True,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': True,
		'compare': False,
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
		'roll': True,
		'compare': False,
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
		'compare': False,
		'roll': True,
		'fail': None
	})

	checks.append({
		'name': 'Comparison Check',
		'critical': False,
		'dc':False,
		'opposed': True,
		'automatic': True,
		'routine': False,
		'graded': False,
		'compare':True,
		'roll': False,
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
		db.seession.close()

	check = ['Initiative Check']

	for i in check:

		entry = Check(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Check.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('check added')
