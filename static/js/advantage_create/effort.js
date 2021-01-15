function effort_check() {
	const check = "effort_check";
	const title = "effort-title";
	const base = 'effort-base';
	const entry = "effort-entry";

	entry_check(check, title, base, entry);
}

function effort_effect() {
	const select = 'effort_effect';
	const options = [{'val': 'benefit', 'div': 'effort-benefit'}]
	const entry = 'effort-entry';

	select_maxheight_entry(select, options, entry);
}


function effort_condition_type() {
	const field = 'effort_condition_type';
	const options = [{'val': 'damage', 'div': 'effort-condition-damage'},
					{'val': 'condition', 'div': 'effort-conditions'}];

	select_opacity(field, options);
}

function effort_benefit_choice() {
	const select = 'effort_benefit_choice';
	const options = [{'val': 'x', 'div': 'effort-benefit-count'}]

	select_opacity(select, options);
}

let effort_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function effort_submit() {

	const columns = effort_grid.columns;
	const created = effort_grid.titles;
	const font = effort_grid.font;

	const benefit = select("effort_benefit");
	const effect = select("effort_effect");
	const condition_type = select("effort_condition_type");
	const condition_damage_value = select("effort_condition_damage_value");
	const condition_damage = select("effort_condition_damage");
	const condition1 = select("effort_condition1");
	const condition2 = select("effort_condition2");
	const benefit_choice = select("effort_benefit_choice");
	const benefit_turns = select("effort_benefit_turns");
	const benefit_count = select("effort_benefit_count");
	const benefit_effort = check("effort_benefit_effort");
	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'effort-err';
	const err_line = 'effort-err-line';

	response = fetch('/advantage/effort/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'effect': effect,
			'condition_type': condition_type,
			'condition_damage_value': condition_damage_value,
			'condition_damage': condition_damage,
			'condition1': condition1,
			'condition2': condition2,
			'benefit_choice': benefit_choice,
			'benefit_turns': benefit_turns,
			'benefit_count': benefit_count,
			'benefit_effort': benefit_effort
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			effort_grid.columns.length = 0;
			effort_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, effort_grid, route);
			clear_errors(err_line, errors)

			effort_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}