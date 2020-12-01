function check_check() {
	const check = document.getElementById("check_check");
	const title = document.getElementById("check-title");
	const base = document.getElementById('check-base');
	const entry = document.getElementById("check-entry");

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function check_base() {
	const field = document.getElementById('check_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("check-entry");

	if (value != '') {
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

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	trait_select(select, fill);
}