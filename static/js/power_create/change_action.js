function change_action_check() {
	const check = "change_action_check";
	const title = "action-title";
	const base = 'action-base';
	const entry = "action-entry";

	check_title(check, title, base, entry);
}

function action_base() {
	const field = 'action_extra';
	const entry = "action-entry";

	base(field, entry);
}

function action_submit() {

	const extra = select("action_extra");
	const action = select("action_change");
	const mod = select("action_mod");
	const objects = check("mod_objects");
	const circumstance = text("action_circ");

	const power_id = document.getElementById('power_id').value;

	const errors = 'action-err';
	const err_line = 'action-err-line';

	response = fetch('/power/change_action/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'action': self.action,
			'mod': self.mod,
			'objects': self.objects,
			'circumstance': self.circumstance
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