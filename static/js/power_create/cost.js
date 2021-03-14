function cost_check() {
	const check = "cost_check";
	const title = "cost-title";
	const base = 'cost-base';
	const entry = "cost-entry";

	entry_check(check, title, base, entry);
}

let cost_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function cost_submit() {

	const columns = cost_grid.columns;
	const created = cost_grid.titles;
	const font = cost_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	const keyword = text("cost_keyword");
	const cost = select("cost_cost");
	const rank = select("cost_rank");
	const flat = check("cost_flat");

	const errors = 'cost-err';
	const err_line = 'cost-err-line';

	const selects = 'cost-entry';

	response = fetch('/power/cost/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'columns': columns,
			'created': created,
			'font': font,
			'keyword': keyword,
			'cost': cost,
			'rank': rank,
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

			selects_add(id, keyword, selects);

			cost_grid.columns.length = 0;
			cost_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, cost_grid, route, [selects]);
			clear_errors(err_line, errors)

			cost_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}