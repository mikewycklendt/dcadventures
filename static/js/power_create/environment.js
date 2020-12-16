function env_check() {
	const check = "env_check";
	const title = "env-title";
	const base = 'env-base';
	const entry = "env-entry";

	check_title(check, title, base, entry);
}

function env_base() {
	const field = 'env_extra';
	const entry = "env-entry";

	base(field, entry);
}

function env_condition() {
	const check = 'env_condition';
	const div = 'env-condition';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_impede() {
	const check = 'env_impede';
	const div = 'env-move';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_conceal() {
	const check = 'env_conceal';
	const div = 'env-conceal';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_visibility() {
	const check = 'env_visibility';
	const div = 'env-visibility';
	const entry = "env-entry";

	check_drop(check, div, entry);
}

function env_move_other() {
	const field = document.getElementById('env_move_nature');
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById('env-move-other');

	if (value == 'other') {
		div.style.opacity = '100%';
	} else  {
		div.style.opacity = '0%';
	}
}


function env_visibility_trait_type() {
	const select = 'env_visibility_trait_type'
	const fill = 'env_visibility_trait'

	trait_select(select, fill)
}

function env_immunity() {
	const check = 'env_immunity';
	const div = 'env-immunity'
	const entry = 'env-entry';

	check_drop(check, div, entry);
}

function env_immunity_environment() {
	const select = 'env_immunity_environment';
	const options = [{'val': 'other', 'div': 'env-immunity-other'}]
	const entry = 'env-entry';

	select_maxheight_entry(select, options, entry);
}

function env_immunity_type() {
	const select = 'env_immunity_type';
	const options = [{'val': 'condition', 'div': 'env-immunity-condition'},
					{'val': 'environment', 'div': 'env-immunity-environment'}]

	select_opacity(select, options);
}

let env_grid = {'titles': false,
					'columns': []}

function env_submit() {

	const columns = env_grid.columns;
	const created = env_grid.titles;

	const extra_id = select("env_extra");
	const radius = text("env_radius");
	const distance = select("env_distance");
	const rank = select("env_rank");
	const condition_check = check("env_condition");
	const impede = check("env_impede");
	const conceal = check("env_conceal");
	const visibility = check("env_visibility");
	const selective = check("env_selective");
	const immunity = check("env_immunity");
	const immunity_type = select("env_immunity_type");
	const temp_type = select("env_temp_type");
	const immunity_extremity = select("env_immunity_extremity");
	const immunity_environment = select("env_immunity_environment");
	const no_penalty = check("env_no_penalty");
	const no_circumstance = check("env_no_circumstance");
	const immunity_other = text("env_immunity_other");
	const condition_temp_type = select("env_condition_temp_type");
	const temp_extremity = select("env_temp_extremity");
	const move_nature = select("env_move_nature");
	const move_speed = select("env_move_speed");
	const move_cost_circ = check("env_move_cost_circ");
	const move_other = text("env_move_other");
	const conceal_type = check("env_conceal_type");
	const visibility_trait_type = select("env_visibility_trait_type");
	const visibility_trait = select("env_visibility_trait");
	const visibility_mod = select("env_visibility_mod");
	const cost = select("env_cost");
	const ranks = select("env_ranks");

	const power_id = document.getElementById('power_id').value;

	const errors = 'env-err';
	const err_line = 'env-err-line';

	response = fetch('/power/environment/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'radius': radius,
			'distance': distance,
			'rank': rank,
			'condition_check': condition_check,
			'impede': impede,
			'conceal': conceal,
			'visibility': visibility,
			'selective': selective,
			'immunity': immunity,
			'immunity_type': immunity_type,
			'temp_type': temp_type,
			'immunity_extremity': immunity_extremity,
			'immunity_environment': immunity_environment,
			'no_penalty': no_penalty,
			'no_circumstance': no_circumstance,
			'immunity_other': immunity_other,
			'condition_temp_type': condition_temp_type,
			'temp_extremity': temp_extremity,
			'move_nature': move_nature,
			'move_speed': move_speed,
			'move_cost_circ': move_cost_circ,
			'move_other': move_other,
			'conceal_type': conceal_type,
			'visibility_trait_type': visibility_trait_type,
			'visibility_trait': visibility_trait,
			'visibility_mod': visibility_mod,
			'cost': cost,
			'ranks': ranks,
			'columns': columns,
			'created': created
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			env_grid.columns = jsonResponse.columns;
			env_grid.titles = jsonResponse.created;

			create_table(jsonResponse);
		} else {

		}
	})
}