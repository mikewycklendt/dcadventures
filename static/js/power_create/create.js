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
	const field = 'create_move_player';
	const update = 'create_move_player_trait';

	trait_select(field, update);
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
	const field = 'create_trap_trait_type';
	const update = 'create_trap_trait';

	trait_select(field, update);
}

function create_trap_resist_check() {
	const field = 'create_trap_resist_check';
	const update = 'create_trap_resist_trait';

	trait_select(field, update);
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

	trait_select(field, update);
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

	trait_select(field, update);
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