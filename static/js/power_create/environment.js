function env_check() {
	const check = document.getElementById("env_check");
	const title = document.getElementById("env-title");
	const base = document.getElementById('env-base')

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

function env_base() {
	const field = document.getElementById('env_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("env-entry")

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

function env_temp() {
	const check = document.getElementById('env_temp');
	const div = document.getElementById('env-temp')
	const entry = document.getElementById("env-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function env_impede() {
	const check = document.getElementById('env_impede');
	const div = document.getElementById('env-move')
	const entry = document.getElementById("env-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function env_conceal() {
	const check = document.getElementById('env_conceal');
	const div = document.getElementById('env-conceal')
	const entry = document.getElementById("env-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function env_visibility() {
	const check = document.getElementById('env_visibility');
	const div = document.getElementById('env-visibility')
	const entry = document.getElementById("env-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function env_move_other() {
	const field = document.getElementById('env_move_other');
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById('env-move-other');

	if (value == 'other') {
		div.style.opacity = '100%';
	} else  {
		div.style.opacity = '0%';
	}
}


function env_visibility_trait_type() {
	const select = 'env_visibility_trait_type'
	const fill = 'env_visibility_trait'
	
	trait_select(select, fill)
}
