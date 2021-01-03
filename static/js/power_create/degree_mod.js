function deg_mod_check() {
	const deg_mod_check = "deg_mod_check";
	const deg_mod_base_form = "deg-mod-base-form";
	const title = "deg-mod-title";
	const entry = "deg-mod-entry";

	check_title_small(deg_mod_check, title, deg_mod_base_form, entry);
}

function deg_mod_base() {
	const target_field = "deg_mod_target";
	const extra_field = 'deg_mod_extra';
	const entry = "deg-mod-entry";

	base_two(target_field, extra_field, entry);
}

function deg_mod_type() {
	let select = 'deg_mod_type';
	const options = [{'val': 'circ', 'div':'deg-mod-circ'},
					{'val': 'measure', 'div':  'deg-mod-measure'},
					{'val': 'condition', 'div': 'deg-mod-condition'},
					{'val': 'level', 'div': 'deg-mod-level'}];
	
	select_opacity(select, options);
}

function deg_mod_circ_trait_type() {
	const select = 'deg_mod_circ_trait_type'
	const fill = 'deg_mod_circ_trait'

	trait_select(select, fill)
}

function deg_mod_condition_type() {
	const field = 'deg_mod_condition_type';
	const options = [{'val': 'damage', 'div': 'deg-mod-condition-damage'},
					{'val': 'condition', 'div': 'deg-mod-conditions'}];

	select_opacity(field, options);
}

function deg_mod_damage_type() {
	const field = 'deg_mod_damage_type';	
	const math = 'deg-mod-damage-math';
	const value = 'deg-mod-damage-value';

	value_type(field, math, value);
}

function deg_mod_measure_type() {
	const field = 'deg_mod_measure_type';
	const math = 'deg-mod-measure-math';
	const value = 'deg-mod-measure-value';
	
	value_type(field, math, value)
}

function deg_mod_measure_trait_type() {
	const select = 'deg_mod_measure_trait_type';
	const fill = 'deg_mod_measure_trait';

	trait_select(select, fill);
}

function deg_mod_level_type() {
	const select = 'deg_mod_level_type';
	const fill = 'deg_mod_level';

	level_select(select, fill)
}

let deg_mod_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function deg_mod_submit() {

	const columns = deg_mod_grid.columns;
	const created = deg_mod_grid.titles;
	const font = deg_mod_grid.font;
	
	const target = select("deg_mod_target");
	const extra_id = select("deg_mod_extra");
	const value = select("deg_value");
	const type = select("deg_mod_type");
	const circ_value = select("deg_mod_circ_value");
	const circ_turns = select("deg_mod_circ_turns");
	const circ_trait_type = select("deg_mod_circ_trait_type");
	const circ_trait = select("deg_mod_circ_trait");
	const measure_type = select("deg_mod_measure_type");
	const measure_val1 = select("deg_mod_measure_val1");
	const measure_math = select("deg_mod_measure_math");
	const measure_trait_type = select("deg_mod_measure_trait_type");
	const measure_trait = select("deg_mod_measure_trait");
	const measure_value = select("deg_mod_measure_value");
	const measure_rank = select("deg_mod_measure_rank");
	const deg_condition_type = select("deg_mod_condition_type");
	const condition_damage_value = select("deg_mod_condition_damage_value");
	const condition_damage = select("deg_mod_condition_damage");
	const condition1 = select("deg_mod_condition1");	
	const condition2 = select("deg_mod_condition2");
	const keyword = text("deg_mod_keyword");
	const nullify = select("deg_mod_nullify");
	const cumulative = check("deg_mod_cumulative");
	const linked = check("deg_mod_linked");
	const level = select('deg_mod_level');

	const power_id = document.getElementById('power_id').value;

	const errors = 'deg-mod-err';
	const err_line = 'deg-mod-err-line';

	response = fetch('/power/degree_mod/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'value': value,
			'deg_type': type,
			'circ_value': circ_value,
			'circ_turns': circ_turns,
			'circ_trait_type': circ_trait_type,
			'circ_trait': circ_trait,
			'measure_type': measure_type,
			'measure_val1': measure_val1,
			'measure_math': measure_math,
			'measure_trait_type': measure_trait_type,
			'measure_trait': measure_trait,
			'measure_value': measure_value,
			'measure_rank': measure_rank,
			'deg_condition_type': deg_condition_type,
			'condition_damage_value': condition_damage_value,
			'condition_damage': condition_damage,
			'condition1': condition1,
			'condition2': condition2,
			'keyword': keyword,
			'nullify': nullify,
			'cumulative': cumulative,
			'linked': linked,
			'level': level,
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

			deg_mod_grid.columns.length = 0;
			deg_mod_grid.columns = jsonResponse.rows

			const table_id = jsonResponse.table_id;
			const route = '/power/degree_mod/delete/'
			create_table(jsonResponse, deg_mod_grid, route);
			clear_errors(err_line, errors)


			deg_mod_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
