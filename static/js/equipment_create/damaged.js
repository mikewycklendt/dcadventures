function damaged_check() {
	const check = "damaged_check";
	const title = "damaged-title";
	const base = 'damaged-base';
	const entry = "damaged-entry";

	entry_check(check, title, base, entry);
}

function damaged_skill_type() {
	const select = 'damaged_skill_type';
	const fill = 'damaged_skill';

	skill_select(select, fill);
}

let damaged_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function damaged_submit() {

	const columns = damaged_grid.columns;
	const created = damaged_grid.titles;
	const font = damaged_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const effect = select("damaged_effect");
	const feature = select("damaged_feature");
	const damage = select("damaged_damage");
	const skill_type = select("damaged_skill_type");
	const skill = select("damaged_skill");
	const toughness = select("damaged_toughness");
	const penalty = select("damaged_penalty");

	const errors = 'damaged-err';
	const err_line = 'damaged-err-line';

	response = fetch('/equipment/damaged/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'effect': effect,
			'feature': feature,
			'damage': damage,
			'skill_type': skill_type,
			'skill': skill,
			'toughness': toughness,
			'penalty': penalty
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			damaged_grid.columns.length = 0;
			damaged_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, damaged_grid, route);
			clear_errors(err_line, errors)

			damaged_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}