function create_check() {
	const check = document.getElementById("create_check");
	const title = document.getElementById("create-title");
	const base = document.getElementById('create-base')

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
	}
}

function create_base() {
	const field = document.getElementById('create_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("create-entry")

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}

function create_moveable() {
	const div = document.getElementById('create-move');
	const check = document.getElementById('create_moveable');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px
	}
}


function create_stationary() {
	const check = document.getElementById('create_stationary');
	const div = document.getElementById('create-move');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px
	}
}

function create_trap() {
	const check = document.getElementById('create_trap');
	const div = document.getElementById('create-trap');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px
	}
}

function create_ranged() {
	const check = document.getElementById('create_ranged');
	const div = document.getElementById('create-ranged');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px
	}
}

function create_weapon() {
	const check = document.getElementById('create_weapon');
	const div = document.getElementById('create-weapon');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px
	}
}

function create_support() {
	const check = document.getElementById('create_support');	
	const div = document.getElementById('create-support');
	const entry = document.getElementById('create-entry');

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxheight = div.scrollHeight + 'px';
		entry.style.maxheight = entry.scrollHeight + div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxheight = entry.scrollHeight - div.scrollHeight + 'px'
	}
}

function create_move_player() {
	const field = document.getElementById('create_move_player')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_move_player_trait');
	const div = document.getElementById('create-move-trait')

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
	const field = document.getElementById('create_trap_type')
	const val = field.options[field.selectedIndex].value;
	const dc = document.getElementById('create-trap-dc')
	const tr = document.getElementById('create-trap-trait')

	if (val == 'dc') {
		dc.style.display = 'grid';
		dc.style.maxheight = dc.scrollHeight + 'px';
		tr.style.display = 'none';
		tr.style.maxheight = '0px';
	} else if (field == 'trait') {
		tr.style.display = 'grid';
		tr.style.maxheight = tr.scrollHeight + 'px';
		dc.style.display = 'none';
		dc.style.maxheight = '0px';
	} else {
		dc.style.display = 'none';
		dc.style.maxheight = '0px';
		tr.style.display = 'none';
		tr.style.maxheight = '0px';
	}

}

function create_trap_trait_type() {
	const field = document.getElementById('create_trap_trait_type')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_trap_trait_type');

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100)

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

function create_trap_resist_check() {
	const field = document.getElementById('create_trap_resist_check')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_trap_resist_trait');

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100)

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

function create_ranged_type() {
	const field = document.getElementById('create_ranged_type');
	const value = field.options[field.selectedIndex].value;
	const dc = document.getElementById('create-ranged-dc');
	const tr = document.getElementById('create-ranged-trait')

	if (value == 'dc') {
		dc.style.display = 'grid';
		dc.style.maxheight = dc.scrollHeight + 'px';
		tr.style.display = 'none';
		tr.style.maxHeight = '0px';
	} else if (value == 'target' || value == 'player') {	
		tr.style.display = 'grid';
		tr.style.maxheight = tr.scrollHeight + 'px';
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
	const field = document.getElementById('create_ranged_trait_type')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_ranged_trait');

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100)

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
	const field = document.getElementById('create_weapon_trait_type')
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById('create_weapon_trait');

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100)

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