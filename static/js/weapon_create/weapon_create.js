

weapon_create = function() {
	const weapon_name = document.getElementById('weapon_name').value;
	const add_weapon = document.getElementById('add-weapon');
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch('/weapon/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': weapon_name,
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const all_fields = document.getElementById('all-fields');
			const name_div = document.getElementById('weapon-name');
			const weapon_id = document.getElementById('weapon_id');
			name_div.innerHTML = jsonResponse.name;
			weapon_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_weapon.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

edit_form = function() {
	const equip_id = document.getElementById('weapon_id').value;
	const edit_field = document.getElementById('weapon_name_edit');
	const name = document.getElementById('weapon-name').innerHTML;
	const edit_grid = document.getElementById('weapon-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

weapon_edit = function() {
	const id = document.getElementById('weapon_id').value;
	const name = document.getElementById('weapon_name_edit').value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch('/weapon/edit_name', {
		method: 'POST',
		body: JSON.stringify({
			'id': id,
			'name': name
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const name_div = document.getElementById('weapon-name');
			const edit_grid = document.getElementById('weapon-edit-grid');
			edit_grid.style.display = "none";
			name_div.innerHTML = jsonResponse.name;
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);

			clear_errors(err_line, errors);

		} else {
				
			back_errors(err_line, errors, jsonResponse);

		}
	})
}

weapon_save = function() {

	const weapon_id = document.getElementById('weapon_id').value;

	const description = text("description");
	const cat_id = select("category")
	const type_id = select("type")
	const cost = select("cost")
	const critical = select("critical")
	const damage = select("damage")
	const toughness = select("toughness")
	const material = select("material")
	const length = text("length")
	const length_units = select("length_units")
	const resist_dc = select("resist_dc")
	const resistance = select("resistance")
	const power_rank = select("power_rank")
	const power = select("power")
	const hands = select("hands")
	const strength = check("strength")
	const thrown = check("thrown")
	const unarmed = check("unarmed")
	const reach = select("reach")
	const ranged_attack_bonus = select("ranged_attack_bonus")
	const protect = select("protect")
	const ranged_area = select("ranged_area")
	const ranged_burst = select("ranged_burst")
	const ranged_area_damage = select("ranged_area_damage")
	const penetrate = check("penetrate")
	const attack_bonus = select("attack_bonus")
	const subtle = check("subtle")
	const perception_dc = select('perception_dc')
	const advantage = select("advantage")
	const grenade_area = select("grenade_area")
	const grenade_burst = select("grenade_burst")
	const grenade_area_damage = select("grenade_area_damage")
	const conceal = select("conceal")
	const sense = select("sense")
	const double = check("double")
	const double_mod = select("double_mod")
	const benefit = check('benefit_check')
	const condition = check('condition_check')
	const descriptor = check('descriptor_check')
	
	const errors = 'weapon-err';
	const err_line = 'weapon-err-line';

	response = fetch('/weapon/save', {
		method: 'POST',
		body: JSON.stringify({
			'weapon_id': weapon_id,
			'cat_id': cat_id,
			'type_id': type_id,
			'cost': cost,
			'description': description,
			'critical': critical,
			'damage': damage,
			'toughness': toughness,
			'material': material,
			'length': length,
			'length_units': length_units,
			'resist_dc': resist_dc,
			'resistance': resistance,
			'power_rank': power_rank,
			'power': power,
			'hands': hands,
			'strength': strength,
			'thrown': thrown,
			'unarmed': unarmed,
			'reach': reach,
			'ranged_attack_bonus': ranged_attack_bonus,
			'protect':protect,
			'ranged_area': ranged_area,
			'ranged_burst': ranged_burst,
			'ranged_area_damage': ranged_area_damage,
			'penetrate': penetrate,
			'attack_bonus': attack_bonus,
			'subtle': subtle,
			'perception_dc': perception_dc,
			'advantage': advantage,
			'grenade_area': grenade_area,
			'grenade_burst': grenade_burst,
			'grenade_area_damage': grenade_area_damage,
			'conceal': conceal,
			'sense': sense,
			'double': double,
			'double_mod': double_mod,
			'benefit': benefit,
			'condition': condition,
			'descriptor': descriptor
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/weapon/save/success/' + equip_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

