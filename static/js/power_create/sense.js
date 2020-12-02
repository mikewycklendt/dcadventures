function sense_check() {
	const check = "sense_check";
	const title = "sense-title";
	const base = 'sense-base';
	const entry = "sense-entry";

	check_title(check, title, base, entry);
}

function sense_base() {
	const field = 'sense_extra';
	const field2 = 'sense_target';
	const entry = "sense-entry";

	base_two(field, field2, entry);
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

	const hei = "sense-height";
	const res = "sense-resist";

	if (field == 'height') {
		hide_maxheight(res);
		show_maxheight(hei);
	} else if (field == 'resist') {
		hide_maxheight(hei);
		show_maxheight(res);
	} else {
		hide_maxheight(hei);
		hide_maxheight(res);
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
	const check = "sense_height_power_req";
	const div = "sense-height-ensense";

	check_opacity(check, div);
}

function sense_resist_immune() {
	const check = "sense_resist_immune";
	const div = "sense-resist-immune-perm";

	check_opacity(check, div);
}

function sense_dark() {
	const check = "sense_dark";
	const lig = "sense-lighting";

	check_opacity(check, lig);
}

function sense_time_set() {
	const field_field = document.getElementById("sense_time_set");
	const field = field_field.options[field_field.selectedIndex].value
	const val = "sense-time-value";
	const ski = "sense-time-skill";
	const bon = "sense-time-bonus";

	if (field == 'value') {
		hide_maxheight(ski);
		hide_maxheight(bon);
		show_maxheight(val);
	} else if (field == 'skill') {
		hide_maxheight(val);
		hide_maxheight(bon);
		show_maxheight(ski);
	} else if (field == 'bonus') {
		hide_maxheight(val);
		hide_maxheight(ski);
		show_maxheight(bon);	
	} else {
		hide_maxheight(val);
		hide_maxheight(ski);
		hide_maxheight(bon);
	}
}

function sense_time() {
	const check = "sense_time";
	const div = "sense-time";
	const sen = "sense-entry";

	check_drop(check, div, sen)
}

function sense_ranged() {
	const check = "sense_ranged";
	const div = "sense-distance";
	const sen = "sense-entry";

	check_drop(check, div, sen)
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