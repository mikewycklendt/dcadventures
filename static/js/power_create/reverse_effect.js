function reverse_check() {
	const check = document.getElementById("reverse_check");
	const base = document.getElementById("reverse-base");
	const title = document.getElementById("reverse-title");

	if (check.checked == true) {
		base.style.opacity = "100%"
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = "0%"
		title.style.color = "#245681";
	}
}

function reverse_base() {
	const target_field = document.getElementById("reverse_target");
	const target = target_field.options[target_field.selectedIndex].value;
	const entry = document.getElementById("reverse-entry")

	if (target != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}

function reverse_check_check() {
	const check = document.getElementById("reverse_check_check");
	const field = document.getElementById("reverse-check")
	const entry = document.getElementById("reverse-entry")

	if (check.checked == true) {
		field.style.display = "grid";
		field.style.padding = "1%";
		field.style.maxHeight = field.scrollHeight + "px";
		entry.style.maxHeight = entry.scrollHeight + field.scrollHeight + "px";
		field.style.padding = "1%";
	} else {
		field.style.maxHeight = "0px";
		field.style.padding = "0px";
		entry.style.maxHeight = entry.scrollHeight - field.scrollHeight + "px";
	}
}

function reverse_time_check() {
	const check = document.getElementById("reverse_time_check");
	const field = document.getElementById("reverse-time")
	const entry = document.getElementById("reverse-entry")

	if (check.checked == true) {
		field.style.display = "grid";
		field.style.padding = "1%";
		field.style.maxHeight = field.scrollHeight + "px";
		entry.style.maxHeight = entry.scrollHeight + field.scrollHeight + "px";
		field.style.padding = "1%";
	} else {
		field.style.maxHeight = "0px";
		field.style.padding = "0px";
		
		entry.style.maxHeight = entry.scrollHeight - field.scrollHeight + "px";
	}
}

function reverse_type() {
	const type_field = document.getElementById('reverse_type');
	let type_value = type_field.options[type_field.selectedIndex].value;

	const abl = document.getElementById('reverse-ability');
	const def = document.getElementById('reverse-defense');
	const skl = document.getElementById('reverse-skill');
	const pwr = document.getElementById('reverse-power');

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

function reverse_value_type() {
	const type_field = document.getElementById("reverse_value_type");
	const type = type_field.options[type_field.selectedIndex].value;
	
	const val = document.getElementById("reverse-check-value");
	const math = document.getElementById("reverse-check-math");

	if (type == "math") {
		math.style.display = "grid";
		math.style.maxHeight = math.scrollHeight + "px";
		val.style.display = "none";
		val.style.maxHeight = "0px";
	} else if (type == "value") {
		val.style.display = "grid";
		val.style.maxHeight = val.scrollHeight + "px";
		math.style.display = "none";
		math.style.maxHeight = "0px";
	} else {
		math.style.display = "none";
		math.style.maxHeight = "0px";
		val.style.display = "none";
		val.style.maxHeight = "0px";
	}
}