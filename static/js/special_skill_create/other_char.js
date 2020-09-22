function char_check() {
	const char_check = document.getElementById("char_check");
	const char_base_form = document.getElementById("char-base-form");
	
	if (char_check.checked == true) {
		char_base_form.style.opacity = "100%";
	} else {
		char_base_form.style.opacity = "0%";
	}
}