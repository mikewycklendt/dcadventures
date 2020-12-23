function descriptor_add_type()  {
	const fields = document.getElementsByClassName('descriptor-sml');
	
	options = [{'type': 11223344, 'name': 'Any Chosen Rare'}, 
				{'type': 22334455, 'name': 'Any Chosen Uncommon'}, 
				{'type': 33445566, 'name': 'Any Chosen Common'}, 
				{'type': 44556677, 'name': 'Any Chosen Very Common'}, 
				{'type': 55667788, 'name': 'Any Chosen Damage'},
				{'type': 66778899, 'name': 'Any Chosen Origin'},
				{'type': 77889900, 'name': 'Any Chosen Source'},
				{'type': 88990011, 'name': 'Any Chosen Medium Type'},
				{'type': 99001122, 'name': 'Any Chosen Medium Subtype'},
				{'type': 11002233, 'name': 'Any Chosen Medium'},
				{'type': 12121212, 'name': 'Any Chosen Descriptor'}]

	let field;
	let option;

	for (field of fields) {
		for (option of options) {
			let o = document.createElement('option');
			o.value = option.type;
			o.text = option.name;
			field.add(o);
		}
	}
}

descriptor_add_type()



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

function select(field_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;

	return value;
}

function text(text_input) {
	const input = document.getElementById(text_input);
	const value = input.value;

	return value;
}

function check(check_input) {
	const checkbox = document.getElementById(check_input);
	const value = checkbox.checked;

	return value;
}

