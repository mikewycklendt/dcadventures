function degree_check() {
	const degree_check = document.getElementById("degree_check");
	const degree_base_form = document.getElementById("degree-base-form");
	
	if (degree_check.checked == true) {
		degree_base_form.style.opacity = "100%";
	} else {
		degree_base_form.style.opacity = "0%";
	}
}

function degree_base() {
	const degree_type = document.getElementById("degree_type");
	const degree_target = document.getElementById("degree_target");
	degrees_target =  degree_target.options[degree_target.selectedIndex].value;
	degrees_type = degree_type.value;
	console.log(degrees_target);
	console.log(degrees_type);
	const degree_entry = document.getElementById("degree-entry");

	if (degrees_type != '' && degrees_target != '') {
		degree_entry.style.display = "grid";
		degree_entry.style.padding = "1%";
		degree_entry.style.maxHeight = degree_entry.scrollHeight + "px";
		degree_entry.style.padding = "1%";
	} else {
		degree_entry.style.maxHeight = "0px";
		degree_entry.style.padding = "0px";
	}
}