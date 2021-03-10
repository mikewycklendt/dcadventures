
class PowerCirc(db.Model):
	__tablename__ = 'power_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	description = db.Column(db.String())
	circ_type = db.Column(db.String())
	circ_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	check_who = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	null_type = db.Column(db.String())
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	null_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	null_trait_type = db.Column(db.String())
	null_trait = db.Column(db.Integer)


	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'mod': self.mod,
			'rounds': self.rounds,
			'description': self.description,
			'circ_type': self.circ_type,
			'circ_range': self.circ_range,
			'check_who': self.check_who,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'null_type': self.null_type,
			'null_condition': self.null_condition,
			'null_descriptor': self.null_descriptor,
			'null_trait_type': self.null_trait_type,
			'null_trait': self.null_trait
		}


class PowerDC(db.Model):
	__tablename__ = 'power_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	dc = db.Column(db.String())
	description = db.Column(db.String())
	value = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_trait_type = db.Column(db.String())
	math_trait = db.Column(db.Integer)
	descriptor_check = db.Column(db.Boolean)
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	descriptor_possess = db.Column(db.String())
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	keyword = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	check_mod = db.Column(db.Integer)
	levels = db.Column(db.Boolean)
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'dc': self.dc,
			'description': self.description,
			'value': self.value,
			'math_value': self.math_vqlue,
			'math': self.math,
			'math_trait_type': self.math_trait_type,
			'math_trait': self.math_trait,
			'descriptor_check': self.descriptor_check,
			'condition': self.condition,
			'keyword_check': self.keyword_check,
			'check_type': self.check_type,
			'descriptor': self.descriptor,
			'descriptor_possess': self.descriptor_possess,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_mod': self.check_mod,
			'levels': self.levels,
			'level': self.level
		}

class PowerDegMod(db.Model):
	__tablename__ = 'power_degree_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	target = db.Column(db.String())
	value = db.Column(db.Integer)
	deg_type = db.Column(db.String())
	circ_value = db.Column(db.Integer)
	circ_turns = db.Column(db.Integer)
	circ_trait_type = db.Column(db.String())
	circ_trait = db.Column(db.Integer)
	measure_type = db.Column(db.String())
	measure_val1 = db.Column(db.Integer)
	measure_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	measure_trait_type = db.Column(db.String())
	measure_trait = db.Column(db.Integer)
	measure_value = db.Column(db.Integer)
	measure_rank = db.Column(db.Integer, db.ForeignKey('ranks.id'))
	deg_condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	consequence_action_type = db.Column(db.String())
	consequence_action = db.Column(db.Integer)
	consequence_trait_type = db.Column(db.String())
	consequence_trait = db.Column(db.Integer)
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	knowledge =db.Column(db.String())
	knowledge_count = db.Column(db.Integer)
	knowledge_specificity = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'value': self.value,
			'deg_type': self.deg_type,
			'circ_value': self.circ_value,
			'circ_turns': self.circ_turns,
			'circ_trait_type': self.circ_trait_type,
			'circ_trait': self.circ_trait,
			'measure_type': self.measure_type,
			'measure_val1': self.measure_val1,
			'measure_math': self.measure_math,
			'measure_trait_type': self.measure_trait_type,
			'measure_trait': self.measure_trait,
			'measure_value': self.measure_value,
			'measure_rank': self.measure_rank,
			'deg_condition_type': self.deg_condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'cumulative': self.cumulative,
			'linked': self.linked,
			'level': self.level,
			'consequence_action_type': self.consequence_action_type,
			'consequence_action': self.consequence_action,
			'consequence_trait_type': self.consequence_trait_type,
			'consequence_trait': self.consequence_trait,
			'consequence': self.consequence,
			'knowledge': self.knowledge,
			'knowledge_count': self.knowledge_count,
			'knowledge_specificity': self.knowledge_specificity
		}

