vehicle_create = function() {
	const vehicle_name = document.getElementById('vehicle_name').value;
	const add_vehicle = document.getElementById('add-vehicle');
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch('/vehicle/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': vehicle_name,
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const all_fields = document.getElementById('all-fields');
			const name_div = document.getElementById('vehicle-name');
			const vehicle_id = document.getElementById('vehicle_id');
			name_div.innerHTML = jsonResponse.name;
			vehicle_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_vehicle.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

edit_form = function() {
	const vehicle_id = document.getElementById('vehicle_id').value;
	const edit_field = document.getElementById('vehicle_name_edit');
	const name = document.getElementById('vehicle-name').innerHTML;
	const edit_grid = document.getElementById('vehicle-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

armor_edit = function() {
	const id = document.getElementById('vehicle_id').value;
	const name = document.getElementById('vehicle_name_edit').value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch('/vehicle/edit_name', {
		method: 'POST',
		body: JSON.stringify({
			'id': id,
			'name': name
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const name_div = document.getElementById('vehicle-name');
			const edit_grid = document.getElementById('vehicle-edit-grid');
			edit_grid.style.display = "none";
			name_div.innerHTML = jsonResponse.name;
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);

			clear_errors(err_line, errors);

		} else {
				
			back_errors(err_line, errors, jsonResponse);

		}
	})
}

let costs = {'size_rsnk': 0,
			'size_cost': 0,
			'size_strength': 0,
			'size_toughness': 0,
			'size_defense': 0,
			'strength': 0,
			'strengths': 0,
			'speed': 0,
			'toughness': 0,
			'toughnesses': 0,
			'defense': 0,
			'defenses': 0,
			'features': 0,
			'powers_rank': 0,
			'powers_cost': 0,
			'cost': 0}

vehicle_save = function() {

	const vehicle_id = document.getElementById('vehicle_id').value;

	const description = text("description");
	
	const errors = 'vehicle-err';
	const err_line = 'vehicle-err-line';

	response = fetch('/vehicle/save', {
		method: 'POST',
		body: JSON.stringify({
			'vehicle_id': vehicle_id,
			'description': description,
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/vehicle/save/success/' + vehicle_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

