from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSense, PowerTime 


def name(Table, name):

	if name == 0:
		name = 'All'
	else:
		try:
			query = db.session,query(Table).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)

def math(Table, name):

	try:
		query = db.session,query(Table).filter_by(id=name).one()
		name = query.symbol
	except:
		print('invalid id')
	
	return (name)

def extra_name(name):
	if name is None:
		name = 'Base Power'
	else:
		try:
			query = db.session,query(Extra).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)

def descriptor_name(name):

	if name == 11223344: 
		name = 'Any Chosen Rare'
	elif name == 22334455:
		name = 'Any Chosen Uncommon' 
	elif name == 33445566:
		name = 'Any Chosen Common'
	elif name == 44556677:
		name = 'Any Chosen Very Common' 
	elif name == 55667788:
		name = 'Any Chosen Damage'
	elif name == 66778899:
		name = 'Any Chosen Origin'
	elif name == 77889900:
		name = 'Any Chosen Source'
	elif name == 88990011:
		name = 'Any Chosen Medium Type'
	elif name == 99001122:
		name = 'Any Chosen Medium Subtype'
	elif name == 11002233:
		name = 'Any Chosen Medium'
	elif name == 12121212:
		name = 'Any Chosen Descriptor'
	else:
		try:
			query = db.session,query(PowerDes).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)

def integer_convert(value):

	if value == 123:
		value = "Permanent"
		print(value)
	elif value == 121:
		value = "Power Rank"
		print(value)
	elif value == 567:
		value = "Any"
		print(value)
	elif value == 222:
		value = "Always"
		print(value)
	elif value == 333:
		value = "One Round"
		print(value)
	elif value == 111:
		value = "Extra Rank"
		print(value)
	elif value == 444:
		value = "Nullified"
		print(value)
	elif value == 555:
		value = "Normal"
		print(value)
	elif value == 666:
		value = "Instant"
		print(value)
	elif value == 777:
		value = "Distance rank"
		print(value)
	elif value == 888:
		value = "Vertical Height"
		print(value)
	elif value == 999:
		value = "No Check"
		print(value)
	elif value == 432:
		value = "Result"
		print(value)
	elif value == 778:
		value = "All"
		print(value)
	elif value == 112:
		value = "Trait"
		print(value)
	elif value == 334:
		value = "Impervious"
		print(value)
	elif value == 556:
		value = "Check"
		print(value)
	elif value == 990:
		value = "Turn"
		print(value)
	elif value is None:
		value = ''
	else:
		value = str(value)

	return (value)

def selects(value, options):

	if value != '':
		for option in options:
			if value == option['type']:
				value = option['name']

	return (value)

def select_multiple(values):
	result = ''

	for value in values:
		result += value + ' '

	return (result)

def entry(cells, body):

	rows = body['rows']
	entry_id = body['id']

	widths = []
	for cell in cells:
		widths.append(cell['width'])

	new_row = [{'id': entry_id, 'cells': widths}]

	rows.append(new_row)

	grid = grid_columns(rows)

	body['grid'] = grid
	body['rows'] = rows

	for cell in cells:
		print(cell)
	print('\n')
	for row in rows:
		print(row)
	print('\n')
	for mod in mod:
		print(mod)
	print('\n')
	print(grid)

	return (body)


def delete_row(entry_id, rows):

	for i in range(0, len(rows) - 1, 1):
		if rows[i]['id'] == entry_id:
			del rows[i]

	return (rows)

def grid_columns(rows):

	columns = []

	if rows == []:
		grid = 'hide'
	else:
		gridrows = [row['cells'] for row in rows] 	
		for row in gridrows:
			if columns == []:
				columns.append(row)
			else:
				for i in range(1, len(row) - 1, 1):
					if row[i] > columns[i]:
						columns[i] = row[i]
		grid = ''
		empty = 5
		for column in columns:
			grid += str(column) + '% '
			empty += column

		if empty < 100:
			empty = 100 - empty
		else:
			empty = .2
		
		grid += str(empty) + '%' + ' 5%;'

	return (grid)


def variable_cell_add(title, value, data, classname, cells=['e']):


	content = ''
	width = .2

	for choice in data:
		if choice['value'] == value:
			contentlist = choice['content']
			width = choice['width']


	content = contentlist[0]

	if len(contentlist) > 1:	
		for i in range(1, len(contentlist) -1, 1):
			content += ' ' + contentlist[i]

	cell = {'title': title,
			'width': width,
			'content': content,
			'class': classname 
			}

	if cells == ['e']:
		new_cells = []
		cells = new_cells

	cells.append(cell)

def variable_cell(value, width, contentlist, data=['e']):
	content = contentlist[0]

	if len(contentlist) > 1:	
		for i in range(1, len(contentlist) -1, 1):
			if contentlist[i] != '':
				content += ' ' + contentlist[i]

	if content == '':
		width = .2

	cell = {'value': value,
			'width': width,
			'content': content}

	if data == ['e']:
		new_data = []
		data = new_data

	data.append(cell)

	return (data)

def check_cell(title, width, check, classname, cells, mod_check=False):

	if check == False:
		width = .2
		mod_check = False

	cell = {'title': title,
			'width': width,
			'content': check,
			'class': classname,
			'mod_check': mod_check
			}

	return (cells)

def cell(title, width, contentlist, classname, cells=['e']):

	content = contentlist[0]

	if len(contentlist) > 1:	
		for i in range(1, len(contentlist) -1, 1):
			if content == '':
				break
			else:
				content += ' ' + contentlist[i]

	if content == '':
		width = .2

	cell = {'title': title,
			'width': width,
			'content': content,
			'class': classname 
			}

	if cells == ['e']:
		new_cells = []
		cells = new_cells

	cells.append(cell)

	return (cells)

def mod_create(title, width, classname, variable=False):
	
	grid = '10% ' + str(width) + '%'
	
	mod = {'class': classname,
			'title': title,
			'grid': grid,
			'cells': [],
			'variable': variable}

	return (mod)

def mod_cell(title, width, data, mod, value=None, variable_data=['e']):

	if variable_data == ['e']:
		new_v_data = []
		variable_data = new_v_data

	variable = mod['variable']

	if variable:
		if variable_data == []:
			d = {}
			d['value'] = value
			d['cells'] = []
			d['grid'] = ''
		else:
			for var in variable_data:
				if str(var['value']) == str(value):
					d = var
				else:
					d = {}
					d['value'] = value
					d['cells'] = []
					d['grid'] = ''
		result = d
	else:
		result = mod

	cells = result['cells']
	grid = result['grid']
	content_cell = 'auto'
	empty = True 

	if data[0] == True or data[0] == False:
		if data[0] == True:
			content = data[0]
			content_cell = '5%'
		elif data[0] == False:
			return (result)			
	else:
		for var in data:
			if var != '':
				empty = False
				break

		if empty:
			return (result)

	content = data[0]

	if len(data) > 1:
		for i in range(1, len(data) - 1, 1):
			if content == '':
				content = data[i]
			else:
				content += ' ' + data[i]


	grid += ' ' + str(width) + '% ' + content_cell
	cells.append({'title': title,
					'content': content})

	result['grid'] = grid
	result['cells'] = cells

	if variable == False:
		return (result)
	else:
		variable_data.append(result)
		return (variable_data)
		

