function check_check() {
	const check = "check_check";
	const title = "check-title";
	const base = 'check-base';
	const entry = "check-entry";

	entry_check(check, title, base, entry);
}

function check_base() {
	const field = 'check_extra';
	const entry =  "check-entry";

	base(field, entry);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	trait_select(select, fill);
}

function check_action_type() {
	const select = 'check_action_type';
	const fill = 'check_action';

	action_select(select, fill);
}

function check_trigger() {
	const select = 'check_trigger';
	const options = [{'val': 'condition', 'div': 'check-condition'},
					{'val': 'conflict', 'div': 'check-conflict'}];
	const entry = 'check-entry';

	select_maxheight_entry(select, options, entry);
}

let check_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function check_submit() {

	const columns = check_grid.columns;
	const created = check_grid.titles;
	const font = check_grid.font;
	
	const benefit = select("check_benefit")
	const check_trigger = select('check_trigger');
	const check_type = select("check_check_type")
	const mod = select("check_mod")
	const circumstance = text("check_circ")
	const trigger = select("check_trigger")
	const when = select("check_when")
	const trait_type = select("check_trait_type")
	const trait = select("check_trait")
	const conflict = select("check_conflict")
	const conflict_range = select("check_conflict_range")
	const conflict_weapon = check("check_conflict_weapon")
	const condition1 = select("check_condition1")
	const condition2 = select("check_condition2")
	const action_type = select("check_action_type")
	const action = select("check_action")
	const free = check("check_free")

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'check-err';
	const err_line = 'check-err-line';

	const route = '/advantage/alt_check/delete/'

	response = fetch('/advantage/alt_check/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'check_trigger': check_trigger,
			'check_type': check_type,
			'mod': mod,
			'circumstance': circumstance,
			'trigger': trigger,
			'when': when,
			'trait_type': trait_type,
			'trait': trait,
			'conflict': conflict,
			'conflict_range': conflict_range,
			'conflict_weapon': conflict_weapon,
			'condition1': condition1,
			'condition2': condition2,
			'action_type': action_type,
			'action': action,
			'free': free
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			check_grid.columns.length = 0;
			check_grid.columns = jsonResponse.rows;

			create_table(jsonResponse, check_grid, route);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)
		}
	})
}
