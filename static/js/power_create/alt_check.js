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

function check_check_type() {
	const select = 'check_check_type';
	const options = [{'val': ['5'], 'div': 'check-attack'}, 
					{'val': ['1', '6'], 'div': 'check-dc'}, 
					{'val': ['2', '7'], 'div': 'check-opposed'}]
	const fields = ['check_attack', 'check_opposed', 'check_dc_value', 'check_dc_type']
	const entry = 'check-entry';

	reset_all(fields); 
	select_maxheight_shared(select, options, entry);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	id_select(select, fill, trait_select);
}

function check_trait() {
	const filter = select('check_trait_type');
	const fill = 'check_trait';

	id_select(fill, fill, trait_filter, filter);
}

function check_action_type() {
	const select = 'check_action_type';
	const fill = 'check_action';

	id_select(select, fill, action_select);
}

function check_trigger() {
	const select = 'check_trigger';
	const options = [{'val': 'change', 'div': 'check-conditions'},
					{'val': 'condition', 'div': 'check-condition'},
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
	
	const extra_id = select("check_extra");
	const check_type = select("check_check_type");
	const circumstance = text("check_circ");
	const trigger = select("check_trigger");
	const when = select("check_when");
	const trait_type = select("check_trait_type");
	const trait = select("check_trait");
	const conflict = select("check_conflict");
	const conflict_range = select("check_conflict_range");
	const conflict_weapon = check("check_conflict_weapon");
	const condition1 = select("check_condition1");
	const condition2 = select("check_condition2");
	const action_type = select("check_action_type");
	const action = select("check_action");
	const free = check("check_free");
	const keyword = text("check_keyword");
	const degree = select("check_degree_type");
	const circ = select("check_circ_type");
	const dc = select("check_dc_type");
	const dc_value = select("check_dc_value");
	const time = select("check_time_type");
	const move = select("check_move_type");
	const attack = select("check_attack");
	const opposed = select("check_opposed");
	const condition = select("check_condition");
	const condition_target = select("check_condition_target");
	const conditions_target = select("check_conditions_target");
	

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'check-err';
	const err_line = 'check-err-line';

	const select_entry = 'check-entry';
	const selects = 'check-sml';

	const route = '/power/check/delete/'

	response = fetch('/power/check/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'columns': columns,
			'created': created,
			'font': font,
			'check_type': check_type,
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
			'free': free,
			'degree': degree,
			'circ': circ,
			'dc': dc,
			'dc_value': dc_value,
			'time': time,
			'move': move,
			'keyword': keyword,
			'attack': attack,
			'opposed': opposed,
			'condition': condition,
			'condition_target': condition_target,
			'conditions_target': conditions_target
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

			selects_add(id, keyword, selects);
			selects_add(id, keyword, select_entry);

			check_grid.columns.length = 0;
			check_grid.columns = jsonResponse.rows;

			create_table('power', jsonResponse, check_grid, route, [selects, select_entry], id);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)
		}
	})
}
