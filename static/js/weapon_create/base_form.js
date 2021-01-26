function category() {
	const select = 'category';
	const fill = 'type';
	const options = [{'val': '1', 'div': 'melee'},
					{'val': '2', 'div': 'ranged'},
					{'val': '4', 'div': 'access'}]

	weapon_type_select(select, fill);
	select_opacity_class(select, options)
}

function power() {
	const select = 'power';
	const div = 'base-power-rank';

	select_opacity_any(select, div);
}

function ranged_area() {
	const select = 'ranged_area';
	const options = [{'val': 'burst', 'div': 'burst'}]
	const div = 'area-damage';

	select_opacity(select, options);
	select_opacity_any(select, div);
}