function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	entry_check(check, title, base, entry);
}

function circ_extra() {
	const field = 'circ_extra';

	descriptor_base(field);
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
					{'val': 'nature', 'div': 'circ-nature'},
					{'val': 'descriptor', 'div': 'circ-descriptor'},
					{'val': 'conflict', 'div': 'circ-conflict'},
					{'val': 'success', 'div': 'circ-success'}]

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

function circ_measure_trait() {
	const filter = select('circ_measure_trait_type');
	const fill = 'circ_measure_trait';

	id_select(fill, fill, trait_filter, filter);
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

function circ_trait() {
	const filter = select('circ_trait_type');
	const fill = 'circ_trait';

	id_select(fill, fill, trait_filter, filter);
}

function circ_conflict() {
	const select = 'circ_conflict';
	const options = [{'val': '7', 'div': 'circ-conflict-grab'}]

	select_opacity(select, options);
}

function circ_success() {
	const select = 'circ_success';
	const options = [{'val': 'check', 'div': 'circ-success-check'},
					{'val': 'check_type', 'div': 'circ-success-check-type'},
					{'val': 'opposed', 'div': 'circ-success-opposed'},
					{'val': 'opposed_type', 'div': 'circ-success-opposed-type'}];

	select_opacity(select, options);
}

function circ_success_bonus() {
	const select = 'circ_success_bonus';
	const options = [{'val': 'check', 'div': 'circ-success-check-bonus'},
					{'val': 'check_type', 'div': 'circ-success-check-type-bonus'},
					{'val': 'opposed', 'div': 'circ-success-opposed-bonus'},
					{'val': 'opposed_type', 'div': 'circ-success-opposed-type-bonus'},
					{'val': 'trait', 'div': 'circ-success-trait'}];

	select_opacity(select, options);
}

function circ_success_bonus_trait_type() {
	const select = 'circ_success_bonus_trait_type';
	const fill = 'circ_success_bonus_trait';

	id_select(select, fill, trait_select);
}

function circ_success_bonus_trait() {
	const filter = select('circ_success_bonus_trait_type');
	const fill = 'circ_success_bonus_trait';

	id_select(fill, fill, trait_filter, filter);
}

let circ_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function circ_submit() {

	const columns = circ_grid.columns;
	const created = circ_grid.titles;
	const font = circ_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const extra_id = select("circ_extra");
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
	const descriptor_effect = select("circ_descriptor_effect");
	const descriptor_target = select("circ_descriptor_target");
	const descriptor = select("circ_descriptor");
	const conflict = select("circ_conflict");
	const conflict_grab = select("circ_conflict_grab");
	const rank = check("circ_rank");
	const apply = select("circ_apply");
	const success = select("circ_success");
	const success_bonus = select("circ_success_bonus");
	const success_target = select("circ_success_target");
	const success_check = select("circ_success_check");
	const success_check_type = select("circ_success_check_type");
	const success_check_bonus = select("circ_success_check_bonus");
	const success_check_type_bonus = select("circ_success_check_type_bonus");
	const success_opposed = select("circ_success_opposed");
	const success_opposed_type = select("circ_success_opposed_type");
	const success_opposed_bonus = select("circ_success_opposed_bonus");
	const success_opposed_type_bonus = select("circ_success_opposed_type_bonus");
	const success_bonus_trait = select("circ_success_bonus_trait");
	const success_bonus_trait_type = select("circ_success_bonus_trait_type");

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	const circ_selects = 'circ-sml';
	const select_title = 'circ-title-sml';
	const opp_selects = 'circ-opp-sml';

	response = fetch('/power/circ/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
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
			'check_type': check_type,
			'descriptor_effect': descriptor_effect,
			'descriptor_target': descriptor_target,
			'descriptor': descriptor,
			'conflict': conflict,
			'conflict_grab': conflict_grab,
			'rank': rank,
			'apply': apply,
			'success': success,
			'success_bonus': success_bonus,
			'success_target': success_target,
			'success_check': success_check,
			'success_check_type': success_check_type,
			'success_check_bonus': success_check_bonus,
			'success_check_type_bonus': success_check_type_bonus,
			'success_opposed': success_opposed,
			'success_opposed_type': success_opposed_type,
			'success_opposed_bonus': success_opposed_bonus,
			'success_opposed_type_bonus': success_opposed_type_bonus,
			'success_bonus_trait': success_bonus_trait,
			'success_bonus_trait_type': success_bonus_trait_type
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
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, circ_grid, route, [circ_selects, opp_selects], title_id, [select_title]);
			clear_errors(err_line, errors)

			circ_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}