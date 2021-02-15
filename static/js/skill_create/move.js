function move_check() {
	const check = "move_check";
	const title = "move-title";
	const base = 'move-base';
	const entry = "move-entry";

	entry_check(check, title, base, entry);
}

function move_speed_trait_type() {
	const select = 'move_speed_trait_type';
	const fill = 'move_speed_trait';

	id_select(select, fill, trait_select);
}

function move_distance_unit_trait_type() {
	const select = 'move_distance_unit_trait_type';
	const fill = 'move_distance_unit_trait';

	id_select(select, fill, trait_select);
}

function move_distance_rank_trait_type() {
	const select = 'move_distance_rank_trait_type';
	const fill = 'move_distance_rank_trait';

	id_select(select, fill, trait_select);
}


function move_speed() {
	const select = 'move_speed';
	const options = [{'val': 'rank', 'div': 'move-speed-rank'},
					{'val': 'mod', 'div': 'move-speed-mod'}]

	select_opacity(select, options);
}

function move_distance() {
	const select = 'move_distance';
	const options = [{'val': 'rank', 'div': 'move-distance-rank'},
					{'val': 'unit', 'div': 'move-distance-unit'},
					{'val': 'unit_math', 'div': 'move-distance-unit-math'},
					{'val': 'rank_math', 'div': 'move-distance-rank-math'}]

	select_opacity(select, options)
}

let move_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function move_submit() {

	const columns = move_grid.columns;
	const created = move_grid.titles;
	const font = move_grid.font;

	const skill_id = document.getElementById('skill_id').value;

	const errors = 'move-err';
	const err_line = 'move-err-line';

	response = fetch('/skill/move/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
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

			move_grid.columns.length = 0;
			move_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, _grid, route);
			clear_errors(err_line, errors)

			move_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}