function benefit_check() {
	const check = "benefit_check";
	const title = "benefit-title";
	const base = 'benefit-base';
	const entry = "benefit-entry";

	entry_check(check, title, base, entry);
}

let benefit_grid = {'titles': false,
					'columns': [],
					'font': 110,
					'mod': []}

function benefit_submit() {

	const columns = benefit_grid.columns;
	const created = benefit_grid.titles;
	const font = benefit_grid.font;

	const weapon_id = document.getElementById('weapon_id').value;
	const benefit = select('benefit_benefit')

	const errors = 'benefit-err';
	const err_line = 'benefit-err-line';

	response = fetch('/weapon/benefit/create', {
		method: 'POST',
		body: JSON.stringify({
			'weapon_id': weapon_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			benefit_grid.columns.length = 0;
			benefit_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/weapon/' + table_id + '/delete/'
			create_table(jsonResponse, _grid, route);
			clear_errors(err_line, errors)

			benefit_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}