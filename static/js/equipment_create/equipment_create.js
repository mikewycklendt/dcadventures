

equip_create = function() {
	const equip_name = document.getElementById('equip_name').value;
	const add_equip = document.getElementById('add-equip');
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch('/equipment/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': equip_name,
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
			const name_div = document.getElementById('equip-name');
			const equip_id = document.getElementById('equip_id');
			name_div.innerHTML = jsonResponse.name;
			equip_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_equip.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

edit_form = function() {
	const equip_id = document.getElementById('equip_id').value;
	const edit_field = document.getElementById('equip_name_edit');
	const name = document.getElementById('equip-name').innerHTML;
	const edit_grid = document.getElementById('equip-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

equip_edit = function() {
	const id = document.getElementById('equip_id').value;
	const name = document.getElementById('equip_name_edit').value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch('/equipment/edit_name', {
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
			const name_div = document.getElementById('equip-name');
			const edit_grid = document.getElementById('equip-edit-grid');
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

equip_save = function() {

	const equip_id = document.getElementById('equip_id').value;

	const description = text("description");
	const type_id = select("equip_type");
	let cost = select("cost");
	const toughness = select("toughness");
	const expertise = select("expertise");
	const alternate = check("alternate");
	const move = check("move");
	const speed_mod = select("speed_mod");
	const direction = select("direction");
	const locks = check("locks");
	const lock_type = select("lock_type");
	const mod_multiple = select("modifiers_multiple");
	const mod_multiple_count = select("modifiers_multiple_count");
	const belt_cost = document.getElementById('belt_cost').value;

	if (type == '6')  {
		cost = belt_cost;
	}

	const errors = 'equip-err';
	const err_line = 'equip-err-line';

	response = fetch('/equipment/save', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'type_id': type_id,
			'cost': cost,
			'description': description,
			'toughness': toughness,
			'expertise': expertise,
			'alternate': alternate,
			'move': move,
			'speed_mod': speed_mod,
			'direction': direction,
			'locks': locks,
			'lock_type': lock_type,
			'mod_multiple': mod_multiple,
			'mod_multiple_count': mod_multiple_count
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/equipment/save/success/' + equip_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

