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