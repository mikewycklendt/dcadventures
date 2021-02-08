

	
class AdvEffort(db.Model):
	
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
class AdvMod(db.Model):
	__tablename__ = 'advantage_modifiers'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	bonus = db.Column(db.Integer)
	bonus_type = db.Column(db.String())
	penalty = db.Column(db.Integer)
	penalty_type = db.Column(db.String())
	trigger = db.Column(db.String())
	bonus_effect = db.Column(db.String())
	penalty_effect = db.Column(db.String())
	environment = db.Column(db.Integer)
	environment_other = db.Column(db.String())
	sense = db.Column(db.Integer)
	mod_range = db.Column(db.Integer)
	subsense = db.Column(db.Integer)
	cover = db.Column(db.Integer)
	conceal = db.Column(db.Integer)
	maneuver = db.Column(db.Integer)
	weapon_melee = db.Column(db.Integer)
	weapon_ranged = db.Column(db.Integer)
	tools = db.Column(db.String())
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	power = db.Column(db.Integer, db.ForeignKey('powers.id'))
	consequence = db.Column(db.Integer)
	creature = db.Column(db.Integer)
	creature_other = db.Column(db.String())
	emotion = db.Column(db.Integer)
	emotion_other = db.Column(db.String())
	conflict = db.Column(db.Integer)
	profession = db.Column(db.Integer)
	profession_other = db.Column(db.String())
	bonus_trait_type = db.Column(db.String())
	bonus_trait = db.Column(db.Integer)
	bonus_check = db.Column(db.Integer)
	bonus_check_range = db.Column(db.Integer)
	bonus_conflict = db.Column(db.Integer)
	penalty_trait_type = db.Column(db.String())
	penalty_trait = db.Column(db.Integer)
	penalty_check = db.Column(db.Integer)
	penalty_check_range = db.Column(db.Integer)
	penalty_conflict = db.Column(db.Integer)
	bonus_active_defense = db.Column(db.Boolean)
	bonus_conflict_defend = db.Column(db.Boolean)
	penalty_active_defense = db.Column(db.Boolean)
	penalty_conflict_defend = db.Column(db.Boolean)
	multiple = db.Column(db.String())
	multiple_count = db.Column(db.Integer)
	lasts = db.Column(db.Integer)



class AdvPoints(db.Model):
	
	benefit_choice = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	
	
	
	
	