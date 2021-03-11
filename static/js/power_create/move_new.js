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

function move_speed_trait() {
	const filter = select('move_speed_trait_type');
	const fill = 'move_speed_trait';

	id_select(fill, fill, trait_filter, filter);
}

function move_distance_unit_trait_type() {
	const select = 'move_distance_unit_trait_type';
	const fill = 'move_distance_unit_trait';

	id_select(select, fill, trait_select);
}

function move_distance_unit_trait() {
	const filter = select('move_distance_unit_trait_type');
	const fill = 'move_distance_unit_trait';

	id_select(fill, fill, trait_filter, filter);
}

function move_distance_rank_trait_type() {
	const select = 'move_distance_rank_trait_type';
	const fill = 'move_distance_rank_trait';

	id_select(select, fill, trait_select);
}

function move_distance_rank_trait() {
	const filter = select('move_distance_rank_trait_type');
	const fill = 'move_distance_rank_trait';

	id_select(fill, fill, trait_filter, filter);
}


function move_speed() {
	const select = 'move_speed';
	const options = [{'val': 'rank', 'div': 'move-speed-rank'},
					{'val': 'rank_mod', 'div': 'move-speed-rank-mod'},
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

const move_entry = 'move-entry';

function move_ground_perm() {
	const field_field = document.getElementById("move_ground_perm");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = "move-ground-time";

	if (field == 'temp') {
		show_maxheight(div)
	} else {
		hide_maxheight(div)
	}

}

function move_ground() {
	const check = 'move_ground';
	const div = 'move-ground';

	check_drop(check, div, move_entry);
}

function move_subtle() {
	const check = 'move_subtle';
	const div = 'move-subtle';
	
	check_drop(check, div, move_entry);
}

function move_subtle_trait_type() {
	const select = 'move_subtle_trait_type';
	const fill = 'move_subtle_trait';

	id_select(select, fill, trait_select);
}

function move_distance_type() {
	const select = 'move_distance_type';
	const val = 'move-distance-value';
	const math = 'move-distance-math';
	const div = 'move-distance';
	const mod = 'move-distance-mod';

	math_mod_div_select(select, val, math, mod, div)
}

function move_flight() {
	const check = 'move_flight';
	const div = 'move-flight';
	
	check_drop(check, div, move_entry);
}

function move_through_objects() {
	const check = 'move_through_objects';
	const div = 'move-through-objects';

	check_opacity(check, div);
}

function move_check_trait_type() {
	const select = 'move_check_trait_type';
	const fill = 'move_check_trait';

	id_select(select, fill, trait_select);
}

function move_check_type() {
	const check = 'move_check_type';
	const div = 'move-check-type';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_objects_skill_type() {
	const select = 'move_objects_skill_type';
	const fill = 'move_objects_skill';

	id_select(select, fill, trait_select);
}

function move_objects() {
	const check = 'move_objects';
	const div = 'move-objects';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_objects_check() {
	const select = 'move_objects_check';
	const options = [{'val': 1, 'div': 'move-objects-skill'}, {'val': 5, 'div': 'move-objects-attack'}]

	select_opacity(select, options);
}

function move_objects_damage() {
	const check = 'move_objects_damage';
	const div = 'move-objects-damage-type';

	check_opacity(check, div);
}

function move_permeate() {
	const check = 'move_permeate';
	const div = 'move-permeate';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_special() {
	const check = 'move_special';
	const div = 'move-special';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_dimension_type() {
	const select = 'move_dimension_type';
	const options = [{'val': 'descriptor', 'div': 'move-dimension-descriptor'}]

	select_opacity(select, options);
}

function move_special_type() {
	const select = 'move_special_type';
	const options = [{'val': 'space', 'div': 'move-special-space'},
					{'val': 'dimension', 'div': 'move-special-dimension'},
					{'val': 'time', 'div': 'move-special-time'},
					{'val': 'teleport', 'div': 'move-special-teleport'}]

	select_opacity(select, options);
}

function move_concealment() {
	const check = 'move_concealment';
	const div = 'move-concealment';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_concealment_trait_type() {
	const select = 'move_concealment_trait_type';
	const fill = 'move_concealment_trait';

	id_select(select, fill, trait_select);
}

function move_aquatic() {
	const check = 'move_aquatic';
	const div = 'move-aquatic';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_extended() {
	const check = 'move_extended';
	const div = 'move-extended';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_mass() {
	const check = 'move_mass';
	const div = 'move-mass';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_ground_ranged() {
	const check = 'move_ground_ranged';
	const div = 'move-ground-ranged';

	check_display(check, div);
}

let move_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function move_submit() {

	const columns = move_grid.columns;
	const created = move_grid.titles;
	const font = move_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const extra_id = select("move_extra");
	const speed = select("move_speed");
	const speed_rank = select("move_speed_rank");
	const speed_rank_mod = select("move_speed_rank_mod");
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

	const speed_per =  check("move_speed_per");
	const distance_per = check("move_distance_per");
	const flight = check("move_flight");
	const aquatic = check("move_aquatic");
	const ground = check("move_ground");
	const special = check("move_special");
	const condition_check = check("move_condition_check");
	
	const errors = 'move-err';
	const err_line = 'move-err-line';

	const selects = 'move-sml';
	const select_title = 'move-title-sml'

	response = fetch('/power/move/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'columns': columns,
			'created': created,
			'font': font,
			'speed': speed,
			'speed_rank_mod': speed_rank_mod,
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
			const add_title = jsonResponse.add_title

			if (add_title == true) {
				selects_add(title_id, title_name, select_title);
			}
			selects_add(id, keyword, selects)

			move_grid.columns.length = 0;
			move_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, move_grid, route, [selects], title_id, [select_title]);
			clear_errors(err_line, errors)

			move_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}