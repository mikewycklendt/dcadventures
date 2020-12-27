from decimal import *

def decRound(value):
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def divide(value1, value2):
	value = Decimal(value1) / Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def multiply(value1, value2):
	value = Decimal(value1) * Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

def measure(measurements):

	for measurement in measurements:
		mass = measurement['mass']
		time = measurement['time']
		distance = measurement['distance']
		volume = measurement['volume']

		measurement['mass'] = Decimal(mass).quantize(Decimal('.01'))
		measurement['time'] = Decimal(time).quantize(Decimal('.01'))
		measurement['distance'] = Decimal(distance).quantize(Decimal('.01'))
		measurement['volume'] = Decimal(volume).quantize(Decimal('.01'))

	print (measurements)

	return measurements


def vcell_add(title, field, vcells, cells):
	cell = {}
	cell['title'] = title
	content = ''

	for vcell in vcells:
		vcell['value'] = value
		vcell['content'] = con
		vcell['width'] = wid
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

	for c in contentlist:
		if content == '':
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