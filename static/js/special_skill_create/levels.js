function levels_check() {
	const levels_check = document.getElementById("levels_check");
	const levels_base_form = document.getElementById("levels-base-form");
	
	if (levels_check.checked == true) {
		levels_base_form.style.opacity = "100%";
	} else {
		levels_base_form.style.opacity = "0%";
	}
}

function levels_base() {
	const level_type = document.getElementById("level_type");
	const level_dc_set = document.getElementById("levels_dc_set");
	const level_target = document.getElementById("levels_target");
	levels_dc =  level_dc_set.options[level_dc_set.selectedIndex].value;
	levels_target =  level_target.options[level_target.selectedIndex].value;
	levels_type = level_type.value;
	console.log(levels_dc);
	console.log(levels_target);
	console.log(levels_type);
	const levels_entry = document.getElementById("levels-entry");

	if (levels_type != '' && levels_target != '' && levels_dc != '') {
		levels_entry.style.display = "grid";
		levels_entry.style.padding = "1%";
		levels_entry.style.maxHeight = levels_entry.scrollHeight + "px";
		levels_entry.style.padding = "1%";
	} else {
		levels_entry.style.maxHeight = "0px";
		levels_entry.style.padding = "0px";
	}
}