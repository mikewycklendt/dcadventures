function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	entry_check(check, title, base, entry);
}

let defense_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function defense_submit() {

	const columns = defense_grid.columns;
	const created = defense_grid.titles;
	const font = defense_grid.font;

	const armor_id = document.getElementById('armor_id').value;

	const errors = 'defense-err';
	const err_line = 'defense-err-line';

	response = fetch('/armor/defense/create', {
		method: 'POST',
		body: JSON.stringify({
			'armor_id': armor_id,
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

			defense_grid.columns.length = 0;
			defense_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/armor/' + table_id + '/delete/'
			create_table(jsonResponse, defense_grid, route);
			clear_errors(err_line, errors)

			defense_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}