function deg_mod_check() {
	const deg_mod_check = document.getElementById("deg_mod_check");
	const deg_mod_base_form = document.getElementById("deg-mod-base-form");
	const title = document.getElementById("deg-mod-title");

	if (deg_mod_check.checked == true) {
		deg_mod_base_form.style.opacity = "100%";
		title.style.color = "#af0101";
		title.style.fontSize = "164%";
		setTimeout(function(){title.style.fontSize = "160%"}, 75);
	} else {
		deg_mod_base_form.style.opacity = "0%";
		title.style.color = "#245681";
	}
}





function deg_mod_base() {
	const deg_mod_target = document.getElementById("deg_mod_target");
	const extra_field = document.getElementById('deg_mod_extra')
	const extra = extra_field.options[extra_field.selectedIndex].value;
	const degmodtarget =  deg_mod_target.options[deg_mod_target.selectedIndex].value;
	console.log(degmodtarget);
	const deg_mod_entry = document.getElementById("deg-mod-entry");

	if (degmodtarget != '' && extra != '') {
		deg_mod_entry.style.display = "grid";
		deg_mod_entry.style.padding = "1%";
		deg_mod_entry.style.maxHeight = deg_mod_entry.scrollHeight + "px";
		deg_mod_entry.style.padding = "1%";
	} else {
		deg_mod_entry.style.maxHeight = "0px";
		deg_mod_entry.style.padding = "0px";
	}
}

function deg_mod_type() {
	let deg_mod_type_field = document.getElementById('deg_mod_type');
	let deg_mod_type_value = deg_mod_type_field.options[deg_mod_type_field.selectedIndex].value;

	console.log(deg_mod_type_value)
	
	const cir = document.getElementById('deg-mod-circ')
	const mea = document.getElementById('deg-mod-measure');
	const con = document.getElementById('deg-mod-condition');

	cir.style.display = 'grid';
	cir.style.maxHeight = '0px';
	mea.style.display = 'grid';
	mea.style.maxHeight = '0px';
	con.style.display = 'grid';
	con.style.maxHeight = '0px';
	

	if (deg_mod_type_value == 'circ') {
		cir.style.display = 'grid';
		cir.style.maxHeight = cir.scrollHeight + 'px'
		mea.style.display = 'grid';;
		mea.style.maxHeight = '0px';
		con.style.display = 'grid';
		con.style.maxHeight = '0px';
	} else if (deg_mod_type_value == 'measure') {
		mea.style.display = 'grid';
		mea.style.maxHeight = mea.scrollHeight + 'px'
		cir.style.display = 'grid';
		cir.style.maxHeight = '0px';
		con.style.display = 'grid';
		con.style.maxHeight = '0px';
	} else if (deg_mod_type_value == 'condition') {
		con.style.display = 'grid';
		con.style.maxHeight = con.scrollHeight + 'px'
		cir.style.display = 'grid';
		cir.style.maxHeight = '0px';
		mea.style.display = 'grid';
		mea.style.maxHeight = '0px';
	} else {
		cir.style.display = 'grid';
		cir.style.maxHeight = '0px';
		mea.style.display = 'grid';
		mea.style.maxHeight = '0px';
		con.style.display = 'grid';
		con.style.maxHeight = '0px';
	}

}

function deg_mod_circ_trait_type() {
	const select = 'deg_mod_circ_trait_type'
	const fill = 'deg_mod_circ_trait'

	trait_select(select, fill)
}

function deg_mod_condition_type() {
	const field = document.getElementById('deg_mod_condition_type')
	const value = field.options[field.selectedIndex].value;
	const val = document.getElementById('deg-mod-condition-damage')
	const math = document.getElementById('deg-mod-conditions')

	if (value == 'condition') {
		val.style.opacity = '0%';
		val.style.display = 'none';
		math.style.display = 'grid';
		setTimeout(function(){math.style.opacity = '100%'}, 10);
	} else if (value == 'damage') {
		math.style.opacity = '0%';
		math.style.display = 'none';
		val.style.display = 'grid';
		setTimeout(function(){val.style.opacity = '100%'}, 10);
	} else {
		val.style.opacity = '0%';
		setTimeout(function(){val.style.display = 'none'}, 300);
		math.style.opacity = '0%';
		setTimeout(function(){math.style.display = 'none'}, 300);
	}
}

