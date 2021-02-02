function skill_create() {
	const create_name = 'skill_name'
	const create_add = 'add-skill'
	const create_route = '/skill/create'
	const create_name_div = 'skill-name'
	const hidden_id = 'skill_id'

	create_id(create_name, create_add, create_route, create_name_div, hidden_id);
}

function edit_form() {
	const item_name_edit = 'skill_name_edit'
	const name_div =  'skill-name'
	const item_edit_grid = 'skill-edit-grid'

	item_edit_form(item_name_edit, name_div, item_edit_grid);
}

function head_edit() {
	const item_id = 'skill_id'
	const item_name_edit = 'skill_name_edit'
	const edit_route = '/skill/edit_name'
	const item_name_div = 'skill-name'
	const item_edit_grid = 'skill-edit-grid'
	
	item_edit(item_id, item_name_edit, edit_route, item_name_div, item_edit_grid)
}


skill_save = function() {

	const skill_id = document.getElementById('skill_id').value;
	const description = text("description")

	const errors = 'skill-err';
	const err_line = 'skill-err-line';

	response = fetch('/skill/save', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'description': description
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/skill/save/success/' + skill_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

