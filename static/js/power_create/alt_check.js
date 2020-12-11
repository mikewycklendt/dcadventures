function check_check() {
	const check = "check_check";
	const title = "check-title";
	const base = 'check-base';
	const entry = "check-entry";

	check_title(check, title, base, entry);
}

function check_base() {
	const field = 'check_extra';
	const entry =  "check-entry";

	base(field, entry);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	trait_select(select, fill);
}

function check_submit() {

	const extra = select("check_extra");
	const check_type = select("check_check_type");
	const mod = select("check_mod");
	const circumstance = text("check_circ");
	const when = select("check_when");
	const trait_type = select("check_trait_type");
	const trait = select("check_trait");

	const power_id = document.getElementById('power_id').value;

	const errors = 'check-err';
	const err_line = 'check-err-line';


	response = fetch('/power/alt_check/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'check_type': self.check_type,
			'mod': self.mod,
			'circumstance': self.circumstance,
			'when': self.when,
			'trait_type': self.trait_type,
			'trait': self.trait
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
