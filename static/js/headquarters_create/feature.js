function feature_check() {
	const check = "feature_check";
	const title = "feature-title";
	const base = 'feature-base';
	const entry = "feature-entry";

	entry_check(check, title, base, entry);
}

function feature_feature() {
	const select = 'feature_feature';

	feature_info(select, head_feature_info_select);
}

let feature_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function feature_submit() {

	const columns = feature_grid.columns;
	const created = feature_grid.titles;
	const font = feature_grid.font;

	const head_id = document.getElementById('head_id').value;
	const name = text('feature_name')
	const description = text('feature_description')
	const feature = select('feature_feature');

	const errors = 'feature-err';
	const err_line = 'feature-err-line';

	response = fetch('/headquarters/feature/create', {
		method: 'POST',
		body: JSON.stringify({
			'head_id': head_id,
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
			}
			
			costs.features = jsonResponse.cost;
			calculate_cost();

			feature_grid.columns.length = 0;
			feature_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/headquarters/' + table_id + '/delete/'
			create_table(jsonResponse, feature_grid, route, selects);
			clear_errors(err_line, errors)

			feature_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}
