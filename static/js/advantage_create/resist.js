function resist_check() {
	const check = "resist_check";
	const title = "resist-title";
	const base = 'resist-base';
	const entry = "resist-entry";

	entry_check(check, title, base, entry);
}

function resist_trait_type() {
	const select = 'resist_trait_type';
	const fill = 'resist_trait';

	trait_select(select, fill);
}

let resist_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function resist_submit() {

	const columns = resist_grid.columns;
	const created = resist_grid.titles;
	const font = resist_grid.font;

	const benefit = select("resist_benefit");
	const trait_type = select("resist_trait_type");
	const trait = select("resist_trait");
	const mod = select("resist_mod");
	const which = select("resist_which");
	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'resist-err';
	const err_line = 'resist-err-line';

	response = fetch('/advantage/resist/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'trait_type': trait_type,
			'trait': trait,
			'mod': mod,
			'which': which
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			multiple_field('resist-multiple');
			multiple_field('resist-multiple-title');

			resist_grid.columns.length = 0;
			resist_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, resist_grid, route);
			clear_errors(err_line, errors)

			resist_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}