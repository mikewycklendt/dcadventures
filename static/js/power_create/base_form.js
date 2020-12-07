function range_type() {
	const range_field = document.getElementById("range");
	let	range = range_field.options[range_field.selectedIndex].value;
	const power_range = document.getElementById("ranged-entry");
	const check = document.getElementById('ranged_check');

	if (range == 'rank') {
		check.checked = true;
		power_range.style.display = "grid";
		power_range.style.opacity = "100%"
		power_range.style.padding = "1%";
		power_range.style.maxHeight = power_range.scrollHeight + "px";
		power_range.style.padding = "1%";
	} else {
		power_range.style.maxHeight = "0px";
		power_range.style.padding = "0px";
		power_range.style.opacity = "0%";
		check.checked = false;
		setTimeout(function(){power_range.style.display = 'none'}, 400);
	}
}

function power_type() {
	const sense = document.getElementById("sense-entry");
	const sense_check = document.getElementById("sense_check");
	const sense_base = document.getElementById('sense_base');
	const move_base = document.getElementById('move_base');
	const move = document.getElementById("move-entry");
	const move_check = document.getElementById('move_check')
	const field_field = document.getElementById('type');
	const field = field_field.options[field_field.selectedIndex].value;

	sense_base.style.opacity = '0%';
	move_base.style.opacity = '0%';

	if (field == 'sense') {
		sense_base.style.opacity = '100%';
		move_base.style.opacity = '0%';
		sense.style.display = "grid";
		sense.style.maxHeight = sense.scrollHeight + "px";
		sense_check.checked = true;
		move_check.checked = false;
		move.style.maxHeight = "0px";
		setTimeout(function(){move.style.display = 'none'}, 400);
	} else if (field == 'move') {
		sense_base.style.opacity = '0%';
		move_base.style.opacity = '100%';
		move.style.display = "grid";
		move.style.maxHeight = move.scrollHeight + "px";
		move_check.checked = true;
		sense_check.checked = false;
		sense.style.maxHeight = "0px";
		setTimeout(function(){sense.style.display = 'none'}, 400);
	} else {
		sense_base.style.opacity = '0%';
		move_base.style.opacity = '0%';
		move_check.checked = false;
		sense_check.checked = false;
		sense.style.maxHeight = "0px";
		setTimeout(function(){sense.style.display = 'none'}, 400);
		move.style.maxHeight = "0px";
		setTimeout(function(){move.style.display = 'none'}, 400);
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
	const move = document.getElementById("move-entry");

	if (field == 2) {
		move.style.display = "grid";
		move.style.maxHeight = move.scrollHeight + "px";
	} else {
		move.style.maxHeight = "0px";
		setTimeout(function(){move.style.display = 'none'}, 400);
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