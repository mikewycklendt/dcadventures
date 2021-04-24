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
	const select = 'time_trait_type';
	const fill = 'time_trait';

	id_select(select, fill, trait_select);
}

function time_trait() {
	const filter = select('time_trait_type');
	const fill = 'time_trait';

	id_select(fill, fill, trait_filter, filter);
}

function time_type() {
	const select = 'time_type';
	const options = [{'val': 'recover', 'div': 'time-recovery'},
					{'val': 'reattempt', 'div': 'time-reattempt'},
					{'val': 'action', 'div': 'time-action'},
					{'val': 'check', 'div': 'time-check'},
					{'val': 'points', 'div': 'time-points'}];
	const fields = ['time_recovery_penalty', 'time_action', 'time_check'];
	const checks =  ['time_recovery_incurable', 'time_reattempt_effort'];
	
	reset_all(fields);
	uncheck_all(checks);
	select_opacity(select, options);
}
function time_value_type() {
	const select = 'time_value_type';
	const options = [{'val': 'math', 'div': 'time-math'}, 
					{'val': 'value', 'div': 'time-value'}, 
					{'val': 'rank', 'div': 'time-rank'}, 
					{'val': 'turns', 'div': 'time-turns'}, 
					{'val': 'time', 'div': 'time-time'}, 
					{'val': 'mod', 'div': 'time-mod'}, 
					{'val': 'factor', 'div': 'time-factor'}]
	const shared = [{'val': ['math', 'value', 'rank', 'turns', 'time'], 'div': 'time-measure-type'}]

	select_opacity_shared(select, shared);
	select_opacity(select, options);
}


let time_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function time_submit() {

	const columns = time_grid.columns;
	const created = time_grid.titles;
	const font = time_grid.font;

	

	const extra_id = select("time_extra");
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
	const recovery_penalty = select("time_recovery_penalty")
	const recovery_incurable = check("time_recovery_incurable")
	const degree = select("time_degree");
	const circ = select("time_circ");
	const dc = select("time_dc");
	const turns = select("time_turns");
	const keyword = text("time_keyword");
	const title = text("time_title");
	const circ_type = select("time_circ_type");
	const degree_type = select("time_degree_type");
	const dc_type = select("time_dc_type");
	const time = select("time_time");
	const mod = select("time_mod");
	const recovery_target = select("time_recovery_target");
	const measure_type = select("time_measure_type");
	const rank = check("time_rank");
	const factor = select("time_factor");
	const reattempt_effort = check("time_reattempt_effort");
	const check_type = select("time_check");
	const action = select("time_action");
	const on_check = select("time_on_check")
	const points = select("points");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");

	const selects = 'time-sml';
	const select_entry = 'time-entry';
	const select_title = 'time-title-sml';
	const recur_entry = 'lasts-entry';
	const recur_sml = 'lasts-sml';
	const recur_title_entry = 'lasts-title-entry';
	const recur_title_sml = 'lasts-title-sml';
	
	const errors = 'time-err';
	const err_line = 'time-err-line';

	response = fetch('/power/time/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
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
			'recovery_penalty': recovery_penalty,
			'recovery_incurable': recovery_incurable,
			'degree': degree,
			'circ': circ,
			'dc': dc,
			'turns': turns,
			'keyword': keyword,
			'title': title,
			'circ_type': circ_type,
			'degree_type': degree_type,
			'dc_type': dc_type,
			'time': time,
			'mod': mod,
			'recovery_target': recovery_target,
			'measure_type': measure_type,
			'rank': rank,
			'factor': factor,
			'reattempt_effort': reattempt_effort,
			'check_type': check_type,
			'action': action,
			'on_check': on_check,
			'points': points
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
			const title_name = jsonResponse.title;
			const title_id = jsonResponse.title_id;
			const add_title = jsonResponse.add_title

			if (add_title == true) {
				selects_add(title_id, title_name, select_title);
			}

			selects_add(id, keyword, selects);
			selects_add(id, keyword, select_entry);

			if (type == 'lasts') {
				selects_add(id, keyword, recur_entry);
				selects_add(id, keyword, recur_sml)				
				selects_add_new(title_id, title_name, recur_title_entry);
				selects_add_new(title_id, title_name, recur_title_sml);
			}

			time_grid.columns.length = 0;
			time_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, time_grid, route, [selects, select_entry], title_id, [select_title]);
			clear_errors(err_line, errors)

			time_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}