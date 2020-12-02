function env_check() {
	const check = "env_check";
	const title = "env-title";
	const base = 'env-base';
	const entry = "env-entry";

	check_title(check, title, base, entry);
}

function env_base() {
	const field = 'env_extra';
	const entry = "env-entry";

	base(field, entry);
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