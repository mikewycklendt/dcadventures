const entry = 'char-entry';

function char_check() {
	const check = "char_check";
	const title = "char-title";
	const base = 'char-base';
	const entry = "char-entry";

	check_title(check, title, base, entry);
}

function char_base() {
	const field ='char_extra';
	const entry = "char-entry";

	base(field, entry)
}

function char_limited() {
	const check = 'char_limited';
	const div = 'char-limited';
	const entry = "char-entry";

	check_drop(check, div, entry);
}

function char_reduced() {
	const check = 'char_reduced';
	const div = 'char-reduced';
	const entry = "char-entry";

	check_drop(check, div, entry);
}

function char_limited_by() {
	const field = 'char_limited_by';
	const options = [{'val': 'other', 'div': 'char-other'},
					{'val': 'emotion', 'div': 'char-emotion'}]

	select_maxheight(field, options);
}

function char_emotion() {
	const field = document.getElementById('char_emotion');
	const value = field.options[field.selectedIndex].value;
	const oth = document.getElementById('char-emotion-other')

	if (value == 'other') {
		oth.style.opacity = '100%';
	} else {
		oth.style.opacity = '0%';
	}
}

function char_limbs() {
	const check = 'char_limbs';
	const div = 'char-limbs';
	const entry = 'char-entry';

	check_drop(check, div, entry)
}

function char_carry() {
	const check = 'char_carry';
	const div = 'char-carry';

	check_drop(check, div, entry);
}

function char_points() {
	const check = 'char_points';
	const div = 'char-points';

	check_drop(check, div, entry);
}

function char_appear() {
	const check = 'char_appear';
	const div = 'char-appear';

	check_drop(check, div, entry)
}

function char_points_trait_type() {
	const select = 'char_points_trait_type'
	const fill = 'char_points_trait'
	
	trait_select(select, fill);
}

function char_insub() {
	const check = 'char_insub';
	const div = 'char-insub';

	check_drop(check, div, entry);
}

function char_reduced_trait_type() {
	const select = 'char_reduced_trait_type';
	const fill = 'char_reduced_trait';

	trait_select(select, fill);
}

function char_trait_type() {
	const select = 'char_trait_type';
	const fill = 'char_trait';

	trait_select(select, fill);
}

function char_size() {
	const tra_field = document.getElementById('char_reduced_trait_type');
	const tra = tra_field.options[tra_field.selectedIndex].value;
	const mod_field = document.getElementById('char_reduced_value');
	const mod = mod_field.options[mod_field.selectedIndex].value;
	const div = document.getElementById('char-reduced-full');

	if (tra == 'size' && mod < 0) {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function char_weaken() {
	const check = 'char_weaken';
	const div = 'char-weaken';
	const entry = 'char-entry';

	check_drop(check, div, entry);
}

function char_weaken_trait_type() {
	const select = 'char_weaken_trait_type';
	const fill = 'char_weaken_trait';

	trait_select(select, fill);
}

function char_weaken_type() {
	const select = 'char_weaken_type';
	const options = [{'val': 'trait', 'div': 'char-weaken-trait'},
					{'val': 'type', 'div': 'char-weaken-type'},
					{'val': 'descriptor', 'div': 'char-weaken-descriptor'}]

	select_opacity(select, options)
}

function char_weaken_broad() {
	const select = document.getElementById('char_weaken_type');
	const value = select.options[select.selectedIndex].value;
	const div = document.getElementById('char-weaken-broad');
	
	if (value == 'type') {
		div.style.opacity = '100%'
	} else if (value == 'descriptor') {
		div.style.opacity = '100%'
	} else {
		div.style.opacity = '0%';
	}
}

let char_grid = {'titles': false,
					'columns': []}

function char_submit() {

	const columns = char_grid.columns;
	const created = char_grid.titles;

	const extra_id = select("char_extra");
	const trait_type = select("char_trait_type");
	const trait = select("char_trait");
	const value = select("char_value");
	const increase = select("char_per");
	const limited = check("char_limited");
	const reduced = check("char_reduced");
	const limbs = check("char_limbs");
	const carry = check("char_carry");
	const sustained = check("char_sustained");
	const permanent = check("char_permanent");
	const points = check("char_points");
	const appear = check("char_appear");
	const insubstantial = check("char_insub");
	const weaken = check("char_weaken");
	const weaken_type = select("char_weaken_type");
	const weaken_trait_type = select("char_weaken_trait_type");
	const weaken_trait = select("char_weaken_trait");
	const weaken_broad = select("char_weaken_broad");
	const weaken_descriptor = select("char_weaken_descriptor");
	const weaken_simultaneous = check("char_simultaneous");
	const limited_by = select("char_limited_by");
	const limited_other = text("char_other");
	const limited_emotion = select("char_emotion");
	const limited_emotion_other = text("char_emotion_other");
	const reduced_trait_type = select("char_reduced_trait_type");
	const reduced_trait = select("char_reduced_trait");
	const reduced_value = select("char_reduced_value");
	const reduced_full = check("char_reduced_full");
	const limbs_continuous = check("char_continuous");
	const limbs_sustained = check("char_sustained");
	const limbs_distracting = check("char_distracting");
	const limbs_projection = check("char_projection");
	const carry_capacity = select("char_carry_capacity");
	const points_value = select("char_points_value");
	const points_trait_type = select("char_points_trait_type");
	const points_trait = select("char_points_trait");
	const points_descriptor = select("char_points_descriptor");
	const appear_target = select("char_appear_target");
	const appear_description = text("char_appear_des");
	const insub_type = select("char_insub_type");
	const insub_description = text("char_insub_des");
	const cost = select("char_cost");
	const ranks = select("char_ranks");

	const power_id = document.getElementById('power_id').value;

	const errors = 'char-err';
	const err_line = 'char-err-line';

	response = fetch('/power/character/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'trait_type': trait_type,
			'trait': trait,
			'value': value,
			'increase': increase,
			'limited': limited,
			'reduced': reduced,
			'limbs': limbs,
			'carry': carry,
			'sustained': sustained,
			'permanent': permanent,
			'points': points,
			'appear': appear,
			'insubstantial': insubstantial,
			'weaken': weaken,
			'weaken_type': weaken_type,
			'weaken_trait_type': weaken_trait_type,
			'weaken_trait': weaken_trait,
			'weaken_broad': weaken_broad,
			'weaken_descriptor': weaken_descriptor,
			'weaken_simultaneous': weaken_simultaneous,
			'limited_by': limited_by,
			'limited_other': limited_other,
			'limited_emotion': limited_emotion,
			'limited_emotion_other': limited_emotion_other,
			'reduced_trait_type': reduced_trait_type,
			'reduced_trait': reduced_trait,
			'reduced_value': reduced_value,
			'reduced_full': reduced_full,
			'limbs_continuous': limbs_continuous,
			'limbs_sustained': limbs_sustained,
			'limbs_distracting': limbs_distracting,
			'limbs_projection': limbs_projection,
			'carry_capacity': carry_capacity,
			'points_value': points_value,
			'points_trait_type': points_trait_type,
			'points_trait': points_trait,
			'points_descriptor': points_descriptor,
			'appear_target': appear_target,
			'appear_description': appear_description,
			'insub_type': insub_type,
			'insub_description': insub_description,
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

		} else {

		}
	})
}