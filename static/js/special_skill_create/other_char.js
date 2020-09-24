function char_check() {
	const char_check = document.getElementById("char_check");
	const char_base_form = document.getElementById("char-base-form");
	
	if (char_check.checked == true) {
		char_base_form.style.opacity = "100%";
	} else {
		char_base_form.style.opacity = "0%";
	}
}

function char_base() {
	const char_type = document.getElementById("char_type");
	const char_target = document.getElementById("char_target");
	let chartype = circ_skill.options[char_type.selectedIndex].value;
	let chartarget =  char_target.options[char_target.selectedIndex].value;
	console.log(chartype);
	console.log(chartarget);
	const char_entry = document.getElementById("char-entry");

	if (chartype != '' && chartarget != '') {
		char_entry.style.display = "grid";
		char_entry.style.padding = "1%";
		char_entry.style.maxHeight = char_entry.scrollHeight + "px";
		char_entry.style.padding = "1%";
	} else {
		char_entry.style.maxHeight = "0px";
		char_entry.style.padding = "0px";
	}
}