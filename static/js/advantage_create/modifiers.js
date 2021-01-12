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
					{'val': 'emotion', 'div': 'modifiers-emotion'},
					{'val': 'power', 'div': 'modifiers-power'},
					{'val': 'consequence', 'div': 'modifiers-consequence'},
					{'val': 'range', 'div': 'modifiers-range'},
					{'val': 'db', 'div': 'modifiers-profession-other'},
					{'val': 'db', 'div': 'modifiers-creature-other'},
					{'val': 'db', 'div': 'modifiers-emotion-other'},
					{'val': 'db', 'div': 'modifiers-environment-other'}]

	select_opacity(select, options);
}

function modifiers_profession() {
	const select = 'modifiers_profession';
	const options = [{'val': 'other', 'div': 'modifiers-profession-other'}]
	const div = 'modifiers-profession';

	select_other(select, options, div)
} 

function modifiers_creature() {
	const select = 'modifiers_creature';
	const options = [{'val': 'other', 'div': 'modifiers-creature-other'}]
	const div = 'modifiers-creature';

	select_other(select, options, div)
}

function modifiers_emotion() {
	const select = 'modifiers_emotion';
	const options = [{'val': 'other', 'div': 'modifiers-emotion-other'}]
	const div = 'modifiers-emotion';

	select_other(select, options, div)
}

function modifiers_environment() {
	const select = 'modifiers_environment';
	const options = [{'val': 'other', 'div': 'modifiers-environment-other'}]
	const div = 'modifiers-environment';

	select_other(select, options, div)
}

let modifiers_effect = {'status': false}

function modifiers_bonus_effect() {
	const select1 = 'modifiers_bonus_effect';
	const select2 = 'modifiers_penalty_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}, 
					{'val': 'check', 'div': 'modifiers-bonus-check'}, 
					{'val': 'conflict', 'div': 'modifiers-bonus-conflict'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row3'
	const second = [{'val': 'trait', 'row': 'modifiers-row4', 'divs': ['modifiers-bonus-defense']}];

	double_select(select1, select2, options, row, entry)
	hide_secondary_double(select1, select2, second, entry);
	
}

function modifiers_penalty_effect() {
	const select1 = 'modifiers_penalty_effect';
	const select2 = 'modifiers_bonus_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}, 
					{'val': 'check', 'div': 'modifiers-penalty-check'}, 
					{'val': 'conflict', 'div': 'modifiers-penalty-conflict'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row3';
	const second = [{'val': 'trait', 'row': 'modifiers-row4', 'divs': ['modifiers-penalty-defense'], 'select1': 'modifiers_penalty_trait_type', 'select2': 'modifiers_bonus_trait_type'}];
	
	
	double_select(select1, select2, options, row, entry);
	hide_secondary_double(select1, select2, second, entry);
}

let modifiers_trait_type = {'status': false}

function modifiers_penalty_trait_type() {
	const select1 = 'modifiers_penalty_trait_type';
	const select2 = 'modifiers_bonus_trait_type';
	const fill = 'modifiers_penalty_trait';
	const options = [{'val': 'defense', 'div': 'modifiers-penalty-defense'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';
	
	double_select(select1, select2, options, row, entry);
	trait_select(select1, fill);
}

function modifiers_bonus_trait_type() {
	const select1 = 'modifiers_bonus_trait_type';
	const select2 = 'modifiers_penalty_trait_type';
	const fill = 'modifiers_bonus_trait';
	const options = [{'val': 'defense', 'div': 'modifiers-bonus-defense'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';

	
	double_select(select1, select2, options, row, entry)
	trait_select(select1, fill);
}

function modifiers_penalty_conflict() {
	const select1 = 'modifiers_penalty_conflict';
	const select2 = 'modifiers_bonus_conflict';
	const options = [{'val': '5', 'div': 'modifier-penalty-conflict-defend'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';

	
	double_select(select1, select2, options, row, entry)
}

function modifiers_bonus_conflict() {
	const select1 = 'modifiers_bonus_conflict';
	const select2 = 'modifiers_penalty_conflict';
	const options = [{'val': '5', 'div': 'modifier-bonus-conflict-defend'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';

	
	double_select(select1, select2, options, row, entry)
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