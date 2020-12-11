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
	const check = "reverse_check_check";
	const field = "reverse-check";
	const entry = "reverse-entry";

	check_drop(check, field, entry);
}

function reverse_time_check() {
	const check = "reverse_time_check";
	const field = "reverse-time";
	const entry = "reverse-entry";

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

function reverse_submit() {

	const target = select("reverse_target");
	const extra = select("reverse_extra");
	const degree = select("reverse_degree");
	const when = select("reverse_when");
	const check_check = check("reverse_check_check");
	const time_check = check("reverse_time_check");
	const trait_type = select("reverse_trait_type");
	const trait = select("reverse_trait");
	const value_type = select("reverse_value_type");
	const value_dc = select("reverse_value_dc");
	const math_dc = select("reverse_math_dc");
	const math = select("reverse_math");
	const time_value = text("reverse_time");
	const time_unit = select("reverse_time_unit");

	const power_id = document.getElementById('power_id').value;

	const errors = 'reverse-err';
	const err_line = 'reverse-err-line';

	response = fetch('/power/reverse_effect/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'target': self.target,
			'degree': self.degree,
			'when': self.when,
			'check_check': self.check_check,
			'time_check': self.time_check,
			'trait_type': self.trait_type,
			'trait': self.trait,
			'value_type': self.value_type,
			'value_dc': self.value_dc,
			'math_dc': self.math_dc,
			'math': self.math,
			'time_value': self.time_value,
			'time_unit': self.time_unit
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

		} else {

		}
	})
}