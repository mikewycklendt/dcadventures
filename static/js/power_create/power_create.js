function trait_select(select, fill) {
	const field = document.getElementById(select)
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

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

function subsense_select(select, fill) {
	const field = document.getElementById(select);
	const sense_id = field.options[field.selectedIndex].value;
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/sense/subsense/select', {
		method: 'POST',
		body: JSON.stringify({
			'sense_id': sense_id
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
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function show_opacity(div_input) {
	const div = document.getElementById(div_input);

	setTimeout(function(){div.style.display = 'grid';}, 300);
	setTimeout(function(){div.style.opacity = '100%';}, 310);
}

function hide_opacity(div_input) {
	const div = document.getElementById(div_input);

	div.style.opacity = '0%';
	setTimeout(function(){div.style.display = 'none';}, 300);
}

function math_div_select(select, val, math, containdiv ) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById(containdiv)

	if (value == 'math') {
		div.style.display = 'grid';
		hide_opacity(val);
		show_opacity(math);
	} else if (value == 'value') {
		div.style.display = 'grid';
		hide_opacity(math);
		show_opacity(val);
	} else {
		hide_opacity(math);
		hide_opacity(val);
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function math_mod_div_select(select, val, math, mod, containdiv ) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById(containdiv)

	if (value == 'math') {
		div.style.display = 'grid';
		hide_opacity(val);
		hide_opacity(mod);
		show_opacity(math);
	} else if (value == 'value') {
		div.style.display = 'grid';
		hide_opacity(math);
		hide_opacity(mod);
		show_opacity(val);
	} else if (value == 'mod') {
		div.style.display = 'grid';
		hide_opacity(math);
		hide_opacity(val);
		show_opacity(mod);
	} else {
		hide_opacity(math);
		hide_opacity(mod);
		hide_opacity(val);
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function value_type(select, math, val) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;

	if (value == 'math') {
		hide_opacity(val);
		show_opacity(math);
	} else if (value == 'value') {
		hide_opacity(math);
		show_opacity(val)
	} else {
		hide_opacity(math);
		hide_opacity(val);
	}
}

function check_drop(field, divdrop, entrydrop) {
	const check = document.getElementById(field);
	const div = document.getElementById(divdrop);
	const entry = document.getElementById(entrydrop);

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function check_opacity(field, divopacity) {
	const check = document.getElementById(field);
	const div = document.getElementById(divopacity);

	if (check.checked == true) {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function check_display(field, divdisplay) {
	const check = document.getElementById(field);
	const div = document.getElementById(divdisplay);

	if (check.checked == true) {
		div.style.display = 'grid';
		setTimeout(function(){div.style.opacity = '100%'}, 10);
	} else {
		div.style.opacity = '0%';
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function clear_errors(line, div) {
		
	const errors_delete = document.getElementsByClassName(line);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
			setTimeout(function(){errors_delete[i].style.display = 'none'}, 400)
		}

		const errors = document.getElementById(div)

		errors.style.display = "none";
		errors.style.padding = "0px";
		errors.style.maxHeight = "0px";
	}
}

function clear_error_lines(line) {
	const errors_delete = document.getElementsByClassName('extras-err-line');

	for (i = 0; i < errors_delete.length; i++) {
		errors_delete[i].style.display = "none";
	}
}

function new_error(description, error_line, errors, errors_height) {
	const error = document.createElement('div');
	error.className = error_line;
	error.innerHTML = description;

	errors.appendChild(error);

	error.style.maxHeight = error.scrollHeight + "px";
	errors_height = errors_height + error.scrollHeight; 
}	

function json_errors(line, div, all_errors) {					
	const errors = document.getElementById(div);

	errors.style.display = "grid";
	errors.style.padding = "1%";

	
	let error_msg;

	for (error_msg of all_errors) {

		const error = document.createElement('div');
		error.className = line;
		error.innerHTML = error_msg;
	
		errors.appendChild(error);
	
		error.style.maxHeight = error.scrollHeight + "px";
	
		errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
		errors.style.padding = "1%";
	}
}

function show_maxheight(div_input) {
	const div = document.getElementById(div_input);

	setTimeout(function(){
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
	}, 300)
}

function hide_maxheight(div_input) {
	const div = document.getElementById(div_input);

	div.style.maxHeight = '0px';
	setTimeout(function(){div.style.display = 'none'}, 300)
}

function shrink_entry(entry_input, div_input) {
	const entry = document.getElementById(entry_input);
	const div = document.getElementById(div_input);

	entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
}

function grow_entry(entry_input, div_input) {
	const entry = document.getElementById(entry_input);
	const div = document.getElementById(div_input);

	setTimeout(function(){
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	}, 300)
}

function select_maxheight_entry(select, options, entry) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;
	const adiv = options[0].div;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_maxheight(div);
		} else {
			show_maxheight(div);
		}
	};

	if (val == '') {
		shrink_entry(entry, adiv)
	} else {
		for (option of options) {
			let valu = option.val;
			let div = option.div;
	
			if (val == valu) {
				grow_entry(entry, div);
			}
		}
	}
}

function select_opacity(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_opacity(div);
		} else {
			show_opacity(div);
		}
	};
}

function select_maxheight(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_maxheight(div);
		} else {
			show_maxheight(div);
		}
	};
}

function base(field_input, entry_input) {
	const field = document.getElementById(field_input)
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById(entry_input)

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";	
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function base_two(field_input, field2_input, entry_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;
	
	const field2 = document.getElementById(field2_input);
	const target = field2.options[field2.selectedIndex].value;
	const entry = document.getElementById(entry_input);

	if (value != '' && target != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function base_text(field_input, text_input, entry_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;
	const type = document.getElementById(text_input).value;
	const entry = document.getElementById(entry_input);

	if (value != '' && type != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function check_title(check_input, title_input, base_input, entry_input) {
	const check = document.getElementById(check_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function check_title_small(check_input, title_input, base_input, entry_input) {
	const check = document.getElementById(check_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "165%";
		setTimeout(function(){title.style.fontSize = "160%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}
	

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