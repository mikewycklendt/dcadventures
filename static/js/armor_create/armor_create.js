
armor_create = function() {
	const armor_name = document.getElementById('armor_name').value;
	const add_armor = document.getElementById('add-armor');
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch('/armor/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': armor_name,
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
			const name_div = document.getElementById('armor-name');
			const armor_id = document.getElementById('armor_id');
			name_div.innerHTML = jsonResponse.name;
			armor_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_armor.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

edit_form = function() {
	const armor_id = document.getElementById('armor_id').value;
	const edit_field = document.getElementById('armor_name_edit');
	const name = document.getElementById('armor-name').innerHTML;
	const edit_grid = document.getElementById('armor-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

armor_edit = function() {
	const id = document.getElementById('armor_id').value;
	const name = document.getElementById('armor_name_edit').value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch('/armor/edit_name', {
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
			const name_div = document.getElementById('armor-name');
			const edit_grid = document.getElementById('armor-edit-grid');
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

armor_save = function() {

	const armor_id = document.getElementById('armor_id').value;

	const description = text("description");
	
	const errors = 'armor-err';
	const err_line = 'armor-err-line';

	response = fetch('/armor/save', {
		method: 'POST',
		body: JSON.stringify({
			'armor_id': armor_id,
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

			window.location.replace('/armor/save/success/' + armor_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

