function feature_check() {
	const check = "feature_check";
	const title = "feature-title";
	const base = 'feature-base';
	const entry = "feature-entry";

	entry_check(check, title, base, entry);
}

let feature_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function feature_submit() {

	const columns = feature_grid.columns;
	const created = feature_grid.titles;
	const font = feature_grid.font;

	const equip_id = document.getElementById('equip_id').value;
	const name = text('feature_name')
	const description = text('feature_description')
	const feature = select('feature_feature');
	let feature_count = document.getElementById('feature_count');

	const errors = 'feature-err';
	const err_line = 'feature-err-line';

	response = fetch('/equipment/feature/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'name': name,
			'description': description,
			'feature': feature
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const id = jsonResponse.id;
			const selects = ['feature-entry']

			if (name != '') {
				selects_add(id, name, 'feature-entry');
				feature_count += 1;
			}
			
			feature_grid.columns.length = 0;
			feature_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, feature_grid, route, selects);
			clear_errors(err_line, errors)

			feature_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}

function feature_save() {
	const feature_count = document.getElementById('feature_count');
	const equip_id = document.getElementById('equip_id').value;
	const errors = 'equip-err';
	const err_line = 'equip-err-line';

	const description = text("description");
	const type_id = select("equip_type");
	let cost = select("cost");
	const toughness = select("toughness");
	const expertise = select("expertise");
	const alternate = check("alternate");
	const move = check("move");
	const speed_mod = select("speed_mod");
	const direction = select("direction");
	const locks = check("locks");
	const lock_type = select("lock_type");

	if (feature_count < 1) {
		const error_msgs = {'error_msgs': ["You haven't created any features."]}
		
		back_errors(err_line, errors, error_msgs);

	} else {
		response = fetch('/equipment/feature/save', {
			method: 'POST',
			body: JSON.stringify({
				'equip_id': equip_id,
				'type_id': type_id,
				'cost': cost,
				'description': description,
				'toughness': toughness,
				'expertise': expertise,
				'alternate': alternate,
				'move': move,
				'speed_mod': speed_mod,
				'direction': direction,
				'locks': locks,
				'lock_type': lock_type
			}),
			headers: {
			'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				window.location.replace('/feature/save/success');

			} else {
				back_errors(err_line, errors, jsonResponse)
			}
		})
 
	}
}