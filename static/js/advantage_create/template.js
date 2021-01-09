function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, entry);
}

let benefit_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function benefit_submit() {

	const columns = benefit_grid.columns;
	const created = benefit_grid.titles;
	const font = benefit_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;
	
	const errors = 'benefit-err';
	const err_line = 'benefit-err-line';

	response = fetch('/advantage/benefit/create', {
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

			modifiers_grid.columns.length = 0;
			modifiers_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, modifiers_grid, route);
			clear_errors(err_line, errors)

			modifiers_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}