function deg_mod_check() {
	const deg_mod_check = document.getElementById("deg_mod_check");
	const deg_mod_base_form = document.getElementById("deg-mod-base-form");
	
	if (deg_mod_check.checked == true) {
		deg_mod_base_form.style.opacity = "100%";
	} else {
		deg_mod_base_form.style.opacity = "0%";
	}
}

function deg_mod_base() {
	const deg_mod_target = document.getElementById("deg_mod_target");
	degmodtarget =  deg_mod_target.options[deg_mod_target.selectedIndex].value;
	console.log(degmodtarget);
	const deg_mod_entry = document.getElementById("deg-mod-entry");

	if (degmodtarget != '') {
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
	
	let damage = document.getElementById('deg-mod-damage');
	
	let damage_type_field = document.getElementById('deg_mod_damage_type');
	let damage_type_value = damage_type_field.options[damage_type_field.selectedIndex].value;
	
	let damage_math = document.getElementById('deg-mod-damage-math');
	let damage_value = document.getElementById('deg-mod-damage-value');
	
	let measure = document.getElementById('deg-mod-measure');

	let measure_type_field = document.getElementById('deg_mod_measure_type');
	let measure_type_value = measure_type_field.options[measure_type_field.selectedIndex].value;

	let measure_math = document.getElementById('deg-mod-measure-math');
	let measure_value = document.getElementById('deg-mod-measure-value');

	let condition = document.getElementById('deg-mod-condition');


	if (deg_mod_type_value == 'damage') {
		damage.style.display = "grid";
		damage.style.opacity = "100%"

		
		measure.style.display = "none";
		measure.style.opacity = "0%";
		condition.style.display = "none";
		condition.style.opacity = "0%";
	} else if (deg_mod_type_value == 'measure') {
		measure.style.display = "grid";
		measure.style.opacity = "100%";

		damage.style.display = "none";
		damage.style.opacity = "0%";
		condition.style.display = "none";
		condition.style.opacity = "0%";
	} else if (deg_mod_type_value == 'condition') {
		condition.style.display = "grid";
		condition.style.opacity = "100%";
		damage.style.display = "none";
		damage.style.opacity = "0%";
		measure.style.display = "none";
		measure.style.opacity = "0%";
	} else {
		damage.style.display = "none";
		damage.style.opacity = "0%";
		measure.style.display = "none";
		measure.style.opacity = "0%";
		condition.style.display = "none";
		condition.style.opacity = "0%";
	}

};

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
	const table = document.getElementById('deg-mod-table');

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
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

	if ((target != '' && deg_value != '' && type != '' && damage_type == 'math' && damage_math1 != '' && damage_math2 != '' && damage_val1 !=  '' && damage_val2 != '' && key != '' && desc != '') || (target != '' && deg_value != '' && type != '' && key != '' && desc != '' && damage_deg_val != '' && damage_type == 'value' && damage_val != '') || (target != '' && deg_value != '' && type != '' && key != '' && desc != '' && measure_type == 'value' && measure_value != '' && measure_rank != '') || (target != '' && deg_value != '' && type != '' && key != '' && desc != '' && measure_type == 'math' && measure_math != '' && measure_val1 != '' && measure_val2 != '' && measure_math_rank != '') || (target != '' && deg_value != '' && type != '' && key != '' && desc != '' && condition1 != '' && condition2 != '')) {


		const deg = document.createElement('div');
		deg.className = 'deg-mod-table-deg'
		deg.innerHTML = deg_value;
		
		if (type == 'damage') {
			if (damage_type == 'math') {
				effect = damage_math + ' ' + damage_val1 + ' ' + damage_math1 + ' ' + damage_val2 + ' ' + damage_math2;
			} else if (damage_type == 'value') {
				effect = 'degree: ' + damage_deg_val + ' damage: ' + damage_val;
			}
		} else if (type == 'measure') {
			if (measure_type == 'math') {
				effect = measure_val1 + ' ' + measure_math + ' ' + measure_val2 + ' ' + measure_math_rank;
			} else if (measure_type == 'value') {
				effect = measure_value + ' ' + measure_rank;
			}
		} else if (type == 'condition') {
			effect = 'from ' + condition1 + ' to ' + condition2;
		}

		const eff = document.createElement('div');
		eff.className = 'deg-mod-table-effect'
		eff.innerHTML = effect;
	
		const key = document.createElement('div');
		key.className = 'deg-mod-table-key'
		key.innerHTML = key;

		const desc = document.createElement('div');
		desc.className = 'deg-mod-table-desc'
		desc.innerHTML = desc;
	
		const nullify = document.createElement('div');
		nullify.className = 'deg-mod-table-null'
		nullify.innerHTML = nullify_val;

		const degmodDelete = document.createElement('div');
		degmodDelete.className = 'deg-mod-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'deg-mod-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', deg_mod_enter);
		degmodDelete.appendChild(deleteBtn);

		deg_mod_enter = deg_mod_enter + 1;
	
		table.appendChild(deg);
		table.appendChild(eff);
		table.appendChild(key);
		table.appendChild(desc);
		table.appendChild(nullify);	
		table.appendChild(degmodDelete);

		deg.style.maxHeight = deg.scrollHeight + "px";
		eff.style.maxHeight = eff.scrollHeight + "px";
		key.style.maxHeight = key.scrollHeight + "px";
		desc.style.maxHeight = desc.scrollHeight + "px";
		nullify.style.maxHeight = nullify.scrollHeight + "px";
		degmodDelete.style.maxHeight = degmodDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		deg_mod_delete()
	}
};

deg_mod_delete = function() {
	const deletes = document.querySelectorAll('.deg-mod-xbox');
	const degs = document.getElementsByClassName('deg-mod-table-deg');
	const effs = document.getElementsByClassName('deg-mod-effect');
	const keys = document.getElementsByClassName('deg-mod-table-key');
	const dess = document.getElementsByClassName('deg-mod-table-desc');
	const nulls = document.getElementsByClassName('deg-mod-table-null');
	const deletesDivs = document.getElementsByClassName('deg-mod-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
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
		}
	}
};

deg_mod_delete();