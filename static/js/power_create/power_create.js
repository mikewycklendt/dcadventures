
power_create = function() {
	const power_name = document.getElementById('power_name').value;
	const add_power = document.getElementById('add-power');
	const edit_button = document.getElementById('edit-button');

	response = fetch('/power/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': power_name,
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
			const name_div = document.getElementById('power-name');
			const power_id = document.getElementById('power_id');
			name_div.innerHTML = jsonResponse.name;
			power_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_power.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			errors_delete = document.getElementsByClassName('name-err-line');

			if (typeof errors_delete[0] === "undefined") {
				console.log('no errors defined')
			} else {
				for (i = 0; i < errors_delete.length; i++) {
					errors_delete[i].style.maxHeight = "0px";
					errors_delete[i].style.padding = "0px";
					errors_delete[i].style.marginBottom = "0px";
				}

			errors = document.getElementById('name-err')

				errors.style.display = "none";
				errors.style.padding = "0px";
				errors.style.maxHeight = "0px";
			}

		} else {
			const errors = document.getElementById('name-err');
			errors.style.display = "grid";

			const error_msgs = jsonResponse.error
			let i;

			for (i of error_msgs) {
				const error = document.createElement('div');
				error.className = 'name-err-line';
				error.innerHTML = i;
		
				errors.appendChild(error);
			
				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		}
	})
}

edit_form = function() {
	const power_id = document.getElementById('power_id').value;
	const edit_field = document.getElementById('power_name_edit');
	const name = document.getElementById('power-name').innerHTML;
	const edit_grid = document.getElementById('power-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

power_edit = function() {
	const id = document.getElementById('power_id').value;
	const name = document.getElementById('power_name_edit').value;
	
	response = fetch('/power/edit_name', {
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
			const name_div = document.getElementById('power-name');
			const edit_grid = document.getElementById('power-edit-grid');
			edit_grid.style.display = "none";
			name_div.innerHTML = jsonResponse.name;
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);

			errors_delete = document.getElementsByClassName('name-err-line');

			if (typeof errors_delete[0] === "undefined") {
				console.log('no errors defined')
			} else {
				for (i = 0; i < errors_delete.length; i++) {
					errors_delete[i].style.maxHeight = "0px";
					errors_delete[i].style.padding = "0px";
					errors_delete[i].style.marginBottom = "0px";
				}

			errors = document.getElementById('name-err')

				errors.style.display = "none";
				errors.style.padding = "0px";
				errors.style.maxHeight = "0px";
			}

		} else {
			const errors = document.getElementById('name-err');
			errors.style.display = "grid";

			const error_msgs = jsonResponse.error
			let i;

			for (i of error_msgs) {
				const error = document.createElement('div');
				error.className = 'name-err-line';
				error.innerHTML = i;
		
				errors.appendChild(error);
			
				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";	
			}
		}
	})
}

power_save = function() {

	const description = text("power_desc");
	const power_type = select("type");
	const action = select("action");
	const power_range = select("range");
	const duration = select("duration");
	const cost = select("cost");
	const ranks = select("base_ranks");
	const flat = check("flat");
	const limit = select("limit");
	const dc_type = select("power_dc_type");
	const dc_mod = select("power_dc_mod");
	const dc_value = select("power_dc_value");
	const opponent_dc = select("opponent_dc");
	const check_type = select("check");
	const routine = check("routine_checkbox");
	const routine_trait_type = select("routine_trait_type");
	const routine_trait = select("routine_trait");
	const materials = check("materials");
	const partner = select("partner");
	const partner_trait_type = select("partner_trait_type");
	const partner_dc = select("partner_dc");
	const partner_trait = select("partner_trait");
	const circ = select("circ");
	const circ_required = select("circ_required");
	const skill = select("skill");
	const skill_required = select("skill_required");
	const skill_when = select("skill_when");
	const conflict = select("conflict");
	const bonus_conflict = select("bonus_conflict");
	const conflict_bonus = select("conflict_bonus");
	const conflict_type = select("conflict_type");
	const condition = select("power_condition");
	const target_type = select("target_type");
	const strength_based = select("strength_based");
	const info = check("info");
	const gm_trigger = check("gm_trigger");
	const req_descriptor = check("req_descriptor");
	const damage_descriptor = check("damage_descriptor");

	const alt_check = check("check_check");
	const change_action = check('change_action_check');
	const character = check('char_check');;
	const circumstance = check('circ_check');
	const create = check('create_check');
	const damage = check('damage_check');
	const dc = check('dc_check');
	const defense = check('defense_check');
	const degree = check('deg_mod_check');
	const environment = check('env_check');
	const levels = check('levels_check');
	const minion = check('minion_check');
	const modifier = check('mod_check');
	const move = check('move_check');
	const opposed = check('opposed_check');
	const ranged = check('ranged_check');
	const resistance = check('resistance_check');
	const resist_by = check('resist_check');
	const reverse = check('reverse_check');
	const sense = check('sense_check');
	const time = check('time_check');

	const power_id = document.getElementById('power_id').value;

	const errors = 'power-err';
	const err_line = 'power-err-line';

	response = fetch('/power/save', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'description': description,
			'power_type': power_type,
			'action': action,
			'power_range': power_range,
			'duration': duration,
			'cost': cost,
			'ranks': ranks,
			'flat': flat,
			'limit': limit,
			'dc_type': dc_type,
			'dc_value': dc_value,
			'dc_mod': dc_mod,
			'opponent_dc': opponent_dc,
			'check_type': check_type,
			'routine': routine,
			'routine_trait_type': routine_trait_type,
			'routine_trait': routine_trait,
			'materials': materials,
			'partner': partner,
			'partner_trait_type': partner_trait_type,
			'partner_dc': partner_dc,
			'partner_trait': partner_trait,
			'circ': circ,
			'circ_required': circ_required,
			'skill': skill,
			'skill_required': skill_required,
			'skill_when': skill_when,
			'conflict': conflict,
			'bonus_conflict': bonus_conflict,
			'conflict_bonus': conflict_bonus,
			'conflict_type': conflict_type,
			'condition': condition,
			'target_type': target_type,
			'strength_based': strength_based,
			'alt_check': alt_check,
			'change_action': change_action,
			'character': character,
			'circumstance': circumstance,
			'create': create,
			'damage': damage,
			'dc': dc,
			'defense': defense,
			'degree': degree,
			'environment': environment,
			'levels': levels,
			'minion': minion,
			'modifier': modifier,
			'move': move,
			'opposed': opposed,
			'ranged': ranged,
			'resistance': resistance,
			'resist_by': resist_by,
			'reverse': reverse,
			'sense': sense,
			'time': time,
			'info': info,
			'gm_trigger': gm_trigger,
			'req_descriptor': req_descriptor,
			'damage_descriptor': damage_descriptor
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/power/save/success/' + power_id)

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

