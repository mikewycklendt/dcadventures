function action_change_check() {
	const action_change_check = document.getElementById("action_change_check");
	const action_entry = document.getElementById("action-entry");
	
	if (action_change_check.checked == true) {
		action_entry.style.display = "grid";
		action_entry.style.padding = "1%";
		action_entry.style.maxHeight = other_entry.scrollHeight + "px";
		action_entry.style.padding = "1%";
	} else {
		action_entry.style.maxHeight = "0px";
		action_entry.style.padding = "0px";
	}
}