class PowerMove(db.Model):
	__tablename__ = 'power_movement'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	rank = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	mod = db.Column(db.Integer)
	per_rank = db.Column(db.Boolean)
	flight = db.Column(db.Boolean)
	aquatic = db.Column(db.Boolean)
	ground = db.Column(db.Boolean)
	condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	direction = db.Column(db.String())
	distance_type = db.Column(db.String())
	distance_value = db.Column(db.Integer)
	distance_math_value = db.Column(db.Integer)
	distance_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	distance_math_value2 = db.Column(db.Integer)
	distance_mod = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	others = db.Column(db.Boolean)
	continuous = db.Column(db.Boolean)
	subtle = db.Column(db.Boolean)
	concentration = db.Column(db.Boolean)
	obstacles = db.Column(db.Boolean)
	objects = db.Column(db.Boolean)
	permeate = db.Column(db.Boolean)
	special = db.Column(db.Boolean)
	prone = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	materials = db.Column(db.Boolean)
	concealment = db.Column(db.Boolean)
	extended = db.Column(db.Boolean)
	mass = db.Column(db.Boolean)
	mass_value = db.Column(db.Integer)
	extended_actions = db.Column(db.Integer)
	acquatic_type = db.Column(db.String())
	concealment_sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	concealment_trait_type = db.Column(db.String())
	concealment_trait = db.Column(db.Integer)
	permeate_type = db.Column(db.String())
	permeate_speed = db.Column(db.Integer)
	permeate_cover = db.Column(db.Boolean)
	special_type = db.Column(db.String())
	teleport_type = db.Column(db.String())
	teleport_change = db.Column(db.String())
	teleport_portal = db.Column(db.Boolean)
	teleport_obstacles = db.Column(db.Boolean)
	dimension_type = db.Column(db.String())
	dimension_mass_rank = db.Column(db.Integer)
	dimension_descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	special_space = db.Column(db.String())
	special_time = db.Column(db.String())
	special_time_carry = db.Column(db.Integer)
	ground_type = db.Column(db.Integer, db.ForeignKey('ground.id'))
	ground_permanence = db.Column(db.String())
	ground_time = db.Column(db.Integer)
	ground_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	ground_ranged = db.Column(db.Boolean)
	subtle_trait_type = db.Column(db.String())
	subtle_trait = db.Column(db.Integer)
	subtle_mod = db.Column(db.Integer)
	flight_resist = db.Column(db.Boolean)
	flight_equip = db.Column(db.Boolean)
	flight_conditions = db.Column(db.ARRAY(db.String))
	objects_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	objects_attack = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	objects_skill_type = db.Column(db.String())
	objects_skill = db.Column(db.Integer)
	objects_direction = db.Column(db.String())
	objects_damage = db.Column(db.Boolean)
	damage_type = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	check_free = db.Column(db.Boolean)
	ranks = db.Column(db.Integer)
	cost = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'rank': self.rank,
			'math': self.math,
			'mod': self.mod,
			'per_rank': self.per_rank,
			'flight': self.flight,
			'aquatic': self.aquatic,
			'ground': self.ground,
			'condition': self.condition,
			'direction': self.direction,
			'distance_type': self.distance_type,
			'distance_value': self.distance_value,
			'distance_math_value': self.distance_math_value,
			'distance_math': self.distance_math,
			'distance_math_value2': self.distance_math_value2,
			'distance_mod': self.distance_mod,
			'dc': self.dc,
			'others': self.others,
			'continuous': self.continuous,
			'subtle': self.subtle,
			'concentration': self.concentration,
			'obstacles': self.obstacles,
			'objects': self.objects,
			'permeate': self.permeate,
			'special': self.special,
			'prone': self.prone,
			'check_type': self.check_type,
			'obstacles_check': self.obstacles_check,
			'concealment': self.concealment,
			'extended': self.extended,
			'mass': self.mass,
			'mass_value': self.mass_value,
			'extended_actions': self.extended_actions,
			'acquatic_type': self.acquatic_type,
			'concealment_sense': self.concealment_sense,
			'concealment_trait_type': self.concealment_trait_type,
			'concealment_trait': self.concealment_trait,
			'permeate_type': self.permeate_type,
			'permeate_speed': self.permeate_speed,
			'permeate_cover': self.permeate_cover,
			'special_type': self.special_type,
			'teleport_type': self.teleport_type,
			'teleport_change': self.teleport_change,
			'teleport_portal': self.teleport_portal,
			'teleport_obstacles': self.teleport_obstacles,
			'dimension_type': self.dimension_type,
			'dimension_mass_rank': self.dimension_mass_rank,
			'dimension_descriptor': self.dimension_descriptor,
			'special_space': self.special_space,
			'special_time': self.special_time,
			'special_time_carry': self.special_time_carry,
			'ground_type': self.ground_type,
			'ground_permanence': self.ground_permanence,
			'ground_time': self.ground_time,
			'ground_units': self.ground_units,
			'ground_ranged': self.ground_ranged,
			'subtle_trait_type': self.subtle_trait_type,
			'subtle_trait': self.subtle_trait,
			'subtle_mod': self.subtle_mod,
			'flight_resist': self.flight_resist,
			'flight_equip': self.flight_equip,
			'flight_conditions': self.flight_conditions,
			'objects_check': self.objects_check,
			'objects_attack': self.objects_attack,
			'objects_skill_type': self.objects_skill_type,
			'objects_skill': self.objects_skill,
			'objects_direction': self.objects_direction,
			'objects_damage': self.objects_damage,
			'damage_type': self.damage_type,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_free': self.check_free,
			'ranks': self.ranks,
			'cost': self.cost
		}

class PowerOpposed(db.Model):
	__tablename__ = 'power_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.Integer)
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'opponent_trait_type': self.opponent_trait_type,
			'opponent_trait': self.opponent_trait,
			'opponent_mod': self.opponent_mod,
			'player_check': self.player_check,
			'opponent_check': self.opponent_check
		}

class PowerTime(db.Model):
	__tablename__ = 'power_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
	extra_id = db.Column(db.Integer, db.ForeignKey('extras.id'))
	time_type = db.Column(db.String())
	value_type = db.Column(db.String())
	value = db.Column(db.Integer)
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	descriptor = db.Column(db.Integer, db.ForeignKey('power_descriptors.id'))
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recovery = db.Column(db.Boolean)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'time_type': self.time_type,
			'value_type': self.value_type,
			'value': self.value,
			'units': self.units,
			'time_value': self.time_value,
			'math': self.math,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'dc': self.dc,
			'descriptor': self.descriptor,
			'check_type': self.check_type,
			'recovery': self.recovery,
			'recovery_penalty': self.recovery_penalty,
			'recovery_time': self.recovery_time,
			'recovery_incurable': self.recovery_incurable
		}