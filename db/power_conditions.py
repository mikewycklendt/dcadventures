

class Power(db.Model):

	duration = db.Column(db.Integer, db.ForeignKey('power_duration.id'))
	
		DELETE grab = db.Column(db.Integer)
		DELETE grab_type = db.Column(db.String())

	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_bonus = db.Column(db.Integer)
	conflict_type = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))

	'conflict': self.conflict,
	'conflict_bonus': self.conflict_bonus,
	'conflict_type': self.conflict_type,


class Extra(db.Model):
	
	inherit = db.Column(db.Integer, db.ForeignKey('powers.id'))
	
	


class PowerCirc(db.Model):
	
	null_condition = db.Column(db.String())




class PowerDC(db.Model):
	
	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())
	
	
	
class PowerDegMod(db.Model):
	
	condition1 = db.Column(db.String())	
	condition2 = db.Column(db.String())
	
	
	
class PowerEnv(db.Model):
	
		move_nature = db.Column(db.Integer, db.ForeignKey('nature.id'))


class PowerMinion(db.Model):

	condition = db.Column(db.String())
	player_condition = db.Column(db.String())


class PowerMove(db.Model):
	
	condition = db.Column(db.String())
	
	damage_type = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	
	




class PowerResistBy(db.Model):

	condition1 = db.Column(db.String())
	condition2 = db.Column(db.String())



class PowerSenseEffect(db.Model):
	
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))


