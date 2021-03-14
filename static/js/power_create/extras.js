
let extras_grid = {'titles': false,
				'columns': [],
				'font': 80,
				'mod': []}

function extras_submit() {

	const columns = extras_grid.columns;
	const created = extras_grid.titles;
	const font = extras_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const inherit = select("extra_inherit");
	const name = text("extra_name");
	const des = text("extra_des");
	const cost = select("extra_cost");
	const ranks = select("extra_rank");
	const alternate = check("extra_alternate");
	const flat = check("extra_flat");
	
	const errors = 'extras-err';
	const err_line = 'extras-err-line';

	const selects = 'extra-select';
	const selects_sml = 'extra-sml'
	const selects_var = 'extra-cost-select';

	response = fetch('/power/extras/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'columns': columns,
			'created': created,
			'font': font,
			'name': name,
			'cost': cost,
			'ranks': ranks,
			'des': des,
			'inherit': inherit,
			'alternate': alternate,
			'flat': flat
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const id = jsonResponse.id;

			selects_add(id, name, selects);
			selects_add(id, name, selects_sml);

			if (cost == 'x') {
				selects_add(id, name, selects_var);
			}

			extras_grid.columns.length = 0;
			extras_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, extras_grid, route, [selects, selects_sml]);
			clear_errors(err_line, errors)

			extras_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}