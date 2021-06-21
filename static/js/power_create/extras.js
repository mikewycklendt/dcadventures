function extra_extra_effect() {
	const check = 'extra_extra_effect';
	const row = 'extras-extra-effect';
	const entry = 'extras-entry';

	check_drop(check, row, entry);
}

function extra_target_check() {
	const check = 'extra_target_check';
	const div = 'extras-target';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_action_check() {
	const check = 'extra_action_check';
	const div = 'extras-action';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_routine() {
	const check = 'extra_routine';
	const div =  'extras-skill';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_skill_type() {
	const select = 'extra_skill_type';
	const fill = 'extra_skill';

	id_select(select, fill, skill_select);
}

function extra_range_check() {
	const check = 'extra_range_check';
	const div = 'extras-range';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_range() {
	const check = 'ranged_check';
	const base = 'ranged-base';
	const entry = 'ranged-entry';
	const field = 'extra_range';
	const value = '5';
	
	select_entry(check, base, entry, field, value);
}

function extra_action() {
	const select = 'extra_action';
	const options = [{'val': '3', 'div': 'extra-action-limit'}]
	const fields = ['extra_action_limit']

	reset_all(fields);
	select_opacity(select, options);
}

function extra_required_check() {
	const check = 'extra_required_check';
	const div = 'extras-required';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_auto() {
	const check = 'extra_auto';
	const div = 'extras-auto';
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_auto_type() {
	const select = 'extra_auto_type';
	const options = [{'val': 'check', 'div': 'extra-auto-check'},
					{'val': 'check_type', 'div': 'extra-auto-check-type'},
					{'val': 'opposed', 'div': 'extra-auto-opposed'},
					{'val': 'opposed_type', 'div': 'extra-auto-opposed-type'}]

	select_opacity(select, options);
}

function extra_power_rank() {
	const check = 'extra_power_rank'
	const checks = ['extra_flat']

	uncheck_check(check, checks);
}

function extra_flat() {
	const check = 'extra_flat';
	const checks = ['extra_power_rank']

	uncheck_check(check, checks);
}

function extra_ranks_check() {
	const check = 'extra_ranks_check';
	const div = 'extras-ranks-check'
	const entry = 'extras-entry';

	check_drop(check, div, entry);
}

function extra_required_power() {
	const select = 'extra_required_power';
	const div = 'extra-required-power-rank';

	select_opacity_any(select, div);
}

let extras_grid = {'titles': false,
				'columns': [],
				'font': 80,
				'mod': []}

function extras_submit() {

	const columns = extras_grid.columns;
	const created = extras_grid.titles;
	const font = extras_grid.font;

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const inherit = select("extra_inherit");
	const name = text("extra_name");
	const des = text("extra_des");
	const cost = select("extra_cost");
	const ranks = select("extra_rank");
	const alternate = check("extra_alternate");
	const flat = check("extra_flat");
	const stack = check("extra_stack");
	const power_rank = check("extra_power_rank");
	const type = select("extra_type");
	const required_check = check("extra_required_check");
	const required = select("extra_required");
	const required_power = select("extra_required_power");
	const required_power_rank = select("extra_required_power_rank");
	const extra_effect = check("extra_extra_effect");
	const extra_effect_count = select("extra_extra_effect_count");
	const variable = check("extra_variable");
	const character = check("extra_character");
	const circ = check("extra_circ");
	const create = check("extra_create");
	const damage = check("extra_damage");
	const dc = check("extra_dc");
	const defense = check("extra_defense");
	const degree = check("extra_degree");
	const env = check("extra_env");
	const minion = check("extra_minion");
	const mod = check("extra_mod");
	const move = check("extra_move");
	const opposed = check("extra_opposed");
	const ranged = check("extra_ranged");
	const sense = check("extra_sense");
	const time = check("extra_time");
	const target = select("extra_target");
	const target_type = select("extra_target_type");
	const target_check = check("extra_target_check");
	const action_check = check("extra_action_check");
	const action = select("extra_action");
	const action_type = select("extra_action_type");
	const action_limit = select("extra_action_limit");
	const routine = check("extra_routine");
	const skill = select("extra_skill");
	const skill_type = select("extra_skill_type");
	const range_check = check("extra_range_check");
	const range = select("extra_range");
	const auto = check("extra_auto");
	const auto_type = select("extra_auto_type");
	const auto_check = select("extra_auto_check");
	const auto_check_type = select("extra_auto_check_type");
	const auto_opposed = select("extra_auto_opposed");
	const auto_opposed_type = select("extra_auto_opposed_type");
	const ranks_check = check("extra_ranks_check");
	const ranks_type = select("extra_ranks_check");
	const rank = select("extra_ranks");

	
	const errors = 'extras-err';
	const err_line = 'extras-err-line';

	const selects = 'extra-select';
	const selects_sml = 'extra-sml'
	const selects_var = 'extra-cost-select';
	const selects_rank = 'extra-rank-select';

	response = fetch('/power/extras/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'columns': columns,
			'created': created,
			'font': font,
			'name': name,
			'cost': cost,
			'ranks': ranks,
			'des': des,
			'inherit': inherit,
			'alternate': alternate,
			'flat': flat,
			'stack': stack,
			'power_rank': power_rank,
			'type': type,
			'required_check': required_check,
			'required': required,
			'required_power': required_power,
			'required_power_rank': required_power_rank,
			'extra_effect': extra_effect,
			'extra_effect_count': extra_effect_count,
			'variable': variable,
			'character': character,
			'circ': circ,
			'create': create,
			'damage': damage,
			'dc': dc,
			'defense': defense,
			'degree': degree,
			'env': env,
			'minion': minion,
			'mod': mod,
			'move': move,
			'opposed': opposed,
			'ranged': ranged,
			'sense': sense,
			'time': time,
			'target_type': target_type,
			'target': target,
			'target_check': target_check,
			'action_check': action_check,
			'action': action,
			'action_type': action_type,
			'action_limit': action_limit,
			'routine': routine,
			'skill_type': skill_type,
			'skill': skill,
			'range_check': range_check,
			'range': range,
			'auto': auto,
			'auto_type': auto_type,
			'auto_check': auto_check,
			'auto_check_type': auto_check_type,
			'auto_opposed': auto_opposed,
			'auto_opposed_type': auto_opposed_type,
			'ranks_check': ranks_check,
			'ranks_type': ranks_type,
			'rank': rank
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

			selects_add(id, name, selects);
			selects_add(id, name, selects_sml);

			if (cost == 'x') {
				selects_add(id, name, selects_var);
			}

			if (flat == false) {
				selects_add(id, name, selects_rank);
			}

			extras_grid.columns.length = 0;
			extras_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, extras_grid, route, [selects, selects_sml, selects_var, selects_rank]);
			clear_errors(err_line, errors)

			extras_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}