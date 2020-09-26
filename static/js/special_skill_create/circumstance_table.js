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
