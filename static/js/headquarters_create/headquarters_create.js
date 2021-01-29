function head_create() {
	const create_name = 'head_name'
	const create_add = 'add-head'
	const create_route = '/headquarters/create'
	const create_name_div = 'head-name'
	const hidden_id = 'head_id'

	create_id(create_name, create_add, create_route, create_name_div, hidden_id);
}

function edit_form() {
	const item_name_edit = 'head_name_edit'
	const name_div =  'head-name'
	const item_edit_grid = 'head-edit-grid'

	item_edit_form(item_name_edit, name_div, item_edit_grid);
}

function head_edit() {
	const item_id = 'head_id'
	const item_name_edit = 'head_name_edit'
	const edit_route = '/headquarters/edit_name'
	const item_name_div = 'head-name'
	const item_edit_grid = 'head-edit-grid'
	
	item_edit(item_id, item_name_edit, edit_route, item_name_div, item_edit_grid)
}


head_save = function() {

	const head_id = document.getElementById('head_id').value;

	
	const errors = 'head-err';
	const err_line = 'head-err-line';

	response = fetch('/headquarters/save', {
		method: 'POST',
		body: JSON.stringify({
			'head_id': head_id,
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/headquarters/save/success/' + head_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

