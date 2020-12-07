const entry = 'char-entry';

function char_check() {
	const check = "char_check";
	const title = "char-title";
	const base = 'char-base';
	const entry = "char-entry";

	check_title(check, title, base, entry);
}

function char_base() {
	const field ='char_extra';
	const entry = "char-entry";

	base(field, entry)
}

function char_limited() {
	const check = 'char_limited';
	const div = 'char-limited';
	const entry = "char-entry";

	check_drop(check, div, entry);
}

function char_reduced() {
	const check = 'char_reduced';
	const div = 'char-reduced';
	const entry = "char-entry";

	check_drop(check, div, entry);
}

function char_limited_by() {
	const field = 'char_limited_by';
	const options = [{'val': 'other', 'div': 'char-other'},
					{'val': 'emotion', 'div': 'char-emotion'}]

	select_maxheight(field, options);
}

function char_emotion() {
	const field = document.getElementById('char_emotion');
	const value = field.options[field.selectedIndex].value;
	const oth = document.getElementById('char-emotion-other')

	if (value == 'other') {
		oth.style.opacity = '100%';
	} else {
		oth.style.opacity = '0%';
	}
}

function char_limbs() {
	const check = 'char_limbs';
	const div = 'char-limbs';
	const entry = 'char-entry';

	check_drop(check, div, entry)
}

function char_carry() {
	const check = 'char_carry';
	const div = 'char-carry';

	check_drop(check, div, entry);
}

function char_points() {
	const check = 'char_points';
	const div = 'char-points';

	check_drop(check, div, entry);
}

function char_appear() {
	const check = 'char_appear';
	const div = 'char-appear';

	check_drop(check, div, entry)
}

function char_points_trait_type() {
	const select = 'char_points_trait_type'
	const fill = 'char_points_trait'
	
	trait_select(select, fill);
}

function char_insub() {
	const check = 'char_insub';
	const div = 'char-insub';

	check_drop(check, div, entry);
}

function char_reduced_trait_type() {
	const select = 'char_reduced_trait_type';
	const fill = 'char_reduced_trait';

	trait_select(select, fill);
}

function char_trait_type() {
	const select = 'char_trait_type';
	const fill = 'char_trait';

	trait_select(select, fill);
}