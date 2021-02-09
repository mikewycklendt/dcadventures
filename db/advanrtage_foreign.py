

	
class AdvEffort(db.Model):
	
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvMod(db.Model):
	
	environment = db.Column(db.Integer, db.ForeignKey('environments.id'))
	
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	mod_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	subsense = db.Column(db.Integer, db.ForeignKey('sub_senses.id'))
	cover = db.Column(db.Integer, db.ForeignKey('cover.id'))
	conceal = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	maneuver = db.Column(db.Integer, db.ForeignKey('maneuvers.id'))
	weapon_melee = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	weapon_ranged = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	creature = db.Column(db.Integer, db.ForeignKey('creature.id'))
	
	emotion = db.Column(db.Integer, db.ForeignKey('emotions.id'))
	
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	profession = db.Column(db.Integer, db.ForeignKey('jobs.id'))
	
	
	
	
	
	bonus_conflict = db.Column(db.Integer, db.ForeignKey('conflict_sctions.id'))
	
	penalty_conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	
	


class AdvPoints(db.Model):
	
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
	
	
	