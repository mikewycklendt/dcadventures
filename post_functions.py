
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()


def descriptor_name(name):
	
	db = SQLAlchemy()

	try:
		query = db.session.query(PowerDes).filter_by(id=name).one()
		name = query.name
	except:
		print('invalid id')
	
	return (name)

def integer_convert(value):

	if value == 123123:
		value = "Permanent"
		print(value)
	elif value == 121121:
		value = "Power Rank"
		print(value)
	elif value == 567567:
		value = "Any"
		print(value)
	elif value == 222222:
		value = "Always"
		print(value)
	elif value == 333333:
		value = "One Round"
		print(value)
	elif value == 111111:
		value = "Extra Rank"
		print(value)
	elif value == 444444:
		value = "Nullified"
		print(value)
	elif value == 555555:
		value = "Normal"
		print(value)
	elif value == 666666:
		value = "Instant"
		print(value)
	elif value == 777777:
		value = "Distance rank"
		print(value)
	elif value == 888888:
		value = "Vertical Height"
		print(value)
	elif value == 999999:
		value = "No Check"
		print(value)
	elif value == 432432:
		value = "Result"
		print(value)
	elif value == 778778:
		value = "All"
		print(value)
	elif value == 112112:
		value = "Trait"
		print(value)
	elif value == 334334:
		value = "Impervious"
		print(value)
	elif value == 556556:
		value = "Check"
		print(value)
	elif value == 990990:
		value = "Turn"
		print(value)
	elif value == 211211:
		value = 'One Per Degree'
	elif value == 322322:
		value = 'Scene'
	elif value == 433433:
		value = 'Automatic'
	elif value == 544544:
		value = 'Advantage Rank'
	elif value == 655655:
		value = 'Same as Bonus'
	elif value == 766766:
		value = 'Immune'
	elif value == 877877:
		value = 'No Penalties'
	elif value == 988988:
		value = 'Doubles Per Rank'
	elif value == 998998:
		value = 'Flat Value'
	elif value == 23452345:
		value = 'This Rank'
	elif value == 34563456:
		value = 'Parent Skill'
	elif value == 45674567:
		value = 'Speed Rank'
	elif value == 56785678:
		value = 'Unlimited'
	elif value == 67896789:
		value = 'GM Decides'
	elif value == 987987:
		value = 'Failure'
	elif value == 876876:
		value = 'Success'
	elif value == 765765:
		value = 'Routine'
	elif value is None:
		value = ''
	else:
		value = str(value)

	return (value)


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

def get_name(Table, value):
	
	db = SQLAlchemy()

	if value is None:
		print (value)
		value = ''
		return (value)
	else:
		try:
			get_name = db.session.query(Table).filter_by(id=value).one()
			value = get_name.name
		except:
			print('no entry')
			value = ''

	return (value)
	
def get_circ(Table, value, name=''):
	
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
			value = query.keyword
		except:
			print('no entry')
	else:
		value = ''

	
	return (value)

def get_description(Table, value, name=''):
	
	db = SQLAlchemy()

	if value is not None:
		try:
			query = db.session.query(Table).filter_by(id=value).one()
			description = query.description
		except:
			print('no entry')
	else:
		value = ''

	return (description)


def action_convert(value, action_value):

	if value == 'auto':
		a = 'Automatic'
	elif value == 'base':
		action = db.session.query(Action).filter_by(id=action_value).one()
		a = action.name
	elif value == 'conflict':
		action = db.session.query(ConflictAction).filter_by(id=action_value).one()
		a = action.name
	else:
		a = ''

	return (a)

def math_convert(name):
	
	db = SQLAlchemy()

	if name is None:
		name =  ''
		return (name)

	try:
		query = db.session.query(Math).filter_by(id=name).one()
		name = query.symbol
	except:
		print('invalid id')
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

def string_value(word, value, field):

	output = ''

	if value == field:
		output = word
	
	return (output)
	
def string_value_else(word, word2, value, field):

	if field == '':
		output = ''
	elif value == field:
		output = word
	else:
		output = word2
	
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


