function subskill_check() {
	const subskill_check = document.getElementById("subskill_check");
	const subskill = document.getElementById("subskill");
	
	if (subskill_check.checked == true) {
		subskill.style.display = "grid";
		subskill.style.padding = "1%";
		subskill.style.maxHeight = other_entry.scrollHeight + "px";
		subskill.style.padding = "1%";
	} else {
		subskill.style.maxHeight = "0px";
		subskill.style.padding = "0px";
		subskill.style.opacity = "0%;"
	}
}