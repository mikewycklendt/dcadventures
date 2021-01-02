from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerLevels, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

def name(Table, name):
	
	db = SQLAlchemy()

	if name == 0:
		name = 'All'
		return (name)

	if name is not None:
		try:
			query = db.session.query(Table).filter_by(id=name).one()
			name = query.name
		except:
			print('no entry')
	else:
		name = ''

	
	return (name)

def math_convert(Table, name):
	
	db = SQLAlchemy()

	if name is not None:
		try:
			query = db.session.query(Table).filter_by(id=name).one()
			name = query.symbol
		except:
			print('invalid id')
	else:
		name = ''
	
	return (name)

def extra_name(name):
	
	db = SQLAlchemy()

	if name is None:
		name = 'Base Power'
	else:
		try:
			query = db.session.query(Extra).filter_by(id=name).one()
			name = query.name
		except:
			print('invalid id')
	
	return (name)

def descriptor_name(name):
	
	db = SQLAlchemy()

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
	elif name is None:
		name = ''
	else:
		try:
			query = db.session.query(PowerDes).filter_by(id=name).one()
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

def string(word, data):

	output = ''

	print('\n\n\n\n')
	for d in data:
		print(d)
		if d != '' and d is not None:
			output = word
	
	return (output)

def check_convert(word, check):
	output = ''

	if check:
		output = word

	return (output)

def width(width, adjust, field):
	if field != '' and field is not None and field != False:
		width += adjust

	return (width)

def send(cells, body):

	body['cells'] = deepcopy(cells)
	rows = body['rows']
	entry_id = body['id']
	mods = body['mods']
	font = body['font']

	widths = []
	for cell in cells:
		width = cell['width']
		widths.append(width)

	new_row = {'id': entry_id, 'cells': widths}

	rows.append(new_row)
	print('\n\n')

	grid_update = grid_columns(rows, font)

	grid = grid_update['grid']
	font = grid_update['font']
	columns = grid_update['columns']
	saverows = grid_update['rows']

	body['rows'] = saverows
	print('\n')
	print(font)

	print(body['rows'])


	body['font'] = font
	body['grid'] = grid
	body['columns'] = columns

	return (body)


def delete_row(entry_id, rows):

	for i in range(0, len(rows), 1):
		row = rows[i]
		print(rows[i])
		if rows[i].get('id') == entry_id:
			del rows[i]
			break

	return (rows)

def grid_columns(rows, font):

	result = {}

	columns = []
	columns.clear()

	for row in rows:
		print(rows)

	saverows = deepcopy(rows)

	if not rows:
		grid = 'hide'
	else:
		gridrows = []
		for row in rows:
			row_cells = row['cells']
			gridrows.append(row_cells)

		
		
		if columns == []:
			columns = gridrows[0]
		
		for g in gridrows:
			if not columns:
				columns = g
			else:
				for i in range(0, len(columns), 1):
					if g[i] > columns[i]:
						columns[i] = g[i]

		

		grid = ''
		empty = 95
		for w in columns:
			empty = empty - w

		if empty < 0:
			while empty < 0:
				x = 95
				for i in range(0, len(columns), 1):
					if columns[i] > 4:
						columns[i] = columns[i] - 1
					x = x - columns[i]
				font = font - 4
				empty = x

		for column in columns:
			grid += str(column) + '% '
		
		grid += str(empty) + '%' + ' 5%'

	print(grid)
	print(columns)

	result['columns'] = columns
	result['grid'] = grid
	result['font'] = font
	result['rows'] = saverows

	return (result)


def vcell_add(title, field, vcells, cells):
	cell = {}
	cell['title'] = title
	content = ''
	width = 0

	for vcell in vcells:
		value = vcell['value']
		con = vcell['content']
		wid = vcell['width']
		if value == field:
			content = con
			width = wid

	cell['content'] = content
	cell['width'] = width

	cells.append(cell)

	return (cells)


def vcell(value, width, contentlist, vcells='e', value2='e', seletion2='e'):

	if vcells == 'e':
		new_vcells = []
		vcells = new_vcells

	cell = {}
	cell['value'] = value

	for c in contentlist:
		if c is None:
			c = ''
		else:
			try:
				c = str(c)
			except:
				if c == True:
					cell['width'] = width
					cell['content'] = c
					return (vcells)
				elif c == False:
					cell['width'] = 0
					cell['content'] = c
				else:
					c = ''

	content = ''

	print(content)

	for c in contentlist:
		if content == '':
			print
			content += c
		else:
			content += ' ' + c

	if content == '':
		width = 0

	cell['content'] = content
	cell['width'] = width

	if value2 == 'e':
		vcells.append(cell)
		return (vcells)

	if selection2 is None or selection2 == '':
		for vcell in vcells:
			vcell['value'] = val
			if value == val:
				return (vcells)
		
		vcells.append(cell)
		return (vcells)

	if value2 == selection2:
		vcells.append(cell)
		return (vcells)



def check_cell(title, width, check, cells, mod_check=False):

	if check == False:
		width = 0
		mod_check = False
	
	cell = {'title': title,
			'width': width,
			'content': check,
			'mod_check': mod_check
			}

	cells.append(cell)

	return (cells)

def cell(title, width, contentlist, cells=[]):

	cell = {}
	cell['title'] = title
		
	for c in contentlist:
		if c is None:
			c = ''
		else:
			try:
				c = str(c)
			except:
				try:
					cells = check_cell(title, width, c, classname)
					return (cells)
				except:
					c = ''
				
	content = ''

	for c in contentlist:
		if content == '':
			content = c
		else:
			content += ' ' + c

	if content == '':
		width = 0

	cell['content'] = content
	cell['width'] = width

	cells.append(cell)

	return (cells)

def mod_create(title, width, value='e', select='e'):

	mod = {'title': title,
			'cells': [],
			'variable': False
			}

	if value != 'e' and select != 'e':
		mod['value'] = value
		for option in select:
			if option['type'] == value:
				sub_title = option['name']
				mod['sub_title'] = sub_title
				sub_width = option['w']
				mod['variable'] = True

	variable = mod['variable']

	if variable:
		grid = '8% ' + str(width) + '% ' + str(sub_width) + '%' 
	else:
		grid = '8% ' + str(width) + '%'
	
	mod['grid'] = grid

	return (mod)

def mod_cell(title, width, content, mod, value='e'):

	variable = mod['variable']
	cells = mod['cells']
	grid = mod['grid']
	cell = {}
	contentwidth = 'auto'

	if variable:
		val = mod['value']
		if value != val:
			return (mod)

	for c in content:
		if c == False:
			return (mod)
		elif c is None:
			c = ''
		try:
			c = str(c)
		except:
			if c == True:
				contentwidth = '7%'
	

	text = ''

	for c in content:
		if c == True:
			text = c
		else:
			if text == '':
				text = c
			else:
				text += ' ' + c

	if text == '':
		return (mod)

	cell['title'] = title
	cell['content'] = text
	cells.append(cell)
	mod['cells'] = cells

	grid += ' ' + str(width) + '% ' + contentwidth

	mod['grid'] = grid 

	return (mod)

		
def mod_add(check, mod, body):

	grid = mod['grid']

	mods = body['mods']

	if check:
		mods.append(mod)

	body['mods'] = mods
	return (body)

	
def alt_check_post(entry, body, cells):
	
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

	check_type = [{'type': 'replace', 'name': 'Replace'}, {'type': 'extra', 'name': 'In Addition'}]
	when = selects(when, check_types)

	mod = integer_convert(mod)

	cells = cell('Extra', 15, [extra])
	cells = cell('Check', 14, [check_type], cells)
	cells = cell('Mod', 8, [mod], cells)
	cells = cell('Trait', 17, [trait], cells)
	cells = cell('When', 12, [when], cells)
	cells = cell('Circumstabce', 35, [circumstance], cells)
	
	body = send(cells, body)
	
	cells.clear()

	return (body)


