function resist_check() {
	const resist_check = document.getElementById("resist_check");
	const resist_target = document.getElementById("resist-target");
	
	if (resist_check.checked == true) {
		resist_target.style.opacity = "100%";
	} else {
		resist_target.style.opacity = "0%";
	}
}