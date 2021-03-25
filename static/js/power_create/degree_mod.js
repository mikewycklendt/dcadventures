function deg_mod_check() {
	const deg_mod_check = "deg_mod_check";
	const deg_mod_base_form = "deg-mod-base-form";
	const title = "deg-mod-title";
	const entry = "deg-mod-entry";

	entry_check(deg_mod_check, title, deg_mod_base_form, entry);
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
					{'val': 'time', 'div': 'deg-mod-time'},
					{'val': 'check', 'div': 'deg-mod-check'},
					{'val': 'duration', 'div': 'deg-mod-duration'},
					{'val': 'descriptor', 'div': 'deg-mod-descriptor'}];
	
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

function deg_mod_consequence_trait() {
	const filter = select('deg_mod_consequence_trait_type');
	const fill = 'deg_mod_consequence_trait';

	id_select(fill, fill, trait_filter, filter);
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
	const selects = ["deg_mod_inflict_flat", "deg_mod_inflict_trait_type", "deg_mod_inflict_trait",
					"deg_mod_inflict_math", "deg_mod_inflict_mod", "deg_mod_inflict_bonus"];

	select_opacity(select, options);
	reset_all(selects);
}

function deg_mod_inflict_trait_type() {
	const select = 'deg_mod_inflict_trait_type';
	const fill = 'deg_mod_inflict_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_inflict_trait() {
	const filter = select('deg_mod_inflict_trait_type');
	const fill = 'deg_mod_inflict_trait';

	id_select(fill, fill, trait_filter, filter);
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
					{'val': 'skill_rank', 'div': 'deg-mod-measure-skill'},
					{'val': 'skill_unit', 'div': 'deg-mod-measure-skill-unit'}]

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

function deg_mod_measure_trait() {
	const filter = select('deg_mod_measure_trait_type');
	const fill = 'deg_mod_measure_trait';

	id_select(fill, fill, trait_filter, filter);
}

function deg_mod_measure_trait_type_unit() {
	const select = 'deg_mod_measure_trait_type_unit';
	const fill = 'deg_mod_measure_trait_unit';

	id_select(select, fill, trait_select);
}

function deg_mod_measure_trait_unit() {
	const filter = select('deg_mod_measure_trait_type_unit');
	const fill = 'deg_mod_measure_trait_unit';

	id_select(fill, fill, trait_filter, filter);
}

function deg_mod_check_type() {
	const select = 'deg_mod_check_type';
	const options = [{'val': '2', 'div': 'deg-mod-check-opposed'},
					{'val': '1', 'div': 'deg-mod-check-skill'},
					{'val': '6', 'div': 'deg-mod-check-resist'},
					{'val': '3', 'div': 'deg-mod-check-routine'},
					{'val': '5', 'div': 'deg-mod-check-attack'},
					{'val': '7', 'div': 'deg-mod-check-compare'}]

	select_opacity(select, options);
}

function deg_mod_check_routine_trait_type() {
	const select = 'deg_mod_check_routine_trait_type';
	const fill = 'deg_mod_check_routine_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_check_routine_trait() {
	const filter = select('deg_mod_check_routine_trait_type');
	const fill = 'deg_mod_check_routine_trait';

	id_select(fill, fill, trait_filter, filter);
}

function deg_mod_check_skill_trait_type() {
	const select = 'deg_mod_check_skill_trait_type';
	const fill = 'deg_mod_check_skill_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_check_skill_trait() {
	const filter = select('deg_mod_check_skill_trait_type');
	const fill = 'deg_mod_check_skill_trait';

	id_select(fill, fill, trait_filter, filter);
}

function deg_mod_check_resist_trait_type() {
	const select = 'deg_mod_check_resist_trait_type';
	const fill = 'deg_mod_check_resist_trait';

	id_select(select, fill, trait_select);
}

