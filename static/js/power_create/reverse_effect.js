function reverse_check() {
	const check = "reverse_check";
	const base = "reverse-base";
	const title = "reverse-title";
	const entry = "reverse-entry";

	check_title(check, title, base, entry);
}

function reverse_base() {
	const target_field = "reverse_target";
	const extra_field = 'reverse_extra';
	const entry = "reverse-entry";


	base_two(target_field, extra_field, entry);
}

function reverse_check_check() {
	const check = "reverse_check_check";
	const field = "reverse-check";
	const entry = "reverse-entry";

	check_drop(check, field, entry);
}

function reverse_time_check() {
	const check = "reverse_time_check";
	const field = "reverse-time";
	const entry = "reverse-entry";

	check_drop(check, field, entry);
}

function reverse_trait_type() {
	const select = 'reverse_trait_type';
	const fill = 'reverse_trait';

	trait_select(select, fill);
}

function reverse_value_type() {
	const type_field = "reverse_value_type";	
	const val = "reverse-check-value";
	const math = "reverse-check-math";

	value_type(type_field, math, val);
}

let reverse_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function reverse_submit() {

	const columns = reverse_grid.columns;
	const created = reverse_grid.titles;
	const font = reverse_grid.font;

	const target = select("reverse_target");
	const extra_id = select("reverse_extra");
	const degree = select("reverse_degree");
	const when = select("reverse_when");
	const check_check = check("reverse_check_check");
	const time_check = check("reverse_time_check");
	const trait_type = select("reverse_trait_type");
	const trait = select("reverse_trait");
	const value_type = select("reverse_value_type");
	const value_dc = select("reverse_value_dc");
	const math_dc = select("reverse_math_dc");
	const math = select("reverse_math");
	const time_value = text("reverse_time");
	const time_unit = select("reverse_time_unit");

	const power_id = document.getElementById('power_id').value;

	const errors = 'reverse-err';
	const err_line = 'reverse-err-line';

	response = fetch('/power/reverse_effect/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'degree': degree,
			'when': when,
			'check_check': check_check,
			'time_check': time_check,
			'trait_type': trait_type,
			'trait': trait,
			'value_type': value_type,
			'value_dc': value_dc,
			'math_dc': math_dc,
			'math': math,
			'time_value': time_value,
			'time_unit': time_unit,
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

			reverse_grid.columns = jsonResponse.columns;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, reverse_grid, route);
			clear_errors(err_line, errors)
			
			reverse_grid.titles = true;


		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}