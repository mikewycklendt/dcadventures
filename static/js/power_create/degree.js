function degree_check() {
	const check = document.getElementById("degree_check");
	const title = document.getElementById("degree-title");
	const base = document.getElementById('degree-base');
	const entry = document.getElementById("degree-entry");

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "165%";
		setTimeout(function(){title.style.fontSize = "160%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function degree_base() {
	const field = document.getElementById('degree_extra');
	const value = field.options[field.selectedIndex].value;
	const type = document.getElementById('degree_type').value;
	const entry = document.getElementById("degree-entry");

	if (value != '' && type != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}