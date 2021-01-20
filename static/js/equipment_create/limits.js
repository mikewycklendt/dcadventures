function limits_check() {
	const check = "limits_check";
	const title = "limits-title";
	const base = 'limits-base';
	const entry = "limits-entry";

	entry_check(check, title, base, entry);
}

let limits_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function limits_submit() {

	const columns = limits_grid.columns;
	const created = limits_grid.titles;
	const font = limits_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const errors = 'limits-err';
	const err_line = 'limits-err-line';

	response = fetch('/equipment/limits/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
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

			limits_grid.columns.length = 0;
			limits_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, limits_grid, route);
			clear_errors(err_line, errors)

			limits_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}