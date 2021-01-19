function _check() {
	const check = "_check";
	const title = "-title";
	const base = '-base';
	const entry = "-entry";

	entry_check(check, title, base, entry);
}

let _grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function benefit_submit() {

	const columns = benefit_grid.columns;
	const created = benefit_grid.titles;
	const font = benefit_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const errors = '-err';
	const err_line = '-err-line';

	response = fetch('/equipment//create', {
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

			_grid.columns.length = 0;
			_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, _grid, route);
			clear_errors(err_line, errors)

			_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}