function check_check() {
	const check = "check_check";
	const title = "check-title";
	const base = 'check-base';
	const entry = "check-entry";

	check_title(check, title, base, entry);
}

function check_base() {
	const field = 'check_extra';
	const entry =  "check-entry";

	base(field, entry);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	id_select(select, fill, trait_select);
}

let check_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function check_submit() {

	const columns = check_grid.columns;
	const created = check_grid.titles;
	const font = check_grid.font;

	const extra_id = select("check_extra");
	const check_type = select("check_check_type");
	const mod = select("check_mod");
	const circumstance = text("check_circ");
	const when = select("check_when");
	const trait_type = select("check_trait_type");
	const trait = select("check_trait");

	const power_id = document.getElementById('power_id').value;

	const errors = 'check-err';
	const err_line = 'check-err-line';

	const route = '/power/alt_check/delete/'

	response = fetch('/power/alt_check/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'check_type': check_type,
			'mod': mod,
			'circumstance': circumstance,
			'when': when,
			'trait_type': trait_type,
			'trait': trait,
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

			check_grid.columns.length = 0;
			check_grid.columns = jsonResponse.rows;

			create_table(jsonResponse, check_grid, route);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)
		}
	})
}
