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

let resistance_grid = {'titles': false,
					'columns': []}

function resistance() {

	const columns = resistance_grid.columns;

	const target = select("resistance_target");
	const extra_id = select("resistance_extra");
	const mod = select("resistance_mod");
	const rounds = select("resistance_rounds");
	const circumstance = text("resistance_circ");
	const resist_check_type = select("resistance_resist_check_type");
	const trait_type = select("resistance_trait_type");
	const trait = select("resistance_trait");
	const descriptor = select("resistance_descriptor");
	const requires_check = check("resistance_requires_check");
	const check_type = select("resistance_check_type");
	const check_trait_type = select("resistance_check_trait_type");
	const check_trait = select("resistance_check_trait");

	const power_id = document.getElementById('power_id').value;
	
	const errors = 'resistance-err';
	const err_line = 'resistance-err-line';

	response = fetch('/power/resist/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'mod': mod,
			'rounds': rounds,
			'circumstance': circumstance,
			'resist_check_type': resist_check_type,
			'trait_type': trait_type,
			'trait': trait,
			'descriptor': descriptor,
			'requires_check': requires_check,
			'check_type': check_type,
			'check_trait_type': check_trait_type,
			'check_trait': check_trait,
			'columns': columns
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