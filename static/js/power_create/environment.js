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
	descriptor_base(field);
}

function env_extra() {
	const field = 'env_extra';
	const fill = 'env_cost';
	const ranks = 'env_ranks';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function env_cost() {
	const field = 'env_cost';
	const fill = 'env_ranks';
	const extra = 'env_extra';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
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

	id_select(select, fill, trait_select);
}

function env_visibility_trait() {
	const filter = select('env_visibility_trait_type');
	const fill = 'env_visibility_trait';

	id_select(fill, fill, trait_filter, filter);
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

function env_elements() {
	const check = 'env_elements';
	const div = 'env-elements';
	const entry = 'env-entry';

	check_drop(check, div, entry);
}

function env_condition_temp_type() {
	const select = 'env_condition_temp_type';
	const options = [{'val': ['select', '1', '2', '3'], 'div': 'env-condition-heat'}]
	const selective = [{'val': 'select', 'div': 'env-condition-selective'}]

	select_opacity_shared(select, options);
	select_opacity(select, selective);

}

function env_darkness_descriptor() {
	const check = 'env_darkness_descriptor';
	const div = 'env-darkness-descriptor';

	check_display(check, div);
}

let env_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function env_submit() {

	const columns = env_grid.columns;
	const created = env_grid.titles;
	const font = env_grid.font;

	const extra_id = select("env_extra");
	const radius = text("env_radius");
	const distance = select("env_distance");
	const rank = select("env_rank");
	const condition_check = check("env_condition");
	const impede = check("env_impede");
	const conceal = check("env_conceal");
	const visibility = check("env_visibility");
	const immunity = check("env_immunity");
	const immunity_type = select("env_immunity_type");
	const temp_type = select("env_temp_type");
	const immunity_extremity = select("env_immunity_extremity");
	const immunity_environment = select("env_immunity_environment");
	const immunity_environment_other = text("env_immunity_environment_other");
	const no_penalty = check("env_no_penalty");
	const no_circumstance = check("env_no_circumstance");
	const condition_temp_type = select("env_condition_temp_type");
	const condition_selective = check("env_condition_selective")
	const temp_extremity = select("env_temp_extremity");
	const move_nature = select("env_move_nature");
	const move_speed = select("env_move_speed");
	const move_cost_circ = check("env_move_cost_circ");
	const move_other = text("env_move_other");
	const conceal_type = select("env_conceal_type");
	const darkness_descriptor = check("env_darkness_descriptor");
	const light_check = select("env_light_check");
	const visibility_trait_type = select("env_visibility_trait_type");
	const visibility_trait = select("env_visibility_trait");
	const visibility_mod = select("env_visibility_mod");
	const cost = select("env_cost");
	const ranks = select("env_ranks");
	const elements = check("env_elements");
	const element = select("env_element");
	const element_strength = select("env_element_strength");
	const element_mass = select("env_element_mass");
	
	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
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
			'immunity': immunity,
			'immunity_type': immunity_type,
			'temp_type': temp_type,
			'immunity_extremity': immunity_extremity,
			'immunity_environment': immunity_environment,
			'immunity_environment_other': immunity_environment_other,
			'no_penalty': no_penalty,
			'no_circumstance': no_circumstance,
			'condition_temp_type': condition_temp_type,
			'condition_selective': condition_selective,
			'temp_extremity': temp_extremity,
			'move_nature': move_nature,
			'move_speed': move_speed,
			'move_cost_circ': move_cost_circ,
			'move_other': move_other,
			'conceal_type': conceal_type,
			'light_check': light_check,
			'darkness_descriptor': darkness_descriptor,
			'visibility_trait_type': visibility_trait_type,
			'visibility_trait': visibility_trait,
			'visibility_mod': visibility_mod,
			'cost': cost,
			'ranks': ranks,
			'columns': columns,
			'created': created,
			'font': font,
			'elements': elements,
			'element': element,
			'element_strength': element_strength,
			'element_mass': element_mass
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const insert = jsonResponse.new;
			const items = jsonResponse.new_items;

			new_items(insert, items);

			env_grid.columns.length = 0;
			env_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, env_grid, route);
			clear_errors(err_line, errors)

			env_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}