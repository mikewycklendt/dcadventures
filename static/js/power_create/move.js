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
					{'val': 'time', 'div': 'move-special-time'}]

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