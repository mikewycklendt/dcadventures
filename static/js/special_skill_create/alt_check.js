function alt_check() {
	const alt_check = document.getElementById("alt_check_check");
	const alt_entry = document.getElementById("alt-check-entry");
	
	if (alt_check.checked == true) {
		alt_entry.style.display = "grid";
		alt_entry.style.padding = "1%";
		alt_entry.style.maxHeight = other_entry.scrollHeight + "px";
		alt_entry.style.padding = "1%";
	} else {
		alt_entry.style.maxHeight = "0px";
		alt_entry.style.padding = "0px";
	}
}