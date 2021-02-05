function time_check_check() {
	const check = "time_check_check";
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

	id_select(select, fill, trait_select);
}

function time_value_type() {
	const select = 'time_value_type';
	const options = [{'val': 'math', 'div': 'time-math'}, 
					{'val': 'value', 'div': 'time-value'}, 
					{'val': 'rank', 'div': 'time-rank'}]

	select_opacity(select, options);
}

function time_recovery() {
	const check = 'time_recovery';
	const div = 'time-recovery';

	check_display(check, div);
}

let time_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function time_submit() {

	const columns = time_grid.columns;
	const created = time_grid.titles;
	const font = time_grid.font;

	
	const type = select("time_type")
	const value_type = select("time_value_type")
	const rank1 = select("time_rank1")
	const rank1_value = select("time_rank1_value")
	const rank_math = select("time_rank_math")
	const rank2 = select("time_rank2")
	const rank2_value = select("time_rank2_value")
	const value = text("time_value")
	const units = select("time_units")
	const trait_type = select("time_trait_type")
	const trait = select("time_trait")
	const math = select("time_math")
	const math_value = select("time_math_value")
	const recovery = check("time_recovery")
	const recovery_penalty = select("time_recovery_penalty")
	const recovery_time = select("time_recovery_time")
	const recovery_incurable = check("time_recovery_incurable")

	const skill_id = document.getElementById('skill_id').value;
	
	const errors = 'time-err';
	const err_line = 'time-err-line';

	response = fetch('/skill/time/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'type': type,
			'value_type': value_type,
			'rank1': rank1,
			'rank1_value': rank1_value,
			'rank_math': rank_math,
			'rank2': rank2,
			'rank2_value': rank2_value,
			'value': value,
			'units': units,
			'trait_type': trait_type,
			'trait': trait,
			'math': math,
			'math_value': math_value,
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
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, time_grid, route);
			clear_errors(err_line, errors)

			time_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}