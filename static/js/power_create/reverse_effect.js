function reverse_check() {
	const check = "reverse_check";
	const base = "reverse-base";
	const title = "reverse-title";
	const entry = "reverse-entry";

	check_title(check, title, base, entry);
}

function reverse_base() {
	const target_field = "reverse_target";
	const extra_field = 'reverse_extra';
	const entry = "reverse-entry";


	base_two(target_field, extra_field, entry);
}

function reverse_check_check() {
	const check = document.getElementById("reverse_check_check");
	const field = document.getElementById("reverse-check")
	const entry = document.getElementById("reverse-entry")

	check_drop(check, field, entry);
}

function reverse_time_check() {
	const check = document.getElementById("reverse_time_check");
	const field = document.getElementById("reverse-time")
	const entry = document.getElementById("reverse-entry")

	check_drop(check, field, entry);
}

function reverse_trait_type() {
	const select = 'reverse_trait_type';
	const fill = 'reverse_trait';

	trait_select(select, fill);
}

function reverse_value_type() {
	const type_field = "reverse_value_type";	
	const val = "reverse-check-value";
	const math = "reverse-check-math";

	value_type(type_field, math, val);
}