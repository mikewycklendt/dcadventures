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

function dc_extra() {
	const field = 'dc_extra';
	
	descriptor_base(field);
}

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';
	const sub = 'skill-dc';

	id_select(select, fill, trait_select, sub);
}

function dc_math_trait() {
	const filter  = select('dc_math_trait_type');
	const fill = 'dc_math_trait';

	id_select(fill, fill, trait_filter, filter);
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

function dc_descrip() {
	const check = 'dc_descrip';
	const div = 'dc-descriptor';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_variable_check() {
	const check = 'dc_variable_check';
	const div = 'dc-variable';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_condition() {
	const check = 'dc_condition';
	const div = 'dc-condition';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_condition1() {
	const select = 'dc_condition1';
	const options = [{'val': 'dead', 'div': 'dc-condition-dead'}];
	const entry = 'dc-entry';

	select_maxheight_entry(select, options, entry);
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

function dc_cover() {
	const check = 'dc_cover'
	const div = 'dc-cover';
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_ranks() {
	const check = 'dc_ranks';
	const div = 'dc-ranks';
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_conceal() {
	const check = 'dc_conceal'
	const div = 'dc-conceal';
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

function dc_equip() {
	const check = 'dc_equip';
	const div = 'dc-equip';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_equipment_type() {
	const select = 'dc_equipment_type';
	const fill = 'dc_equipment';

	id_select(select, fill, equipment_select);
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
					{'val': 'skill_rank', 'div': 'dc-measure-skill'},
					{'val': 'skill_unit', 'div': 'dc-measure-skill-unit'}]

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

function dc_measure_trait() {
	const filter = select('dc_measure_trait_type');
	const fill = 'dc_measure_trait';

	id_select(fill, fill, trait_filter, filter);
}

function dc_measure_trait_type_unit() {
	const select = 'dc_measure_trait_type_unit';
	const fill = 'dc_measure_trait_unit';

	id_select(select, fill, trait_select);
}

function dc_measure_trait_unit() {
	const filter = select('dc_measure_trait_type_unit');
	const fill = 'dc_measure_trait_unit';

	id_select(fill, fill, trait_filter, filter);
}


function dc_damage() {
	const check = 'dc_damage';
	const div = 'dc-damage';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_tools_check() {
	const check = 'dc_tools_check';
	const div = 'dc-tools';
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
	const fields = ["dc_inflict_flat", "dc_inflict_trait_type", "dc_inflict_trait", 
					"dc_inflict_math", "dc_inflict_mod", "dc_inflict_bonus"]

	select_opacity(select, options);
	reset_all(fields)
}

function dc_inflict_trait_type() {
	const select = 'dc_inflict_trait_type';
	const fill = 'dc_inflict_trait';

	id_select(select, fill, trait_select);
}

function dc_inflict_trait() {
	const filter = select('dc_inflict_trait_type');
	const fill = 'dc_inflict_trait';

	id_select(fill, fill, trait_filter, filter);
}


let dc_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function dc_submit() {

	const columns = dc_grid.columns;
	const created = dc_grid.titles;
	const font = dc_grid.font;

	const extra_id = select("dc_extra");
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
	const levels = check("dc_levels")
	const damage = check("dc_damage")
	const cover = check("dc_cover")
	const complex = check("dc_complex")
	const measure = check("dc_measure")
	const conceal = check("dc_conceal")
	const action_when = select("dc_action_when")
	const action_no_damage = check("dc_action_no_damage")
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
	const measure_type = select("dc_meaasure_type");
	const measure_rank_value = select("dc_measure_rank_value")
	const measure_rank = select("dc_measure_rank")
	const unit_value = text("dc_unit_value")
	const unit_type = select("dc_unit_type")
	const unit = select("dc_unit")
	const measure_trait_type = select("dc_measure_trait_type")
	const measure_trait = select("dc_measure_trait")
	const measure_trait_math = select("dc_measure_trait_math")
	const measure_mod = select("dc_measure_mod")
	const measure_math_rank = select('dc_measure_math_rank')
	const measure_trait_type_unit = select("dc_measure_trait_type_unit")
	const measure_trait_unit = select("dc_measure_trait_unit")
	const measure_trait_math_unit = select("dc_measure_trait_math_unit")
	const measure_mod_unit = select("dc_measure_mod_unit")
	const measure_math_unit = select('dc_measure_math_unit')
	const level_type = select("dc_level_type")
	const level = select("dc_level")
	const condition1 = select("dc_condition1")
	const condition2 = select("dc_condition2")
	const condition_turns = select("dc_condition_turns")
	const condition_no_damage = check("dc_condition_no_damage")
	const condition_dead = select("dc_condition_dead");
	const keyword = text("dc_keyword")
	const complexity = select("dc_complexity")
	const tools_check = check("dc_tools_check");
	const cover_effect = select("dc_cover_effect");
	const cover_type = select("dc_cover_type");
	const conceal_effect = select("dc_conceal_effect");
	const conceal_type = select("dc_conceal_type");
	const tools = select("dc_tools");
	const variable_check = check("dc_variable_check");
	const variable = select("dc_variable");
	const time = select("dc_time");
	const title = text("dc_title")
	const surface = check("dc_surface")
	const effect_target = select("dc_effect_target");
	const equipment_use = select("dc_equipment_use");
	const equipment_type = select("dc_equipment_type");
	const equipment = select("dc_equipment");
	const equip = check("dc_equip");
	const descriptor_effect = select("dc_descriptor_effect");
	const descriptor_target = select("dc_descriptor_target");
	const descriptor = select("dc_descriptor");
	const descrip = check("dc_descrip")
	const ranks =  check("dc_ranks");
	const rank = select("dc_rank");
	const ranks_per = select("dc_ranks_per");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'dc-err';
	const err_line = 'dc-err-line';

	const dc_selects = 'dc-sml';
	const select_title = 'dc-title-sml';
	const opp_selects = 'dc-opp-sml';
	const player_selects = 'dc-player-sml';

	response = fetch('/power/dc/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
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
			'levels': levels,
			'damage': damage,
			'cover': cover,
			'complex': complex,
			'measure': measure,
			'conceal': conceal,
			'action_when': action_when,
			'action_no_damage': action_no_damage,			
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
			'level_type': level_type,
			'level': level,
			'condition1': condition1,
			'condition2': condition2,
			'condition_turns': condition_turns,
			'condition_no_damage': condition_no_damage,
			'condition_dead': condition_dead,
			'keyword': keyword,
			'complexity': complexity,
			'tools_check': tools_check,
			'cover_effect': cover_effect,
			'cover_type': cover_type,
			'conceal_effect': conceal_effect,
			'conceal_type': conceal_type,
			'tools': tools,
			'variable_check': variable_check,
			'variable': variable,
			'time': time,
			'title': title,
			'surface': surface,
			'effect_target': effect_target,
			'equipment_use': equipment_use,
			'equipment_type': equipment_type,
			'equipment': equipment,
			'equip': equip,
			'descriptor_effect': descriptor_effect,
			'descriptor_target': descriptor_target,
			'descriptor': descriptor,
			'descrip': descrip,
			'ranks': ranks,
			'rank': rank,
			'ranks_per': ranks_per
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
			selects_add(id, keyword, dc_selects);

			if (target == 'opp') {
				selects_add(id, keyword, opp_selects);
			} else if (target == 'active') {
				selects_add(id, keyword, player_selects)
			}

			dc_grid.columns.length = 0;
			dc_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, dc_grid, route, [dc_selects, opp_selects, player_selects], title_id, [select_title]);
			clear_errors(err_line, errors)

			dc_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}