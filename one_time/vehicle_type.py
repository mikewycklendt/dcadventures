
@app.route('/vehicletype/create')
def vehicletype_create():

	entries = ['Ground', 'Water', 'Air', 'Space', 'Special']

	for i in entries:

		entry = VehicleType(name=i)
		db.session.add(entry)
		db.session.commit()

	results = VehicleType.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('vehicle types added')
	
@app.route('/vehicleaub/create')
def vehiclesub_create():

	entries = ['Car', 'Truck', 'Tank', 'Armored Personnel Carrier', 'Motorcycle', 'Police Cruiser', 'Limousine', 'Truck', 'Armored Car', 'Bus', 'Semi-Truck', 'Train Engine']

	for i in entries:

		entry = VehicleSub(name=i, type_id=1)
		db.session.add(entry)
		db.session.commit()
		
	entries = ['Cutter', 'Destroyer', 'Battleship', 'Submarine', 'Jet-Ski', 'Speedboat', 'Yacht', 'Cruise Ship']

	for i in entries:

		entry = VehicleSub(name=i, type_id=2)
		db.session.add(entry)
		db.session.commit()

	entries = ['Military Helicopter', 'Fighter Jet', 'Bomber', 'Helicopter', 'Private Jet', 'Jumbo-Je']

	for i in entries:

		entry = VehicleSub(name=i, type_id=3)
		db.session.add(entry)
		db.session.commit()
	
	entries = ['Space Fighter', 'Space Cruiser', 'Space Battleship']

	for i in entries:

		entry = VehicleSub(name=i, type_id=4)
		db.session.add(entry)
		db.session.commit()

	entries = []

	for i in entries:

		entry = VehicleSub(name=i, type_id=5)
		db.session.add(entry)
		db.session.commit()

	results = VehicleSub.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print ('type: ' + str(result.type_id))
	
	return ('vehicle types added')