function variable_check() {
	const check = "variable_check";
	const title = "variable-title";
	const base = 'variable-base';
	const entry = "variable-entry";

	entry_check(check, title, base, entry);
}

function variable_trait_type() {
	const select = 'variable_trait_type';
	const fill = 'variable_trait';

	trait_select(select, fill);
}

let variable_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function variable_submit() {

	const columns = variable_grid.columns;
	const created = variable_grid.titles;
	const font = variable_grid.font;

	
	const trait_type = select("variable_trait_type");
	const trait = select("variable_trait");

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'variable-err';
	const err_line = 'variable-err-line';

	response = fetch('/advantage/modifiers/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			variable_grid.columns.length = 0;
			variable_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, variable_grid, route);
			clear_errors(err_line, errors)

			variable_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}