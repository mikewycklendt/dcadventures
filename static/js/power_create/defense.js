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
	
	trait_select(select, fill);
}

function defense_reflect_resist_trait_type() {
	const select = 'defense_reflect_resist_trait_type';
	const fill = 'defense_reflect_resist_trait';
	
	trait_select(select, fill);
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

	trait_select(select, fill);
}

function defense_immunity_type() {
	const select = 'defense_immunity_type';
	const options = [{'val': 'trait', 'div': 'defense-immunity-trait'},
					{'val': 'damage', 'div': 'defense-immunity-damage'},
					{'val': 'descriptor', 'div': 'defense-immunity-descriptor'},
					{'val': 'rule', 'div': 'defense-immunity-rule'}]

	select_opacity(select, options);
}

function defense_cover() {
	const check = 'defense_cover_check';
	const div = 'defense-cover';

	check_opacity(check, div);
}

let defense_grid = {'titles': false,
					'columns': [],
					'font': 80}

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
	const resist_area = check("defense_resist_area");
	const resist_perception = check("defense_resist_perc");
	const reflect = check("defense_reflect");
	const immunity = check("defense_immunity");
	const reflect_action = select("defense_reflect_action");
	const reflect_check = select("defense_reflect_check");
	const reflect_dc = select("defense_reflect_dc");
	const reflect_opposed_trait_type = select("defense_reflect_opposed_trait_type");
	const reflect_opposed_trait = select("defense_reflect_opposed_trait");
	const reflect_resist_trait_type = select("defense_reflect_resist_trait_type");
	const reflect_resist_trait = select("defense_reflect_resist_trait");
	const immunity_type = select("defense_immunity_type");
	const immunity_trait_type = select("defense_immunity_trait_type");
	const immunity_trait = select("defense_immunity_trait");
	const immunity_descriptor = select("defense_immunity_descriptor");
	const immunity_damage = select("defense_immunity_damage");
	const immunity_rule = select("defense_immunity_rule");
	const cover_check = check("defense_cover_check");
	const cover_type = select("defense_cover_type");

	const power_id = document.getElementById('power_id').value;

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
			'resist_area': resist_area,
			'resist_perception': resist_perception,
			'reflect': reflect,
			'immunity': immunity,
			'reflect_action': reflect_action,
			'reflect_check': reflect_check,
			'reflect_dc': reflect_dc,
			'reflect_opposed_trait_type': reflect_opposed_trait_type,
			'reflect_opposed_trait': reflect_opposed_trait,
			'reflect_resist_trait_type': reflect_resist_trait_type,
			'reflect_resist_trait': reflect_resist_trait,
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

			console.log(degree_grid)

			defense_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse);
			row_delete(jsonResponse, route, defense_grid)
			clear_errors(err_line, errors)

			defense_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}