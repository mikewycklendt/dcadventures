function resistance_check() {
	const deg_mod_check = "resistance_check";
	const deg_mod_base_form = "resistance-base";
	const title = "resistance-title";
	const entry = "resistance-entry";

	check_title(deg_mod_check, title, deg_mod_base_form, entry);
}

function resistance_base() {
	const target_field = "resistance_target";
	const extra_field = 'resistance_extra';
	const entry = "resistance-entry";

	base_two(target_field, extra_field, entry);
}

function resistance_trait_type() {
	const select = 'resistance_trait_type'
	const fill = 'resistance_trait'

	trait_select(select, fill)
}

function resistance_check_type() {
	const field = 'resistance_check_type';
	const options = [{'val': 'descriptor', 'div': 'resistance-descriptor'},
					{'val': 'trait', 'div': 'resistance-trait'}];

	select_opacity(field, options);
}

function resistance_check_trait_type() {
	const select = 'resistance_check_trait_type';
	const fill = 'resistance_check_trait';

	trait_select(select, fill);
}

function resistance_requires_check() {
	const check = 'resistance_requires_check';
	const div = 'resistance-check';

	check_opacity(check, div);
}