function rounds_check() {
	const rounds_check = document.getElementById("rounds_check");
	const rounds_entry = document.getElementById("rounds-entry");
	
	if (rounds_check.checked == true) {
		rounds_entry.style.display = "grid";
		rounds_entry.style.padding = "1%";
		rounds_entry.style.maxHeight = rounds_entry.scrollHeight + "px";
		rounds_entry.style.padding = "1%";
	} else {
		rounds_entry.style.maxHeight = "0px";
		rounds_entry.style.padding = "0px";
	}
}