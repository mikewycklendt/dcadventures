function addon_check() {
	const check = "addon_check";
	const title = "addon-title";
	const base = 'addon-base';
	const entry = "addon-entry";

	entry_check(check, title, base, entry);
}

function addon() {
	const select = 'addon';
	const options = [{'val': 'feature', 'div': 'addon-feature'},
					{'val': 'weapon', 'div': 'addon-weapon'},
					{'val': 'equipment', 'div': 'addon-equipment'}]

	select_opacity(select, options)
}

let addon_cost = {'cost': 0}

function addon_feature() {
	const select = 'addon_feature';

	addon_info(select, feature_info_select);
}

function equipment()  {
	const select = 'equipment';

	addon_info(select, equipment_info_select);
}

function weapon() {
	const select = 'weapon';

	addon_info(select, weapon_info_select);
}

function weapon_cat() {
	const select = 'weapon_cat';
	const fill = 'weapon_type';

	id_select(select, fill, weapon_type_select);
}

function weapon_type() {
	const select = 'weapon_type';
	const fill = 'weapon';

	id_select(select, fill, weapon_select);
}

function equipment_type() {
	const select = 'equipment_type';
	const fill = 'equipment';
	const route =  '/vehicle/equipment/select';

	id_select(select, fill, route);	
}

function addon_equipment() {
	const select = 'addon_equipment';
	const fill = 'addon_feature';
	const route = '/vehicle/feature/select';

	id_select(select, fill, route);

}

function addon_equipment_type() {
	const select = 'addon_equipment_type';
	const fill = 'addon_equipment';
	const route =  '/vehicle/equipment/select';

	id_select(select, fill, route);	
}
let addon_grid = {'titles': false,
					'columns': [],
					'font': 110,
					'mod': []}



function addon_submit() {

	const columns = addon_grid.columns;
	const created = addon_grid.titles;
	const font = addon_grid.font;

	const head_id = document.getElementById('head_id').value;
	const feature = select('addon_feature');
	const equipment = select("equipment");
	const weapon = select("weapon");
	const addon = select("addon")

	const errors = 'addon-err';
	const err_line = 'addon-err-line';

	response = fetch('/headquarters/addon/create', {
		method: 'POST',
		body: JSON.stringify({
			'head_id': head_id,
			'columns': columns,
			'created': created,
			'font': font,
			'feature': feature,
			'equipment': equipment,
			'weapon': weapon,
			'addon': addon
	
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			addon_grid.columns.length = 0;
			addon_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/headquarters/' + table_id + '/delete/'
			create_table(jsonResponse, addon_grid, route);
			clear_errors(err_line, errors)

			addon_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}