def variable_mod(value, select, data, mod):

	grid = mod['grid']
	cells = mod['cells']

	for option in select:
		if option['type'] == value:
			sub_title = option['name']
			mod['sub_title'] = sub_title
			width = option['w']
	for d in data:
		if d['value'] == value:
			variable_grid = d['grid']
			variable_cellS = d['cells']

	grid += ' ' + str(width) + '%'
	grid += variable_grid
	cells.append(variable_cellS)

	mod['grid'] = grid
	mod['cells'] = celld

	return (mod)

def mod_add(check, mod, body):

	mods = body['mods']

	if check:
		mods.append(mod)

	body['mods'] = mods
	return (body)

	

def alt_check_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'alt-check'
	spot = "alt-check-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	check_type = entry.check_type
	mod = entry.mod
	circumstance = entry.circumstance
	when = entry.when
	trait_type = entry.trait_type
	trait = entry.trait

	extra = extra_name(extra_id)
	check_type = name(Check, check_type)

	check_types = [{'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'power', 'name': 'Power'}]
	when = selects(when, check_types)

	mod = integer_convert(mod)


def change_action_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'action'
	spot = "action-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	action = entry.action
	mod = entry.mod
	objects = entry.objects
	circumstance = entry.circumstance

	extra = extra_name(extra_id)
	action = name(Action, action)

	mod = integer_convert(mod)

def character_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'char'
	spot = "char-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	value = entry.value
	increase = entry.increase
	limited = entry.limited
	reduced = entry.reduced
	limbs = entry.limbs
	carry = entry.carry
	sustained = entry.sustained
	permanent = entry.permanent
	points = entry.points
	appear = entry.appear
	insubstantial = entry.insubstantial
	weaken = entry.weaken
	weaken_type = entry.weaken_type
	weaken_trait_type = entry.weaken_trait_type
	weaken_trait = entry.weaken_trait
	weaken_broad = entry.weaken_broad
	weaken_descriptor = entry.weaken_descriptor
	weaken_simultaneous = entry.weaken_simultaneous
	limited_by = entry.limited_by
	limited_other = entry.limited_other
	limited_emotion = entry.limited_emotion
	limited_emotion_other = entry.limited_emotion_other
	reduced_trait_type = entry.reduced_trait_type
	reduced_trait = entry.reduced_trait
	reduced_value = entry.reduced_value
	reduced_full = entry.reduced_full
	limbs_continuous = entry.limbs_continuous
	limbs_sustained = entry.limbs_sustained
	limbs_distracting = entry.limbs_distracting
	limbs_projection = entry.limbs_projection
	carry_capacity = entry.carry_capacity
	points_value = entry.points_value
	points_trait_type = entry.points_trait_type
	points_trait = entry.points_trait
	points_descriptor = entry.points_descriptor
	appear_target = entry.appear_target
	appear_description = entry.appear_description
	insub_type = entry.insub_type
	insub_description = entry.insub_description
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)
	weaken_descriptor = descriptor_name(weaken_descriptor)
	points_descriptor = descriptor_name(points_descriptor)

	weaken_select = [{'type': '', 'name': 'Weaken Type'}, {'type': 'trait', 'name': 'Specific'}, {'type': 'type', 'name': 'Broad Trait'}, {'type': 'descriptor', 'name': 'Broad Descriptor'}]
	weaken_type = selects(weaken_type, weaken_select)

	limited_select = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]
	limited_by = selects(limited_by, limited_select)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	appear_target =  selects(appear_target, targets_select)

	insub_select = [{'type': '', 'name': 'Insubstantial Type'}, {'type': 'fluid', 'name': 'Fluid'}, {'type': 'gas', 'name': 'Gaseous'}, {'type': 'energy', 'name': 'Energy'}, {'type': 'incorp', 'name': 'Incorporeal'}]
	insub_type = selects(insub_type, insub_select)

	value = integer_convert(value)
	increase = integer_convert(increase)
	reduced_value = integer_convert(reduced_value)
	carry_capacity = integer_convert(carry_capacity)
	points_value = integer_convert(points_value)
	cost = integer_convert(cost)
	ranks = integer_convert(ranks)	 

def circ_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'circ'
	spot = "circ-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	mod = entry.mod
	rounds = entry.rounds
	description = entry.description
	circ_type = entry.circ_type
	circ_range = entry.circ_range
	check_who = entry.check_who
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	null_type = entry.null_type
	null_condition = entry.null_condition
	null_descriptor = entry.null_descriptor
	null_trait_type = entry.null_trait_type
	null_trait = entry.null_trait

	extra = extra_name(extra_id)
	circ_range = name(Range, circ_range)
	null_descriptor = descriptor_name(null_descriptor)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	circ_type_select = [{'type': '', 'name': 'Triggered By'}, {'type': 'range', 'name': 'Range'}, {'type': 'check', 'name': 'Check Type'}]
	circ_type = selects(circ_type, circ_type_select)

	who_check_select = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]
	check_who = selects(check_who, who_check_select)

	circ_null_select = [{'type': '', 'name': 'Nullified'}, {'type': 'trait', 'name': 'From Trait'}, {'type': 'descriptor', 'name': 'From Descriptor'}, {'type': 'condition', 'name': 'From Condition'}]
	null_type = selects(null_type, circ_null_select)

	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	circ_range = integer_convert(circ_range)




