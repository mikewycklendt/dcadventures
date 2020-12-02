function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	check_title(check, title, base, entry);
}

function circ_base() {
	const field = 'circ_extra';
	const field2 = 'circ_target';
	const entry = "circ-entry";

	base_two(field, field2, entry);
}

function circ_type() {
	const field = document.getElementById('circ_type');
	const value = field.options[field.selectedIndex].value;
	const ran = 'circ-range';
	const chk = 'circ-check'; 
	const entry = 'circ-entry';


	if (value == 'range') {
		show_maxheight(ran);
		hide_maxheight(chk);
	} if (value == 'check') {
		show_maxheight(chk);
		hide_maxheight(ran);
	} else {
		hide_maxheight(chk);
		hide_maxheight(ran);
	}

	if (value != 'range' && value != 'check') {
		shrink_entry(entry, chk);
	} else {
		if (value == 'range') {
			grow_entry(entry, ran);
		} else if (value == 'check') {
			grow_entry(entry, chk);
		}
	}
}