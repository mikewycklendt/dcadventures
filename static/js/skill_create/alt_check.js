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
	const fields = ['check_attack', 'check_opposed', 'check_dc']
	const entry = 'check-entry';

	reset_all(fields); 
	select_maxheight_shared(select, options, entry);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	id_select(select, fill, trait_select);
}

function check_action_type() {
	const select = 'check_action_type';
	const fill = 'check_action';

	id_select(select, fill, action_select);
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
	
	const check_type = select("check_check_type");
	const mod = select("check_mod");
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
	const degree = select("check_degree");
	const circ = select("check_circ");
	const dc = select("check_dc");
	const time = select("check_time");
	const move = select("check_move");
	const attack = select("check_attack");
	const opposed = select("check_opposed");
	
	///const skill_id = document.getElementById('skill_id').value;
	const skill_id = select("create_bonus_select");

	const errors = 'check-err';
	const err_line = 'check-err-line';

	const select_entry = 'check-entry';
	const selects = 'check-sml';

	const route = '/skill/check/delete/'

	response = fetch('/skill/check/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'columns': columns,
			'created': created,
			'font': font,
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
			'free': free,
			'degree': degree,
			'circ': circ,
			'dc': dc,
			'time': time,
			'move': move,
			'keyword': keyword,
			'attack': attack,
			'opposed': opposed
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

			create_table(jsonResponse, check_grid, route, [selects, select_entry]);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)
		}
	})
}
