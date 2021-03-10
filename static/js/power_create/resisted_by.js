function resist_check() {
	const check = "resist_check";
	const title = "resist-title";
	const base = 'resist-base';
	const entry = "resist-entry"

	check_title(check, title, base, entry);
}


function resist_base() {
	const field = 'resist_extra';
	const entry = "resist-entry";

	base(field, entry);
}

function resist_type() {
	const select = 'resist_trait_type';
	const fill = 'resist_trait';

	id_select(select, fill, trait_select);
}

function resist_trait() {
	const filter = select('resist_trait_type');
	const fill = 'resist_trait';

	id_select(fill, fill, trait_filter, filter);
}

function resist_effect() {
	const field = "resist_eft";
	const options = [{'val': 'condition', 'div': "resist-condition"},
					{'val': 'damage', 'div': "resist-damage"},
					{'val': 'nullify', 'div': "resist-nullify"},
					{'val': 'trait', 'div': "resist-weaken"},
					{'val': 'level', 'div': "resist-level"}];

	select_maxheight(field, options);
}

function resist_level_type() {
	const select = 'resist_level_type';
	const fill = 'resist_level';

	id_select(select, fill, level_select);
}

let resist_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function resist_submit() {

	const columns = resist_grid.columns;
	const created = resist_grid.titles;
	const font = resist_grid.font;

	const extra_id = select("resist_extra");
	const trait_type = select("resist_trait_type");
	const dc = select("resist_dc");
	const mod = select("resist_mod");
	const description = text("range_desc");
	const trait = select("resist_trait");
	const effect = select("resist_eft");
	const degree = select("resist_deg");
	const descriptor = select("resist_descriptor");
	const level = select('resist_level');
	const weaken_max = select("resist_weaken_max");
	const weaken_restored = select("resist_weaken_restored");
	const condition1 = select("resist_con1");
	const condition2 = select("resist_con2");
	const damage =  select("resist_dam");
	const strength = check("resist_strength");
	const nullify_descriptor = select("resist_nullify_descriptor");
	const nullify_alternate = select("resist_nullify_alternate");
	const extra_effort = check("resist_extra_effort");

	const power_id = document.getElementById('power_id').value;

	const errors = 'resist-err';
	const err_line = 'resist-err-line';

	response = fetch('/power/resisted_by/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'trait_type': trait_type,
			'dc': dc,
			'mod': mod,
			'description': description,
			'trait': trait,
			'effect': effect,
			'level': level,
			'degree': degree,
			'descriptor': descriptor,
			'weaken_max': weaken_max,
			'weaken_restored': weaken_restored,
			'condition1': condition1,
			'condition2': condition2,
			'damage': damage,
			'strength': strength,
			'nullify_descriptor': nullify_descriptor,
			'nullify_alternate': nullify_alternate,
			'extra_effort': extra_effort,
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

			resist_grid.columns.length = 0;
			resist_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, resist_grid, route);
			clear_errors(err_line, errors)

			resist_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}