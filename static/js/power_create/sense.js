function sense_check() {
	const check = document.getElementById("sense_check");
	const title = document.getElementById("sense-title");
	const base = document.getElementById('sense-base');
	const entry = document.getElementById("sense-entry");

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

function sense_base() {
	const field = document.getElementById('sense_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("sense-entry");

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

function sense_sense() {

	const select = 'sense_sense';
	const fill = 'sense_subsense';

	subsense_select(select, fill)
}

function sense_skill() {
	const field_field = document.getElementById("sense_skill");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("sense-skill-req")

	if (field != '') {
		div.style.opacity = "100%"	
	} else {
		div.style.opacity = "0%";
	}
}

function sense_type() {
	const field_field = document.getElementById("sense_type");
	const field = field_field.options[field_field.selectedIndex].value;

	const hei = document.getElementById("sense-height");
	const res = document.getElementById("sense-resist");

	if (field == 'height') {
		hei.style.display = "grid";
		hei.style.maxHeight = hei.scrollHeight + "px";
		res.style.display = "none";
		res.style.maxHeight = "0px";
	} else if (field == 'resist') {
		res.style.display = "grid";
		res.style.maxHeight = res.scrollHeight + "px";
		hei.style.display = "none";
		hei.style.maxHeight = "0px";
	} else {
		hei.style.display = "none";
		hei.style.maxHeight = "0px";
		res.style.display = "none";
		res.style.maxHeight = "0px";
	}
}

function sense_height_trait() {
	const select = 'sense_height_trait_type';
	const fill = 'sense_height_trait';

	trait_select(select, fill)
}

function sense_resist_trait() {
	const select = 'sense_resist_trait_type';
	const fill = 'sense_resist_trait';

	trait_select(select, fill)
}

function sense_power_req() {
	const check = document.getElementById("sense_height_power_req");
	const div = document.getElementById("sense-height-ensense");

	if (check.checked == true) {
		div.style.opacity = "100%";
	} else {
		div.style.opacity = "0%";
	}
}

function sense_resist_immune() {
	const check = document.getElementById("sense_resist_immune")
	const div = document.getElementById("sense-resist-immune-perm")

	if (check.checked == true) {
		div.style.opacity = "100%";
	} else {
		div.style.opacity = "0%";
	}
}

function sense_dark() {
	const check = document.getElementById("sense_dark")
	const lig = document.getElementById("sense-lighting");
	const hea = document.getElementById("sense-lighting-head");

	if (check.checked == true) {
		lig.style.opacity = "100%"
		hea.style.opacity = "100%"
	} else {
		lig.style.opacity = "0%"
		hea.style.opacity = "0%"
	}
}

function sense_time_set() {
	const field_field = document.getElementById("sense_time_set");
	const field = field_field.options[field_field.selectedIndex].value
	const val = document.getElementById("sense-time-value");
	const ski = document.getElementById("sense-time-skill");
	const bon = document.getElementById("sense-time-bonus");

	if (field == 'value') {
		val.style.display = "grid";
		val.style.maxHeight = val.scrollHeight + "px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";	
	} else if (field == 'skill') {
		ski.style.display = "grid";
		ski.style.maxHeight = ski.scrollHeight + "px";		
		val.style.display = "none";
		val.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";
	} else if (field == 'bonus') {
		bon.style.display = "grid";
		bon.style.maxHeight = bon.scrollHeight + "px";		
		val.style.display = "none";
		val.style.maxHeight = "0px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";	
	} else {
		val.style.display = "none";
		val.style.maxHeight = "0px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";
	}
}

function sense_time() {
	const check = document.getElementById("sense_time");
	const div = document.getElementById("sense-time");
	const sen = document.getElementById("power-sense");
	
	if (check.checked == true) {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
		sen.style.maxHeight = div.scrollHeight + sen.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px";
	}
}

function sense_ranged() {
	const check = document.getElementById("sense_ranged");
	const div = document.getElementById("sense-distance");
	const sen = document.getElementById("power-sense");

	if (check.checked == true) {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
		sen.style.maxHeight = div.scrollHeight + sen.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px";
	}
}

function sense_distance() {
	const field_field = document.getElementById("sense_distance")
	const field = field_field.options[field_field.selectedIndex].value;
	const val = document.getElementById("sense-distance-values")
	const fac = document.getElementById("sense-distance-factor")

	if (field == 'flat') {
		val.style.opacity = "100%";
		fac.style.opacity = "0%";
	} else if (field == 'rank') {
		val.style.opacity = "100%";
		fac.style.opacity = "100%";
	} else {
		val.style.opacity = "0%";
		fac.style.opacity = "0%";
	}
}