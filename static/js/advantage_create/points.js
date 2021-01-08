function points_check() {
	const check = "points_check";
	const title = "points-title";
	const base = 'points-base';
	const entry = "points-entry";

	entry_check(check, title, entry);
}

function points_benefit() {
	const select = 'points_benefit';
	const options = [{'val': 'ranks', 'div': 'points-ranks'}]

	select_opacity(select, options)
}

function points_ranks_trait_type() {
	const select = 'points_ranks_trait_type';
	const fill = 'points_ranks_trait';

	trait_select(select, fill);
}

let points_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function points_submit() {

	const columns = points_grid.columns;
	const created = points_grid.titles;
	const font = points_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'points-err';
	const err_line = 'points-err-line';

	response = fetch('/advantage/modifiers/create', {
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

			points_grid.columns.length = 0;
			points_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, modifiers_grid, route);
			clear_errors(err_line, errors)

			points_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}