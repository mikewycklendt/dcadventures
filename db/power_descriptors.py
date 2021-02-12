

class PowerChar(db.Model):

	weaken_descriptor = db.Column(db.Integer)

	points_descriptor = db.Column(db.Integer)



class PowerCirc(db.Model):

	null_descriptor = db.Column(db.Integer)


class PowerCreate(db.Model):
	
	transform_start_descriptor = db.Column(db.Integer)
	transform_end_descriptor = db.Column(db.Integer)
	
	
class PowerDamage(db.Model):

	descriptor = db.Column(db.Integer)


class PowerDC(db.Model):

	descriptor = db.Column(db.Integer)


class PowerDefense(db.Model):

	immunity_descriptor = db.Column(db.Integer)






class PowerMod(db.Model):

	simultaneous_descriptor = db.Column(db.Integer)

	area_descriptor = db.Column(db.Integer)

	limited_source = db.Column(db.Integer)

	limited_descriptor = db.Column(db.Integer)

	reflect_descriptor = db.Column(db.Integer)


class PowerMove(db.Model):

	dimension_descriptor = db.Column(db.Integer)



class PowerResist(db.Model):
	
	descriptor = db.Column(db.Integer)
	
	

class PowerResistBy(db.Model):
	
	descriptor = db.Column(db.Integer)
	
	nullify_descriptor = db.Column(db.Integer)
	
	
	
	


class PowerTime(db.Model):

	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	
	
class PowerDes(db.Model):
	__tablename__ = 'power_descriptors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())	
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	des_id = db.Column(db.Integer, db.ForeignKey('descriptors.id'))
	origin = db.Column(db.Integer, db.ForeignKey('origin.id'))
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	medium = db.Column(db.Integer, db.ForeignKey('medium.id'))
	medium_type = db.Column(db.Integer, db.ForeignKey('medium_type.id'))
	medium_subtype = db.Column(db.Integer, db.ForeignKey('medium_subtype.id'))
	result = db.Column(db.String())
	descriptor = db.Column(db.Boolean)
	damage = db.Column(db.Boolean)
	hidden = db.Column(db.Boolean)
	rare = db.Column(db.Boolean)
	uncommon = db.Column(db.Boolean)
	common = db.Column(db.Boolean)
	very = db.Column(db.Boolean)
	any_damage = db.Column(db.Boolean)
	any_origin = db.Column(db.Boolean)
	any_source = db.Column(db.Boolean)
	any_medium_type = db.Column(db.Boolean)
	any_medium_subtype = db.Column(db.Boolean)
	any_medium = db.Column(db.Boolean)
	any_descriptor = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'power_id': self.power_id,
			'des_id': self.des_id,
			'origin': self.origin,
			'source': self.source,
			'medium': self.medium,
			'medium_type': self.medium_type,
			'medium_subtype': self.medium_subtype,
			'result': self.result,
			'descriptor': self.descriptor,
			'damage': self.damage,
			'hidden': self.hidden,
			'rare': self.rare,
			'uncommon': self.uncommon,
			'common': self.common,
			'very': self.very,
			'any_damage': self.any_damage,
			'any_origin': self.any_origin,
			'any_source': self.any_source,
			'any_medium_type': self.any_medium_type,
			'any_medium_subtype': self.any_medium_subtype,
			'any_medium': self.any_medium,
			'any_descriptor': self.any_descriptor
		}