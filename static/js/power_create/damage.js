function damage_check() {
	const check = "damage_check";
	const title = "damage-title";
	const base = 'damage-base';
	const entry = "damage-entry";

	check_title(check, title, base, entry);
}

function damage_base() {
	const field = 'damage_extra';
	const entry = "damage-entry";

	base(field, entry);
}

function dam_trait_type() {
	const select = 'dam_trait_type'
	const fill = 'dam_trait'

	trait_select(select, fill)
}

let damage_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function damage_submit() {

	const columns = damage_grid.columns;
	const created = damage_grid.titles;
	const font = damage_grid.font;

	const extra_id = select("damage_extra")
	const trait_type = select("dam_trait_type");
	const trait = select("dam_trait");
	const mod = select("dam_mod");
	const strength = check("dam_strength");
	const damage_type = select("damage_damage_type");
	const descriptor = select("damage_descriptor");

	const power_id = document.getElementById('power_id').value;

	const errors = 'damage-err';
	const err_line = 'damage-err-line';

	response = fetch('/power/damage/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'trait_type': trait_type,
			'trait': trait,
			'mod': mod,
			'strength': strength,
			'damage_type': damage_type,
			'descriptor': descriptor,
			'columns': columns,
			'created': created,
			'font': font
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			damage_grid.columns = jsonResponse.columns;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, damage_grid, route);
			clear_errors(err_line, errors)

			damage_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}