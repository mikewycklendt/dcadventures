function time_check() {
	const check = "time_check";
	const title = "time-title";
	const base = 'time-base';
	const entry = "time-entry";

	entry_check(check, title, base, entry);
}

function time_base() {
	const field = 'time_extra';
	const entry = "time-entry";

	base(field, entry);
}

function time_trait_type() {
	const select = 'time_trait_type'
	const fill = 'time_trait'

	trait_select(select, fill)
}

function time_value_type() {
	const select = 'time_value_type';
	const math = 'time-math';
	const value = 'time-value';

	value_type(select, math, value)
}

function time_recovery() {
	const check = 'time_recovery';
	const div = 'time-recovery';
	const entry = 'time-entry';

	check_drop(check, div, entry);
}

let time_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function time_submit() {

	const columns = time_grid.columns;
	const created = time_grid.titles;
	const font = time_grid.font;

	const benefit = select("time_benefit");
	const time_type = select("time_type");
	const value_type = select("time_value_type");
	const value = text("time_value");
	const units = select("time_units");
	const time_value = select("time_math_value");
	const math = select("time_math");
	const trait_type = select("time_trait_type");
	const trait = select("time_trait");
	const dc = select("time_dc");
	const check_type = select("time_check_type");
	const recovery = check("time_recovery");
	const recovery_penalty = select("time_recovery_penalty");
	const recovery_time = select("time_recovery_time");
	const recovery_incurable = check("time_recovery_incurable");
	const advantage_id = document.getElementById('advantage_id').value;
	
	const errors = 'time-err';
	const err_line = 'time-err-line';

	response = fetch('/advantage/time/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'time_type': time_type,
			'value_type': value_type,
			'value': value,
			'units': units,
			'time_value': time_value,
			'math': math,
			'trait_type': trait_type,
			'trait': trait,
			'dc': dc,
			'check_type': check_type,
			'recovery': recovery,
			'recovery_penalty': recovery_penalty,
			'recovery_time': recovery_time,
			'recovery_incurable': recovery_incurable
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			time_grid.columns.length = 0;
			time_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, time_grid, route);
			clear_errors(err_line, errors)

			time_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}