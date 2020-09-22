function levels_check() {
	const levels_check = document.getElementById("levels_check");
	const levels_base_form = document.getElementById("levels-base-form");
	
	if (levels_check.checked == true) {
		levels_base_form.style.opacity = "100%";
	} else {
		levels_base_form.style.opacity = "0%";
	}
}