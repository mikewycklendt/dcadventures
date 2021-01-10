function rounds_check() {
	const check = "rounds_check";
	const title = "rounds-title";
	const base = 'rounds-base';
	const entry = "rounds-entry";

	entry_check(check, title, base, entry);
}

let rounds_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function rounds_submit() {

	const columns = rounds_grid.columns;
	const created = rounds_grid.titles;
	const font = rounds_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;
	
	const errors = 'rounds-err';
	const err_line = 'rounds-err-line';

	response = fetch('/advantage/rounds/create', {
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

			rounds_grid.columns.length = 0;
			rounds_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, rounds_grid, route);
			clear_errors(err_line, errors)

			rounds_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}