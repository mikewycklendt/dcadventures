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
	const con = "resist-condition";
	const dam = "resist-damage";

	if (effect == 'condition') {
		hide_maxheight(dam);
		show_maxheight(con);
	} else if (effect == 'damage') {
		hide_maxheight(con);
		show_maxheight(dam);
	} else {
		hide_maxheight(dam);
		hide_maxheight(con);
	}
}