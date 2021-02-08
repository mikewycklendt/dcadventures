

class Weapon(db.Model):
	
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	
	
	

