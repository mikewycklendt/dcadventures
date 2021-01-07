function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, entry);
}

function modifiers_bonus_effect() {
	const select = 'modifiers_bonus_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-row3'}]
	const div = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}]
	const entry = 'modifiers-entry';

	select_maxheight_entry(select, options, entry);
	select_opacity(select, div)
}


function modifiers_penalty_effect() {
	const select = 'modifiers_penalty_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-row3'}]
	const div = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}]
	const entry = 'modifiers-entry';

	select_maxheight_entry(select, options, entry);
	select_opacity(select, div)
}

function modifiers_penalty_trait_type() {
	const select = 'modifiers_penalty_trait_type';
	const fill = 'modifiers_penalty_trait';

	trait_select(select, fill);
}

function modifiers_bonus_trait_type() {
	const select = 'modifiers_bonus_trait_type';
	const fill = 'modifiers_bonus_trait';

	trait_select(select, fill);
}

let modifiers_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function modifiers_submit() {

	const columns = modifiers_grid.columns;
	const created = modifiers_grid.titles;
	const font = modifiers_grid.font;

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'modifiers-err';
	const err_line = 'modifiers-err-line';

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