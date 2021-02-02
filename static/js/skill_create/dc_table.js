function dc_check() {
	const check = "dc_check";
	const title = "dc-title";
	const base = 'dc-base';
	const entry = "dc-entry";

	entry_check(check, title, base, entry);
}

function dc_base() {
	const field = 'dc_target';
	const entry = "dc-entry";

	base(field, entry);
}

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';

	id_select(select, fill, trait_select);
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
	const check = 'dc_descriptor_check';
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
	const check = 'dc_keyword_check';
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

	id_select(select, fill, trait_select)
}

function dc_levels() {
	const check = 'dc_levels';
	const div = 'dc-levels';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_level_type() {
	const select = 'dc_level_type';
	const fill = 'dc_level';

	id_select(select, fill, level_select);
}

function dc_measure() {
	const check = 'dc_measure';
	const div = 'dc-measure';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_measure_effect() {
	const select = 'dc_measure_effect';
	const options = [{'val': 'rank', 'div': 'dc-measure-rank'},
					{'val': 'unit', 'div': 'dc-measure-unit'},
					{'val': 'skill', 'div': 'dc-measure-skill'}]

	select_opacity(select, options);
}

function dc_unit_type() {
	const select = 'dc_unit_type';
	const fill = 'dc_unit';

	id_select(select, fill, unit_select);
}

function dc_measure_trait_type() {
	const select = 'dc_measure_trait_type';
	const fill = 'dc_measure_trait_type';

	id_select(select, fill, trait_select);
}
let dc_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function dc_submit() {

	const columns = dc_grid.columns;
	const created = dc_grid.titles;
	const font = dc_grid.font;

	const target = select("dc_target");
	const benefit = select("dc_benefit");
	const dc = select("dc_dc");
	const description = text("dc_description");
	const value_value = select("dc_value_value");
	const math_value = select("dc_math_vqlue");
	const math_math = select("dc_math_math");
	const math_trait_type = select("dc_math_trait_type");
	const math_trait = select("dc_math_trait");
	const condition = check("dc_condition");
	const keyword_check = check("dc_keyword_check");
	const check_type = check("dc_check_type");
	const levels = check("dc_levels");
	const level_type = select("dc_level_type");
	const level = select("dc_level");
	const condition1 = select("dc_condition1");
	const condition2 = select("dc_condition2");
	const keyword = text("dc_keyword");
	const check_trait_type = select("dc_check_trait_type");
	const check_trait = select("dc_check_trait");
	const check_mod = select("dc_check_mod");

	const skill_id = document.getElementById('skill_id').value;

	const errors = 'dc-err';
	const err_line = 'dc-err-line';

	response = fetch('/skill/dc/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'target': target,
			'benefit': benefit,
			'dc': dc,
			'description': description,
			'value_value': value_value,
			'math_value': math_value,
			'math_math': math_math,
			'math_trait_type': math_trait_type,
			'math_trait': math_trait,
			'condition': condition,
			'keyword_check': keyword_check,
			'check_type': check_type,
			'levels': levels,
			'level_type': level_type,
			'level': level,
			'condition1': condition1,
			'condition2': condition2,
			'keyword': keyword,
			'check_trait_type': check_trait_type,
			'check_trait': check_trait,
			'check_mod': check_mod
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			dc_grid.columns.length = 0;
			dc_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, dc_grid, route);
			clear_errors(err_line, errors)

			dc_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}