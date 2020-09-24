function resist_check() {
	const resist_check = document.getElementById("resist_check");
	const resist_target = document.getElementById("resist-target");
	
	if (resist_check.checked == true) {
		resist_target.style.opacity = "100%";
	} else {
		resist_target.style.opacity = "0%";
	}
}

function resist_base() {
	const resist_target = document.getElementById("resist_target");
	resisttarget =  deg_mod_target.options[resist_target.selectedIndex].value;
	console.log(resisttarget);
	const resist_entry = document.getElementById("resist-entry");

	if (resisttarget != '') {
		resist_entry.style.display = "grid";
		resist_entry.style.padding = "1%";
		resist_entry.style.maxHeight = resist_entry.scrollHeight + "px";
		resist_entry.style.padding = "1%";
	} else {
		resist_entry.style.maxHeight = "0px";
		resist_entry.style.padding = "0px";
	}
}