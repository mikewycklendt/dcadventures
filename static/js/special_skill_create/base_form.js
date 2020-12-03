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

function subskill_check() {
	const subskill_check = document.getElementById("subskill_check");
	const subskill = document.getElementById("subskill");
	
	if (subskill_check.checked == true) {
		subskill.style.display = "grid";
		alt_entry.style.maxHeight = other_entry.scrollHeight + "px";
	} else {
		alt_entry.style.maxHeight = "0px";
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
	const prep_field = document.getElementById('prep_type');
	let prep = prep_field.options[prep_field.selectedIndex].value;

	const prep_value = 'prep-value';
	const prep_math = 'prep-math-rank';
		
	if (prep == 'value') {
		hide_maxheight(prep_math);
		show_maxheight(prep_value);
	} else if (prep == 'math') {
		hide_maxheight(prep_value);
		show_maxheight(prep_math);
	}
	else {
		hide_maxheight(prep_value);
		hide_maxheight(prep_math);		
	}
}