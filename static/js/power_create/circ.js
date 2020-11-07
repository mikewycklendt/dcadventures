function circ_check() {
	const check = document.getElementById("circ_check");
	const title = document.getElementById("circ-title");
	const base = document.getElementById('circ-base')

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

function circ_base() {
	const field = document.getElementById('circ_extra')
	const value = field.options[field.selectedIndex].value;
	
	const field2 = document.getElementById('circ_target')
	const target = field2.options[field2.selectedIndex].value;
	const entry = document.getElementById("circ-entry")

	if (value != '' && target != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}

function circ_type() {
	const field = document.getElementById('circ_type');
	const value = field.options[field.selectedIndex].value;
	const ran = document.getElementById('circ-range');
	const entry = document.getElementById('circ-entry')

	if (value == 'range') {
		ran.style.display = 'grid';
		ran.style.maxHeight = ran.scrollHeight + 'px';
		entry.style.maxHeight = ran.scrollHeight + entry.scrollHeight + 'px';
	} else {
		ran.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - ran.scrollHeight;
	}
}