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
		setTimeout(function(){val.style.display = 'grid'}, 300)
		setTimeout(function(){val.style.maxHeight = val.scrollHeight + 'px'}, 300)
		math.style.maxHeight = '0px'
		setTimeout(function(){math.style.display = 'none'}, 300)
	} else if (value == 'math') {
		setTimeout(function(){math.style.display = 'grid'}, 300)
		setTimeout(function(){math.style.maxHeight = math.scrollHeight + 'px'}, 300)
		val.style.maxHeight = '0px'
		setTimeout(function(){val.style.display = 'none'}, 300)
	} else {
		val.style.maxHeight = '0px'
		setTimeout(function(){val.style.display = 'none'}, 300)
		math.style.maxHeight = '0px'
		setTimeout(function(){math.style.display = 'none'}, 300)	
	}

	if ((value != 'value') && (value != 'math')) {
		setTimeout(function(){entry.style.maxHeight = entry.scrollHeight - val.scrollHeight + 'px'}, 300)
	} else {
		if (value == 'math') {
			setTimeout(function(){entry.style.maxHeight = entry.scrollHeight + math.scrollHeight + 'px'}, 300)
		} else if (value == 'value') {
			setTimeout(function(){entry.style.maxHeight = entry.scrollHeight + val.scrollHeight + 'px'}, 300)
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

	check_drop(check, div)
}

function dc_check_trait_type() {
	const select = 'dc_check_trait_type';
	const fill = 'dc_check_trait';

	trait_select(select, fill)
}