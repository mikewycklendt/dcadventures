function deg_mod_check() {
	const deg_mod_check = "deg_mod_check";
	const deg_mod_base_form = "deg-mod-base-form";
	const title = "deg-mod-title";
	const entry = 'deg-mod-entry';

	check_title_small(deg_mod_check, title, deg_mod_base_form, entry);
}

function deg_mod_base() {
	const deg_mod_target = "deg_mod_target";
	const deg_mod_entry = "deg-mod-entry";

	base(deg_mod_target, deg_mod_entry);
}

function deg_mod_type() {
	const select = 'deg_mod_type';
	const options = [{'val': 'damage', 'div': 'deg-mod-damage'},
					{'val': 'measure', 'div': 'deg-mod-measure'},
					{'val': 'condition', 'div': 'deg-mod-condition'}]

	select_opacity(select, options);	
};

function deg_mod_damage_type() {
	const damage_type_field = 'deg_mod_damage_type';
	const damage_math = 'deg-mod-damage-math';
	const damage_value = 'deg-mod-damage-value';

	value_type(damage_type_field, damage_math, damage_value);
}

function deg_mod_measure_type() {
	const measure_type_field = 'deg_mod_measure_type';
	const measure_math = 'deg-mod-measure-math';
	const measure_value = 'deg-mod-measure-value';
	
	value_type(measure_type_field, measure_math, measure_value);
}

deg_mod_enter = 0;

