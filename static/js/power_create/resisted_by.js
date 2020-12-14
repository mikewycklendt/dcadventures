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

	trait_select(select, fill);
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

let resist_grid = {'titles': false,
					'columns': []}

function resist_submit() {

	const columns = resist_grid.columns;

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
			'columns': columns
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

		} else {

		}
	})

}