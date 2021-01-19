function opposed_check() {
	const check = "opposed_check";
	const title = "opposed-title";
	const base = 'opposed-base';
	const entry = "opposed-entry";

	entry_check(check, title, base, entry);
}

function opposed_base() {
	const field = 'opposed_extra';
	const entry = "opposed-entry";

	base(field, entry);
}

function opposed_trait_type() {
	const select = 'opposed_trait_type'
	const fill = 'opposed_trait'

	trait_select(select, fill)
}


function opposed_opponent_trait_type() {
	const select = 'opposed_opponent_trait_type'
	const fill = 'opposed_opponent_trait'

	trait_select(select, fill)
}

let opposed_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function opposed_submit() {

	const columns = opposed_grid.columns;
	const created = opposed_grid.titles;
	const font = opposed_grid.font;

	
	const benefit = select("opposed_benefit");
	const trait_type = select("opposed_trait_type");
	const trait = select("opposed_trait");
	const mod = select("opposed_mod");
	const opponent_trait_type = select("opposed_opponent_trait_type");
	const opponent_trait = select("opposed_opponent_trait");
	const opponent_mod = select("opposed_opponent_mod");
	const player_check = select("opposed_player_check");
	const opponent_check = select("opposed_opponent_check");
	const multiple = select("opposed_multiple");

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'opposed-err';
	const err_line = 'opposed-err-line';

	response = fetch('/advantage/opposed/create', {
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
			'opponent_trait_type': opponent_trait_type,
			'opponent_trait': opponent_trait,
			'opponent_mod': opponent_mod,
			'player_check': player_check,
			'opponent_check': opponent_check,
			'multiple': multiple
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			multiple_field('opposed-multiple');

			opposed_grid.columns.length = 0;
			opposed_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table(jsonResponse, opposed_grid, route);
			clear_errors(err_line, errors)

			opposed_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}