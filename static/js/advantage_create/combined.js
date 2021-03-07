function combined_check() {
	const check = "combined_check";
	const title = "combined-title";
	const base = 'combined-base';
	const entry = "combined-entry";

	entry_check(check, title, base, entry);
}

let combined_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function combined_submit() {

	const columns = combined_grid.columns;
	const created = combined_grid.titles;
	const font = combined_grid.font;

	const ranks = select("combined_ranks");
	const advantage = select("combined_advantage");

	///const advantage_id = document.getElementById('advantage_id').value;
	const advantage_id = select("create_advantage_select");

	const errors = 'combined-err';
	const err_line = 'combined-err-line';

	response = fetch('/advantage/combined/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'ranks': ranks,
			'advantage': advantage
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			combined_grid.columns.length = 0;
			combined_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, combined_grid, route);
			clear_errors(err_line, errors)

			combined_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}