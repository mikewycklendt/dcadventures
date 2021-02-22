class Advantage(db.Model):
	
	trait = db.Column(db.Integer)

	replaced_trait =  db.Column(db.Integer)
	
	skill = db.Column(db.Integer)
	
	invent_trait = db.Column(db.Integer)
	
	gm_trait = db.Column(db.Integer)

class AdvAltCheck(db.Model):

	trait = db.Column(db.Integer)



class AdvCirc(db.Model):

	check_trait = db.Column(db.Integer)

	null_trait = db.Column(db.Integer)

	null_override_trait = db.Column(db.Integer)


class AdvDC(db.Model):

	math_trait = db.Column(db.Integer)

	check_trait = db.Column(db.Integer)


class AdvDegree(db.Model):
	
	consequence_trait = db.Column(db.Integer)

	circ_trait = db.Column(db.Integer)

	measure_trait = db.Column(db.Integer)


class AdvMinion(db.Model):

	attitude_trait = db.Column(db.Integer)


class AdvMod(db.Model):
	
	bonus_trait = db.Column(db.Integer)

	penalty_trait = db.Column(db.Integer)


class AdvOpposed(db.Model):

	trait = db.Column(db.Integer)

	opponent_trait = db.Column(db.Integer)


class AdvPoints(db.Model):

	ranks_trait = db.Column(db.Integer)



class AdvResist(db.Model):

	trait = db.Column(db.Integer)


class AdvRounds(db.Model):

	trait = db.Column(db.Integer)



class AdvSkill(db.Model):

	trait = db.Column(db.Integer)

	replaced_trait = db.Column(db.Integer)



class AdvTime(db.Model):

	trait = db.Column(db.Integer)

class AdvVariable(db.Model):


	trait = db.Column(db.Integer)

