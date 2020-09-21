function untrained_check() {
	const untrained_check = document.getElementById("untrained_check");
	const untrained_details_field = document.getElementById("untrained-details-field");
	
	if (untrained_check.checked == true) {
		untrained_details_field.style.display = "grid"
	if (untrained_check == false) {
		untrained_details_field.xtyle.display = "none"
	}
}