function defense_check() {
	const check = document.getElementById("defense_check");
	const title = document.getElementById("defense-title");
	const base = document.getElementById('defense-base')

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
	}
}

function defense_base() {
	const field = document.getElementById('defense_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("defense-entry")

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}
