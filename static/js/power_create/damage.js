function damage_check() {
	const check = document.getElementById("damage_check");
	const entry = document.getElementById("damage-entry")
	const title = document.getElementById("damage-title");

	if (check.checked == true) {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}
