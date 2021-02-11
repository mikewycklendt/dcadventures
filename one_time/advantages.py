

@app.route('/advantages/all')
def advantages_all_create():


	names = ['Accurate Attack',
			'Agile Feint',
			'All-Out Attack',
			'Animal Empathy',
			'Artificer',
			'Assessment',
			'Attractive',
			'Beginners Luck',
			'Benefit',
			'Chokehold',
			'Close Attack',
			'Connected',
			'Contacts',
			'Daze',
			'Defensive Attack',
			'Defensive Roll',
			'Diehard',
			'Eidetic Memory',
			'Equipment',
			'Evasion',
			'Extraordinary Effort',
			'Fascinate',
			'Fast Grab',
			'Favored Environment',
			'Favored Foe',
			'Fearless',
			'Grabbing Finesse',
			'Great Endurance',
			'Hide In Plain Sight',
			'Improved Aim',
			'Improved Critical',
			'Improved Defense',
			'Improved Disarm',
			'Improved Grab',
			'Improved Initiative',
			'Improved Hold',
			'Improved Smash',
			'Impproved Trip',
			'Improvised Tools',
			'Inspire',
			'Instant Up',
			'Interpose',
			'Inventor',
			'Jack-of-All-Trades',
			'Languages',
			'Leadership',
			'Luck',
			'Minion',
			'Move-By Action',
			'Power Attack',
			'Precise Attack',
			'Prone Fighting',
			'Quick Draw',
			'Ranged Attack',
			'Redirect',
			'Ritualist',
			'Second Chance',
			'Seize Initiative',
			'Set-Up',
			'Sidekick',
			'Skill Mastery',
			'Startle',
			'Takedown',
			'Taunt',
			'Teamwork',
			'Throwing Mastery',
			'Tracking',
			'Trance',
			'Ultimate Effort',
			'Uncanny Dodge',
			'Weapon Bind',
			'Weapon Break',
			'Well-Informed']

	for name in names:

		entry = Advantage(show=True, name=name, base=True )
		db.session.add(entry)
		db.session.commit()

	results = Advantage.query.all()

	for r in results:
		print(str(r.id) + ' ' + r.name)

	return ('advantages added')