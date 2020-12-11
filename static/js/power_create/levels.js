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

	const power_id = document.getElementById('power_id').value;

	const errors = 'level-err';
	const err_line = 'level-err-line';

	response = fetch('/power/levels/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'level_type': self.level_type,
			'level': self.level,
			'level_effect': self.level_effect
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
};
