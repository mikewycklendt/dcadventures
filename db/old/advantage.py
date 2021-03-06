
class AdvAltCheck(db.Model):
	__tablename__ = 'advantage_alt_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	check_trigger = db.Column(db.String())
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	mod = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	trigger = db.Column(db.String())
	when = db.Column(db.String())
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	conflict_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	conflict_weapon = db.Column(db.Boolean)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	action_type = db.Column(db.String())
	action = db.Column(db.Integer)
	free = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'check_trigger': self.check_trigger,
			'check_type': self.check_type,
			'mod': self.mod,
			'circumstance': self.circumstance,
			'trigger': self.trigger,
			'when': self.when,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'conflict': self.conflict,
			'conflict_range': self.conflict_range,
			'conflict_weapon': self.conflict_weapon,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'action_type': self.action_type,
			'action': self.action,
			'free': self.free
		}

class AdvCirc(db.Model):
	__tablename__ = 'advantage_circumstance'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	target = db.Column(db.String())
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	mod = db.Column(db.Integer)
	rounds = db.Column(db.Integer)
	circumstance = db.Column(db.String())
	circ_type = db.Column(db.String())
	circ_range = db.Column(db.Integer, db.ForeignKey('ranged.id'))
	conflict = db.Column(db.Integer, db.ForeignKey('conflict_actions.id'))
	check_who = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	null_type = db.Column(db.String())
	null_condition = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	null_trait_type = db.Column(db.String())
	null_trait = db.Column(db.Integer)	
	null_override_trait_type = db.Column(db.String())
	null_override_trait = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'advantage_id': self.advantage_id,
			'target': self.target,
			'benefit': self.benefit,
			'mod': self.mod,
			'rounds': self.rounds,
			'circumstance': self.circumstance,
			'circ_type': self.circ_type,
			'circ_range': self.circ_range,
			'conflict': self.conflict,
			'check_who': self.check_who,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'null_type': self.null_type,
			'null_condition': self.null_condition,
			'null_trait_type': self.null_trait_type,
			'null_trait': self.null_trait,
			'null_override_trait_type': self.null_override_trait_type,
			'null_override_trait': self.null_override_trait
		}


class AdvDC(db.Model):
	__tablename__ = 'advantage_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	target = db.Column(db.String())
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	dc = db.Column(db.String())
	description = db.Column(db.String())
	value_value = db.Column(db.Integer)
	math_value = db.Column(db.Integer)
	math_math = db.Column(db.Integer, db.ForeignKey('math.id'))
	math_trait_type = db.Column(db.String())
	math_trait = db.Column(db.Integer)
	condition = db.Column(db.Boolean)
	keyword_check = db.Column(db.Boolean)
	check_type = db.Column(db.Boolean)
	levels = db.Column(db.Boolean)
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	keyword = db.Column(db.String())
	check_trait_type = db.Column(db.String())
	check_trait = db.Column(db.Integer)
	check_mod = db.Column(db.Integer)

	def format(self):
		return {
			'id': self.id,
			'target': self.target,
			'benefit': self.benefit,
			'dc': self.dc,
			'description': self.description,
			'value_value': self.value_value,
			'math_value': self.math_value,
			'math_math': self.math_math,
			'math_trait_type': self.math_trait_type,
			'math_trait': self.math_trait,
			'condition': self.condition,
			'keyword_check': self.keyword_check,
			'check_type': self.check_type,
			'levels': self.levels,
			'level_type': self.level_type,
			'level': self.level,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_mod': self.check_mod
		}

class AdvDegree(db.Model):
	__tablename__ = 'advantage_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	target = db.Column(db.String())
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	value = db.Column(db.Integer)
	deg_mod_type = db.Column(db.String())
	consequence_action_type = db.Column(db.String())
	consequence_action = db.Column(db.Integer)
	consequence_trait_type = db.Column(db.String())
	consequence_trait = db.Column(db.Integer)
	consequence = db.Column(db.Integer, db.ForeignKey('consequences.id'))
	knowledge = db.Column(db.String())
	knowledge_count = db.Column(db.Integer)
	knowledge_specificity = db.Column(db.String())
	level_type = db.Column(db.Integer, db.ForeignKey('level_type.id'))
	level = db.Column(db.Integer, db.ForeignKey('levels.id'))
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
	condition_type = db.Column(db.String())
	condition_damage_value = db.Column(db.Integer)
	condition_damage = db.Column(db.Integer)
	condition1 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	condition2 = db.Column(db.Integer, db.ForeignKey('conditions.id'))
	keyword = db.Column(db.String())
	nullify = db.Column(db.Integer)
	cumulative = db.Column(db.Boolean)
	linked = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'target': self.target,
			'benefit': self.benefit,
			'value': self.value,
			'deg_mod_type': self.deg_mod_type,
			'consequence_action_type': self.consequence_action_type,
			'consequence_action': self.consequence_action,
			'consequence_trait_type': self.consequence_trait_type,
			'consequence_trait': self.consequence_trait,
			'consequence': self.consequence,
			'knowledge': self.knowledge,
			'knowledge_count': self.knowledge_count,
			'knowledge_specificity': self.knowledge_specificity,
			'level_type': self.level_type,
			'level': self.level,
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
			'condition_type': self.condition_type,
			'condition_damage_value': self.condition_damage_value,
			'condition_damage': self.condition_damage,
			'condition1': self.condition1,
			'condition2': self.condition2,
			'keyword': self.keyword,
			'nullify': self.nullify,
			'cumulative': self.cumulative,
			'linked': self.linked
		}


class AdvOpposed(db.Model):
	__tablename__ = 'advantage_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	mod = db.Column(db.Integer)
	opponent_trait_type = db.Column(db.String())
	opponent_trait = db.Column(db.Integer)
	opponent_mod = db.Column(db.Integer)
	player_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	opponent_check = db.Column(db.Integer, db.ForeignKey('checks.id'))
	multiple = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'mod': self.mod,
			'opponent_trait_type': self.opponent_trait_type,
			'opponent_trait': self.opponent_trait,
			'opponent_mod': self.opponent_mod,
			'player_check': self.player_check,
			'opponent_check': self.opponent_check,
			'multiple': self.multiple
		}

class AdvTime(db.Model):
	__tablename__ = 'advantage_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	advantage_id = db.Column(db.Integer, db.ForeignKey('advantages.id'))
	benefit = db.Column(db.Integer, db.ForeignKey('benefits.id'))
	time_type = db.Column(db.String())
	value_type = db.Column(db.String())
	value = db.Column(db.Integer)
	units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	time_value = db.Column(db.Integer)
	math = db.Column(db.Integer, db.ForeignKey('math.id'))
	trait_type = db.Column(db.String())
	trait = db.Column(db.Integer)
	dc = db.Column(db.Integer)
	check_type = db.Column(db.Integer, db.ForeignKey('checks.id'))
	recovery = db.Column(db.Boolean)
	recovery_penalty = db.Column(db.Integer)
	recovery_time = db.Column(db.Integer)
	recovery_incurable = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'benefit': self.benefit,
			'time_type': self.time_type,
			'value_type': self.value_type,
			'value': self.value,
			'units': self.units,
			'time_value': self.time_value,
			'math': self.math,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'dc': self.dc,
			'check_type': self.check_type,
			'recovery': self.recovery,
			'recovery_penalty': self.recovery_penalty,
			'recovery_time': self.recovery_time,
			'recovery_incurable': self.recovery_incurable
		}
