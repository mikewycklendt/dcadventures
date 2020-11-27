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
	const sub = 'mod-limited-subjects'
	const field = document.getElementById('mod_limited_type');
	const val = field.options[field.selectedIndex].value;

	if (val == 'trait'){
		hide_maxheight(desc);
		hide_maxheight(sub);
		show_maxheight(trait, entry);
	} else if (val == 'other') {
		hide_maxheight(trait);
		hide_maxheight(sub)
		show_maxheight(desc, entry);
	} else if (val == 'subjects') {
		hide_maxheight(trait);
		hide_maxheight(desc);
		show_maxheight(sub, entry)
	} else {
		hide_maxheight(desc);
		show_maxheight(trait);
	}
}

function mod_ranged() {
	const check = 'mod_ranged';
	const div = 'mod-ranged';
	const entry = 'mod-entry';

	check_drop(check, div, entry)
}

function mod_ranged_type() {
	const select = 'mod_ranged_type';
	const val = 'mod-ranged-value';
	const math = 'mod-ranged-math';

	value_type(select, math, val)
}

function mod_ranged_math_trait_type() {
	const select = 'mod_ranged_math_trait_type';
	const fill = 'mod_ranged_math_trait'; 

	trait_select(select, fill)
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