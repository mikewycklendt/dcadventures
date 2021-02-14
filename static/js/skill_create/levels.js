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

	response = fetch('/skill/levels/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
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

			const add_level = jsonResponse.created;

			if (add_level == false) {
				
				const id = jsonResponse.level_type_id		
				const name = jsonResponse.level_type

				selects_add(id, name, level_selects)
			}

			levels_grid.columns.length = 0;
			levels_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/levels/delete/'
			create_table(jsonResponse, levels_grid, route);
			clear_errors(err_line, errors)
			row_delete(jsonResponse, route, levels_grid) 


			levels_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
};
