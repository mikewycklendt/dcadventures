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
	const titles = [{'val': '1', 'text': 'Skill Check', 'div': 'check-dc-title'},
					{'val': '6', 'text': 'Resistance Check', 'div': 'check-dc-title'},
					{'val': '2', 'text': 'Opposed Check', 'div': 'check-opposed-title'},
					{'val': '7', 'text': 'Comparison Check', 'div': 'check-opposed-title'}]

	reset_all(fields); 
	select_maxheight_shared(select, options, entry);
	div_text_multiple(select, titles);
}

function check_trait_type() {
	const select = 'check_trait_type';
	const fill = 'check_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function check_trait() {
	const filter = select('check_trait_type');
	const fill = 'check_trait';

	id_select(fill, fill, trait_filter, filter);
}

function check_action_type() {
	const select = 'check_action_type';
	const fill = 'check_action';
	const options = [{'val': 'conflict', 'div': 'check-defenseless'}]
	const entry = 'check-entry';

	id_select(select, fill, action_select);
	select_maxheight_entry(select, options, entry)
}

function check_trigger() {
	const select = 'check_trigger';
	const options = [{'val': 'change', 'div': 'check-conditions'},
					{'val': 'condition', 'div': 'check-condition'},
					{'val': 'variable', 'div': 'check-trigger-variable'},
					{'val': 'opposed', 'div': 'check-trigger-opposed'},
					{'val': 'conflict', 'div': 'check-conflict'},
					{'val': 'sense', 'div': 'check-sense'},
					{'val': 'consequence', 'div': 'check-consequence'},
					{'val': 'target', 'div': 'check-target'}];
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
	const target = select("check_target")
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
	const attack_range = select("check_attack_range");
	const opposed = select("check_opposed");
	const condition = select("check_condition");
	const condition_target = select("check_condition_target");
	const conditions_target = select("check_conditions_target");
	const ranged = select("check_ranged_type")
	const variable = select("check_variable")
	const opponent = select("check_opponent")
	const variable_type = select("check_variable_type")
	const opponent_type = select("check_opponent_type")
	const title = text("check_title");
	const multiple = select("check_multiple");
	const sense = select("check_sense");
	const mental = check("check_mental");
	const maneuver = select("check_maneuver");
	const consequence = select("check_consequence");
	const consequence_target = select("check_consequence_target");
	const defenseless = select("check_defenseless");
	const touch = check("check_touch");
	const target_type = select("check_target_type")

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");

	const errors = 'check-err';
	const err_line = 'check-err-line';

	const select_entry = 'check-entry';
	const selects = 'check-sml';
	const selects_title = 'check-title-sml';
	const title_entry = 'check-title-entry'

	const route = '/power/check/delete/'

	response = fetch('/power/check/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'columns': columns,
			'created': created,
			'font': font,
			'target': target,
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
			'ranged': ranged,
			'keyword': keyword,
			'attack': attack,
			'attack_range': attack_range,
			'opposed': opposed,
			'condition': condition,
			'condition_target': condition_target,
			'conditions_target': conditions_target,
			'variable': variable,
			'opponent': opponent,
			'opponent_type': opponent_type,
			'varible_type': variable_type,
			'title': title,
			'multiple': multiple,
			'sense': sense,
			'mental': mental,
			'maneuver':  maneuver,
			'consequence': consequence,
			'consequence_target': consequence_target,
			'defenseless': defenseless,
			'touch': touch,
			'target_type': target_type
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			extra_effect_check(jsonResponse);

			const id = jsonResponse.id;

			selects_add(id, keyword, selects);
			selects_add(id, keyword, select_entry);
			
			const title_name = jsonResponse.title;
			const title_id = jsonResponse.title_id;
			const add_title = jsonResponse.add_title

			if (add_title == true) {
				selects_add(title_id, title_name, selects_title);
				selects_add(title_id, title_name, title_entry);
			}

			check_grid.columns.length = 0;
			check_grid.columns = jsonResponse.rows;

			create_table('power', jsonResponse, check_grid, route, [selects, select_entry], title_id, [selects_title]);
			clear_errors(err_line, errors)

			check_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)
		}
	})
}
