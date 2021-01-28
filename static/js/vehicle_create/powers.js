function powers_check() {
	const check = "powers_check";
	const title = "powers-title";
	const base = 'powers-base';
	const entry = "powers-entry";

	entry_check(check, title, base, entry);
}

let power_data = {'cost': 5,
					'ranks': 5,
					'power': 1}

let powers_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function powers_submit() {

	const columns = powers_grid.columns;
	const created = powers_grid.titles;
	const font = powers_grid.font;

	const vehicle_id = document.getElementById('vehicle_id').value;
	const cost = power_data.cost;
	const ranks = power_data.ranks;
	const power = power_data.power;
	
	const errors = 'powers-err';
	const err_line = 'powers-err-line';

	response = fetch('/vehicle/powers/create', {
		method: 'POST',
		body: JSON.stringify({
			'vehicle_id': vehicle_id,
			'columns': columns,
			'created': created,
			'font': font,
			'cost':  cost,
			'ranks':  ranks,
			'power': power
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			powers_grid.columns.length = 0;
			powers_grid.columns = jsonResponse.rows;
			
			costs.powers_cost = jsonResponse.cost;
			costs.powers_rank = jsonResponse.rank;
			calculate_cost();

			const table_id = jsonResponse.table_id;
			const route = '/vehicle/' + table_id + '/delete/'
			create_table(jsonResponse, powers_grid, route);
			clear_errors(err_line, errors)

			powers_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}