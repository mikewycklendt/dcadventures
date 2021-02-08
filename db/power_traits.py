

class Power(db.Model):
	
	routine_trait = db.Column(db.Integer)
	
	partner_trait = db.Column(db.Integer)
	
	
	
class PowerAltCheck(db.Model):

	trait = db.Column(db.Integer)


class PowerChar(db.Model):

	trait = db.Column(db.Integer)

	weaken_trait = db.Column(db.Integer)

		weaken_broad = db.Column(db.String())

	reduced_trait = db.Column(db.Integer)
	
	points_trait = db.Column(db.Integer)
	
	
class PowerCirc(db.Model):
	
	check_trait = db.Column(db.Integer)

	null_trait = db.Column(db.Integer)


class PowerCreate(db.Model):
	
	move_player_trait = db.Column(db.Integer)
	
	trap_trait = db.Column(db.Integer)

	trap_resist_trait = db.Column(db.Integer)

	ranged_trait = db.Column(db.Integer)
	
	weapon_trait = db.Column(db.Integer)
	
	

class PowerDamage(db.Model):

	trait = db.Column(db.Integer)



class PowerDC(db.Model):

	math_trait = db.Column(db.Integer)

	check_trait = db.Column(db.Integer)


class PowerDefense(db.Model):

	
	defense = db.Column(db.Integer, db.ForeignKey('defenses.id'))
	
	reflect_opposed_trait = db.Column(db.Integer)
	
	reflect_resist_trait = db.Column(db.Integer)
	
	immunity_trait = db.Column(db.Integer)
	
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))


class PowerDegMod(db.Model):

	circ_trait = db.Column(db.Integer)

	measure_trait = db.Column(db.Integer)

	consequence_trait = db.Column(db.Integer)

class PowerEnv(db.Model):

	visibility_trait = db.Column(db.Integer)


class PowerMinion(db.Model):

	attitude_trait = db.Column(db.Integer)


class PowerMod(db.Model):
	
	limited_trait = db.Column(db.Integer)

	reflect_trait = db.Column(db.Integer)

	subtle_opponent_trait = db.Column(db.Integer)

	subtle_null_trait = db.Column(db.Integer)

	ranks_trait = db.Column(db.Integer)
	
	
class PowerMove(db.Model):

	concealment_trait = db.Column(db.Integer)

	subtle_trait = db.Column(db.Integer)

	objects_skill = db.Column(db.Integer)

	check_trait = db.Column(db.Integer)


class PowerOpposed(db.Model):
	
	trait = db.Column(db.Integer)
	
	opponent_trait = db.Column(db.Integer)
	
	
class PowerRanged(db.Model):
	
	check_trait = db.Column(db.Integer)
	
	trait_trait = db.Column(db.Integer)
	
	distance_mod_trait = db.Column(db.Integer)
	
	dc_trait = db.Column(db.Integer)


class PowerResist(db.Model):
	
	trait = db.Column(db.Integer)

	check_trait = db.Column(db.Integer)


class PowerResistBy(db.Model):

	trait = db.Column(db.Integer)


class PowerSenseEffect(db.Model):

	height_trait = db.Column(db.Integer)

	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))

	resist_trait = db.Column(db.Integer)

	time_bonus = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))


class PowerReverse(db.Model):
	
	trait = db.Column(db.Integer)
	
	

class PowerTime(db.Model):

	trait = db.Column(db.Integer)