def change_action_post(entry, body, cells):
	
	power_id = entry.power_id
	extra_id = entry.extra_id
	action = entry.action
	mod = entry.mod
	objects = entry.objects
	circumstance = entry.circumstance

	extra = extra_name(extra_id)
	action = name(Action, action)

	mod = integer_convert(mod)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Action', 17, [action], cells)
	cells = cell('Modifier', 12, [mod], cells)
	cells = check_cell('No Check', 9, objects, cells)
	cells = cell('Circumstance', 40, [circumstance], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def character_post(entry, body, cells):
		
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


	limited_select = [{'type': '', 'name': 'Enhanced While'}, {'type': 'day', 'name': 'Daytime'}, {'type': 'night', 'name': 'Nightime'}, {'type': 'water', 'name': 'Underwater'}, {'type': 'emotion', 'name': 'Emotional State'}, {'type': 'complication', 'name': 'Complication'}, {'type': 'other', 'name': 'Other Condition'}]
	limited_by = selects(limited_by, limited_select)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	appear_target =  selects(appear_target, targets_select)

	insub_select = [{'type': '', 'name': 'Insubstantial Type'}, {'type': 'fluid', 'name': 'Fluid'}, {'type': 'gas', 'name': 'Gaseous'}, {'type': 'energy', 'name': 'Energy'}, {'type': 'incorp', 'name': 'Incorporeal'}]
	insub_type = selects(insub_type, insub_select)
	
	traits_select = [{'type': '', 'name': 'Trait Type'}, {'type': 'this_power', 'name': 'This Power'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'power', 'name': 'Power'}, {'type': 'extra', 'name': 'Power Extra'}]
	weaken_broad = selects(weaken_broad, traits_select)

	value = integer_convert(value)
	increase = integer_convert(increase)
	reduced_value = integer_convert(reduced_value)
	carry_capacity = integer_convert(carry_capacity)
	points_value = integer_convert(points_value)
	cost = integer_convert(cost)
	ranks = integer_convert(ranks)	 


	
	cells = cell('Extra', 15, [extra])
	cells = cell('Trait', 14, [trait], cells)
	wid = 8
	perrank = string('Per', increase)
	rank = string('Rank', increase)
	wid = width(wid, 8, increase)
	cells = cell('Increase', wid, [value, perrank, increase, rank], cells)

	cells = check_cell('Limited', 8, limited, cells, True)
	new_mod = mod_create('Limited', 12)
	new_mod = mod_cell('Limited While:', 15, [limited_by], new_mod)
	body = mod_add(limited, new_mod, body)

	cells = check_cell('Reduced', 9, reduced, cells, True)
	new_mod = mod_create('Reduced Trait', 16)
	new_mod = mod_cell('Trait:', 8, [reduced_trait], new_mod)
	new_mod = mod_cell('Reduced By:', 12, [reduced_value], new_mod)
	new_mod = mod_cell('Normal Strength:', 16, [reduced_full], new_mod)
	body = mod_add(reduced, new_mod, body)

	cells = check_cell('Limbs', 8, limbs, cells, True)
	new_mod = mod_create('Extra Limbs', 14)
	new_mod = mod_cell('Continuous:', 11, [limbs_continuous], new_mod)
	new_mod = mod_cell('Sustained:', 10, [limbs_sustained], new_mod)
	new_mod = mod_cell('Distracting:', 12, [limbs_distracting], new_mod)
	new_mod = mod_cell('Projection:', 12, [limbs_projection], new_mod)
	body = mod_add(limbs, new_mod, body)

	cells = check_cell('Carry', 7, carry, cells, True)
	new_mod = mod_create('Extra Carry Capacity:', 25)
	sizerank = string('- Size Rank', [carry_capacity])
	new_mod = mod_cell('Maximum Size Rank', 22, [carry_capacity, sizerank], new_mod)
	body = mod_add(carry, new_mod, body)

	cells = check_cell('Sustained', 11, sustained, cells)
	cells = check_cell('Permanent', 10, permanent, cells)

	cells = check_cell('Points', 8, points, cells, True)
	new_mod = mod_create('Hero Points', 14)
	new_mod = mod_cell('Affected Trait', 18, [points_trait], new_mod)
	new_mod = mod_cell('Points:', 9, [points_value], new_mod)
	new_mod = mod_cell('Descriptor:', 12, [points_descriptor], new_mod)
	body = mod_add(points, new_mod, body)

	cells = check_cell('Appearance', 14, appear, cells, True)
	new_mod = mod_create('Alters Appearance', 20)
	new_mod = mod_cell('Target:', 7, [appear_target], new_mod)
	new_mod = mod_cell('Description:', 11, [appear_description], new_mod)
	body = mod_add(appear, new_mod, body)

	cells = check_cell('Insubstantial', 14, insubstantial, cells, True)
	new_mod = mod_create('Insubstantial', 16)
	new_mod = mod_cell('Type:', 6, [insub_type], new_mod)
	new_mod = mod_cell('Description:', 11, [insub_description], new_mod)
	body = mod_add(insubstantial, new_mod, body)

	cells = check_cell('Weaken', 8, weaken, cells, True)
	weaken_select = [{'type': 'trait', 'name': 'Specific', 'w': 12}, {'type': 'type', 'name': 'Broad Trait', 'w': 16}, {'type': 'descriptor', 'name': 'Broad Descriptor', 'w': 20}]
	new_mod = mod_create('Weaken', 10, weaken_type, weaken_select)
	value = 'trait'
	new_mod = mod_cell('Trait:', 8, [weaken_trait], new_mod, value)	
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	value = 'type'
	new_mod = mod_cell('Trait Type:', 12, [weaken_broad], new_mod, value)
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Descriptor:', 8, [weaken_descriptor], new_mod, value)
	new_mod = mod_cell('Simultaneous:', 15, [weaken_simultaneous], new_mod, value)
	body = mod_add(weaken, new_mod, body)

	cells = cell('Cost/Rank', 10, [cost], cells)
	cells = cell('Ranks', 8, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)

def circ_post(entry, body, cells):
		
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


	who_check_select = [{'type': '', 'name': 'Whose Check'}, {'type': 'player', 'name': 'Player Check'}, {'type': 'opponent', 'name': 'Opponent Check'}]
	check_who = selects(check_who, who_check_select)

	
	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	circ_range = integer_convert(circ_range)


	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 12, [target], cells)
	cells = cell('Modifier', 9, [mod], cells)
	cells = cell('Lasts', 8, [rounds], cells)

	circrange = string('Range', [circ_range])
	vcells = vcell('range', 20, [circ_range, circrange])
	vcells = vcell('check', 25, [check_who, check_trait], vcells)
	cells = vcell_add('Trigger', circ_type, vcells, cells)

	vcells = vcell('trait', 17, [null_trait])
	vcells = vcell('descriptor', 19, [null_descriptor], vcells)
	vcells = vcell('condition', 17, [null_condition], vcells)	
	cells = vcell_add('Nullified', null_type, vcells, cells)

	cells = cell('Circumstance', 35, [description], cells)

	body = send(cells, body)


	cells.clear()

	return (body)


