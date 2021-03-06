function category() {
	const select = 'category';
	const fill = 'type';
	const options = [{'val': '1', 'div': 'melee'},
					{'val': '2', 'div': 'ranged'},
					{'val': '3', 'div': 'grenade'},
					{'val': '4', 'div': 'access'}]

	id_select(select, fill, weapon_type_select);
	select_opacity_class(select, options)
}

function power() {
	const select = 'power';
	const div = 'base-power-rank';

	select_opacity_any(select, div);
}

function ranged_area() {
	const select = 'ranged_area';
	const options = [{'val': 'burst', 'div': 'ranged-burst'}]
	const div = 'ranged-area-damage';

	select_opacity(select, options);
	select_opacity_any(select, div);
}

function grenade_area() {
	const select = 'grenade_area';
	const options = [{'val': 'burst', 'div': 'grenade-burst'}]
	const div = 'grenade-area-damage';

	select_opacity(select, options);
	select_opacity_any(select, div);
}

function subtle() {
	const check = 'subtle';
	const div = 'subtle-dc';

	check_opacity(check, div);
}

function double() {
	const check = 'double';
	const div = 'double-mod';

	check_opacity(check, div);
}