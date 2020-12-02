function dc_check() {
	const check = document.getElementById("dc_check");
	const title = document.getElementById("dc-title");
	const base = document.getElementById('dc-base');
	const entry = document.getElementById("dc-entry");

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

function dc_base() {
	const field = document.getElementById('dc_extra')
	const value = field.options[field.selectedIndex].value;
	
	const field2 = document.getElementById('dc_target')
	const target = field2.options[field2.selectedIndex].value;
	const entry = document.getElementById("dc-entry")

	if (value != '' && target != '') {
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

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';

	trait_select(select, fill);
}

function dc_dc() {
	const field = document.getElementById('dc_dc');
	const value = field.options[field.selectedIndex].value;
	const val = document.getElementById('dc-value');
	const math = document.getElementById('dc-math');
	const entry = document.getElementById('dc-entry');

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