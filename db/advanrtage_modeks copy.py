


class Advantage(db.Model):
	
	adv_type = db.Column(db.Integer, db.ForeignKey('advantage_type.id'))
	
class AdvAltCheck(db.Model):

	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvCirc(db.Model):
	
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
		
class AdvCombined(db.Model):
	
	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))


class AdvCondition(db.Model):
	
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition_null = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvDC(db.Model):
	
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvDegree(db.Model):

	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class AdvEffort(db.Model):

	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))


class AdvMinion(db.Model):
	
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	player_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	
	
class AdvMod(db.Model):

	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))



class AdvPoints(db.Model):
	
	condition1 = 
	condition2 = 
	
	