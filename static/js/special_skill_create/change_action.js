function action_change_check() {
	const action_change_check = document.getElementById("action_change_check");
	const action_entry = document.getElementById("action-entry");
	const title = document.getElementById("action-title");
	
	if (action_change_check.checked == true) {
		action_entry.style.display = "grid";
		action_entry.style.padding = "1%";
		action_entry.style.maxHeight = action_entry.scrollHeight + "px";
		action_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		action_entry.style.maxHeight = "0px";
		action_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}




