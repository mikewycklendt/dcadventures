

class SkillBonus(db.Model):

	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))



class SkillCheck(db.Model):

	trait = db.Column(db.Integer)


class SkillCirc(db.Model):

	measure_trait = db.Column(db.Integer)


class SkillDC(db.Model):
	
	math_trait = db.Column(db.Integer)
	
	inflict_trait = db.Column(db.Integer)

	measure_trait = db.Column(db.Integer)


class SkillDegree(db.Model):

	inflict_trait = db.Column(db.Integer)

	consequence_trait = db.Column(db.Integer)

	measure_trait = db.Column(db.Integer)



class SkillMod(db.Model):

	bonus_trait = db.Column(db.Integer)

	penalty_trait = db.Column(db.Integer)


class SkillOpposed(db.Model):

	trait = db.Column(db.Integer)

	opponent_trait = db.Column(db.Integer)


class SkillTime(db.Model):

	trait = db.Column(db.Integer)

