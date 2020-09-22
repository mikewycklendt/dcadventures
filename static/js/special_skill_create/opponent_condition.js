function opp_cond_check() {
	const opp_cond_check = document.getElementById("opp_cond_check");
	const opp_cond_entry = document.getElementById("opp-cond-entry");
	
	if (opp_cond_check.checked == true) {
		opp_cond_entry.style.display = "grid";
		opp_cond_entry.style.padding = "1%";
		opp_cond_entry.style.maxHeight = opp_cond_entry.scrollHeight + "px";
		opp_cond_entry.style.padding = "1%";
	} else {
		opp_cond_entry.style.maxHeight = "0px";
		opp_cond_entry.style.padding = "0px";
	}
}