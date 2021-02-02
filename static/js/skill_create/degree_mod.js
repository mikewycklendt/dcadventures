function deg_mod_check() {
	const deg_mod_check = "deg_mod_check";
	const deg_mod_base_form = "deg-mod-base-form";
	const title = "deg-mod-title";
	const entry = "deg-mod-entry";

	entry_check(deg_mod_check, title, deg_mod_base_form, entry, 160);
}

function deg_mod_base() {
	const target_field = "deg_mod_target";
	const entry = "deg-mod-entry";

	base(target_field, entry);
}

function deg_mod_type() {
	const select = 'deg_mod_type';
	const options = [{'val': 'circ', 'div':'deg-mod-circ'},
					{'val': 'measure', 'div':  'deg-mod-measure'},
					{'val': 'condition', 'div': 'deg-mod-condition'},
					{'val': 'level', 'div': 'deg-mod-level'},
					{'val': 'knowledge', 'div': 'deg-mod-knowledge'},
					{'val': 'consequence', 'div': 'deg-mod-consequence'}];
	
	select_opacity(select, options);
}

function deg_mod_consequence_action_type() {
	const select = 'deg_mod_consequence_action_type';
	const fill = 'deg_mod_consequence_action';

	id_select(select, fill, action_select);
}

function deg_mod_consequence_trait_type() {
	const select = 'deg_mod_consequence_trait_type';
	const fill = 'deg_mod_consequence_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_knowledge() {
	const select = 'deg_mod_knowledge';
	const options = [{'val': 'bonus', 'div':'deg-mod-knowledge-bonus'}];
	
	select_opacity(select, options);
}

function deg_mod_circ_trait_type() {
	const select = 'deg_mod_circ_trait_type'
	const fill = 'deg_mod_circ_trait'

	id_select(select, fill, trait_select);
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

	id_select(select, fill, trait_select);
}

function deg_mod_level_type() {
	const select = 'deg_mod_level_type';
	const fill = 'deg_mod_level';

	id_select(select, fill, level_select)
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
	const benefit = select("deg_mod_benefit");
	const value = select("deg_value");
	const deg_mod_type = select("deg_mod_type");
	const consequence_action_type = select("deg_mod_consequence_action_type");
	const consequence_action = select("deg_mod_consequence_action");
	const consequence_trait_type = select("deg_mod_consequence_trait_type");
	const consequence_trait = select("deg_mod_consequence_trait");
	const consequence = select("deg_mod_consequence");
	const knowledge = select("deg_mod_knowledge");
	const knowledge_count = select("deg_mod_knowledge_count");
	const knowledge_specificity = select("deg_mod_knowledge_specificity");
	const level_type = select("deg_mod_level_type");
	const level = select("deg_mod_level");
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
	const condition_type = select("deg_mod_condition_type");
	const condition_damage_value = select("deg_mod_condition_damage_value");
	const condition_damage = select("deg_mod_condition_damage");
	const condition1 = select("deg_mod_condition1");
	const condition2 = select("deg_mod_condition2");
	const keyword = text("deg_mod_keyword");
	const nullify = select("deg_mod_nullify");
	const cumulative = check("deg_mod_cumulative");
	const linked = check("deg_mod_linked");

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'deg-mod-err';
	const err_line = 'deg-mod-err-line';

	response = fetch('/advantage/degree_mod/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'target': target,
			'benefit': benefit,
			'value': value,
			'deg_mod_type': deg_mod_type,
			'consequence_action_type': consequence_action_type,
			'consequence_action': consequence_action,
			'consequence_trait_type': consequence_trait_type,
			'consequence_trait': consequence_trait,
			'consequence': consequence,
			'knowledge': knowledge,
			'knowledge_count': knowledge_count,
			'knowledge_specificity': knowledge_specificity,
			'level_type': level_type,
			'level': level,
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
			'condition_type': condition_type,
			'condition_damage_value': condition_damage_value,
			'condition_damage': condition_damage,
			'condition1': condition1,
			'condition2': condition2,
			'keyword': keyword,
			'nullify': nullify,
			'cumulative': cumulative,
			'linked': linked
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
			const route = '/advantage/degree_mod/delete/'
			create_table(jsonResponse, deg_mod_grid, route);
			clear_errors(err_line, errors)


			deg_mod_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
