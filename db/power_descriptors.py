``

class PowerChar(db.Model):

	weaken_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	points_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))


class PowerCirc(db.Model):

	null_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))


class PowerCreate(db.Model):
	
	transform_start_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	transform_end_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	
class PowerDamage(db.Model):

	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))


class PowerDC(db.Model):

	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))


class PowerDefense(db.Model):

	immunity_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))






class PowerMod(db.Model):

	simultaneous_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	area_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	limited_source = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	limited_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))

	reflect_descriptor = 


class PowerMove(db.Model):

	dimension_descriptor = 



class PowerResist(db.Model):
	
	descriptor = 
	
	

class PowerResistBy(db.Model):
	
	descriptor = 
	
	nullify_descriptor = 
	
	
	


class PowerTime(db.Model):

	descriptor = get_name(PowerDes, )
	
	