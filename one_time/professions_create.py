@app.route('/job/create')
def job_create():

	entries = ['Soldier', 'Police', 'Yakuza', 'Lawyer', 'Artist', 'Business', 'Carpentry', 'Chef', 'Criminal', 'Dancer', 'Historian', 'Journalist', 'Doctor', 'Musician', 'Magiccian',  'Philosopher', 'Politician', 'Actor', 'Psychiatrist', 'Psychologist', 'Scientist', 'Sociologist', 'Gangster', 'Theologist']

	for i in entries:

		entry = Job(name=i)
		db.session.add(entry)
		db.session.commit()

	results = Job.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('professions added')