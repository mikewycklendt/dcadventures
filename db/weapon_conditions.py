

class WeapCondition(db.Model):
	
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_null = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	