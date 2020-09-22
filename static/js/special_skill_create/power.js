function power_check() {
	const power_check = document.getElementById("power_check");
	const power_entry = document.getElementById("power-entry");
	
	if (power_check.checked == true) {
		power_entry.style.display = "grid";
		power_entry.style.padding = "1%";
		power_entry.style.maxHeight = power_entry.scrollHeight + "px";
		power_entry.style.padding = "1%";
	} else {
		power_entry.style.maxHeight = "0px";
		power_entry.style.padding = "0px";
	}
}