














class PowerSenseEffect(db.Model):
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))

	skill = db.Column(db.Integer, db.ForeignKey('skills.id'))

	time_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_skill = db.Column(db.Integer, db.ForeignKey('skills.id'))
	
	
	distance_unit = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	
	
	
	