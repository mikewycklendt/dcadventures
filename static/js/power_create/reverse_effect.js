function reverse_check() {
	const check = document.getElementById("reverse_check");
	const base = document.getElementById("reverse-base");
	const title = document.getElementById("reverse-title");

	if (check.checked == true) {
		base.style.opacity = "100%"
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = "0%"
		title.style.color = "#245681";
	}
}

function reverse_base() {
	const target_field = document.getElementById("reverse_target");
	const target = target_field.options[target_field.selectedIndex].value;
	const entry = document.getElementById("reverse-entry")

	if (target != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}
