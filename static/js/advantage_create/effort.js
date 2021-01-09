function effort_check() {
	const check = "effort_check";
	const title = "effort-title";
	const base = 'effort-base';
	const entry = "effort-entry";

	entry_check(check, title, entry);
}

let effort_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function effort_submit() {

	const columns = effort_grid.columns;
	const created = effort_grid.titles;
	const font = effort_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'effort-err';
	const err_line = 'effort-err-line';

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

			effort_grid.columns.length = 0;
			effort_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, effort_grid, route);
			clear_errors(err_line, errors)

			effort_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}