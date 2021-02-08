


class SkillBonus(db.Model):

	condition = db.Column(db.String())



class SkillCheck(db.Model):
	
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	
	
class SkillCirc(db.Model):

	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())


class SkillDC(db.Model):
	
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	
	
class SkillDegree(db.Model):

	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())


class SkillMod(db.Model):
	
	condition = db.Column(db.String())
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	
	
