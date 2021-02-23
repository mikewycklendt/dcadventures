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
	const description = 'move-speed-description';
	const entry = 'move-entry';

	select_opacity(select, options);
	select_maxheight_any_entry(select, description, entry);
}

function move_distance() {
	const select = 'move_distance';
	const options = [{'val': 'rank', 'div': 'move-distance-rank'},
					{'val': 'unit', 'div': 'move-distance-unit'},
					{'val': 'unit_math', 'div': 'move-distance-unit-math'},
					{'val': 'rank_math', 'div': 'move-distance-rank-math'}]
	const description = 'move-distance-description';
	const entry = 'move-entry';

	select_opacity(select, options);
	select_maxheight_any_entry(select, description, entry);
}

let move_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function move_submit() {

	const columns = move_grid.columns;
	const created = move_grid.titles;
	const font = move_grid.font;

	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");

	const speed = select("move_speed");
	const speed_rank = select("move_speed_rank");
	const speed_trait_type = select("move_speed_trait_type");
	const speed_trait = select("move_speed_trait");
	const speed_math1 = select("move_speed_math1");
	const speed_value1 = select("move_speed_value1");
	const speed_math2 = select("move_speed_math2");
	const speed_value2 = select("move_speed_value2");
	const speed_description = text("move_speed_description")
	const distance = select("move_distance");
	const distance_rank = select("move_distance_rank");
	const distance_value = text("move_distance_value");
	const distance_units = select("move_distance_units");
	const distance_rank_trait_type = select("move_distance_rank_trait_type");
	const distance_rank_trait = select("move_distance_rank_trait");
	const distance_rank_math1 = select("move_distance_rank_math1");
	const distance_rank_value1 = select("move_distance_rank_value1");
	const distance_rank_math2 = select("move_distance_rank_math2");
	const distance_rank_value2 = select("move_distance_rank_value2");
	const distance_unit_trait_type = select("move_distance_unit_trait_type");
	const distance_unit_trait = select("move_distance_unit_trait");
	const distance_unit_math1 = select("move_distance_unit_math1");
	const distance_unit_value1 = select("move_distance_unit_value1");
	const distance_unit_math2 = select("move_distance_unit_math2");
	const distance_unit_value2 = select("move_distance_unit_value2");
	const distance_math_units = select("move_distance_math_units");
	const distance_description = text("move_distance_description");
	const direction = select("move_direction");
	const dc = select("move_dc");
	const degree = select("move_degree");
	const circ = select("move_circ");
	const time = select("move_time");
	const keyword = text("move_keyword");
	const title = text("move_title");
	
	const errors = 'move-err';
	const err_line = 'move-err-line';

	const selects = 'move-sml';
	const select_title = 'move-title-sml'

	response = fetch('/skill/move/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'speed': speed,
			'speed_rank': speed_rank,
			'speed_trait_type': speed_trait_type,
			'speed_trait': speed_trait,
			'speed_math1': speed_math1,
			'speed_value1': speed_value1,
			'speed_math2': speed_math2,
			'speed_value2': speed_value2,
			'speed_description': speed_description,
			'distance': distance,
			'distance_rank': distance_rank,
			'distance_value': distance_value,
			'distance_units': distance_units,
			'distance_rank_trait_type': distance_rank_trait_type,
			'distance_rank_trait': distance_rank_trait,
			'distance_rank_math1': distance_rank_math1,
			'distance_rank_value1': distance_rank_value1,
			'distance_rank_math2': distance_rank_math2,
			'distance_rank_value2': distance_rank_value2,
			'distance_unit_trait_type': distance_unit_trait_type,
			'distance_unit_trait': distance_unit_trait,
			'distance_unit_math1': distance_unit_math1,
			'distance_unit_value1': distance_unit_value1,
			'distance_unit_math2': distance_unit_math2,
			'distance_unit_value2': distance_unit_value2,
			'distance_math_units': distance_math_units,
			'distance_description': distance_description,
			'direction': direction,
			'degree': degree,
			'circ': circ,
			'dc': dc,
			'time': time,
			'keyword': keyword,
			'title': title
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
			const title_name = jsonResponse.title;
			const title_id = jsonResponse.title_id;

			selects_add(title_id, title_name, select_title);

			selects_add(id, keyword, selects)

			move_grid.columns.length = 0;
			move_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table('skill', jsonResponse, move_grid, route, [selects], title_id, [select_title]);
			clear_errors(err_line, errors)

			move_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}