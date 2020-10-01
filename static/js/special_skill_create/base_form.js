function untrained_check() {
	const untrained_check = document.getElementById("untrained_check");
	const untrained_details_field = document.getElementById("untrained-details-field");
	
	if (untrained_check.checked == true) {
		untrained_details_field.style.display = "grid";
	} else {
		untrained_details_field.style.display = "none";
	}

	if (untrained_check.checked != false) {
		untrained_details_field.style.opacity = "100%";
	} else {
		untrained_details_field.style.display = "none";
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