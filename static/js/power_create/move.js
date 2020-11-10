const entry = 'move-entry';

function move_check() {
	const check = document.getElementById("move_check");
	const title = document.getElementById("move-title");
	const base = document.getElementById('move-base')

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
	}
}

function move_base() {
	const field = document.getElementById('move_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("move-entry")

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}

function move_ground_perm() {
	const field_field = document.getElementById("move_ground_perm");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("move-ground-time");

	if (field == 'temp') {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px"
		setTimeout(function(){div.style.display = 'none'}, 400);
	}

}

function move_ground() {
	const check = 'move_ground';
	const div = 'move-ground';

	check_drop(check, div, entry);
}

function move_subtle() {
	const check = 'move_subtle';
	const div = 'move-subtle';
	
	check_drop(check, div, entry);
}

function move_subtle_trait_type() {
	const select = 'move_subtle_trait_type';
	const fill = 'move_subtle_trait';

	trait_select(select, fill);
}

function move_distance_type() {
	const select = 'move_distance_type'
	const val = 'move-distance-value'
	const math = 'move-distance-math'
	const div = 'move-distance'

	math_div_select(select, val, math, div)
}