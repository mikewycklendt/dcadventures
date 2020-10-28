function move_perm() {
	const field_field = document.getElementById("move_perm");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("move-time");

	if (field == 'temp') {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
	} else {
		div.style.display = "none";
		div.style.maxHeight = "0px"
	}

}