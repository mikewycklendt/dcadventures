function sense_sense() {
	const field_field  = document.getElementById("sense_sense");
	const field = field_field.options[field_field.selectedIndex].value;
	const vis = document.getElementById("sense-visual");
	const aud = document.getElementById("sense-auditory");
	const olf = document.getElementById("sense-olfactory");
	const tac = document.getElementById("sense-tactile");
	const rad = document.getElementById("sense-radio");
	const men = document.getElementById("sense-mental");
	const spe = document.getElementById("sense-special");

	if (field == 6) {
		vis.style.display = "block";
		vis.style.maxHeight = vis.scrollHeight + "px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	} else if (field == 7) {
		aud.style.display = "block";
		aud.style.maxHeight = aud.scrollHeight + "px";
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	} else if (field == 8) {
		olf.style.display = "block";
		olf.style.maxHeight = olf.scrollHeight + "px";
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	} else if (field == 9) {
		tac.style.display = "block";
		tac.style.maxHeight = tac.scrollHeight + "px";
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	} else if (field == 10) {
		rad.style.display = "block";
		rad.style.maxHeight = rad.scrollHeight + "px";
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	} else if (field == 11) {
		men.style.display = "block";
		men.style.maxHeight = men.scrollHeight + "px";
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px"
	} else if (field == 12) {
		spe.style.display = "block";
		spe.style.maxHeight = spe.scrollHeight + "px"
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
	} else {
		vis.style.display = "none";
		vis.style.maxHeight = "0px";
		aud.style.display = "none";
		aud.style.maxHeight = "0px";
		olf.style.display = "none";
		olf.style.maxHeight = "0px";
		tac.style.display = "none";
		tac.style.maxHeight = "0px";
		rad.style.display = "none";
		rad.style.maxHeight = "0px";
		men.style.display = "none";
		men.style.maxHeight = "0px";
		spe.style.display = "none";
		spe.style.maxHeight = "0px";
	}
}

function sense_skill() {
	const field_field = document.getElementById("sense_skill");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("sense-skill-req")

	if (field != '') {
		div.style.opacity = "100%"	
	} else {
		div.style.opacity = "0%";
	}
}

function sense_type() {
	const field_field = document.getElementById("sense_type");
	const field = field_field.options[field_field.selectedIndex].value;

	const hei = document.getElementById("sense-height");
	const res = document.getElementById("sense-resist");

	if (field == 'height') {
		hei.style.display = "grid";
		hei.style.maxHeight = hei.scrollHeight + "px";
		res.style.display = "none";
		res.style.maxHeight = "0px";
	} else if (field == 'resist') {
		res.style.display = "grid";
		res.style.maxHeight = res.scrollHeight + "px";
		hei.style.display = "none";
		hei.style.maxHeight = "0px";
	} else {
		hei.style.display = "none";
		hei.style.maxHeight = "0px";
		res.style.display = "none";
		res.style.maxHeight = "0px";
	}
}

function sense_height_trait() {
	const field_field = document.getElementById("sense_height_trait");
	const field = field_field.options[field_field.selectedIndex].value;
	const abi = document.getElementById("sense-height-ability")
	const ski = document.getElementById("sense-height-skill")
	const bon = document.getElementById("sense-height-bonus")
	const def = document.getElementById("sense-height-defense")

	if (field == 'ability') {
		abi.style.display = "block";
		abi.style.maxHeight = abi.scrollHeight + "px";		
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'skill') {
		ski.style.display = "block";
		ski.style.maxHeight = ski.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'bonus') {
		bon.style.display = "block";
		bon.style.maxHeight = bon.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'defense') {
		def.style.display = "block";
		def.style.maxHeight = def.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
	} else {
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	}
}

