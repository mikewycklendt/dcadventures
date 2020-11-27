function env_check() {
	const check = document.getElementById("env_check");
	const title = document.getElementById("env-title");
	const base = document.getElementById('env-base');
	const entry = document.getElementById("env-entry");

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

function env_base() {
	const field = document.getElementById('env_extra');
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("env-entry");

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

function env_condition() {
	const check = 'env_condition';
	const div = 'env-condition';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_impede() {
	const check = 'env_impede';
	const div = 'env-move';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_conceal() {
	const check = 'env_conceal';
	const div = 'env-conceal';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_visibility() {
	const check = 'env_visibility';
	const div = 'env-visibility';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_move_other() {
	const field = document.getElementById('env_move_nature');
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

function env_immune() {
	const check = 'env_immune';
	const div = 'env-immune'

	check_display(check, div)
}