function deg_mod_check() {
	const deg_mod_check = document.getElementById("deg_mod_check");
	const deg_mod_base_form = document.getElementById("deg-mod-base-form");
	
	if (deg_mod_check.checked == true) {
		deg_mod_base_form.style.opacity = "100%";
	} else {
		deg_mod_base_form.style.opacity = "0%";
	}
}