function sense_resist_trait() {
	const field_field = document.getElementById("sense_resist_trait");
	const field = field_field.options[field_field.selectedIndex].value;
	const abi = document.getElementById("sense-resist-ability")
	const ski = document.getElementById("sense-resist-skill")
	const bon = document.getElementById("sense-resist-bonus")
	const pow = document.getElementById("sense-resist-power")
	const def = document.getElementById("sense-resist-defense")

	if (field == 'ability') {
		abi.style.display = "block";
		abi.style.maxHeight = abi.scrollHeight + "px";		
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		pow.style.display =  "none";
		pow.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'skill') {
		ski.style.display = "block";
		ski.style.maxHeight = ski.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		pow.style.display =  "none";
		pow.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'bonus') {
		bon.style.display = "block";
		bon.style.maxHeight = bon.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px"
		pow.style.display =  "none";
		pow.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'power') {
		pow.style.display = "block";
		pow.style.maxHeight = pow.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	} else if (field == 'defense') {
		def.style.display = "block";
		def.style.maxHeight = def.scrollHeight + "px";
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		pow.style.display =  "none";
		pow.style.maxHeight = "0px";
	} else {
		abi.style.display =  "none";
		abi.style.maxHeight = "0px";
		ski.style.display =  "none";
		ski.style.maxHeight = "0px";
		bon.style.display =  "none";
		bon.style.maxHeight = "0px";
		pow.style.display =  "none";
		pow.style.maxHeight = "0px";
		def.style.display =  "none";
		def.style.maxHeight = "0px";
	}

}

function sense_power_req() {
	const check = document.getElementById("sense_height_power_req");
	const div = document.getElementById("sense-height-ensense");

	if (check.checked == true) {
		div.style.opacity = "100%";
	} else {
		div.style.opacity = "0%";
	}
}

function sense_resist_immune() {
	const check = document.getElementById("sense_resist_immune")
	const div = document.getElementById("sense-resist-immune-perm")

	if (check.checked == true) {
		div.style.opacity = "100%";
	} else {
		div.style.opacity = "0%";
	}
}

function sense_dark() {
	const check = document.getElementById("sense_dark")
	const lig = document.getElementById("sense-lighting");
	const hea = document.getElementById("sense-lighting-head");

	if (check.checked == true) {
		lig.style.opacity = "100%"
		hea.style.opacity = "100%"
	} else {
		lig.style.opacity = "0%"
		hea.style.opacity = "0%"
	}
}

function sense_time_set() {
	const field_field = document.getElementById("sense_time_set");
	const field = field_field.options[field_field.selectedIndex].value
	const val = document.getElementById("sense-time-value");
	const ski = document.getElementById("sense-time-skill");
	const bon = document.getElementById("sense-time-bonus");

	if (field == 'value') {
		val.style.display = "grid";
		val.style.maxHeight = val.scrollHeight + "px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";	
	} else if (field == 'skill') {
		ski.style.display = "grid";
		ski.style.maxHeight = ski.scrollHeight + "px";		
		val.style.display = "none";
		val.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";
	} else if (field == 'bonus') {
		bon.style.display = "grid";
		bon.style.maxHeight = bon.scrollHeight + "px";		
		val.style.display = "none";
		val.style.maxHeight = "0px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";	
	} else {
		val.style.display = "none";
		val.style.maxHeight = "0px";
		ski.style.display = "none";
		ski.style.maxHeight = "0px";
		bon.style.display = "none";
		bon.style.maxHeight = "0px";
	}
}

function sense_time() {
	const check = document.getElementById("sense_time");
	const div = document.getElementById("sense-time");

	if (check.checked == true) {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px";
	}
}

function sense_ranged() {
	const check = document.getElementById("sense_ranged");
	const div = document.getElementById("sense-distance");

	if (check.checked == true) {
		div.style.display = "grid";
		div.style.maxHeight = div.scrollHeight + "px";
	} else {
		div.style.maxHeight = "0px";
	}
}

function sense_distance() {
	const field_field = document.getElementById("sense_distance")
	const field = field_field.options[field_field.selectedIndex].value;
	const val = document.getElementById("sense-distance-values")
	const fac = document.getElementById("sense-distance-factor")

	if (field == 'flat') {
		val.style.opacity = "100%";
		fac.style.opacity = "0%";
	} else if (field == 'rank') {
		val.style.opacity = "100%";
		fac.style.opacity = "100%";
	} else {
		val.style.opacity = "0%";
		fac.style.opacity = "0%";
	}
}