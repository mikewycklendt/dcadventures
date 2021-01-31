function feature_check() {
	const check = "feature_check";
	const title = "feature-title";
	const base = 'feature-base';
	const entry = "feature-entry";

	entry_check(check, title, base, entry);
}

function addon() {
	const select = 'addon';
	const options = [{'val': 'feature', 'div': 'feature-feature'},
					{'val': 'weapon', 'div': 'feature-weapon'},
					{'val': 'equipment', 'div': 'feature-equipment'}]

	select_opacity(select, options)
}

let addon_cost = {'cost': 0}

function feature_feature() {
	const select = 'feature_feature';
	const entry = 'feature-entry';
	const route = '/vehicle/feature/info'
	const item = 'feature-item';

	addon_info(select, route;
}

function equipment()  {
	const select = 'equipment';
	const entry = 'feature-entry';
	const route = '/equipment/equipment/select/info';
	const item = 'feature-item';

	addon_info(select, route);
}

function weapon() {
	const select = 'weapon';
	const entry = 'feature-entry';
	const route = '/equipment/weapon/select/info';
	const item = 'feature-item';

	addon_info(select, route);
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

function feature_equipment() {
	const select = 'feature_equipment';
	const fill = 'feature_feature';
	const route = '/vehicle/feature/select';

	id_select(select, fill, route);

}

function feature_equipment_type() {
	const select = 'feature_equipment_type';
	const fill = 'feature_equipment';
	const route =  '/vehicle/equipment/select';

	id_select(select, fill, route);	
}
let feature_grid = {'titles': false,
					'columns': [],
					'font': 110,
					'mod': []}



function feature_submit() {

	const columns = feature_grid.columns;
	const created = feature_grid.titles;
	const font = feature_grid.font;

	const head_id = document.getElementById('head_id').value;
	const feature = select('feature_feature');
	const equipment = select("equipment");
	const weapon = select("weapon");
	const addon = select("addon")

	const errors = 'feature-err';
	const err_line = 'feature-err-line';

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

			feature_grid.columns.length = 0;
			feature_grid.columns = jsonResponse.rows;
			costs.features = jsonResponse.cost;
			calculate_cost()

			const table_id = jsonResponse.table_id;
			const route = '/headquarters/' + table_id + '/delete/'
			create_table(jsonResponse, feature_grid, route);
			clear_errors(err_line, errors)

			feature_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}