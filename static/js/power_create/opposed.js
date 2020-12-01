function opposed_check() {
	const check = document.getElementById("opposed_check");
	const title = document.getElementById("opposed-title");
	const base = document.getElementById('opposed-base');
	const entry = document.getElementById("opposed-entry");

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

function opposed_base() {
	const field = document.getElementById('opposed_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("opposed-entry");

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

function opposed_trait_type() {
	const select = 'opposed_trait_type'
	const fill = 'opposed_trait'

	trait_select(select, fill)
}


function opposed_opponent_trait_type() {
	const select = 'opposed_opponent_trait_type'
	const fill = 'opposed_opponent_trait'

	trait_select(select, fill)
}