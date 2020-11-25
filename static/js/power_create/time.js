function time_check() {
	const check = document.getElementById("time_check");
	const title = document.getElementById("time-title");
	const base = document.getElementById('time-base');
	const entry = document.getElementById("time-entry");

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

function time_base() {
	const field = document.getElementById('time_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("time-entry");

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

function time_trait_type() {
	const select = 'time_trait_type'
	const fill = 'time_trait'

	trait_select(select, fill)
}

function time_value_type() {
	const select = 'time_value_type';
	const math = 'time-math';
	const value = 'time-value';

	value_type(select, math, value)
}