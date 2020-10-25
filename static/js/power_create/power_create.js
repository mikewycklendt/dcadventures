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
			all_fields.style.opacity = "100%";

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
```
power_save = function() {

	errors_delete = document.getElementsByClassName('skill-bonus-err-line');

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
		}

		errors = document.getElementById('skill-bonus-err')

		errors.style.display = "none";
		errors.style.padding = "0px";
		errors.style.maxHeight = "0px";
	}

	const description = document.getElementById('bonus_desc').value;

	const skill_id_field = document.getElementById('skill');
	const skill_id = skill_id_field.options[skill_id_field.selectedIndex].value;

	const action_field = document.getElementById('action');
	const action = action_field.options[action_field.selectedIndex].value;

	const check_field = document.getElementById('check');
	const check_id = check_field.options[check_field.selectedIndex].value;

	const condition_field = document.getElementById('condition');
	const condition = condition_field.options[condition_field.selectedIndex].value;

	const speed_mod_field = document.getElementById('speed');
	const speed_mod = speed_mod_field.options[speed_mod_field.selectedIndex].value;

	const skilltype_field = document.getElementById('skilltype');
	const skill_type = skilltype_field.options[skilltype_field.selectedIndex].value;

	const dc_set_field = document.getElementById('dc_set');
	const dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;

	const time_type_field = document.getElementById('prep_type');
	const time_type = time_type_field.options[time_type_field.selectedIndex].value;

	const time_val = document.getElementById('prep_value').value;

	const time_val_unit_field = document.getElementById('prep_unit');
	const time_val_unit = time_val_unit_field.options[time_val_unit_field.selectedIndex].value;

	const time_rank_field = document.getElementById('prep_rank');
	const time_rank = time_rank_field.options[time_rank_field.selectedIndex].value;

	const time_unit_field = document.getElementById('prep_math');
	const time_unit = time_unit_field.options[time_unit_field.selectedIndex].value;

	const time_mod_field = document.getElementById('prep_mod');
	const time_mod = time_mod_field.options[time_mod_field.selectedIndex].value;

	const subskill_check = document.getElementById('subskill_check');
	const sub_check = subskill_check.checked;

	const cover_check_check = document.getElementById('cover_check');
	const cover_check = cover_check_check.checked;

	const materials_check_check = document.getElementById('materials_check');
	const materials_check = materials_check_check.checked;

	const secret_check = document.getElementById('secret_check');
	const hidden_check = secret_check.checked;

	const secret_mod = document.getElementById('secret_mod');
	const hidden_mod = secret_mod.options[secret_mod.selectedIndex].value;

	const untrained_check_check = document.getElementById('untrained_check');
	const untrained_check = untrained_check_check.checked;

	const untrained_dclimit = document.getElementById('untrained_dclimit');
	const untrained_limit = untrained_dclimit.options[untrained_dclimit.selectedIndex].value;

	const untrained_mod_field = document.getElementById('untrained_mod');
	const untrained_mod = untrained_mod_field.options[untrained_mod_field.selectedIndex].value;

	const change_level_type = document.getElementById('change_level_type');
	const level_type = change_level_type.options[change_level_type.selectedIndex].value;

	const change_level_level = document.getElementById('change_level_level');
	const level_change = change_level_level.options[change_level_level.selectedIndex].value;

	const subskill = document.getElementById('sub_name').value;
	const subskill_description = document.getElementById('sub_desc').value;

	const move_rank_field = document.getElementById('move_rank');
	const move_rank = move_rank_field.options[move_rank_field.selectedIndex].value;

	const move_math_field = document.getElementById('move_math');
	const move_math = move_math_field.options[move_math_field.selectedIndex].value;

	const move_value = document.getElementById('move_value');
	const move_val = move_value.options[move_value.selectedIndex].value;

	const action_change_field = document.getElementById('action_change');
	const action_change = action_change_field.options[action_change_field.selectedIndex].value;

	const action_mod_field = document.getElementById('action_mod');
	const action_mod = action_mod_field.options[action_mod_field.selectedIndex].value;

	const other_check_check = document.getElementById('other_check');
	const other = other_check_check.checked;

	const pre_check_check = document.getElementById('pre_check_check');
	const other_check = pre_check_check.checked;

	const opposed_by_check = document.getElementById('opposed_by_check');
	const opposed = opposed_by_check.checked;

	const rounds_check = document.getElementById('rounds_check');
	const round = rounds_check.checked;

	const power_check = document.getElementById('power_check');
	const power = power_check.checked;

	const levels_check = document.getElementById('levels_check');
	const levels = levels_check.checked;

	const circ_check = document.getElementById('circ_check');
	const circ_mod = circ_check.checked;

	const degree_check = document.getElementById('degree_check');
	const degree_key = degree_check.checked;

	const deg_mod_check = document.getElementById('deg_mod_check');
	const degree_mod = deg_mod_check.checked;

	const resist_effect_check = document.getElementById('resist_effect_check');
	const resist_effect = resist_effect_check.checked;

	const resist_check_check = document.getElementById('resist_check');
	const resist_check = resist_check_check.checked;

	const opp_cond_check = document.getElementById('opp_cond_check');
	const opp_condition = opp_cond_check.checked;

	const char_check_check = document.getElementById('char_check');
	const char_check = char_check_check.checked;

	const bonus_id = document.getElementById('bonus_id').value;

	if ((description != '' && action != '' && check_id != '') && 
		((time_type == 'immediate') || (time_type == 'value' && time_val != '' && time_val_unit != '') || (time_type == 'math' && time_unit != '' && time_rank != '' && time_mod != '')) && 
		((sub_check == false) || (sub_check == true && subskill != '' && subskill_description != ''))) {

		response = fetch('/skill/save', {
			method: 'POST',
			body: JSON.stringify({
				'id': bonus_id,
				'skill_id': skill_id,
				'description': description,
				'action': action,
				'check_id': check_id,
				'condition': condition,
				'speed_mod': speed_mod,
				'skill_type': skill_type,
				'dc_set': dc_set,
				'time_type': time_type,
				'time_unit': time_unit,
				'time_rank': time_rank,
				'time_mod': time_mod,
				'time_val': time_val,
				'time_val_unit': time_val_unit,
				'sub_check': sub_check,
				'cover_check': cover_check,
				'materials_check': materials_check,
				'hidden_check': hidden_check,
				'hidden_mod': hidden_mod,
				'untrained_check': untrained_check,
				'untrained_limit': untrained_limit,
				'untrained_mod': untrained_mod,
				'level_type': level_type,
				'level_change': level_change,
				'subskill': subskill,
				'subskill_description': subskill_description,
				'move_rank': move_rank,
				'move_math': move_math,
				'move_val': move_val,
				'action_change': action_change,
				'action_mod': action_mod,
				'public': false,
				'approved': false,
				'other': other,
				'other_check': other_check,
				'opposed': opposed,
				'round': round,
				'power': power,
				'levels': levels,
				'circ_mod': circ_mod,
				'degree_key': degree_key,
				'degree_mod': degree_mod,
				'resist_check': resist_check,
				'resist_effect': resist_effect,
				'opp_condition': opp_condition,
				'char_check': char_check
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			if (jsonResponse.success) {
				window.location.replace('/skill/save/success/' + bonus_id)
			} else {
				console.log(jsonResponse)
				const errors = document.getElementById('skill-bonus-err');

				let errors_height = errors.scrollHeight + 20;

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error_msgs = jsonResponse.error
				let i;

				for (i of error_msgs) {
					const error = document.createElement('div');
					error.className = 'skill-bonus-err-line';
					error.innerHTML = i;
			
					errors.appendChild(error);
				
					error.style.maxHeight = error.scrollHeight + "px";

					error.style.maxHeight = error.scrollHeight + "px";
					errors_height = errors_height + error.scrollHeight; 
				}

				errors.style.maxHeight = errors_height + "px";
				errors.style.padding = "1%";	
				
			}
		})
	} else {
		errors_delete = document.getElementsByClassName('skill-bonus-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('skill-bonus-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (description == '') {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must write a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (action == '') {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must choose an action type';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (check_id == '') {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must choose a check type';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (time_type == 'value' && (time_val == '' || time_val_unit == '')) {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must fill out all time to complete fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (time_type == 'math' && (time_unit == '' || time_rank == '' || time_mod == '')) {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must fill out all time to complete fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (sub_check == true && (subskill == '' || subskill_description == '')) {
			const error = document.createElement('div');
			error.className = 'skill-bonus-err-line'
			error.innerHTML = ' You must fill out both subskill fields or uncheck the subskill box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + 20 + "px";
		errors.style.padding = "1%";

	}
}
```