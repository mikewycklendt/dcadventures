function resist_check() {
	const check = document.getElementById("resist_check");
	const title = document.getElementById("resist-title");
	const base = document.getElementById('resist-base')
	const entry = document.getElementById("resist-entry")

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}


function resist_base() {
	const field = document.getElementById('resist_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("resist-entry")

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
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

function resist_effect() {
	const effect_field = document.getElementById("resist_eft");
	const effect = effect_field.options[effect_field.selectedIndex].value;
	const con = document.getElementById("resist-condition");
	const dam = document.getElementById("resist-damage");

	if (effect == 'condition') {
		con.style.display = "grid";
		con.style.maxHeight = con.scrollHeight + 'px';
		dam.style.display = "none";
		dam.style.maxHeight = "0px";
	} else if (effect == 'damage') {
		dam.style.display = "grid";
		dam.style.maxHeight = dam.scrollHeight + 'px';
		con.style.display = "none";
		con.style.maxHeight = "0px";
	} else {
		con.style.display = "none";
		con.style.maxHeight = "0px";
		dam.style.display = "none";
		dam.style.maxHeight = "0px";
	}
}