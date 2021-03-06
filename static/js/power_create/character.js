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

	base(field, entry);
	descriptor_base(field);
}

function char_extra() {
	const power_id = select("all_power_select");
	///const power_id = document.getElementById('power_id');
	const field = 'char_extra';
	const fill = 'char_cost';
	const ranks = 'char_ranks';

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function char_cost() {
	const power_id = select("all_power_select");
	///const power_id = document.getElementById('power_id');
	const field = 'char_cost';
	const fill = 'char_ranks';
	const extra = 'char_extra';

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
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
	
	id_select(select, fill, trait_select, variable_sub);
}

function char_points_trait() {
	const filter = select('char_points_trait_type');
	const fill = 'char_points_trait';
	
	id_select(fill, fill, trait_filter, filter);
}

function char_insub() {
	const check = 'char_insub';
	const div = 'char-insub';

	check_drop(check, div, entry);
}

function char_insub_type() {
	const select = 'char_insub_type';
	const options = [{'val': 'energy', 'div': 'char-insub-descriptor'}];
	const fields = ['char_insub_descriptor']

	reset_all(fields);
	select_opacity(select, options);
}

function char_reduced_trait_type() {
	const select = 'char_reduced_trait_type';
	const fill = 'char_reduced_trait';
	const options = [{'val': ['speed', 'size', 'mass_rank'], 'div': 'char-penalty'}]
	const checks = ['char_penalty']

	uncheck_all(checks);
	id_select(select, fill, trait_select, variable_sub);
	select_opacity_if_not(select, options)
}

function char_reduced_trait() {
	const filter = select('char_reduced_trait_type');
	const fill = 'char_reduced_trait';

	id_select(fill, fill, trait_filter, filter);
}

function char_trait_type() {
	const select = 'char_trait_type';
	const fill = 'char_trait';
	const options = [{'val': ['speed', 'size', 'mass_rank'], 'div': 'char-bonus'}]
	const checks = ['char_bonus']

	uncheck_all(checks);
	id_select(select, fill, trait_select, variable_sub);
	select_opacity_if_not(select, options)
}

function char_trait() {
	const filter = select('char_trait_type');
	const fill = 'char_trait';

	id_select(fill, fill, trait_filter, filter);
}

function char_meta() {
	const check = 'char_meta';
	const div = 'char-meta';
	const entry = 'char-entry';

	check_drop(check, div, entry);
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

	id_select(select, fill, trait_select);
}

function char_weaken_trait() {
	const filter = select('char_weaken_trait_type');
	const fill = 'char_weaken_trait';

	id_select(fill, fill, trait_filter, filter);
}

function char_weaken_type() {
	const select = 'char_weaken_type';
	const options = [{'val': 'trait', 'div': 'char-weaken-trait'},
					{'val': 'type', 'div': 'char-weaken-type'},
					{'val': 'descriptor', 'div': 'char-weaken-descriptor'}];
	const broad = [{'val': ['type', 'descriptor'], 'div': 'char-weaken-broad'}];
	const checks = ['char_weaken_simultaneous'];

	uncheck_all(checks);
	select_opacity(select, options);
	select_opacity_shared(select, broad);
}


function char_appear_creature() {
	const select = 'char_appear_creature';
	const fill = 'char_appear_creature_narrow';
	const options = [{'val': 'other', 'div': 'char-appear-creature-other', 'text': 'Other Broad Form'}];
	const entry = 'char-entry';
	const div = 'char-appear-creature-other-title';

	select_maxheight_entry(select, options, entry);
	id_select(select, fill, narrow_creature_select, other_var_sub);
	div_text(select, div, options);
}

function char_appear_creature_narrow() {
	const select = 'char_appear_creature_narrow';
	const options = [{'val': 'other', 'div': 'char-appear-creature-other', 'text': 'Other Narrow Form'}];
	const entry = 'char-entry';
	const div = 'char-appear-creature-other-title';

	select_maxheight_entry(select, options, entry);
	div_text(select, div, options);
}

function char_appear_form() {
	const select = 'char_appear_form';
	const options = [{'val': ['broad', 'narrow'], 'div': 'char-appear-broad'},
					{'val': ['narrow'], 'div': 'char-appear-narrow'},
					{'val': ['single'], 'div': 'char-appear-single'}];
	const fields = ['char_appear_creature_narrow', 'char_appear_creature'];
	const text = ['char_appear_des'];
	const other = [{'val': 'other', 'div': 'char-appear-creature-other'}];
	const entry = 'char-entry';
	const checks = ["char_appear_costume"];
	const base = [{'val': ['broad', 'narrow', 'single'], 'div': 'char-appear-form'},
					{'val': ['quick'], 'div': 'char-appear-quick'}];

	uncheck_all(checks);
	select_maxheight_entry(select, other, entry);
	reset_all(fields);
	reset_text(text);
	select_opacity_shared(select, base);
	select_opacity_shared(select, options);
}

function char_sustained() {
	const check = 'char_sustained';
	const checks = ['char_permanent'];

	uncheck_check(check, checks);
}

function char_permanent() {
	const check = 'char_permanent';
	const checks = ['char_sustained'];

	uncheck_check(check, checks);
}

let char_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

let char_counts = {'count': 0, 'trait': 0, 'insub': 0}

function char_submit() {

	const columns = char_grid.columns;
	const created = char_grid.titles;
	const font = char_grid.font;

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
	const weaken_opposed_type = select("char_weaken_opposed_type");
	const weaken_degree_type = select("char_weaken_degree_type")
	const weaken_trait_type = select("char_weaken_trait_type");
	const weaken_trait = select("char_weaken_trait");
	const weaken_broad = select("char_weaken_broad");
	const weaken_descriptor = select("char_weaken_descriptor");
	const weaken_simultaneous = check("char_weaken_simultaneous");
	const limited_by = select("char_limited_by");
	const limited_other = text("char_other");
	const limited_emotion = select("char_emotion");
	const limited_emotion_other = text("char_emotion_other");
	const reduced_trait_type = select("char_reduced_trait_type");
	const reduced_trait = select("char_reduced_trait");
	const reduced_value = select("char_reduced_value");
	const reduced_rank = select("char_reduced_rank");
	const reduced_full = check("char_reduced_full");
	const limbs_count = select("char_limbs_count")
	const limbs_rank = check("char_limbs_rank")
	const limbs_continuous = check("char_limbs_continuous");
	const limbs_sustained = check("char_limbs_sustained");
	const limbs_projection = check("char_limbs_projection");
	const limbs_condition = select("char_limbs_condition");
	const limbs_duration = select("char_limbs_duration")
	const carry_capacity = select("char_carry_capacity");
	const carry_internal = check("char_carry_internal");
	const carry_mass = select("char_carry_mass");
	const points_value = select("char_points_value");
	const points_trait_type = select("char_points_trait_type");
	const points_trait = select("char_points_trait");
	const points_descriptor = select("char_points_descriptor");
	const appear_form = select("char_appear_form");
	const appear_target = select("char_appear_target");
	const appear_description = text("char_appear_des");
	const appear_creature = select("char_appear_creature")
	const appear_creature_narrow = select("char_appear_creature_narrow")
	const appear_creature_other = text("char_appear_creature_other");
	const appear_costume = check("char_appear_costume");
	const insub_type = select("char_insub_type");
	const insub_descriptor = select("char_insub_descriptor");
	const insub_description = text("char_insub_des");
	const cost = select("char_cost");
	const ranks = select("char_ranks");
	const multiple = select("char_multiple");
	const points_type = select("char_points_type");
	const meta = check("char_meta");
	const metamorph = select("char_metamorph");
	const penalty = check("char_penalty")
	const bonus = check("char_bonus");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");

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
			'weaken_opposed_type': weaken_opposed_type,
			'weaken_degree_type': weaken_degree_type,
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
			'reduced_rank': reduced_rank,
			'reduced_full': reduced_full,
			'limbs_count': limbs_count,
			'limbs_rank': limbs_rank,
			'limbs_continuous': limbs_continuous,
			'limbs_sustained': limbs_sustained,
			'limbs_projection': limbs_projection,
			'limbs_condition': limbs_condition,
			'limbs_duration': limbs_duration,
			'carry_capacity': carry_capacity,
			'carry_internal': carry_internal,
			'carry_mass': carry_mass,
			'points_type': points_type,
			'points_value': points_value,
			'points_trait_type': points_trait_type,
			'points_trait': points_trait,
			'points_descriptor': points_descriptor,
			'appear_form': appear_form,
			'appear_target': appear_target,
			'appear_description': appear_description,
			'appear_creature': appear_creature,
			'appear_creature_narrow': appear_creature_narrow,
			'appear_creature_other': appear_creature_other,
			'appear_costume': appear_costume,
			'insub_type': insub_type,
			'insub_descriptor': insub_descriptor,
			'insub_description': insub_description,
			'cost': cost,
			'ranks': ranks,
			'columns': columns,
			'created': created,
			'font': font,
			'multiple': multiple,
			'meta': meta,
			'metamorph': metamorph,
			'penalty': penalty,
			'bonus': bonus
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

			extra_effect_check(jsonResponse)
			
			if (trait != '' || reduced_trait != '') {
				selects_add('trait', 'Changes to Traits Permanent', 'permanent-sml', char_counts.trait);
				char_counts.trait += 1;
			}

			if (insubstantial === true) {
				selects_add('insub', 'Permanently Insubstantial', 'permanent-sml', char_counts.insub);	
				selects_add('body', 'Effects Speecific Parts of Body', 'precise-sml', char_counts.insub);
				char_counts.insub += 1;
			}
			
			char_grid.columns.length = 0;
			char_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, char_grid, route);
			clear_errors(err_line, errors)
			
			char_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}