function ranks_check() {
	const check = "ranks_check";
	const title = "ranks-title";
	const base = 'ranks-base';
	const entry = "ranks-entry";

	entry_check(check, title, base, entry);
}

function ranks_extra() {
	const field = 'ranks_extra';
	const fill = 'ranks_cost';
	const power_id = select("all_power_select");
	///const power_id = document.getElementById('power_id');

	id_select(field, fill, power_cost_select, power_id);
}

function ranks_required() {
	const select = 'ranks_required';
	const div = 'ranks-required';

	select_opacity_any(select, div);
}

let ranks_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function ranks_submit() {

	const columns = ranks_grid.columns;
	const created = ranks_grid.titles;
	const font = ranks_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	const cost = select("cost_cost");
	const ranks = select("ranks_rank");
	const extra = select("cost_extra");
	const base_cost = select("cost");
	const base_ranks = select("base_ranks");
	const base_flat = check("flat");
	const unique = check("ranks_unique");
	const effect = text("ranks_effect")
	const required = select("ranks_required");
	const required_type = select("ranks_required_type");

	const errors = 'ranks-err';
	const err_line = 'ranks-err-line';

	response = fetch('/power/cost/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'columns': columns,
			'created': created,
			'font': font,
			'cost': cost,
			'ranks': ranks,
			'base_cost': base_cost,
			'extra': extra,
			'unique': unique,
			'base_ranks': base_ranks,
			'base_flat': base_flat,
			'effect': effect,
			'required': required,
			'required_type': required_type
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

			ranks_grid.columns.length = 0;
			ranks_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, ranks_grid, route);
			clear_errors(err_line, errors)

			ranks_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}