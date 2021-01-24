function check_check() {
	const check = "check_check";
	const title = "check-title";
	const base = 'check-base';
	const entry = "check-entry";

	entry_check(check, title, base, entry);
}

let check_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function check_submit() {

	const columns = check_grid.columns;
	const created = check_grid.titles;
	const font = check_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const effect = select("check_effect");
	const feature = select("check_feature");
	const when = select("check_when");
	const skill_type = select("check_skill_type");
	const skill = select("check_skill");
	const check_type = select("check_check_type");
	const action = select("check_action");
	const action_time = check("check_action_time");

	const errors = 'check-err';
	const err_line = 'check-err-line';

	response = fetch('/equipment/check/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
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

			check_grid.columns.length = 0;
			check_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, check_grid, route);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}