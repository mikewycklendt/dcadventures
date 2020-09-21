function other_check() {
	const other_check = document.getElementById("other_check");
	const other_entry = document.getElementById("other-entry");
	
	if (other_check.checked == true) {
		other_entry.style.display = "grid"
	} else {
		other_entry.style.display = "none"
	}
}