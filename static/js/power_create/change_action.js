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

let action_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function action_submit() {

	const columns = action_grid.columns;
	const created = action_grid.titles;
	const font = action_grid.font;

	const extra_id = select("action_extra");
	const action = select("action_change");
	const mod = select("action_mod");
	const objects = check("mod_objects");
	const circumstance = text("action_circ");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'action-err';
	const err_line = 'action-err-line';

	response = fetch('/power/change_action/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'action': action,
			'mod': mod,
			'objects': objects,
			'circumstance': circumstance,
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
			
			action_grid.columns.length = 0;
			action_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, action_grid, route);
			clear_errors(err_line, errors)

			action_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}