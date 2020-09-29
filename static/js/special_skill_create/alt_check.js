function alt_check() {
	const alt_check = document.getElementById("alt_check_check");
	const alt_entry = document.getElementById("alt-check-entry");
	
	if (alt_check.checked == true) {
		alt_entry.style.display = "grid";
		alt_entry.style.padding = "1%";
		alt_entry.style.maxHeight = alt_entry.scrollHeight + "px";
		alt_entry.style.padding = "1%";
	} else {
		alt_entry.style.maxHeight = "0px";
		alt_entry.style.padding = "0px";
	}
}

function check_type() {
	const check_field = document.getElementById('check');
	let check_value = check_field.options[check_field.selectedIndex].value;

	alt_check = document.getElementById('alt-check');

	if (check_value != 1) {
		alt_check.style.display = 'grid';
	}

}