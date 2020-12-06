function time_check() {
	const check = "time_check";
	const title = "time-title";
	const base = 'time-base';
	const entry = "time-entry";

	check_title(check, title, base, entry);
}

function time_base() {
	const field = 'time_extra';
	const entry = "time-entry";

	base(field, entry);
}

function time_trait_type() {
	const select = 'time_trait_type'
	const fill = 'time_trait'

	trait_select(select, fill)
}

function time_value_type() {
	const select = 'time_value_type';
	const math = 'time-math';
	const value = 'time-value';

	value_type(select, math, value)
}

function time_recovery() {
	const check = 'time_recovery';
	const div = 'time-recovery';
	const entry = 'time-entry';

	check_drop(check, div, entry);
}