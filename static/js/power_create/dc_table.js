function dc_check() {
	const check = "dc_check";
	const title = "dc-title";
	const base = 'dc-base';
	const entry = "dc-entry";

	check_title(check, title, base, entry);
}

function dc_base() {
	const field = 'dc_extra';
	const field2 = 'dc_target';
	const entry = "dc-entry";

	base_two(field, field2, entry);
}

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';

	trait_select(select, fill);
}

function dc_dc() {
	const field = document.getElementById('dc_dc');
	const value = field.options[field.selectedIndex].value;
	const val = 'dc-value';
	const math = 'dc-math';
	const entry = 'dc-entry';

	if (value == 'value') {
		show_maxheight(val);
		hide_maxheight(math)
	} else if (value == 'math') {
		show_maxheight(math);
		hide_maxheight(val)
	} else {
		hide_maxheight(val);
		hide_maxheight(math)	
	}

	if ((value != 'value') && (value != 'math')) {
		shrink_entry(entry, val)
	} else {
		if (value == 'math') {
			grow_entry(entry, math);
		} else if (value == 'value') {
			grow_entry(entry, val);
		}
	}
}

function dc_time() {
	const check = 'dc_time';
	const div = 'dc-time';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_descriptor() {
	const check = 'dc_descriptor';
	const div = 'dc-descriptor';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_condition() {
	const check = 'dc_condition';
	const div = 'dc-condition';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_keyword() {
	const check = 'dc_keyword';
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

function dc_check_trait_type() {
	const select = 'dc_check_trait_type';
	const fill = 'dc_check_trait';

	trait_select(select, fill)
}