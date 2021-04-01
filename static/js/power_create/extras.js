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
	const required = select("extra_required");
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
			'required': required,
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
			'target_check': target_check
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