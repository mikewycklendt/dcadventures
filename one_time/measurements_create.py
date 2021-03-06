
@app.route('/measurements/create')
def measurements_create():

	measurements = []

	measurements.append({
		'rank': -5,
		'mass': Decimal(1.5),
		'mass_unit': 'pounds',
		'time': divide(1, 8),
		'time_unit': 'seconds',
		'distance': 6,
		'distance_unit': 'inches',
		'volume': divide(1, 32),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -4,
		'mass': 3,
		'mass_unit': 'pounds',
		'time': divide(1, 4),
		'time_unit': 'seconds',
		'distance': 1,
		'distance_unit': 'feet',
		'volume': divide(1, 16),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -3,
		'mass': 6,
		'mass_unit': 'pounds',
		'time': divide(1, 2),
		'time_unit': 'seconds',
		'distance': 3,
		'distance_unit': 'feet',
		'volume': divide(1, 8),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -2,
		'mass': 12,
		'mass_unit': 'pounds',
		'time': 1,
		'time_unit': 'seconds',
		'distance': 6,
		'distance_unit': 'feet',
		'volume': divide(1, 4),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -1,
		'mass': 25,
		'mass_unit': 'pounds',
		'time': 3,
		'time_unit': 'seconds',
		'distance': 15,
		'distance_unit': 'feet',
		'volume': divide(1, 2),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 0,
		'mass': 50,
		'mass_unit': 'pounds',
		'time': 6,
		'time_unit': 'seconds',
		'distance': 30,
		'distance_unit': 'feet',
		'volume': 1,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 1,
		'mass': 100,
		'mass_unit': 'pounds',
		'time': 12,
		'time_unit': 'seconds',
		'distance': 60,
		'distance_unit': 'feet',
		'volume': 2,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 2,
		'mass': 200,
		'mass_unit': 'pounds',
		'time': 30,
		'time_unit': 'seconds',
		'distance': 120,
		'distance_unit': 'feet',
		'volume': 4,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 3,
		'mass': 400,
		'mass_unit': 'pounds',
		'time': 1,
		'time_unit': 'minutes',
		'distance': 250,
		'distance_unit': 'feet',
		'volume': 8,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 4,
		'mass': 800,
		'mass_unit': 'pounds',
		'time': 2,
		'time_unit': 'minutes',
		'distance': 500,
		'distance_unit': 'feet',
		'volume': 15,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 5,
		'mass': 1600,
		'mass_unit': 'pounds',
		'time': 4,
		'time_unit': 'minutes',
		'distance': 900,
		'distance_unit': 'feet',
		'volume': 30,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 6,
		'mass': 3200,
		'mass_unit': 'pounds',
		'time': 8,
		'time_unit': 'minutes',
		'distance': 1800,
		'distance_unit': 'feet',
		'volume': 60,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 7,
		'mass': 3,
		'mass_unit': 'tons',
		'time': 15,
		'time_unit': 'minutes',
		'distance': divide(1, 2),
		'distance_unit': 'miles',
		'volume': 125,
		'volume_unit': 'cubic feet'
	})
	
	measurements.append({
		'rank': 8,
		'mass': 6,
		'mass_unit': 'tons',
		'time': 30,
		'time_unit': 'minutes',
		'distance': 1,
		'distance_unit': 'miles',
		'volume': 250,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 9,
		'mass': 12,
		'mass_unit': 'tons',
		'time': 1,
		'time_unit': 'hours',
		'distance': 2,
		'distance_unit': 'miles',
		'volume': 500,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 10,
		'mass': 25,
		'mass_unit': 'tons',
		'time': 2,
		'time_unit': 'hours',
		'distance': 4,
		'distance_unit': 'miles',
		'volume': 1000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 11,
		'mass': 50,
		'mass_unit': 'tons',
		'time': 4,
		'time_unit': 'hours',
		'distance': 8,
		'distance_unit': 'miles',
		'volume': 2000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 12,
		'mass': 100,
		'mass_unit': 'tons',
		'time': 8,
		'time_unit': 'hours',
		'distance': 16,
		'distance_unit': 'miles',
		'volume': 4000,
		'volume_unit': 'cubic feet'
	})
	
	measurements.append({
		'rank': 13,
		'mass': 200,
		'mass_unit': 'tons',
		'time': 16,
		'time_unit': 'hours',
		'distance': 30,
		'distance_unit': 'miles',
		'volume': 8000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 14,
		'mass': 400,
		'mass_unit': 'tons',
		'time': 1,
		'time_unit': 'days',
		'distance': 60,
		'distance_unit': 'miles',
		'volume': 15000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 15,
		'mass': 800,
		'mass_unit': 'tons',
		'time': 2,
		'time_unit': 'days',
		'distance': 120,
		'distance_unit': 'miles',
		'volume': 32000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 16,
		'mass': 1600,
		'mass_unit': 'tons',
		'time': 4,
		'time_unit': 'days',
		'distance': 250,
		'distance_unit': 'miles',
		'volume': 65000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 17,
		'mass': Decimal(3.2),
		'mass_unit': 'kilotons',
		'time': 1,
		'time_unit': 'weeks',
		'distance': 500,
		'distance_unit': 'miles',
		'volume': 125000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 18,
		'mass': 6,
		'mass_unit': 'kilotons',
		'time': 2,
		'time_unit': 'weeks',
		'distance': 1000,
		'distance_unit': 'miles',
		'volume': 250000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 19,
		'mass': 12,
		'mass_unit': 'kilotons',
		'time': 1,
		'time_unit': 'months',
		'distance': 2000,
		'distance_unit': 'miles',
		'volume': 500000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 20,
		'mass': 25,
		'mass_unit': 'kilotons',
		'time': 2,
		'time_unit': 'months',
		'distance': 4000,
		'distance_unit': 'miles',
		'volume': 1,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 21,
		'mass': 50,
		'mass_unit': 'kilotons',
		'time': 4,
		'time_unit': 'months',
		'distance': 8000,
		'distance_unit': 'miles',
		'volume': 2,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 22,
		'mass': 100,
		'mass_unit': 'kilotons',
		'time': 8,
		'time_unit': 'months',
		'distance': 16000,
		'distance_unit': 'miles',
		'volume': 4,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 23,
		'mass': 200,
		'mass_unit': 'kilotons',
		'time': Decimal(1.5),
		'time_unit': 'years',
		'distance': 32000,
		'distance_unit': 'miles',
		'volume': 8,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 24,
		'mass': 400,
		'mass_unit': 'kilotons',
		'time': 3,
		'time_unit': 'years',
		'distance': 64000,
		'distance_unit': 'miles',
		'volume': 15,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 25,
		'mass': 800,
		'mass_unit': 'kilotons',
		'time': 6,
		'time_unit': 'years',
		'distance': 125000,
		'distance_unit': 'miles',
		'volume': 32,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 26,
		'mass': 1600,
		'mass_unit': 'kilotons',
		'time': 12,
		'time_unit': 'years',
		'distance': 250000,
		'distance_unit': 'miles',
		'volume': 65,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 27,
		'mass': 3200,
		'mass_unit': 'kilotons',
		'time': 25,
		'time_unit': 'years',
		'distance': 500000,
		'distance_unit': 'miles',
		'volume': 125,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 28,
		'mass': 6400,
		'mass_unit': 'kilotons',
		'time': 50,
		'time_unit': 'years',
		'distance': 1,
		'distance_unit': 'million miles',
		'volume': 250,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 29,
		'mass': 12500,
		'mass_unit': 'kilotons',
		'time': 100,
		'time_unit': 'years',
		'distance': 2,
		'distance_unit': 'million miles',
		'volume': 500,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 30,
		'mass': 25000,
		'mass_unit': 'kilotons',
		'time': 200,
		'time_unit': 'years',
		'distance': 4,
		'distance_unit': 'million miles',
		'volume': 1,
		'volume_unit': 'billion cubic feet'
	})

	for measurement in measurements:
		rank = measurement['rank']
		mass = measurement['mass']
		mass_unit = measurement['mass_unit']
		time = measurement['time']
		time_unit = measurement['time_unit']
		distance = measurement['distance']
		distance_unit = measurement['distance_unit']
		volume = measurement['volume']
		volume_unit = measurement['volume_unit']

		entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
		db.session.add(entry)
		db.session.commit()

	for i in range(30, 101, 1):
		rank = i + 1
		mass = mass * 2
		mass_unit = 'kilotons'
		time = multiply(time, 2)
		time_unit = 'years'
		distance = multiply(distance, 2)
		distance_unit = 'million miles'
		volume = multiply(volume, 2)
		volume_unit = 'billion cubic feet'

		entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
		db.session.add(entry)
		db.session.commit()
		
	results = Measurement.query.all()

	for result in results:
		print (result.rank)
	
	return ('measurements added')