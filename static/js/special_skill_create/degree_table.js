function degree_check() {
	const degree_check = document.getElementById("degree_check");
	const degree_base_form = document.getElementById("degree-base-form");
	
	if (degree_check.checked == true) {
		degree_base_form.style.opacity = "100%";
	} else {
		degree_base_form.style.opacity = "0%";
	}
}