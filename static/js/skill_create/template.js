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

function _submit() {

	const columns = _grid.columns;
	const created = _grid.titles;
	const font = _grid.font;

	const skill_id = document.getElementById('skill_id').value;

	const errors = '-err';
	const err_line = '-err-line';

	response = fetch('/skill//create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
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
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, _grid, route);
			clear_errors(err_line, errors)

			_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}