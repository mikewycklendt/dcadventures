function create_check() {
	const check = "create_check";
	const title = "create-title";
	const base = 'create-base';
	const entry = "create-entry";

	check_title(check, title, base, entry);
}

function create_base() {
	const field = 'create_extra';
	const entry = "create-entry";

	base(field, entry);
	descriptor_base(field);
}

function create_extra() {
	const field = 'create_extra';
	const fill = 'create_cost';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");
	const ranks = 'create_ranks';

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function create_cost() {
	const field = 'create_cost';
	const fill = 'create_ranks';
	const extra = 'create_extra';
	///const power_id = document.getElementById('power_id');
	const power_id = select("all_power_select");

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
}


function create_moveable() {
	const div = document.getElementById('create-move');
	const check = document.getElementById('create_moveable');
	const entry = document.getElementById('create-entry');
	const check2 = document.getElementById('create_stationary');

	if (check.checked == true || check2.checked == true) {
			div.style.display = 'grid';
			div.style.maxHeight = div.scrollHeight + 'px';
			entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	} else if (check.checked == false && check2.checked == false) {
			div.style.maxHeight = '0px';
			setTimeout(function(){div.style.display = 'none';}, 400)
			entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_trap() {
	const check = 'create_trap';
	const div = 'create-trap';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_ranged() {
	const check = 'create_ranged';
	const div = 'create-ranged';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_weapon() {
	const check = 'create_weapon';
	const div = 'create-weapon';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_support() {
	const check = 'create_support';	
	const div = 'create-support';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_move_player() {
	const select = 'create_move_player';
	const options = [{'val': 'check', 'div': 'create-move-check'}];

	select_opacity(select, options);
}

function create_move_opponent_check() {
	const check = 'create_move_opponent_check';
	const div = 'create-move-opp';

	check_opacity(check, div);
}

function create_trap_type() {
	const field = 'create_trap_type';
	const options = [{'val': 'dc', 'div': 'create-trap-dc'},
				{'val': 'trait', 'div': 'create-trap-trait'}];

	select_maxheight(field, options);
}

function create_trap_trait_type() {
	const select = 'create_trap_trait_type';
	const fill = 'create_trap_trait';

	id_select(select, fill, trait_select);
}

function create_trap_trait() {
	const filter = select('create_trap_trait_type');
	const fill = 'create_trap_trait';

	id_select(fill, fill, trait_filter, filter);
}

function create_trap_resist_check() {
	const field = 'create_trap_resist_check';
	const update = 'create_trap_resist_trait';

	id_select(field, update, trait_select);
}

function create_trap_resist_trait() {
	const filter = select('create_trap_resist_check');
	const update = 'create_trap_resist_trait';

	id_select(update, update, trait_filter, filter);
}

function create_ranged_type() {
	const field = document.getElementById('create_ranged_type');
	const value = field.options[field.selectedIndex].value;
	const dc = 'create-ranged-dc';
	const tr = 'create-ranged-trait'

	if (value == 'dc') {
		hide_maxheight(tr);
		show_maxheight(dc);
	} else if (value == 'target' || value == 'player') {
		hide_maxheight(dc);
		show_maxheight(tr);
	} else {
		hide_maxheight(dc);
		hide_maxheight(tr);
	}
}

function create_ranged_trait_type() {
	const field = 'create_ranged_trait_type';
	const update = 'create_ranged_trait';

	id_select(field, update, trait_select);
}

function create_ranged_trait() {
	const filter = select('create_ranged_trait_type');
	const update = 'create_ranged_trait';

	id_select(update, update, trait_filter, filter);
}

function create_ranged_damage_type() {
	const field = document.getElementById('create_ranged_damage_type');
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById('create-ranged-damage')

	if (value == 'value') {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function create_weapon_trait_type() {
	const field = 'create_weapon_trait_type';
	const update = 'create_weapon_trait';

	id_select(field, update, trait_select);
}

function create_weapon_trait() {
	const filter = select('create_weapon_trait_type');
	const update = 'create_weapon_trait';

	id_select(update, update, trait_filter, filter);
}

function create_weapon_damage_type() {
	const field = document.getElementById('create_weapon_damage_type');
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById('create-weapon-value')

	if (value == 'value') {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function create_support_strengthen() {
	const check = 'create_support_strengthen';
	const div = 'create-support-strengthen';

	check_opacity(check, div);
}

function create_transform() {
	const check = 'create_transform';
	const div = 'create-transform';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_trap_escape() {
	const check = 'create_trap_escape';
	const div = 'create-trap-escape';

	check_display(check, div);
}

function create_duration() {
	const check = 'create_duration';
	const div = 'create-duration';
	const entry = 'create-entry';

	check_drop(check, div, entry);
}

function create_duration_type() {
	const select = 'create_duration_type';
	const options = [{'val': ['4', '5'], 'div': 'create-duration-innate'}];
	const checks = ['create_duration_innate']

	uncheck_all(checks);
	select_opacity_shared(select, options);
}

let create_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

let create_counts = {'count': 0}

function create_submit() {

	const columns = create_grid.columns;
	const created = create_grid.titles;
	const font = create_grid.font;

	const extra_id = select("create_extra");
	const solidity = select("create_solidity");
	const visibility = select("create_visibility");
	const complexity = select("create_complexity");
	const volume = select("create_volume");
	const toughness = select("create_toughness");
	const mass = select("create_mass");
	const damageable = check("create_damageable");
	const maintained = check("create_maintained");
	const repairable = check("create_repairable");
	const moveable = check("create_moveable");
	const stationary = check("create_stationary");
	const trap = check("create_trap");
	const ranged = check("create_ranged");
	const weapon = check("create_weapon");
	const support = check("create_support");
	const real = check("create_real");
	const cover = check("create_cover");
	const conceal = check("create_conceal");
	const incoming = check("create_incoming");
	const outgoing = check("create_outgoing");
	const transform = check("create_transform");
	const transform_type = select("create_transform_type");
	const transform_start_mass = select("create_transform_start_mass");
	const transfom_mass = select("create_transfom_mass");
	const transform_start_descriptor = select("create_transform_start_descriptor");
	const transform_end_descriptor = select("create_transform_end_descriptor");
	const move_player = select("create_move_player");
	const move_check =  select("create_move_check");
	const move_opponent_check = check("create_move_opponent_check");
	const move_opposed =  select("create_move_opposed");
	const trap_check = select("create_trap_check");
	const trap_resist = select("create_trap_resist");
	const trap_opposed = select("create_trap_opposed");
	const trap_escape = check("create_trap_escape");
	const weapon_damage = select("create_weapon_damage");
	const support_strength = select("create_support_strength");
	const support_strengthen = check("create_support_strengthen");
	const support_action = select("create_support_action");
	const support_action_rounds = select("create_support_action_rounds");
	const support_effort = select("create_support_effort");
	const support_effort_rounds = select("create_support_effort_rounds");
	const cost = select("create_cost_per_rank");
	const ranks = select("create_ranks");
	const ranged_damage = select("create_ranged_damage")
	const ranged_check = select("create_ranged_check")
	const multiple = select("create_multiple")
	const duration = check("create_duration");
	const duration_type = select("create_duration_type");
	const duration_innate = check("create_duration_innate");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'create-err';
	const err_line = 'create-err-line';

	response = fetch('/power/create/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'solidity': solidity,
			'visibility': visibility,
			'complexity': complexity,
			'volume': volume,
			'toughness': toughness,
			'mass': mass,
			'damageable': damageable,
			'maintained': maintained,
			'repairable': repairable,
			'moveable': moveable,
			'stationary': stationary,
			'trap': trap,
			'ranged': ranged,
			'weapon': weapon,
			'support': support,
			'real': real,
			'cover': cover,
			'conceal': conceal,
			'incoming': incoming,
			'outgoing': outgoing,
			'transform': transform,
			'transform_type': transform_type,
			'transform_start_mass': transform_start_mass,
			'transfom_mass': transfom_mass,
			'transform_start_descriptor': transform_start_descriptor,
			'transform_end_descriptor': transform_end_descriptor,
			'move_player': move_player,
			'move_check': move_check,
			'move_opponent_check': move_opponent_check,
			'move_opposed': move_opposed,
			'trap_check': trap_check,
			'trap_resist': trap_resist,
			'trap_opposed': trap_opposed,
			'trap_escape': trap_escape,
			'weapon_damage': weapon_damage,
			'support_strength': support_strength,
			'support_strengthen': support_strengthen,
			'support_action': support_action,
			'support_action_rounds': support_action_rounds,
			'support_effort': support_effort,
			'support_effort_rounds': support_effort_rounds,
			'cost': cost,
			'ranks': ranks,
			'columns': columns,
			'created': created,
			'font': font,
			'ranged_damage': ranged_damage,
			'ranged_check': ranged_check,
			'multiple': multiple,
			'duration': duration,
			'duration_type': duration_type,
			'duration_innate': duration_innate
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			extra_effect_check(jsonResponse)

			selects_add('create', 'Created Objects are Damaged', 'feedback-sml', create_counts.count);
			selects_add('create', 'Created Objects Permanent', 'permanent-sml', create_counts.count);
			create_counts.count += 1;

			create_grid.columns.length = 0;
			create_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, create_grid, route);
			clear_errors(err_line, errors)

			create_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}