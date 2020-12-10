const move_entry = 'move-entry';

function move_check() {
	const check = "move_check";
	const title = "move-title";
	const base = 'move-base';
	const entry = "move-entry";

	check_title(check, title, base, entry);
}

function move_base() {
	const field = 'move_extra';
	const entry = "move-entry";

	base(field, entry);
}

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

	trait_select(select, fill);
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

	trait_select(select, fill);
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

	trait_select(select, fill);
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

	trait_select(select, fill);
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

function move_submit() {

	const extra = select("move_extra");
	const rank = select("move_rank");
	const math = select("move_math");
	const mod = select("move_mod");
	const per_rank = check("move_per_rank");
	const flight = check("move_flight");
	const aquatic = check("move_aquatic");
	const ground = check("move_ground");
	const condition = select("move_condition");
	const direction = select("move_direction");
	const distance_type = select("move_distance_type");
	const distance_value = select("move_distance_value");
	const distance_math_value = select("move_distance_math_value");
	const distance_math = select("move_distance_math");
	const distance_math_value2 = select("move_distance_math_value2");
	const distance_mod = select("move_distance_mod");
	const dc = select("move_dc");
	const others = check("move_others");
	const continuous = check("move_continuous");
	const subtle = check("move_subtle");
	const concentration = check("move_concentration");
	const obstacles = check("move_obstacles");
	const objects = check("move_objects");
	const permeate = check("move_permeate");
	const special = check("move_special");
	const prone = check("move_prone");
	const check_type = check("move_check_type");
	const obstacles_check = check("move_obstacles");
	const concealment = check("move_concealment");
	const extended = check("move_extended");
	const mass = check("move_mass");
	const mass_value = select("move_mass_value");
	const extended_actions = select("move_extended_actions");
	const acquatic_type = select("move_acquatic_type");
	const concealment_sense = select("move_concealment_sense");
	const concealment_trait_type = select("move_concealment_trait_type");
	const concealment_trait = select("move_concealment_trait");
	const permeate_type = select("move_permeate_type");
	const permeate_speed = select("move_permeate_speed");
	const permeate_cover = check("move_permeate_cover");
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
	const ground_type = select("move_ground_type");
	const ground_permanence = select("move_ground_perm");
	const ground_time = select("move_ground_time");
	const ground_units = select("move_ground_units");
	const ground_ranged = check("move_ground_ranged");
	const subtle_trait_type = select("move_subtle_trait_type");
	const subtle_trait = select("move_subtle_trait");
	const subtle_mod = select("move_subtle_mod");
	const flight_resist = check("move_flight_resist");
	const flight_equip = check("move_flight_equip");
	const flight_conditions = multiple("move_flight_conditions");
	const objects_check = select("move_objects_check");
	const objects_attack = select("move_objects_attack");
	const objects_skill_type = select("move_objects_skill_type");
	const objects_skill = select("move_objects_skill");
	const objects_direction = select("move_objects_direction");
	const objects_damage = check("move_objects_damage");
	const damage_type = select("move_objects_damage_type");
	const check_trait_type = select("move_check_trait_type");
	const check_trait = select("move_check_trait");
	const check_free = check("move_check_free");
	const ranks = select("move_ranks");
	const cost = select("move_cost");

}