function deg_mod_damage_type() {
	let damage = document.getElementById('deg-mod-damage');
	
	let damage_type_field = document.getElementById('deg_mod_damage_type');
	let damage_type_value = damage_type_field.options[damage_type_field.selectedIndex].value;
	
	let damage_math = document.getElementById('deg-mod-damage-math');
	let damage_value = document.getElementById('deg-mod-damage-value');

	if(damage_type_value == 'math') {
		damage_math.style.display = "grid";
		damage_math.style.opacity = "100%";
		damage_value.style.display = "none";
		damage_value.style.opacity = "0%";
	} else if (damage_type_value == 'value') {
		damage_value.style.display = "grid";
		damage_value.style.opacity = "100%";
		damage_math.style.display = "none";
		damage_math.style.opacity = "0%";
	} else {
		damage_value.style.display = "none";
		damage_value.style.opacity = "0%";
		damage_math.style.display = "none";
		damage_math.style.opacity = "0%";
	}
}

function deg_mod_measure_type() {
	let measure = document.getElementById('deg-mod-measure');

	let measure_type_field = document.getElementById('deg_mod_measure_type');
	let measure_type_value = measure_type_field.options[measure_type_field.selectedIndex].value;

	let measure_math = document.getElementById('deg-mod-measure-math');
	let measure_value = document.getElementById('deg-mod-measure-value');
	
	if(measure_type_value == 'math') {
		measure_math.style.display = "grid";
		measure_math.style.opacity = "100%";
		measure_value.style.display = "none";
		measure_value.style.opacity = "0%";
	} else if (measure_type_value == 'value') {
		measure_value.style.display = "grid";
		measure_value.style.opacity = "100%";
		measure_math.style.display = "none";
		measure_math.style.opacity = "0%";
	} else {
		measure_value.style.display = "none";
		measure_value.style.opacity = "0%";
		measure_math.style.display = "none";
		measure_math.style.opacity = "0%";
	}
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
				deleteBtn.innerHTML = '&cross;';
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
		
				errors_delete = document.getElementsByClassName('deg-mod-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('deg-mod-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}
			} else {
				const errors = document.getElementById('deg-mod-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'deg-mod-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
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
	const deletes = document.querySelectorAll('.deg-mod-xbox');
	const degs = document.getElementsByClassName('deg-mod-table-deg');
	const effs = document.getElementsByClassName('deg-mod-table-effect');
	const keys = document.getElementsByClassName('deg-mod-table-key');
	const dess = document.getElementsByClassName('deg-mod-table-desc');
	const nulls = document.getElementsByClassName('deg-mod-table-null');
	const deletesDivs = document.getElementsByClassName('deg-mod-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/degree_mod/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {
				degs[i].style.maxHeight = "0px";
				degs[i].style.padding = "0px";
				degs[i].style.marginBottom = "0px";
				effs[i].style.maxHeight = "0px";
				effs[i].style.padding = "0px";
				effs[i].style.marginBottom = "0px";
				keys[i].style.maxHeight = "0px";
				keys[i].style.padding = "0px";
				keys[i].style.marginBottom = "0px";
				dess[i].style.maxHeight = "0px";
				dess[i].style.padding = "0px";
				dess[i].style.marginBottom = "0px";
				nulls[i].style.maxHeight = "0px";
				nulls[i].style.padding = "0px";
				nulls[i].style.marginBottom = "0px";
				deletesDivs[i].style.maxHeight = "0px";
				deletesDivs[i].style.padding = "0px";
				deletesDivs[i].style.marginBottom = "0px";
			})
		}
	}
};

deg_mod_delete();