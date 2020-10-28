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

