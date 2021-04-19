
from models import *
from db.rule_models import *
from db.measure_models import *
from db.user_rules import *

from db.advanrtage_modeks import *
from db.armor_models import *
from db.descriptor_models import*
from db.equipment_models import *
from db.headquarters_models import *
from db.power_models import *
from db.skill_models import *
from db.vehicle_models import *
from db.weapon_models import *

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from copy import deepcopy



def one(name, value):

	data = {'name': name, 'value': value}

	return (data)

def field(name, value, fields=['empty']):


	field = {'name': name, 'value': value}

	if fields == ['empty']:
		new_data = []
		new_data.append(field)
		fields = new_data
	else:
		fields.append(field)

	return (fields)

def int_word(word, value):

	try:
		value = int(value)
		word = word
	except:
		word = ''

	return (word)


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


def string_all(word, data):
	full = True

	output = ''

	print('\n\n\n\n')
	for d in data:
		print(d)
		if d == '':
			full = False

	if full:
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


def send_multiple(title, cells, body, table_rows='e'):
	
	body['cells'] = deepcopy(cells)
	tables = body['rows']
	add_table = body['add_title']
	entry_id = body['id']
	mods = body['mods']
	font = body['font']
	new_table = []

	if table_rows == 'e':
		table_rows = new_table

	widths = []
	for cell in cells:
		width = cell['width']
		widths.append(width)

	new_row = {'id': entry_id, 'cells': widths}
	if add_table:
		table = {}
		rows = []
		rows.append(new_row)
		table['id'] = title
		grid_update = grid_columns(rows, font)
		table['rows'] = grid_update['rows']
		tables.append(table)
	else:
		for i in range(0, len(tables), 1):
			table = tables[i]
			rows = table['rows']
			if table['id'] == title:
				rows.append(new_row)
				grid_update = grid_columns(rows, font)
				tables[i]['rows'] = grid_update['rows']
			else:
				print('no match')

	grid_update = grid_columns(rows, font)

	grid = grid_update['grid']
	font = grid_update['font']
	columns = grid_update['columns']
	saverows = grid_update['rows']

	body['rows'] = tables
	print('\n')

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

def drop_vcell(title, names, w, field, vcells, cells, body):

	circs = body['circ']
	
	content = ''
	width = 0
	
	circ_check = False

	for vcell in vcells:
		value = vcell['value']
		con = vcell['content']
		if value == field:
			content = con
			width = w
			circ_check = True

	cell = {'title': title,
			'width': width,
			'content': '',
			'circ': circ_check
			}

	name = ''
	for n in names:
		if name == '':
			name = n
		else:
			name += ' ' + n

	if circ_check:
		circ = {'title': name,
				'content': content}
		circs.append(circ)

	body['circ'] = circs

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
		content = ''
		for c in contentlist:
			if content == '':
				content += c
			else:
				content += ' ' + c
		return (content)

def arrow_cell(contentlist, final=''):
	empty = True

	for c in contentlists:
		if c != '':
			empty = False

	if empty:
		return (final)

	content = ''
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


def circ_cell(title, name, width, circumstance, cells, body, circ_check=True):

	circs = body['circ']

	if circumstance ==  '':
		width = 0
		circ_check = False
	
	cell = {'title': title,
			'width': width,
			'content': '',
			'circ': circ_check
			}

	if circ_check:
		circ = {'title': name,
				'content': circumstance}
		circs.append(circ)

	body['circ'] = circs

	cells.append(cell)

	return (cells)

def drop_cell(title, name, width, values, cells, body, circ_check=True):

	circs = body['circ']

	if circumstance ==  '':
		width = 0
		circ_check = False
	
	cell = {'title': title,
			'width': width,
			'content': '',
			'circ': circ_check
			}

	content = ''
	for v in values:
		if content == '':
			content = v
		else:
			content += ' ' + v


	if circ_check:
		circ = {'title': name,
				'content': content}
		circs.append(circ)

	body['circ'] = circs

	cells.append(cell)

	return (cells)



def if_cell(name, width, values, cells):
	cell = {}
	cell['title'] = title
	cell['width'] = 0
	cell['content'] = ''
	cell['circ'] = False

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
	cell['circ'] = False
		
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

def checks_strings(word, value, words=''):

	if value == True:
		value = word
	else:
		value = ''

	if words == '':
		words = value
	else:
		words += ', ' + value

	return (value)

def substitute(value, field, sub):
	
	if value == field:
		value = sub

	return (value)