function multiple(multiple_input) {
	let selectElement = document.getElementById(multiple_input);
	let selectedValues = Array.from(selectElement.selectedOptions).map(option => option.value);

	return selectedValues;
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


function create_table(jsonResponse, object) {

	const spot_string = jsonResponse.spot;
	const table_id = jsonResponse.table_id;
	const created = jsonResponse.created;
	const id = jsonResponse.id; 
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const rows = jsonResponse.rows;
	const size = jsonResponse.font;

	console.log(size);

	console.log(id)

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const base_table = 'power-table-table';
	const base_cell_title = 'power-table-cell-title ';
	const base_title = 'power-table-title'
	const base_titles = 'power-table-titles';

	
	console.log(created)


	if (created == false) {

		let grow =  0;

		create_titles(jsonResponse, grow, object);
	
	} else {

		let grow = 0

		const table = document.getElementById(table_class)

		cells_create(table, grow, jsonResponse, object);
	}


}

function create_titles(jsonResponse, grow, object) {
	
	const spot_string = jsonResponse.spot;
	const table_id = jsonResponse.table_id;
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const cells = jsonResponse.cells;

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const base_table = 'power-table-table';
	const base_cell_title = 'power-table-cell-title ';
	const base_title = 'power-table-title'
	const base_titles = 'power-table-titles';

	const spot = document.getElementById(spot_string);
	if (title_string != '') {
		const title = document.createElement('div');
		title.className = base_title;
		title.innerHTML = title_string;
		spot.appendChild(title)
	}
	const new_table = document.createElement('div');
	new_table.className = base_table;
	new_table.setAttribute('id', table_class);
	spot.appendChild(new_table);

	const title_row = document.createElement('div');
	title_row.className = base_titles;
	title_row.classList.add(cells_class);
	title_row.style.gridTemplateColumns = grid;
	grow = grow + title_row.scrollHeight;
	new_table.appendChild(title_row);
	
	let cell;
	for (cell of cells) {
		const cell_title = document.createElement('div');
		const title_id = table_id + '-' + cell.class + '-title';
		cell_title.setAttribute('id', title_id);
		cell_title.className = base_cell_title + cells_class;
		cell_title.innerHTML = cell.title;
		if (cell.width > 1) {
			cell_title.style.opacity = '100%';
			cell_title.style.maxHeight = cell_title.scrollHeight + 'px';
		}
		title_row.appendChild(cell_title);
	}
	
	grow += title_row.scrollHeight

	cells_create(new_table, grow, jsonResponse, object)
	
}

function grow_table(table, grow) {

	table.style.display = 'grid';
	table.style.maxHeight = table.scrollHeight + grow + 'px';
}

function grid__update(cells, table_id, grid, cells_class, size) {
	for (let i = 0; i < cells.length; i++) {
		const title_id = table_id + '-' + cells[i].class + '-title';
		const cell_title = document.getElementById(title_id)
		if (cells[i].width > 1) {
			cell_title.style.maxHeight = cell_title.scrollHeight + 'px';
			cell_title.style.opacity = '100%';
		}
		else {
			cell_title.style.opacity = '0%';
			cell_title.style.maxHeight = '0px'
		}
	}

	const cells_rows = document.getElementsByClassName(cells_class);
	for (let i = 0; i < cells_rows.length; i++) {
		cells_rows[i].style.gridTemplateColumns = grid;
		cells_rows[i].style.fontSize = size + '%';
	}

	const cell = document.getElementsByClassName('power-table-cell');
	for (let i = 0; i < cells_rows.length; i++) {
		cell[i].style.fontSize = size + '%';
	}
}

function cells_create(table_input, grow, jsonResponse, object) {

	const table = table_input;
	const table_id = jsonResponse.table_id;
	const id = jsonResponse.id; 
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const size = jsonResponse.font;


	const cells_class = table_id + '-cells';
	const entry_class = table_id + '-row';
	const delete_class = table_id + '-xbox';
	const check_button_class = table_id + '-button'
	const base_cells = 'power-table-cells';
	const base_cell = 'power-table-cell'
	const base_button_check = 'power-check-button ';
	const base_check = 'power-check';
	const base_entry = 'power-table-row';
	const base_delete = 'xbox ';

	const entry = document.createElement('div');
	entry.className = base_entry
	entry.classList.add(entry_class);
	table.appendChild(entry);
	const row = document.createElement('div');
	row.className = base_cells;
	row.classList.add(cells_class);	
	row.style.gridTemplateColumns = grid;
	entry.appendChild(row);

	let create_mod = false;
	let cell;
	let cell_heights = [];
	for (cell of cells) {
		const cell_class = table_id + '-' + cell.class;
		const new_cell = document.createElement('div');
		new_cell.className = base_cell;
		new_cell.classList.add(cell_class);
		if (cell.content == false) {
			new_cell.innerHTML = '';
		} else if (cell.content == true) {
			if (cell.mod_check == true) {
				create_mod = true;
				const check = document.createElement('button');
				check.className = base_button_check;
				check.classList.add(check_button_class);
				new_cell.appendChild(check);
				const cell_height = new_cell.scrollHeight;
				cell_heights.push(cell_height);
			} else {
				const check = document.createElement('div');
				check.className = base_check;
				new_cell.appendChild(check);
				const cell_height = new_cell.scrollHeight;
				cell_heights.push(cell_height);
			}
		} else {
			new_cell.innerText = cell.content;
			console.log(cell.content);
			const cell_height = new_cell.scrollHeight;
			cell_heights.push(cell_height);
		}
		row.appendChild(new_cell);
	}

	let height;
	for (height of cell_heights) {
		if (height > grow) {
			grow += height;
		}
	}

	const empty_cell = document.createElement('div');
	empty_cell.className = base_cell;
	row.appendChild(empty_cell);

	const delete_cell = document.createElement('div');
	delete_cell.className = base_cell;
	const delete_btn = document.createElement('button');
	delete_btn.className = base_delete + delete_class;
	delete_btn.setAttribute('data-id', id);
	delete_cell.appendChild(delete_btn)
	row.appendChild(delete_cell)

	table.style.display = 'grid';
	row.style.maxHeight = row.scrollHeight + 'px';
	grow += row.scrollHeight; 

	if (create_mod) {
		mod_create(mods, id, entry, table_id, object);
	}
	
	grow_table(table, grow)
	
	grid__update(cells, table_id, grid, cells_class, size)

}



function mod_create(mods_input, id_input, entry_input, table_id_input, object) {

	const mods = mods_input;
	const id = id_input;
	const entry = entry_input;
	const table_id = table_id_input;

	const mod_class = table_id + '-mod'; 
	const base_mod = 'mod-row';
	const mod_cell_empty = 'mod-cell-empty';
	const mod_cell_mod = 'mod-cell-mod';
	const mod_cell_sub = 'mod-cell-sub';
	const mod_cell_title = 'mod-cell-title';
	const mod_cell_content = 'mod-cell-content';

	let new_mod;
	for (new_mod of mods) {
		const grid = new_mod.grid;		
		const cells = new_mod.cells;
		const mod_title = new_mod.title;
		const variable = new_mod.variable;
		object.mod.push(false)

		const mod = document.createElement('div');
		mod.className = mod_class;
		mod.classList.add(base_mod);
		mod.style.gridTemplateColumns = grid;
		entry.appendChild(mod);
		
		const empty = document.createElement('div');
		empty.className = mod_cell_empty
		mod.appendChild(empty);

		const title = document.createElement('div');
		title.className = mod_cell_mod;
		title.innerHTML = mod_title;
		mod.appendChild(title);

		if (variable == true) {
			const sub_title = new_mod.sub_title;
			const sub = document.createElement('div');
			sub.className = mod_cell_sub;
			sub.innerHTML = sub_title;
			mod.appendChild(sub)
		}

		let new_cell;
		for (new_cell of cells) {
			const tit = document.createElement('div');
			tit.className = mod_cell_title;
			tit.innerHTML = new_cell.title;
			mod.appendChild(tit);

			const con = document.createElement('div');
			con.className = mod_cell_content;
				
			if (new_cell.content == true) {
				mod.appendChild(con);
				const check = document.createElement('div');
				check.className = 'power-check';
				con.appendChild(check)
			} else {
				con.innerHTML = new_cell.content;
				mod.appendChild(con);
			}
		}
		
	}

	
	check_buttons(table_id, object, entry);

}

function check_buttons(table_id, object, entry) {
	console.log(object)
	const check_button_class = table_id + '-button'
	const mod_class = table_id + '-mod';
	const table_class = table_id + '-table'

	const table = document.getElementById(table_class)
	const btns = document.getElementsByClassName(check_button_class);
	const mods = document.getElementsByClassName('mod-row');

	for (let i = 0; i < btns.length; i++) {
		const btn = btns[i];
		btn.onclick = function(e) {
			console.log('click');
			console.log(object.mod)
			console.log(object.mod[i])

			const  mod = mods[i]

			if (object.mod[i] == true) {
				mod.style.maxHeight = '0px';
				table.style.maxHeight = table.scrollHeight - mod.scrollHeight + 'px';
				setTimeout(function(){mod.style.display = 'none'}, 400);
				object.mod[i] = false;
			} else {
				mod.style.display = 'grid';
				mod.style.maxHeight = mod.scrollHeight + 'px';
				table.style.maxHeight = table.scrollHeight + mod.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight + mod.scrollHeight + 'px';
				object.mod[i] = true;
			}

			console.log(mod)
		}
	}
}

function row_delete(jsonResponse, route, object) {
	const table_id = jsonResponse.table_id;
	const rows = jsonResponse.rows;
	const size = jsonResponse.font;
	console.log(rows)

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const entry_class = table_id + '-row';
	const table = document.getElementById(table_class);
	const delete_class = table_id + '-xbox';

	const deletes = document.getElementsByClassName(delete_class);
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click');

			const delId = e.target.dataset['id']
			fetch(route + delId, {
				method: 'DELETE'
			})
			.then(function() {
				response = fetch('/power/grid', {
					method: 'POST',
					body: JSON.stringify({
						'rows': rows,
						'font': size,
						'id': delId				}),
					headers: {
					  'Content-Type': 'application/json',
					}
				})
				.then(response => response.json())
				.then(jsonResponse => {
					if (jsonResponse.success) {
						const grid = jsonResponse.grid;
						const new_rows = jsonResponse.rows
						const all_rows = document.getElementsByClassName('power-table-row')
						const all_cells = document.getElementsByClassName(cells_class)

						console.log(new_rows)
						object.columns = new_rows;
						
						let cells;

						for (cells of all_cells) {
							if (grid == 'none') {
								table.style.maxHeight = '0px'
							} else {
								cells.style.gridTemplateColumns = grid;
							}
						}

						setTimeout(function() {
							if (grid == 'none') {
								table.style.maxHeight = '0px'
							}
						}, 400)

						all_rows[i].style.maxHeight = '0px';

						
					} else {
						console.log('error')
					}
				})
			
			})
		}
	}
}

function back_errors(line, table, jsonResponse) {
	errors_delete = document.getElementsByClassName(line);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
		};
		setTimeout(function(){
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.display = 'none';
			}
		}, 400);
	}


	setTimeout(function(){
		const errors = document.getElementById(table);

		errors.style.display = "grid";
		errors.style.padding = "1%";

		const error_msgs = jsonResponse.error_msgs;
		let li;

		let errors_height = errors.scrollHeight;
		for (li of error_msgs) {
			const error = document.createElement('div');
			error.className = line;
			error.innerHTML = li;
				
			errors.appendChild(error);
					
			error.style.maxHeight = error.scrollHeight + "px";

			errors_height = errors_height + error.scrollHeight;
			console.log(errors_height)
			errors.style.padding = "1%";	
		}

		errors.style.maxHeight = errors.scrollHeight + errors_height + 20 + 'px';
	}, 420)
}


function clear_errors(line, div) {
	errors_delete = document.getElementsByClassName(line);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
		};
		setTimeout(function(){
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.display = 'none';
			}
		}, 400);

		errors = document.getElementById(div);

		errors.style.maxHeight = "0px";
		errors.style.padding = "0px";
	}
}

