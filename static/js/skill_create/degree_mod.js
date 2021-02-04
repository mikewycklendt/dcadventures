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
					{'val': 'consequence', 'div': 'deg-mod-consequence'},
					{'val': 'damage', 'div': 'deg-mod-damage'},
					{'val': 'action', 'div': 'deg-mod-action'},
					{'val': 'time', 'div': 'deg-mod-time'}];
	
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
	const select = 'deg_mod_damage_type';
	const options = [{'val': 'inflict', 'div': 'deg-mod-damage-inflict'}, 
					{'val': 'reduce', 'div': 'deg-mod-damage-reduce'}, 
					{'val': 'object', 'div': 'deg-mod-damage-object'}];

	select_opacity(select, options);
}

function deg_mod_inflict_type() {
	const select = 'deg_mod_inflict_type';
	const options = [{'val': 'flat', 'div': 'deg-mod-damage-inflict-flat'},
					{'val': 'bonus', 'div': 'deg-mod-damage-inflict-bonus'},
					{'val': 'math', 'div': 'deg-mod-damage-inflict-math'}];
	
	select_opacity(select, options);
}

function deg_mod_inflict_trait_type() {
	const select = 'deg_mod_inflict_trait_type';
	const fill = 'deg_mod_inflict_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_level_type() {
	const select = 'deg_mod_level_type';
	const fill = 'deg_mod_level';

	id_select(select, fill, level_select)
}

function deg_mod_measure_effect() {
	const select = 'deg_mod_measure_effect';
	const options = [{'val': 'rank', 'div': 'deg-mod-measure-rank'},
					{'val': 'unit', 'div': 'deg-mod-measure-unit'},
					{'val': 'skill', 'div': 'deg-mod-measure-skill'}]

	select_opacity(select, options);
}

function deg_mod_unit_type() {
	const select = 'deg_mod_unit_type';
	const fill = 'deg_mod_unit';

	id_select(select, fill, unit_select);
}

function deg_mod_measure_trait_type() {
	const select = 'deg_mod_measure_trait_type';
	const fill = 'deg_mod_measure_trait';

	id_select(select, fill, trait_select);
}


let deg_mod_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function deg_mod_submit() {

	const columns = deg_mod_grid.columns;
	const created = deg_mod_grid.titles;
	const font = deg_mod_grid.font;
	
	const target = select("deg_mod_target")
	const value = select("deg_value")
	const type = select("deg_mod_type")
	const action = select("deg_mod_action")
	const time = select("deg_mod_time")
	const recovery = check("deg_mod_time_recovery")
	const damage_type = select("deg_mod_damage_type")
	const object = select("deg_mod_damage_object")
	const object_effect = select("deg_mod_damage_object_effect")
	const inflict_type = select("deg_mod_inflict_type")
	const inflict_flat = select("deg_mod_inflict_flat")
	const inflict_trait_type = select("deg_mod_inflict_trait_type")
	const inflict_trait = select("deg_mod_inflict_trait")
	const inflict_math = select("deg_mod_inflict_math")
	const inflict_mod = select("deg_mod_inflict_mod")
	const inflict_bonus = select("deg_mod_inflict_bonus")
	const damage_mod = select("deg_mod_damage_mod")
	const damage_consequence = select("deg_mod_damage_consequence")
	const consequence_action_type = select("deg_mod_consequence_action_type")
	const consequence_action = select("deg_mod_consequence_action")
	const consequence_trait_type = select("deg_mod_consequence_trait_type")
	const consequence_trait = select("deg_mod_consequence_trait")
	const consequence = select("deg_mod_consequence")
	const knowledge = select("deg_mod_knowledge")
	const knowledge_count = select("deg_mod_knowledge_count")
	const knowledge_specificity = select("deg_mod_knowledge_specificity")
	const level_type = select("deg_mod_level_type")
	const level = select("deg_mod_level")
	const level_direction = select("deg_mod_level_direction")
	const circumstance = select("deg_mod_circumstance")
	const circ_target = select("deg_mod_circ_target")
	const measure_effect = select("deg_mod_measure_effect")
	const measure_rank_value = select("deg_mod_measure_rank_value")
	const measure_rank = select("deg_mod_measure_rank")
	const unit_value = text("deg_mod_unit_value")
	const unit_type = select("deg_mod_unit_type")
	const unit = select("deg_mod_unit")
	const measure_trait_type = select("deg_mod_measure_trait_type")
	const measure_trait = select("deg_mod_measure_trait")
	const measure_trait_math = select("deg_mod_measure_trait_math")
	const measure_mod = select("deg_mod_measure_mod")
	const condition_type = select("deg_mod_condition_type")
	const condition_damage_value = select("deg_mod_condition_damage_value")
	const condition_damage = select("deg_mod_condition_damage")
	const condition1 = select("deg_mod_condition1")
	const condition2 = select("deg_mod_condition2")
	const condition_turns = select("deg_mod_condition_turns")
	const keyword = text("deg_mod_keyword")
	const nullify = select("deg_mod_nullify")
	const cumulative = check("deg_mod_cumulative")
	const linked = check("deg_mod_linked")

	const skill_id = document.getElementById('skill_id').value;

	const errors = 'deg-mod-err';
	const err_line = 'deg-mod-err-line';

	response = fetch('/skill/degree_mod/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'skill_id': skill_id,
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
			const route = '/skill/degree_mod/delete/'
			create_table(jsonResponse, deg_mod_grid, route);
			clear_errors(err_line, errors)


			deg_mod_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
