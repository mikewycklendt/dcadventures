from models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, SkillAlt, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus, SkillOther, SkillOtherCheck, SkillOpposed, SkillRound, SkillPower, SkillDC, SkillLevels, SkillOppCondition, SkillResistCheck, SkillResistEffect, SkillCircMod, SkillDegreeKey, SkillDegreeMod, SkillCharCheck, SkillLevelsType, SkillDegreeType
from models import Environment, Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
from models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()



def name(Table, value, name=''):
	
	db = SQLAlchemy()

	if value == 0:
		value = 'All'
		return (value)

	if value == 1234:
		value = name
		return (value)

	if value is not None:
		try:
			query = db.session.query(Table).filter_by(id=value).one()
			value = query.name
		except:
			print('no entry')
	else:
		value = ''

	
	return (value)


def action_convert(value, action_value):

	if value == 'auto':
		a = 'Automatic'
	if value == 'base':
		action = db.seession.query(Action).filter_by(id=action_value).one()
		a = action.name
	if value == 'conflict':
		action = db.seession.query(ConflictAction).filter_by(id=action_value).one()
		a = action.name

	return (a)

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
	elif value == 211:
		value = 'One Per Degree'
	elif value == 322:
		value = 'Scene'
	elif value == 433:
		value = 'Automatic'
	elif value == 544:
		value = 'Advantage Rank'
	elif value == 655:
		value = 'Same as Bonus'
	elif value == 766:
		value = 'Immune'
	elif value == 877:
		value = 'No Penalties'
	elif value == 988:
		value = 'Doubles Per Rank'
	elif value == 998:
		value = 'Flat Value'
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


def vcell(value, width, contentlist, vcells='e', value2='e', selection2='e'):

	if vcells == 'e':
		new_vcells = []
		vcells = new_vcells

	cell = {}
	cell['value'] = value

	if value2 != selection2:
		return (vcells)

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
