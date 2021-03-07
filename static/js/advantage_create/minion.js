function minion_check() {
	const check = "minion_check";
	const title = "minion-title";
	const base = 'minion-base';
	const entry = "minion-entry";

	entry_check(check, title, base, entry);
}

function minion_base() {
	const field = 'minion_extra';
	const entry = "minion-entry";

	base(field, entry);
}

function minion_multiple() {
	const check = 'minion_multiple'
	const div = 'minion-multiple';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_attitude() {
	const check = 'minion_attitude';
	const div = 'minion-attitude';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_attitude_type() {
	const select = 'minion_attitude_type';
	const fill = 'minion_attitude_attitude';

	id_select(select, fill, level_select);
}

function minion_resitable() {
	const check = 'minion_resitable';
	const div = 'minion-resitable';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_sacrifice() {
	const check = 'minion_sacrifice';
	const div = 'minion-sacrifice';

	check_display(check, div);
}

function minion_attitude_trait_type() {
	const select = 'minion_attitude_trait_type';
	const fill = 'minion_attitude_trait';

	id_select(select, fill, trait_select, variable_sub);
}

let minion_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function minions_submit() {

	const columns = minion_grid.columns;
	const created = minion_grid.titles;
	const font = minion_grid.font;

	const points = select("mod_minion_points");
	const condition = select("mod_minion_condition");
	const player_condition = select("mod_minion_player_condition");
	const link = check("mod_minion_link");
	const variable_type = select("mod_minion_variable_type");
	const multiple = check("minion_multiple");
	const attitude = check("minion_attitude");
	const resitable = check("minion_resitable");
	const heroic = check("minion_heroic");
	const sacrifice = check("minion_sacrifice");
	const sacrifice_cost = select("mod_minion_sacrifice_cost");
	const attitude_type = select("minion_attitude_type");
	const attitude_attitude = select('minion_attitude_attitude');
	const attitude_trait_type = select("minion_attitude_trait_type");
	const attitude_trait = select("minion_attitude_trait");
	const resitable_check = select("minion_resitable_check");
	const resitable_dc = select("minion_resitable_dc");
	const multiple_value = select("mod_minion_multiple_value");
	const horde = check("mod_minion_horde");

	///const advantage_id = document.getElementById('advantage_id').value;
	const advantage_id = select("create_advantage_select");

	const errors = 'minion-err';
	const err_line = 'minion-err-line';

	response = fetch('/advantage/minion/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'points': points,
			'condition': condition,
			'player_condition': player_condition,
			'link': link,
			'variable_type': variable_type,
			'multiple': multiple,
			'attitude': attitude,
			'resitable': resitable,
			'heroic': heroic,
			'sacrifice': sacrifice,
			'sacrifice_cost': sacrifice_cost,
			'attitude_type': attitude_type,
			'attitude_attitude': attitude_attitude,
			'attitude_trait_type': attitude_trait_type,
			'attitude_trait': attitude_trait,
			'resitable_check': resitable_check,
			'resitable_dc': resitable_dc,
			'multiple_value': multiple_value,
			'horde': horde,
			'columns': columns,
			'created': created,
			'font': font
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			minion_grid.columns.length = 0;
			minion_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, minion_grid, route);
			clear_errors(err_line, errors)

			minion_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}