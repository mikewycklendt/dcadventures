function mod_check() {
	const check = document.getElementById("mod_check");
	const title = document.getElementById("mod-title");
	const base = document.getElementById('mod-base');
	const entry = document.getElementById("mod-entry");

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function mod_base() {
	const field = document.getElementById('mod_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("mod-entry");

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
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
	const entry =  'mod-entry';
	const trait = 'mod-limited-trait';
	const desc = 'mod-limited-description';
	const sub = 'mod-limited-subjects';
	const extra = 'mod-limited-extra';
	const lan = 'mod-limited-language';
	const deg = 'mod-limited-degree'
	const sen = 'mod-limited-sense';
	const field = document.getElementById('mod_limited_type');
	const val = field.options[field.selectedIndex].value;

	if (val == 'trait'){
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(desc);
		hide_maxheight(sub);
		hide_maxheight(deg);
		hide_maxheight(sen);
		show_maxheight(trait, entry);
	} else if (val == 'other') {
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(trait);
		hide_maxheight(sub)
		hide_maxheight(deg);
		hide_maxheight(sen);
		show_maxheight(desc, entry);
	} else if (val == 'subjects') {
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(trait);
		hide_maxheight(desc);
		hide_maxheight(deg);
		hide_maxheight(sen);
		show_maxheight(sub, entry)
	} else if (val == 'extra') {
		hide_maxheight(trait);
		hide_maxheight(desc);
		hide_maxheight(lan);
		hide_maxheight(sub);
		hide_maxheight(deg);
		hide_maxheight(sen);
		show_maxheight(extra);		
	} else if (val == 'language') {
		hide_maxheight(trait);
		hide_maxheight(desc);
		hide_maxheight(extra);
		hide_maxheight(sub);
		hide_maxheight(deg);
		hide_maxheight(sen);
		show_maxheight(lan);
	} else if (val == 'degree') {
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(sub);
		hide_maxheight(desc);
		hide_maxheight(trait);
		hide_maxheight(sen);
		show_maxheight(deg);
	} else if (val == 'sense') {
		hide_maxheight(deg);
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(sub);
		hide_maxheight(desc);
		hide_maxheight(trait);
		show_maxheight(sen);
	} else {
		hide_maxheight(deg);
		hide_maxheight(lan);
		hide_maxheight(extra);
		hide_maxheight(sub);
		hide_maxheight(desc);
		hide_maxheight(trait);
		hide_maxheight(sen);
	}
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
	const select = document.getElementById('mod_ranged_type');
	const value = select.options[select.selectedIndex].value;
	const val = 'mod-ranged-value';
	const math = 'mod-ranged-math';
	const mod = 'mod-ranged-mod';
	const che = 'mod-ranged-check';

	if (value == 'value') {
		hide_opacity(math);
		hide_opacity(mod);
		hide_opacity(che);
		show_opacity(val)
	} else if (value == 'math') {
		hide_opacity(val);
		hide_opacity(mod);
		hide_opacity(che);
		show_opacity(math);
	} else if (value == 'mod') {
		hide_opacity(math);
		hide_opacity(val);
		hide_opacity(che);
		show_opacity(mod);
	} else if (value == 'check') {
		hide_opacity(math);
		hide_opacity(mod);
		hide_opacity(val);
		show_opacity(che);
	} else {
		hide_opacity(math);
		hide_opacity(mod);
		hide_opacity(val);
		hide_opacity(che);
	}
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

function mod_side() {
	const check = 'mod_side';
	const div = 'mod-side';
	const entry = 'mod-entry';

	check_drop(check, div, entry);
}