function mod_check() {
	const check = "mod_check";
	const title = "mod-title";
	const base = 'mod-base';
	const entry = "mod-entry";

	check_title(check, title, base, entry);
}

function mod_base() {
	const field = 'mod_extra_id';
	const entry = "mod-entry";

	base(field, entry);
	descriptor_base(field);
}

function mod_extra_id() {
	const field = 'mod_extra_id';
	const fill = 'mod_cost';
	const ranks = 'mod_ranks';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function mod_cost() {
	const field = 'mod_cost';
	const fill = 'mod_ranks';
	const extra = 'mod_extra';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
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
	const options = [{'val': ['trait'], 'div': 'mod-limited-trait'},
					{'val': ['other'], 'div': 'mod-limited-description'},
					{'val': ['subjects'], 'div': 'mod-limited-subjects'},
					{'val': ['extra'], 'div': 'mod-limited-extra'},
					{'val': ['degree'], 'div': 'mod-limited-degree'},
					{'val': ['sense'], 'div': 'mod-limited-sense'},
					{'val': ['range'], 'div': 'mod-limited-range'},
					{'val': ['descriptor'], 'div': 'mod-limited-descriptor'},
					{'val': ['task'], 'div': 'mod-limited-task'},
					{'val': ['task_type'], 'div': 'mod-limited-task-type'},
					{'val': ['source'], 'div': 'mod-limited-source'},
					{'val': ['level', 'to_level'], 'div': 'mod-limited-level'},
					{'val': ['ground'], 'div': 'mod-limited-ground'},
					{'val': ['creature'], 'div': 'mod-limited-creature'},
					{'val': ['env'], 'div': 'mod-limited-env'},
					{'val': ['emotion'], 'div': 'mod-limited-emotion'},
					{'val': ['material'], 'div': 'mod-limited-material'},
					{'val': ['org'], 'div': 'mod-limited-org'}];
	const field = 'mod_limited_type';

	select_opacity_shared(field, options);
}

function mod_limited_sense() {
	const select = 'mod_limited_sense';
	const fill = 'mod_limited_subsense';

	id_select(select, fill, subsense_select, all_var_sub);
}

function mod_limited_env() {
	const select = 'mod_limited_env';
	const options = [{'val': 'other', 'div': 'mod-limited-env-other'}];

	select_opacity(select, options);
}

function mod_limited_emotion() {
	const select = 'mod_limited_emotion';
	const options = [{'val': 'other', 'div': 'mod-limited-emotion-other'}];

	select_opacity(select, options);
}

function mod_limited_org() {
	const select = 'mod_limited_org';
	const options = [{'val': 'other', 'div': 'mod-limited-org-other'}];

	select_opacity(select, options);
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
	const field = 'mod_points_type';
	const options =  [{'val': 'reroll', 'div': 'mod-points-reroll'},
					{'val': 'give', 'div': 'mod-points-give'},];

	
	select_opacity(field, options)
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

function mod_effortless_type() {
	const select = 'mod_effortless_type';
	const options = [{'val': 'reattempt', 'div': 'mod-effortless-reattempt'}]

	select_opacity(select, options);
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

function mod_extra() {
	const check = 'mod_extra';
	const div = 'mod-extra';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_limited_creature() {
	const select = 'mod_limited_creature';
	const fill = 'mod_limited_creature_narrow';
	const options = [{'val': 'other', 'div': 'mod-limited-creature-other'}]
	
	id_select(select, fill, narrow_creature_select, other_var_sub);
	select_opacity(select, options)
}

function mod_limited_creature_narrow() {
	const select = 'mod_limited_creature_narrow';
	const options = [{'val': 'other', 'div': 'mod-limited-creature-other'}]
	
	select_opacity(select, options)
}

function mod_limited_material() {
	const select = 'mod_limited_material';
	const options = [{'val': 'other', 'div': 'mod-limited-material-other'}]

	select_opacity(select, options);
}

function mod_feedback() {
	const check = 'mod_feedback';
	const div = 'mod-feedback';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_feedback_type() {
	const select = 'mod_feedback_type';
	const options = [{'val': 'mod', 'div': 'mod-feedback-mod'},
					{'val': 'defense', 'div': 'mod-feedback-defense'}]

	select_opacity(select, options);
}

function mod_adv() {
	const check = 'mod_adv';
	const div = 'mod-advantage';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_precise() {
	const check = 'mod_precise';
	const div = 'mod-precise';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_sustained() {
	const check = 'mod_sustained';
	const div = 'mod-sustained';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_concentration() {
	const check = 'mod_concentration';
	const div = 'mod-concentration';
	const entry  = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_unreliable() {
	const check = 'mod_unreliable';
	const div = 'mod-unreliable';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_incurable() {
	const check = 'mod_incurable';
	const div = 'mod-incurable';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_progressive() {
	const check = 'mod_progressive';
	const div = 'mod-progressive';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}

function mod_progressive_type() {
	const select = 'mod_progressive_type';
	const options = [{'val': ['increase'], 'div': 'mod-progressive-degree-type'},
					{'val': ['repeat'], 'div': 'mod-progressive-degree'}];
	const fields = ['mod_progressive_degree_type', 'mod_progressive_degree']
					
	reset_all(fields);
	select_opacity_shared(select, options);
}

let mod_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function mod_submit() {

	const columns = mod_grid.columns;
	const created = mod_grid.titles;
	const font = mod_grid.font;

	const extra_id = select("mod_extra_id");
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
	const effortless_degree_type = select("mod_effortless_degree_type");
	const simultaneous_descriptor = select("mod_simultaneous_descriptor");
	const area_damage = select("mod_area_damage");
	const area_ranged = select("mod_area_ranged");
	const area_descriptor = select("mod_area_descriptor");
	const area_attach = check("mod_area_attach");
	const limited_type = select("mod_limited_type");
	const limited_mod = select("mod_limited_mod");
	const limited_level_degree = select("mod_limited_level_degree");
	const limited_level = select('mod_limited_level');
	const limited_source_type = select("mod_limited_source_type")
	const limited_source = select("mod_limited_source");
	const limited_task_type = select("mod_limited_task_type");
	const limited_task = text("mod_limited_task");
	const limited_trait_type = select("mod_limited_trait_type");
	const limited_trait = select("mod_limited_trait");
	const limited_description = text("mod_limited_description");
	const limited_subjects = select("mod_limited_subjects");
	const limited_extra = select("mod_limited_extra");
	const limited_language_type = select("mod_limited_language_type");
	const limited_degree_type = select("mod_limited_degree_type");
	const limited_degree = select("mod_limited_degree");
	const limited_sense = select("mod_limited_sense");
	const limited_subsense = select("mod_limited_subsense");
	const limited_sense_depend = check("mod_limited_sense_depend");
	const limited_descriptor = select("mod_limited_descriptor");
	const limited_range_type = select("mod_limited_range_type");
	const limited_range = select("mod_limited_range");
	const limited_ground = select("mod_limited_ground");
	const limited_creature = select("mod_limited_creature");
	const limited_creature_narrow = select("mod_limited_creature_narrow");
	const limited_creature_other = text("mod_limited_creature_other");
	const limited_emotion_other =  text("mod_mod_limited_emotion_other");
	const limited_emotion = select("mod_limited_emotion");
	const limited_env = select("mod_limited_env");
	const limited_env_other = text("mod_limited_env_other");
	const limited_material = select("mod_limited_material");
	const limited_material_other = text("mod_limited_material_other");
	const limited_material_other_tough = select("mod_limited_material_other_tough");
	const limited_org = select('mod_limited_org');
	const limited_org_other = text("mod_limited_org_other");
	const side_effect_type = select("mod_side_effect_type");
	const side_other = text("mod_side_other");
	const side_level = select('mod_side_level');
	const reflect_check = select("mod_reflect_check");
	const reflect_descriptor = select("mod_reflect_descriptor");
	const subtle_type = select("mod_subtle_type");
	const subtle_opposed = select("mod_subtle_opposed");
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
	const points_give = select("mod_points_give");
	const ranks = select("mod_ranks");
	const cost = select("mod_cost");
	const extra = check("mod_extra");
	const extra_count = select("mod_extra_count");
	const extra_degree = select("mod_extra_degree");
	const extra_dc = select("mod_extra_dc");
	const extra_circ = select("mod_extra_circ");
	const multiple = select("mod_multiple");
	const feedback = check("mod_feedback");
	const feedback_mod = select("mod_feedback_mod");
	const feedback_type = select("mod_feedback_type");
	const feedback_cover = select("mod_feedback_cover");
	const feedback_defense = select("mod_feedback_defense");
	const passive = check("mod_passive");
	const adv = check("mod_adv");
	const advantage = select("mod_advantage");
	const advantage_rank = select("mod_advantage_rank");
	const advantage_rank_per = check("mod_advantage_rank_per");
	const advantage_effect = check("mod_advantage_effect");
	const precise_type = select("mod_precise_type");
	const sustained_action = select("mod_sustained_action");
	const sustained_no_move = check("mod_sustained_no_move");
	const concentration_check = select("mod_concentration_check");
	const concentration_check_type = select("mod_concentration_check_type");
	const concentration_opposed = select("mod_concentration_opposed");
	const concentration_effort = check("mod_concentration_effort");
	const unreliable_type = select("mod_unreliable_type");
	const incurable_type = select("mod_incurable_type");
	const progressive_type = select("mod_progressive_type");
	const progressive_degree = select("mod_progressive_degree");
	const progressive_degree_type = select("mod_progressive_degree_type")
	
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
			'effortless_degree_type': effortless_degree_type,
			'effortless_degree': effortless_degree,
			'effortless_retries': effortless_retries,
			'simultaneous_descriptor': simultaneous_descriptor,
			'area_damagw': area_damage,
			'area_range': area_ranged,
			'area_descriptor': area_descriptor,
			'area_attach': area_attach,
			'limited_type': limited_type,
			'limited_mod': limited_mod,
			'limited_level_degree': limited_level_degree,
			'limited_level': limited_level,
			'limited_source_type': limited_source_type,
			'limited_source': limited_source,
			'limited_task_type': limited_task_type,
			'limited_task': limited_task,
			'limited_trait_type': limited_trait_type,
			'limited_trait': limited_trait,
			'limited_description': limited_description,
			'limited_subjects': limited_subjects,
			'limited_extra': limited_extra,
			'limited_language_type': limited_language_type,
			'limited_degree_type': limited_degree_type,
			'limited_degree': limited_degree,
			'limited_sense': limited_sense,
			'limited_subsense': limited_subsense,
			'limited_sense_depend': limited_sense_depend,
			'limited_descriptor': limited_descriptor,
			'limited_range_type': limited_range_type,
			'limited_range': limited_range,
			'limited_ground': limited_ground,
			'limited_creature': limited_creature,
			'limited_creature_narrow': limited_creature_narrow,
			'limited_creature_other': limited_creature_other,
			'limited_emotion': limited_emotion,
			'limited_emotion_other': limited_emotion_other,
			'limited_env': limited_env,
			'limited_env_other': limited_env_other,
			'limited_org': limited_org,
			'limited_org_other': limited_org_other,
			'limited_material': limited_material,
			'limited_material_other': limited_material_other,
			'limited_material_other_tough': limited_material_other_tough,
			'side_effect_type': side_effect_type,
			'side_level': side_level,
			'side_other': side_other,
			'reflect_check': reflect_check,
			'reflect_descriptor': reflect_descriptor,
			'subtle_type': subtle_type,
			'subtle_opposed': subtle_opposed,
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
			'points_give': points_give,
			'ranks': ranks,
			'cost': cost,
			'columns': columns,
			'created': created,
			'font': font,
			'extra': extra,
			'extra_count': extra_count,
			'extra_degree': extra_degree,
			'extra_dc': extra_dc,
			'extra_circ': extra_circ,
			'multiple': multiple,
			'feedback': feedback,
			'feedback_type': feedback_type,
			'feedback_cover': feedback_cover,
			'feedback_mod': feedback_mod,
			'feedback_defense': feedback_defense,
			'passive': passive,
			'adv': adv,
			'advantage': advantage,
			'advantage_rank': advantage_rank,
			'advantage_rank_per': advantage_rank_per,
			'advantage_effect': advantage_effect,
			'precise_type': precise_type,
			'sustained_action': sustained_action,
			'sustained_no_move': sustained_no_move,
			'concentration_check': concentration_check,
			'concentration_check_type': concentration_check_type,
			'concentration_opposed': concentration_opposed,
			'concentration_effort': concentration_effort,
			'unreliable_type': unreliable_type,
			'incurable_type': incurable_type,
			'progressive_type': progressive_type,
			'progressive_degree': progressive_degree,
			'progressive_degree_type': progressive_degree_type
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

			const insert = jsonResponse.new;
			const items = jsonResponse.new_items;

			new_items(insert, items);
			
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