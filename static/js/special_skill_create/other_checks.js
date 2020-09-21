function other_check() {
	const other_check = document.getElementById("other_check");
	const other_entry = document.getElementById("other-entry");
	
	if (other_check.checked == true) {
		other_entry.style.display = "grid"
		if (other_entry.style.maxHeight){
			other_entry.style.maxHeight = null;
		  } else {
			other_entry.style.maxHeight = other_entry.scrollHeight + "px";
		  }
	} else {
		other_entry.style.display = "none"
	}
}