function deg_mod_submit() {
	
	let target_field = document.getElementById('deg_mod_target');
	let target =  target_field.options[target_field.selectedIndex].value;
	let deg_field = document.getElementById('deg_value');
	let deg_value =  deg_field.options[deg_field.selectedIndex].value;
	let type_field = document.getElementById('deg_mod_type');
	let type =  type_field.options[type_field.selectedIndex].value;
	let damage_type_field = document.getElementById('deg_mod_damage_type');
	let damage_type =  damage_type_field.options[damage_type_field.selectedIndex].value;
	let danage_math_field = document.getElementById('deg_mod_math_damage');
	let damage_math =  danage_math_field.options[danage_math_field.selectedIndex].value;
	let damage_math1_field = document.getElementById('deg_mod_damage_math1');
	let damage_math1 =  damage_math1_field.options[damage_math1_field.selectedIndex].value;
	let damage_math2_field = document.getElementById('deg_mod_damage_math2');
	let damage_math2 =  damage_math2_field.options[damage_math2_field.selectedIndex].value;
	let damage_val1_field = document.getElementById('deg_mod_damage_val1');
	let damage_val1 =  damage_val1_field.options[damage_val1_field.selectedIndex].value;
	let damage_val2_field = document.getElementById('deg_mod_damage_val2');
	let damage_val2 =  damage_val2_field.options[damage_val2_field.selectedIndex].value;
	let damage_deg_val_field = document.getElementById('deg_damage_deg_value');
	let damage_deg_val =  damage_deg_val_field.options[damage_deg_val_field.selectedIndex].value;
	let damage_val_field = document.getElementById('deg_damage_value');
	let damage_val =  damage_val_field.options[damage_val_field.selectedIndex].value;
	let measure_type_field = document.getElementById('deg_mod_measure_type');
	let measure_type =  measure_type_field.options[measure_type_field.selectedIndex].value;
	let measure_val1_field = document.getElementById('deg_mod_measure_val1');
	let measure_val1 =  measure_val1_field.options[measure_val1_field.selectedIndex].value;
	let measure_val2_field = document.getElementById('deg_mod_measure_val2');
	let measure_val2 =  measure_val2_field.options[measure_val2_field.selectedIndex].value;
	let measure_math_field = document.getElementById('deg_mod_measure_math');
	let measure_math =  measure_math_field.options[measure_math_field.selectedIndex].value;
	let measure_math_rank_field = document.getElementById('deg_mod_measure_math_rank');
	let measure_math_rank =  measure_math_rank_field.options[measure_math_rank_field.selectedIndex].value;
	let measure_value_field = document.getElementById('deg_mod_measure_value');
	let measure_value =  measure_value_field.options[measure_value_field.selectedIndex].value;
	let measure_rank_field = document.getElementById('deg_mod_measure_rank');
	let measure_rank =  measure_rank_field.options[measure_rank_field.selectedIndex].value;
	let condition1_field = document.getElementById('deg_mod_condition1');
	let condition1 =  condition1_field.options[condition1_field.selectedIndex].value;
	let condition2_field = document.getElementById('deg_mod_condition2');
	let condition2 =  condition2_field.options[condition2_field.selectedIndex].value;
	let nullify_field = document.getElementById('deg_mod_nullify');
	let nullify_val = nullify_field.options[nullify_field.selectedIndex].value;
	let key = document.getElementById('deg_mod_keyword').value;
	let desc = document.getElementById('deg_mod_desc').value;

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'deg-mod-err-line';
	const error_table = 'deg-mod-err';

	if ((target != '' && deg_value != '' && type == 'event' && key != '' && desc != '') || 
		(target != '' && deg_value != '' && type == 'damage' && damage_type == 'math' && damage_math != '' && damage_math1 != '' && damage_math2 != '' && damage_val1 !=  '' && damage_val2 != '' && key != '' && desc != '') || 
		(target != '' && deg_value != '' && type == 'damage' && key != '' && desc != '' && damage_deg_val != '' && damage_type == 'value' && damage_val != '') || 
		(target != '' && deg_value != '' && type == 'measure' && key != '' && desc != '' && measure_type == 'value' && measure_value != '' && measure_rank != '') || 
		(target != '' && deg_value != '' && type == 'measure' && key != '' && desc != '' && measure_type == 'math' && measure_math != '' && measure_val1 != '' && measure_val2 != '' && measure_math_rank != '') || 
		(target != '' && deg_value != '' && type == 'condition' && key != '' && desc != '' && condition1 != '' && condition2 != '')) {

		response = fetch('/skill/degree_mod/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'target': target,
				'degree': deg_value,
				'type': type,
				'damage_value_degree': damage_deg_val,
				'damage_value_value': damage_val,
				'damage_math_damage': damage_math,
				'damage_math_math1': damage_math1,
				'damage_math_value': damage_val1,
				'damage_math_math2': damage_math2,
				'damage_math_rank': damage_val2,
				'measure_value': measure_value,
				'measure_value_rank': measure_rank,
				'measure_math_value': measure_val1,
				'measure_math_math': measure_math,
				'measure_math_rank': measure_val2,
				'measure_math_measure_rank': measure_math_rank,
				'condition_1': condition1,
				'condition_2': condition2,
				'keyword': key,
				'description': desc,
				'nullify': nullify_val
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const deg = document.createElement('div');
				deg.className = 'deg-mod-table-deg'
				deg.innerHTML = deg_value;
		
				if (type == 'damage') {
					if (damage_type == 'math') {
						effect = jsonResponse.damage_math_damage + ' ' + jsonResponse.damage_math_math1 + ' ' + jsonResponse.damage_math_value + ' ' + jsonResponse.damage_math_math2 + ' ' + jsonResponse.damage_math_rank;
					} else if (damage_type == 'value') {
						effect = 'degree: ' + jsonResponse.damage_value_degree + ' damage: ' + jsonResponse.damage_value_value;
					}
				} else if (type == 'measure') {
					if (measure_type == 'math') {
						effect = jsonResponse.measure_math_value + ' ' + jsonResponse.measure_math_math + ' ' + jsonResponse.measure_math_rank + ' ' + jsonResponse.measure_math_measure_rank;
					} else if (measure_type == 'value') {
						effect = jsonResponse.measure_value + ' ' + jsonResponse.measure_value_rank;
					}
				} else if (type == 'condition') {
					effect = 'from ' + jsonResponse.condition_1 + ' to ' + jsonResponse.condition_2;
				} else if (type == 'event') {
					effect = 'Event';
				}

				const eff = document.createElement('div');
				eff.className = 'deg-mod-table-effect'
				eff.innerHTML = effect;

				const key_div = document.createElement('div');
				key_div.className = 'deg-mod-table-key'
				key_div.innerHTML = jsonResponse.keyword;

				const desc_div = document.createElement('div');
				desc_div.className = 'deg-mod-table-desc'
				desc_div.innerHTML = jsonResponse.description;
	
				const nullify = document.createElement('div');
				nullify.className = 'deg-mod-table-null'
				nullify.innerHTML = jsonResponse.nullify;

				const degmodDelete = document.createElement('div');
				degmodDelete.className = 'deg-mod-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'deg-mod-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				degmodDelete.appendChild(deleteBtn);

				const table = document.getElementById('deg-mod-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(deg);
				table.appendChild(eff);
				table.appendChild(key_div);
				table.appendChild(desc_div);
				table.appendChild(nullify);	
				table.appendChild(degmodDelete);

		
				rows = [deg.scrollHeight, eff.scrollHeight, key_div.scrollHeight, desc_div.scrollHeight, nullify.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

				deg.style.maxHeight = deg.scrollHeight + "px";
				eff.style.maxHeight = eff.scrollHeight + "px";
				key_div.style.maxHeight = key_div.scrollHeight + "px";
				desc_div.style.maxHeight = desc_div.scrollHeight + "px";
				nullify.style.maxHeight = nullify.scrollHeight + "px";
				degmodDelete.style.maxHeight = degmodDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				deg_mod_delete()
		
				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})				


	} else {
		errors = document.getElementById('deg-mod-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		errors_delete = document.getElementsByClassName('deg-mod-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}

		let errors_height = errors.scrollHeight + 20;

		if (target == '') { 
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must choose a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (deg_value == '') {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must chose a degree value';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'event') && ((key == '') && (desc == ''))) {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must fill out all event fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'damage') && (damage_type == 'math') && ((damage_math1 == '') || (damage_math2 == '') || (damage_val1 ==  '') || (damage_val2 == ''))) { 
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter all math fields for damage';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'damage') && (damage_type == 'value') && ((damage_deg_val == '') ||  (damage_val == ''))) {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter all damage values';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (key == '') {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter a keyword';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (desc == '') {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'measure') && (measure_type == 'value') && ((measure_value == '') || (measure_rank == ''))) {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter all measurement values';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'measure') && (measure_type == 'math') && ((measure_math == '') || (measure_val1 == '') || (measure_val2 == '') || (measure_math_rank == ''))) {
			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter all math values for the measurement';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if ((type == 'condition') && ((condition1 == '') || (condition2 == ''))) {

			const error = document.createElement('div');
			error.className = 'deg-mod-err-line'
			error.innerHTML = ' You must enter BOTH CONDITIONS';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}
		
		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

deg_mod_delete = function() {
	const deletes = '.deg-mod-xbox';
	const divs = ['deg-mod-table-deg', 'deg-mod-table-effect', 'deg-mod-table-key', 'deg-mod-table-desc', 'deg-mod-table-null', 'deg-mod-table-delete'];
	const route = '/skill/degree_mod/delete/';

	delete_function(deletes, divs, route);
};

deg_mod_delete();