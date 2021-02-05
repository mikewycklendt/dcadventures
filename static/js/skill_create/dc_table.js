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
				{'val': 'math', 'div': 'dc-math'},
				{'val': 'mod', 'div': 'dc-mod'}]
	const entry = 'dc-entry';

	select_maxheight_entry(field, options, entry);
}

function dc_time() {
	const check = 'dc_time';
	const div = 'dc-time';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_complex() {
	const check = 'dc_complex';
	const div = 'dc-complexity';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_descriptor() {
	const check = 'dc_descriptor_check';
	const div = 'dc-descriptor';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_change_action() {
	const check = 'dc_change_action';
	const div = 'dc-action';
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
	const fill = 'dc_measure_trait';

	id_select(select, fill, trait_select);
}


function dc_damage() {
	const check = 'dc_damage';
	const div = 'dc-damage';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_damage_type() {
	const select = 'dc_damage_type';
	const options = [{'val': 'inflict', 'div': 'dc-damage-inflict'}, 
					{'val': 'reduce', 'div': 'dc-damage-reduce'}];

	select_opacity(select, options);
}

function dc_inflict_type() {
	const select = 'dc_inflict_type';
	const options = [{'val': 'flat', 'div': 'dc-damage-inflict-flat'},
					{'val': 'bonus', 'div': 'dc-damage-inflict-bonus'},
					{'val': 'math', 'div': 'dc-damage-inflict-math'}];
	
	select_opacity(select, options);
}

function dc_inflict_trait_type() {
	const select = 'dc_inflict_trait_type';
	const fill = 'dc_inflict_trait';

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

	const target = select("dc_target")
	const dc = select("dc_dc")
	const description = text("dc_description")
	const value = select("dc_value_value")
	const mod = select("dc_mod")
	const math_value = select("dc_math_vqlue")
	const math = select("dc_math_math")
	const math_trait_type = select("dc_math_trait_type")
	const math_trait = select("dc_math_trait")
	const condition = check("dc_condition")
	const keyword_check = check("dc_keyword_check")
	const levels = check("dc_levels")
	const damage = check("dc_damage")
	const cover = check("dc_cover")
	const complex = check("dc_complex")
	const measure = check("dc_measure")
	const change_action = check("dc_change_action")
	const conceal = check("dc_conceal")
	const action = select("dc_action")
	const action_when = select("dc_action_when")
	const damage_type = select("dc_damage_type")
	const inflict_type = select("dc_inflict_type")
	const inflict_flat = select("dc_inflict_flat")
	const inflict_trait_type = select("dc_inflict_trait_type")
	const inflict_trait = select("dc_inflict_trait")
	const inflict_math = select("dc_inflict_math")
	const inflict_mod = select("dc_inflict_mod")
	const inflict_bonus = select("dc_inflict_bonus")
	const damage_mod = select("dc_damage_mod")
	const damage_consequence = select("dc_damage_consequence")
	const measure_effect = select("dc_measure_effect")
	const measure_rank_value = select("dc_measure_rank_value")
	const measure_rank = select("dc_measure_rank")
	const unit_value = text("dc_unit_value")
	const unit_type = select("dc_unit_type")
	const unit = select("dc_unit")
	const measure_trait_type = select("dc_measure_trait_type")
	const measure_trait = select("dc_measure_trait")
	const measure_trait_math = select("dc_measure_trait_math")
	const measure_mod = select("dc_measure_mod")
	const level_type = select("dc_level_type")
	const level = select("dc_level")
	const condition1 = select("dc_condition1")
	const condition2 = select("dc_condition2")
	const condition_turns = select("dc_condition_turns")
	const keyword = text("dc_keyword")
	const complexity = select("dc_complexity")

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
			'dc': dc,
			'description': description,
			'value': value,
			'mod': mod,
			'math_value': math_value,
			'math': math,
			'math_trait_type': math_trait_type,
			'math_trait': math_trait,
			'condition': condition,
			'keyword_check': keyword_check,
			'levels': levels,
			'damage': damage,
			'cover': cover,
			'complex': complex,
			'measure': measure,
			'change_action': change_action,
			'conceal': conceal,
			'action': action,
			'action_when': action_when,
			'damage_type': damage_type,
			'inflict_type': inflict_type,
			'inflict_flat': inflict_flat,
			'inflict_trait_type': inflict_trait_type,
			'inflict_trait': inflict_trait,
			'inflict_math': inflict_math,
			'inflict_mod': inflict_mod,
			'inflict_bonus': inflict_bonus,
			'damage_mod': damage_mod,
			'damage_consequence': damage_consequence,
			'measure_effect': measure_effect,
			'measure_rank_value': measure_rank_value,
			'measure_rank': measure_rank,
			'unit_value': unit_value,
			'unit_type': unit_type,
			'unit': unit,
			'measure_trait_type': measure_trait_type,
			'measure_trait': measure_trait,
			'measure_trait_math': measure_trait_math,
			'measure_mod': measure_mod,
			'level_type': level_type,
			'level': level,
			'condition1': condition1,
			'condition2': condition2,
			'condition_turns': condition_turns,
			'keyword': keyword,
			'complexity': complexity
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