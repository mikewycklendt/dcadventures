function move_check() {
	const check = "move_check";
	const title = "move-title";
	const base = 'move-base';
	const entry = "move-entry";

	entry_check(check, title, base, entry);
}

function move_extra() {
	const select = 'move_extra';
	const fill = 'move_cost'

	id_select(select, fill, power_cost_select, the_power);
}

function move_cost() {
	const select = 'move_cost';
	const fill = 'move_ranks';
	const extra = 'move_extra';

	id_select(select, fill, power_ranks_select, extra, false, false, false, the_power);
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
	const select = "move_ground_perm";
	const options = [{'val': 'temp', 'div': 'move-ground-perm'}];

	select_opacity(select, options);
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
	const div = 'move-objects-damage';

	check_display(check, div);
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

function move_flight_resist() {
	const check = 'move_flight_resist';
	const div = 'move-flight-resist';

	check_display(check, div);
}

function move_flight_equip() {
	const check = 'move_flight_equip';
	const div = 'move-flight-equip';

	check_display(check, div);
}

function move_flight_equip_type() {
	const select = 'move_flight_equip_type';
	const fill = 'move_flight_equipment';
	const sub = 'variable-equip';

	id_select(select, fill, equipment_select, sub);
}

function move_condition_check() {
	const check = 'move_condition_check';
	const div =  'move-condition';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_equip() {
	const check = 'move_equip';
	const div = 'move-equip';
	const entry = 'move-entry';

	check_drop(check, div, entry);
}

function move_equip_type() {
	const select = 'move_equip_type';
	const fill = 'move_equipment';
	const sub = 'variable-equip';

	id_select(select, fill, equipment_select, sub);
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
	const dc_type = select("move_dc_type");
	const degree_type = select("move_degree_type");
	const circ_type = select("move_circ_type");
	const time_type = select("move_time_type");
	const keyword = text("move_keyword");
	const title = text("move_title");

	const speed_per =  check("move_speed_per");
	const distance_per = check("move_distance_per");
	const flight = check("move_flight");
	const aquatic = check("move_aquatic");
	const ground = check("move_ground");
	const special = check("move_special");
	const condition_check = check("move_condition_check");
	const obstacles = check("move_obstacles");
	const objects = check("move_objects");
	const permeate = check("move_permeate");
	const prone = check("move_prone");
	const equip = check("move_equip");
	const concealment = check("move_concealment");
	const extended = check("move_extended");
	const mass = check("move_mass");
	const flight_resist = check("move_flight_resist");
	const flight_resist_check = select("move_flight_resist_check");
	const flight_equip = check("move_flight_equip");
	const flight_equip_type = select("move_flight_equip_type");
	const flight_equipment = select("move_flight_equipment");
	const flight_conditions = multiple("move_flight_conditions");
	const acquatic_type = select("move_acquatic_type");
	const ground_type = select("move_ground_type");
	const ground_perm = select("move_ground_perm");
	const ground_time = select("move_ground_time");
	const ground_ranged = check("move_ground_ranged");
	const ground_range = select("move_ground_range");
	const special_type = select("move_special_type");
	const teleport_type = select("move_teleport_type");
	const teleport_change = select("move_teleport_change");
	const teleport_portal = check("move_teleport_portal");
	const teleport_obstacles = check("move_teleport_obstacles");
	const dimension_type = select("move_dimension_type");
	const dimension_mass_rank = select("move_dimension_mass_rank");
	const dimension_descriptor = select("move_dimension_descriptor");
	const special_space = select("move_special_space");
	const special_time = select("move_special_time");
	const special_time_carry = select("move_special_time_carry");
	const condition = select("move_condition");
	const objects_check = select("move_objects_check");
	const objects_direction = select("move_objects_direction");
	const objects_damage = check("move_objects_damage");
	const object_damage = select("move_object_damage");
	const permeate_type = select("move_permeate_type");
	const permeate_speed = select("move_permeate_speed");
	const permeate_cover = check("move_permeate_cover");
	const equip_type = select("move_equip_type");
	const equipment = select("move_equipment");
	const concealment_sense = select("move_concealment_sense");
	const conceal_opposed = select("move_conceal_opposed");
	const extended_actions = select("move_extended_actions");
	const mass_value = select("move_mass_value");

	const cost = select("move_cost");
	const ranks = select("move_ranks");
	
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
			'degree_type': degree_type,
			'circ_type': circ_type,
			'dc_type': dc_type,
			'time_type': time_type,
			'keyword': keyword,
			'title': title,
			'speed_per': speed_per,
			'distance_per': distance_per,
			'flight': flight,
			'aquatic': aquatic,
			'ground': ground,
			'special': special,
			'condition_check': condition_check,
			'obstacles': obstacles,
			'objects': objects,
			'permeate': permeate,
			'prone': prone,
			'equip': equip,
			'concealment': concealment,
			'extended': extended,
			'mass': mass,
			'flight_resist': flight_resist,
			'flight_resist_check': flight_resist_check,
			'flight_equip': flight_equip,
			'flight_equip_type': flight_equip_type,
			'flight_equipment': flight_equipment,
			'flight_conditions': flight_conditions,
			'acquatic_type': acquatic_type,
			'ground_type': ground_type,
			'ground_perm': ground_perm,
			'ground_time': ground_time,
			'ground_ranged': ground_ranged,
			'ground_range': ground_range,
			'special_type': special_type,
			'teleport_type': teleport_type,
			'teleport_change': teleport_change,
			'teleport_portal': teleport_portal,
			'teleport_obstacles': teleport_obstacles,
			'dimension_type': dimension_type,
			'dimension_mass_rank': dimension_mass_rank,
			'dimension_descriptor': dimension_descriptor,
			'special_space': special_space,
			'special_time': special_time,
			'special_time_carry': special_time_carry,
			'condition': condition,
			'objects_check': objects_check,
			'objects_direction': objects_direction,
			'objects_damage': objects_damage,
			'object_damage': object_damage,
			'permeate_type': permeate_type,
			'permeate_speed': permeate_speed,
			'permeate_cover': permeate_cover,
			'equip_type': equip_type,
			'equipment': equipment,
			'concealment_sense': concealment_sense,
			'conceal_opposed': conceal_opposed,
			'extended_actions': extended_actions,
			'mass_value': mass_value,
			'cost': cost,
			'ranks': ranks
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