@app.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h1' 
	table = Ability.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/defense')
def defense():

	title = 'Defense'
	size = 'h2'
	table = Defense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/modifiers')
def modifiers():

	title = 'Modifiers'
	
	size = 'h1'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skills')
def skills():

	title = 'Skills'
	
	size = 'h1'

	table = Skill.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skill/type')
def skill_type():

	title = 'Skill Type'
	
	size = 'h1'

	table = SkillType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/checks')
def checks():

	title = 'Check Types'
	
	size = 'h1'

	table = Check.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/conditions')
def conditions():

	title = 'Basic Conditions'
	
	size = 'h1'

	table = Condition.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/phases')
def phases():

	title = 'Phases'
	
	size = 'h1'

	table = Phase.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/senses')
def senses():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measuretype')
def measurement_type():

	title = 'Measurement Type'
	
	size = 'h1'

	table = MeasureType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/units')
def unit_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Unit.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/ranks')
def rank_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Rank.query.all()

	return render_template('ranks.html', table=table, title=title, size=size)


@app.route('/math')
def math_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Math.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measurements')
def measurements():

	title = 'Measurements Table'
	
	size = 'h3'

	measurements = Measurement.query.all()

	formatted = [measurement.format() for measurement in measurements]
	
	print (formatted)

	table = measure(formatted)

	return render_template('measurements.html', table=table, title=title, size=size)
