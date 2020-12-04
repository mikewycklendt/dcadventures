function untrained_check() {
	const untrained_check = document.getElementById("untrained_check");
	const untrained_details_field = document.getElementById("untrained-details-field");
	
	if (untrained_check.checked == true) {
		untrained_details_field.style.display = "grid";
		setTimeout(function(){untrained_details_field.style.opacity = '100%'}, 10);
	} else {
		untrained_details_field.style.opacity = '0%';
		setTimeout(function(){untrained_details_field.style.display = 'none'}, 400);
	}


}

function secret_check() {
	const secret_check = document.getElementById("secret_check");
	const secret_mod = document.getElementById("secret-mod");
	
	if (secret_check.checked == true) {
		secret_mod.style.display = "grid";
		secret_mod.style.opacity = "100%";
	} else {
		secret_mod.style.opacity = "0%";
	}
}

function prep_type() {
	const prep_field = 'prep_type';
	const prep_value = 'prep-value';
	const prep_math = 'prep-math-rank';
		
	value_type_maxheight(prep_field, prep_math, prep_value);
}

function subskill_check() {
	const subskill_check = "subskill_check";
	const subskill = "subskill";
	
	check_drop(subskill_check, subskill);
}