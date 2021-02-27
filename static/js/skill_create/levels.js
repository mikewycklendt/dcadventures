function levels_check() {
	const levels_check = "levels_check";
	const levels_base_form = "levels-base-form";
	const title = "levels-title";
	const entry = "levels-entry";

	check_title(levels_check, title, levels_base_form, entry);
}

function levels_base() {
	const type = "level_type";
	const entry = "levels-entry";

	base_text(type, entry);
}


let bonus_level = true;

let levels_grid = {'titles': false,
					'columns': [],
					'font': 100,
					'mod': [],
					'old_level_type': ''}

function levels_submit() {

	const columns = levels_grid.columns;
	const created = levels_grid.titles;
	const font = levels_grid.font;

	const level_type = text("level_type");
	const level = text("level");
	const level_effect = text("level_effect");

	const old_level_type = levels_grid.old_level_type;

	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");

	const errors = 'levels-err';
	const err_line = 'levels-err-line';
	const level_selects = 'level-type-sml';

	response = fetch('/levels/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'column': 'bonus_id',
			'level_type': level_type,
			'level': level,
			'level_effect': level_effect,
			'columns': columns,
			'created': created,
			'font': font,
			'old_level_type': old_level_type
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
			const title_name = level_type;
			const title_id = jsonResponse.title_id;
			const add_title = jsonResponse.add_title;

			if (add_title == true) {
				selects_add(title_id, title_name, level_selects);
			}			
			
			levels_grid.columns.length = 0;
			levels_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/levels/delete/'
			create_table('skill', jsonResponse, levels_grid, route, false, title_id, [level_selects]);
			clear_errors(err_line, errors)

			levels_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
