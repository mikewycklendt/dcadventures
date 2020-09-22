function pre_check_check() {
	const pre_check_check = document.getElementById("pre_check_check");
	const pre_check_header_type = document.getElementById("pre-check-header-type");
	
	if (pre_check_check.checked == true) {
		pre_check_header_type.style.opacity = "100%";
	} else {
		pre_check_header_type.style.opacity = "0%";
	}
}

function pre_check_entry() {
	pre_check_type = document.getElementById("pre_check_type")
	pre_check_type_value = pre_check_type.options[pre_check_type.selectedIndex].value;
	console.log(pre_check_type_value)
	pre_check_entry_standard = document.getElementById("pre-check-entry-standard")
	pre_check_entry_opposed = document.getElementById("pre-check-entry-standard")

	if (pre_check_type_value = 'skill') {
		pre_check_entry_standard.style.display = "grid";
		pre_check_entry_standard.style.padding = "1%";
		pre_check_entry_standard.style.maxHeight = pre_check_entry_standard.scrollHeight + "px";
		pre_check_entry_standard.style.padding = "1%";
		pre_check_entry_opposed.style.display = "none";
	} else if (pre_check_type_value = 'opposed') {
		pre_check_entry_standard.style.display = "none";
		pre_check_entry_opposed.style.display = "grid";
		pre_check_entry_opposed.style.padding = "1%";
		pre_check_entry_opposed.style.maxHeight = pre_check_entry_opposed.scrollHeight + "px";
		pre_check_entry_opposed.style.padding = "1%";
	} else {
		pre_check_entry_opposed.style.display = "none";
		pre_check_entry_standard.styl.display = "none";

	}
}