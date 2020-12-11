function degree_check() {
	const check = "degree_check";
	const title = "degree-title";
	const base = 'degree-base';
	const entry = "degree-entry";

	check_title_small(check, title, base, entry);
}

function degree_base() {
	const field = 'degree_extra';
	const type = 'degree_type';
	const entry = "degree-entry";

	base_text(field, type, entry);
}

function degree_submit() {
	
	const degree_type = text("degree_type");
	const extra = select("degree_extra");
	const degree = select("degree_degree");
	const keyword = text("degree_keyword");
	const desscription = text("degree_desscription");
	const extra_effort = check("mod_extra_effort");
	const cumulative = check("mod_cumulative");
	const target = select("degree_target");

	const power_id = document.getElementById('power_id').value;

	const errors = 'degree-err';
	const err_line = 'degree-err-line';

	response = fetch('/power/degree/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'degree_type': self.degree_type,
			'degree': self.degree,
			'keyword': self.keyword,
			'desscription': self.desscription,
			'extra_effort': self.extra_effort,
			'cumulative': self.cumulative,
			'target': self.target
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