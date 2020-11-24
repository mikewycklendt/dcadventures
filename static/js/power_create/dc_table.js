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
	const field = document.getElementById('dc_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("dc-entry");

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

	if (value == 'value') {
		setTimeout(function(){val.style.display = 'grid'}, 300)
		setTimeout(function(){val.style.maxHeight = val.scrollHeight + 'px';}, 300)
		math.style.maxHeight = '0px'
		setTimeout(function(){math.style.display = 'none'}, 300)
	} else if (value == 'math') {
		setTimeout(function(){math.style.display = 'grid'}, 300)
		setTimeout(function(){math.style.maxHeight = math.scrollHeight + 'px';}, 300)
		val.style.maxHeight = '0px'
		setTimeout(function(){val.style.display = 'none'}, 300)
	} else {
		val.style.maxHeight = '0px'
		setTimeout(function(){val.style.display = 'none'}, 300)
		math.style.maxHeight = '0px'
		setTimeout(function(){math.style.display = 'none'}, 300)	
	}
}