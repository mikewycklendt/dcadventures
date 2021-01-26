

weapon_create = function() {
	const weapon_name = document.getElementById('weapon_name').value;
	const add_weapon = document.getElementById('add-weapon');
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch('/weapon/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': weapon_name,
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
			const name_div = document.getElementById('weapon-name');
			const weapon_id = document.getElementById('weapon_id');
			name_div.innerHTML = jsonResponse.name;
			weapon_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_weapon.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

edit_form = function() {
	const equip_id = document.getElementById('weapon_id').value;
	const edit_field = document.getElementById('weapon_name_edit');
	const name = document.getElementById('weapon-name').innerHTML;
	const edit_grid = document.getElementById('weapon-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

weapon_edit = function() {
	const id = document.getElementById('weapon_id').value;
	const name = document.getElementById('weapon_name_edit').value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch('/weapon/edit_name', {
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
			const name_div = document.getElementById('weapon-name');
			const edit_grid = document.getElementById('weapon-edit-grid');
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

weapon_save = function() {

	const weapon_id = document.getElementById('weapon_id').value;

	const description = text("description");

	const errors = 'weapon-err';
	const err_line = 'weapon-err-line';

	response = fetch('/weapon/save', {
		method: 'POST',
		body: JSON.stringify({
			'weapon_id': weapon_i
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/weapon/save/success/' + equip_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

