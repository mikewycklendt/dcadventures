function vehicle_create() {
	const create_name = 'vehicle_name'
	const create_add = 'add-vehicle'
	const create_route = '/vehicle/create'
	const create_name_div = 'vehicle-name'
	const hidden_id = 'vehicle_id'

	create_id(create_name, create_add, create_route, create_name_div, hidden_id);
}

function edit_form() {
	const item_name_edit = 'vehicle_name_edit'
	const name_div =  'vehicle-name'
	const item_edit_grid = 'vehicle-edit-grid'

	item_edit_form(item_name_edit, name_div, item_edit_grid);
}

function vehicle_edit() {
	const item_id = 'vehicle_id'
	const item_name_edit = 'vehicle_name_edit'
	const edit_route = '/vehicle/edit_name'
	const item_name_div = 'vehicle-name'
	const item_edit_grid = 'vehicle-edit-grid'
	
	item_edit(item_id, item_name_edit, edit_route, item_name_div, item_edit_grid)
}


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

