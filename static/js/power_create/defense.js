function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	check_title(check, title, base, entry);
}

function defense_base() {
	const field = 'defense_extra';
	const entry = "defense-entry";

	base(field, entry);
}

function defense_reflect() {
	const check = 'defense_reflect';
	const base = 'defense-reflect-action';

	check_opacity(check, base);
}

function defense_immunity() {
	const check = 'char_immunity';
	const div = 'char-immunity';

	check_drop(check, div, entry);
}

function defense_immunity_trait_type() {
	const select = 'char_immunity_trait_type';
	const fill = 'char_immunity_trait';

	trait_select(select, fill);
}
