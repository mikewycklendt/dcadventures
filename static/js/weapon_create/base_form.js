function category() {
	const select = 'category';
	const fill = 'type';
	const options = [{'val': '1', 'div': 'base-thrown'},
					{'val': '1', 'div': 'base-hands'},
					{'val': '1', 'div': 'base-reach'},
					{'val': '1', 'div': 'base-unarmed'}]

	weapon_type_select(select, fill);
	select_opacity(select, options)
}

function power() {
	const select = 'power';
	const div = 'base-power-rank';

	select_opacity_any(select, div);
}