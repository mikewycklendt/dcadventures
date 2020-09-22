function movement_check() {
	const movement_check = document.getElementById("movement_check");
	const move_entry = document.getElementById("move-entry");
	
	if (movement_check.checked == true) {
		move_entry.style.display = "grid";
		move_entry.style.padding = "1%";
		move_entry.style.maxHeight = other_entry.scrollHeight + "px";
		move_entry.style.padding = "1%";
	} else {
		move_entry.style.maxHeight = "0px";
		move_entry.style.padding = "0px";
	}
}