def create_post(entry, body, cells):
	
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
	trap_resist_trait = entry.trap_resist_trait
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

	moveable_select = [{'type': '', 'name': 'Moveable With'}, {'type': 'auto', 'name': 'Automatic'}, {'type': 'immoveable', 'name': 'Immoveable'}, {'type': 'ability', 'name': 'Ability'}, {'type': 'skill', 'name': 'Skill'}, {'type': 'bonus', 'name': 'Enhanced Skill'}, {'type': 'defense', 'name': 'Defense'}, {'type': 'power', 'name': 'Power'}]
	move_player = selects(move_player, moveable_select)

	against_select = [{'type': '', 'name': 'Check Against'}, {'type': 'dc', 'name': 'DC'}, {'type': 'trait', 'name': 'Opponent Trait'} ]
	trap_type = selects(trap_type, against_select)

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
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Solidity', 11, [solidity], cells)
	cells = cell('Visibility', 9, [visibility], cells)
	cells = cell('Complexity', 12, [complexity], cells)
	cells = cell('Volume', 8, [volume], cells)
	cells = cell('Toughness', 11, [toughness], cells)
	cells = cell('Mass', 9, [mass], cells)
	cells = check_cell('Damageable', 12, damageable, cells)
	cells = check_cell('Maintained', 12, maintained, cells)
	cells = check_cell('Repairable', 12, repairable, cells)
	
	cells = check_cell('Moveable', 10, moveable, cells, True)
	new_mod = mod_create('Moveable', 13)
	new_mod = mod_cell('Trait:', 8, [move_player_trait], new_mod)
	new_mod = mod_cell('Ability to Move:', 16, [move_opponent_ability], new_mod)
	new_mod = mod_cell('Rank:', 8, [move_opponent_rank], new_mod)
	body = mod_add(moveable, new_mod, body)

	cells = check_cell('Stationary', 13, stationary, cells, True)
	new_mod = mod_create('Stationary', 14)
	new_mod = mod_cell('Trait:', 8, [move_player_trait], new_mod)
	new_mod = mod_cell('Ability to Move:', 16, [move_opponent_ability], new_mod)
	new_mod = mod_cell('Rank:', 8, [move_opponent_rank], new_mod)
	body = mod_add(stationary, new_mod, body)

	cells = check_cell('Trap', 7, trap, cells, True)
	new_mod = mod_create('Trap', 6)
	new_mod = mod_cell('DC:', 4, [trap_dc], new_mod)
	new_mod = mod_cell('Trait:', 15, [trap_trait], new_mod)
	new_mod = mod_cell('Resistance Trait:', 19, [trap_resist_trait], new_mod)
	new_mod = mod_cell('Resistance DC:', 18, [trap_resist_dc], new_mod)
	new_mod = mod_cell('Can Escape:', 11, [trap_escape], new_mod)
	body = mod_add(trap, new_mod, body)

	cells = check_cell('Ranged', 8, ranged, cells, True)
	determined_select = [{'type': 'dc', 'name': 'DC', 'w': 5}, {'type': 'target', 'name': 'Target Trait', 'w': 16}, {'type': 'player', 'name': 'Player Trait', 'w': 16}]
	new_mod = mod_create('Ranged', 9, ranged_type, determined_select)
	value = 'dc'
	new_mod = mod_cell('Value:', 8, [ranged_dc], new_mod, value)
	new_mod = mod_cell('Damage Type:', 17, [ranged_damage_type], new_mod, value)
	new_mod = mod_cell('Damage Value:', 19, [ranged_damage_value], new_mod, value)
	value = 'target'
	new_mod = mod_cell('Trait:', 7, [ranged_trait], new_mod, value)
	new_mod = mod_cell('Damage Type:', 17, [ranged_damage_type], new_mod, value)
	new_mod = mod_cell('Damage Value:', 19, [ranged_damage_value], new_mod, value)
	value = 'player'
	new_mod = mod_cell('Trait:', 7, [ranged_trait], new_mod, value)
	new_mod = mod_cell('Damage Type:', 17, [ranged_damage_type], new_mod, value)
	new_mod = mod_cell('Damage Value:', 19, [ranged_damage_value], new_mod, value)
	body = mod_add(ranged, new_mod, body)

	cells = check_cell('Weapon', 9, weapon, cells, True)
	new_mod = mod_create('Weapon', 10)
	new_mod = mod_cell('Trait:', 7, [weapon_trait], new_mod)
	new_mod = mod_cell('Modifier:', 9, [weapon_mod], new_mod)
	new_mod = mod_cell('Damage Type:', 14, [weapon_damage_type], new_mod)
	new_mod = mod_cell('Damage:', 8, [weapon_damage], new_mod)
	body = mod_add(weapon, new_mod, body)

	cells = check_cell('Support', 9, support, cells, True)
	new_mod = mod_create('Supports Weight', 19)
	new_mod = mod_cell('Strength Rank:', 14, [support_strength], new_mod)
	new_mod = mod_cell('Strength with Action:', 14, [support_action], new_mod)
	new_mod = mod_cell('Rounds:', 7, [support_action_rounds], new_mod)
	new_mod = mod_cell('With Extra Efffort:', 14, [support_effort], new_mod)
	new_mod = mod_cell('Extra Effort Rounds:', 14, [support_effort_rounds], new_mod)
	body = mod_add(support, new_mod, body)

	cells = check_cell('Appears Real', 15, real, cells)
	cells = check_cell('Cover', 8, cover, cells)
	cells = check_cell('Conceal', 8, conceal, cells)
	cells = check_cell('Blocks Incoming', 16, incoming, cells)
	cells = check_cell('Blocks Outgoing', 16, outgoing, cells)
	cells = check_cell('Transform', 10, transform, cells, True)
	new_mod = mod_create('Transform', 12)
	new_mod = mod_cell('Type', 5, [transform_type], new_mod)
	word = string('Per Rank', [transform_start_mass, transfom_mass])
	new_mod = mod_cell('Mass', 6, [transform_start_mass, transfom_mass, word], new_mod)
	new_mod = mod_cell('Start Descriptor', 17, [transform_start_descriptor], new_mod)
	new_mod = mod_cell('End Descriptor', 15, [transform_end_descriptor], new_mod)
	body = mod_add(transform, new_mod, body)

	cells = cell('Cost/Rank', 10, [cost], cells)
	cells = cell('Ranks', 8, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def damage_post(entry, body, cells):

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


	
	cells = cell('Extra', 15, [extra])
	cells = cell('Trait', 8, [trait], cells)
	cells = cell('Modifier', 11, [mod], cells)
	cells = check_cell('Strength Based', 16, strength, cells)
	cells = cell('Damage Type', 14, [damage_type], cells)
	cells = cell('Descriptor', 12, [descriptor], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def dc_table_post(entry, body, cells):
		
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
	math = math_convert(Math, math)
	descriptor = descriptor_name(descriptor)
	level = name(PowerLevels, level)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	
	possess_select = [{'type': '', 'name': 'Possession'}, {'type': 'possess', 'name': 'While Possessing'}, {'type': 'oppose', 'name': 'While Opposing'}]
	descriptor_possess = selects(descriptor_possess, possess_select)

	value = integer_convert(value)
	math_value = integer_convert(math_value)
	check_mod = integer_convert(check_mod)

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 14, [target], cells)
	vcells = vcell('value', 7, [value])
	vcells = vcell('math', 15, [math_value, math, math_trait], vcells)
	cells = vcell_add('DC', dc, vcells, crlls)

	cells = check_cell('Descriptor', 14, [descriptor_check], cells, True)
	new_mod = mod_cell('Descriptor', 12, [descriptor], new_mod)
	new_mod = mod_cell('Possession', 12, [descriptor_possess], new_mod)	
	body = mod_add(descriptor_check, new_mod, body)

	cells = check_cell('Condition', 13, [condition], cells, True)
	new_mod = mod_create('Condition', 12)
	word = string('to', [condition1, condition2])
	new_mod = mod_cell('Conditions', 14, [condition1, word, condition2], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Keyword', 10, [keyword_check], cells, True)
	new_mod = mod_create('Keyword', 10)
	new_mod = mod_cell('Key:', 7, [keyword], new_mod)
	body = mod_add(keyword_check, new_mod, body)

	cells = check_cell('Check', 7, [check_type], cells, True)
	new_mod = mod_create('Check Type', 15)
	new_mod = mod_cell('Trait:', 7, [check_trait], new_mod)
	new_mod = mod_cell('Modifier:', 12, [check_mod], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Level', 7, [levels], cells, True)
	new_mod = mod_create('Level', 8)
	new_mod = mod_cell('Level:', 7, [level], new_mod)
	body = mod_add(levels, new_mod, body)

	cells = cell('Description', 40, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def defense_post(entry, body, cells):

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

	outcome_select = [{'type': '', 'name': ''}, {'type': '<', 'name': 'Lower'}, {'type': '>', 'name': 'Higher'}]
	outcome = selects(outcome, outcome_select)

	cells.clear()

	cells = cell('Extra', 15, [extra])
	cells = cell('Defense', 12, [defense])
	cells = cell('Use', 10, [use], cells)
	cells = cell('Mod', 7, [mod], cells)
	word = string('or', [roll, outcome])
	print('\n\n\n')
	print(word)
	print(roll)
	print(outcome)
	cells = cell('Roll', 10, [roll, word, outcome], cells)
	cells = check_cell('Dodge', 7, dodge, cells)
	cells = check_cell('Fortitude', 10, fortitude, cells)
	cells = check_cell('Parry', 7, parry, cells)
	cells = check_cell('Toughness', 10, toughness, cells)
	cells = check_cell('Will', 5, will, cells)
	cells = check_cell('Resists Area', 12, resist_area, cells)
	cells = check_cell('Resists Perception', 19, resist_perception, cells)
	
	cells = check_cell('Reflect', 10, reflect, cells, True)
	select = [{'type': 1, 'name': 'Skill Check', 'w': 10}, {'type': 2, 'name': 'Opposed Check', 'w': 15}, {'type': 3, 'name': 'Routine Check', 'w': 15}, {'type': 4, 'name': 'Team Check', 'w': 15}, {'type': 5, 'name': 'Attack Check', 'w': 15}, {'type': 6, 'name': 'Resistance Check', 'w': 15}, {'type': 7, 'name': 'Comparison Check', 'w': 15}]
	new_mod = mod_create('Reflects Attacks', 17, reflect_check, select)

	value = 1
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('DC:', 7, [reflect_dc], new_mod, value)
	value = 2
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('Opposed By:', 15, [reflect_opposed_trait], new_mod, value)
	value = 3
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 4
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 5
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	value = 6
	new_mod = mod_cell('Action Type', 15, [reflect_action], new_mod, value)
	new_mod = mod_cell('Resisted By', 15, [reflect_resist_trait], new_mod, value)
	body = mod_add(reflect, new_mod, body)
	value = 7
	new_mod = mod_cell('Action Type:', 15, [reflect_action], new_mod, value)
	cells = check_cell('Immunity', 10, immunity, cells, True)
	select =[{'type': 'trait', 'name': 'Immune From Trait', 'w': 18}, {'type': 'damage', 'name': 'Immune From Damage Type', 'w': 25}, {'type': 'descriptor', 'name': 'Immune From Descriptor', 'w': 25}, {'type': 'rule', 'name': 'Immune From Game Rule', 'w': 25}]
	new_mod = mod_create('Immunity', 17, immunity_type, select)
	value = 'trait'
	new_mod = mod_cell('Trait:', 15, [immunity_trait], new_mod, value)
	value = 'damage'
	new_mod = mod_cell('Damage:', 10, [immunity_damage], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Descriptor:', 15, [immunity_descriptor], new_mod, value)
	value = 'rule'
	new_mod = mod_cell('Rule:', 10, [immunity_rule], new_mod, value)
	body = mod_add(immunity, new_mod, body)	

	cells = check_cell('Cover', 7, cover_check, cells, True)
	new_mod = mod_create('Provides Cover', 20)
	new_mod = mod_cell('Cover Type', 18, [cover_type], new_mod)
	body = mod_add(cover_check, new_mod, body)
		

	body = send(cells, body)

	cells.clear()

	return (body)

	

def degree_mod_post(entry, body, cells):

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
	measure_math = math_convert(Math, measure_math)
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

	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 14, [target], cells)
	cells = cell('Degree', 7, [value], cells)
	cells = cell('Keyword', 14, [keyword], cells)
	cells = cell('Nullify DC', 10, [value], cells)
	cells = check_cell('Cumulative', 12, cumulative, cells)
	cells = check_cell('Linked', 7, linked, cells)
	word = string('for', [circ_trait, circ_value, circ_turns])
	word2 = stromg('Turns', [circ_trait, circ_value, circ_turns])
	vcells = vcell('circ', 24, [circ_trait, circ_value, word, circ_turns, word2], vcells) 
	vcells = vcell('uncontrolled', 12, ['Uncontrolled'], vcells)
	vcells = vcell('level', 10, [level], vcells)
	vcells = vcell('measure', 17, [measure_value, measure_rank], vcells, 'value', measure_type)
	vcells = vcell('measure', 18, [measure_val1, measure_math, measure_trait], vcells, 'math', measure_type)
	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 25, [condition1, word, condition2], vcells, 'condition', deg_condition_type)
	word = string('Condition', [condition_damage_value, condition_damage])
	vcells = vcell('condition', 17, [condition_damage_value, word, condition_damage], vcells, 'damage', deg_condition_type)
	vcell_add('Effect', deg_type, vcells, cells)
	
	body = send(cells, body)

	cells.clear()

	return (body)



def degree_post(entry, body, cells):

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

	
	cells = cell('Extra', 15, [extra])



	body = send(cells, body)

	cells.clear()

	return (body)


def environment_post(entry, body, cells):
		
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

	
	cells = cell('Extra', 15, [extra])
	cells = cell('Start Radius', 16, [radius]. cells)
	word = string('Per', [distance, rank], cells)
	word2 = string('Rank', [distance, rank], cells)
	cells = cell('Radius', 14, [distance, word, rank, word2], cells)
	cells = check_cell('Condition', 9, condition, cells, True)
	new_mod = mod_create('Temperature Condition', 25)
	new_mod = mod_cell('Temperature Type:', 20, [condition_temp_type], new_mod)
	new_mod = mod_cell('Extremity:', 10, [temp_extremity], new_mod)
	body = mod_add(condition, new_mod, body)

	cells = check_cell('Impede', 7, impede, cells, True)
	new_mod = mod_create('Impede Movement', 20)
	new_mod = mod_cell('Nature Type:', 12, [move_nature], new_mod)
	new_mod = mod_cell('Other:', 7, [move_other], new_mod)
	new_mod = mod_cell('Speed:', 7, [move_speed], new_mod)
	new_mod = mod_cell('Surface Modifier:', 18, [move_cost_circ], new_mod)
	body = mod_add(impede, new_mod, body)

	cells = check_cell('Counter Conceal', 17, conceal, cells, True)
	new_mod = mod_create('Counters Concealment', 23)
	new_mod = mod_cell('Type:', 7, [conceal_type], new_mod)
	body = mod_add(conceal, new_mod, body)

	cells = check_cell('Visibility', 13, visibility, cells, True)
	new_mod = mod_create('Lessen Visibility', 22)
	new_mod = mod_cell('Trait:', 7, [visibility_trait], new_mod)
	new_mod = mod_cell('Modifier:', 11, [visibility_mod], new_mod)
	body = mod_add(visibility, new_mod, body)

	cells = check_cell('Selective', 10, selective, cells)
	cells = check_cell('Immunity', 11, immunity, cells, True)
	environment_immunity_select = [{'type': 'environment', 'name': 'Environment', 'w': 13}, {'type': 'condition', 'name': 'Condition', 'w': 12}]
	new_mod = mod_create('Immunity', 12, immunity_type, environment_immunity_select)
	value = 'environment'
	new_mod = mod_cell('Type', 6, [immunity_environment], new_mod, value)
	new_mod = mod_cell('No Penalty', 13, [no_penalty], new_mod, value)
	new_mod = mod_cell('No Circumstance', 16, [no_circumstance], new_mod, value)
	value = 'condition'
	new_mod = mod_cell('Type', 6, [temp_type], new_mod, value)
	new_mod = mod_cell('Extremity', 10, [immunity_extremity], new_mod, value)
	body = mod_add(immunity, new_mod, body)

	cells = cell('Cost/Rank', 10, [cost], cells)
	cells = cell('Ranks', 6, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def levels_post(entry, body, cells):

	power_id = entry.power_id
	extra_id = entry.extra_id
	level_type = entry.level_type
	level = entry.level
	level_effect = entry.level_effect

	

	extra = extra_name(extra_id)

	
	cells = cell('Extra', 15, [extra])



	body = send(cells, body)

	cells.clear()

	return (body)


def minion_post(entry, body, cells):
		
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

	cells = cell('Extra', 15, [extra])
	cells = cell('Points', 8, [points], cells)
	cells = cell('Minion Condition', 16, [condition], cells)
	cells = cell('Player Condition', 16, [player_condition], cells)
	cells = cell('Type', 10, [variable_type], cells)
	cells = check_cell('Link', 7, [link], cells)
	cells = check_cell('Multiple', 9, multiple, cells, True)
	new_mod = mod_create('Multiple Minions', 20)
	new_mod  = mod_cell('Count', 7, [multiple_value], new_mod)
	new_mod  = mod_cell('Horde', 7, [horde], new_mod)
	body = mod_add(multiple, new_mod, body)
	
	cells = check_cell('Attitide', 9, attitude, cells, True)
	new_mod = mod_create('Attitude', 11)
	new_mod  = mod_cell('Level', 7, [attitude_type], new_mod)
	new_mod  = mod_cell('Trait to Control', 18, [attitude_trait], new_mod)
	body = mod_add(attitude, new_mod, body)
	
	cells = check_cell('Resistable', 9, resitable, cells, True)
	new_mod = mod_create('Resistable', 11)
	new_mod  = mod_cell('Defense', 9, [resitable_check], new_mod)
	new_mod  = mod_cell('DC', 4, [resitable_dc], new_mod)
	body = mod_add(resitable, new_mod, body)
	
	cells = check_cell('Heroic', 7, [heroic], cells)
	cells = check_cell('Sacrifice', 9, sacrifice, cells, True)
	new_mod = mod_create('Sacrifice', 11)
	new_mod  = mod_cell('Cost', 6, [sacrifice_cost], new_mod)
	body = mod_add(sacrifice, new_mod, body)
	body = send(cells, body)

	cells.clear()

	return (body)

def mod_post(entry, body, cells):
		
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
	radius = entry.radius
	accurate = entry.accurate
	acute = entry.acute
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
	reflect_check = entry.reflect_check
	reflect_dc = entry.reflect_dc
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

	task_type_select = [{'type': '', 'name': 'Does Not Work On'}, {'type': 'physical', 'name': 'Physical Tasks'}, {'type': 'mental', 'name': 'Mental Tasks'}]
	limited_task_type = selects(limited_task_type, task_type_select)

	null_type_select = [{'type': '', 'name': 'Effect'}, {'type': 'null', 'name': 'Nullifies Effect'}, {'type': 'mod', 'name': 'Modifier to Check'}]
	limited_language_type = selects(limited_language_type, null_type_select)

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

	
	cells = cell('Extra', 15, [extra])
	cells = check_cell('Affects Objects', 16, affects_objects, cells, True)
	new_mod = mod_create('Affects Objects', 20)
	new_mod = mod_cell('Objects Alone', 17, [objects_alone], new_mod)
	new_mod = mod_cell('With Character', 15, [objects_character], new_mod)
	body = mod_add(affects_objects, new_mod, body)

	cells = check_cell('Area', 7, area, cells, True)
	new_mod = mod_create('Area', 6)
	new_mod = mod_cell('Modifier', 9, [area_mod], new_mod)
	new_mod = mod_cell('Range', 7, [area_range], new_mod)
	body = mod_add(area, new_mod, body)

	cells = check_cell('Persistant', 10, persistent, cells)
	cells = check_cell('Incurable', 8, incurable, cells)
	cells = check_cell('Selective', 9, selective, cells)

	cells = check_cell('Limited', 8, limited, cells, True)
	limited_type_select = [{'type': 'task_type', 'name': 'Limited by Task Type', 'w': 23}, {'type': 'task', 'name': 'Limited by All tasks but One', 'w': 34}, {'type': 'trait', 'name': 'Limited by Trait', 'w': 19}, {'type': 'descriptor', 'name': 'Limited by Descriptor', 'w': 23}, {'type': 'subjects', 'name': 'Limited by Subjects', 'w': 22}, {'type': 'language', 'name': 'Limited by Language', 'w': 24}, {'type': 'extra', 'name': 'Limited to Extra', 'w': 20}, {'type': 'degree', 'name': 'Limited by Degree of Success', 'w': 33}, {'type': 'sense', 'name': 'Limited by Sense', 'w': 19},  {'type': 'range', 'name': 'Limited by Range', 'w': 19}, {'type': 'source', 'name': 'Limited by Requireed Descriptor', 'w': 35}, {'type': 'other', 'name': 'Limited by Other Factor', 'w': 27}, {'type': 'level', 'name': 'Limited by Level', 'w': 19}]
	new_mod = mod_create('Limited', 9, limited_type, limited_type_select)
	value = 'task_type'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell("Doesn't Work On:", 16, [limited_task_type], new_mod, value)
	value = 'task'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Task:', 6, [limited_task], new_mod, value)
	value = 'trait'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Trait:', 7, [limited_trait], new_mod, value)
	value = 'descriptor'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Descriptor:', 12, [limited_descriptor], new_mod, value)
	value = 'subjects'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Number of Affected Characters:', 28, [limited_subjects], new_mod, value)
	value = 'language'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Effect:', 8, [limited_language_type], new_mod, value)
	value = 'extra'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Extra Effect:', 15, [limited_extra], new_mod, value)
	value = 'degree'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Degree:', 8, [limited_degree], new_mod, value)
	value = 'sense'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Sense:', 7, [limited_sense], new_mod, value)
	new_mod = mod_cell('Subsense:', 10, [limited_subsense], new_mod, value)
	value = 'range'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Range:', 7, [limited_range], new_mod, value)
	value = 'source'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Required Descriptor:', 20, [limited_source], new_mod, value)
	value = 'other'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Other Factor:', 16, [limited_description], new_mod, value)
	value = 'level'
	new_mod = mod_cell('Modifier', 9, [limited_mod], new_mod, value)
	new_mod = mod_cell('Level:', 7, [limited_level], new_mod, value)
	body = mod_add(limited, new_mod, body)

	cells = check_cell('Innate', 8, innate, cells)

	cells = check_cell('Affects Others', 15, others, cells, True)
	new_mod = mod_create('Affects Others', 17)
	new_mod = mod_cell('Requires Carrying:', 18, [others_carry], new_mod)
	new_mod = mod_cell('Requires Touch:', 18, [others_touch], new_mod)
	new_mod = mod_cell('Continous Touch:', 18, [others_touch_continuous], new_mod)
	body = mod_add(others, new_mod, body)

	cells = check_cell('Sustained', 9, sustained, cells)

	cells = check_cell('Reflect', 8, reflect, cells, True)
	new_mod = mod_create('Reflect', 8)
	new_mod = mod_cell('Check:', 7, [reflect_check], new_mod)
	new_mod = mod_cell('DC:', 5, [reflect_dc], new_mod)
	new_mod = mod_cell('Trait:', 8, [reflect_trait], new_mod)
	new_mod = mod_cell('Descriptor:', 12, [reflect_descriptor], new_mod)
	body = mod_add(others, new_mod, body)
	
	body = mod_add(reflect, new_mod, body)

	cells = check_cell('Redirect', 8, redirect, cells)
	cells = check_cell('Half', 7, half, cells)
	cells = check_cell('Affects Corporeal', 17, affects_corp, cells)
	cells = check_cell('Continuous', 10, continuous, cells)
	cells = check_cell('Vulnerable', 11, vulnerable, cells)
	cells = check_cell('Precise', 8, precise, cells)
	cells = check_cell('Progressive', 11, progressive, cells)

	cells = check_cell('Subtle', 7, subtle, cells, True)
	new_mod = mod_create('Subtle', 8)
	new_mod = mod_cell('Opponent Trait:', 17, [subtle_opponent_trait], new_mod)
	new_mod = mod_cell('DC:', 4, [subtle_dc], new_mod)
	new_mod = mod_cell('Nullfied Trait:', 17, [subtle_null_trait], new_mod)
	body = mod_add(subtle, new_mod, body)

	cells = check_cell('Permanent', 10, permanent, cells)

	cells = check_cell('Points', 8, points, cells, True)
	new_mod = mod_create('Points Rerolls', 17)
	new_mod = mod_cell('Target:', 8, [points_reroll_target], new_mod)
	new_mod = mod_cell('Cost:', 6, [points_reroll_cost], new_mod)
	new_mod = mod_cell('Rerolls:', 10, [points_reroll_result], new_mod)

	body = mod_add(points, new_mod, body)

	cells = check_cell('Ranks', 7, ranks, cells, True)
	new_mod = mod_create('Gain Trait', 12)
	new_mod = mod_cell('Trait:', 7, [ranks_trait], new_mod)
	new_mod = mod_cell('Ranks:', 6, [ranks_ranks], new_mod)
	new_mod = mod_cell('Modifier:', 9, [ranks_mod], new_mod)	
	body = mod_add(ranks, new_mod, body)
	cells = check_cell('Action', 7, action, cells)
	
	cells = check_cell('Side Effect', 12, side_effect, cells, True)
	side_effects_select = [{'type': 'complication', 'name': 'Complication', 'w': 14}, {'type': 'level', 'name': 'Level', 'w': 8}, {'type': 'other', 'name': 'Other', 'w': 8}]
	new_mod = mod_create('Side Effect', 13, side_effect_type, side_effects_select)
	value = 'complication'
	value = 'level'	
	new_mod = mod_cell('Level:', 8, [side_level], new_mod, value)
	value = 'other'
	new_mod = mod_cell('Other Side Effect:', 22, [side_other], new_mod, value)
	body = mod_add(side_effect, new_mod, body)
	
	cells = check_cell('Concentration', 13, concentration, cells)
	
	cells = check_cell('Simultaneous', 13, simultaneous, cells, True)
	new_mod = mod_create('Simultaneous', 14)
	new_mod = mod_cell('Descriptor:',13 , [simultaneous_descriptor], new_mod)
	body = mod_add(simultaneous, new_mod, body)
	
	cells = check_cell('Effortless', 11, effortless, cells, True)
	new_mod = mod_create('Effortless', 12)
	new_mod = mod_cell('Degree:', 8, [effortless_degree], new_mod)
	new_mod = mod_cell('Unlimited Retries:', 20, [effortless_retries], new_mod)	
	body = mod_add(effortless, new_mod, body)
	
	cells = check_cell('Noticeable', 11, noticeable, cells)
	cells = check_cell('Unreliable', 11, unreliable, cells)
	cells = check_cell('Radius', 7, ranks, cells)
	cells = check_cell('Accurate', 9, accurate, cells)
	cells = check_cell('Acute', 7, acute, cells)
	cells = cell('Cost/Rank', 10, cost, cells)
	cells = cell('Ranks', 10, ranks_cost, cells)

	body = send(cells, body)

	cells.clear()

	return (body)


	
def move_post(entry, body, cells):

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
	materials = entry.materials
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
	math = math_convert(Math, math)
	distance_math = math_convert(Math, distance_math)
	concealment_sense = name(Sense, concealment_sense)
	dimension_descriptor = descriptor_name(dimension_descriptor)
	ground_type = name(Ground, ground_type)
	ground_units = name(Unit, ground_units)
	objects_attack = name(ConflictAction, objects_attack)

	directions_select = [{'type': '', 'name': 'Direction'}, {'type': 'vert', 'name': 'Vertical'}, {'type': 'horiz', 'name': 'Horizontal'}, {'type': 'all', 'name': 'All Directions'}]
	direction = selects(direction, directions_select)

	aquatic_select = [{'type': '', 'name': 'Aquatic Type'}, {'type': 'surface', 'name': 'Surface'}, {'type': 'underwater', 'name': 'Underwater'}]
	acquatic_type = selects(acquatic_type, aquatic_select)

	openings_select = [{'type': '', 'name': 'Move through'}, {'type': 'opening', 'name': 'Less than water tight'}, {'type': 'water', 'name': 'Less than air tight'}, {'type': 'solid', 'name': 'Through Solid'}, {'type': 'any', 'name': 'Throughh anything'}]
	permeate_type = selects(permeate_type, openings_select)

	travel_select = [{'type': '', 'name': 'Travel Type'}, {'type': 'dimension', 'name': 'Dimension Travel'}, {'type': 'space', 'name': 'Space Travel'}, {'type': 'time', 'name': 'Time Travel'}, {'type': 'teleport', 'name': 'Teleport'}]

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
	
	
	cells = cell('Extra', 15, [extra])
	per = check_convert('Per Rank', per_rank)
	cells = cell('Speed', 18, [rank, math, mod, per], cells)
	cells = cell('Condition', 12, [condition], cells)
	cells = cell('Direction', 13, [direction], cells)
	
	vcells = vcell('unlimited', 12, ['Unlimited'])
	vcells = vcell('value', 12, [distance_value], vcells)
	vcells = vcell('math', 20, [distance_math_value, distance_math, distance_math_value2], vcells)
	vcells = vcell('mod', 20, ['Effect Rank', '-', distance_mod], vcells)
	cells = vcell_add('Distance', distance_type, vcells, cells)

	cells = cell('DC', 7, dc, cells)

	print('\n\n\n\n')
	print(ground_time)
	print('\n\n\n')
	

	cells = check_cell('Flight', 10, flight, cells, True)
	new_mod = mod_create('Flight', 10)
	new_mod = mod_cell('Conditions:', 10, [flight_conditions], new_mod)
	new_mod = mod_cell('Perception Check:', 15, [flight_resist], new_mod)
	new_mod = mod_cell('Requires Equipment:', 20, [flight_equip], new_mod)
	body = mod_add(flight, new_mod, body)

	cells = check_cell('Aquatic', 10, aquatic, cells, True)
	new_mod = mod_create('Aquatic', 10)
	new_mod = mod_cell('Type:', 7, [acquatic_type], new_mod)
	body = mod_add(aquatic, new_mod, body)

	cells = check_cell('Ground', 10, ground, cells, True)
	new_mod = mod_create('Through Ground', 17)
	new_mod = mod_cell('Type:', 7, [ground_type], new_mod)
	new_mod = mod_cell('Permanance:', 10, [ground_permanence], new_mod)
	new_mod = mod_cell('Lasts:', 5, [ground_time, ground_units], new_mod)
	new_mod = mod_cell('Ranged', 7, [ground_ranged], new_mod)
	body = mod_add(ground, new_mod, body)

	cells = check_cell('Affects Others', 18, others, cells)
	cells = check_cell('Continuous', 13, continuous, cells)
	
	cells = check_cell('Subtle', 8, subtle, cells, True)
	new_mod = mod_create('Subtle', 10)
	new_mod = mod_cell('Bonus Against:', 15, [subtle_trait], new_mod)
	new_mod = mod_cell('Bonus:', 8, [subtle_mod], new_mod)
	body = mod_add(subtle, new_mod, body)

	cells = check_cell('Concentration', 15, concentration, cells)
	cells = check_cell('Through Obstacles', 20, obstacles, cells)

	cells = check_cell('Move Objects', 18, objects, cells, True)
	select = [{'type': 1, 'name': 'Skill Check', 'w': 10}, {'type': 2, 'name': 'Opposed Check', 'w': 15}, {'type': 3, 'name': 'Routine Check', 'w': 15}, {'type': 4, 'name': 'Team Check', 'w': 15}, {'type': 5, 'name': 'Attack Check', 'w': 15}, {'type': 6, 'name': 'Resistance Check', 'w': 15}, {'type': 7, 'name': 'Comparison Check', 'w': 15}]
	new_mod = mod_create('Move Objects', 17, objects_check, select)
	value = 1
	new_mod = mod_cell('Skill:', 7, [objects_skill], new_mod, value)
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 2
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 3
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 4
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 5
	new_mod = mod_cell('Check Type:', 12, [objects_attack], new_mod, value)
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 6
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	value = 7
	new_mod = mod_cell('Direction:', 12, [objects_direction], new_mod, value)
	new_mod = mod_cell('Damage Dealt By:', 20, [damage_type], new_mod, value)
	body = mod_add(objects, new_mod, body)

	cells = check_cell('Permeate', 10, permeate, cells, True)
	new_mod = mod_create('Permeate', 12)
	new_mod = mod_cell('Type:', 8, [permeate_type], new_mod)
	new_mod = mod_cell('Speed Modifier:', 18, [permeate_speed], new_mod)
	new_mod = mod_cell('Provides Cover:', 18, [permeate_cover], new_mod)
	body = mod_add(permeate, new_mod, body)

	cells = check_cell('Special', 12, special, cells, True)
	travel_select = [{'type': 'dimension', 'name': 'Dimension Travel', 'w': 20}, {'type': 'space', 'name': 'Space Travel', 'w': 18}, {'type': 'time', 'name': 'Time Travel', 'w': 15}, {'type': 'teleport', 'name': 'Teleport', 'w': 10}]
	new_mod = mod_create('Special Travel', 19, special_type, travel_select)
	value = 'dimension'
	new_mod = mod_cell('Type:', 8, [dimension_type], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [dimension_mass_rank], new_mod, value)
	new_mod = mod_cell('Descriptor:', 13, [dimension_descriptor], new_mod, value)
	value = 'space'
	new_mod = mod_cell('Type:', 8, [special_space], new_mod, value)
	value = 'time'
	new_mod = mod_cell('Type:', 8, [special_time], new_mod, value)
	new_mod = mod_cell('Carry Mass:', 12, [special_time_carry], new_mod, value)
	value = 'teleport'
	new_mod = mod_cell('Type:', 8, [teleport_type], new_mod, value)
	new_mod = mod_cell('Can Change:', 12, [teleport_change], new_mod, value)
	new_mod = mod_cell('Portal:', 9, [teleport_portal], new_mod, value)
	new_mod = mod_cell('Turnabout:', 9, [teleport_obstacles], new_mod, value)
	body = mod_add(special, new_mod, body)

	cells = check_cell('While Prone', 18, prone, cells)

	cells = check_cell('Check', 8, check_type, cells, True)
	new_mod = mod_create('Check Type', 18)
	new_mod = mod_cell('Trait:', 10, [check_trait], new_mod)
	new_mod = mod_cell('Free Check:', 12, [check_free], new_mod)
	body = mod_add(check_type, new_mod, body)

	cells = check_cell('Material', 12, materials, cells)

	cells = check_cell('Concealment', 14, concealment, cells, True)
	new_mod = mod_create('Concealment', 15)
	new_mod = mod_cell('Concealed From:', 18, [concealment_sense], new_mod)
	new_mod = mod_cell('Detected By:', 15, [concealment_trait], new_mod)
	body = mod_add(concealment, new_mod, body)

	cells = check_cell('Extended', 11, extended, cells, True)
	new_mod = mod_create('Extended', 10)
	word = string('Actions', [extended_actions])
	new_mod = mod_cell('For:', 5, [extended_actions, word], new_mod)
	body = mod_add(extended, new_mod, body)

	cells = check_cell('Carry Mass', 14, mass, cells, True)
	new_mod = mod_create('Increased Carry Mass', 30)
	new_mod = mod_cell('Mass Rank:', 13, [mass_value], new_mod)
	body = mod_add(mass, new_mod, body)
	
	cells = cell('Cost/Rank', 9, [cost], cells)
	cells = cell('Ranks', 7, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)



def opposed_post(entry, body, cells):	

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

	
	cells = cell('Extra', 15, [extra])

	cells = cell('Player Trait', 18, [trait], cells)
	cells = cell('Mod', 6, [mod], cells)
	cells = cell('Player Check', 18, [player_check], cells)
	cells = cell('Opponent Trait', 18, [opponent_trait], cells)
	cells = cell('Mod', 6, [opponent_mod], cells)
	cells = cell('Opponent Check', 18, [opponent_check], cells)
	
	body = send(cells, body)

	cells.clear()

	return (body)

def ranged_post(entry, body, cells):
		
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
	effect_mod_math = math_convert(Math, effect_mod_math)
	check_math = math_convert(Math, check_math)
	trait_math = math_convert(Math, trait_math)
	distance_mod_math = math_convert(Math, distance_mod_math)

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


	cells = cell('Extra', 15, [extra])

	vcells = vcell('flat_units', 30, [flat_value, flat_units])

	distance_rank = string('Rank Distance', [flat_rank])
	vcells = vcell('distance_rank', 30, [flat_rank, distance_rank], vcells)

	rank = string('Rank:', [flat_rank_rank, flat_rank_value, flat_rank_units])
	equals = string('=', [flat_rank_rank, flat_rank_value, flat_rank_units])
	vcells = vcell('flat_rank_units', 30, [rank, flat_rank_rank, equals, flat_rank_value, flat_rank_units], vcells)
	
	rank = string('Rank:', [flat_rank_distance, flat_rank_distance_rank])
	equals = string('=', [flat_rank_distance, flat_rank_distance_rank])
	distance_rank = string('Rank Distance', [flat_rank_distance, flat_rank_distance_rank])
	vcells = vcell('flat_rank_distance', 35, [rank, flat_rank_distance_rank, equals, flat_rank_distance, distance_rank], vcells)
	
	start = string('Starts at', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	then = string('then', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	per = string('Per', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	rank = string('Rank', [units_rank_start_value, units_rank_value, units_rank_units, units_rank_rank])
	vcells = vcell('units_rank', 75, [start, units_rank_start_value, units_rank_units, then, units_rank_value, units_rank_units, per, units_rank_rank, rank], vcells)
	
	start = string('Starts at', [rank_distance_start, rank_distance, rank_effect_rank])
	rankdistance = string('Rank Distance', [rank_distance_start, rank_distance, rank_effect_rank])
	then = string('then', [rank_distance_start, rank_distance, rank_effect_rank])
	per = string('Per', [rank_distance_start, rank_distance, rank_effect_rank])
	rank = string('Rank', [rank_distance_start, rank_distance, rank_effect_rank])
	vcells = vcell('rank_rank', 75, [start, rank_distance_start, rankdistance, then, rank_distance, rankdistance, per, rank_effect_rank, rank], vcells)
	
	effect_rank = string('Effect Rank', [effect_mod_math, effect_mod])
	distance_rank = string('= Distance Rank', [effect_rank, effect_mod_math, effect_mod])
	vcells = vcell('effect_mod', 50, [effect_rank, effect_mod_math, effect_mod, distance_rank], vcells) 
	
	distance_rank = string('= Distance Rank', [trait_trait, trait_math, trait_mod])
	vcells = vcell('trait_mod', 45, [trait_trait, trait_math, trait_mod, distance_rank], vcells)
	
	distance_rank = string('= Distance Rank', [distance_mod_rank, distance_mod_math, distance_mod_trait])
	vcells = vcell('distance_mod', 70, [distance_mod_rank, distance_mod_math, distance_mod_trait, distance_rank], vcells)
	
	distance_rank = string('= Distance Rank', [check_trait, check_math, check_mod, distance_rank])
	vcells = vcell('check', 70, [check_trait, check_math, check_mod, distance_rank], vcells)
	cells = vcell_add('Range', range_type, vcells, cells)

	cells = check_cell('DC', 10, dc, cells, True)
	new_mod = mod_create('DC', 10)
	new_mod = mod_cell('DC Value:', 15, [dc_value], new_mod)
	new_mod = mod_cell('DC Trait:', 15, [dc_trait], new_mod)
	body = mod_add(dc, new_mod, body)

	body = send(cells, body)

	cells.clear()

	return (body)

def resist_post(entry, body, cells):

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


	mod = integer_convert(mod)
	rounds = integer_convert(rounds)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 16, [target], cells)
	cells = cell('Mod', 7, [mod], cells)
	cells = cell('Rounds', 8, [rounds], cells)

	vcells = vcell('descriptor', 18, [descriptor])
	vcells = vcell('trait', 16, [trait], vcells) 
	vcells = vcell('harmed', 18, ['Subject Harmed'], vcells)

	cells = vcell_add('Applies to', resist_check_type, vcells, cells)

	cells = check_cell('Check', 8, requires_check, cells, True)
	new_mod = mod_create('Requires Check', 17)
	new_mod = mod_cell('Check Type:', 12, [check_type], new_mod)
	new_mod = mod_cell('TraitL', 7, [check_trait], new_mod)
	body = mod_add(requires_check, new_mod, body)

	cells = cell('Circumstance', 35, [circumstance], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def resisted_by_post(entry, body, cells):

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


	dc = integer_convert(dc)
	mod = integer_convert(mod)
	degree = integer_convert(degree)
	weaken_max = integer_convert(weaken_max)
	weaken_restored = integer_convert(weaken_restored)
	damage =  integer_convert(damage)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Trait', 15, [trait], cells)
	cells = cell('DC', 7, [dc], cells)
	cells = cell('Mod', 7, [mod], cells)
	cells = cell('Degree', 9, [degree], cells)
	cells = cell('Descriptor', 22, [descriptor], cells)

	word = string('to', [condition1, condition2])
	vcells = vcell('condition', 25, [condition1, word, condition2])
	vcells = vcell('damage', 18, [damage], vcells)
	wid = width(18, 10, nullify_alternate)
	vcells = vcell('nullify', wid, [nullify_descriptor, nullify_alternate], vcells)
	wid = width(10, 15, weaken_restored)
	word =  string('Max:', [weaken_max])
	word2 = string('Restored', [weaken_max, weaken_restored])
	vcells = vcell('trait', wid, [word, weaken_max, word2, weaken_restored], vcells) 
	vcells = vcell('level', 18, [level], vcells)
	cells = vcell_add('Effect', effect, vcells, cells)
	cells = check_cell('Extra Effort', 14, extra_effort, cells)
	cells = cell('Circumstaance', 30, [description], cells)

	body = send(cells, body)

	cells.clear()

	return (body)
	
def reverse_effect_post(entry, body, cells):

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
	math = math_convert(Math, math)
	time_unit = name(Unit, time_unit)

	targets_select = [{'type': '', 'name': 'Target'}, {'type': 'active', 'name': 'Active Player'}, {'type': 'other', 'name': 'Other Character'}]
	target = selects(target, targets_select)

	whens_select = [{'type': '', 'name': 'When'}, {'type': 'before', 'name': 'Before Turn'}, {'type': 'after', 'name': 'After Turn'}]
	when = selects(when, whens_select)

	degree = integer_convert(degree)
	value_dc = integer_convert(value_dc)
	math_dc = integer_convert(math_dc)
	time_value = integer_convert(time_value)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Target', 16, [target], cells)
	cells = cell('Degree', 8, [degree], cells)
	cells = cell('When', 10, [when], cells)

	cells = check_cell('Reverse by Check', 25, check_check, cells, True)
	select =  [{'type': 'value', 'name': 'DC', 'w': 10}, {'type': 'math', 'name': 'DC', 'w': 10}]
	new_mod = mod_create('Reverse by Check', 23, value_type, select)
	value = 'value'
	new_mod = mod_cell('Value:', 13, [value_dc], new_mod, value)
	new_mod = mod_cell('Trait:', 10, [trait], new_mod, value)
	value = 'math'
	word = string('Rank', [math_dc, math])
	new_mod = mod_cell('Math:', 10, [math_dc, math, word], new_mod, value)
	new_mod = mod_cell('Trait:', 10, [trait], new_mod, value)
	body = mod_add(check_check, new_mod, body)

	cells = check_cell('Reverse by Time', 25, time_check, cells, True)
	new_mod = mod_create('Reverse by Time', 23)
	new_mod = mod_cell('Time:', 10, [time_value, time_unit], new_mod)
	body = mod_add(time_check, new_mod, body)

	body = send(cells, body)

	cells.clear()

	return (body)


def sense_post(entry, body, cells):	

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

	all_some_select = [{'type': 'always', 'name': 'Always'}, {'type': 'some', 'name': 'Sometimes'}]
	resist_permanent = selects(resist_permanent, all_some_select)

	darkness_select = [{'type': '', 'name': 'See In:'}, {'type': 'dark', 'name': 'Darkness'}, {'type': 'poor', 'name': 'Poor Light'}]
	lighting = selects(lighting, darkness_select)

	
	sense_distance_select = [{'type': '', 'name': 'Range'}, {'type': 'unlimited', 'name': 'Unlimited'}, {'type': 'flat', 'name': 'Flat'}, {'type': 'unit', 'name': 'By Rank (Units)'}, {'type': 'rank', 'name': 'By Rank'}]
	distance = selects(distance, sense_distance_select)

	dimensions_select = [{'type': '', 'name': 'Dimension Type'}, {'type': 'one', 'name': 'Specific Dimension'}, {'type': 'descriptor', 'name': 'Descriptor Dimension'}, {'type': 'any', 'name': 'Any Dimension'}]
	dimensional_type = selects(dimensional_type, dimensions_select)

	sense_cost = integer_convert(sense_cost)
	subsense_cost = integer_convert(subsense_cost)
	resist_circ = integer_convert(resist_circ)
	time_value = integer_convert(time_value)
	time_factor = integer_convert(time_factor)
	distance_dc = integer_convert(distance_dc)
	distance_mod = integer_convert(distance_mod)
	distance_value = integer_convert(distance_value)
	distance_factor = integer_convert(distance_factor)
	ranks = integer_convert(ranks)
	cost = integer_convert(cost)
	
	cells = cell('Extra', 15, [extra])
	cells = cell('Sense', 9, [sense], cells)
	cells = cell('Cost', 6, [sense_cost], cells)
	cells = cell('Subsense', 14, [subsense], cells)
	cells = cell('Cost', 6, [subsense_cost], cells)
	cells = cell('Check', 16, [skill], cells)

	wid = 14
	affects = string('Affects', [height_trait])
	word = string('Requires', [height_ensense])
	wid = width(wid, 17, height_ensense)
	vcells = vcell('height', wid, [affects, height_trait, word, height_ensense])
	wid = 14
	affects =  string('Affects', [resist_trait])
	word = check_convert('Immune', resist_immune)
	wid = width(wid, 10, resist_immune)
	perm = string(resist_permanent, word)
	wid = width(wid, 12, resist_permanent)
	circ = string('Modifier', resist_circ)
	wid = width(wid, 12, resist_circ)
	vcells = vcell('resist', wid, [affects, resist_trait, word, perm, resist_circ, circ], vcells)
	vcell_add('Effect', sense_type, vcells, cells)

	cells = check_cell('Penetrates', 12, objects, cells)
	cells = check_cell('Exclusive', 10, exclusive, cells)
	cells = check_cell('GM', 6, gm, cells)

	cells = check_cell('Counters Dark', 16, dark, cells, True)
	new_mod = mod_create('Counters Darkness', 22)
	new_mod = mod_cell('See In:', 8, lighting, new_mod)
	body = mod_add(dark, new_mod, body)

	cells = check_cell('Time Effect', 14, time, cells, True)
	sense_time_select = [{'type': 'value', 'name': 'Set by Value', 'w': 15}, {'type': 'skill', 'name': 'Set by Skill', 'w': 15}, {'type': 'bonus', 'name': 'Set by Enhanced Skill', 'w': 22}]
	new_mod = mod_create('Time Effect', 15, time_set, sense_time_select)
	value = 'value'
	new_mod = mod_cell('Time:', 8, [time_value, time_unit], new_mod, value)
	new_mod = mod_cell('X Per Rank', 12, [time_factor], new_mod, value)
	value = 'skill' 
	new_mod = mod_cell('Skill:', 8, [time_skill], new_mod, value)
	new_mod = mod_cell('X Per Rank', 12, [time_factor], new_mod, value)
	value = 'bonus'
	new_mod = mod_cell('Enhanced Skill:', 18, [time_bonus], new_mod, value)
	new_mod = mod_cell('X Per Rank', 12, [time_factor], new_mod, value)
	body = mod_add(time, new_mod, body)

	cells = check_cell('Dimensional', 14, dimensional, cells, True)
	new_mod = mod_create('Dimensional', 15)
	new_mod = mod_cell('Type', 6, [dimensional_type], new_mod)
	body = mod_add(dimensional, new_mod, body)

	cells = check_cell('Radius', 8, radius, cells)
	cells = check_cell('Accurate', 10, accurate, cells)
	cells = check_cell('Acute', 7, acute, cells)
	cells = cell('Cost/Rank', 9, [cost], cells)
	cells = cell('Ranks', 7, [ranks], cells)

	body = send(cells, body)

	cells.clear()

	return (body)


def time_post(entry, body, cells):
		
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
	math = math_convert(Math, math)
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

		
	cells = cell('Extra', 15, [extra])
	cells = cell('Type', 18, [time_type], cells)
	vcells = vcell('value', 18, [value, units])
	word = string('= Time Rank', [time_value, math, trait])
	vcells = vcell('math', 26, [time_value, math, trait, word], vcells)
	vcell_add('Time', value_type, vcells, cells)
	cells = cell('DC', 7, [dc], cells)
	cells = cell('Descriptor', 15, [descriptor], cells)
	cells = cell('Check', 18, [check_type], cells)

	cells = check_cell('Recovery', 10, recovery, cells, True)
	new_mod = mod_create('Recovery Time', 18)
	word = ('Every', [recovery_penalty, recovery_time])
	word2 = ('Time Rank', [recovery_penalty, recovery_time])
	new_mod = mod_cell('Toughness Penalty Nullified', 27, [recovery_penalty, word, recovery_time, word2])
	new_mod = mod_cell('Includes Incurable', 16, [recovery_incurable])
	body = mod_add(recovery, new_mod, body)

	body = send(cells, body)

	cells.clear()

	return (body)
