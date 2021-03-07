function condition_check() {
	const check = "condition_check";
	const title = "condition-title";
	const base = 'condition-base';
	const entry = "condition-entry";

	entry_check(check, title, base, entry);
}

function condition_type() {
	const select = 'condition_type';
	const options = [{'val': 'active', 'div': 'condition-active'},
					{'val': 'change', 'div': 'condition-change'},
					{'val': 'damage', 'div': 'condition-damage'},
					{'val': 'null', 'div': 'condition-null'}]

	select_opacity(select, options);
}

let condition_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function condition_submit() {

	const columns = condition_grid.columns;
	const created = condition_grid.titles;
	const font = condition_grid.font;

	const benefit = select("condition_benefit");
	const condition_type = select("condition_type");
	const condition = select("condition_condition");
	const condition_null = select("condition_null");
	const condition1 = select("condition_condition1");
	const condition2 = select("condition_condition2");
	const damage_value = select("condition_damage_value");
	const damage = select("condition_damage");

	///const advantage_id = document.getElementById('advantage_id').value;
	const advantage_id = select("create_advantage_select");

	const errors = 'condition-err';
	const err_line = 'condition-err-line';

	response = fetch('/advantage/condition/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'condition_type': condition_type,
			'condition': condition,
			'condition_null': condition_null,
			'condition1': condition1,
			'condition2': condition2,
			'damage_value': damage_value,
			'damage': damage
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			condition_grid.columns.length = 0;
			condition_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, condition_grid, route);
			clear_errors(err_line, errors)

			condition_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}