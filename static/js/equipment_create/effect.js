function effect_check() {
	const check = "effect_check";
	const title = "effect-title";
	const base = 'effect-base';
	const entry = "effect-entry";

	entry_check(check, title, base, entry);
}

let effect_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function effect_submit() {

	const columns = effect_grid.columns;
	const created = effect_grid.titles;
	const font = effect_grid.font;

	const equip_id = document.getElementById('equip_id').value;
	const name = text('effect_name')
	const description = text('effect_description')

	const errors = 'effect-err';
	const err_line = 'effect-err-line';

	response = fetch('/equipment/effect/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'name': name,
			'description': description
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const selects = ['effect-entry']
			const id = jsonResponse.id
			selects_add(id, name, 'effect-entry');
			
			effect_grid.columns.length = 0;
			effect_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, effect_grid, route, selects);
			clear_errors(err_line, errors)

			effect_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}