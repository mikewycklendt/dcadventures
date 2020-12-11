function minion_check() {
	const check = "minion_check";
	const title = "minion-title";
	const base = 'minion-base';
	const entry = "minion-entry";

	check_title(check, title, base, entry);
}

function minion_base() {
	const field = 'minion_extra';
	const entry = "minion-entry";

	base(field, entry);
}

function minion_multiple() {
	const check = 'minion_multiple'
	const div = 'minion-multiple';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_attitude() {
	const check = 'minion_attitude';
	const div = 'minion-attitude';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_resitable() {
	const check = 'minion_resitable';
	const div = 'minion-resitable';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_sacrifice() {
	const check = 'minion_sacrifice';
	const div = 'minion-sacrifice';

	check_display(check, div);
}

function minion_attitude_trait_type() {
	const select = 'minion_attitude_trait_type';
	const fill = 'minion_attitude_trait';

	trait_select(select, fill);
}

function minion_submit() {

	const extra = select("minion_extra");
	const points = select("mod_minion_points");
	const condition = select("mod_minion_condition");
	const player_condition = select("mod_minion_player_condition");
	const link = check("mod_minion_link");
	const variable_type = select("mod_minion_variable_type");
	const multiple = check("minion_multiple");
	const attitude = check("minion_attitude");
	const resitable = check("minion_resitable");
	const heroic = check("minion_heroic");
	const sacrifice = check("minion_sacrifice");
	const sacrifice_cost = select("mod_minion_sacrifice_cost");
	const attitude_type = select("minion_attitude_type");
	const attitude_trait_type = select("minion_attitude_trait_type");
	const attitude_trait = select("minion_attitude_trait");
	const resitable_check = select("minion_resitable_check");
	const resitable_dc = select("minion_resitable_dc");
	const multiple_value = select("mod_minion_multiple_value");
	const horde = check("mod_minion_horde");

	const power_id = document.getElementById('power_id').value;

	const errors = 'minion-err';
	const err_line = 'minion-err-line';

	response = fetch('/power/minion/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'points': self.points,
			'condition': self.condition,
			'player_condition': self.player_condition,
			'link': self.link,
			'variable_type': self.variable_type,
			'multiple': self.multiple,
			'attitude': self.attitude,
			'resitable': self.resitable,
			'heroic': self.heroic,
			'sacrifice': self.sacrifice,
			'sacrifice_cost': self.sacrifice_cost,
			'attitude_type': self.attitude_type,
			'attitude_trait_type': self.attitude_trait_type,
			'attitude_trait': self.attitude_trait,
			'resitable_check': self.resitable_check,
			'resitable_dc': self.resitable_dc,
			'multiple_value': self.multiple_value,
			'horde': self.horde
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