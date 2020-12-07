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

	trait_select(select, fill);
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
					{'val': 'source', 'div': 'mod-limited-task-source'}];
	const field = 'mod_limited_type';

	select_opacity(field, options);
}

function mod_limited_sense() {
	const select = 'mod_limited_sense';
	const fill = 'mod_limited_subsense';

	subsense_select(select, fill);
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

	trait_select(select, fill)
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

	trait_select(select, fill);
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

function mod_subtle_trait_type() {
	const select = 'mod_subtle_trait_type';
	const fill = 'mod_subtle_trait';

	trait_select(select, fill);
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

function mod_ranks() {
	const check = 'mod_ranks';
	const div = 'mod-ranks';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_ranks_trait_type() {
	const select = 'mod_ranks_trait_type';
	const fill = 'mod_ranks_trait';

	trait_select(select, fill);
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
	const options = [{'val': 'other', 'div': 'mod-side-other'}]

	select_opacity(select, options);
}