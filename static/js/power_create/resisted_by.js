function resist_check() {
	const check = document.getElementById("resist_check");
	const entry = document.getElementById("resist-entry");
	const title = document.getElementById("resist-title");
	
	if (check.checked == true) {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}

function resist_type() {
	const type_field = document.getElementById('resist_type');
	let type_value = type_field.options[type_field.selectedIndex].value;

	const abl = document.getElementById('resist-ability');
	const def = document.getElementById('resist-defense');
	const skl = document.getElementById('resist-skill');
	const pwr = document.getElementById('resist-power');

	if (type_value == 'ability') {
		abl.style.display = "grid";
		abl.style.maxHeight = abl.scrollHeight + "px";
		def.style.display = "none";
		def.style.maxHeight = "0px";
		skl.style.display = "none";
		skl.style.maxHeight = "0px";
		pwr.style.display = "none";
		pwr.style.maxHeight = "0px";
	} else if (type_value == 'defense') {
		def.style.display = "grid";
		def.style.maxHeight = def.scrollHeight + "px";
		abl.style.display = "none";
		abl.style.maxHeight = "0px";
		skl.style.display = "none";
		skl.style.maxHeight = "0px";
		pwr.style.display = "none";
		pwr.style.maxHeight = "0px";
	} else if (type_value == 'skill') {
		skl.style.display = "grid";
		skl.style.maxHeight = skl.scrollHeight + "px";
		def.style.display = "none";
		def.style.maxHeight = "0px";
		abl.style.display = "none";
		abl.style.maxHeight = "0px";
		pwr.style.display = "none";
		pwr.style.maxHeight = "0px";
	} else if (type_value == 'power') {
		pwr.style.display = "grid";
		pwr.style.maxHeight = pwr.scrollHeight + "px";
		def.style.display = "none";
		def.style.maxHeight = "0px";
		skl.style.display = "none";
		skl.style.maxHeight = "0px";
		abl.style.display = "none";
		abl.style.maxHeight = "0px";
	} else {
		def.style.display = "none";
		def.style.maxHeight = "0px";
		skl.style.display = "none";
		skl.style.maxHeight = "0px";
		abl.style.display = "none";
		abl.style.maxHeight = "0px";
		pwr.style.display = "none";
		pwr.style.maxHeight = "0px";
	}
}