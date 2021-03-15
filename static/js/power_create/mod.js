function mod_check() {
	const check = "mod_check";
	const title = "mod-title";
	const base = 'mod-base';
	const entry = "mod-entry";

	check_title(check, title, base, entry);
}

function mod_base() {
	const field = 'mod_extra';
	const entry = "mod-entry";

	base(field, entry);
}

function mod_extra() {
	const select = 'mod_extra';
	const fill = 'mod_cost';

	id_select(select, fill, power_cost_select, the_power);
}

function mod_cost() {
	const select = 'mod_cost';
	const fill = 'mod_ranks';
	const extra = 'mod_extra';

	id_select(select, fill, power_ranks_select, extra, false, false, false, the_power);
}

function mod_cost() {
	const select = 'mod_cost';
	const fill = 'mod_ranks';
	const extra = 'mod_extra';

	id_select(select, fill, power_ranks_select, extra, false, false, false, the_power);
}
function mod_area() {

	const check = 'mod_area';
	const div = 'mod-area';
	const entry = 'mod-entry';
	
	check_drop(check, div, entry);
}

function mod_limited() {
	const check = 'mod_limited'
	const div = 'mod-limited';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_limited_trait_type() {
	const select = 'mod_limited_trait_type';
	const fill = 'mod_limited_trait'

	id_select(select, fill, trait_select);
}

function mod_limited_trait() {
	const filter = select('mod_limited_trait_type');
	const fill = 'mod_limited_trait'

	id_select(fill, fill, trait_filter, filter);
}

function mod_limited_type() {
	const options = [{'val': 'trait', 'div': 'mod-limited-trait'},
					{'val': 'other', 'div': 'mod-limited-description'},
					{'val': 'subjects', 'div': 'mod-limited-subjects'},
					{'val': 'extra', 'div': 'mod-limited-extra'},
					{'val': 'language', 'div': 'mod-limited-language'},
					{'val': 'degree', 'div': 'mod-limited-degree'},
					{'val': 'sense', 'div': 'mod-limited-sense'},
					{'val': 'range', 'div': 'mod-limited-range'},
					{'val': 'descriptor', 'div': 'mod-limited-descriptor'},
					{'val': 'task', 'div': 'mod-limited-task'},
					{'val': 'task_type', 'div': 'mod-limited-task-type'},
					{'val': 'source', 'div': 'mod-limited-source'},
					{'val': 'level', 'div': 'mod-limited-level'}];
	const field = 'mod_limited_type';

	select_opacity(field, options);
}

function mod_limited_sense() {
	const select = 'mod_limited_sense';
	const fill = 'mod_limited_subsense';

	id_select(select, fill, subsense_select);
}

function mod_ranged() {
	const check = 'mod_ranged';
	const div = 'mod-ranged';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_ranged_type() {
	const select = 'mod_ranged_type';
	const options = [{'val': 'value', 'div': 'mod-ranged-value'},
					{'val': 'math', 'div': 'mod-ranged-math'},
					{'val': 'mod', 'div': 'mod-ranged-mod'},
					{'val': 'check', 'div': 'mod-ranged-check'}];

	select_opacity(select, options);
}

function mod_ranged_math_trait_type() {
	const select = 'mod_ranged_math_trait_type';
	const fill = 'mod_ranged_math_trait'; 

	id_select(select, fill, trait_select);
}

function mod_ranged_check() {
	const field = document.getElementById('mod_ranged_check');
	const val = field.options[field.selectedIndex].value;
	const div = document.getElementById('mod-ranged-check-dc');

	if ((val == 1) || (val == 6)) {
		div.style.opacity = '100%'
	} else {
		div.style.opacity = '0%';
	}
}

function mod_reflect() {
	const check = 'mod_reflect';
	const div = 'mod-reflect';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_reflect_trait_type() {
	const select = 'mod_reflect_trait_type';
	const fill = 'mod_reflect_trait';

	id_select(select, fill, trait_select);
}

function mod_reflect_trait() {
	const filter = select('mod_reflect_trait_type');
	const fill = 'mod_reflect_trait';

	id_select(fill, fill, trait_filter, filter);
}

function mod_subtle() {
	const check = 'mod_subtle';
	const div = 'mod-subtle';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_subtle_perception_check() {
	const check = 'mod_subtle_perception_check';
	const div = 'mod-subtle-dc';

	check_opacity(check, div);
}

function mod_subtle_null_trait_type() {
	const select = 'mod_subtle_null_trait_type';
	const fill = 'mod_subtle_null_trait';

	id_select(select, fill, trait_select);
}

function mod_subtle_null_trait() {
	const filter = select('mod_subtle_null_trait_type');
	const fill = 'mod_subtle_null_trait';

	id_select(fill, fill, trait_filter, filter);
}

function mod_subtle_opponent_trait_type() {
	const select = 'mod_subtle_opponent_trait_type';
	const fill = 'mod_subtle_opponent_trait';

	id_select(select, fill, trait_select);
}

function mod_subtle_opponent_trait() {
	const filter = select('mod_subtle_opponent_trait_type');
	const fill = 'mod_subtle_opponent_trait';

	id_select(fill, fill, trait_filter, filter);
}

function mod_others() {
	const check = 'mod_others';
	const div = 'mod-others';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_others_touch() {
	const check = 'mod_others_touch';
	const div = 'mod-others-touch';

	check_opacity(check, div);
}

function mod_points() {
	const check = 'mod_points';
	const div = 'mod-points';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_ranks_check() {
	const check = 'mod_ranks_check';
	const div = 'mod-ranks';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_ranks_trait_type() {
	const select = 'mod_ranks_trait_type';
	const fill = 'mod_ranks_trait';

	id_select(select, fill, trait_select);
}

function mod_ranks_trait() {
	const filter = select('mod_ranks_trait_type');
	const fill = 'mod_ranks_trait';

	id_select(fill, fill, trait_filter, filter);
}

function mod_points_type() {
	const field = document.getElementById('mod_points_type');
	const val = field.options[field.selectedIndex].value;
	const rer = 'mod-points-reroll';

	if (val == 'reroll') {
		show_opacity(rer)
	} else {
		hide_opacity(rer)
	}
}

function mod_points_reerolls() {
	const field = document.getElementById("mod_points_rerolls");
	const val = field.options[field.selectedIndex].value;
	const div = document.getElementById('mod-points-reroll-result');

	if (val > 1) {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function mod_side_effect() {
	const check = 'mod_side_effect';
	const div = 'mod-side';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_simultaneous() {
	const check = 'mod_simultaneous';
	const div = 'mod-simultaneous';
	const entry =  'mod-entry';

	check_drop(check, div, entry)
}

function mod_effortless() {
	const check =  'mod_effortless';
	const div = 'mod-effortless';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_side_effect_type() {
	const select = 'mod_side_effect_type';
	const options = [{'val': 'other', 'div': 'mod-side-other'},
					{'val': 'level', 'div': 'mod-side-level'}]

	select_opacity(select, options);
}

function mod_affects_objects() {
	const check = 'mod_affects_objects';
	const div = 'mod-affects-objects';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_side_level_type() {
	const select = 'mod_side_level_type';
	const fill = 'mod_side_level';

	id_select(select, fill, level_select);
}

function mod_limited_level_type() {
	const select = 'mod_limited_level_type';
	const fill = 'mod_limited_level';

	id_select(select, fill, level_select);
}


let mod_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function mod_submit() {

	const columns = mod_grid.columns;
	const created = mod_grid.titles;
	const font = mod_grid.font;

	const extra_id = select("mod_extra");
	const affects_objects = check("mod_affects_objects");
	const area = check("mod_area");
	const persistent = check("mod_persistent");
	const incurable = check("mod_incurable");
	const selective = check("mod_selective");
	const limited = check("mod_limited");
	const innate = check("mod_innate");
	const others = check("mod_others");
	const sustained = check("mod_sustained");
	const reflect = check("mod_reflect");
	const redirect = check("mod_redirect");
	const half = check("mod_half");
	const affects_corp = check("mod_affects_corp");
	const continuous = check("mod_continuous");
	const vulnerable = check("mod_vulnerable");
	const precise = check("mod_precise");
	const progressive = check("mod_progressive");
	const subtle = check("mod_subtle");
	const permanent = check("mod_permanent");
	const points = check("mod_points");
	const ranks_check = check("mod_ranks_check");
	const action = check("mod_action");
	const side_effect = check("mod_side_effect");
	const concentration = check("mod_concentration");
	const simultaneous = check("mod_simultaneous");
	const effortless = check("mod_effortless");
	const noticeable = check("mod_noticeable");
	const unreliable = check("mod_unreliable");
	const radius = check("ranks_radius");
	const accurate = check("ranks_accurate");
	const acute = check("ranks_acute");
	const objects_alone = select("mod_objects_alone");
	const objects_character = select("mod_objects_character");
	const effortless_degree = select("mod_effortless_degree");
	const effortless_retries = check("mod_effortless_retries");
	const simultaneous_descriptor = select("mod_simultaneous_descriptor");
	const area_mod = select("mod_area_mod");
	const area_range = select("mod_area_range");
	const area_per_rank = check("mod_area_per_rank");
	const area_descriptor = select("mod_area_descriptor");
	const limited_type = select("mod_limited_type");
	const limited_mod = select("mod_limited_mod");
	const limited_level = select('mod_limited_level');
	const limited_source = select("mod_limited_source");
	const limited_task_type = select("mod_limited_task_type");
	const limited_task = text("mod_limited_task");
	const limited_trait_type = select("mod_limited_trait_type");
	const limited_trait = select("mod_limited_trait");
	const limited_description = text("mod_limited_description");
	const limited_subjects = select("mod_limited_subjects");
	const limited_extra = select("mod_limited_extra");
	const limited_language_type = select("mod_limited_language_type");
	const limited_degree = select("mod_limited_degree");
	const limited_sense = select("mod_limited_sense");
	const limited_subsense = select("mod_limited_subsense");
	const limited_descriptor = select("mod_limited_descriptor");
	const limited_range = select("mod_limited_range");
	const side_effect_type = select("mod_side_effect_type");
	const side_other = text("mod_side_other");
	const side_level = select('mod_side_level');
	const reflect_check = select("mod_reflect_check");
	const reflect_dc = select("mod_reflect_dc");
	const reflect_trait_type = select("mod_reflect_trait_type");
	const reflect_trait = select("mod_reflect_trait");
	const reflect_descriptor = select("mod_reflect_descriptor");
	const subtle_opponent_trait_type = select("mod_subtle_opponent_trait_type");
	const subtle_opponent_trait = select("mod_subtle_opponent_trait");
	const subtle_dc = select("mod_subtle_dc");
	const subtle_null_trait_type = select("mod_subtle_null_trait_type");
	const subtle_null_trait = select("mod_subtle_null_trait");
	const others_carry = check("mod_others_carry");
	const others_touch = check("mod_others_touch");
	const others_touch_continuous = check("mod_others_touch_continuous");
	const ranks_trait_type = select("mod_ranks_trait_type");
	const ranks_trait = select("mod_ranks_trait");
	const ranks_ranks = select("mod_ranks_ranks");
	const ranks_mod = select("mod_ranks_mod");
	const points_type = select("mod_points_type");
	const points_reroll_target = select("mod_points_reroll_target");
	const points_reroll_cost = select("mod_points_reroll_cost");
	const points_rerolls = select("mod_points_rerolls");
	const points_reroll_result = select("mod_points_reroll_result");
	const ranks = select("mod_ranks");
	const cost = select("mod_cost");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'mod-err';
	const err_line = 'mod-err-line';

	response = fetch('/power/mod/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'affects_objects': affects_objects,
			'area': area,
			'persistent': persistent,
			'incurable': incurable,
			'selective': selective,
			'limited': limited,
			'innate': innate,
			'others': others,
			'sustained': sustained,
			'reflect': reflect,
			'redirect': redirect,
			'half': half,
			'affects_corp': affects_corp,
			'continuous': continuous,
			'vulnerable': vulnerable,
			'precise': precise,
			'progressive': progressive,
			'subtle': subtle,
			'permanent': permanent,
			'points': points,
			'ranks_check': ranks_check,
			'action': action,
			'side_effect': side_effect,
			'concentration': concentration,
			'simultaneous': simultaneous,
			'effortless': effortless,
			'noticeable': noticeable,
			'unreliable': unreliable,
			'radius': radius,
			'accurate': accurate,
			'acute': acute,
			'objects_alone': objects_alone,
			'objects_character': objects_character,
			'effortless_degree': effortless_degree,
			'effortless_retries': effortless_retries,
			'simultaneous_descriptor': simultaneous_descriptor,
			'area_mod': area_mod,
			'area_range': area_range,
			'area_per_rank': area_per_rank,
			'area_descriptor': area_descriptor,
			'limited_type': limited_type,
			'limited_mod': limited_mod,
			'limited_level': limited_level,
			'limited_source': limited_source,
			'limited_task_type': limited_task_type,
			'limited_task': limited_task,
			'limited_trait_type': limited_trait_type,
			'limited_trait': limited_trait,
			'limited_description': limited_description,
			'limited_subjects': limited_subjects,
			'limited_extra': limited_extra,
			'limited_language_type': limited_language_type,
			'limited_degree': limited_degree,
			'limited_sense': limited_sense,
			'limited_subsense': limited_subsense,
			'limited_descriptor': limited_descriptor,
			'limited_range': limited_range,
			'side_effect_type': side_effect_type,
			'side_level': side_level,
			'side_other': side_other,
			'reflect_check': reflect_check,
			'reflect_dc': reflect_dc,
			'reflect_trait_type': reflect_trait_type,
			'reflect_trait': reflect_trait,
			'reflect_descriptor': reflect_descriptor,
			'subtle_opponent_trait_type': subtle_opponent_trait_type,
			'subtle_opponent_trait': subtle_opponent_trait,
			'subtle_dc': subtle_dc,
			'subtle_null_trait_type': subtle_null_trait_type,
			'subtle_null_trait': subtle_null_trait,
			'others_carry': others_carry,
			'others_touch': others_touch,
			'others_touch_continuous': others_touch_continuous,
			'ranks_trait_type': ranks_trait_type,
			'ranks_trait': ranks_trait,
			'ranks_ranks': ranks_ranks,
			'ranks_mod': ranks_mod,
			'points_type': points_type,
			'points_reroll_target': points_reroll_target, 
			'points_reroll_cost': points_reroll_cost,
			'points_rerolls': points_rerolls,
			'points_reroll_result': points_reroll_result,
			'ranks': ranks,
			'cost': cost,
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

			mod_grid.columns.length = 0;
			mod_grid.columns = jsonResponse.rows;
			cells = jsonResponse.cells

			let c;
			for (c of cells){
				console.log(c)
			}

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, mod_grid, route);
			clear_errors(err_line, errors)

			mod_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}