function deg_mod_check_resist_trait() {
	const filter = select('deg_mod_check_resist_trait_type');
	const fill = 'deg_mod_check_resist_trait';

	id_select(fill, fill, trait_filter, filter);
}

let deg_mod_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function deg_mod_submit() {

	const columns = deg_mod_grid.columns;
	const created = deg_mod_grid.titles;
	const font = deg_mod_grid.font;
	
	const extra_id = select("deg_mod_extra");
	const target = select("deg_mod_target");
	const value = select("deg_value");
	const type = select("deg_mod_type");
	const action = select("deg_mod_action");
	const time = select("deg_mod_time");
	const recovery = check("deg_mod_time_recovery");
	const damage_type = select("deg_mod_damage_type");
	const object = select("deg_mod_damage_object");
	const object_effect = select("deg_mod_damage_object_effect");
	const inflict_type = select("deg_mod_inflict_type");
	const inflict_flat = select("deg_mod_inflict_flat");
	const inflict_trait_type = select("deg_mod_inflict_trait_type");
	const inflict_trait = select("deg_mod_inflict_trait");
	const inflict_math = select("deg_mod_inflict_math");
	const inflict_mod = select("deg_mod_inflict_mod");
	const inflict_bonus = select("deg_mod_inflict_bonus");
	const damage_mod = select("deg_mod_damage_mod");
	const damage_consequence = select("deg_mod_damage_consequence");
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
	const level_direction = select("deg_mod_level_direction");
	const circumstance = select("deg_mod_circumstance");
	const circ_target = select("deg_mod_circ_target");
	const measure_effect = select("deg_mod_measure_effect");
	const measure_type = select("deg_mod_meaasure_type");
	const measure_rank_value = select("deg_mod_measure_rank_value");
	const measure_rank = select("deg_mod_measure_rank");
	const unit_value = text("deg_mod_unit_value");
	const unit_type = select("deg_mod_unit_type");
	const unit = select("deg_mod_unit");
	const measure_trait_type = select("deg_mod_measure_trait_type");
	const measure_trait = select("deg_mod_measure_trait");
	const measure_trait_math = select("deg_mod_measure_trait_math");
	const measure_mod = select("deg_mod_measure_mod");
	const measure_math_rank = select("deg_mod_measure_math_rank");
	const measure_trait_type_unit = select("deg_mod_measure_trait_type_unit");
	const measure_trait_unit = select("deg_mod_measure_trait_unit");
	const measure_trait_math_unit = select("deg_mod_measure_trait_math_unit");
	const measure_mod_unit = select("deg_mod_measure_mod_unit");
	const measure_math_unit = select("deg_mod_measure_math_unit");
	const condition_type = select("deg_mod_condition_type");
	const condition_damage_value = select("deg_mod_condition_damage_value");
	const condition_damage = select("deg_mod_condition_damage");
	const condition1 = select("deg_mod_condition1");
	const condition2 = select("deg_mod_condition2");
	const condition_turns = select("deg_mod_condition_turns");
	const keyword = text("deg_mod_keyword");
	const nullify = select("deg_mod_nullify");
	const nullify_type = select("deg_mod_nullify_type");
	const cumulative = check("deg_mod_cumulative");
	const linked = select("deg_mod_linked");
	const check_type = select("deg_mod_check_type");
	const opposed = select("deg_mod_check_opposed");
	const resist_dc = select("deg_mod_check_resist_dc");
	const resist_trait_type = select("deg_mod_check_resist_trait_type");
	const resist_trait = select("deg_mod_check_resist_trait");
	const skill_dc = select("deg_mod_check_skill_dc");
	const skill_trait_type = select("deg_mod_check_skill_trait_type");
	const skill_trait = select("deg_mod_check_skill_trait");
	const routine_trait_type = select("deg_mod_check_routine_trait_type");
	const routine_trait = select("deg_mod_check_routine_trait");
	const routine_mod = select("deg_mod_check_routine_mod");
	const attack = select("deg_mod_check_attack");
	const attack_turns = select("deg_mod_check_attack_turns");
	const compare = select("deg_mod_check_compare");
	const duration = select("deg_mod_duration");
	const variable = select("deg_mod_check_variable");
	const title = text("deg_mod_title");
	const level_time = select("deg_mod_level_time");
	const effect_target = select("deg_mod_effect_target");
	const value_type = select("deg_mod_value_type");
	const description = text("deg_mod_desc");
	const descriptor_effect = select("deg_mod_descriptor_effect");
	const descriptor_target = select("deg_mod_descriptor_target");
	const descriptor = select("deg_mod_descriptor");
	const multiple = select("deg_mod_multiple");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'deg-mod-err';
	const err_line = 'deg-mod-err-line';

	const selects = 'degree-sml';
	const opp_selects = 'degree-opp-title-sml';
	const select_title = 'degree-title-sml';

	response = fetch('/power/degree/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'columns': columns,
			'created': created,
			'font': font,
			'target': target,
			'value': value,
			'type': type,
			'action': action,
			'time': time,
			'recovery': recovery,
			'damage_type': damage_type,
			'object': object,
			'object_effect': object_effect,
			'inflict_type': inflict_type,
			'inflict_flat': inflict_flat,
			'inflict_trait_type': inflict_trait_type,
			'inflict_trait': inflict_trait,
			'inflict_math': inflict_math,
			'inflict_mod': inflict_mod,
			'inflict_bonus': inflict_bonus,
			'damage_mod': damage_mod,
			'damage_consequence': damage_consequence,
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
			'level_direction': level_direction,
			'circumstance': circumstance,
			'circ_target': circ_target,
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
			'measure_trait_type_unit': measure_trait_type_unit,
			'measure_trait_unit': measure_trait_unit,
			'measure_trait_math_unit': measure_trait_math_unit,
			'measure_mod_unit': measure_mod_unit,
			'measure_math_unit': measure_math_unit,
			'condition_type': condition_type,
			'condition_damage_value': condition_damage_value,
			'condition_damage': condition_damage,
			'condition1': condition1,
			'condition2': condition2,
			'condition_turns': condition_turns,
			'keyword': keyword,
			'nullify': nullify,
			'nullify_type': nullify_type,
			'cumulative': cumulative,
			'linked': linked,
			'check_type': check_type,
			'opposed': opposed,
			'resist_dc': resist_dc,
			'resist_trait_type': resist_trait_type,
			'resist_trait': resist_trait,
			'skill_dc': skill_dc,
			'skill_trait_type': skill_trait_type,
			'skill_trait': skill_trait,
			'routine_trait_type': routine_trait_type,
			'routine_trait': routine_trait,
			'routine_mod': routine_mod,
			'attack': attack,
			'attack_turns': attack_turns,
			'compare': compare,
			'duration': duration,
			'variable': variable,
			'title': title,
			'level_time': level_time,
			'effect_target': effect_target,
			'value_type': value_type,
			'description': description,
			'descriptor_effect': descriptor_effect,
			'descriptor_target': descriptor_target,
			'descriptor': descriptor,
			'multiple': multiple
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			extra_effect_check(jsonResponse);
			
			const id = jsonResponse.id;
			const title_name = jsonResponse.title;
			const title_id = jsonResponse.title_id;
			const add_title = jsonResponse.add_title

			if (add_title == true) {
				selects_add(title_id, title_name, select_title);
			}

			selects_add(id, keyword, selects);

			deg_mod_grid.columns.length = 0;
			deg_mod_grid.columns = jsonResponse.rows

			const table_id = jsonResponse.table_id;
			const route = '/power/degree/delete/'
			create_table('power', jsonResponse, deg_mod_grid, route, [selects], title_id, [select_title]);
			clear_errors(err_line, errors)



			deg_mod_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
