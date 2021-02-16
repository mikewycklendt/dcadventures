
@app.route('/fight/create')
def fight_create():

entries = ['Brawling'
'Boxing'
'Capoeira'
'Karate'
'Kickboxing'
'Krav Maga'
'Kung Fu'
'Muay Thai'
'Tae Kwon Do'
'Tang Soo Do'
'Brazilian Jiu-Jitsu'
'Catch Wrestling'
'Jujutsu'
'Luta Livre'
'Russian Sambo'
'Sumo'
'Wrestling'
'Throwing or Takedown Styles'
'Aikido'
'Judo'
'Hapkido'
'Shuai Jiao'
'Kali'
'Iaido'
'Kendo'
'Baguazhang'
'Tai Chi'
'MMA'
'Jeet Kune Do'
'Ninjutsu'
'Shootfighting']

	for i in entries:

		entry = FightStyle(name=i)
		db.session.add(entry)
		db.session.commit()

	results = FightStyle.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('fighting style added')
