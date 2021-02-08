

class Power(db.Model):
	
	routine_trait = db.Column(db.String())
	
	partner_trait = db.Column(db.String())
	
	
	
class PowerAltCheck(db.Model):

	trait = db.Column(db.String())




class PowerChar(db.Model):

	trait = db.Column(db.String())

	weaken_trait = db.Column(db.String())

		weaken_broad = db.Column(db.String())

	reduced_trait = db.Column(db.String())
	
	points_trait = db.Column(db.String())
	
	
class PowerCirc(db.Model):
	
	check_trait = db.Column(db.String())

	null_trait = db.Column(db.String())


class PowerCreate(db.Model):
	
	move_player_trait = db.Column(db.String())
	
	trap_trait = db.Column(db.String())

	trap_resist_trait = db.Column(db.String())

	ranged_trait = db.Column(db.String())
	
	weapon_trait = db.Column(db.String())
	
	

class PowerDamage(db.Model):

	trait = db.Column(db.String())



class PowerDC(db.Model):

	math_trait = db.Column(db.String())

	check_trait = db.Column(db.String())


class PowerDefense(db.Model):

	
	defense = db.Column(db.Integer, db.ForeignKey('defenses.id'))
	
	reflect_opposed_trait = db.Column(db.String())
	
	reflect_resist_trait = db.Column(db.String())
	
	immunity_trait = db.Column(db.String())
	
	cover_type = db.Column(db.Integer, db.ForeignKey('cover.id'))


class PowerDegMod(db.Model):

	circ_trait = db.Column(db.String())

	measure_trait = db.Column(db.String())

	consequence_trait = db.Column(db.String())

class PowerEnv(db.Model):

	visibility_trait = db.Column(db.String())


class PowerMinion(db.Model):

	attitude_trait = db.Column(db.String())


class PowerMod(db.Model):
	
	limited_trait = db.Column(db.String())

	reflect_trait = db.Column(db.String())

	subtle_opponent_trait = db.Column(db.String())
	
	subtle_null_trait = db.Column(db.String())

	ranks_trait = db.Column(db.String())
	
	
class PowerMove(db.Model):

	concealment_trait = db.Column(db.String())

	subtle_trait = db.Column(db.String())

	objects_skill = db.Column(db.String())

	check_trait = db.Column(db.String())


class PowerOpposed(db.Model):
	
	trait = db.Column(db.String())
	
	opponent_trait = db.Column(db.String())
	
	
class PowerRanged(db.Model):
	
	check_trait = db.Column(db.String())
	
	trait_trait = db.Column(db.String())
	
	distance_mod_trait = db.Column(db.String())
	
	dc_trait = db.Column(db.String())


class PowerResist(db.Model):
	
	trait = db.Column(db.String())

	check_trait = db.Column(db.String())


class PowerResistBy(db.Model):

	trait = db.Column(db.String())


class PowerSenseEffect(db.Model):

	height_trait = db.Column(db.String())

	height_ensense = db.Column(db.Integer, db.ForeignKey('powers.id'))

	resist_trait = db.Column(db.String())

	time_bonus = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))


class PowerReverse(db.Model):
	
	trait = db.Column(db.String())
	
	

class PowerTime(db.Model):

	trait = db.Column(db.String())

