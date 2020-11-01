function ranks_distance() {
	const field_field = document.getElementById("ranks_distance")
	const field = field_field.options[field_field.selectedIndex].value;
	const val = document.getElementById("ranks-distance-values")
	const fac = document.getElementById("ranks-distance-factor")

	if (field == 'flat') {
		val.style.opacity = "100%";
		fac.style.opacity = "0%";
	} else if (field == 'rank') {
		val.style.opacity = "100%";
		fac.style.opacity = "100%";
	} else {
		val.style.opacity = "0%";
		fac.style.opacity = "0%";
	}
}

function ranks_ranged() {
	const check = document.getElementById("ranks_ranged");
	const div = document.getElementById("ranks-distance");

	if (check.checked == true) {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px";
	}
}