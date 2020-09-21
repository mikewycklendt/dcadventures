function untrained_check() {
	const untrained_check = document.getElementById("untrained_check");
	const untrained_details_field = document.getElementById("untrained-details-field");
	
	if (untrained_check.checked == true) {
		untrained_details_field.style.display = "grid"
	} else {
		untrained_details_field.style.display = "none"
	}
}

function subskill_check() {
	const subskill_check = document.getElementById("subskill_check");
	const subskill = document.getElementById("subskill");
	
	if (subskill_check.checked == true) {
		subskill.style.display = "grid"
	} else {
		subskill.style.display = "none"
	}
}