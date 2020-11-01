function range_type() {
	const range_field = document.getElementById("range");
	let	range = range_field.options[range_field.selectedIndex].value;
	const power_range = document.getElementById("power-range");

	if (range == 'rank') {
		power_range.style.display = "grid";
		power_range.style.opacity = "100%"
		power_range.style.padding = "1%";
		power_range.style.maxHeight = power_range.scrollHeight + "px";
		power_range.style.padding = "1%";
	} else {
		power_range.style.maxHeight = "0px";
		power_range.style.padding = "0px";
		power_range.style.opacity = "0%";
	}
}

function power_type() {
	const move = document.getElementById('power-move');
	const sense = document.getElementById('power-sense');
	const field_field = document.getElementById('type');
	const field = field_field.options[field_field.selectedIndex].value;

	if (field == 'move') {
		move.style.display = "grid";
		move.style.opacity = "100%";
		move.style.maxHeight = move.scrollHeight + "px";
		move.style.padding = "1%";
		sense.style.maxHeight = "0px";
		sense.style.padding = "0%"
		sense.style.opacity = "0%";
	} else if (field == 'sense') {
		sense.style.display = "grid";
		sense.style.opacity = "100%";
		sense.style.maxHeight = sense.scrollHeight + "px";
		sense.style.padding = "1%";
		move.style.maxHeight = "0px";
		move.style.padding = "0%"
		move.style.opacity = "0%";
	} else {
		move.style.maxHeight = "0px";
		move.style.padding = "0%"
		move.style.opacity = "0%";
		sense.style.maxHeight = "0px";
		sense.style.padding = "0%"
		sense.style.opacity = "0%";
	}
}

function circ() {
	const range_field = document.getElementById("circ");
	let	range = range_field.options[range_field.selectedIndex].value;
	const power_range = document.getElementById("power-circ");

	if (range == 'rank') {
		power_range.style.display = "grid";
		power_range.style.opacity = "100%"
		power_range.style.padding = "1%";
		power_range.style.maxHeight = power_range.scrollHeight + "px";
		power_range.style.padding = "1%";
	} else {
		power_range.style.maxHeight = "0px";
		power_range.style.padding = "0px";
		power_range.style.opacity = "0%";
	}
}

function power_dc_type() {
	const type_field = document.getElementById("power_dc_type");
	const type = type_field.options[type_field.selectedIndex].value;
	const mod = document.getElementById("power-dc-mod");

	if (type == 'mod') {
		mod.style.opacity = "100%";
	} else {
		mod.style.opacity  = "0%"
	}
}

function skill() {
	const type_field = document.getElementById("skill");
	const type = type_field.options[type_field.selectedIndex].value;
	const mod = document.getElementById("skill-grid");

	if (type == 'mod') {
		mod.style.opacity = "100%";
	} else {
		mod.style.opacity  = "0%"
	}
}

function categorized() {
	const check = document.getElementById("categorized");
	const div = document.getElementById("category")

	if (check.checked == true) {
		div.style.display = "grid";
		div.style.opacity = "100%";
		div.style.maxHeight = div.scrollHeight + "px";
		div.style.padding = "1%";
	} else {
		div.style.maxHeight = "0px";
		div.style.padding = "0%"
		div.style.opacity = "0%";
	}
}

function movement() {
	const field_field = document.getElementById("action");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("power-move")

	if (field == 2) {
		div.style.display = "grid";
		div.style.opacity = "100%";
		div.style.maxHeight = div.scrollHeight + "px";
		div.style.padding = "1%";
	} else {
		div.style.maxHeight = "0px";
		div.style.padding = "0%"
		div.style.opacity = "0%";
	}
}


function ranks() {
	const field_field = document.getElementById("cost");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("ranks")

	if (field == 'table') {
		div.style.display = "grid";
		div.style.opacity = "100%";
		div.style.maxHeight = div.scrollHeight + "px";
		div.style.padding = "1%";
	} else {
		div.style.maxHeight = "0px";
		div.style.padding = "0%"
		div.style.opacity = "0%";
	}	
}

function senses() {
	const sense = document.getElementById('power-sense');
	const field = document.getElementById('senses');

	if (field.checked == true) {
		sense.style.display = "grid";
		sense.style.opacity = "100%";
		sense.style.maxHeight = sense.scrollHeight + "px";
		sense.style.padding = "1%";
	} else {
		sense.style.maxHeight = "0px";
		sense.style.padding = "0%"
		sense.style.opacity = "0%";
	}
}

function creates() {
	const check = document.getElementById("creates");
	const div = document.getElementById("creates-mat");

	if (check.checked == true) {
		div.style.opacity = "100%"
	} else {
		div.style.opacity = "0%"
	}
}