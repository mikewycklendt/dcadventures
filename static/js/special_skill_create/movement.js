function movement_check() {
	const movement_check = document.getElementById("movement_check");
	const move_entry = document.getElementById("move-entry");
	const title = document.getElementById("move-title");
	
	if (movement_check.checked == true) {
		move_entry.style.display = "grid";
		move_entry.style.padding = "1%";
		move_entry.style.maxHeight = move_entry.scrollHeight + "px";
		move_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		move_entry.style.maxHeight = "0px";
		move_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}