def create_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'create'
	spot = "create-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	solidity = entry.solidity
	visibility = entry.visibility
	complexity = entry.complexity
	volume = entry.volume
	toughness = entry.toughness
	mass = entry.mass
	damageable = entry.damageable
	maintained = entry.maintained
	repairable = entry.repairable
	moveable = entry.moveable
	stationary = entry.stationary
	trap = entry.trap
	ranged = entry.ranged
	weapon = entry.weapon
	support = entry.support
	real = entry.real
	cover = entry.cover
	conceal = entry.conceal
	incoming = entry.incoming
	outgoing = entry.outgoing
	transform = entry.transform
	transform_type = entry.transform_type
	transform_start_mass = entry.transform_start_mass
	transfom_mass = entry.transfom_mass
	transform_start_descriptor = entry.transform_start_descriptor
	transform_end_descriptor = entry.transform_end_descriptor
	move_player = entry.move_player
	move_player_trait = entry.move_player_trait
	move_opponent_check = entry.move_opponent_check
	move_opponent_ability = entry.move_opponent_ability
	move_opponent_rank = entry.move_opponent_rank
	trap_type = entry.trap_type
	trap_dc = entry.trap_dc
	trap_trait_type = entry.trap_trait_type
	trap_trait = entry.trap_trait
	trap_resist_check = entry.trap_resist_check
	trap_resist_trait = entry.trap_resist_check
	trap_resist_dc = entry.trap_resist_dc
	trap_escape = entry.trap_escape
	ranged_type = entry.ranged_type
	ranged_dc = entry.ranged_dc
	ranged_trait_type = entry.ranged_trait_type
	ranged_trait = entry.ranged_trait
	ranged_damage_type = entry.ranged_damage_type
	ranged_damage_value = entry.ranged_damage_value
	weapon_trait_type = entry.weapon_trait_type
	weapon_trait = entry.weapon_trait
	weapon_mod = entry.weapon_mod
	weapon_damage_type = entry.weapon_damage_type
	weapon_damage = entry.weapon_damage
	support_strength = entry.support_strength
	support_strengthen = entry.support_strengthen
	support_action = entry.support_action
	support_action_rounds = entry.support_action_rounds
	support_effort = entry.support_effort
	support_effort_rounds = entry.support_effort_rounds
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)
	complexity = name(Complex, complexity)
	transform_start_descriptor = descriptor_name(transform_start_descriptor)
	transform_end_descriptor = descriptor_name(transform_end_descriptor)
	move_opponent_ability = name(Ability, move_opponent_ability)

	solidity_select = [{'type': '', 'name': 'Solidity'}, {'type': 'solid', 'name': 'Solid'}, {'type': 'incorp', 'name': 'Incorporeal'}, {'type': 'select', 'name': 'Selective'}]
	solidity = selects(solidity, solidity_select)

	visibility_select = [{'type': '', 'name': 'Visibility'}, {'type': 'visible', 'name': 'Visible'}, {'type': 'invisible', 'name': 'Invisible'}, {'type': 'select', 'name': 'Selective'}]
	visibility = selects(visibility, visibility_select)

	transform_select = [{'type': '', 'name': 'Transform Type'}, {'type': 'one', 'name': 'One Substance to One Substance'}, {'type': 'result', 'name': 'Group to Single Result'}, {'type': 'broad', 'name': 'Broad Group to Broad Group'}, {'type': 'any', 'name': 'Any Material into Anything Else'}]
	transform_type = selects(transform_type, transform_select)

	moveable_select = [{'type': '', 'name': 'Moveable With'}, {'type': None, 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]
	move_player = selects(move_player, moveable_select)

	against_select = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]
	trap_type = selects(trap_type, against_select)

	determined_select = [{'type': '', 'name': 'Determined By'}, {'type': 'dc', 'name': 'DC'}, {'type': 'target', 'name': 'Target Trait'}, {'type': 'player', 'name': 'Player Trait'}]
	ranged_type = selects(ranged_type, determined_select)

	object_damage_select = [{'type': '', 'name': 'Damage Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'effect', 'name': 'Effect Rank'}, {'type': 'mass', 'name': 'Object Mass'}, {'type': 'volume', 'name': 'Object Volume'}, {'type': 'tough', 'name': 'Object Toughness'}, {'type': 'ability', 'name': 'Player Ability'}]
	ranged_damage_type = selects(ranged_damage_type, object_damage_select)

	weapon_damage_type = selects(weapon_damage_type, object_damage_select)

	volume = integer_convert(volume)
	toughness = integer_convert(toughness)
	mass = integer_convert(mass)
	transform_start_mass = integer_convert(transform_start_mass)
	transfom_mass = integer_convert(transfom_mass)
	move_opponent_rank = integer_convert(move_opponent_rank)
	trap_dc = integer_convert(trap_dc)
	trap_resist_dc = integer_convert(trap_resist_dc)
	ranged_dc = integer_convert(ranged_dc)
	ranged_damage_value = integer_convert(ranged_damage_value)
	weapon_mod = integer_convert(weapon_mod)
	weapon_damage = integer_convert(weapon_damage)
	support_strength = integer_convert(support_strength)
	support_action = integer_convert(support_action)
	support_action_rounds = integer_convert(support_action_rounds)
	support_effort = integer_convert(support_effort)
	support_effort_rounds = integer_convert(support_effort_rounds)
	cost = integer_convert(cost)
	ranks = integer_convert(ranks)


def damage_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'damage'
	spot = "damage-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	strength = entry.strength
	damage_type = entry.damage_type
	descriptor = entry.descriptor

	extra = extra_name(extra_id)
	damage_type = name(Descriptor, damage_type)
	descriptor = descriptor_name(descriptor)

	mod = integer_convert(mod)
	damage_type = integer_convert(damage_type)




def dc_table_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	body['rows'] = rows
	mods = []
	cells = []
	table_id = 'dc'
	spot = "dc-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	dc = entry.dc
	description = entry.description
	value = entry.value
	math_value = entry.math_value
	math = entry.math
	math_trait_type = entry.math_trait_type
	math_trait = entry.math_trait
	descriptor_check = entry.descriptor_check
	condition = entry.condition
	keyword_check = entry.keyword_check
	check_type = entry.check_type
	descriptor = entry.descriptor
	descriptor_possess = entry.descriptor_possess
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_mod = entry.check_mod
	levels = entry.level

	extra = extra_name(extra_id)
	math = math(Math, math)
	descriptor = descriptor_name(descriptor)
	level = name(PowerLevels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	value_type_select = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]
	dc = selects(dc, value_type_select)

	possess_select = [{'type': '', 'name': 'Possession'}, {'type': 'possess', 'name': 'While Possessing'}, {'type': 'oppose', 'name': 'While Opposing'}]
	descriptor_possess = selects(descriptor_possess, possess_select)

	value = integer_convert(value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

def defense_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'defense'
	spot = "defense-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows

	power_id = entry.power_id
	extra_id = entry.extra_id
	defense = entry.defense
	use = entry.use
	mod = entry.mod
	roll = entry.roll
	outcome = entry.outcome
	dodge = entry.dodge
	fortitude = entry.fortitude
	parry = entry.parry
	toughness = entry.toughness
	will = entry.will
	resist_area = entry.resist_area
	resist_perception = entry.resist_perception
	reflect = entry.reflect
	immunity = entry.immunity
	reflect_action = entry.reflect_action
	reflect_check = entry.reflect_check
	reflect_dc = entry.reflect_dc
	reflect_opposed_trait_type = entry.reflect_opposed_trait_type
	reflect_opposed_trait = entry.reflect_opposed_trait
	reflect_resist_trait_type = entry.reflect_resist_trait_type
	reflect_resist_trait = entry.reflect_resist_trait
	immunity_type = entry.immunity_type
	immunity_trait_type = entry.immunity_trait_type
	immunity_trait = entry.immunity_trait
	immunity_descriptor = entry.immunity_descriptor
	immunity_damage = entry.immunity_damage
	immunity_rule = entry.immunity_rule
	cover_check = entry.cover_check
	cover_type = entry.cover_type

	extra = extra_name(extra_id)
	reflect_action = name(Action, reflect_action)
	immunity_descriptor = descriptor_name(immunity_descriptor)
	immunity_damage = name(Descriptor, immunity_damage)

	game_rule_select = [{'type': '', 'name': 'Game Rule'}, {'type': 'critical', 'name': 'Critical Hits'}, {'type': 'suffocate', 'name': 'Suffocation'}, {'type': 'starve', 'name': 'Starvation'}, {'type': 'thirst', 'name': 'Thirst'}, {'type': 'sleep', 'name': 'Need for Sleep'}, {'type': 'fall', 'name': 'Falling'}]
	immunity_rule = selects(immunity_rule, game_rule_select)

	mod = integer_convert(mod)
	roll = integer_convert(roll)
	reflect_dc = integer_convert(reflect_dc)

	use_type_select = [{'type': '', 'name': 'Use Type'}, {'type': 'add', 'name': 'Add to'}, {'type': 'replace', 'name': 'In Place of'}, {'type': 'gm', 'name': 'GM Choice'}]
	use = selects(use, use_type_select)

	cover_select = [{'type': '', 'name': 'Cover Type'}, {'type': 'partial', 'name': 'Partial Cover'}, {'type': 'total', 'name': 'Total Cover'}]
	cover_type = selects(cover_type, cover_select)


	cells = cell('Defense', 15, [defense], 'defense')
	cells = cell('Use', 10, [use], 'use', cells)
	cells = cell('Mod', 5, [mod], 'mod', cells)
	cells = cell('Roll', 15, [roll, 'or', outcome], 'roll', cells)
	cells = check_cell('Dodge', 5, dodge, 'dodge', cells)
	cells = check_cell('Fortitude', 7, fortitude, 'fort', cells)
	cells = check_cell('Parry', 5, parry, 'parry', cells)
	cells = check_cell('Toughness', 7, toughness, 'tough', cells)
	cells = check_cell('Will', 5, will, 'will', cells)
	cells = check_cell('Resists Area', 10, resist_area, 'area', cells)
	cells = check_cell('Resists Perception', 15, resist_perception, 'perc', cells)
	
	classname = 'reflect'
	cells = check_cell('Reflect', 10, reflect, classname, cells, True)
	new_mod = mod_create('Reflects Attacks', 17, classname, True)
	print(new_mod)
	print('\n\n\n')
	value = 1
	data = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	data = mod_cell('DC:', 7, [reflect_dc], new_mod, value, data)
	print(data)
	print('\n\n\n')
	value = 2
	data = mod_cell('Action Type:', 15, [reflect_action], new_mod, value, data)
	data = mod_cell('Opposed By:', 15, [reflect_opposed_trait], new_mod, value, data)
	value = 6
	data = mod_cell('Action Type', 15, [reflect_action], new_mod, value, data)
	data = mod_cell('Resisted By', 15, [reflect_action], new_mod, value, data)
	select = [{'type': 1, 'name': 'Skill Check', 'w': 10}, {'type': 2, 'name': 'Opposed Check', 'w': 15}, {'type': 6, 'name': 'Resistance Check', 'w': 15}]
	new_mod = variable_mod(reflect_check, select, data, new_mod)
	body = mod_add(reflect, new_mod, body)
	
	classname = 'immunity'
	cells = check_cell('Immunity', 10, immunity, classname, cells, True)
	new_mod = mod_create('Immunity', 17, classname, True)
	value = 'trait'
	data = mod_cell('Trait:', 15, [immunity_trait], new_mod, value)
	value = 'damage'
	data = mod_cell('Damage:', 10, [immunity_damage], new_mod, value, data)
	value = 'descriptor'
	data = mod_cell('Descriptor:', 15, [immunity_descriptor], new_mod, value, data)
	value = 'rule'
	data = mod_cell('Rule:', 10, [immunity_rule], new_mod, value, data)
	select =[{'type': 'trait', 'name': 'Immune From Trait', 'w': 18}, {'type': 'damage', 'name': 'Immune From Damage Type', 'w': 25}, {'type': 'descriptor', 'name': 'Immune From Descriptor', 'w': 25}, {'type': 'rule', 'name': 'Immune From Game Rule', 'w': 25}]
	new_mod = variable_mod(immunity_type, select, data, new_mod)
	body = mod_add(immunity, new_mod, body)	

	classname = cover
	cells = check_cell('Cover', 10, cover_check, classname, cells, True)
	new_mod = mod_create('Provides Cover', 17, classname)
	new_mod = mod_cell('Cover Type', 10, [cover_type], new_mod)
	body = mod_add(cover_check, new_mod, body)

	body = entry(cells, body)

	return (body)
	

def degree_mod_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'deg-mod'
	spot = "deg-mod-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	value = entry.value
	deg_type = entry.deg_type
	circ_value = entry.circ_value
	circ_turns = entry.circ_turns
	circ_trait_type = entry.circ_trait_type
	circ_trait = entry.circ_trait
	measure_type = entry.measure_type
	measure_val1 = entry.measure_val1
	measure_math = entry.measure_math
	measure_trait_type = entry.measure_trait_type
	measure_trait = entry.measure_trait
	measure_value = entry.measure_value
	measure_rank = entry.measure_rank
	deg_condition_type = entry.deg_condition_type
	condition_damage_value = entry.condition_damage_value
	condition_damage = entry.condition_damage
	condition1 = entry.condition1
	condition2 = entry.condition2
	keyword = entry.keyword
	nullify = entry.nullify
	cumulative = entry.cumulative
	linked = entry.linked
	level = entry.level

	extra = extra_name(extra_id)
	measure_math = math(Math, measure_math)
	measure_rank = name(Rank, measure_rank)
	level = name(PowerLevels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	deg_mod_type_select = [{'type': 'measure', 'name': 'Measurement'}, {'type': 'condition', 'name': 'Condition'}, {'type': 'circ', 'name': 'Circumstance'}, {'type': 'uncontrolled', 'name': 'Effect Uncontrolled'}, {'type': 'level', 'name': 'Level'}]
	deg_type = selects(deg_type, deg_mod_type_select)

	value_type_select = [{'type': '', 'name': 'Type'}, {'type': 'value', 'name': 'Value'}, {'type': 'math', 'name': 'Math'}]
	measure_type = selects(measure_type, value_type_select)

	condition_type_select = [{'type': '', 'name': 'Condition Type'}, {'type': 'condition', 'name': 'Condition Change'}, {'type': 'damage', 'name': 'Damage Condition'}]
	deg_condition_type = selects(deg_condition_type, condition_type_select)

	updown_select = [{'id': 1, 'name': 'Up'}, {'id': -1, 'name': 'Down'}]
	condition_damage = selects(condition_damage, updown_select)

	value = integer_convert(value)
	circ_value = integer_convert(circ_value)
	circ_turns = integer_convert(circ_turns)
	measure_val1 = integer_convert(measure_val1)
	measure_value = integer_convert(measure_value)
	measure_rank = integer_convert(measure_rank)
	condition_damage_value = integer_convert(condition_damage_value)
	condition_damage = integer_convert(condition_damage)
	nullify = integer_convert(nullify)




def degree_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'degree'
	spot = "degree-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows

	power_id = entry.power_id
	extra_id = entry.extra_id
	degree_type = entry.degree_type
	degree = entry.degree
	keyword = entry.keyword
	desscription = entry.desscription
	extra_effort = entry.extra_effort
	cumulative = entry.cumulative
	target = entry.target

	extra = extra_name(extra_id)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	degree = integer_convert(degree)

def environment_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'env'
	spot = "env-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	radius = entry.radius
	distance = entry.distance
	rank = entry.rank
	condition_check = entry.condition_check
	impede = entry.impede
	conceal = entry.conceal
	visibility = entry.visibility
	selective = entry.selective
	immunity = entry.immunity
	immunity_type = entry.immunity_type
	temp_type = entry.temp_type
	immunity_extremity = entry.immunity_extremity
	immunity_environment = entry.immunity_environment
	no_penalty = entry.no_penalty
	no_circumstance = entry.no_circumstance
	immunity_other = entry.immunity_other
	condition_temp_type = entry.condition_temp_type
	temp_extremity = entry.temp_extremity
	move_nature = entry.move_nature
	move_speed = entry.move_speed
	move_cost_circ = entry.move_cost_circ
	move_other = entry.move_other
	conceal_type = entry.conceal_type
	visibility_trait_type = entry.visibility_trait_type
	visibility_trait = entry.visibility_trait
	visibility_mod = entry.visibility_mod
	cost = entry.cost
	ranks = entry.ranks

	extra = extra_name(extra_id)

	environment_immunity_select = [{'type': '', 'name': 'Immune From'}, {'type': 'environment', 'name': 'Environment'}, {'type': 'condition', 'name': 'Condition'}]
	immunity_type = selects(immunity_type, environment_immunity_select)

	temp_type_select = [{'type': '', 'name': 'Type'}, {'type': 'all', 'name': 'All'}, {'type': 'cold', 'name': 'Cold'}, {'type': 'heat', 'name': 'Heat'}, {'type': 'pressure', 'name': 'High Pressure'}, {'type': 'radiation', 'name': 'Radiation'}, {'type': 'vaccum', 'name': 'Vaccuum'}]
	temp_type = selects(temp_type, temp_type_select)

	extremity_select = [{'type': '', 'name': 'Extremity'}, {'type': 'intense', 'name': 'Intense'}, {'type': 'extreme', 'name': 'Extreme'}]
	immunity_extremity = selects(immunity_extremity, extremity_select)

	environment_select = [{'type': '', 'name': 'Environment Type'}, {'type': 'underwater', 'name': 'Underwater'}, {'type': 'gravity', 'name': 'Zero Gravity'}, {'type': 'mountains', 'name': 'Mountains'}, {'type': 'jungle', 'name': 'Jungle'}, {'type': 'desert', 'name': 'Desert'}, {'type': 'volcano', 'name': 'Volcano'}, {'type': 'other', 'name': 'Other'}]
	immunity_environment = selects(immunity_environment, environment_select)

	condition_temp_type = selects(condition_temp_type, temp_type_select)

	temp_extremity = selects(temp_extremity, extremity_select)

	nature_select = [{'type': '', 'name': 'Nature'}, {'type': 'ice', 'name': 'Ice'}, {'type': 'rain', 'name': 'Rain'}, {'type': 'snow', 'name': 'Snow'}, {'type': 'wind', 'name': 'Wind'}, {'type': 'other', 'name': 'Other'}]
	move_nature = selects(move_nature, nature_select)

	conceal_type_select = [{'type': 'reduce', 'name': 'Reduce'}, {'type': 'eliminate', 'name': 'Eliminate'}]
	conceal_type = selects(conceal_type, conceal_type_select)

	radius = integer_convert(radius)
	distance = integer_convert(distance)
	rank = integer_convert(rank)
	move_speed = integer_convert(move_speed)
	visibility_mod = integer_convert(visibility_mod)
	cost = integer_convert(cost)
	ranks = integer_convert(ranks)

def levels_post(entry, columns, created, old_level_type):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns

	power_id = entry.power_id
	extra_id = entry.extra_id
	level_type = entry.level_type
	level = entry.level
	level_effect = entry.level_effect

	mods = []
	cells = []
	table_id = 'levels-' + level_type
	spot = "levels-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['rows'] = rows
	
	if old_level_type != level_type:
		body['created'] = False
	else:
		body['created'] = True
	body['title'] = level_type
	

	extra = extra_name(extra_id)

def minion_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'minion'
	spot = "minion-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	points = entry.points
	condition = entry.condition
	player_condition = entry.player_condition
	link = entry.link
	variable_type = entry.variable_type
	multiple = entry.multiple
	attitude = entry.attitude
	resitable = entry.resitable
	heroic = entry.heroic
	sacrifice = entry.sacrifice
	sacrifice_cost = entry.sacrifice_cost
	attitude_type = entry.attitude_type
	attitude_trait_type = entry.attitude_trait_type
	attitude_trait = entry.attitude_trait
	resitable_check = entry.resitable_check
	resitable_dc = entry.resitable_dc
	multiple_value = entry.multiple_value
	horde = entry.horde

	extra = extra_name(extra_id)	
	attitude_type = name(PowerLevels, attitude_type)
	resitable_check = name(Defense, resitable_check)

	minion_type_select = [{'type': '', 'name': 'Minion Type'}, {'type': 'specific', 'name': 'Specific'}, {'type': 'general', 'name': 'General'}, {'type': 'broad', 'name': 'Broad'}]
	variable_type = selects(variable_type, minion_type_select)

	points = integer_convert(points)
	sacrifice_cost = integer_convert(sacrifice_cost)
	resitable_dc = integer_convert(resitable_dc)
	multiple_value = integer_convert(multiple_value)

def mod_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'mod'
	spot = 'mod-spot'

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	affects_objects = entry.affects_objects
	area = entry.area
	persistent = entry.persistent
	incurable = entry.incurable
	selective = entry.selective
	limited = entry.limited
	innate = entry.innate
	others = entry.others
	sustained = entry.sustained
	reflect = entry.reflect
	redirect = entry.redirect
	half = entry.half
	affects_corp = entry.affects_corp
	continuous = entry.continuous
	vulnerable = entry.vulnerable
	precise = entry.precise
	progressive = entry.progressive
	subtle = entry.subtle
	permanent = entry.permanent
	points = entry.points
	ranks = entry.ranks
	action = entry.action
	side_effect = entry.side_effect
	concentration = entry.concentration
	simultaneous = entry.simultaneous
	effortless = entry.effortless
	noticeable = entry.noticeable
	unreliable = entry.unreliable
	objects_alone = entry.objects_alone
	objects_character = entry.objects_character
	effortless_degree = entry.effortless_degree
	effortless_retries = entry.effortless_retries
	simultaneous_descriptor = entry.simultaneous_descriptor
	area_mod = entry.area_mod
	area_range = entry.area_range
	area_per_rank = entry.area_per_rank
	area_descriptor = entry.area_descriptor
	limited_type = entry.limited_type
	limited_mod = entry.limited_mod
	limited_level = entry.limited_level
	limited_source = entry.limited_source
	limited_task_type = entry.limited_task_type
	limited_task = entry.limited_task
	limited_trait_type = entry.limited_trait_type
	limited_trait = entry.limited_trait
	limited_description = entry.limited_description
	limited_subjects = entry.limited_subjects
	limited_extra = entry.limited_extra
	limited_language_type = entry.limited_language_type
	limited_degree = entry.limited_degree
	limited_sense = entry.limited_sense
	limited_subsense = entry.limited_subsense
	limited_descriptor = entry.limited_descriptor
	limited_range = entry.limited_range
	side_effect_type = entry.side_effect_type
	side_level = entry.side_level
	side_other = entry.side_other
	reflect_check = entry.reflect
	reflect_trait_type = entry.reflect_trait_type
	reflect_trait = entry.reflect_trait
	reflect_descriptor = entry.reflect_descriptor
	subtle_opponent_trait_type = entry.subtle_opponent_trait_type
	subtle_opponent_trait = entry.subtle_opponent_trait
	subtle_dc = entry.subtle_dc
	subtle_null_trait_type = entry.subtle_null_trait_type
	subtle_null_trait = entry.subtle_opponent_trait
	others_carry = entry.others_carry
	others_touch = entry.others_touch
	others_touch_continuous = entry.others_touch_continuous
	ranks_trait_type = entry.ranks_trait_type
	ranks_trait = entry.ranks_trait
	ranks_ranks = entry.ranks_ranks
	ranks_mod = entry.ranks_mod
	points_type = entry.points_type
	points_reroll_target = entry.points_reroll_target
	points_reroll_cost = entry.points_reroll_cost
	points_rerolls = entry.points_rerolls
	points_reroll_result = entry.points_reroll_result
	ranks_cost = entry.ranks_cost
	cost = entry.cost

	extra = extra_name(extra_id)
	objects_alone = name(Defense, objects_alone)
	objects_character = name(Defense, objects_character)
	simultaneous_descriptor = descriptor_name(simultaneous_descriptor)
	area_descriptor = descriptor_name(area_descriptor)
	limited_level = name(PowerLevels, limited_level)
	limited_source = descriptor_name(limited_source)
	limited_extra = name(Extra, limited_extra)
	limited_sense = name(Sense, limited_sense)
	limited_descriptor = descriptor_name(limited_descriptor)
	limited_range = name(Range, limited_range)
	side_level = name(PowerLevels, side_level)
	reflect_check = name(Check, reflect_check)
	reflect_descriptor = descriptor_name(reflect_descriptor)

	limited_type_select = [{'type': '', 'name': 'Limited Against'}, {'type': 'task_type', 'name': 'Task Type'}, {'type': 'task', 'name': 'All tasks but One'}, {'type': 'trait', 'name': 'Trait'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'subjects', 'name': 'Subjects'}, {'type': 'language', 'name': 'Different Language'}, {'type': 'extra', 'name': 'Extra Effect'}, {'type': 'degree', 'name': 'Degree of Success'}, {'type': 'sense', 'name': 'Sense'},  {'type': 'range', 'name': 'Range'}, {'type': 'source', 'name': 'Requires Descriptor'}, {'type': 'other', 'name': 'Other'}, {'type': 'level', 'name': 'Level'}]
	limited_type   = selects(limited_type, limited_type_select)

	task_type_select = [{'type': '', 'name': 'Does Not Work On'}, {'type': 'physical', 'name': 'Physical Tasks'}, {'type': 'mental', 'name': 'Mental Tasks'}]
	limited_task_type = selects(limited_task_type, task_type_select)

	null_type_select = [{'type': '', 'name': 'Effect'}, {'type': 'null', 'name': 'Nullifies Effect'}, {'type': 'mod', 'name': 'Modifier to Check'}]
	limited_language_type = selects(limited_language_type, null_type_select)

	side_effects_select = [{'type': '', 'name': 'Side Effect'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'level', 'name': 'Level'}, {'type': 'other', 'name': 'Other'}]
	side_effect_type = selects(side_effect_type, side_effects_select)

	spend_select = [{'type': '', 'name': 'Effect'}, {'type': 'reroll', 'name': 'Re-roll'}]
	points_type = selects(points_type, spend_select)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	points_reroll_target = selects(points_reroll_target, targets_select)

	result_select = [{'type': '', 'name': 'Result'}, {'type': 'high', 'name': 'Higher'}, {'type': 'low', 'name': 'Lower'}]
	points_reroll_result = selects(points_reroll_result, result_select)

	effortless_degree = integer_convert(effortless_degree)
	area_mod = integer_convert(area_mod)
	area_range = integer_convert(area_range)
	limited_mod = integer_convert(limited_mod)
	limited_subjects = integer_convert(limited_subjects)
	limited_degree = integer_convert(limited_degree)
	subtle_dc = integer_convert(subtle_dc)
	ranks_ranks = integer_convert(ranks_ranks)
	ranks_mod = integer_convert(ranks_mod)
	points_reroll_cost = integer_convert(points_reroll_cost)
	points_rerolls = integer_convert(points_rerolls)
	points_reroll_result = integer_convert(points_reroll_result)
	ranks_cost = integer_convert(ranks_cost)
	cost = integer_convert(cost)



	
def move_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'move'
	spot = "move-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id
	rank = entry.rank
	math = entry.math	
	mod = entry.mod
	per_rank = entry.per_rank
	flight = entry.flight
	aquatic = entry.aquatic
	ground = entry.ground
	condition = entry.condition
	direction = entry.direction
	distance_type = entry.distance_type
	distance_value = entry.distance_value
	distance_math_value = entry.distance_math_value
	distance_math = entry.distance_math
	distance_math_value2 = entry.distance_math_value2
	distance_mod = entry.distance_mod
	dc = entry.dc
	others = entry.others
	continuous = entry.continuous
	subtle = entry.subtle
	concentration = entry.concentration
	obstacles = entry.obstacles
	objects = entry.objects
	permeate = entry.permeate
	special = entry.special
	prone = entry.prone
	check_type = entry.check_type
	obstacles_check = entry.obstacles_check
	concealment = entry.concealment
	extended = entry.extended
	mass = entry.mass
	mass_value = entry.mass_value
	extended_actions = entry.extended_actions
	acquatic_type = entry.acquatic_type
	concealment_sense = entry.concealment_sense
	concealment_trait_type = entry.concealment_trait_type
	concealment_trait = entry.concealment_trait
	permeate_type = entry.permeate_type
	permeate_speed = entry.permeate_speed
	permeate_cover = entry.permeate_cover
	special_type = entry.special_type
	teleport_type = entry.teleport_type
	teleport_change = entry.teleport_change
	teleport_portal = entry.teleport_portal
	teleport_obstacles = entry.teleport_obstacles
	dimension_type = entry.dimension_type
	dimension_mass_rank = entry.dimension_mass_rank
	dimension_descriptor = entry.dimension_descriptor
	special_space = entry.special_space
	special_time = entry.special_time
	special_time_carry = entry.special_time_carry
	ground_type = entry.ground_type
	ground_permanence = entry.ground_permanence
	ground_time = entry.ground_time
	ground_units = entry.ground_units
	ground_ranged = entry.ground_ranged
	subtle_trait_type = entry.subtle_trait_type
	subtle_trait = entry.subtle_trait
	subtle_mod = entry.subtle_mod
	flight_resist = entry.flight_resist
	flight_equip = entry.flight_equip
	flight_conditions = entry.flight_conditions
	objects_check = entry.objects_check
	objects_attack = entry.objects_attack
	objects_skill_type = entry.objects_skill_type
	objects_skill = entry.objects_skill
	objects_direction = entry.objects_direction
	objects_damage = entry.objects_damage
	damage_type = entry.damage_type
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_free = entry.check_free
	ranks = entry.ranks
	cost = entry.cost

	extra = extra_name(extra_id)
	math = math(Math, math)
	distance_math = math(Math, distance_math)
	concealment_sense = name(Sense, concealment_sense)
	dimension_descriptor = descriptor_name(dimension_descriptor)
	ground_type = name(Ground, ground_type)
	ground_units = name(Unit, ground_units)
	objects_check = name(Check, objects_check)
	objects_attack = name(ConflictAction, objects_attack)

	directions_select = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]
	direction = selects(direction, directions_select)

	aquatic_select = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}]
	acquatic_type = selects(acquatic_type, aquatic_select)

	openings_select = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]
	permeate_type = selects(permeate_type, openings_select)

	travel_select = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]
	special_type = selects(special_type, travel_select)

	teleport_change_select = [{'type': '', 'name': 'Can Change'}, {'type': 'direction', 'name': 'Direction'}, {'type': 'velocity', 'name': 'Velocity'}]
	teleport_change = selects(teleport_change, teleport_change_select)

	teleport_select = [{'type': '', 'name': 'Type'}, {'type': 'know', 'name': 'Know Destination'}, {'type': 'any', 'name': 'Any Destination'}]
	teleport_type = selects(teleport_type, teleport_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimension_type = selects(dimension_type, dimensions_select)

	space_select = [{'type': '', 'name': 'Space Travel Type'}, {'type': 'solar', 'name': 'Planets in Solar System'}, {'type': 'star', 'name': 'Other Star Systems'}, {'type': 'galaxy', 'name': 'Other Galaxies'}]
	special_space = selects(special_space, space_select)

	time_travel_select = [{'type': '', 'name': 'Time Travel Type'}, {'type': 'Fixed', 'name': 'Fixed Point in Time'}, {'type': 'past', 'name': 'Any Point in Past'}, {'type': 'future', 'name': 'Any Point in Future'}, {'type': 'timeline', 'name': 'Alternate Timeline'}, {'type': 'any', 'name': 'Any Point in time'}  ]
	special_time = selects(special_time, time_travel_select)

	permanence_select = [{'type': '', 'name': 'Permanence'},{'type': 'temp', 'name': 'Temporary'}, {'type': 'perm', 'name': 'Permanent'}]
	ground_permanence = selects(ground_permanence, permanence_select)

	flight_conditions = select_multiple(flight_conditions)

	move_objects_select = [{'type': '', 'name': 'Direction'}, {'type': 'all', 'name': 'All Directions'}, {'type': 'vertical', 'name': 'Up and Down'}, {'type': 'horizontal', 'name': 'Towards and Away'}, {'type': 'attract', 'name': 'Attraction'}, {'type': 'repel', 'name': 'Repulsion'}]
	objects_direction = selects(objects_direction, move_objects_select)

	rank = integer_convert(rank)
	mod = integer_convert(mod)
	distance_value = integer_convert(distance_value)
	distance_math_value = integer_convert(distance_math_value)
	distance_math_value2 = integer_convert(distance_math_value2)
	distance_mod = integer_convert(distance_mod)
	dc = integer_convert(dc)
	mass_value = integer_convert(mass_value)
	extended_actions = integer_convert(extended_actions)
	permeate_speed = integer_convert(permeate_speed)
	dimension_mass_rank = integer_convert(dimension_mass_rank)
	special_time_carry = integer_convert(special_time_carry)
	ground_time = integer_convert(ground_time)
	subtle_mod = integer_convert(subtle_mod)
	ranks = integer_convert(ranks)
	cost = integer_convert(cost)
	



def opposed_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'opposed'
	spot = "opposed-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id
	trait_type = entry.trait_type
	trait = entry.trait
	mod = entry.mod
	opponent_trait_type = entry.opponent_trait_type
	opponent_trait = entry.opponent_trait
	opponent_mod = entry.opponent_mod
	player_check = entry.player_check
	opponent_check = entry.opponent_check

	extra = extra_name(extra_id)
	player_check = name(Check, player_check)
	opponent_check = name(Check, opponent_check)

	mod = integer_convert(mod)
	opponent_mod = integer_convert(opponent_mod)


def ranged_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'ranged'
	spot = "ranged-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	range_type = entry.range_type
	flat_value = entry.flat_value
	flat_units = entry.flat_units
	flat_rank = entry.flat_rank
	flat_rank_value = entry.flat_rank_value
	flat_rank_units = entry.flat_rank_units
	flat_rank_rank = entry.flat_rank_rank
	flat_rank_distance = entry.flat_rank_distance
	flat_rank_distance_rank = entry.flat_rank_distance_rank
	units_rank_start_value = entry.units_rank_start_value
	units_rank_value = entry.units_rank_value
	units_rank_units = entry.units_rank_units
	units_rank_rank = entry.units_rank_rank
	rank_distance_start = entry.rank_distance_start
	rank_distance = entry.rank_distance
	rank_effect_rank = entry.rank_effect_rank
	effect_mod_math = entry.effect_mod_math
	effect_mod = entry.effect_mod
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait
	check_math = entry.check_math
	check_mod = entry.check_mod
	trait_trait_type = entry.trait_trait_type
	trait_trait = entry.trait_trait
	trait_math = entry.trait_math
	trait_mod = entry.trait_mod
	distance_mod_rank = entry.distance_mod_rank
	distance_mod_math = entry.distance_mod_math
	distance_mod_trait_type = entry.distance_mod_trait_type
	distance_mod_trait = entry.distance_mod_trait
	dc = entry.dc
	dc_value = entry.dc_value
	dc_trait_type = entry.dc_trait_type
	dc_trait = entry.dc_trait

	extra = extra_name(extra_id)
	flat_units = name(Unit, flat_units)
	flat_rank_units = name(Unit, flat_rank_units)
	units_rank_units = name(Unit, units_rank_units)
	effect_mod_math = math(Math, effect_mod_math)
	check_math = math(Math, check_math)
	trait_math = math(Math, trait_math)
	distance_mod_math = math(Math, distance_mod_math)

	flat_value = integer_convert(flat_value)
	flat_rank = integer_convert(flat_rank)
	flat_rank_value = integer_convert(flat_rank_value)
	flat_rank_rank = integer_convert(flat_rank_rank)
	flat_rank_distance = integer_convert(flat_rank_distance)
	flat_rank_distance_rank = integer_convert(flat_rank_distance_rank)
	units_rank_start_value = integer_convert(units_rank_start_value)
	units_rank_value = integer_convert(units_rank_value)
	units_rank_units = integer_convert(units_rank_units)
	units_rank_rank = integer_convert(units_rank_rank)
	rank_distance_start = integer_convert(rank_distance_start)
	rank_distance = integer_convert(rank_distance)
	rank_effect_rank = integer_convert(rank_effect_rank)
	effect_mod = integer_convert(effect_mod)
	check_mod = integer_convert(check_mod)
	trait_mod = integer_convert(trait_mod)
	distance_mod_rank = integer_convert(distance_mod_rank)
	dc_value = integer_convert(dc_value)


def resist_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'resistance'
	spot = "resistance-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	mod = entry.mod	
	rounds = entry.rounds
	circumstance = entry.circumstance
	resist_check_type = entry.resist_check_type
	trait_type = entry.trait_type
	trait = entry.trait
	descriptor = entry.descriptor
	requires_check = entry.requires_check
	check_type = entry.check_type
	check_trait_type = entry.check_trait_type
	check_trait = entry.check_trait

	extra = extra_name(extra_id)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	resistance_type_select = [{'type': '', 'name': 'Applies to'}, {'type': 'descriptor', 'name': 'Descriptor'}, {'type': 'trait', 'name': 'Check Type'}, {'type': 'harmed', 'name': 'Subject Harmed'}]
	resist_check_type = selects(resist_check_type, resistance_type_select)

	mod = integer_convert(mod)
	rounds = integer_convert(rounds)

def resisted_by_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'resist'
	spot = "resist-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id	
	trait_type = entry.trait_type
	dc = entry.dc
	mod = entry.mod
	description = entry.description
	trait = entry.trait
	effect = entry.effect
	level = entry.level
	degree = entry.degree
	descriptor = entry.descriptor
	weaken_max = entry.weaken_max
	weaken_restored = entry.weaken_restored
	condition1 = entry.condition1
	condition2 = entry.condition2
	damage =  entry.damage
	strength = entry.strength
	nullify_descriptor = entry.nullify_descriptor
	nullify_alternate = entry.nullify_alternate
	extra_effort = entry.extra_effort

	extra = extra_name(extra_id)
	level = name(PowerLevels, level)
	descriptor = descriptor_name(descriptor)
	nullify_descriptor = descriptor_name(nullify_descriptor)
	nullify_alternate = name(Defense, nullify_alternate)

	effects_select = [{'type': 'condition', 'name': 'Condition'}, {'type': 'damage', 'name': 'Damage'}, {'type': 'nullify', 'name': 'Nullifies Opponent Effect'}, {'type': 'trait', 'name': 'Weakened Trait'}, {'type': 'level', 'name': 'Level'}]
	effect = selects(effect, effects_select)

	dc = integer_convert(dc)
	mod = integer_convert(mod)
	degree = integer_convert(degree)
	weaken_max = integer_convert(weaken_max)
	weaken_restored = integer_convert(weaken_restored)
	damage =  integer_convert(damage)
	
def reverse_effect_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'reverse'
	spot = "reverse-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	degree = entry.degree
	when = entry.when
	check_check = entry.check_check
	time_check = entry.time_check
	trait_type = entry.trait_type
	trait = entry.trait
	value_type = entry.value_type
	value_dc = entry.value_dc
	math_dc = entry.math_dc
	math = entry.math
	time_value = entry.time_value
	time_unit = entry.time_unit

	extra = extra_name(extra_id)
	math = math(Math, math)
	time_unit = name(Unit, time_unit)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	whens_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]
	when = selects(when, whens_select)

	degree = integer_convert(degree)
	value_dc = integer_convert(value_dc)
	math_dc = integer_convert(math_dc)
	time_value = integer_convert(time_value)


