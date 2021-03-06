function benefit_check() {
	const check = "benefit_check";
	const title = "benefit-title";
	const base = 'benefit-base';
	const entry = "benefit-entry";

	entry_check(check, title, base, entry);
}

let benefit_grid = {'titles': false,
					'columns': [],
					'font': 120,
					'mod': []}

function benefit_submit() {

	const columns = benefit_grid.columns;
	const created = benefit_grid.titles;
	const font = benefit_grid.font;
					
	const advantage_id = document.getElementById('advantage_id').value;
	
	const name = text('benefit_name')
	const description = text('benefit_description')
	const effort = check('benefit_effort')
	const ranked = check('benefit_ranked');
					
	const errors = 'benefit-err';
	const err_line = 'benefit-err-line';
					
	response = fetch('/advantage/benefit/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'name': name,
			'description': description,
			'effort': effort,
			'ranked': ranked
		}),
		headers: {
			'Content-Type': 'application/json',
		}
		})
		.then(response => response.json())
		.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
					
			const id = jsonResponse.id;
					
			selects_add(id, name, 'benefit-sml');
			selects_add(id, name, 'benefit-entry');

			const benefit_delete = true
					
			benefit_grid.columns.length = 0;
			benefit_grid.columns = jsonResponse.rows;
					
			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, benefit_grid, route, [benefit_delete]);
			clear_errors(err_line, errors)
					
			benefit_grid.titles = true;
					
		} else {
			back_errors(err_line, errors, jsonResponse)
					
		}
	})
}