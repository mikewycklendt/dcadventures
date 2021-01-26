function category() {
	const select = 'category';
	const fill = 'type';
	const options = [{'val': '1', 'div': 'base-thrown'},
					{'val': '1', 'div': 'base-reach'},
					{'val': '1', 'div': 'base-unarmed'},
					{'val': '2', 'div': 'base-accurate'},
					{'val': '2', 'div': 'base-protection'},
					{'val': '2', 'div': 'base-area'},
					{'val': '2', 'div': 'base-penetrate'}]

	weapon_type_select(select, fill);
	select_opacity(select, options)
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