function feature_check() {
	const check = "feature_check";
	const title = "feature-title";
	const base = 'feature-base';
	const entry = "feature-entry";

	entry_check(check, title, base, entry);
}

let feature_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function feature_submit() {

	const columns = feature_grid.columns;
	const created = feature_grid.titles;
	const font = feature_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const errors = 'feature-err';
	const err_line = 'feature-err-line';

	response = fetch('/equipment/feature/create', {
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

			feature_grid.columns.length = 0;
			feature_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, feature_grid, route);
			clear_errors(err_line, errors)

			feature_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}