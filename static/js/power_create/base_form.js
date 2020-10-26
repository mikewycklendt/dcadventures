function range_type() {
	const range_field = document.getElementById("range");
	let	range = range_field.options[range_field.selectedIndex].value;
	const power_range = document.getElementById("power-range");

	if (range == 'rank') {
		power_range.style.display = "grid";
		power_range.style.padding = "1%";
		power_range.style.maxHeight = power_range.scrollHeight + "px";
		power_range.style.padding = "1%";
	} else {
		power_range.style.maxHeight = "0px";
		power_range.style.padding = "0px";
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