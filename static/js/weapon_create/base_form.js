function category() {
	const select = 'category';
	const fill = 'type';
	const options = [{'val': '1', 'div': 'base-thrown'}]

	weapon_type_select(select, fill);
	select_opacity(select, options)
}

function power() {
	const select = 'power';
	const div = 'base-power-rank';

	select_opacity_any(select, div);
}