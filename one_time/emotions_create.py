@app.route('/emotions/create')
def emotions_create():

	emotions = ['Anger', 'Fear', 'Sadness', 'Happiness', 'Surprise', 'Disgust']

	for emotion in emotions:

		entry = Emotion(name=emotion)
		db.session.add(entry)
		db.session.commit()

	results = Emotion.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('emotions added')