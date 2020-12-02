function resist_check() {
	const check = "resist_check";
	const title = "resist-title";
	const base = 'resist-base';
	const entry = "resist-entry"

	check_title(check, title, base, entry);
}


function resist_base() {
	const field = 'resist_extra';
	const entry = "resist-entry";

	base(field, entry);
}
function resist_type() {
	const select = 'resist_trait_type';
	const fill = 'resist_trait';

	trait_select(select, fill);
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