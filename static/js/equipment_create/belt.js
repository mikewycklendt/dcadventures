function belt_item_type() {
	const select = 'belt_item_type';
	const options = [{'val': 'feature', 'div': 'belt-feature'},
					{'val': 'weapon', 'div': 'belt-weapon'},
					{'val': 'equip', 'div': 'belt-equipment'}];
	const selects = ['belt_feature', 'belt_weapon_cat', 'belt_weapon_type', 'belt_weapon', 'belt_equipment_type', 'belt_equipment'];

	select_opacity(select, options);
	reset_all(selects)
}

function belt_equipment() {
	const entry = 'belt-entry';
	const select = 'belt_equipment';
	const route = '/equipment/equipment/select/info'

	belt_info(select, route, entry)
}

function belt_feature() {
	const entry = 'belt-entry';
	const select = 'belt_feature';
	const route = '/equipment/feature/select/info'

	belt_info(select, route, entry)
}

function belt_weapon() {
	const entry = 'belt-entry';
	const select = 'belt_weapon';
	const route = '/equipment/weapon/select/info'

	belt_info(select, route, entry)
}

function belt_weapon_cat() {
	const select = 'belt_weapon_cat';
	const fill = 'belt_weapon_type';

	weapon_type_select(select, fill);
}

function belt_weapon_type() {
	const select = 'belt_weapon_type';
	const fill = 'belt_weapon';

	weapon_select(select, fill);
}

function belt_equipment_type() {
	const select = 'belt_equipment_type';
	const fill = 'belt_equipment';

	equipment_select(select, fill);
}

function belt_check() {
	const check = "belt_check";
	const title = "belt-title";
	const base = 'belt-base';
	const entry = "belt-entry";

	entry_check(check, title, base, entry);
}

let belt_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function belt_submit() {

	const columns = belt_grid.columns;
	const created = belt_grid.titles;
	const font = belt_grid.font;

	const equip_id = document.getElementById('equip_id').value;

	const item_type = select("belt_item_type");
	const feature = select("belt_feature");
	const weapon = select("belt_weapon");
	const equipment = select("belt_equipment");
	const belt_item_type = select('belt_item_type');
	const belt_cost = document.getElementById("belt-cost");
	const cost = document.getElementById('belt_cost');

	const errors = 'belt-err';
	const err_line = 'belt-err-line';

	response = fetch('/equipment/belt/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'feature': feature,
			'weapon': weapon,
			'equipment': equipment,
			'belt_item_type': belt_item_type
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			const total_cost = jsonResponse.total_cost;
			belt_cost.style.opacity = '100%';
			belt_cost.innerHTML = total_cost;
			cost.value = total_cost;

			belt_grid.columns.length = 0;
			belt_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, belt_grid, route);
			clear_errors(err_line, errors)

			belt_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}