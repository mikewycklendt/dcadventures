function resist_check() {
	const check = "resist_check";
	const title = "resist-title";
	const base = 'resist-base';
	const entry = "resist-entry";

	entry_check(check, title, entry);
}

function resist_trait_type() {
	const select = 'resist_trait_type';
	const fill = 'resist_trait';

	trait_select(select, fill);
}

let resist_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function resist_submit() {

	const columns = resist_grid.columns;
	const created = resist_grid.titles;
	const font = resist_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'resist-err';
	const err_line = 'resist-err-line';

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

			resist_grid.columns.length = 0;
			resist_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, resist_grid, route);
			clear_errors(err_line, errors)

			resist_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}