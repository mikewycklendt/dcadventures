function damage_check() {
	const check = document.getElementById("damage_check");
	const title = document.getElementById("damage-title");
	const base = document.getElementById('damage-base')

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

function damage_base() {
	const field = document.getElementById('damage_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("damage-entry")

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
