function skill_check() {
	const check = "skill_check";
	const title = "skill-title";
	const base = 'skill-base';
	const entry = "skill-entry";

	entry_check(check, title, entry);
}

let skill_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function skill_submit() {

	const columns = skill_grid.columns;
	const created = skill_grid.titles;
	const font = skill_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'skill-err';
	const err_line = 'skill-err-line';

	response = fetch('/advantage/skill/create', {
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

			skill_grid.columns.length = 0;
			skill_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, modifiers_grid, route);
			clear_errors(err_line, errors)

			skill_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}