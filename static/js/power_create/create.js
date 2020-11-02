function create_check() {
	const check = document.getElementById("create_check");
	const base = document.getElementById("create-base");
	const title = document.getElementById("create-title");

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

function create_base() {
	const field_field = document.getElementById("create_rank");
	const field = field_field.options[field_field.selectedIndex].value;
	const entry = document.getElementById("create-entry")

	if (field != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}