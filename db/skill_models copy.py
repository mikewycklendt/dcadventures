

class SkillBonus(db.Model):

	advantage = db.Column(db.Integer, db.ForeignKey('advantages.id'))



class SkillCheck(db.Model):

	trait = db.Column(db.String())


class SkillCirc(db.Model):

	measure_trait = db.Column(db.String())


class SkillDC(db.Model):
	
	math_trait = db.Column(db.String())
	
	inflict_trait = db.Column(db.String())

	measure_trait = db.Column(db.String())


class SkillDegree(db.Model):

	inflict_trait = db.Column(db.String())

	consequence_trait = db.Column(db.String())

	measure_trait = db.Column(db.String())



class SkillMod(db.Model):

	bonus_trait = db.Column(db.String())

	penalty_trait = db.Column(db.String())


class SkillOpposed(db.Model):

	trait = db.Column(db.String())

	opponent_trait = db.Column(db.String())


class SkillTime(db.Model):

	trait = db.Column(db.String())

