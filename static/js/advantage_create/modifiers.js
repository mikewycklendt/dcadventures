function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, base, entry);
}

function modifiers_trigger() {
	const select = 'modifiers_trigger';
	const options = [{'val': 'environment', 'div': 'modifiers-environment'}, 
					{'val': 'sense', 'div': 'modifiers-sense'},
					{'val': 'subsense', 'div': 'modifiers-subsense'},
					{'val': 'condition', 'div': 'modifiers-condition'},
					{'val': 'profession', 'div': 'modifiers-profession'},
					{'val': 'creature', 'div': 'modifiers-creature'},
					{'val': 'db', 'div': 'modifiers-profession-other'},
					{'val': 'db', 'div': 'modifiers-creature-other'}]

	select_opacity(select, options);
}

function modifiers_profession() {
	const select = 'modifiers_profession';
	const options = [{'val': 'other', 'div': 'modifiers-profession-other'}]
	const field = 'modifiers-profession';

	select_other(select, options, field)
}

function modifiers_creature() {
	const select = 'modifiers_creature';
	const options = [{'val': 'other', 'div': 'modifiers-creature-other'}]
	const field = 'modifiers-creature';

	select_other(select, options, field)
}

let modifiers_effect = {'status': false}

function modifiers_bonus_effect() {
	const select1 = 'modifiers_bonus_effect';
	const select2 = 'modifiers_penalty_effect';
	const options = ['trait', 'check', 'conflict']
	const divs = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}, 
					{'val': 'check', 'div': 'modifiers-bonus-check'}, 
					{'val': 'conflict', 'div': 'modifiers-bonus-conflict'}];
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';
	const div_grow = '1.8vw';

	double_select(select1, select2, options, modifiers_effect, div, div_grow, entry);
	select_opacity(select1, divs)
}

function modifiers_penalty_effect() {
	const select1 = 'modifiers_penalty_effect';
	const select2 = 'modifiers_bonus_effect';
	const divs = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}, 
					{'val': 'check', 'div': 'modifiers-penalty-check'}, 
					{'val': 'conflict', 'div': 'modifiers-penalty-conflict'}];
	const options = ['trait', 'check', 'conflict']
	const entry = 'modifiers-entry';
	const div = 'modifiers-row3';
	const div_grow = '1.8vw';
	
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

			const multiple_div = document.getElementById('modifiers-multiple')
			multiple_div.style.display = 'grid';
			setTimeout(function(){multiple_div.style.opacity = '100%'}, 10);

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