function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, base, entry);
}

let modifiers_effect = {'status': false}

function modifiers_bonus_effect() {
	const select1 = 'modifiers_bonus_effect';
	const select2 = 'modifiers_penalty_effect';
	const option1 = 'trait';
	const option2 = 'check';
	const options = ['trait', 'check']
	const divs = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}, {'val': 'check', 'div': 'modifiers-bonus-check'}];
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';
	const div_grow = '1.4vw';

	console.log(modifiers_effect.status)

	//double_select_maxheight_entry(select1, select2, option1, option2, div, select1, entry)

	double_select(select1, select2, options, modifiers_effect, div, div_grow, entry);
	select_opacity(select1, divs)
}

function modifiers_penalty_effect() {
	const select1 = 'modifiers_penalty_effect';
	const select2 = 'modifiers_bonus_effect';
	const divs = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}, {'val': 'check', 'div': 'modifiers-penalty-check'}];
	const option1 = 'trait';
	const option2 = 'check';
	const options = ['trait', 'check']
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';
	const div_grow = '1.4vw';
	
	//double_select_maxheight_entry(select1, select2, option1, option2, div, select1, entry)
	
	double_select(select1, select2, options, modifiers_effect, div, div_grow, entry);
	select_opacity(select1, divs)
}

function modifiers_penalty_trait_type() {
	const select = 'modifiers_penalty_trait_type';
	const fill = 'modifiers_penalty_trait';
	const select2 = 'modifiers_bonus_trait_type';
	const option1 = 'defense';
	const option2 = 'defense';
	const divs = [{'val': 'defense', 'div': 'modifiers-penalty-defense'}];
	const entry = 'modifiers-entry';
	const div = 'modifiers-row4';
	const div_grow = 'modifiers_penalty_effect';

	
	double_select_maxheight_entry(select, select2, option1, option2, div, div_grow, entry)
	select_opacity(select, divs)

	trait_select(select, fill);
}

function modifiers_bonus_trait_type() {
	const select = 'modifiers_bonus_trait_type';
	const select2 = 'modifiers_penalty_trait_type';
	const fill = 'modifiers_bonus_trait';
	const option1 = 'defense';
	const option2 = 'defense';
	const divs = [{'val': 'defense', 'div': 'modifiers-bonus-defense'}];
	const entry = 'modifiers-entry';
	const div = 'modifiers-row4';
	const div_grow = 'modifiers_penalty_effect';

	
	double_select_maxheight_entry(select, select2, option1, option2, div, div_grow, entry)
	select_opacity(select, divs)

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