def sense_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'sense'
	spot = "sense-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		

	power_id = entry.power_id
	extra_id = entry.extra_id
	target = entry.target
	sense = entry.sense
	subsense = entry.subsense
	sense_cost = entry.sense_cost
	subsense_cost = entry.subsense_cost
	skill = entry.skill
	skill_required = entry.skill_required
	sense_type = entry.sense_type
	height_trait_type = entry.height_trait_type
	height_trait = entry.height_trait
	height_power_required = entry.height_power_required
	height_ensense = entry.height_ensense
	resist_trait_type = entry.resist_trait_type
	resist_trait = entry.resist_trait
	resist_immune = entry.resist_immune
	resist_permanent = entry.resist_permanent
	resist_circ = entry.resist_circ
	objects = entry.objects
	exclusive = entry.exclusive
	gm = entry.gm
	dark = entry.dark
	lighting = entry.lighting
	time = entry.time
	dimensional = entry.dimensional
	radius = entry.radius
	accurate = entry.accurate
	acute = entry.acute
	time_set = entry.time_set
	time_value = entry.time_value
	time_unit = entry.time_unit
	time_skill = entry.time_skill	
	time_bonus = entry.time_bonus
	time_factor = entry.time_factor
	distance = entry.distance
	distance_dc = entry.distance_dc
	distance_mod = entry.distance_mod
	distance_value = entry.distance_value
	distance_unit = entry.distance_unit
	distance_factor = entry.distance_factor
	dimensional_type = entry.dimensional_type
	ranks = entry.ranks
	cost = entry.cost


	extra = extra_name(extra_id)
	skill = name(Skill, skill)
	time_unit = name(Unit, time_unit)
	time_skill = name(Skill, time_skill)
	distance_unit = name(Unit, distance_unit)
	sense = name(Sense, sense)
	subsense = name(SubSense, subsense)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	sense_type_select =  [{'type': '', 'name': 'Effect Type'}, {'type': 'height', 'name': 'Heightened'}, {'type': 'resist', 'name': 'Resistant'}]
	sense_type = selects(sense_type, sense_type_select)

	all_some_select = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]
	resist_permanent = selects(resist_permanent, all_some_select)

	darkness_select = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]
	lighting = selects(lighting, darkness_select)

	sense_time_select = [{'type': '', 'name': ''}, {'type': 'value', 'name': 'Value'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}]
	time_set = selects(time_set, sense_time_select)

	sense_distance_select = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'unit', 'name': 'By Rank (Units)'}, {'type': 'rank', 'name': 'By Rank'}]
	distance = selects(distance, sense_distance_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimensional_type = selects(dimensional_type, dimensions_select)

	sense_cost = db.Column_convert(db.Integer)
	subsense_cost = db.Column_convert(db.Integer)
	resist_circ = integer_convert(resist_circ)
	time_value = integer_convert(time_value)
	time_factor = integer_convert(time_factor)
	distance_dc = integer_convert(distance_dc)
	distance_mod = integer_convert(distance_mod)
	distance_value = integer_convert(distance_value)
	distance_factor = integer_convert(distance_factor)
	ranks = integer_convert(ranks)
	cost = integer_convert(cost)


def time_post(entry, columns, created):

	body = {}
	body['id'] = entry.id
	error = False
	error_msg = []
	body['success'] = True

	rows = columns
	mods = []
	cells = []
	table_id = 'time'
	spot = "time-spot"

	body['table_id'] = table_id
	body['spot'] = spot
	body['created'] = created
	body['title'] = ''
	body['rows'] = rows
		
	power_id = entry.power_id
	extra_id = entry.extra_id
	time_type = entry.time_type
	value_type = entry.value_type
	value = entry.value
	units = entry.units
	time_value = entry.time_value
	math = entry.math
	trait_type = entry.trait_type
	trait = entry.trait
	dc = entry.dc
	descriptor = entry.descriptor
	check_type = entry.check_type
	recovery = entry.recovery
	recovery_penalty = entry.recovery_penalty
	recovery_time = entry.recovery_time
	recovery_incurable = entry.recovery_incurable

	extra = extra_name(extra_id)
	units = name(Unit, units)
	math = math(Math, math)
	descriptor = descriptor_name(descriptor)
	check_type = name(Check, check_type)

	time_effect_select = [{'type': '', 'name': 'Time Type'}, {'type': 'action', 'name': 'Time Action Takes'}, {'type': 'limit', 'name': 'Time limit to Respond'}, {'type': 'lasts', 'name': 'Time Result Lasts'}]
	time_type = selects(time_type, time_effect_select)

	value = integer_convert(value)
	time_value = integer_convert(time_value)
	trait = integer_convert(trait)
	dc = integer_convert(descriptor)
	recovery_penalty = integer_convert(recovery_penalty)
	recovery_time = integer_convert(recovery_time)