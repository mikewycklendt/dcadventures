function pre_check_check() {
	const pre_check_check = document.getElementById("pre_check_check");
	const pre_check_header_type = document.getElementById("pre-check-header-type");
	
	if (pre_check_check.checked == true) {
		pre_check_header_type.style.opacity = "100%";
	} else {
		pre_check_header_type.style.opacity = "0%";
	}
}