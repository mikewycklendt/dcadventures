function resist_effect_check() {
	const resist_effect_check = document.getElementById("resist_effect_check");
	const resist_effect_entry = document.getElementById("resist-effect-entry");
	
	if (resist_effect_check.checked == true) {
		resist_effect_entry.style.display = "grid";
		resist_effect_entry.style.padding = "1%";
		resist_effect_entry.style.maxHeight = resist_effect_entry.scrollHeight + "px";
		resist_effect_entry.style.padding = "1%";
	} else {
		resist_effect_entry.style.maxHeight = "0px";
		resist_effect_entry.style.padding = "0px";
	}
}