function ability_check() {
	const check = "ability_check";
	const title = "ability-title";
	const base = 'ability-base';
	const entry = "ability-entry";

	entry_check(check, title, base, entry);
}

let ability_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function ability_submit() {

	const columns = ability_grid.columns;
	const created = ability_grid.titles;
	const font = ability_grid.font;

	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");
	const ability = select("ability_ability");
	const circumstance = text("ability_circumstance");

	const errors = 'ability-err';
	const err_line = 'ability-err-line';

	response = fetch('/skill/ability/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'ability': ability,
			'circumstance': circumstance
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			ability_grid.columns.length = 0;
			ability_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, ability_grid, route);
			clear_errors(err_line, errors)

			ability_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}