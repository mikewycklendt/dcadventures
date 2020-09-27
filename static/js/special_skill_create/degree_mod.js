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
		damage.style.maxWidth = damage.scrollWidth + "px";

		
		measure.style.display = "none";
		measure.style.maxWidth = "0px";
		condition.style.display = "none";
		condition.style.maxWidth = "0px";
	} else if (deg_mod_type_value == 'measure') {
		measure.style.display = "grid";
		measure.style.maxWidth = measure.scrollWidth + "px";

		damage.style.display = "none";
		damage.style.maxWidth = "0px";
		condition.style.display = "none";
		condition.style.maxWidth = "0px";
	} else if (deg_mod_type_value == 'condition') {
		condition.style.display = "grid";
		condition.style.maxWidth = condition.scrollWidth + "px";
		damage.style.display = "none";
		damage.style.maxWidth = "0px";
		measure.style.display = "none";
		measure.style.maxWidth = "0px";
	} else {
		damage.style.display = "none";
		damage.style.maxWidth = "0px";
		measure.style.display = "none";
		measure.style.maxWidth = "0px";
		condition.style.display = "none";
		condition.style.maxWidth = "0px";
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
		damage_math.style.maxWidth = damage_math.scrollWidth + "px";
		damage.style.maxWidth = damage.scrollWidth + damage_math.scrollWidth + "px";
		damage_value.style.display = "none";
		damage_value.style.maxWidth = "0px";
	} else if (damage_type_value == 'value') {
		damage_value.style.display = "grid";
		damage_value.style.maxWidth = damage_value.scrollWidth + "px";
		damage.style.maxWidth = damage.scrollWidth + damage_value.scrollWidth + "px";
		damage_math.style.display = "none";
		damage_math.style.maxWidth = "0px";
	} else {
		damage_value.style.display = "none";
		damage_value.style.maxWidth = "0px";
		damage_math.style.display = "none";
		damage_math.style.maxWidth = "0px";
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
		measure_math.style.maxWidth = measure_math.scrollWidth + "px";
		measure.style.maxWidth = measure.scrollWidth + measure_math.scrollWidth + "px";
		measure_value.style.display = "none";
		measure_value.style.maxWidth = "0px";
	} else if (measure_type_value == 'value') {
		measure_value.style.display = "grid";
		measure_value.style.maxWidth = measure_value.scrollWidth + "px";
		measure.style.maxWidth = measure.scrollWidth + measure_value.scrollWidth + "px";
		measure_math.style.display = "none";
		measure_math.style.maxWidth = "0px";
	} else {
		measure_value.style.display = "none";
		measure_value.style.maxWidth = "0px";
		measure_math.style.display = "none";
		measure_math.style.maxWidth = "0px";
	}
}