function limits_check() {
	const check = "limits_check";
	const title = "limits-title";
	const base = 'limits-base';
	const entry = "limits-entry";

	entry_check(check, title, base, entry);
}

let limits_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function limits_submit() {

	const columns = limits_grid.columns;
	const created = limits_grid.titles;
	const font = limits_grid.font;

	const equip_id = document.getElementById('equip_id').value;
	const effect = select("limits_effect")
	const feature = select("limits_feature")
	const time = text("limits_time")
	const time_units = select("limits_time_units")
	const range = text("limits_range")
	const range_units = select("limits_range_units")
	const extend = check("limits_extend")
	const extendable = check("limits_extends")
	const time_capacity = text("limits_time_capacity")
	const time_capacity_units = select("limits_time_capacity_units")
	const capacity = text("limits_capacity")
	const item = text("limits_item")
	const ammo = check("limits_ammo")
	const fuel = check("limits_fuel")
	const area_long = text("limits_area_long")
	const area_wide = text("limits_area_wide")
	const area_units = select("limits_area_units")
	const recharge = check("limits_recharge")
	const refill = check("limits_refill")
	const uses = select("limits_uses")
	const light = select("limits_light")
	const internet = check("limits_internet")
	const needs_internet = check("limits_needs_internet")

	const errors = 'limits-err';
	const err_line = 'limits-err-line';

	response = fetch('/equipment/limits/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'effect': effect,
			'feature': feature,
			'time': time,
			'time_units': time_units,
			'range': range,
			'range_units': range_units,
			'extend': extend,
			'extendable': extendable,
			'time_capacity': time_capacity,
			'time_capacity_units': time_capacity_units,
			'capacity': capacity,
			'item': item,
			'ammo': ammo,
			'fuel': fuel,
			'area_long': area_long,
			'area_wide': area_wide,
			'area_units': area_units,
			'recharge': recharge,
			'refill': refill,
			'uses': uses,
			'light': light,
			'internet': internet,
			'needs_interneT': needs_internet
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			limits_grid.columns.length = 0;
			limits_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, limits_grid, route);
			clear_errors(err_line, errors)

			limits_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}