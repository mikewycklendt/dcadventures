function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	entry_check(check, title, base, entry);
}

function circ_effect() {
	const select = 'circ_effect';
	const options = [{'val': 'condition', 'div': 'circ-condition'},
					{'val': 'measure', 'div': 'circ-measure'},
					{'val': 'level', 'div': 'circ-level'},
					{'val': 'speed', 'div': 'circ-speed'},
					{'val': 'time', 'div': 'circ-time-mod'},
					{'val': 'temp', 'div': 'circ-temp'},
					{'val': 'target', 'div': 'circ-target'},
					{'val': 'tools', 'div': 'circ-tools'},
					{'val': 'materials', 'div': 'circ-materials'},
					{'val': 'trait', 'div': 'circ-trait'},
					{'val': 'env', 'div': 'circ-env'},
					{'val': 'nature', 'div': 'circ-nature'}]

	select_opacity(select, options);
}

function circ_condition_type() {
	const select = 'circ_condition_type';
	const options = [{'val': 'condition', 'div': 'circ-condition-condition'},
					{'val': 'damage', 'div': 'circ-condition-damage'}]

	select_opacity(select, options);
}

function circ_measure_effect() {
	const select = 'circ_measure_effect';
	const options = [{'val': 'rank', 'div': 'circ-measure-rank'},
					{'val': 'unit', 'div': 'circ-measure-unit'},
					{'val': 'skill', 'div': 'circ-measure-skill'}]

	select_opacity(select, options);
}

function circ_unit_type() {
	const select = 'circ_unit_type';
	const fill = 'circ_unit';

	id_select(select, fill, unit_select);
}

function circ_measure_trait_type() {
	const select = 'circ_measure_trait_type';
	const fill = 'circ_measure_trait';

	id_select(select, fill, trait_select);
}

function circ_level_type() {
	const select = 'circ_level_type';
	const fill = 'circ_level';

	id_select(select, fill, level_select);
}

function circ_lasts() {
	const select = 'circ_lasts';
	const options = [{'val': 'turns', 'div': 'circ-turns'}, 
					{'val': 'time', 'div': 'circ-time'}, 
					{'val': 'rank', 'div': 'circ-time-rank'}]

	select_opacity(select, options);
}

function circ_cumulative() {
	const check = 'circ_cumulative';
	const div = 'circ-max';

	check_display(check, div);
}

function circ_trait_type() {
	const select = 'circ_trait_type';
	const fill = 'circ_trait';

	id_select(select, fill, trait_select);
}
let circ_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function circ_submit() {

	const columns = circ_grid.columns;
	const created = circ_grid.titles;
	const font = circ_grid.font;

	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");
	
	const circ_target = select("circ_target")
	const mod = select("circ_mod")
	const effect = select("circ_effect")
	const speed = select("circ_speed")
	const target = select("circ_if_target")
	const level_type = select("circ_level_type")
	const level = select("circ_level")
	const condition_type = select("circ_condition_type")
	const condition1 = select("circ_condition1")
	const condition2 = select("circ_condition2")
	const conditions = select("circ_conditions")
	const conditions_effect = select("circ_conditions_effect")
	const measure_effect = select("circ_measure_effect")
	const measure_rank_value = select("circ_measure_rank_value")
	const measure_type = select("circ_meaasure_type");
	const measure_rank = select("circ_measure_rank")
	const unit_value = text("circ_unit_value")
	const unit_type = select("circ_unit_type")
	const unit = select("circ_unit")
	const measure_trait_type = select("circ_measure_trait_type")
	const measure_trait = select("circ_measure_trait")
	const measure_trait_math = select("circ_measure_trait_math")
	const measure_mod = select("circ_measure_mod")
	const measure_math_rank = select("circ_measure_math_rank");
	const keyword = text("circ_keyword")
	const cumulative = check("circ_cumulative")
	const optional = check("circ_optional")
	const circumstance = text("circ_circumstance");
	const lasts = select("circ_lasts");
	const title = text("circ_title");
	const surface = check("circ_surface");
	const tools = select("circ_tools");
	const materials = select("circ_materials");
	const max = select("circ_max");
	const trait_type = select("circ_trait_type");
	const trait = select("circ_trait");
	const trait_target = select("circ_trait_target");
	const environment = select("circ_environment")
	const nature = select("circ_nature")
	const check_type  = select("circ_check_type");

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	const circ_selects = 'circ-sml';
	const select_title = 'circ-title-sml';
	const opp_selects = 'circ-opp-sml';

	response = fetch('/skill/circ/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'circ_target': circ_target,
			'mod': mod,
			'effect': effect,
			'speed': speed,
			'target': target,
			'level_type': level_type,
			'level': level,
			'condition_type': condition_type,
			'condition1': condition1,
			'condition2': condition2,
			'conditions': conditions,
			'conditions_effect': conditions_effect,
			'measure_effect': measure_effect,
			'measure_type': measure_type,
			'measure_rank_value': measure_rank_value,
			'measure_rank': measure_rank,
			'unit_value': unit_value,
			'unit_type': unit_type,
			'unit': unit,
			'measure_trait_type': measure_trait_type,
			'measure_trait': measure_trait,
			'measure_trait_math': measure_trait_math,
			'measure_mod': measure_mod,
			'measure_math_rank': measure_math_rank,
			'keyword': keyword,
			'cumulative': cumulative,
			'optional': optional,
			'circumstance': circumstance,
			'lasts': lasts,
			'title': title,
			'surface': surface,
			'tools': tools,
			'materials': materials,
			'max': max,
			'trait_type': trait_type,
			'trait': trait,
			'trait_target': trait_target,
			'environment': environment,
			'nature': nature,
			'check_type': check_type
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
			selects_add(id, keyword, circ_selects);

			if (target == 'opp') {
				selects_add(id, keyword, opp_selects)
			}

			circ_grid.columns.length = 0;
			circ_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table('skill', jsonResponse, circ_grid, route, [circ_selects, opp_selects], title_id, [select_title]);
			clear_errors(err_line, errors)

			circ_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}