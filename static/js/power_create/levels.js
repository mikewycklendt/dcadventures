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

let levels_grid = {'titles': false,
					'columns': [],
					'font': 80}

function levels_submit() {

	const columns = levels_grid.columns;
	const created = levels_grid.titles;
	const font = levels_grid.font;

	const level_type = text("level_type");
	const extra_id = select("levels_extra");
	const level = text("level");
	const level_effect = text("level_effect");

	const power_id = document.getElementById('power_id').value;

	const errors = 'level-err';
	const err_line = 'level-err-line';

	response = fetch('/power/levels/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'level_type': level_type,
			'level': level,
			'level_effect': level_effect,
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

			levels_grid.columns = jsonResponse.columns;

			const table_id = jsonResponse.table_id;
			const route = '/power/levels/delete/'
			create_table(jsonResponse);
			delete_row(jsonResponse, route, levels_grid)
			clear_errors(err_line, errors)

			levels_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
