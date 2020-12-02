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
			entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_trap() {
	const check = document.getElementById('create_trap');
	const div = document.getElementById('create-trap');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_ranged() {
	const check = document.getElementById('create_ranged');
	const div = document.getElementById('create-ranged');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_weapon() {
	const check = document.getElementById('create_weapon');
	const div = document.getElementById('create-weapon');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_support() {
	const check = document.getElementById('create_support');	
	const div = document.getElementById('create-support');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function create_move_player() {
	const field = document.getElementById('create_move_player')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_move_player_trait');
	const div = document.getElementById('create-move-trait')

	console.log(trait)

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100);

	response = fetch('/power/trait/select', {
		method: 'POST',
		body: JSON.stringify({
			'trait': trait
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			div.style.opacity = '100%';

			const options = jsonResponse.options;
			let option;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option;
				o.text = option;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})
}

function create_move_opponent_check() {
	const check = document.getElementById('create_move_opponent_check')
	const div = document.getElementById('create-move-opp');

	if (check.checked == true) {
		div.style.opacity = '100%'
	} else {
		div.style.opacity = '0%'
	}
}

function create_trap_type() {
	const field = document.getElementById('create_trap_type');
	const val = field.options[field.selectedIndex].value;
	const dc = document.getElementById('create-trap-dc');
	const tr = document.getElementById('create-trap-trait');

	console.log(val)

	if (val == 'dc') {
		hide_maxheight(tr);
		show_maxheight(dc);
	} else if (val == 'trait') {
		hide_maxheight(dc);
		show_maxheight(tr);
	} else {
		hide_maxheight(dc);
		hide_maxheight(tr);
	}

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
	const dc = document.getElementById('create-ranged-dc');
	const tr = document.getElementById('create-ranged-trait')

	if (value == 'dc') {
		dc.style.display = 'grid';
		dc.style.maxHeight = dc.scrollHeight + 'px';
		tr.style.display = 'none';
		tr.style.maxHeight = '0px';
	} else if (value == 'target' || value == 'player') {	
		tr.style.display = 'grid';
		tr.style.maxHeight = tr.scrollHeight + 'px';
		dc.style.display = 'none';
		dc.style.maxHeight = '0px';
	} else {
		dc.style.display = 'none';
		dc.style.maxHeight = '0px';
		tr.style.display = 'none';
		tr.style.maxHeight = '0px';	
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
	const check = document.getElementById('create_support_strengthen')
	const div = document.getElementById('create-support-strengthen');

	if (check.checked == true) {
		div.style.opacity = '100%'
	} else {
		div.style.opacity = '0%'
	}
}