def vcell(value, width, contentlist, vcells='e', value2='e', selection2='e', selection3='e', value3='e'):

	if vcells == 'e':
		new_vcells = []
		vcells = new_vcells

	cell = {}
	cell['value'] = value

	if value2 != selection2:
		return (vcells)

	if value3 != selection3:
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
			content += c
		else:
			content += ' ' + c

	if content == '':
		width = 0

	cell['content'] = content
	cell['width'] = width

	vcells.append(cell)
	return (vcells)

def one_of(value, contentlist, final=''):
	if final != '':
		return (final)

	if value == '' or value == None:
		value = ''
		return (value)
	else:
		content = '`'
		for c in contentlist:
			if content == '':
				content += c
			else:
				content += ' ' + c
		return (content)


def check_cell(title, width, check, cells, mod_check=False):

	if check == False or check == '':
		width = 0
		mod_check = False
	
	cell = {'title': title,
			'width': width,
			'content': check,
			'mod_check': mod_check
			}

	cells.append(cell)

	return (cells)


def if_cell(name, width, values, cells):
	cell = {}
	cell['title'] = title
	cell['width'] = 0
	cell['content'] = ''

	for v in value:
		if v != '' and v is not None and v != False:
			cell['content'] = v
			cell['width'] = width
			cells.append(cell)
			return (cells)

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
			if c == True:
				print('true')
			else:
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

def variable_value(option, field, value):

	if option == field:
		return (value)
	else:
		value = ''
		
	return (value)

def add_plus(value):

	try:
		value = int(value)
		if value > 0:
			value = str(value)
			value = '+' + value
		else:
			value = str(value)
		return (value)
	except:
		return (value)

def int_word(value, word):

	try:
		value = int(value)
		value = str(value)
		value = value + ' ' + word
	except:
		return (value)

	return (value)
	

def check_string(word, value):

	if value == True:
		value = word
	else:
		value = ''

	return (value)

def variable_trait(value, trait):
	
	if value == 'x':
		if trait == 'ability':
			value = 'Variable Ability'
		elif trait == 'defense':
			value = 'Variable Defense'
		elif trait == 'skill':
			value = 'Variable Skill'
		elif trait == 'bonus':
			value = 'Variable Enhanced Skill'
		elif trait == 'power':
			value = 'Variable Power'
		elif trait == 'advantage':
			value = 'Variable Advantage'
		elif trait == 'extra':
			value = 'Variable Extra'

	return (value)


def trait_select(value, trait):

	if trait == 'ability':
		try:
			query = db.session.query(Ability).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'defense':
		try:
			query = db.session.query(Defense).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'skill':
		try:
			query = db.session.query(Skill).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'bonus':
		try:
			query = db.session.query(SkillBonus).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'power':
		try:
			query = db.session.query(Power).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'advantage':
		try:
			query = db.session.query(Advantage).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'extra':
		try:
			query = db.session.query(Extra).filter_by(id=value).one()
			value = query.name
		except:
			value = 'Not Found'
	elif trait == 'interact':
		value =  'Any Interarction'
	elif trait == 'manipulate':
		value =  'Any Manipulation'
	elif trait == 'this_power':
		value =  'This Power'
	elif trait == 'this_advantage':
		value =  'This Advantage'
	elif trait == 'sense':
		value =  'Sense'
	elif trait == 'size':	
		value =  'Size Rank'
	elif trait == 'speed':	
		value =  'Speed Rank'
	elif trait == 'intim':
		value =  'Intimidation Rank'
	elif trait == 'any':
		value =  'Any Trait'
	elif trait == 'x':
		value =  'Variable'
	elif trait == 'auto':
		value =  'Automatic'
	elif trait == '':
		 value = ''
	elif trait == 'immoveable':
		value =  'Immoveable'
	elif trait == 'this_bonus':
		value =  'This Skill'
	elif trait == 'active':
		value =  'Active Opponent Rank'
	elif trait == 'choice':
		value =  'Players Chosen DC'
	
	return (value)