function opposed_skill_type() {
	const select = 'opposed_skill_type';
	const fill = 'opposed_skill';

	skill_select(select, fill);
}

function opposed_check() {
	const check = "opposed_check";
	const title = "opposed-title";
	const base = 'opposed-base';
	const entry = "opposed-entry";

	entry_check(check, title, base, entry);
}

let opposed_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function opposed_submit() {

	const columns = opposed_grid.columns;
	const created = opposed_grid.titles;
	const font = opposed_grid.font;

	const equip_id = document.getElementById('equip_id').value;
	const effect = select("opposed_effect");
	const feature = select("opposed_feature");
	const dc = select("opposed_dc");
	const skill_type = select("opposed_skill_type");
	const skill = select("opposed_skill");
	const check = select ("opposed_check");
	const when = select("opposed_when");
	const condition1 = select("opposed_condition1");
	const condition2 = select("opposed_condition2");

	const errors = 'opposed-err';
	const err_line = 'opposed-err-line';

	response = fetch('/equipment/opposed/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'effect': effect,
			'feature': feature,
			'dc': dc,
			'skill_type': skill_type,
			'skill': skill,
			'check': check,
			'when': when,
			'condition1': condition1,
			'condition2': condition2
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			opposed_grid.columns.length = 0;
			opposed_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, opposed_grid, route);
			clear_errors(err_line, errors)

			opposed_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}