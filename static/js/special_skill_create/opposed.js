function opposed_by_check() {
	const opposed_by_check = document.getElementById("opposed_by_check");
	const opposed_by_base_form = document.getElementById("opposed-by-base-form");
	
	if (opposed_by_check.checked == true) {
		opposed_by_base_form.style.opacity = "100%";
	} else {
		opposed_by_base_form.style.opacity = "0%";
	}
}

function opposed_by_by() {
	opposed_by_by = document.getElementById("opposed_by_by")
	opposed_by_by_value = pre_check_type.options[opposed_by_by.selectedIndex].value;
	console.log(opposed_by_by_value)
	opposed_by_entry = document.getElementById("opposed-by-entry")

	if (opposed_by_by_value != '') {
		opposed_by_entry.style.display = "grid";
		opposed_by_entry.style.padding = "1%";
		opposed_by_entry.style.maxHeight = opposed_by_entry.scrollHeight + "px";
		opposed_by_entry.style.padding = "1%";

	} else {
		opposed_by_entry.style.maxHeight = "0px";
		opposed_by_entry.style.padding = "0px";
	}
}