function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	check_title(check, title, base, entry);
}

function defense_base() {
	const field = 'defense_extra';
	const entry = "defense-entry";

	base(field, entry);
}

function defense_extra() {
	const power_id = select("all_power_select");
	const field = 'defense_extra';
	const fill = 'defense_cost';
	const ranks = 'defense_ranks';
	///const power_id = document.getElementById('power_id');

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function defense_cost() {
	const power_id = select("all_power_select");
	const field = 'defense_cost';
	const fill = 'defense_ranks';
	const extra = 'defense_extra';
	///const power_id = document.getElementById('power_id');

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
}


function defense_reflect() {
	const check = 'defense_reflect';
	const div = 'defense-reflect';
	const entry = 'defense-entry';

	check_drop(check, div, entry);
}

function defense_immunity() {
	const check = 'defense_immunity';
	const div = 'defense-immunity';
	const entry = 'defense-entry'

	check_drop(check, div, entry);
}

function defense_reflect_opposed_trait_type() {
	const select = 'defense_reflect_opposed_trait_type';
	const fill = 'defense_reflect_opposed_trait';
	
	id_select(select, fill, trait_select);
}

function defense_reflect_opposed_trait() {
	const filter = select('defense_reflect_opposed_trait_type');
	const fill = 'defense_reflect_opposed_trait';
	
	id_select(fill, fill, trait_filter, filter);
}

function defense_reflect_resist_trait_type() {
	const select = 'defense_reflect_resist_trait_type';
	const fill = 'defense_reflect_resist_trait';
	
	id_select(select, fill, trait_select);
}

function defense_reflect_resist_trait() {
	const filter = select('defense_reflect_resist_trait_type');
	const fill = 'defense_reflect_resist_trait';
	
	id_select(fill, fill, trait_filter, filter);
}

function defense_reflect_check() {
	const select = 'defense_reflect_check';
	const options = [{'val': 1, 'div': 'defense-reflect-dc'},
					{'val': 2, 'div': 'defense-reflect-opposed'},
					{'val': 6, 'div': 'defense-reflect-resist'}];

	select_opacity(select, options);
}

function defense_immunity_trait_type() {
	const select = 'defense_immunity_trait_type';
	const fill = 'defense_immunity_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function defense_immunity_trait() {
	const filter = select('defense_immunity_trait_type');
	const fill = 'defense_immunity_trait';

	id_select(fill, fill, trait_filter, filter);
}

function defense_immunity_type() {
	const select = 'defense_immunity_type';
	const options = [{'val': ['trait'], 'div': 'defense-immunity-trait'},
					{'val': ['damage'], 'div': 'defense-immunity-damage'},
					{'val': ['descriptor'], 'div': 'defense-immunity-descriptor'},
					{'val': ['consequence'], 'div': 'defense-immunity-consequence'},
					{'val': ['env'], 'div': 'defense-immunity-env'},
					{'val': ['condition_attack', 'condition_effect'], 'div': 'defense-immunity-condition'}]

	select_opacity_shared(select, options);
}

function defense_immunity_consequence() {
	const select = 'defense_immunity_consequence';
	const options = [{'val': '5', 'div': 'defense-immunity-suffocate'}]

	select_opacity(select, options)
}

function defense_immunity_env() {
	const select = 'defense_immunity_env';
	const options = [{'val': 'env', 'div': 'defense-env-immunity-environment'},
					{'val': 'condition', 'div': 'defense-env-immunity-condition'}]
	const fields = ['defense_immunity_temp', 'defense_immunity_extremity', 'defense_immunity_environment'];
	const checks = ['defense_immunity_env_penalty', 'defense_immunity_env_circumstance'];

	reset_all(fields);
	uncheck_all(checks);
	select_opacity(select, options);
}

function defense_immunity_environment() {
	const select = 'defense_immunity_environment';
	const options = [{'val': 'other', 'div': 'defense-env-other'}];
	const entry = 'defense-entry';

	select_maxheight_entry(select, options, entry);
}

function defense_cover() {
	const check = 'defense_cover_check';
	const div = 'defense-cover';
	const entry = 'defense-entry'

	check_drop(check, div, entry);
}

let defense_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function defense_submit() {

	const columns = defense_grid.columns;
	const created = defense_grid.titles;
	const font = defense_grid.font;

	const extra_id = select("defense_extra");
	const defense = select("defense_defense");
	const use = select("defense_use");
	const mod = select("defense_mod");
	const roll = select("defense_roll");
	const outcome = select("defense_outcome");
	const dodge = check("defense_dodge");
	const fortitude = check("defense_fortitude");
	const parry = check("defense_parry");
	const toughness = check("defense_toughness");
	const will = check("defense_will");
	const active = check("defense_active");
	const resist_area = check("defense_resist_area");
	const resist_perception = check("defense_resist_perc");
	const reflect = check("defense_reflect");
	const immunity = check("defense_immunity");
	const reflect_check = select("defense_reflect_check")
	const redirect = check("defense_redirect");
	const immunity_type = select("defense_immunity_type");
	const immunity_trait_type = select("defense_immunity_trait_type");
	const immunity_trait = select("defense_immunity_trait");
	const immunity_descriptor = select("defense_immunity_descriptor");
	const immunity_damage = select("defense_immunity_damage");
	const immunity_rule = select("defense_immunity_rule");
	const cover_check = check("defense_cover_check");
	const cover_type = select("defense_cover_type");
	const immunity_consequence = select("defense_immunity_consequence");
	const immunity_suffocate = select("defense_immunity_suffocate");
	const immunity_env = select("defense_immunity_env");
	const immunity_temp = select("defense_immunity_temp");
	const immunity_extremity = select("defense_immunity_extremity");
	const immunity_environment = select("defense_immunity_environment");
	const immunity_condition = select("defense_immunity_condition")
	const env_other = text("defense_env_other");
	const immunity_env_penalty = check("defense_immunity_env_penalty");
	const immunity_env_circumstance = check("defense_immunity_env_circumstance");
	const multiple = select("defense_multiple");
	const cost = select("defense_cost");
	const ranks = select("defense_ranks");
	

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'defense-err';
	const err_line = 'defense-err-line';

	response = fetch('/power/defense/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'defense': defense,
			'use': use,
			'mod': mod,
			'roll': roll,
			'outcome': outcome,
			'dodge': dodge,
			'fortitude': fortitude,
			'parry': parry,
			'toughness': toughness,
			'will': will,
			'active': active,
			'resist_area': resist_area,
			'resist_perception': resist_perception,
			'reflect': reflect,
			'immunity': immunity,
			'reflect_check': reflect_check,
			'redirect': redirect,
			'immunity_type': immunity_type,
			'immunity_trait_type': immunity_trait_type,
			'immunity_trait': immunity_trait,
			'immunity_descriptor': immunity_descriptor,
			'immunity_damage': immunity_damage,
			'immunity_rule': immunity_rule,
			'cover_check': cover_check,
			'cover_type': cover_type,
			'columns': columns,
			'created': created,
			'font': font,
			'immunity_consequence': immunity_consequence,
			'immunity_suffocate': immunity_suffocate,
			'immunity_env': immunity_env,
			'immunity_temp': immunity_temp,
			'immunity_extremity': immunity_extremity,
			'immunity_environment': immunity_environment,
			'env_other': env_other,
			'immunity_env_penalty': immunity_env_penalty,
			'immunity_env_circumstance': immunity_env_circumstance,
			'immunity_condition': immunity_condition,
			'multiple': multiple,
			'cost': cost,
			'ranks': ranks
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			
			defense_grid.columns.length = 0;
			defense_grid.columns = jsonResponse.rows;
		
			const insert = jsonResponse.new;
			const items = jsonResponse.new_items;

			extra_effect_check(jsonResponse)
			
			new_items(insert, items);
			
			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, defense_grid, route);
			clear_errors(err_line, errors)

			defense_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}