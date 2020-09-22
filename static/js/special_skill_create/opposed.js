function opposed_by_check() {
	const opposed_by_check = document.getElementById("opposed_by_check");
	const opposed_by_base_form = document.getElementById("opposed-by-base-form");
	
	if (opposed_by_check.checked == true) {
		opposed_by_base_form.style.opacity = "100%";
	} else {
		opposed_by_base_form.style.opacity = "0%";
	}
}