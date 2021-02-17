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

	id_select(select, fill, trait_select);
}


function opposed_opponent_trait_type() {
	const select = 'opposed_opponent_trait_type'
	const fill = 'opposed_opponent_trait'

	id_select(select, fill, trait_select)
}

function opposed_recurring() {
	const check = 'opposed_recurring';
	const div = 'opposed-recurring';

	check_display(check, div);
}

let opposed_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function opposed_submit() {

	const columns = opposed_grid.columns;
	const created = opposed_grid.titles;
	const font = opposed_grid.font;

	const attached = select("opposed_attached")
	const frequency = select("opposed_frequency")
	const trait_type = select("opposed_trait_type")
	const trait = select("opposed_trait")
	const mod = select("opposed_mod")
	const opponent_trait_type = select("opposed_opponent_trait_type")
	const opponent_trait = select("opposed_opponent_trait")
	const opponent_mod = select("opposed_opponent_mod")
	const player_check = select("opposed_player_check")
	const opponent_check = select("opposed_opponent_check")
	const secret = check("opposed_secret")
	const recurring = check("opposed_recurring")
	const multiple = select("opposed_multiple")
	const recurring_value = text("opposed_recurring_value")
	const recurring_units = select("opposed_recurring_units")
	const description = text("opposed_description");
	const keyword = text("opposed_keyword");

	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");

	const errors = 'opposed-err';
	const err_line = 'opposed-err-line';

	const opposed_selects = 'opposed-sml';

	response = fetch('/skill/opposed/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
			'attached': attached,
			'frequency': frequency,
			'trait_type': trait_type,
			'trait': trait,
			'mod': mod,
			'opponent_trait_type': opponent_trait_type,
			'opponent_trait': opponent_trait,
			'opponent_mod': opponent_mod,
			'player_check': player_check,
			'opponent_check': opponent_check,
			'secret': secret,
			'recurring': recurring,
			'multiple': multiple,
			'recurring_value': recurring_value,
			'recurring_units': recurring_units,
			'description': description,
			'keyword': keyword
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

			multiple_field('opposed-multiple');
			
			selects_add(id, keyword, opposed_selects);

			opposed_grid.columns.length = 0;
			opposed_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, opposed_grid, route, [opposed_selects]);
			clear_errors(err_line, errors)

			opposed_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}