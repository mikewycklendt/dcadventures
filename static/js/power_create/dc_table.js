function dc_check() {
	const check = "dc_check";
	const title = "dc-title";
	const base = 'dc-base';
	const entry = "dc-entry";

	check_title(check, title, base, entry);
}

function dc_base() {
	const field = 'dc_extra';
	const field2 = 'dc_target';
	const entry = "dc-entry";

	base_two(field, field2, entry);
}

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';

	trait_select(select, fill);
}

function dc_dc() {
	const field = 'dc_dc';
	const options = [{'val': 'value', 'div': 'dc-value'},
				{'val': 'math', 'div': 'dc-math'}]
	const entry = 'dc-entry';

	select_maxheight_entry(field, options, entry);
}

function dc_time() {
	const check = 'dc_time';
	const div = 'dc-time';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_descriptor() {
	const check = 'dc_descriptor';
	const div = 'dc-descriptor';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_condition() {
	const check = 'dc_condition';
	const div = 'dc-condition';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_keyword() {
	const check = 'dc_keyword';
	const div = 'dc-keyword';
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_check_type() {
	const check = 'dc_check_type';
	const div = 'dc-check'
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_check_trait_type() {
	const select = 'dc_check_trait_type';
	const fill = 'dc_check_trait';

	trait_select(select, fill)
}

function dc_levels() {
	const check = 'dc_levels';
	const div = 'dc-levels';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

let dc_grid = {'titles': false,
					'columns': []}

function dc_submit() {

	const columns = dc_grid.columns;
	const created = dc_grid.titles;

	const target = select("dc_target");
	const extra_id = select("dc_extra");
	const dc = select("dc_dc");
	const description = text("dc_description");
	const value = select("dc_value_value");
	const math_value = select("dc_math_vqlue");
	const math = select("dc_math_math");
	const math_trait_type = select("dc_math_trait_type");
	const math_trait = select("dc_math_trait");
	const descriptor_check = check("dc_descriptor_check");
	const condition = check("dc_condition");
	const keyword_check = check("dc_keyword_check");
	const check_type = check("dc_check_type");
	const descriptor = select("dc_descriptor");
	const descriptor_possess = select("dc_descriptor_possess");
	const condition1 = select("dc_condition1");
	const condition2 = select("dc_condition2");
	const keyword = text("dc_keyword");
	const check_trait_type = select("dc_check_trait_type");
	const check_trait = select("dc_check_trait");
	const check_mod = select("dc_check_mod");
	const levels = check('dc_levels');
	const level = select('dc_level');

	const power_id = document.getElementById('power_id').value;

	const errors = 'dc-err';
	const err_line = 'dc-err-line';

	response = fetch('/power/dc_table/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'dc': dc,
			'description': description,
			'value': value,
			'math_value': math_value,
			'math': math,
			'math_trait_type': math_trait_type,
			'math_trait': math_trait,
			'descriptor_check': descriptor_check,
			'condition': condition,
			'keyword_check': keyword_check,
			'check_type': check_type,
			'descriptor': descriptor,
			'descriptor_possess': descriptor_possess,
			'condition1': condition1,
			'condition2': condition2,
			'keyword': keyword,
			'check_trait_type': check_trait_type,
			'check_trait': check_trait,
			'check_mod': check_mod,
			'levels': levels,
			'level': level,
			'columns': columns,
			'created': created
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			dc_grid.columns = jsonResponse.columns;
			dc_grid.titles = jsonResponse.created;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse);
			delete_row(jsonResponse, route, dc_grid)
			clear_errors(err_line, errors)

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}