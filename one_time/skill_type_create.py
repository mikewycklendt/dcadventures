@app.route('/skills/type')
def skill_type_create():

	types = []

	types.append({
		'name': 'Interaction',
		'check_id': 2,
		'group': True,
		'team': False,
		'gm': True,
		'description': 'Certain skills, called interaction skills, are aimed at dealing with others through social interaction. Interaction skills allow you to influence the attitudes of others and get them to cooperate with you in one way or another. Since interaction skills are intended for dealing with others socially, they have certain requirements.\n\n First, you must be able to interact with the subject(s) of the skill. They must be aware of you and able to understand you. If they can’t hear or understand you for some reason, you have a –5 circumstance penalty to your skill check (see Circumstance Modifiers in The Basics). \n\n Interaction skills work best on intelligent subjects, ones with an Intellect rank of –4 or better. You can use them on creatures with Int –5, but again with a –5 circumstance penalty; they’re just too dumb to get the subtleties of your point. You can’t use interaction skills at all on subjects lacking one or more mental abilities. (Try convincing a rock to be your friend—or afraid of you—sometime.) The Immunity effect (see the Powers chapter) can also render characters immune to interaction skills. \n\n You can use interaction skills on groups of subjects at once, but only to achieve the same result for everyone. So you can attempt to use Deception or Persuasion toconvince a group of something, or Intimidation to cow a crowd, for example, but you can’t convince some individuals of one thing and the rest of another, or intimidate some and not others. The GM decides if a particular use of an interaction skill is effective against a group, and may apply modifiers depending on the situation. The general rules for interaction still apply: everyone in the group must be able to hear and understand you, for example, or you suffer a –5 on your skill check against them. Mindless subjects are unaffected, as usual.' 
	})

	types.append({
		'name': 'Manipulation',
		'check_id': 1,
		'group': False,
		'team': True,
		'gm': True,
		'description': 'Some skills, called manipulation skills, require a degree of fine physical manipulation. You need prehensile limbs and a Strength rank or some suitable Precise power effect to use manipulation skills effectively. If your physical manipulation capabilities are impaired in some fashion (such as having your hands tied or full use of only one hand), the GM may impose a circumstance modifier based on the severity of the impairment. Characters lacking the ability to use manipulation skills can still have ranks in them and use them to oversee or assist the work of others (see Team Checks,'
	})
 
	for skill in types:
		name = skill['name']
		check_id = skill['check_id']
		group = skill['group']
		team = skill['team']
		gm = skill['gm']
		description = skill['description']

		entry = SkillType(name=name, check_id=check_id, group=group, team=team, gm=gm, description=description)
		db.session.add(entry)
		db.session.commit()

	results = SkillType.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.description)

	return ('skill types added')
