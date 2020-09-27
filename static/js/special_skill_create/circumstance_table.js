function circ_check() {
	const circ_check = document.getElementById("circ_check");
	const circ_base_form = document.getElementById("circ-base-form");
	
	if (circ_check.checked == true) {
		circ_base_form.style.opacity = "100%";
	} else {
		circ_base_form.style.opacity = "0%";
	}
}

function circ_base() {
	const circ_skill = document.getElementById("circ_skill");
	const circ_target = document.getElementById("circ_target");
	circskill = circ_skill.options[circ_skill.selectedIndex].value;
	circtarget =  circ_target.options[circ_target.selectedIndex].value;
	console.log(circskill);
	console.log(circtarget);
	const circ_entry = document.getElementById("circ-entry");

	if (circskill != '' && circtarget != '') {
		circ_entry.style.display = "grid";
		circ_entry.style.padding = "1%";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		circ_entry.style.padding = "1%";
	} else {
		circ_entry.style.maxHeight = "0px";
		circ_entry.style.padding = "0px";
	}
}


function circ_mod() {
	let circ_mod_type_field = document.getElementById('circ_mod_type');
	let circ_mod_type_value =  circ_mod_type_field.options[circ_mod_type_field.selectedIndex].value;
	let mod_field = document.getElementById('circ-mod-field');
	const value_field = document.getElementById('circ-mod-value');
	const math_field = document.getElementById('circ-mod-math');
	const adjust_field = document.getElementById('circ-mod-adjust');
	const circ_entry = document.getElementById("circ-entry");


	if (circ_mod_type_value = 'value') {
		value_field.style.display = "grid";
		value_field.style.padding = "1%";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		math_field.style.display = "none";
		adjust_field.style.display = "none"
	} else if (circ_mod_type_value = 'math') {
		math_field.style.display = "grid";
		math_field.style.padding = "1%";
		math_field.style.maxHeight = math_field.scrollHeight + "px";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		value_field.style.display = "none";
		adjust_field.style.display = "none"
	} else if (circ_mod_type_value = 'Adjust') {
		adjust_field.style.display = "grid";
		adjust_field.style.padding = "1%";
		adjust_field.style.maxHeight = adj.scrollHeight + "px";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		value_field.style.display = "none";
		math_field.style.display = "none"
	} else if (circ_mod_type_value = 'No equipment') {
		value_field.style.display = "grid";
		value_field.style.padding = "1%";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		adjust_field.style.display = "none"
	} else {
		math_field.style.display = "none";
		value_field.style.display = "none";
		adjust_field.style.display = "none"
	}

};