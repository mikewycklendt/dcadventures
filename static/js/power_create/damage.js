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
	descriptor_base(field);
}

function dam_trait_type() {
	const select = 'dam_trait_type'
	const fill = 'dam_trait'

	id_select(select, fill, trait_select);
}

function dam_trait() {
	const filter = select('dam_trait_type');
	const fill = 'dam_trait';

	id_select(fill, fill, trait_filter, filter);
}

function dam_strength() {
	const check = 'dam_strength';
	const div = 'dam-strength';

	check_opacity(check, div);
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
	const strength_based = select("dam_strength_based")
	const damage_type = multiple("damage_damage_type");
	const descriptor = multiple("damage_descriptor");
	const keyword = text("damage_keyword")
	const value_type = select("dam_value_type");
	const math = select("dam_math")
	const check = select("damage_check");
	const check_type = select("damage_check_type");
	const applied = select("damage_applied");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'damage-err';
	const err_line = 'damage-err-line';
	const selects = 'damage-sml';

	response = fetch('/power/damage/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'trait_type': trait_type,
			'trait': trait,
			'mod': mod,
			'strength': strength,
			'strength_based': strength_based,
			'damage_type': damage_type,
			'descriptor': descriptor,
			'columns': columns,
			'created': created,
			'font': font,
			'keyword': keyword,
			'value_type': value_type,
			'math': math,
			'check': check,
			'check_type': check_type,
			'applied': applied
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const id = jsonResponse.id;

			selects_add(id, keyword, selects);
			
			damage_grid.columns.length = 0;
			damage_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, damage_grid, route, [selects]);
			clear_errors(err_line, errors)

			damage_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}