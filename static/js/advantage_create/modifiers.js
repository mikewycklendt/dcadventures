function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, entry);
}

function modifiers_bonus_effect() {
	const select1 = 'modifiers_bonus_effect';
	const select2 = 'modifiers_penalty_effect';
	const option1 = 'trait';
	const option2 = 'check';
	const divs = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}, {'val': 'check', 'div': 'modifiers-bonus-check'}]
	const options = [{'val': 'trait', 'div':'modifiers-row3'}, {'val': 'check', 'div':'modifiers-row3'} ];
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';

	double_select_maxheight_entry(select1, select2, option1, div, entry)
	double_select_maxheight_entry(select1, select2, option2, div, entry)
	
	select_opacity(select1, divs)
}


function modifiers_penalty_effect() {
	const select1 = 'modifiers_penalty_effect';
	const select2 = 'modifiers_bonus_effect';
	const divs = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}, {'val': 'check', 'div': 'modifiers-penalty-check'}]
	const options = [{'val': 'trait', 'div':'modifiers-row3'}, {'val': 'check', 'div':'modifiers-row3'} ];
	const option1 = 'trait';
	const option2 = 'check';
	const row3 = 'modifiers-row3'; 
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';
	
	double_select_maxheight_entry(select1, select2, option1, div, entry)
	double_select_maxheight_entry(select1, select2, option2, div, entry)
	
	select_opacity(select1, divs)
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