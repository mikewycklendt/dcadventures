function levels_check() {
	const levels_check = "levels_check";
	const levels_base_form = "levels-base-form";
	const title = "levels-title";
	const entry = "levels-entry";

	check_title(levels_check, title, levels_base_form, entry);
}

function levels_base() {
	const type = "level_type";
	const extra_field = 'levels_extra';
	const entry = "levels-entry";

	base_text(extra_field, type, entry);
}


let bonus_level = true;

function levels_submit() {

	const level_type = text("level_type");
	const extra = select("levels_extra");
	const level = text("level");
	const level_effect = text("level_effect");

};
